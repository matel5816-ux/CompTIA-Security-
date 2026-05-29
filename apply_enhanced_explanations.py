#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apply enhanced explanations to the question bank.
Preserves manual corrections (13 hand-verified questions).
"""
import json
import re

# Load enhanced explanations
with open("enhanced_explanations.json", "r", encoding="utf-8") as f:
    enhanced = json.load(f)

# Load manual corrections
try:
    from translation_corrections import CORRECTIONS
    manual_corrected = set(CORRECTIONS.keys())
except ImportError:
    manual_corrected = set()

# Load bank
with open("integrated_question_bank.json", "r", encoding="utf-8") as f:
    bank = json.load(f)

# Apply enhanced explanations
updated = 0
preserved_manual = 0
for q in bank:
    num = q["num"]
    num_str = str(num)
    if num in manual_corrected:
        preserved_manual += 1
        continue
    if num_str in enhanced:
        q["zh"]["explain"] = enhanced[num_str]
        updated += 1

print(f"Updated {updated} explanations")
print(f"Preserved {preserved_manual} manual corrections")

# Save bank
with open("integrated_question_bank.json", "w", encoding="utf-8") as f:
    json.dump(bank, f, ensure_ascii=False, indent=2)

# Regenerate index.html
print("\nRegenerating index.html...")

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

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

pattern = r'const questionPool\s*=\s*\[.*?\n\s*\];'
match = re.search(pattern, html, re.DOTALL)
if match:
    new_html = html[:match.start()] + js_code + html[match.end():]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"index.html updated: {len(new_html):,} chars")
else:
    print("ERROR: questionPool not found")
