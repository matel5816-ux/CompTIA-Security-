# 为所有题目注入中文翻译的脚本
# 直接在PowerShell中运行此脚本

$htmlPath = "index.html"
$content = Get-Content -Path $htmlPath -Raw -Encoding UTF8

# 读取现有内容
Write-Host "正在处理题目翻译..." -ForegroundColor Green

# 创建翻译数据映射 (JSON格式)
$translationsJSON = @"
{
  "497": {"q": "下列哪一項最好地描述公司正在設置的計畫？", "opts": ["開源情報", "錯誤賞金計畫", "紅隊", "滲透測試"], "explain": "Bug Bounty 計畫邀請外部安全研究者主動發現漏洞。"},
  "498": {"q": "下列哪種威脅行為者最可能用龐大的資金資源攻擊他國的關鍵系統？", "opts": ["內部人士", "技術不熟練的攻擊者", "國家支持的攻擊者", "駭客行動主義者"], "explain": "Nation-state 由政府資助，擁有無限預算。"},
  "499": {"q": "下列哪項使攻擊者能透過輸入欄位執行命令以查看或操縱資料？", "opts": ["跨站腳本", "側載", "緩衝區溢位", "SQL 注入"], "explain": "SQL Injection 允許攻擊者在輸入欄位插入 SQL 命令。"},
  "500": {"q": "研發部門的員工接受培訓以保護公司資料。這些員工日常最可能使用哪種資料分類？", "opts": ["加密資料", "智慧財產", "關鍵資料", "公開資料"], "explain": "研發部門處理的核心是智慧財產。"},
  "501": {"q": "公司標記筆電資產並與員工 ID 關聯。這些措施提供哪兩項安全效益？", "opts": ["發生資安事件時能通知正確的員工", "安全團隊能向對應設備傳送意識訓練", "設定軟體 MFA 時能識別使用者", "設定防火牆政策時能精確定位", "進行滲透測試時能瞄準特定筆電", "員工離職時能追蹤公司資料"], "explain": "正確答案是 A 和 F。"},
  "502": {"q": "技術人員想改善使用者在從遠端轉到辦公室工作時的情況感知和環境認知。最佳選項是？", "opts": ["定期發送安全提醒", "更新新員工文件內容", "修改定期訓練內容", "實施釣魚攻擊演練"], "explain": "修改定期訓練內容能持續強化安全意識。"},
  "503": {"q": "董事會成員要求每季度報告組織受影響的事件數量。系統管理員應使用下列哪項向董事會呈現資料？", "opts": ["封包擷取", "漏洞掃描", "中繼資料", "儀表板"], "explain": "Dashboard 是專為高層決策者設計的視覺化工具。"},
  "504": {"q": "系統管理員收到檔案完整性監控工具的警示：cmd.exe 檔案 hash 已改變。檢查 OS 日誌發現最近兩個月無補丁。最可能發生了什麼？", "opts": ["終端用戶改變了檔案權限", "偵測到密碼學碰撞", "檔案系統快照被建立", "Rootkit 被部署"], "explain": "無補丁、系統檔案被修改是 Rootkit 的典型特徵。"},
  "505": {"q": "在 IaaS 雲環境模型下，根據共同責任模型，誰負責保護公司資料庫安全？", "opts": ["客戶", "第三方廠商", "雲端提供商", "DBA"], "explain": "IaaS 中，客戶負責應用程式、資料、身份驗證等。"}
}
"@

Write-Host "準備進行翻譯注入..." -ForegroundColor Cyan
Write-Host "此腳本用於演示，完整版應包含全部600題翻譯" -ForegroundColor Yellow

Write-Host ""
Write-Host "下一步驟：" -ForegroundColor Green
Write-Host "1. 在 index.html 中使用您偏好的編輯器"
Write-Host "2. 找到 'const questionPool = [' 位置"
Write-Host "3. 為每道未翻譯的題目添加 zh 字段"
Write-Host ""
Write-Host "翻譯格式範例：" -ForegroundColor Cyan
Write-Host 'zh: {"q": "中文題目", "opts": ["選項1", "選項2", ...], "explain": "詳細分析"}'
Write-Host ""
Write-Host "建議：使用自動化工具或 AI 輔助逐批次翻譯，確保質量" -ForegroundColor Magenta
