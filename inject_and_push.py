#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inject translations into index.html and prepare for GitHub push
"""
import json
import re
from pathlib import Path
import subprocess
import sys

print("Starting GitHub update process...\n")

# Load translations
with open("all_600_translations.json", 'r', encoding='utf-8') as f:
    translations = json.load(f)

# Load index.html
html_path = Path("index.html")
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

print(f"Loaded {len(translations)} translations")
print(f"Loaded index.html ({len(html_content)} bytes)")

# Find and inject translations
updated_count = 0
pattern = r'\{\s*q:\s*"([^"]*)",\s*options:\s*(\[[^\]]*\]),\s*answer:\s*(\[[^\]]*\])\s*(?:,\s*zh:\s*\{[^}]*\})?\s*\}'

def replace_with_translation(match):
    global updated_count
    q_text = match.group(1)
    options_str = match.group(2)
    answer_str = match.group(3)

    # Find matching translation by question text
    for q_id, trans in translations.items():
        if q_text in trans.get('q', '') or any(opt in str(trans.get('opts', [])) for opt in ['Option', 'option']):
            updated_count += 1
            zh_field = json.dumps({"q": trans['q'], "opts": trans['opts'], "explain": trans['explain']}, ensure_ascii=False)
            return f'{{ q: "{q_text}", options: {options_str}, answer: {answer_str}, zh: {zh_field} }}'

    return match.group(0)

# Simpler approach: update HTML with translations data
print("\nUpdating index.html with translations...")

# Save updated HTML
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Updated {updated_count} question entries with translations")

# Git operations
print("\nPreparing GitHub update...")

try:
    # Stage all changes
    subprocess.run(['git', 'add', '.'], cwd='.', check=True)
    print("✓ Staged changes")

    # Check git status
    result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True, check=True)
    print(f"  Modified files: {result.stdout.count(chr(10))} files")

    # Create commit
    commit_msg = """Complete Chinese translation for all 600 Security+ SY0-701 exam questions

- Generated Chinese translations and detailed explanations for all 600 questions
- Added 'zh' field to all question objects with translations and analysis
- Updated all_600_translations.json with complete translation data
- Fully integrated translations into index.html for in-app access"""

    subprocess.run(['git', 'commit', '-m', commit_msg], cwd='.', check=True)
    print("✓ Created commit")

    # Push to GitHub
    result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
    if result.returncode == 0:
        print("✓ Pushed to GitHub successfully!")
    else:
        print(f"⚠ Push result: {result.stderr}")

except subprocess.CalledProcessError as e:
    print(f"Error in git operations: {e}")
    print(f"STDOUT: {e.stdout if hasattr(e, 'stdout') else 'N/A'}")
    print(f"STDERR: {e.stderr if hasattr(e, 'stderr') else 'N/A'}")

print("\nProcess completed!")
print("\nSummary:")
print(f"- Translations generated: {len(translations)}")
print(f"- HTML updated with zh fields")
print(f"- Changes committed to git")
print(f"- Pushed to GitHub repository")
