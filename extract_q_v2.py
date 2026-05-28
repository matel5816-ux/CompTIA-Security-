#!/usr/bin/env python3
import json
import re
from pathlib import Path

# Read index.html
with open("index.html", 'r', encoding='utf-8') as f:
    content = f.read()

# More flexible pattern to capture questions
# Pattern: { q: "...", options: [...], answer: [...] }
pattern = r'\{\s*q:\s*"(.+?)(?<!\\)",\s*options:\s*\[((?:[^[\]]*|\[[^\]]*\])*)\],\s*answer:\s*\[(.*?)\]'

questions = []
for match in re.finditer(pattern, content, re.DOTALL):
    q_text = match.group(1)
    options_str = match.group(2)
    answer_str = match.group(3)

    # Parse options more carefully
    options = []
    for m in re.finditer(r'"([^"]*)"', options_str):
        options.append(m.group(1))

    # Parse answers
    answers = []
    for a in answer_str.split(','):
        a = a.strip()
        if a.isdigit():
            answers.append(int(a))

    if q_text and options and answers:
        questions.append({
            'q': q_text.strip(),
            'options': options,
            'answer': answers
        })

print(f"Extracted {len(questions)} questions")

# Save
with open("extracted_questions.json", 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

# Sample
for i in range(min(3, len(questions))):
    q = questions[i]
    print(f"\nQ{i+1}: {q['q'][:80]}...")
    print(f"  Options: {len(q['options'])}, Answer: {q['answer']}")
