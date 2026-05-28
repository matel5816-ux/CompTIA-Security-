#!/usr/bin/env python3
"""
Generate translations for Security+ exam questions.
This script uses my translation suggestions to build the complete JSON.
"""
import json
from pathlib import Path

# Load extracted questions
with open("extracted_questions.json", 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Load existing translations
existing_file = Path("all_600_translations.json")
existing = {}
if existing_file.exists():
    try:
        with open(existing_file, 'r', encoding='utf-8') as f:
            existing = json.loads(f.read())
    except:
        pass

print(f"Existing translations: {len(existing)}")
print(f"Total questions: {len(questions)}")
print(f"Need to translate: {len(questions) - len(existing)}")

# Show which questions need translation
need_translation = [i+1 for i in range(len(questions)) if str(i+1) not in existing]
if need_translation:
    print(f"\nQuestions needing translation: {need_translation[:20]}...")
    if len(need_translation) > 20:
        print(f"... and {len(need_translation)-20} more")

# Show a sample of existing translation
if existing:
    first_key = list(existing.keys())[0]
    print(f"\nSample of existing translation (Q{first_key}):")
    sample = existing[first_key]
    print(f"  Q: {sample['q'][:60]}...")
    print(f"  Opts: {sample['opts'][0][:40]}...")
    print(f"  Explain: {sample['explain'][:60]}...")

print("\n✓ Ready for batch translation")
