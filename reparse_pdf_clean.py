#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Robust PDF parser for SY0-701 questions.
Fixes the bug where multi-line question text was captured as option[0].
"""
import PyPDF2
import re
import json

with open("NEW-SY0-701-611Q.pdf", 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    all_text = ""
    for i in range(len(reader.pages)):
        all_text += reader.pages[i].extract_text() + "\n"

def clean_text(text):
    """Clean OCR artifacts from PDF text"""
    # Remove URLs
    text = re.sub(r'https?://\S+', '', text)
    # Remove encoding artifacts (��)
    text = text.replace('\x00', '')
    text = re.sub(r'[�]', '', text)
    # Smart quotes
    text = text.replace('“', '"').replace('”', '"')
    text = text.replace('‘', "'").replace('’', "'")
    text = text.replace('–', '-').replace('—', '-')
    # Replace strange spacing characters
    text = re.sub(r'[ ​‌‍]', ' ', text)
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Split into question blocks
parts = re.split(r'(Topic \d+ Question #\d+)', all_text)

questions = {}
parse_errors = []

for i in range(1, len(parts), 2):
    marker = parts[i]
    content = parts[i+1] if i+1 < len(parts) else ""

    num_match = re.search(r'#(\d+)', marker)
    if not num_match:
        continue
    q_num = int(num_match.group(1))

    # Find "Correct Answer:" - this delimits the option section
    answer_match = re.search(r'Correct Answer:\s*([A-Z, ]+)', content)
    if not answer_match:
        # Maybe HOTSPOT/SIMULATION
        parse_errors.append({"num": q_num, "reason": "no_correct_answer"})
        continue

    answer_str = answer_match.group(1).strip()
    answer_letters = [c for c in answer_str if c.isalpha()]

    before_answer = content[:answer_match.start()]

    # Find option markers - they are on their own line/position starting with single letter + period
    # Pattern: at start of line OR after newline: "A. ", "B. ", etc.
    # Use a more careful pattern: letter followed by period followed by space, where letter is the only character before period on its position

    # Best approach: find each "X. " where X is single letter A-Z preceded by newline or start
    # Handle BOTH "A. text" AND "A.text" formats (no space after period)
    option_pattern = re.compile(r'(?:^|\n)\s*([A-Z])\.\s*(.+?)(?=(?:\n\s*[A-Z]\.\s*)|$)', re.DOTALL)

    options_found = []
    for m in option_pattern.finditer(before_answer):
        letter = m.group(1)
        text = clean_text(m.group(2))
        # Remove "Most Voted" suffix
        text = re.sub(r'\s*Most Voted\s*$', '', text)
        text = re.sub(r'\s*Most Voted\b', '', text)
        options_found.append((letter, text))

    # Validate: should have sequential A, B, C, ...
    expected_letters = [chr(ord('A') + i) for i in range(len(options_found))]
    actual_letters = [opt[0] for opt in options_found]

    if actual_letters != expected_letters:
        # Try to fix: filter to keep only sequential ones
        valid_options = []
        next_expected = 'A'
        for letter, text in options_found:
            if letter == next_expected:
                valid_options.append((letter, text))
                next_expected = chr(ord(next_expected) + 1)
        options_found = valid_options

    if not options_found:
        parse_errors.append({"num": q_num, "reason": "no_options"})
        continue

    # Question text = everything before the first option
    # Find position of first option marker in original content
    first_option_match = re.search(r'(?:^|\n)\s*A\.\s*', before_answer)
    if first_option_match:
        question_text = clean_text(before_answer[:first_option_match.start()])
    else:
        question_text = clean_text(before_answer)

    # Convert answer letters to indices
    answer_indices = []
    for letter in answer_letters:
        idx = ord(letter) - ord('A')
        if idx < len(options_found):
            answer_indices.append(idx)

    questions[q_num] = {
        "num": q_num,
        "q": question_text,
        "options": [opt[1] for opt in options_found],
        "letters": [opt[0] for opt in options_found],
        "answer": answer_indices,
        "answer_str": answer_str
    }

print(f"Parsed {len(questions)} questions cleanly")
print(f"Parse errors: {len(parse_errors)}")
if parse_errors:
    print(f"Error question numbers: {[e['num'] for e in parse_errors[:10]]}")

# Verify specific cases
for n in [49, 271, 53, 168]:
    if n in questions:
        q = questions[n]
        print(f"\n--- Q{n} (clean) ---")
        print(f"Q: {q['q'][:120]}")
        print(f"Options ({len(q['options'])}):")
        for i, opt in enumerate(q['options']):
            print(f"  {chr(65+i)}. {opt[:80]}")
        print(f"Answer: {q['answer_str']} (index {q['answer']})")

# Save
sorted_data = dict(sorted(questions.items(), key=lambda x: int(x[0])))
with open("pdf_questions_clean.json", "w", encoding="utf-8") as f:
    json.dump({str(k): v for k, v in sorted_data.items()}, f, ensure_ascii=False, indent=2)

print(f"\nSaved {len(questions)} clean questions to pdf_questions_clean.json")
