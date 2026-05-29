#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Direct corrections for batch translations that had wrong content.
These were verified by reading PDF and confirming the Chinese was about
a completely different topic than the English question.
"""

CORRECTIONS = {
    # Q28: PDF about IT manager limiting console access to himself + lead
    28: {
        "q": "IT 經理通知服務台全體：管理員主控台只有 IT 經理與服務台組長能存取。這是哪種安全技術？",
        "opts": ["強化 (Hardening)", "員工監控", "組態強制執行", "最小權限 (Least privilege)"],
        "explain": "正確答案：D（Least privilege 最小權限）。限制特定權限只給「真正需要的人員」是最小權限原則的核心應用。減少擁有高權限帳號的人數可大幅降低帳號被盜或誤用的風險。"
    },
    # Q91: PDF about maximum allowance of accepted risk → Risk threshold
    91: {
        "q": "下列何者描述「可接受風險的最大值」？",
        "opts": ["風險指標 (Risk indicator)", "風險等級 (Risk level)", "風險分數 (Risk score)", "風險門檻 (Risk threshold)"],
        "explain": "正確答案：D（Risk threshold 風險門檻）。Risk threshold 是組織願意接受的風險上限值；超過此值就必須採取減緩、轉移或規避措施。Risk appetite 是整體風險偏好，threshold 則是具體可量化的門檻值。"
    },
    # Q94: PDF about secure zone + access control + reduce threat scope → Zero Trust
    94: {
        "q": "管理員處理以下需求：① 提供安全區 ② 強制全公司存取控制政策 ③ 縮小威脅範圍。應建置下列何者？",
        "opts": ["零信任 (Zero Trust)", "AAA 驗證/授權/稽核", "不可否認性 (Non-repudiation)", "CIA 三元組"],
        "explain": "正確答案：A（Zero Trust 零信任）。Zero Trust 架構同時提供：安全區段化、全企業統一存取政策（基於身分+裝置+情境的條件式驗證）、最小權限與微分段以縮小攻擊面，三者完全對應題目需求。"
    },
    # Q98: PDF about quantitative vulnerability criticality → CVSS
    98: {
        "q": "下列何者用於「定量衡量漏洞的嚴重度」？",
        "opts": ["CVE 通用漏洞編號", "CVSS 通用漏洞評分系統", "CIA 機密/完整/可用性", "CERT 緊急應變小組"],
        "explain": "正確答案：B（CVSS）。CVSS（Common Vulnerability Scoring System）為漏洞提供 0–10 的量化分數，反映其嚴重度與可利用性。CVE 只是漏洞編號（識別用）；CIA 是安全三元組；CERT 是應變組織。"
    },
    # Q109: PDF about ransomware-as-a-service → Organized crime
    109: {
        "q": "CISO 想在給管理層的報告中提升員工對「勒索軟體即服務 (RaaS) 增加」的意識。下列何者最能描述 CISO 報告中的威脅行為者？",
        "opts": ["內部威脅 (Insider threat)", "駭客主義者 (Hacktivist)", "民族國家 (Nation-state)", "組織犯罪集團 (Organized crime)"],
        "explain": "正確答案：D（Organized crime 組織犯罪集團）。勒索軟體即服務 (RaaS) 是組織犯罪集團的標誌性商業模式：他們開發勒索軟體並出租給附屬攻擊者賺取分成。動機是金錢，最符合組織犯罪定義。Hacktivist 為理念、Nation-state 為政治、Insider 為內部濫用。"
    },
    # Q280: PDF about MFA with smart card → PIN
    280: {
        "q": "公司想實作 MFA。使用智慧卡時，下列何者可作為「額外的驗證因素」？",
        "opts": ["PIN 碼", "硬體令牌 (Hardware token)", "使用者 ID", "SMS 簡訊"],
        "explain": "正確答案：A（PIN）。智慧卡屬於「Something you have」（擁有的東西）。為達成真正 MFA，需要不同類別的因素，PIN 屬於「Something you know」（知道的東西），與智慧卡組合即為雙因素驗證。Hardware token 同為「have」不算多因素；User ID 是識別非驗證；SMS 雖屬 have 但智慧卡已是 have。"
    },
    # Q24: PDF asks about new tactic and threat hunting tool
    24: {
        "q": "資安運營團隊告知分析師：惡意行為者正使用新手法在內部網路中傳播。分析師應使用下列何者主動找出該手法的痕跡？",
        "opts": ["EDR 端點偵測回應", "弱點掃描", "SIEM 警報關聯", "威脅獵捕 (Threat hunting)"],
        "explain": "正確答案：D（Threat hunting 威脅獵捕）。Threat hunting 是主動搜尋環境中尚未被自動化工具偵測的進階威脅與 TTPs（戰術/技巧/程序），最適合針對「新手法」這類未知威脅的調查。"
    },
    # Q26: PDF asks about laptop encryption → Full disk encryption
    26: {
        "q": "資安管理員想保護員工筆電上的資料。下列哪種加密技術最適合？",
        "opts": ["檔案加密", "資料庫加密", "全磁碟加密 (Full disk)", "傳輸層加密 (TLS)"],
        "explain": "正確答案：C（Full disk encryption / FDE）。FDE 加密整顆硬碟，筆電遺失或被竊時即使取出硬碟也無法讀取任何資料，是保護端點靜態資料的標準做法（如 BitLocker、FileVault）。"
    },
    # Q78: PDF asks about IR phase when analyst reviews
    78: {
        "q": "下列何者是事件回應流程中「資安分析師在事件發生前就會檢視其角色職責的階段」？",
        "opts": ["準備 (Preparation)", "偵測 (Detection)", "遏制 (Containment)", "復原 (Recovery)"],
        "explain": "正確答案：A（Preparation 準備階段）。事件回應 (NIST SP 800-61) 的 Preparation 階段在事件發生前完成：建立 IR 團隊、定義角色、準備工具、執行訓練演練。其他階段都是事件發生後執行。"
    },
    # Q79: PDF asks about hardening routers → disable Web-based administration
    79: {
        "q": "最近弱點掃描後，資安工程師需要強化企業網路中的路由器。下列何者最適合「停用」？",
        "opts": ["SSH 管理介面", "本地主控台存取", "SNMPv3 監控", "Web 為基的管理介面"],
        "explain": "正確答案：D（Web-based administration 基於 Web 的管理介面）。路由器強化的標準作法是停用未加密或非必要的管理通道，特別是 Web 管理介面通常含已知漏洞且加密強度不足。SSH 與 SNMPv3 是加密版本應保留。"
    },
    # Q87: PDF asks about IR activities ensuring evidence is properly handled
    87: {
        "q": "下列哪一項事件回應活動可確保「證據被妥善處理」？",
        "opts": ["撰寫事件報告", "證據鏈 (Chain of custody)", "通知執法單位", "進行根本原因分析"],
        "explain": "正確答案：B（Chain of custody 證據鏈）。Chain of Custody 是數位鑑識的核心：記錄證據從蒐集到呈交法庭每一次的轉手、儲存、處理人員與時間。確保證據完整性、可追溯且可被法庭採信。"
    },
    # Q92: PDF asks about internal system sending large amount of unusual DNS queries
    92: {
        "q": "資安分析師收到警報：某內部系統正向外部域名發送大量異常的 DNS 查詢。最可能正在發生什麼事？",
        "opts": ["DNS 服務遭破壞", "資料正被外洩 (DNS Tunneling 外洩)", "DNS 快取投毒", "正常的 DNS 解析"],
        "explain": "正確答案：B（資料正被外洩 / Data is being exfiltrated）。「大量異常 DNS 查詢」是 DNS Tunneling 外洩的典型特徵：攻擊者將機敏資料編碼進 DNS 查詢子域名，繞過防火牆對外傳送。應立即隔離該主機並深入分析。"
    },
    # Q95: PDF asks about database miscongurations → SQL injection
    95: {
        "q": "下列何者涉及「試圖利用資料庫的錯誤設定」進行的攻擊？",
        "opts": ["緩衝區溢位 (Buffer overflow)", "SQL 注入 (SQL injection)", "VM 逃逸 (VM escape)", "記憶體注入 (Memory injection)"],
        "explain": "正確答案：B（SQL Injection / SQL 注入）。SQL Injection 攻擊者透過應用程式輸入欄位注入惡意 SQL 命令，利用資料庫缺乏輸入驗證、過寬權限、未過濾錯誤訊息等設定不當問題，達成資料外洩或竄改。防範方式：使用參數化查詢、輸入驗證、最小權限原則。"
    },
}
