// 全部600题目的中文翻译和分析数据 (第497-600题)
const fullTranslationData = {
  497: {"q": "下列哪一項最好地描述公司正在設置的計畫？", "opts": ["開源情報 (OSINT) - 公開資訊蒐集", "錯誤賞金計畫 (Bug bounty) - 招募安全研究者", "紅隊 (Red team) - 內部測試隊伍", "滲透測試 (Penetration testing) - 一次性測試"], "explain": "Bug Bounty 計畫邀請外部安全研究者主動發現漏洞，並根據漏洞嚴重程度給予報酬。Red team 是內部組織；開源情報是情報蒐集方法；滲透測試是一次性聘僱服務。"},
  498: {"q": "下列哪種威脅行為者最可能用龐大的資金資源攻擊他國的關鍵系統？", "opts": ["內部人士 (Insider)", "技術不熟練的攻擊者 (Unskilled attacker)", "國家支持的攻擊者 (Nation-state)", "駭客行動主義者 (Hacktivist)"], "explain": "Nation-state (民族國家) 由政府資助，擁有無限預算、專業技術人員和先進工具，能夠針對他國進行大規模持續性攻擊。其他類型的攻擊者資源或動機都不夠充分。"},
  499: {"q": "下列哪項使攻擊者能透過輸入欄位執行命令以查看或操縱資料？", "opts": ["跨站腳本 (XSS)", "側載 (Side loading)", "緩衝區溢位 (Buffer overflow)", "SQL 注入 (SQL injection)"], "explain": "SQL Injection 允許攻擊者在輸入欄位插入 SQL 命令，繞過應用邏輯直接操縱資料庫。例如在登入欄輸入 ' OR '1'='1 可以未授權存取資料。"},
  500: {"q": "研發部門的員工接受培訓以保護公司資料。這些員工日常最可能使用哪種資料分類？", "opts": ["加密資料 (Encrypted)", "智慧財產 (Intellectual property)", "關鍵資料 (Critical)", "公開資料 (Public)"], "explain": "研發部門處理的核心是技術創新、產品設計、研究成果等智慧財產 (IP)，這是公司的競爭優勢和資產，必須嚴格保護。"},
  501: {"q": "公司標記筆電資產並與員工 ID 關聯。這些措施提供哪兩項安全效益？", "opts": ["發生資安事件時能通知正確的員工", "安全團隊能向對應設備傳送意識訓練", "設定軟體 MFA 時能識別使用者", "設定防火牆政策時能精確定位", "進行滲透測試時能瞄準特定筆電", "員工離職時能追蹤公司資料"], "explain": "正確答案是 A 和 F：(A) 資產與員工綁定後出現事件可立即通知相關人；(F) 離職時能確認員工之前使用的筆電上的公司資料。"},
  502: {"q": "技術人員想改善使用者在從遠端轉到辦公室工作時的情況感知和環境認知。最佳選項是？", "opts": ["定期發送安全提醒", "更新新員工文件內容", "修改定期訓練內容", "實施釣魚攻擊演練"], "explain": "修改定期訓練內容能持續強化安全意識，特別適合「轉變工作環境」這類情境變化。新員工文件只針對入職；定期提醒無法深入教育；釣魚演練是測試而非教育。"},
  503: {"q": "董事會成員要求每季度報告組織受影響的事件數量。系統管理員應使用下列哪項向董事會呈現資料？", "opts": ["封包擷取 (Packet captures)", "漏洞掃描 (Vulnerability scans)", "中繼資料 (Metadata)", "儀表板 (Dashboard)"], "explain": "Dashboard (儀表板) 是專為高層決策者設計的視覺化工具，能以圖表、KPI、趨勢等方式清楚呈現關鍵指標。"},
  504: {"q": "系統管理員收到檔案完整性監控工具的警示：cmd.exe 檔案 hash 已改變。檢查 OS 日誌發現最近兩個月無補丁。最可能發生了什麼？", "opts": ["終端用戶改變了檔案權限", "偵測到密碼學碰撞", "檔案系統快照被建立", "Rootkit 被部署"], "explain": "無補丁、系統檔案被修改卻未觸發正常更新機制，這是 Rootkit 的典型特徵。Rootkit 在核心層駐留，偽裝系統變化。"},
  505: {"q": "在 IaaS 雲環境模型下，根據共同責任模型，誰負責保護公司資料庫安全？", "opts": ["客戶 (Client)", "第三方廠商 (Third-party vendor)", "雲端提供商 (Cloud provider)", "DBA"], "explain": "IaaS 中，客戶 (租戶) 負責應用程式、資料、身份驗證等。雲端提供商只負責基礎設施 (伺服器、網路、儲存設備)。"},
  506: {"q": "安全公司客戶要求提供概述專案、成本和完成期限的文件。公司應提供下列哪份文件？", "opts": ["主服務協議 (MSA)", "服務水準協議 (SLA)", "業務夥伴協議 (BPA)", "工作說明書 (SOW)"], "explain": "SOW (Statement of Work) 詳述專案內容、交付物、時程表、成本和責任分工。"},
  507: {"q": "滲透測試報告發現 Web 應用表單欄位存在跨站腳本 (XSS) 漏洞。分析師應建議開發者實施下列哪項應用安全技術？", "opts": ["安全 Cookie (Secure cookies)", "版本控制 (Version control)", "輸入驗證 (Input validation)", "代碼簽章 (Code signing)"], "explain": "Input Validation (輸入驗證) 是防止 XSS 的首要防線，驗證和淨化使用者輸入，移除或編碼危險字元。"},
  508: {"q": "設計高可用性網路時應考慮哪兩項？", "opts": ["復原容易度 (Ease of recovery)", "修補能力 (Ability to patch)", "物理隔離 (Physical isolation)", "回應能力 (Responsiveness)", "攻擊面 (Attack surface)", "可擴展驗證 (Extensible authentication)"], "explain": "答案是 A 和 D：快速復原是高可用性核心；快速回應用戶請求確保服務不中斷。"},
  509: {"q": "技術人員需要對生產系統套用高優先級補丁。首先應採取下列哪個步驟？", "opts": ["將系統隔離 (Air gap)", "移動系統到不同網段", "建立變更控制請求 (Change control request)", "對系統套用補丁"], "explain": "變更控制是任何生產環境修改的必須第一步，確保備份、評估風險、定義回滾計畫。"},
  510: {"q": "根本原因分析應在事件回應的哪個階段進行，其目的是什麼？", "opts": ["蒐集調查的 IoC (Indicators of Compromise)", "發現受影響的系統", "清除網路上所有惡意軟體蹤跡", "防止未來發生相同事件"], "explain": "根本原因分析的目標是找出「為什麼會發生」而非「發生了什麼」，以實施長期修正措施。"},
  511: {"q": "大型銀行未通過內部 PCI DSS 合規評估，最可能的結果是？", "opts": ["罰款 (Fines)", "稽核發現 (Audit findings)", "制裁 (Sanctions)", "聲譽損害 (Reputation damage)"], "explain": "未通過合規評估首先產生「稽核發現」，文件記錄不合規項目。罰款是洩露後才會發生。"},
  512: {"q": "公司在規劃業務連續性策略時，需要決定在發生中斷時維持業務所需的員工數量。最佳描述此步驟的是？", "opts": ["容量規劃 (Capacity planning)", "冗餘 (Redundancy)", "地理分散 (Geographic dispersion)", "桌上演習 (Tabletop exercise)"], "explain": "Capacity Planning (容量規劃) 評估維持營運所需的資源、人員、技術等最低容量。"},
  513: {"q": "公司想確保在 SaaS 應用中起草的敏感文件無法被高風險國家的個人存取。最有效的方式是？", "opts": ["資料遮罩 (Data masking)", "加密 (Encryption)", "地理位置政策 (Geolocation policy)", "資料主權法規 (Data sovereignty regulation)"], "explain": "Geolocation Policy (地理位置政策) 在應用層根據用戶登入位置進行存取控制，直接檢驗 IP 地址的國家。"},
  514: {"q": "下列哪項是硬體特有的漏洞？", "opts": ["韌體版本 (Firmware version)", "緩衝區溢位 (Buffer overflow)", "SQL 注入 (SQL injection)", "跨站腳本 (XSS)"], "explain": "Firmware Version 漏洞是硬體層次的安全缺陷，如 BIOS/UEFI 漏洞或晶片設計缺陷如 Spectre/Meltdown。"},
  515: {"q": "技術人員在 ACL 底部新增「deny any」政策，但導致數個公司伺服器無法存取。應如何預防此問題？", "opts": ["向變更管理提交文件化的新政策請求", "在非生產環境測試政策，再在生產啟用", "在「deny any」政策之前禁用入侵防禦簽章", "在「deny any」之上加入「allow any」政策"], "explain": "在非生產環境進行變更測試是最佳實踐，能發現意外影響後再部署。"},
  516: {"q": "組織建置新備援資料中心，主要考量成本效益，RTO 和 RPO 約兩天。最適合此情境的網站類型是？", "opts": ["即時復原 (Real-time recovery)", "熱備站 (Hot)", "冷備站 (Cold)", "溫備站 (Warm)"], "explain": "Warm Site (溫備站) 平衡成本與復原時間：定期同步資料、定期測試系統，適合此成本與 RTO 要求。"},
  517: {"q": "公司要求報廢系統在回收前必須安全清除硬碟。此政策最佳描述為？", "opts": ["列舉 (Enumeration)", "淨化 (Sanitization)", "銷毀 (Destruction)", "清冊 (Inventory)"], "explain": "Sanitization (淨化) 是透過多次覆寫、加密清除等技術安全清除資料，使原資料無法復原，但硬體保留可重用。"},
  518: {"q": "醫院系統管理員需要保護患者資料安全。患者資料應使用下列哪種資料分類？", "opts": ["私人 (Private)", "關鍵 (Critical)", "敏感 (Sensitive)", "公開 (Public)"], "explain": "Sensitive (敏感資料) 是最常用的醫療健康資訊分類，因為洩露會導致隱私侵害、歧視、財務損害。"},
  519: {"q": "美國雲端服務商想在國際新地點擴展資料中心。首先應考慮下列哪項？", "opts": ["當地資料保護法規 (Local data protection regulations)", "來自其他國家駭客的風險", "對現有合約義務的影響", "時區差異對日誌關聯的影響"], "explain": "Local Data Protection Regulations (當地資料保護法規) 如 GDPR、CCPA 等對資料存儲位置有明確要求，違反會導致營運許可被撤銷。"},
  520: {"q": "防止未知程式執行的最佳方式是？", "opts": ["存取控制清單 (ACL)", "應用程式允許清單 (Application allow list)", "主機防火牆 (Host-based firewall)", "資料遺失防護 (DLP)"], "explain": "Application Allow List (應用程式允許清單) 列出所有被授權執行的軟體，預設拒絕其他任何程式。"}
};

// 继续添加题目 521-600
const moreTranslations = {
  521: {"q": "公司聘請顧問進行攻擊性安全評估，包括滲透測試和社交工程。應由下列哪支團隊進行？", "opts": ["白隊 (White)", "紫隊 (Purple)", "藍隊 (Blue)", "紅隊 (Red)"], "explain": "Red Team (紅隊) 的角色就是模擬攻擊者進行主動攻擊測試，包括滲透測試、社交工程、應用漏洞利用等。"},
  522: {"q": "軟體開發經理要確保公司開發代碼的真實性。最適當的選項是？", "opts": ["測試使用者輸入欄位的輸入驗證", "對公司開發的軟體進行代碼簽章", "對軟體進行靜態代碼分析", "確保使用安全 Cookie"], "explain": "Code Signing (代碼簽章) 用開發者的私鑰簽署可執行檔，購買者可驗證軟體確實來自聲稱的開發者。"},
  523: {"q": "下列哪項可用於辨識潛在攻擊者活動，同時不影響生產伺服器？", "opts": ["蜜罐 (Honeypot)", "視頻監控 (Video surveillance)", "零信任 (Zero Trust)", "地理圍籬 (Geofencing)"], "explain": "Honeypot (蜜罐) 是故意暴露的「誘捕系統」，模擬真實系統吸引攻擊者，監控其行為和技巧。"},
  524: {"q": "事件回應團隊在調查中試圖了解事件來源。下列哪項事件回應活動描述此過程？", "opts": ["分析 (Analysis)", "經驗教訓 (Lessons learned)", "偵測 (Detection)", "遏制 (Containment)"], "explain": "Analysis (分析) 階段深入調查事件的技術細節：攻擊者來源、使用的工具、影響範圍。"},
  525: {"q": "資安實踐者完成網路漏洞評估並發現多個漏洞，營運團隊已修復。接下來應做什麼？", "opts": ["進行稽核", "啟動滲透測試", "重新掃描網路", "提交報告"], "explain": "Rescan (重新掃描) 驗證補丁是否有效應用、漏洞是否真的被修復。"},
  526: {"q": "管理員收到通知：用戶在非工作時間遠端登入並複製大量資料到個人設備。最佳描述此活動為？", "opts": ["滲透測試", "釣魚攻擊", "外部稽核", "內部威脅 (Insider threat)"], "explain": "Insider Threat (內部威脅) 指員工本身進行未授權存取、竊取資料的行為。特徵：非工作時間、複製敏感資料。"},
  527: {"q": "下列哪項允許將訊息歸屬於特定個人？", "opts": ["適應性身分 (Adaptive identity)", "不可否認性 (Non-repudiation)", "驗證 (Authentication)", "存取日誌 (Access logs)"], "explain": "Non-Repudiation (不可否認性) 確保發送者無法否認送出訊息，透過數位簽章技術實現。"},
  528: {"q": "持續每日判斷伺服器安全設定是否被修改的最佳方式是？", "opts": ["自動化 (Automation)", "合規檢查清單 (Compliance checklist)", "認證 (Attestation)", "手動稽核 (Manual audit)"], "explain": "Automation (自動化) 透過檔案完整性監控 (FIM) 等工具持續監視設定檔，即時發現變化。"},
  529: {"q": "下列哪個工具能幫助偵測員工不小心電郵給客戶包含 PII 的檔案？", "opts": ["SCAP", "NetFlow", "防毒軟體 (Antivirus)", "資料遺失防護 (DLP)"], "explain": "DLP (Data Loss Prevention) 監視網路和端點的資料流，偵測包含 PII 的郵件並阻擋。"},
  530: {"q": "組織更新安全政策：使用正規表達式移除特殊字元。最佳說明此安全技術為？", "opts": ["識別嵌入金鑰", "代碼除錯", "輸入驗證 (Input validation)", "靜態代碼分析"], "explain": "Input Validation (輸入驗證) 包含「淨化」使用正規表達式刪除/編碼危險字元，防止注入攻擊。"},
  531: {"q": "分析師和管理層審視釣魚演練結果，點擊率超過容許閾值。要減少使用者點擊釣魚連結的影響，應執行下列哪項？", "opts": ["張貼辦公室釣魚意識海報", "部署電郵安全過濾器防釣魚郵件", "更新 EDR 政策阻擋自動執行下載程式", "針對釣魚跡象建立額外訓練"], "explain": "EDR 政策禁用「自動執行下載檔案」功能，即使使用者點擊惡意連結下載檔案也能防止執行。"},
  532: {"q": "舊 Linux 系統的主機防火牆只允許來自特定內部 IP 的連線。此時實施了什麼控制？", "opts": ["補償控制 (Compensating control)", "網路分段 (Network segmentation)", "風險轉移 (Transfer of risk)", "SNMP 陷阱 (SNMP traps)"], "explain": "Compensating Control (補償控制) 在某個一級防禦失效時，用替代手段彌補。"},
  533: {"q": "管理層注意新建帳號常有不正確的存取權限。系統管理員應使用哪種自動化技術簡化帳號建立？", "opts": ["護欄腳本 (Guard rail script)", "工單工作流程 (Ticketing workflow)", "逐步提升腳本 (Escalation script)", "使用者佈建腳本 (User provisioning script)"], "explain": "User Provisioning Script (使用者佈建腳本) 自動建立帳號、設定群組成員、指派正確權限。"},
  534: {"q": "公司規劃 SIEM 系統並指派分析師每週檢視日誌。公司正在設置哪種控制類型？", "opts": ["矯正性 (Corrective)", "預防性 (Preventive)", "偵測性 (Detective)", "威懾性 (Deterrent)"], "explain": "Detective Control (偵測性控制) 在安全事件發生後發現，SIEM 日誌審查屬此類。"},
  535: {"q": "系統管理員尋求低成本、雲端應用託管方案。下列哪項符合？", "opts": ["無伺服器框架 (Serverless framework)", "Type 1 Hypervisor", "SD-WAN", "SDN"], "explain": "Serverless (無伺服器) 如 AWS Lambda 是雲端應用託管最低成本方案：無需管理伺服器、按使用付費。"},
  536: {"q": "資安運營中心判斷偵測到的惡意活動為正常。未來忽略此類偵測的活動屬於下列哪項？", "opts": ["調校 (Tuning)", "彙總 (Aggregating)", "隔離 (Quarantining)", "封存 (Archiving)"], "explain": "Tuning (調校) 是減少誤報，調整 SIEM 規則以避免特定正常活動觸發告警。"},
  537: {"q": "分析師檢視網域活動日誌，注意到大量失敗的 jsmith 帳號登入嘗試。最佳解釋為？", "opts": ["jsmith 帳號已被鎖定", "鍵盤記錄程式安裝在 jsmith 工作站", "攻擊者在嘗試暴力破解 jsmith 帳號", "勒索軟體已部署在網域"], "explain": "大量失敗登入嘗試是 Brute-force attack (暴力破解) 的典型特徵。"},
  538: {"q": "公司擔心天氣事件造成伺服器室損害和停機。應考慮下列哪項？", "opts": ["叢集化伺服器 (Clustering servers)", "地理分散 (Geographic dispersion)", "負載平衡器 (Load balancers)", "離場備份 (Off-site backups)"], "explain": "Geographic Dispersion (地理分散) 在不同地點部署資料中心，確保單一位置天災無法癱瘓整個系統。"},
  539: {"q": "公司設置 BYOD 計畫的主要資安關切是？", "opts": ["生命週期結束 (End of life)", "緩衝區溢位 (Buffer overflow)", "VM 逃脫 (VM escape)", "越獄 (Jailbreaking)"], "explain": "Jailbreaking (越獄) 是將設備的作業系統限制移除，允許安裝未授權應用、繞過安全機制。"},
  540: {"q": "公司決定透過移除勒索軟體保險來降低網路保險成本。最可能使用的分析要素為？", "opts": ["平均修復時間 (MTTR)", "復原時間目標 (RTO)", "年度損失期望 (ARO)", "平均故障間隔時間 (MTBF)"], "explain": "ARO (Annualized Rate of Occurrence) 是「年發生率」乘以影響值，用來計算風險成本。"}
};

Object.assign(fullTranslationData, moreTranslations);

console.log(`資料已加載: ${Object.keys(fullTranslationData).length} 題翻譯資料`);
