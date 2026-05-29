#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final build v2: integrate clean PDF + auto-translated options + my batch translations
- English from PDF (clean parser)
- Chinese options from option_translator.py (bound to PDF exactly)
- Chinese question + explain from my batch files (where available)
"""
import json
import re

# Load clean PDF data
with open("pdf_questions_clean.json", "r", encoding="utf-8") as f:
    pdf_qs = json.load(f)

# Load translated options (bound to PDF)
with open("translated_options.json", "r", encoding="utf-8") as f:
    trans_opts = json.load(f)

# Load my batch translations (for question text and explanation)
from translations_batch_1 import TRANSLATIONS as B1
from translations_batch_2 import TRANSLATIONS as B2
from translations_batch_3 import TRANSLATIONS as B3
from translations_batch_4 import TRANSLATIONS as B4
from translations_batch_5 import TRANSLATIONS as B5
from translations_batch_6 import TRANSLATIONS as B6
from translations_batch_7 import TRANSLATIONS as B7
from translations_batch_8 import TRANSLATIONS as B8
from translations_batch_9 import TRANSLATIONS as B9
from translations_batch_10 import TRANSLATIONS as B10
from translations_batch_11 import TRANSLATIONS as B11
from translations_batch_12 import TRANSLATIONS as B12

batch_trans = {**B1, **B2, **B3, **B4, **B5, **B6, **B7, **B8, **B9, **B10, **B11, **B12}

# Apply verified corrections to questions whose batch translations were wrong topics
try:
    from translation_corrections import CORRECTIONS
    for num, fix in CORRECTIONS.items():
        batch_trans[num] = fix
    print(f"Applied {len(CORRECTIONS)} translation corrections")
except ImportError:
    pass

print(f"PDF questions: {len(pdf_qs)}")
print(f"Translated options: {len(trans_opts)}")
print(f"Batch translations (for q/explain): {len(batch_trans)}")

# Build integrated bank
integrated = []
for num_str in sorted(pdf_qs.keys(), key=lambda x: int(x)):
    num = int(num_str)
    pdf_q = pdf_qs[num_str]

    en_q = pdf_q["q"]
    en_opts = pdf_q["options"]
    answer = pdf_q["answer"]

    # Get translated options (correctly bound to PDF)
    zh_opts = trans_opts.get(num_str, [])
    # Ensure count matches PDF
    while len(zh_opts) < len(en_opts):
        zh_opts.append(f"(選項 {chr(65+len(zh_opts))})")
    zh_opts = zh_opts[:len(en_opts)]

    # Get question text and explanation from batches (if available)
    if num in batch_trans:
        zh_q = batch_trans[num].get("q", "")
        zh_explain = batch_trans[num].get("explain", "")
    else:
        zh_q = f"【第 {num} 題】{en_q[:60]}..."
        zh_explain = f"正確答案：{pdf_q['answer_str']}。本題詳細解析待補充。"

    # Extract vocabulary from question text and options
    try:
        from vocabulary import extract_vocabulary
        vocab_source = en_q + ' ' + ' '.join(en_opts)
        vocab_list = extract_vocabulary(vocab_source)
    except ImportError:
        vocab_list = []

    integrated.append({
        "num": num,
        "q": en_q,
        "options": en_opts,
        "answer": answer,
        "zh": {
            "q": zh_q,
            "opts": zh_opts,
            "explain": zh_explain,
            "vocab": vocab_list
        }
    })

print(f"\nIntegrated bank: {len(integrated)} questions")

# Save canonical bank
with open("integrated_question_bank.json", "w", encoding="utf-8") as f:
    json.dump(integrated, f, ensure_ascii=False, indent=2)

# HTML-safe escape (prevent </script> from breaking parser)
def html_safe(s):
    if not isinstance(s, str):
        return s
    return (s
            .replace("</script>", "<\\/script>")
            .replace("</SCRIPT>", "<\\/SCRIPT>")
            .replace("<!--", "<\\!--")
            .replace("-->", "--\\>"))

# Generate JavaScript questionPool
js_lines = ["        const questionPool = ["]
for q in integrated:
    en_q_safe = html_safe(q["q"])
    en_q_escaped = en_q_safe.replace("\\", "\\\\").replace('"', '\\"')
    opts_safe = [html_safe(opt) for opt in q["options"]]
    options_js = "[" + ", ".join(f'"{opt.replace(chr(92), chr(92)+chr(92)).replace(chr(34), chr(92)+chr(34))}"' for opt in opts_safe) + "]"
    answer_js = "[" + ", ".join(str(a) for a in q["answer"]) + "]"

    zh_safe = {
        "q": html_safe(q["zh"]["q"]),
        "opts": [html_safe(o) for o in q["zh"]["opts"]],
        "explain": html_safe(q["zh"]["explain"])
    }
    zh_js = json.dumps(zh_safe, ensure_ascii=False, separators=(',', ': '))
    line = f'            {{ q: "{en_q_escaped}", options: {options_js}, answer: {answer_js}, zh: {zh_js} }},'
    js_lines.append(line)
js_lines.append("        ];")

js_code = "\n".join(js_lines)

# Final safety check
if "</script>" in js_code:
    print("WARNING: emergency fix applied")
    js_code = js_code.replace("</script>", "<\\/script>")

# Inject into index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

pattern = r'const questionPool\s*=\s*\[.*?\n\s*\];'
match = re.search(pattern, html, re.DOTALL)
if match:
    new_html = html[:match.start()] + js_code + html[match.end():]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)

    new_q_count = new_html.count('{ q: "')
    print(f"\nindex.html updated: {len(new_html):,} chars")
    print(f"  Question objects: {new_q_count}")
    print(f"  zh fields: {new_html.count(', zh:')}")

    # Verify counts match
    if new_q_count == len(integrated):
        print(f"  ✓ Count match: {new_q_count}")
    else:
        print(f"  ✗ MISMATCH: expected {len(integrated)}, got {new_q_count}")
else:
    print("ERROR: questionPool pattern not found in index.html")
