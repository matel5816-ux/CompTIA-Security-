#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final build: integrate all 12 batches of translations with PDF questions
and inject into index.html with EN+ZH bound structure.
"""
import json
import re

# Load PDF questions (canonical English source)
with open("pdf_questions_clean.json", "r", encoding="utf-8") as f:
    pdf_qs = json.load(f)

# Load all 12 translation batches
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

all_translations = {**B1, **B2, **B3, **B4, **B5, **B6, **B7, **B8, **B9, **B10, **B11, **B12}
print(f"Loaded {len(all_translations)} translations across 12 batches")

# Build integrated bank
integrated = []
quality_count = 0
placeholder_count = 0
sim_count = 0

for num_str in sorted(pdf_qs.keys(), key=lambda x: int(x)):
    num = int(num_str)
    pdf_q = pdf_qs[num_str]

    en_q = pdf_q["q"]
    en_opts = pdf_q["options"]
    answer = pdf_q["answer"]

    if num in all_translations:
        zh = all_translations[num].copy()
        quality_count += 1
        # Ensure opts count matches
        while len(zh["opts"]) < len(en_opts):
            zh["opts"].append("(翻譯待確認)")
        zh["opts"] = zh["opts"][:len(en_opts)]
    elif "HOTSPOT" in en_q.upper() or "SIMULATION" in en_q.upper() or "INSTRUCTIONS" in en_q.upper() or len(en_opts) == 0:
        zh = {
            "q": f"[第 {num} 題：原 PDF 為互動模擬題型 (HOTSPOT/SIMULATION)，需在實作平台練習]",
            "opts": ["—"] * max(1, len(en_opts)),
            "explain": "本題為 PDF 中的互動式模擬題，需在實際題庫平台拖拉設定才能完成。建議跳過或參考相關章節練習。"
        }
        sim_count += 1
    else:
        zh = {
            "q": f"【第 {num} 題 - 中文翻譯待補充】英文摘要：{en_q[:100]}",
            "opts": [f"(翻譯待補) {opt[:50]}" for opt in en_opts],
            "explain": f"本題中文翻譯尚待補充。正確答案：{pdf_q['answer_str']}"
        }
        placeholder_count += 1

    integrated.append({
        "num": num,
        "q": en_q,
        "options": en_opts,
        "answer": answer,
        "zh": zh
    })

print(f"\nFinal bank:")
print(f"  Total questions: {len(integrated)}")
print(f"  Quality translations: {quality_count}")
print(f"  Placeholder translations: {placeholder_count}")
print(f"  Simulation markers: {sim_count}")
print(f"  Coverage: {quality_count*100//len(integrated)}%")

# Save integrated bank
with open("integrated_question_bank.json", "w", encoding="utf-8") as f:
    json.dump(integrated, f, ensure_ascii=False, indent=2)

# Escape strings that would break the embedding HTML <script> block.
# When JSON / JS string literals contain literal "</script>", the HTML parser
# closes the script tag prematurely. The standard fix is to break the
# closing tag pattern: "</script>" -> "<\/script>". JavaScript treats "\/" as
# "/", but the HTML parser no longer sees a script-close.
def html_safe(s):
    if not isinstance(s, str):
        return s
    # Replace ALL HTML-sensitive sequences inside JS string literals
    return (s
            .replace("</script>", "<\\/script>")
            .replace("</SCRIPT>", "<\\/SCRIPT>")
            .replace("<!--", "<\\!--")
            .replace("-->", "--\\>"))

def sanitize_zh(zh):
    return {
        "q": html_safe(zh.get("q", "")),
        "opts": [html_safe(o) for o in zh.get("opts", [])],
        "explain": html_safe(zh.get("explain", ""))
    }

# Generate JavaScript questionPool
js_lines = ["        const questionPool = ["]
for q in integrated:
    en_q_safe = html_safe(q["q"])
    en_q_escaped = en_q_safe.replace("\\", "\\\\").replace('"', '\\"')
    opts_safe = [html_safe(opt) for opt in q["options"]]
    options_js = "[" + ", ".join(f'"{opt.replace(chr(92), chr(92)+chr(92)).replace(chr(34), chr(92)+chr(34))}"' for opt in opts_safe) + "]"
    answer_js = "[" + ", ".join(str(a) for a in q["answer"]) + "]"
    zh_safe = sanitize_zh(q["zh"])
    zh_js = json.dumps(zh_safe, ensure_ascii=False, separators=(',', ': '))
    line = f'            {{ q: "{en_q_escaped}", options: {options_js}, answer: {answer_js}, zh: {zh_js} }},'
    js_lines.append(line)
js_lines.append("        ];")

js_code = "\n".join(js_lines)

# Final safety: scan generated JS for any remaining </script>
if "</script>" in js_code:
    print("WARNING: </script> still present in generated JS - this will break HTML!")
    js_code = js_code.replace("</script>", "<\\/script>")
    print("  Applied emergency fix.")
with open("new_question_pool.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print(f"\nJS code length: {len(js_code):,} chars")

# Inject into index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

pattern = r'const questionPool\s*=\s*\[.*?\n\s*\];'
match = re.search(pattern, html, re.DOTALL)
if match:
    new_html = html[:match.start()] + js_code + html[match.end():]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"\nindex.html updated: {len(new_html):,} chars")

    new_q_count = new_html.count('{ q: "')
    zh_count = new_html.count(", zh:")
    print(f"  Question objects: {new_q_count}")
    print(f"  zh fields: {zh_count}")
else:
    print("ERROR: questionPool not found in index.html")
