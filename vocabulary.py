#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Security+ SY0-701 重要單字字典
每個單字包含：英文 + 中文翻譯 + 簡要說明

用途：在每題後面列出該題出現的關鍵單字，幫助學習。
"""

# 字典格式：{ "英文term (lowercase)": ("英文標準寫法", "中文翻譯", "簡要說明") }
VOCABULARY = {
    # ===== 威脅行為者 (Threat Actors) =====
    "threat actor": ("Threat Actor", "威脅行為者", "對組織造成資安威脅的人或團體"),
    "hacktivist": ("Hacktivist", "駭客主義者", "為政治/社會理念進行駭客活動"),
    "nation-state": ("Nation-State", "民族國家", "由政府支持的網路攻擊組織，常為 APT"),
    "organized crime": ("Organized Crime", "組織犯罪集團", "以財務獲利為動機的犯罪組織"),
    "insider threat": ("Insider Threat", "內部威脅", "來自組織內部人員的威脅"),
    "unskilled attacker": ("Unskilled Attacker", "技術不熟練攻擊者", "俗稱 Script Kiddie，使用現成工具"),
    "script kiddie": ("Script Kiddie", "腳本小子", "技術不熟練、使用現成攻擊工具者"),
    "shadow it": ("Shadow IT", "影子 IT", "員工未經 IT 部門核可使用的軟體/服務"),
    "whistleblower": ("Whistleblower", "吹哨者", "揭露組織內部不當行為者"),
    "apt": ("APT", "進階持續性威脅", "Advanced Persistent Threat，長期潛伏的針對性攻擊"),
    "advanced persistent threat": ("APT", "進階持續性威脅", "長期潛伏的針對性攻擊"),

    # ===== 攻擊手法 (Attacks) =====
    "phishing": ("Phishing", "釣魚攻擊", "透過偽造郵件騙取憑證或機敏資訊"),
    "spear phishing": ("Spear Phishing", "魚叉式釣魚", "針對特定個人的精緻釣魚"),
    "whaling": ("Whaling", "鯨釣攻擊", "針對 CEO/CFO 等高層的釣魚"),
    "smishing": ("Smishing", "簡訊釣魚", "SMS + Phishing，透過簡訊進行的釣魚"),
    "vishing": ("Vishing", "語音釣魚", "Voice + Phishing，透過電話進行的社交工程"),
    "pretexting": ("Pretexting", "假借身分", "編造情境劇本欺騙目標"),
    "impersonation": ("Impersonation", "冒充", "假冒他人身分（常為主管）"),
    "tailgating": ("Tailgating", "尾隨進入", "跟隨有權限員工通過門禁"),
    "typosquatting": ("Typosquatting", "錯字搶註", "註冊與合法網域相近的網域"),
    "watering hole": ("Watering Hole", "水坑攻擊", "在目標常造訪的網站植入惡意程式"),
    "social engineering": ("Social Engineering", "社交工程", "利用人性弱點而非技術漏洞的攻擊"),
    "dumpster diving": ("Dumpster Diving", "翻垃圾蒐情", "從廢棄文件/硬碟取得敏感資訊"),
    "shoulder surfing": ("Shoulder Surfing", "肩窺", "從旁觀察他人輸入密碼/PIN"),
    "ddos": ("DDoS", "分散式阻斷服務", "Distributed Denial of Service"),
    "dos": ("DoS", "阻斷服務", "Denial of Service，使服務無法回應"),
    "ransomware": ("Ransomware", "勒索軟體", "加密檔案並索取贖金"),
    "malware": ("Malware", "惡意軟體", "Malicious Software 的合稱"),
    "trojan": ("Trojan", "特洛伊木馬", "偽裝成合法軟體的惡意程式"),
    "rootkit": ("Rootkit", "Rootkit", "深層隱藏自身的惡意程式，難以偵測"),
    "worm": ("Worm", "蠕蟲", "可自我複製跨主機傳播的惡意程式"),
    "spyware": ("Spyware", "間諜軟體", "暗中收集使用者資訊的程式"),
    "keylogger": ("Keylogger", "鍵盤側錄", "記錄使用者按鍵的程式"),
    "logic bomb": ("Logic Bomb", "邏輯炸彈", "符合條件時觸發的隱藏惡意程式"),
    "fileless malware": ("Fileless Malware", "無檔案惡意軟體", "只在記憶體中運作不寫入磁碟的惡意程式"),
    "sql injection": ("SQL Injection", "SQL 注入", "透過輸入欄位注入惡意 SQL 語句"),
    "xss": ("XSS", "跨站腳本", "Cross-Site Scripting，注入惡意 JavaScript"),
    "cross-site scripting": ("XSS", "跨站腳本", "注入惡意 JavaScript 攻擊使用者瀏覽器"),
    "csrf": ("CSRF", "跨站請求偽造", "Cross-Site Request Forgery"),
    "buffer overflow": ("Buffer Overflow", "緩衝區溢位", "寫入超過緩衝區容量造成記憶體破壞"),
    "memory injection": ("Memory Injection", "記憶體注入", "將惡意程式碼注入合法程序的記憶體"),
    "directory traversal": ("Directory Traversal", "目錄遍歷", "利用 ../ 跳出網站目錄存取系統檔案"),
    "command injection": ("Command Injection", "命令注入", "透過輸入欄位執行系統命令"),
    "side-channel": ("Side-channel Attack", "側通道攻擊", "利用硬體實作細節（功耗、時序）"),
    "side loading": ("Side Loading", "旁路安裝", "繞過官方應用商店安裝程式"),
    "jailbreaking": ("Jailbreaking", "越獄/Root", "繞過 OS 安全限制取得 root 權限"),
    "brute force": ("Brute Force", "蠻力破解", "嘗試所有可能組合破解密碼"),
    "dictionary attack": ("Dictionary Attack", "字典攻擊", "用常見密碼清單嘗試破解"),
    "password spraying": ("Password Spraying", "密碼噴灑", "對多帳號嘗試少數常見密碼"),
    "credential stuffing": ("Credential Stuffing", "憑證填充", "用洩漏的帳密組合嘗試其他系統"),
    "credential harvesting": ("Credential Harvesting", "憑證收集", "竊取使用者帳密的攻擊"),
    "pass-the-hash": ("Pass-the-Hash", "Pass-the-Hash 攻擊", "直接用 NTLM hash 認證，不需明文密碼"),
    "on-path": ("On-path Attack", "中間人攻擊", "舊稱 MITM，攔截兩方通訊"),
    "mitm": ("MITM", "中間人攻擊", "Man-in-the-Middle，攻擊者攔截兩方通訊"),
    "replay attack": ("Replay Attack", "重放攻擊", "竊取並重新發送有效的通訊資料"),
    "session hijacking": ("Session Hijacking", "會話劫持", "竊取使用者 session token 接管登入"),
    "dns poisoning": ("DNS Poisoning", "DNS 投毒", "竄改 DNS 解析將使用者導到惡意站"),
    "arp poisoning": ("ARP Poisoning", "ARP 投毒", "竄改 ARP 表竊聽區網流量"),
    "evil twin": ("Evil Twin", "邪惡雙胞胎", "偽造同名 Wi-Fi 接入點誘騙連線"),
    "rogue access point": ("Rogue Access Point", "未授權無線接入點", "未經組織核可的無線基地台"),
    "deauthentication": ("Deauthentication", "去驗證攻擊", "強制斷開無線連線的攻擊"),
    "mac flooding": ("MAC Flooding", "MAC 洪水", "塞滿交換器 MAC 表使其廣播流量"),
    "footprinting": ("Footprinting", "踩點偵察", "蒐集目標環境資訊的階段"),
    "reconnaissance": ("Reconnaissance", "偵察", "攻擊前的資訊蒐集階段"),
    "enumeration": ("Enumeration", "列舉", "枚舉系統中的帳號/服務/資源"),
    "fuzzing": ("Fuzzing", "模糊測試", "對應用送入大量隨機輸入找漏洞"),
    "lateral movement": ("Lateral Movement", "橫向移動", "攻擊者在內部從一台主機跳到另一台"),
    "pivoting": ("Pivoting", "橫向移動", "Lateral Movement 同義"),
    "privilege escalation": ("Privilege Escalation", "權限提升", "從低權限取得高權限"),
    "supply chain attack": ("Supply Chain Attack", "供應鏈攻擊", "透過信任的廠商/軟體入侵目標"),
    "watering-hole": ("Watering-hole", "水坑攻擊", "在目標常造訪的網站植入惡意程式"),
    "vm escape": ("VM Escape", "VM 逃逸", "從 Guest VM 突破到 Host Hypervisor"),
    "race condition": ("Race Condition", "競爭條件", "兩程序同時存取造成的漏洞"),
    "zero-day": ("Zero-day", "零日漏洞", "尚未公開或未修補的漏洞"),
    "0-day": ("0-day", "零日漏洞", "尚未公開或未修補的漏洞"),
    "business email compromise": ("Business Email Compromise", "商業電郵入侵", "BEC，偽裝高層詐騙轉帳/機密"),
    "bec": ("BEC", "商業電郵入侵", "Business Email Compromise"),
    "ransomware-as-a-service": ("Ransomware-as-a-Service", "勒索軟體即服務", "RaaS，將勒索軟體出租給附屬攻擊者"),

    # ===== 加密與密碼學 (Cryptography) =====
    "encryption": ("Encryption", "加密", "將明文轉換為密文以保護資料"),
    "decryption": ("Decryption", "解密", "將密文還原為明文"),
    "hashing": ("Hashing", "雜湊", "單向函數，產生固定長度的雜湊值"),
    "hash": ("Hash", "雜湊值", "雜湊函數的輸出，用於驗證完整性"),
    "salting": ("Salting", "加鹽", "雜湊前加入隨機字串防彩虹表"),
    "salt": ("Salt", "鹽值", "加鹽用的隨機字串"),
    "key stretching": ("Key Stretching", "金鑰延展", "反覆雜湊增加破解成本"),
    "key escrow": ("Key Escrow", "金鑰託管", "將金鑰副本安全存放於第三方"),
    "pki": ("PKI", "公開金鑰基礎設施", "Public Key Infrastructure"),
    "public key": ("Public Key", "公鑰", "非對稱加密中可公開的金鑰"),
    "private key": ("Private Key", "私鑰", "非對稱加密中必須保密的金鑰"),
    "certificate": ("Certificate", "數位憑證", "證明公鑰所有權的電子文件"),
    "digital signature": ("Digital Signature", "數位簽章", "用私鑰簽署提供真實性與完整性"),
    "code signing": ("Code Signing", "程式碼簽章", "對軟體簽章驗證來源未被竄改"),
    "crl": ("CRL", "憑證撤銷清單", "Certificate Revocation List"),
    "ocsp": ("OCSP", "線上憑證狀態", "即時查詢憑證撤銷狀態的協定"),
    "csr": ("CSR", "憑證簽署請求", "Certificate Signing Request"),
    "aes": ("AES", "AES", "Advanced Encryption Standard，對稱加密標準"),
    "rsa": ("RSA", "RSA", "業界最常用的非對稱加密演算法"),
    "ecc": ("ECC", "橢圓曲線加密", "金鑰較短但安全性高的非對稱加密"),
    "sha-256": ("SHA-256", "SHA-256", "256 位元雜湊演算法"),
    "md5": ("MD5", "MD5", "已過時不安全的雜湊演算法"),
    "tls": ("TLS", "傳輸層安全", "Transport Layer Security，加密通訊協定"),
    "ssl": ("SSL", "SSL", "TLS 的前身，已過時不安全"),
    "symmetric encryption": ("Symmetric Encryption", "對稱式加密", "加解密使用相同金鑰，如 AES"),
    "asymmetric encryption": ("Asymmetric Encryption", "非對稱式加密", "公私鑰一對，如 RSA"),
    "tokenization": ("Tokenization", "代符化", "用無意義 token 取代敏感資料"),
    "masking": ("Masking", "資料遮罩", "隱藏部分敏感資料（如卡號末四碼）"),
    "steganography": ("Steganography", "隱寫術", "將訊息隱藏於影像/音訊等檔案中"),
    "obfuscation": ("Obfuscation", "程式碼混淆", "將程式改寫為難以理解的形式"),
    "fde": ("FDE", "全磁碟加密", "Full Disk Encryption"),
    "full disk encryption": ("Full Disk Encryption", "全磁碟加密", "加密整顆硬碟保護靜態資料"),
    "hsm": ("HSM", "硬體安全模組", "Hardware Security Module，金鑰保護裝置"),
    "tpm": ("TPM", "受信任平台模組", "主機板上的硬體信任根晶片"),

    # ===== 驗證與存取控制 (Authentication & Access) =====
    "authentication": ("Authentication", "身分驗證", "確認「你是誰」"),
    "authorization": ("Authorization", "授權", "決定「你可以做什麼」"),
    "accounting": ("Accounting", "稽核記帳", "記錄「你做了什麼」"),
    "aaa": ("AAA", "AAA 三元組", "Authentication + Authorization + Accounting"),
    "mfa": ("MFA", "多因素驗證", "Multi-Factor Authentication"),
    "multifactor authentication": ("Multifactor Authentication", "多因素驗證", "結合多種不同驗證因素"),
    "2fa": ("2FA", "雙因素驗證", "Two-Factor Authentication"),
    "sso": ("SSO", "單一登入", "Single Sign-On，一組憑證存取多應用"),
    "single sign-on": ("Single Sign-On", "單一登入", "一組憑證存取多應用"),
    "federation": ("Federation", "聯邦身分", "跨組織信任的身分認證"),
    "saml": ("SAML", "SAML", "Web SSO 的 XML 標準協議"),
    "oauth": ("OAuth", "OAuth", "授權框架，常用於第三方登入"),
    "kerberos": ("Kerberos", "Kerberos", "票證為基的網路驗證協議"),
    "ldap": ("LDAP", "LDAP", "輕量目錄存取協議"),
    "radius": ("RADIUS", "RADIUS", "集中式 AAA 驗證協議"),
    "tacacs+": ("TACACS+", "TACACS+", "Cisco 的集中驗證協議"),
    "rbac": ("RBAC", "角色為基存取控制", "Role-Based Access Control"),
    "dac": ("DAC", "自主存取控制", "Discretionary Access Control"),
    "mac": ("MAC (Access)", "強制存取控制", "Mandatory Access Control"),
    "abac": ("ABAC", "屬性為基存取控制", "Attribute-Based Access Control"),
    "acl": ("ACL", "存取控制清單", "Access Control List"),
    "pam": ("PAM", "特權存取管理", "Privileged Access Management"),
    "least privilege": ("Least Privilege", "最小權限", "只授予必要的最低權限"),
    "separation of duties": ("Separation of Duties", "職責分離", "敏感任務需多人共同執行"),
    "privilege creep": ("Privilege Creep", "權限蠕變", "員工調職後舊權限未被收回"),
    "zero trust": ("Zero Trust", "零信任", "永不信任、永遠驗證的安全模型"),
    "biometric": ("Biometric", "生物辨識", "指紋、臉部、虹膜等生理特徵驗證"),
    "totp": ("TOTP", "時間型一次性密碼", "Time-based OTP"),
    "otp": ("OTP", "一次性密碼", "One-Time Password"),

    # ===== 網路安全 (Network Security) =====
    "firewall": ("Firewall", "防火牆", "根據規則過濾網路流量"),
    "ngfw": ("NGFW", "次世代防火牆", "Next-Generation Firewall，含應用層檢測"),
    "waf": ("WAF", "Web 應用防火牆", "Web Application Firewall"),
    "ids": ("IDS", "入侵偵測系統", "Intrusion Detection System，偵測警報"),
    "ips": ("IPS", "入侵防護系統", "Intrusion Prevention System，主動阻擋"),
    "nids": ("NIDS", "網路入侵偵測", "Network-based IDS"),
    "nips": ("NIPS", "網路入侵防護", "Network-based IPS"),
    "dmz": ("DMZ", "非軍事區", "對外服務區，隔離內外網"),
    "vlan": ("VLAN", "虛擬區域網路", "Virtual LAN，邏輯網路分段"),
    "vpn": ("VPN", "虛擬私人網路", "在公開網路上建立加密通道"),
    "ipsec": ("IPSec", "IPSec", "網路層的加密與驗證協議"),
    "ssh": ("SSH", "SSH", "Secure Shell，加密遠端管理協議"),
    "telnet": ("Telnet", "Telnet", "明文遠端管理協議（不安全）"),
    "ftp": ("FTP", "FTP", "明文檔案傳輸協議（不安全）"),
    "sftp": ("SFTP", "SFTP", "基於 SSH 的安全檔案傳輸"),
    "rdp": ("RDP", "遠端桌面", "Remote Desktop Protocol"),
    "dns": ("DNS", "網域名稱系統", "Domain Name System，網址解析"),
    "dhcp": ("DHCP", "動態主機配置協議", "自動分配 IP 位址"),
    "smtp": ("SMTP", "SMTP", "Simple Mail Transfer Protocol，郵件協議"),
    "snmp": ("SNMP", "SNMP", "Simple Network Management Protocol"),
    "snmpv3": ("SNMPv3", "SNMPv3", "支援加密與驗證的 SNMP 版本"),
    "https": ("HTTPS", "HTTPS", "HTTP over TLS，加密 Web 通訊"),
    "nat": ("NAT", "網路位址轉換", "Network Address Translation"),
    "port security": ("Port Security", "連接埠安全", "限制 switch port 的 MAC 數量"),
    "mac filtering": ("MAC Filtering", "MAC 篩選", "依 MAC 位址過濾允許的裝置"),
    "segmentation": ("Segmentation", "網路分段", "將網路分為多個獨立區段"),
    "microsegmentation": ("Microsegmentation", "微分段", "細粒度的網路分段，常用於 Zero Trust"),
    "air-gapped": ("Air-gapped", "氣隙網路", "完全與外網實體隔離"),
    "jump server": ("Jump Server", "跳板伺服器", "存取受控網段的中介伺服器"),
    "bastion host": ("Bastion Host", "堡壘主機", "暴露於外網的受控存取點"),
    "load balancer": ("Load Balancer", "負載平衡器", "分散流量到多伺服器提升可用性"),
    "proxy": ("Proxy", "代理伺服器", "中介伺服器轉發請求"),
    "reverse proxy": ("Reverse Proxy", "反向代理", "代表伺服器接收外部請求"),
    "honeypot": ("Honeypot", "蜜罐", "誘餌系統蒐集攻擊者情資"),
    "honeyfile": ("Honeyfile", "蜜檔", "誘餌檔案觸發告警偵測內部威脅"),
    "honeytoken": ("Honeytoken", "蜜餌憑證", "誘餌帳密用於偵測未授權使用"),
    "dns sinkhole": ("DNS Sinkhole", "DNS 黑洞", "攔截到惡意域名的流量"),
    "nac": ("NAC", "網路存取控制", "Network Access Control"),
    "captive portal": ("Captive Portal", "強制門戶", "Wi-Fi 登入頁面要求驗證"),
    "wpa2": ("WPA2", "WPA2", "無線網路加密標準"),
    "wpa3": ("WPA3", "WPA3", "最新的無線加密標準"),
    "wep": ("WEP", "WEP", "已過時的無線加密協議"),
    "802.1x": ("802.1X", "802.1X", "連接埠為基的網路存取控制"),
    "sd-wan": ("SD-WAN", "軟體定義廣域網路", "Software-Defined WAN"),
    "sase": ("SASE", "安全存取服務邊緣", "整合 SD-WAN + 雲端安全"),
    "casb": ("CASB", "雲端存取安全代理", "Cloud Access Security Broker"),
    "ztna": ("ZTNA", "零信任網路存取", "Zero Trust Network Access"),

    # ===== 風險與合規 (Risk & Compliance) =====
    "risk": ("Risk", "風險", "威脅利用漏洞造成損害的可能性"),
    "threat": ("Threat", "威脅", "可能對資產造成損害的事件"),
    "vulnerability": ("Vulnerability", "漏洞", "可被利用的弱點"),
    "exploit": ("Exploit", "漏洞利用", "利用漏洞達成攻擊"),
    "risk register": ("Risk Register", "風險登記簿", "記錄追蹤所有已識別風險的文件"),
    "risk appetite": ("Risk Appetite", "風險偏好", "組織願意承擔的整體風險程度"),
    "risk tolerance": ("Risk Tolerance", "風險容忍度", "可接受風險的具體範圍"),
    "risk threshold": ("Risk Threshold", "風險門檻", "可接受風險的最大值"),
    "residual risk": ("Residual Risk", "剩餘風險", "套用控制後仍存在的風險"),
    "inherent risk": ("Inherent Risk", "固有風險", "未套用任何控制前的原始風險"),
    "risk mitigation": ("Risk Mitigation", "風險減緩", "導入控制降低風險的策略"),
    "risk acceptance": ("Risk Acceptance", "風險接受", "明確接受風險並記錄"),
    "risk avoidance": ("Risk Avoidance", "風險規避", "停止活動完全避免風險"),
    "risk transfer": ("Risk Transfer", "風險轉移", "將風險轉給保險或第三方"),
    "ale": ("ALE", "年度預期損失", "Annualized Loss Expectancy = SLE × ARO"),
    "aro": ("ARO", "年度發生率", "Annualized Rate of Occurrence"),
    "sle": ("SLE", "單次損失預期", "Single Loss Expectancy"),
    "compliance": ("Compliance", "合規", "符合法律法規與標準"),
    "audit": ("Audit", "稽核", "系統性檢視合規與控制有效性"),
    "attestation": ("Attestation", "證明文件", "獨立第三方出具的合規證明"),
    "due diligence": ("Due Diligence", "盡職調查", "決策前的事前研究調查"),
    "due care": ("Due Care", "盡職保密", "已知風險後採取的保護行動"),
    "gap analysis": ("Gap Analysis", "差距分析", "比較現況與目標的差距"),
    "gdpr": ("GDPR", "一般資料保護規則", "歐盟個資保護法規"),
    "hipaa": ("HIPAA", "HIPAA", "美國健保資訊保護法案"),
    "pci dss": ("PCI DSS", "支付卡產業標準", "信用卡資料保護標準"),
    "sox": ("SOX", "沙賓法案", "美國公司財務透明法案"),
    "iso 27001": ("ISO 27001", "ISO 27001", "資訊安全管理系統國際標準"),
    "nist": ("NIST", "NIST", "美國國家標準與技術研究院"),
    "data sovereignty": ("Data Sovereignty", "資料主權", "資料受儲存地法律管轄"),
    "data residency": ("Data Residency", "資料駐留", "資料實際儲存的地理位置"),
    "pii": ("PII", "個人識別資訊", "Personally Identifiable Information"),
    "phi": ("PHI", "受保護健康資訊", "Protected Health Information"),

    # ===== 控制類型 (Controls) =====
    "preventive control": ("Preventive Control", "預防控制", "事前防止事件發生"),
    "detective control": ("Detective Control", "偵測控制", "事中或事後察覺異常"),
    "corrective control": ("Corrective Control", "矯正控制", "事件後復原系統"),
    "deterrent control": ("Deterrent Control", "嚇阻控制", "讓潛在攻擊者打消念頭"),
    "compensating control": ("Compensating Control", "補償控制", "替代主要控制達成等效保護"),
    "directive control": ("Directive Control", "指示控制", "政策、規範類控制"),
    "managerial control": ("Managerial Control", "管理控制", "政策、計畫、風險評估等"),
    "technical control": ("Technical Control", "技術控制", "防火牆、加密等技術措施"),
    "physical control": ("Physical Control", "實體控制", "門禁、警衛、監視器等"),

    # ===== 事件回應與營運 (IR & Operations) =====
    "incident response": ("Incident Response", "事件回應", "處理資安事件的標準流程"),
    "irp": ("IRP", "事件回應計畫", "Incident Response Plan"),
    "preparation": ("Preparation", "準備階段", "IR 流程第一階段：事前準備"),
    "containment": ("Containment", "遏制階段", "限制攻擊範圍與影響"),
    "eradication": ("Eradication", "根除階段", "移除攻擊痕跡與惡意程式"),
    "recovery": ("Recovery", "復原階段", "恢復系統正常運作"),
    "lessons learned": ("Lessons Learned", "經驗教訓", "事後檢討改善流程"),
    "forensic": ("Forensic", "鑑識", "蒐集分析數位證據的程序"),
    "chain of custody": ("Chain of Custody", "證據鏈", "記錄證據從蒐集到呈交的轉手過程"),
    "playbook": ("Playbook", "事件劇本", "預先寫好的事件處理步驟"),
    "siem": ("SIEM", "SIEM", "Security Information and Event Management"),
    "soar": ("SOAR", "SOAR", "Security Orchestration, Automation and Response"),
    "soc": ("SOC", "安全運營中心", "Security Operations Center"),
    "edr": ("EDR", "端點偵測回應", "Endpoint Detection and Response"),
    "xdr": ("XDR", "延伸偵測回應", "Extended Detection and Response"),
    "dlp": ("DLP", "資料外洩防護", "Data Loss Prevention"),
    "mdm": ("MDM", "行動裝置管理", "Mobile Device Management"),
    "ueba": ("UEBA", "使用者行為分析", "User and Entity Behavior Analytics"),
    "threat hunting": ("Threat Hunting", "威脅獵捕", "主動搜尋環境中的進階威脅"),
    "threat intelligence": ("Threat Intelligence", "威脅情報", "關於威脅的可行動情資"),
    "ioc": ("IOC", "入侵指標", "Indicator of Compromise"),
    "mitre att&ck": ("MITRE ATT&CK", "MITRE ATT&CK", "攻擊者戰術技巧程序知識庫"),
    "cvss": ("CVSS", "CVSS", "Common Vulnerability Scoring System，漏洞評分"),
    "cve": ("CVE", "CVE", "Common Vulnerabilities and Exposures，漏洞編號"),
    "false positive": ("False Positive", "誤判", "工具誤報為威脅實際非"),
    "false negative": ("False Negative", "漏報", "工具未偵測到實際威脅"),
    "tuning": ("Tuning", "規則調校", "調整偵測規則減少誤報"),
    "penetration test": ("Penetration Test", "滲透測試", "模擬真實攻擊者測試防禦"),
    "vulnerability scan": ("Vulnerability Scan", "弱點掃描", "自動掃描系統漏洞"),
    "vulnerability assessment": ("Vulnerability Assessment", "弱點評估", "系統性評估弱點與風險"),
    "red team": ("Red Team", "紅隊", "模擬攻擊者進行測試的團隊"),
    "blue team": ("Blue Team", "藍隊", "負責防守的安全團隊"),
    "purple team": ("Purple Team", "紫隊", "整合紅隊攻擊與藍隊防守"),
    "rules of engagement": ("Rules of Engagement", "交戰守則", "滲透測試的範圍與限制"),
    "tabletop exercise": ("Tabletop Exercise", "桌上演練", "圍坐討論的情境推演"),
    "bug bounty": ("Bug Bounty", "漏洞獎金計畫", "獎勵發現漏洞的合法測試者"),

    # ===== 業務持續性與災害復原 (BCP/DRP) =====
    "bcp": ("BCP", "業務持續性計畫", "Business Continuity Plan"),
    "drp": ("DRP", "災害復原計畫", "Disaster Recovery Plan"),
    "bia": ("BIA", "業務影響分析", "Business Impact Analysis"),
    "rto": ("RTO", "恢復時間目標", "Recovery Time Objective"),
    "rpo": ("RPO", "恢復點目標", "Recovery Point Objective"),
    "mtbf": ("MTBF", "平均故障間隔", "Mean Time Between Failures"),
    "mttr": ("MTTR", "平均修復時間", "Mean Time To Repair"),
    "hot site": ("Hot Site", "熱備站", "即時可用的災難備援站"),
    "warm site": ("Warm Site", "溫備站", "部分準備的備援站"),
    "cold site": ("Cold Site", "冷備站", "只有空間的最低成本備援站"),
    "snapshot": ("Snapshot", "快照", "某時間點的系統狀態副本"),
    "geographic dispersion": ("Geographic Dispersion", "地理分散", "備援站位於不同地理位置"),
    "failover": ("Failover", "故障切換", "自動切換到備援系統"),
    "replication": ("Replication", "複寫", "資料即時同步到其他位置"),

    # ===== 雲端與開發 (Cloud & DevOps) =====
    "cloud": ("Cloud", "雲端", "透過網路提供的運算服務"),
    "iaas": ("IaaS", "基礎設施即服務", "Infrastructure as a Service"),
    "paas": ("PaaS", "平台即服務", "Platform as a Service"),
    "saas": ("SaaS", "軟體即服務", "Software as a Service"),
    "iac": ("IaC", "基礎設施即程式碼", "Infrastructure as Code，如 Terraform"),
    "serverless": ("Serverless", "無伺服器", "FaaS，按使用付費的運算"),
    "container": ("Container", "容器", "輕量級隔離的應用執行環境"),
    "containerization": ("Containerization", "容器化", "用容器部署應用的技術"),
    "virtualization": ("Virtualization", "虛擬化", "在一硬體執行多個虛擬機"),
    "hypervisor": ("Hypervisor", "Hypervisor", "管理虛擬機的軟體層"),
    "microservices": ("Microservices", "微服務", "將應用拆分為獨立小服務"),
    "sdlc": ("SDLC", "軟體開發生命週期", "Software Development Life Cycle"),
    "devops": ("DevOps", "DevOps", "整合開發與運維的文化方法"),
    "devsecops": ("DevSecOps", "DevSecOps", "在 DevOps 中整合資安"),
    "ci/cd": ("CI/CD", "持續整合部署", "Continuous Integration / Continuous Delivery"),
    "sast": ("SAST", "靜態應用安全測試", "Static Application Security Testing"),
    "dast": ("DAST", "動態應用安全測試", "Dynamic Application Security Testing"),
    "sca": ("SCA", "軟體組成分析", "Software Composition Analysis，掃描相依套件"),
    "input validation": ("Input Validation", "輸入驗證", "驗證使用者輸入符合預期格式"),
    "parameterized query": ("Parameterized Query", "參數化查詢", "防 SQL Injection 的標準做法"),

    # ===== 文件與協議 (Documents) =====
    "aup": ("AUP", "可接受使用政策", "Acceptable Use Policy"),
    "sla": ("SLA", "服務水準協議", "Service Level Agreement"),
    "sow": ("SOW", "工作說明書", "Statement of Work"),
    "msa": ("MSA", "主服務協議", "Master Service Agreement"),
    "nda": ("NDA", "保密協議", "Non-Disclosure Agreement"),
    "mou": ("MOU", "諒解備忘錄", "Memorandum of Understanding"),
    "moa": ("MOA", "協議備忘錄", "Memorandum of Agreement"),
    "bpa": ("BPA", "業務合作協議", "Business Partnership Agreement"),
    "right-to-audit": ("Right-to-Audit", "稽核權", "合約中允許客戶稽核供應商的條款"),

    # ===== 行動裝置與 IoT =====
    "byod": ("BYOD", "自帶裝置", "Bring Your Own Device"),
    "cope": ("COPE", "COPE", "Company-Owned, Personally Enabled"),
    "cobo": ("COBO", "COBO", "Company-Owned, Business Only"),
    "cyod": ("CYOD", "CYOD", "Choose Your Own Device"),
    "iot": ("IoT", "物聯網", "Internet of Things"),
    "ot": ("OT", "運營技術", "Operational Technology，工控系統"),
    "ics": ("ICS", "工業控制系統", "Industrial Control System"),
    "scada": ("SCADA", "SCADA", "監控與資料擷取系統"),
    "rtos": ("RTOS", "即時作業系統", "Real-Time Operating System"),
    "firmware": ("Firmware", "韌體", "嵌入硬體的低階軟體"),

    # ===== 資料管理 =====
    "data classification": ("Data Classification", "資料分類", "依敏感度分級資料"),
    "data sanitization": ("Data Sanitization", "資料淨化", "安全清除資料但保留媒介"),
    "sanitization": ("Sanitization", "資料淨化", "安全清除資料但保留媒介可再用 (NIST 800-88)"),
    "destruction": ("Destruction", "物理銷毀", "物理破壞媒介使其無法再使用"),
    "degaussing": ("Degaussing", "消磁銷毀", "用強磁場破壞磁性媒介（HDD/磁帶）"),
    "wiping": ("Wiping", "資料擦除", "多次覆寫磁區使資料不可復原"),
    "wipe": ("Wipe", "擦除", "覆寫資料的標準做法"),
    "formatting": ("Formatting", "格式化", "重建檔案系統但資料可被復原（非安全清除）"),
    "defragmentation": ("Defragmentation", "磁碟重組", "重組磁碟碎片（與資料清除無關）"),
    "shredding": ("Shredding", "碎紙銷毀", "物理碎紙或硬碟剪碎"),
    "data retention": ("Data Retention", "資料保留", "依法規保留資料的期限"),
    "legal hold": ("Legal Hold", "法律保留", "訴訟期間禁止銷毀相關資料"),
    "data owner": ("Data Owner", "資料所有者", "決定資料分類與政策的角色"),
    "data custodian": ("Data Custodian", "資料保管者", "實際執行存取控制與備份的角色"),
    "data controller": ("Data Controller", "資料控制者", "GDPR 中決定處理目的的角色"),
    "data processor": ("Data Processor", "資料處理者", "GDPR 中代為處理資料的角色"),

    # ===== 其他常見術語 =====
    "patching": ("Patching", "修補", "套用安全更新修復漏洞"),
    "hardening": ("Hardening", "強化", "強化系統設定減少攻擊面"),
    "baseline": ("Baseline", "基準", "標準配置或正常狀態參考"),
    "end of life": ("End of Life", "生命終期", "EOL，廠商停止提供新功能"),
    "end of support": ("End of Support", "結束支援", "EOS，廠商停止提供安全更新"),
    "legacy system": ("Legacy System", "舊系統", "過時但仍在使用的系統"),
    "decommissioning": ("Decommissioning", "除役", "停用報廢系統的程序"),
    "change management": ("Change Management", "變更管理", "管控系統變更的流程"),
    "backout plan": ("Backout Plan", "回退計畫", "變更失敗時的回復計畫"),
    "maintenance window": ("Maintenance Window", "維護時段", "預定可進行系統變更的時段"),
    "security awareness training": ("Security Awareness Training", "安全意識訓練", "教育員工辨識威脅的計畫"),
}


def normalize_term(s):
    """Normalize term for matching"""
    import re
    return re.sub(r'\s+', ' ', s.lower().strip())


def extract_vocabulary(english_text):
    """Extract key vocabulary terms from English text"""
    import re
    if not english_text:
        return []

    # Fix OCR issues for matching
    text = english_text.lower()
    ocr_fixes = {
        'rewall': 'firewall',
        'tra c': 'traffic',
        'conguring': 'configuring',
        'congure': 'configure',
        'certicate': 'certificate',
        'classication': 'classification',
        'identi cation': 'identification',
        'modi cation': 'modification',
        'noti cation': 'notification',
        'speci c': 'specific',
        'overow': 'overflow',
        'over ow': 'overflow',
        'leless': 'fileless',
        'condentiality': 'confidentiality',
    }
    for bad, good in ocr_fixes.items():
        text = text.replace(bad, good)

    found_terms = []
    seen = set()
    # Sort vocabulary keys by length (longest first) to match compound terms first
    sorted_keys = sorted(VOCABULARY.keys(), key=lambda x: -len(x))

    for key in sorted_keys:
        # Word boundary match (for multi-word terms)
        if ' ' in key or '-' in key or '/' in key:
            # Multi-word term: simple substring match
            pattern = re.escape(key)
        else:
            # Single word: use word boundaries
            pattern = r'\b' + re.escape(key) + r'\b'

        if re.search(pattern, text):
            en_official, zh, desc = VOCABULARY[key]
            if en_official not in seen:
                found_terms.append({
                    "en": en_official,
                    "zh": zh,
                    "desc": desc
                })
                seen.add(en_official)

    return found_terms


if __name__ == "__main__":
    # Test
    test = "An employee receives a phishing email claiming to be from MFA admin. Which of the following social engineering attacks is this?"
    vocab = extract_vocabulary(test)
    print(f"Found {len(vocab)} terms:")
    for v in vocab:
        print(f"  {v['en']} → {v['zh']}: {v['desc']}")
