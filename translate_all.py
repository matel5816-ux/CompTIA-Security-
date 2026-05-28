#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量翻譯所有 600 題並內嵌到 HTML
"""

import json
import re
import time
import requests
from pathlib import Path

# ============= 設定 =============
API_KEY = ""  # 會在執行時從環境或代碼中填入
GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent"
HTML_PATH = Path("index.html")
BATCH_SIZE = 20  # 每批翻譯 20 題

def extract_questions_from_html():
    """從 HTML 中提取所有題目"""
    html = HTML_PATH.read_text(encoding='utf-8')

    # 找到 questionPool 的起始位置
    start = html.find('const questionPool = [')
    if start == -1:
        print("❌ 找不到 questionPool")
        return None

    # 找到陣列開始
    bracket_start = html.find('[', start)
    bracket_count = 0
    bracket_end = -1

    for i in range(bracket_start, len(html)):
        if html[i] == '[':
            bracket_count += 1
        elif html[i] == ']':
            bracket_count -= 1
            if bracket_count == 0:
                bracket_end = i + 1
                break

    json_str = html[bracket_start:bracket_end]

    # 使用 eval 評估 JavaScript 陣列
    try:
        # 先轉換為有效的 JSON（處理 JavaScript 特性）
        # 移除末尾的逗號等
        json_str = re.sub(r',\s*}', '}', json_str)
        json_str = re.sub(r',\s*]', ']', json_str)

        questions = json.loads(json_str)
        print(f"✅ 成功提取 {len(questions)} 題")
        return questions
    except json.JSONDecodeError as e:
        print(f"❌ JSON 解析失敗: {e}")
        return None

def translate_batch(questions, start_idx, end_idx):
    """批量翻譯一組題目"""
    batch = questions[start_idx:end_idx]
    print(f"\n📝 正在翻譯第 {start_idx + 1}-{min(end_idx, len(questions))} 題...")

    # 組合翻譯請求
    batch_text = ""
    for i, q in enumerate(batch, start=start_idx + 1):
        if 'zh' in q and q['zh']:
            continue  # 跳過已翻譯

        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        opts_str = '\n'.join([f"{letters[j]}. {opt}" for j, opt in enumerate(q['options'])])
        answer_letters = ', '.join([letters[i] for i in q['answer']])

        batch_text += f"""
【第 {i} 題】
題目: {q['q']}
選項:
{opts_str}
正確答案: {answer_letters}
---"""

    prompt = f"""你是 CompTIA Security+ 認證專家。請將以下題目翻譯為繁體中文，並對每題提供詳細解析。

{batch_text}

對每題，請按照以下 JSON 格式輸出（不要包含 markdown 代碼塊）：

[
  {{
    "qIndex": 1,
    "q": "中文題目翻譯",
    "opts": ["選項A中文", "選項B中文", "選項C中文", "選項D中文"],
    "explain": "詳細解析：說明正確答案為何正確，以及為何其他選項錯誤的深度分析"
  }},
  ...
]"""

    try:
        response = requests.post(
            f"{GEMINI_ENDPOINT}?key={API_KEY}",
            headers={'Content-Type': 'application/json'},
            json={
                'contents': [{'role': 'user', 'parts': [{'text': prompt}]}],
                'systemInstruction': {'parts': [{'text': '只輸出有效的 JSON，不要包含任何其他文字。'}]}
            },
            timeout=60
        )

        if response.status_code != 200:
            print(f"❌ API 錯誤 {response.status_code}: {response.text}")
            return None

        data = response.json()
        result_text = data['candidates'][0]['content']['parts'][0]['text']

        # 嘗試解析 JSON
        result_text = result_text.strip()
        if result_text.startswith('```json'):
            result_text = result_text[7:-3]
        elif result_text.startswith('```'):
            result_text = result_text[3:-3]

        translations = json.loads(result_text)
        print(f"✅ 第 {start_idx + 1}-{min(end_idx, len(questions))} 題翻譯完成")
        return translations

    except Exception as e:
        print(f"❌ 翻譯失敗: {e}")
        return None

def inject_translations(questions, all_translations):
    """將翻譯注入題目"""
    for trans_batch in all_translations:
        if not trans_batch:
            continue

        for trans in trans_batch:
            q_idx = trans.get('qIndex', 0) - 1
            if 0 <= q_idx < len(questions):
                questions[q_idx]['zh'] = {
                    'q': trans['q'],
                    'opts': trans['opts'],
                    'explain': trans['explain']
                }

    return questions

def save_questions_to_html(questions):
    """將翻譯後的題目保存回 HTML"""
    html = HTML_PATH.read_text(encoding='utf-8')

    # 轉換為 JavaScript 格式
    js_array = "["
    for i, q in enumerate(questions):
        zh_part = ""
        if 'zh' in q and q['zh']:
            zh_str = json.dumps(q['zh'], ensure_ascii=False)
            zh_part = f", zh: {zh_str}"

        opts_str = ', '.join([f'"{opt}"' for opt in q['options']])
        ans_str = ', '.join([str(a) for a in q['answer']])

        q_str = f'{{"q": "{q["q"]}", options: ["{opts_str}"], answer: [{ans_str}]{zh_part}}}'
        js_array += q_str
        if i < len(questions) - 1:
            js_array += ",\n            "
    js_array += "\n        ];"

    # 替換 HTML 中的 questionPool
    pattern = r'const questionPool = \[[^\]]*\];'
    new_html = re.sub(pattern, f'const questionPool = {js_array}', html, flags=re.DOTALL)

    HTML_PATH.write_text(new_html, encoding='utf-8')
    print(f"✅ 已更新 HTML")

def main():
    print("🚀 開始批量翻譯所有題目...\n")

    # 提取題目
    questions = extract_questions_from_html()
    if not questions:
        return

    # 檢查已翻譯的題目
    untranslated = [i for i, q in enumerate(questions) if 'zh' not in q or not q['zh']]
    print(f"📊 已翻譯: {len(questions) - len(untranslated)} 題")
    print(f"📊 未翻譯: {len(untranslated)} 題")

    if not untranslated:
        print("✅ 所有題目已翻譯！")
        return

    # 批量翻譯
    all_translations = []
    for i in range(0, len(questions), BATCH_SIZE):
        trans = translate_batch(questions, i, min(i + BATCH_SIZE, len(questions)))
        if trans:
            all_translations.append(trans)
        time.sleep(2)  # 避免 API 限流

    # 注入翻譯
    print("\n💾 正在注入翻譯到 HTML...")
    questions = inject_translations(questions, all_translations)
    save_questions_to_html(questions)

    print("\n✅ 翻譯完成！")

if __name__ == '__main__':
    if not API_KEY:
        print("⚠️  未設定 API_KEY，請設定環境變數或在代碼中填入")
        print("💡 您也可以直接在 index.html 中執行 JavaScript 來調用 Gemini API")
    else:
        main()
