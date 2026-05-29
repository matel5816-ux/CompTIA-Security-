#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apply Google-quality translations from cache to the question bank.
- Replace zh.q with google-translated version (where available)
- Keep zh.opts (already auto-translated and bound to PDF)
- Keep zh.explain (manual + auto-generated)
- Keep zh.vocab (extracted from English source)
- Honor manual corrections in translation_corrections.py (those override Google)
"""
import json
import re
import os

# Load Google translations
with open("google_translated_questions.json", "r", encoding="utf-8") as f:
    google_trans = json.load(f)

print(f"Google translations available: {len(google_trans)}")

# Load current bank
with open("integrated_question_bank.json", "r", encoding="utf-8") as f:
    bank = json.load(f)

# Load manual corrections (these override Google for verified-correct content)
try:
    from translation_corrections import CORRECTIONS
    print(f"Manual corrections (override Google): {len(CORRECTIONS)}")
except ImportError:
    CORRECTIONS = {}

updated = 0
skipped_manual = 0
not_in_google = 0

for q in bank:
    num = q["num"]
    num_str = str(num)

    # Manual corrections take priority
    if num in CORRECTIONS:
        # Already applied via rebuild
        skipped_manual += 1
        continue

    # Use Google translation if available
    if num_str in google_trans and google_trans[num_str].get("zh"):
        q["zh"]["q"] = google_trans[num_str]["zh"]
        updated += 1
    else:
        not_in_google += 1

print(f"\nUpdated with Google translation: {updated}")
print(f"Kept manual correction: {skipped_manual}")
print(f"Not in Google cache (kept batch translation): {not_in_google}")

# Save updated bank
with open("integrated_question_bank.json", "w", encoding="utf-8") as f:
    json.dump(bank, f, ensure_ascii=False, indent=2)

# Regenerate index.html
print("\nRegenerating index.html with Google-quality translations...")

def html_safe(s):
    if not isinstance(s, str):
        return s
    return (s.replace("</script>", "<\\/script>")
              .replace("</SCRIPT>", "<\\/SCRIPT>")
              .replace("<!--", "<\\!--")
              .replace("-->", "--\\>"))

js_lines = ["        const questionPool = ["]
for q in bank:
    en_q_safe = html_safe(q["q"])
    en_q_escaped = en_q_safe.replace("\\", "\\\\").replace('"', '\\"')
    opts_safe = [html_safe(opt) for opt in q["options"]]
    options_js = "[" + ", ".join(
        f'"{opt.replace(chr(92), chr(92)+chr(92)).replace(chr(34), chr(92)+chr(34))}"'
        for opt in opts_safe
    ) + "]"
    answer_js = "[" + ", ".join(str(a) for a in q["answer"]) + "]"
    zh_safe = {
        "q": html_safe(q["zh"]["q"]),
        "opts": [html_safe(o) for o in q["zh"]["opts"]],
        "explain": html_safe(q["zh"]["explain"]),
        "vocab": q["zh"].get("vocab", [])
    }
    zh_js = json.dumps(zh_safe, ensure_ascii=False, separators=(',', ': '))
    line = f'            {{ q: "{en_q_escaped}", options: {options_js}, answer: {answer_js}, zh: {zh_js} }},'
    js_lines.append(line)
js_lines.append("        ];")
js_code = "\n".join(js_lines)

# Inject into index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

pattern = r'const questionPool\s*=\s*\[.*?\n\s*\];'
match = re.search(pattern, html, re.DOTALL)
if match:
    new_html = html[:match.start()] + js_code + html[match.end():]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"index.html updated: {len(new_html):,} chars")
    print(f"  Question objects: {new_html.count(chr(123) + ' q: ')}")
else:
    print("ERROR: questionPool not found")
