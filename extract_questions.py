#!/usr/bin/env python3
import json
import re
from pathlib import Path

# Read index.html
html_path = Path("index.html")
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find the questions array
start_idx = html_content.find('const questions = [')
if start_idx == -1:
    # Try alternate format
    start_idx = html_content.find('questions = [')
    if start_idx == -1:
        print("Could not find questions array")
        exit(1)

# Extract up to the closing bracket
bracket_count = 0
found_start = False
end_idx = start_idx

for i in range(start_idx, len(html_content)):
    if html_content[i] == '[':
        bracket_count += 1
        found_start = True
    elif html_content[i] == ']' and found_start:
        bracket_count -= 1
        if bracket_count == 0:
            end_idx = i + 1
            break

# Extract the array content
array_content = html_content[start_idx:end_idx]

# Now parse each question object
pattern = r'\{\s*q:\s*"([^"]+)",\s*options:\s*\[([^\]]*)\],\s*answer:\s*\[([^\]]*)\]'

questions = []
for match in re.finditer(pattern, array_content):
    q_text = match.group(1)
    options_str = match.group(2)
    answer_str = match.group(3)

    # Parse options - they are quoted strings separated by commas
    options = re.findall(r'"([^"]*)"', options_str)

    # Parse answers
    answers = [int(x.strip()) for x in answer_str.split(',')]

    questions.append({
        'q': q_text,
        'options': options,
        'answer': answers
    })

print(f"Extracted {len(questions)} questions")

# Save to JSON for review
output_file = Path("extracted_questions.json")
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Saved to {output_file}")

# Print first 3 questions as sample
print("\nFirst 3 questions:")
for i, q in enumerate(questions[:3]):
    print(f"\n{i+1}. {q['q']}")
    for j, opt in enumerate(q['options']):
        print(f"   {chr(65+j)}: {opt}")
    print(f"   Answer: {', '.join([chr(65+a) for a in q['answer']])}")
