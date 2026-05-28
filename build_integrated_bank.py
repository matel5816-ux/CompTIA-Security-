#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build integrated question bank:
- English content from PDF (canonical source)
- Chinese translation BOUND to each English question (no drift possible)
- Q1-150 have quality translations
- Q151-606 have placeholder marker bound to English topic
"""
import json
import re

# Load PDF questions (canonical English source)
with open("pdf_questions_clean.json", "r", encoding="utf-8") as f:
    pdf_qs = json.load(f)

# Load translation batches
from translations_batch_1 import TRANSLATIONS as B1
from translations_batch_2 import TRANSLATIONS as B2
from translations_batch_3 import TRANSLATIONS as B3

all_translations = {**B1, **B2, **B3}
print(f"Loaded {len(all_translations)} quality translations")

# Extract topic keywords from English question for placeholder
def extract_topic(en_q):
    """Extract a short topic descriptor from English question"""
    # Find key security terms
    keywords = re.findall(r'\b(MFA|VPN|SIEM|SSO|RBAC|MDM|DLP|WAF|EDR|IDS|IPS|SOC|DMZ|PKI|TLS|SSL|AES|RSA|HSM|TPM|FDE|SASE|CASB|MITRE|ATT&CK|RTO|RPO|MTBF|ALE|ARO|SLE|SLA|SOW|MOU|NDA|GDPR|HIPAA|PCI|SOX|ISO|NIST|firewall|encryption|phishing|ransomware|malware|backup|certificate|hash|salt|token|kerberos|oauth|saml|ldap|biometric|jailbreak|honeypot|sandbox|zero.trust|VLAN|DHCP|DNS|HTTPS|HTTP|FTP|SSH|RDP|SMB)\b', en_q, re.IGNORECASE)
    return ", ".join(set(keywords[:5]))

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

    # Get Chinese translation - bound to this question
    if num in all_translations:
        zh = all_translations[num]
        quality_count += 1
        # Make sure opts count matches
        if len(zh["opts"]) != len(en_opts):
            # Pad with placeholder if mismatch
            while len(zh["opts"]) < len(en_opts):
                zh["opts"].append("(翻譯待確認)")
            zh["opts"] = zh["opts"][:len(en_opts)]
    elif "HOTSPOT" in en_q.upper() or "SIMULATION" in en_q.upper() or "INSTRUCTIONS" in en_q.upper() or len(en_opts) == 0:
        # Simulation/HOTSPOT type
        zh = {
            "q": f"[第 {num} 題：原 PDF 為互動模擬題型 (HOTSPOT/SIMULATION)，需在實作平台練習]",
            "opts": ["—"] * max(1, len(en_opts)),
            "explain": "此題為 PDF 中的互動式模擬題（HOTSPOT/SIMULATION），需在實際題庫平台拖拉設定才能完成。建議跳過或參考相關章節練習。"
        }
        sim_count += 1
    else:
        # Placeholder - bound to English content
        topic = extract_topic(en_q)
        zh = {
            "q": f"【第 {num} 題 - 中文翻譯待補充】英文摘要：{en_q[:100]}{'...' if len(en_q) > 100 else ''}",
            "opts": [f"選項 {chr(65+i)}（原文：{opt[:40]}...）" if len(opt) > 40 else f"選項 {chr(65+i)}（原文：{opt}）" for i, opt in enumerate(en_opts)],
            "explain": f"此題中文翻譯尚待補充。主題關鍵字：{topic if topic else '（請參考英文題目）'}。正確答案：{pdf_q['answer_str']}。"
        }
        placeholder_count += 1

    # Bound object
    integrated.append({
        "num": num,
        "q": en_q,
        "options": en_opts,
        "answer": answer,
        "zh": zh
    })

print(f"\nIntegrated bank built:")
print(f"  Total questions: {len(integrated)}")
print(f"  Quality Chinese translations: {quality_count}")
print(f"  Placeholder translations: {placeholder_count}")
print(f"  Simulation/HOTSPOT markers: {sim_count}")

# Save integrated bank
with open("integrated_question_bank.json", "w", encoding="utf-8") as f:
    json.dump(integrated, f, ensure_ascii=False, indent=2)

print(f"\nSaved to integrated_question_bank.json")

# Generate JavaScript questionPool array
print("\nGenerating JavaScript questionPool...")
js_lines = ["        const questionPool = ["]
for q in integrated:
    # Convert to compact JS object
    en_q_escaped = q["q"].replace("\\", "\\\\").replace('"', '\\"')
    options_js = "[" + ", ".join(f'"{opt.replace(chr(92), chr(92)+chr(92)).replace(chr(34), chr(92)+chr(34))}"' for opt in q["options"]) + "]"
    answer_js = "[" + ", ".join(str(a) for a in q["answer"]) + "]"
    zh_js = json.dumps(q["zh"], ensure_ascii=False, separators=(',', ': '))

    line = f'            {{ q: "{en_q_escaped}", options: {options_js}, answer: {answer_js}, zh: {zh_js} }},'
    js_lines.append(line)
js_lines.append("        ];")

js_code = "\n".join(js_lines)
with open("new_question_pool.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print(f"JS code length: {len(js_code):,} chars")
print(f"Saved to new_question_pool.js")
print(f"\nReady to inject into index.html")
