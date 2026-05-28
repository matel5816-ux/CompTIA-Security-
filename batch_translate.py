#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import time
import re
from pathlib import Path

# 讀取 index.html
html_path = Path("index.html")
html_content = html_path.read_text(encoding='utf-8')

# 提取 questionPool 開始到結束的 JSON
# 查找 const questionPool = [
start_idx = html_content.find('const questionPool = [')
if start_idx == -1:
    print("❌ 找不到 questionPool")
    exit(1)

# 找到陣列開始
array_start = html_content.find('[', start_idx)
# 需要找到陣列結束
bracket_count = 0
array_end = -1
for i in range(array_start, len(html_content)):
    if html_content[i] == '[':
        bracket_count += 1
    elif html_content[i] == ']':
        bracket_count -= 1
        if bracket_count == 0:
            array_end = i + 1
            break

questions_json_str = html_content[array_start:array_end]
print(f"✅ 提取的 JSON 長度: {len(questions_json_str)}")

# 嘗試解析 JSON
try:
    questions = json.loads(questions_json_str)
    print(f"✅ 成功解析 {len(questions)} 題")
except json.JSONDecodeError as e:
    # JSON 可能包含 JavaScript 物件，需要清理
    # 嘗試用正則表達式提取每題
    question_pattern = r'\{\s*q:\s*"([^"]*)".*?answer:\s*\[([^\]]*)\].*?(?:zh:\s*\{[^}]*\})?'
    matches = re.findall(question_pattern, questions_json_str, re.DOTALL)
    print(f"⚠️  無法直接解析 JSON，嘗試正則解析: 找到 {len(matches)} 題")

# 替代方案：使用正規運算式分割
# 查詢已翻譯的題目數量
zh_count = html_content.count('"zh":')
print(f"📊 已翻譯題目: {zh_count} 題")
print(f"📊 需翻譯題目: {max(0, 600 - zh_count)} 題")

if zh_count >= 600:
    print("✅ 所有題目已完成翻譯！")
    exit(0)

# 提取單題的正規表達式（簡化版）
single_q_pattern = r'\{\s*q:\s*"([^"]+)".*?options:\s*\[(.*?)\],\s*answer:\s*\[([^\]]*)\](?:,\s*zh:\s*\{[^}]*\})?'

print("\n⏳ 正在掃描題目...")
