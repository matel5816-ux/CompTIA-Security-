#!/usr/bin/env python3
# 为所有600题生成翻译数据
import json

# 预定义的完整翻译（题目1-30已有，31-600需要系统化生成）
translations = {}

# 题目1-20的完整翻译已在文件中

# 为题目21-600生成结构化翻译框架
# 每题包含：中文题目、选项翻译、详细分析

for i in range(21, 601):
    translations[str(i)] = {
        "q": f"[题目{i}中文翻译待补充]",
        "opts": [f"选项A", f"选项B", f"选项C", f"选项D"],
        "explain": f"题目{i}的详细分析待补充"
    }

# 保存为JSON
with open("all_translations_framework.json", "w", encoding="utf-8") as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"✅ 已创建包含{len(translations)}题的翻译框架")

