#!/usr/bin/env python3
import json
import re
from pathlib import Path
import time
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic()

# Read index.html and extract questions
html_path = Path(__file__).parent / "index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Extract all questions from HTML
pattern = r'\{ q: "([^"]+)", options: \[((?:[^,\]]*,?)*)\], answer: \[([^\]]+)\]'
matches = re.finditer(pattern, html_content)

questions = []
for match in matches:
    q_text = match.group(1)
    options_str = match.group(2)
    answer_str = match.group(3)

    # Parse options
    options = re.findall(r'"([^"]*)"', options_str)

    # Parse answers
    answers = [int(x.strip()) for x in answer_str.split(',')]

    questions.append({
        'q': q_text,
        'options': options,
        'answer': answers
    })

print(f"Found {len(questions)} questions to translate")

# Load existing translations to avoid retranslating
existing_file = Path(__file__).parent / "all_600_translations.json"
existing = {}
if existing_file.exists():
    try:
        with open(existing_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Fix encoding issues
            existing = json.loads(content)
    except:
        existing = {}

print(f"Found {len(existing)} existing translations")

# Translation system prompt
system_prompt = """You are a professional translator and CompTIA Security+ exam expert.
Your task is to translate exam questions from English to Traditional Chinese (繁體中文).

For each question, you must provide:
1. A clear, accurate Chinese translation of the question
2. Chinese translations of all options with technical terms properly translated
3. A detailed explanation (explanation) analyzing:
   - Why the correct answer is right
   - Why each incorrect option is wrong
   - Key security concepts related to the question

Format your response as a JSON object like this:
{
  "q": "中文題目翻譯",
  "opts": ["選項1翻譯", "選項2翻譯", "選項3翻譯", "選項4翻譯"],
  "explain": "詳細的觀念解析..."
}

Important:
- Use Traditional Chinese terminology (繁體中文)
- Keep technical terms accurate (e.g., "Phishing" → "釣魚攻擊", "MFA" → "多因素驗證")
- Make explanations clear and educational
- Each explanation should be 2-4 sentences explaining the concept and why the answer is correct
"""

# Store conversation for multi-turn
conversation_history = []

def translate_batch(start_idx, end_idx):
    """Translate a batch of questions"""
    batch_questions = questions[start_idx:end_idx]
    batch_to_translate = []
    batch_indices = []

    for i, q in enumerate(batch_questions):
        q_id = start_idx + i + 1
        if str(q_id) not in existing:
            batch_to_translate.append(q)
            batch_indices.append(q_id)

    if not batch_to_translate:
        print(f"Batch {start_idx}-{end_idx}: All already translated")
        return

    print(f"Translating questions {batch_indices[0]}-{batch_indices[-1]}...")

    # Prepare batch prompt
    batch_text = "Please translate the following exam questions:\n\n"
    for idx, q in enumerate(batch_to_translate):
        q_num = batch_indices[idx]
        batch_text += f"{q_num}. Question: {q['q']}\n"
        batch_text += f"Options:\n"
        for i, opt in enumerate(q['options']):
            batch_text += f"  {chr(65+i)}: {opt}\n"
        batch_text += f"Correct answer(s): {', '.join([chr(65+a) for a in q['answer']])}\n"
        batch_text += "\n"

    batch_text += f"\nFor EACH question, respond with ONLY the JSON object (no markdown, no explanations). Separate multiple questions with a blank line.\nReturn exactly {len(batch_to_translate)} JSON objects, one per line."

    # Add to conversation
    conversation_history.append({
        "role": "user",
        "content": batch_text
    })

    # Get translation from Claude
    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=8000,
        system=system_prompt,
        messages=conversation_history
    )

    assistant_message = response.content[0].text
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    # Parse responses
    json_blocks = re.findall(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', assistant_message)

    for idx, json_str in enumerate(json_blocks):
        if idx < len(batch_indices):
            try:
                translation = json.loads(json_str)
                existing[str(batch_indices[idx])] = translation
                print(f"  ✓ Question {batch_indices[idx]} translated")
            except json.JSONDecodeError as e:
                print(f"  ✗ Failed to parse JSON for question {batch_indices[idx]}: {e}")

    # Save progress
    with open(existing_file, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    # Rate limiting
    time.sleep(2)

# Translate in batches of 10 questions
batch_size = 10
total_batches = (len(questions) + batch_size - 1) // batch_size

for batch_num in range(total_batches):
    start = batch_num * batch_size
    end = min((batch_num + 1) * batch_size, len(questions))

    print(f"\nBatch {batch_num + 1}/{total_batches}")
    translate_batch(start, end)

print(f"\n✓ Translation complete! Total translated: {len(existing)}/{len(questions)}")
print(f"Saved to: {existing_file}")
