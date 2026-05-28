// 運行此腳本於瀏覽器控制台，可提取所有未翻譯的題目

const untranslated = [];

// 複製 questionPool 到控制台後運行此函數
function findUntranslated() {
    let count = 0;
    questionPool.forEach((q, idx) => {
        if (!q.zh || !q.zh.q) {
            untranslated.push({
                index: idx + 1,
                question: q.q,
                options: q.options,
                answer: q.answer,
                answerLetters: q.answer.map(i => String.fromCharCode(65 + i)).join(', ')
            });
            count++;
        }
    });
    console.log(`找到 ${count} 題未翻譯的題目`);
    return untranslated;
}

// 取得第一個未翻譯的題目
function getFirstUntranslated() {
    const first = untranslated.find(q => !q.translated);
    if (!first) {
        console.log('✅ 所有題目已翻譯！');
        return null;
    }
    console.log(`\n📌 第 ${first.index} 題`);
    console.log(`題目: ${first.question}`);
    console.log(`選項:`);
    first.options.forEach((opt, i) => {
        console.log(`  ${String.fromCharCode(65 + i)}. ${opt}`);
    });
    console.log(`正確答案: ${first.answerLetters}`);
    return first;
}

// 複製翻譯範本
function copyTemplateToClipboard() {
    const template = `zh: {
  "q": "中文題目翻譯",
  "opts": [
    "選項A中文翻譯",
    "選項B中文翻譯",
    "選項C中文翻譯",
    "選項D中文翻譯"
  ],
  "explain": "詳細的觀念解析："
}`;
    navigator.clipboard.writeText(template);
    console.log('✅ 範本已複製到剪貼板');
}

// 使用說明
console.log(`
📚 未翻譯題目提取工具

1️⃣  執行: findUntranslated()
    取得所有未翻譯的題目清單

2️⃣  執行: getFirstUntranslated()
    查看第一個未翻譯的題目詳情

3️⃣  執行: copyTemplateToClipboard()
    複製翻譯範本到剪貼板

4️⃣  手動將翻譯粘貼到 index.html 對應位置

5️⃣  保存後刷新頁面測試
`);
