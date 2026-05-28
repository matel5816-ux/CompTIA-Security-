#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate English options to Chinese with proper technical terminology.
Strategy:
- Short options (technical terms only): Use term dictionary directly
- Long options (sentences): Use phrase translation + term replacement
"""
import json
import re

# Phrase translations for common option sentence patterns
# These are applied BEFORE term replacement, in order of priority (longest first)
PHRASE_MAP = {
    # Procedural / action patterns
    "Documenting the new policy in a change request and submitting the request to change management": "在變更請求中記錄新政策並提交給變更管理",
    "Testing the policy in a non-production environment before enabling the policy in the production network": "在生產網路啟用前先於非生產環境測試政策",
    "Disabling any intrusion prevention signatures on the \"deny any\" policy prior to enabling the new policy": "啟用新政策前停用『deny any』政策上的所有 IPS 簽章",
    "Including an \"allow any\" policy above the \"deny any\" policy": "在『deny any』政策上方加入『allow any』政策",

    # Cloud / international
    "Local data protection regulations": "當地的資料保護法規",
    "Risks from hackers residing in other countries": "來自其他國家駭客的風險",
    "Impacts to existing contractual obligations": "對現有合約義務的影響",
    "Time zone differences in log correlation": "日誌關聯分析中的時區差異",

    # Hardening / server
    "Disable default accounts.": "停用預設帳號",
    "Disable default accounts": "停用預設帳號",
    "Add the server to the asset inventory.": "將伺服器加入資產清冊",
    "Add the server to the asset inventory": "將伺服器加入資產清冊",
    "Remove unnecessary services.": "移除非必要服務",
    "Remove unnecessary services": "移除非必要服務",
    "Document default passwords.": "記錄預設密碼",
    "Document default passwords": "記錄預設密碼",
    "Send server logs to the SIEM.": "將伺服器日誌送到 SIEM",
    "Send server logs to the SIEM": "將伺服器日誌送到 SIEM",
    "Join the server to the corporate domain.": "將伺服器加入企業網域",
    "Join the server to the corporate domain": "將伺服器加入企業網域",

    # Password
    "Increasing the minimum password length to 14 characters.": "將最短密碼長度提升到 14 字元",
    "Increasing the minimum password length to 14 characters": "將最短密碼長度提升到 14 字元",
    "Upgrading the password hashing algorithm from MD5 to SHA-512.": "把密碼雜湊演算法從 MD5 升級到 SHA-512",
    "Upgrading the password hashing algorithm from MD5 to SHA-512": "把密碼雜湊演算法從 MD5 升級到 SHA-512",
    "Increasing the maximum password age to 120 days.": "將密碼最長使用期延長到 120 天",
    "Reducing the minimum password length to ten characters.": "將最短密碼長度減為 10 字元",
    "Reducing the minimum password age to zero days.": "將最短密碼使用期降為 0 天",
    "Including a requirement for at least one special character.": "要求至少一個特殊字元",
    "Username and password": "使用者名稱與密碼",
    "Time-based tokens": "時間型令牌 (TOTP)",
    "Password, authentication token, thumbprint": "密碼、驗證令牌、指紋",

    # Common physical security options
    "Fencing": "圍籬",
    "Video surveillance": "影像監視",
    "Badge access": "門禁卡",
    "Access control vestibule": "門禁通道 (Mantrap)",
    "Sign-in sheet": "簽到表",
    "Sensor": "感測器",
    "Bollards": "防撞柱",
    "Lighting": "照明",
    "Security guard": "保全人員",
    "Signs": "警示標誌",

    # Common cryptography options
    "Key escrow": "金鑰託管",
    "TPM presence": "TPM 存在",
    "Digital signatures": "數位簽章",
    "Data tokenization": "資料代符化",
    "Public key management": "公鑰管理",
    "Certificate authority linking": "憑證機構連結",
    "Hashing": "雜湊",
    "Encryption": "加密",
    "Tokenization": "代符化",
    "Masking": "資料遮罩",
    "Obfuscation": "程式碼混淆",

    # Common access control / network options
    "Full disk encryption": "全磁碟加密 (FDE)",
    "Network access control": "網路存取控制 (NAC)",
    "File integrity monitoring": "檔案完整性監控 (FIM)",
    "User behavior analytics": "使用者行為分析 (UBA)",
    "Application allow list": "應用程式允許名單",
    "Application allowlist": "應用程式允許名單",

    # Threat actors
    "Hacktivist": "駭客主義者",
    "Whistleblower": "吹哨者",
    "Organized crime": "組織犯罪集團",
    "Unskilled attacker": "技術不熟練的攻擊者",
    "Nation-state": "民族國家",
    "Insider threat": "內部威脅",
    "Script kiddie": "Script Kiddie (技術不熟者)",

    # Frequent risk strategies
    "Avoid": "規避",
    "Accept": "接受",
    "Transfer": "轉移",
    "Mitigate": "減緩",
    "Mitigation": "減緩",
    "Acceptance": "接受",
    "Avoidance": "規避",
    "Transference": "轉移",

    # Vulnerability scan related
    "Non-credentialed scan": "無憑證掃描",
    "Credentialed scan": "授權掃描",
    "Packet capture": "封包擷取",
    "Privilege escalation": "權限提升",
    "System enumeration": "系統列舉",
    "Passive scan": "被動掃描",

    # Common control types (single word)
    "Preventive": "預防控制",
    "Detective": "偵測控制",
    "Corrective": "矯正控制",
    "Deterrent": "嚇阻控制",
    "Compensating": "補償控制",
    "Directive": "指示控制",
    "Managerial": "管理控制",
    "Technical": "技術控制",
    "Operational": "營運控制",
    "Physical": "實體控制",
    "Administrative": "行政控制",

    # Common backup / DR options
    "Hot": "熱備站 (Hot site)",
    "Warm": "溫備站 (Warm site)",
    "Cold": "冷備站 (Cold site)",
    "Hot site": "熱備站",
    "Warm site": "溫備站",
    "Cold site": "冷備站",
    "Mobile site": "行動備站",
    "Snapshot": "快照",
    "Snapshots": "快照",
    "Generator": "發電機",
    "UPS": "UPS 不斷電系統",
    "Off-site replication": "離站複寫",
    "Backup": "備份",
    "Backups": "備份",
    "Geographic dispersion": "地理分散",

    # Common processes / phases
    "Preparation": "準備",
    "Detection": "偵測",
    "Analysis": "分析",
    "Containment": "遏制",
    "Eradication": "根除",
    "Recovery": "復原",
    "Lessons learned": "經驗教訓",
    "Acquisition": "證據擷取",
    "Identification": "識別",
    "Reporting": "報告",
    "Inventory": "資產清冊",
    "Retention": "保留",
    "Sanitization": "資料淨化",
    "Destruction": "銷毀",
    "Classification": "分類",
    "Compromise": "妥協",

    # Common red/blue/purple
    "Red": "紅隊",
    "Blue": "藍隊",
    "Purple": "紫隊",
    "White": "白隊",
    "Yellow": "黃隊",
    "Red team": "紅隊",
    "Blue team": "藍隊",
    "Purple team": "紫隊",

    # Common encryption / data
    "Symmetric": "對稱式加密",
    "Asymmetric": "非對稱式加密",
    "Symmetric encryption": "對稱式加密",
    "Asymmetric encryption": "非對稱式加密",

    # Misc common phrases
    "Wired": "有線",
    "Wireless": "無線",
    "Sensitive": "敏感",
    "Confidential": "機密",
    "Public": "公開",
    "Private": "私有",
    "Restricted": "限制",
    "Critical": "關鍵",
    "Recurring": "週期性",
    "Continuous": "持續",
    "One-time": "一次性",
    "Ad-hoc": "臨時",
    "Quantitative": "定量分析",
    "Qualitative": "定性分析",
    "Standard operating procedure": "標準作業程序 (SOP)",
    "Backout plan": "回退計畫",
    "Maintenance window": "維護時段",
    "Change control process": "變更控制流程",
    "Scheduled downtime": "預定停機時間",
    "Conditional access policies": "條件式存取政策",
    "Trusted devices": "可信裝置",
    "Time-of-day restrictions": "時段限制",
    "Time-based access control": "時間型存取控制",
    "Independent audit": "獨立稽核",
    "Internal audit": "內部稽核",
    "External audit": "外部稽核",
    "Internal auditing": "內部稽核",
    "Third-party attestation": "第三方證明文件",
    "Attestation": "證明文件",
    "Attestation report": "證明報告",
    "Attestation of compliance": "合規證明 (AoC)",
    "Compliance attestation": "合規證明",
    "Right-to-audit": "稽核權",
    "Right to audit clause": "稽核權條款",
    "Due diligence": "盡職調查",
    "Due care": "盡職保密",
    "Gap analysis": "差距分析",
    "Risk register": "風險登記簿",
    "Risk matrix": "風險矩陣",
    "Risk appetite": "風險偏好",
    "Risk tolerance": "風險容忍度",

    # Communication
    "Channels by which the organization communicates with customers": "組織與客戶的溝通管道",
    "The reporting mechanisms for ethics violations": "倫理違規的回報機制",
    "Threat vectors based on the industry in which the organization operates": "依組織所在行業的威脅向量",
    "Secure software development training for all personnel": "全員的安全軟體開發訓練",
    "Cadence and duration of training events": "訓練的頻率與時長",
    "Retraining requirements for individuals who fail phishing simulations": "釣魚演練未通過者的重訓要求",

    # Decommission reasons
    "The device has been moved from a production environment to a test environment.": "裝置從生產環境移到測試環境",
    "The device is configured to use cleartext passwords.": "裝置設定使用明文密碼",
    "The device is moved to an isolated segment on the enterprise network.": "裝置移到企業網路的隔離區段",
    "The device is moved to a different location in the enterprise.": "裝置移到企業內的其他位置",
    "The device's encryption level cannot meet organizational standards.": "裝置的加密強度無法達到組織標準",
    "The device is unable to receive authorized updates.": "裝置無法接收授權的更新",

    # Network components
    "Application": "應用",
    "Authentication": "驗證",
    "DHCP": "DHCP",
    "Network": "網路",
    "Firewall": "防火牆",
    "Database": "資料庫",

    # User / employee
    "Reporting phishing attempts or other suspicious activities": "回報釣魚或其他可疑活動",
    "Cancel current employee recognition gift cards.": "取消現有員工獎勵禮品卡",
    "Add a smishing exercise to the annual company training.": "在年度訓練加入簡訊釣魚演練",
    "Issue a general email warning to the company.": "向全公司發出警示郵件",
    "Have the CEO change phone numbers.": "讓 CEO 更換電話號碼",
    "Conduct a forensic investigation on the CEO's phone.": "對 CEO 手機進行鑑識調查",
    "Implement mobile device management.": "實施行動裝置管理 (MDM)",

    # Common metric / measurement
    "ALE": "ALE 年度預期損失",
    "ARO": "ARO 年度發生率",
    "SLE": "SLE 單次損失預期",
    "RTO": "RTO 恢復時間目標",
    "RPO": "RPO 恢復點目標",
    "MTBF": "MTBF 平均故障間隔",
    "MTTR": "MTTR 平均修復時間",

    # Common authentication methods
    "Federation": "聯邦身分",
    "Identity proofing": "身分驗證",
    "Identity proofng": "身分驗證",
    "Password complexity": "密碼複雜度",
    "Default password changes": "更改預設密碼",
    "Password manager": "密碼管理器",
    "Open authentication": "Open Authentication",
}

# Technical term dictionary (for fallback / term replacement)
TERM_MAP = {
    "MFA": "MFA 多因素驗證",
    "Multifactor authentication": "多因素驗證 (MFA)",
    "SSO": "SSO 單一登入",
    "Single sign-on": "單一登入 (SSO)",
    "Single Sign-On": "單一登入 (SSO)",
    "RBAC": "RBAC 角色為基存取控制",
    "DAC": "DAC 自主存取控制",
    "ABAC": "ABAC 屬性為基存取控制",
    "VPN": "VPN",
    "IPSec": "IPSec",
    "IPsec": "IPSec",
    "TLS": "TLS",
    "SSL": "SSL",
    "HTTPS": "HTTPS",
    "HTTP": "HTTP",
    "FTP": "FTP",
    "SFTP": "SFTP",
    "SSH": "SSH",
    "Telnet": "Telnet",
    "RDP": "RDP",
    "SNMP": "SNMP",
    "SNMPv3": "SNMPv3",
    "SMTP": "SMTP",
    "DNS": "DNS",
    "DHCP": "DHCP",
    "LDAP": "LDAP",
    "Kerberos": "Kerberos",
    "OAuth": "OAuth",
    "SAML": "SAML",
    "RADIUS": "RADIUS",
    "TACACS+": "TACACS+",
    "AES": "AES",
    "RSA": "RSA",
    "ECC": "ECC",
    "SHA-256": "SHA-256",
    "MD5": "MD5",
    "PKI": "PKI",
    "HSM": "HSM 硬體安全模組",
    "TPM": "TPM 受信任平台模組",
    "FDE": "FDE 全磁碟加密",
    "SIEM": "SIEM",
    "SOAR": "SOAR",
    "EDR": "EDR 端點偵測回應",
    "XDR": "XDR",
    "DLP": "DLP 資料外洩防護",
    "MDM": "MDM 行動裝置管理",
    "WAF": "WAF Web應用防火牆",
    "NGFW": "NGFW 次世代防火牆",
    "IDS": "IDS 入侵偵測",
    "IPS": "IPS 入侵防護",
    "NIDS": "NIDS",
    "NIPS": "NIPS",
    "DMZ": "DMZ 非軍事區",
    "VLAN": "VLAN",
    "NAC": "NAC 網路存取控制",
    "CASB": "CASB",
    "SASE": "SASE",
    "ZTNA": "ZTNA",
    "SD-WAN": "SD-WAN",
    "DDoS": "DDoS",
    "BYOD": "BYOD 自帶裝置",
    "COPE": "COPE",
    "COBO": "COBO",
    "CYOD": "CYOD",
    "IoT": "IoT 物聯網",
    "OT": "OT 運營技術",
    "ICS": "ICS 工業控制系統",
    "RTOS": "RTOS 即時作業系統",
    "GDPR": "GDPR",
    "HIPAA": "HIPAA",
    "PCI DSS": "PCI DSS",
    "PCI": "PCI",
    "SOX": "SOX",
    "ISO 27001": "ISO 27001",
    "NIST": "NIST",
    "SOC 2 Type 1": "SOC 2 Type 1",
    "SOC 2 Type 2": "SOC 2 Type 2",
    "SOC 2": "SOC 2",
    "SOC": "SOC 安全運營中心",
    "AUP": "AUP 可接受使用政策",
    "SLA": "SLA 服務水準協議",
    "MOU": "MOU 諒解備忘錄",
    "MSA": "MSA 主服務協議",
    "SOW": "SOW 工作說明書",
    "NDA": "NDA 保密協議",
    "OWASP": "OWASP",
    "MITRE ATT&CK": "MITRE ATT&CK",
    "ATT&CK": "ATT&CK",
    "CVE": "CVE",
    "CVSS": "CVSS",
    "CWE": "CWE",
    "PII": "PII 個人識別資訊",
    "PHI": "PHI 受保護健康資訊",
    "BCP": "BCP 業務持續性計畫",
    "DRP": "DRP 災害復原計畫",
    "IRP": "IRP 事件回應計畫",
    "BIA": "BIA 業務影響分析",
    "IaaS": "IaaS",
    "PaaS": "PaaS",
    "SaaS": "SaaS",
    "IaC": "IaC 基礎設施即程式碼",
    "CI/CD": "CI/CD",
    "SAST": "SAST 靜態應用安全測試",
    "DAST": "DAST 動態應用安全測試",
    "SCA": "SCA 軟體組成分析",
    "GPO": "GPO 群組原則",
    "ACL": "ACL 存取控制清單",
    "PAM": "PAM 特權存取管理",
    "OCSP": "OCSP",
    "CRL": "CRL 憑證撤銷清單",
    "CSR": "CSR 憑證簽署請求",
    "AES": "AES",
    "WPA2": "WPA2",
    "WPA3": "WPA3",
    "WEP": "WEP",
    "PEAP": "PEAP",
    "LEAP": "LEAP",
    "EAP": "EAP",
    "EAP-TLS": "EAP-TLS",
    "OSINT": "OSINT 開源情報",
    "APT": "APT 進階持續性威脅",
    "SPOF": "SPOF 單點故障",

    # Threats
    "Phishing": "釣魚攻擊",
    "Spear-phishing": "魚叉式釣魚",
    "Spear phishing": "魚叉式釣魚",
    "Whaling": "鯨釣 (針對高層)",
    "Smishing": "簡訊釣魚",
    "Vishing": "語音釣魚",
    "Pretexting": "假借身分",
    "Impersonation": "冒充",
    "Impersonating": "冒充",
    "Tailgating": "尾隨進入",
    "Typosquatting": "錯字搶註",
    "Brand impersonation": "品牌冒充",
    "Social engineering": "社交工程",
    "Misinformation": "假訊息",
    "Watering-hole": "水坑攻擊",
    "Watering hole": "水坑攻擊",
    "Dumpster diving": "翻垃圾蒐情",
    "Blackmail": "勒索",
    "Malware": "惡意軟體",
    "Ransomware": "勒索軟體",
    "Trojan": "特洛伊木馬",
    "Worm": "蠕蟲",
    "Virus": "病毒",
    "Spyware": "間諜軟體",
    "Adware": "廣告軟體",
    "Rootkit": "Rootkit",
    "Keylogger": "鍵盤側錄",
    "Backdoor": "後門",
    "Logic bomb": "邏輯炸彈",
    "Botnet": "Botnet",
    "Zero-day": "零日漏洞 (0-day)",
    "0-day": "零日漏洞",
    "SQL injection": "SQL 注入",
    "Cross-site scripting": "XSS 跨站腳本",
    "XSS": "XSS 跨站腳本",
    "CSRF": "CSRF 跨站請求偽造",
    "Buffer overflow": "緩衝區溢位",
    "Memory injection": "記憶體注入",
    "Directory traversal": "目錄遍歷",
    "Command injection": "命令注入",
    "Side-channel attack": "側通道攻擊",
    "Side loading": "Side-loading 旁路安裝",
    "Side-loading": "Side-loading 旁路安裝",
    "Jailbreaking": "越獄",
    "Pass-the-hash": "Pass-the-hash 攻擊",
    "On-path": "中間人攻擊",
    "On-path attack": "中間人攻擊 (MITM)",
    "MITM": "中間人攻擊 (MITM)",
    "Brute force": "蠻力破解",
    "Brute-force": "蠻力破解",
    "DNS poisoning": "DNS 投毒",
    "ARP poisoning": "ARP 投毒",
    "Rogue access point": "未授權無線接入點",
    "Evil twin": "邪惡雙胞胎",
    "Footprinting": "踩點偵察",
    "Reconnaissance": "偵察",
    "Fuzzing": "模糊測試",
    "Lateral movement": "橫向移動",
    "Pivoting": "橫向移動",
    "Hacktivist": "駭客主義者",
    "Whistleblower": "吹哨者",
    "Organized crime": "組織犯罪集團",
    "Nation-state": "民族國家",
    "Insider threat": "內部威脅",
    "Unskilled attacker": "技術不熟練攻擊者",
    "Shadow IT": "影子 IT",
    "Script kiddie": "Script Kiddie",

    # Common nouns
    "Firewall": "防火牆",
    "Encryption": "加密",
    "Hashing": "雜湊",
    "Hash": "雜湊",
    "Hashes": "雜湊值",
    "Salting": "加鹽",
    "Certificate": "憑證",
    "Certi cate": "憑證",
    "Digital signature": "數位簽章",
    "Code signing": "程式碼簽章",
    "Backup": "備份",
    "Backups": "備份",
    "Snapshot": "快照",
    "Container": "容器",
    "Containers": "容器",
    "Containerization": "容器化",
    "Virtualization": "虛擬化",
    "VM escape": "VM 逃逸",
    "Serverless": "無伺服器",
    "Serverless framework": "無伺服器框架",
    "Serverless architecture": "無伺服器架構",
    "Microservices": "微服務",
    "Monolithic": "巨型應用",
    "Hot site": "Hot site 熱備站",
    "Warm site": "Warm site 溫備站",
    "Cold site": "Cold site 冷備站",
    "Honeypot": "蜜罐",
    "Honeypots": "蜜罐",
    "Honeyfile": "蜜檔",
    "Honeytoken": "蜜餌",
    "Air-gapped": "氣隙網路",
    "Air gapped": "氣隙網路",
    "Jump server": "跳板伺服器",
    "Jump host": "跳板主機",
    "Bastion host": "堡壘主機",
    "Load balancer": "負載平衡器",
    "Load balancing": "負載平衡",
    "Proxy": "代理",
    "Reverse proxy": "反向代理",
    "Port security": "Port security 連接埠安全",
    "MAC filtering": "MAC 篩選",
    "Segmentation": "網路分段",
    "Network segmentation": "網路分段",
    "Captive portal": "強制門戶",
    "Sandbox": "沙箱",
    "Vulnerability scan": "弱點掃描",
    "Vulnerability assessment": "弱點評估",
    "Penetration test": "滲透測試",
    "Wireshark": "Wireshark",
    "Nessus": "Nessus",
    "Nmap": "Nmap",
    "Tokenization": "代符化",
    "Masking": "資料遮罩",
    "Steganography": "隱寫術",
    "Obfuscation": "程式碼混淆",
    "Geofencing": "地理圍欄",
    "Geolocation": "地理位置",
    "Encryption at rest": "靜態加密",

    # Common acronyms
    "FIM": "FIM 檔案完整性監控",
    "UEBA": "UEBA 使用者行為分析",
    "UBA": "UBA 使用者行為分析",
    "GRE": "GRE 通用路由封裝",
    "STP": "STP",
    "WAF": "WAF Web應用防火牆",

    # Common short words
    "Wired": "有線",
    "Wireless": "無線",
    "Hot": "熱",
    "Warm": "溫",
    "Cold": "冷",
    "True positive": "真陽性",
    "False positive": "誤判 (False Positive)",
    "False negative": "漏報 (False Negative)",
    "True negative": "真陰性",
    "Tuning": "規則調校",
    "Configuration management": "組態管理",
    "Resource consumption": "資源耗盡",
    "Single point of failure": "單點故障 (SPOF)",
    "Reputational damage": "聲譽損害",
    "Impossible travel": "不可能的旅行",
    "Self-signed": "自簽",
    "Wildcard": "萬用字元憑證",
    "Cloud-native": "雲原生",
    "Microsegmentation": "微分段",
}

# Sort phrases and terms by length descending
SORTED_PHRASES = sorted(PHRASE_MAP.items(), key=lambda x: -len(x[0]))
SORTED_TERMS = sorted(TERM_MAP.items(), key=lambda x: -len(x[0]))

# Load comprehensive phrase translations
try:
    from phrase_translations import PHRASE_TRANSLATIONS as EXTRA_PHRASES
except ImportError:
    EXTRA_PHRASES = {}

def clean_input(text):
    """Clean input text"""
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def normalize_for_match(text):
    """Normalize text for matching: lowercase, no trailing period, fix OCR 'fi/ff' ligature drops"""
    text = text.lower().rstrip('.').strip()
    # PDF OCR dropped 'fi' and 'ff' ligatures - restore them
    ocr_fixes = {
        # 'fi' was dropped
        'rewall': 'firewall',
        'rewalls': 'firewalls',
        'certicate': 'certificate',
        'certicates': 'certificates',
        'certication': 'certification',
        'cation': 'fication',  # classification, certification etc - careful
        'cations': 'fications',
        ' lter': ' filter',
        ' ltering': ' filtering',
        ' lters': ' filters',
        ' nd ': ' find ',
        ' nds': ' finds',
        ' nding': ' finding',
        ' eld': ' field',
        ' elds': ' fields',
        ' rst': ' first',
        ' xed': ' fixed',
        ' ne ': ' fine ',
        ' rm ': ' firm ',
        ' rmware': ' firmware',
        ' sh ': ' fish ',
        ' shing': ' shing',  # phishing - careful
        # 'ff' was dropped
        'tra c': 'traffic',
        'sta ': 'staff ',
        'sta\'': 'staff\'',
        'sta.': 'staff.',
        'sta,': 'staff,',
        'sta-': 'staff-',
        ' o ce': ' office',
        ' o cer': ' officer',
        ' o cial': ' official',
        ' a ected': ' affected',
        ' di erent': ' different',
        ' di erence': ' difference',
        ' di culty': ' difficulty',
        ' su cient': ' sufficient',
        ' e ort': ' effort',
        ' e ects': ' effects',
        ' e ect': ' effect',
        ' o er ': ' offer ',
        ' o ers': ' offers',
        # 'fl' dropped sometimes
        ' ow ': ' flow ',
        # 'fi' inside word starts
        'conguration': 'configuration',
        'congurations': 'configurations',
        'conguring': 'configuring',
        'congure': 'configure',
        'congured': 'configured',
        'congures': 'configures',
        'speci c': 'specific',
        'cation': 'fication',
        'classication': 'classification',
        'classications': 'classifications',
        'identi cation': 'identification',
        'identi er': 'identifier',
        'noti cation': 'notification',
        'noti ed': 'notified',
        'noti es': 'notifies',
        'modi ed': 'modified',
        'modi es': 'modifies',
        'modi cation': 'modification',
        'veri ed': 'verified',
        'veri es': 'verifies',
        'veri cation': 'verification',
        'speci ed': 'specified',
        'speci es': 'specifies',
        'speci cation': 'specification',
        'rati ed': 'ratified',
        'simpli ed': 'simplified',
        'simpli es': 'simplifies',
        'unied': 'unified',
        'uni ed': 'unified',
        'identi ed': 'identified',
        'condentiality': 'confidentiality',
        'con dentiality': 'confidentiality',
        'con dential': 'confidential',
        'condential': 'confidential',
        'bene t': 'benefit',
        'bene cial': 'beneficial',
        'pro t': 'profit',
        'overow': 'overflow',
        'over ow': 'overflow',
        'over ows': 'overflows',
        'workow': 'workflow',
        'leless': 'fileless',
        'le-sharing': 'file-sharing',
        ' les': ' files',
        ' le ': ' file ',
        ' le,': ' file,',
        ' le.': ' file.',
        ' le\'s': ' file\'s',
        'rmware': 'firmware',
        'rmly': 'firmly',
    }
    for bad, good in ocr_fixes.items():
        text = text.replace(bad, good)
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text)
    return text

# Pre-compute normalized phrase lookup
NORM_PHRASES = {}
for phrase, trans in EXTRA_PHRASES.items():
    NORM_PHRASES[normalize_for_match(phrase)] = trans

def translate_option(text):
    """Translate an English option to Chinese"""
    if not text or text == "—":
        return text

    text = clean_input(text)
    has_period = text.endswith('.')
    text_no_period = text[:-1] if has_period else text
    norm_text = normalize_for_match(text)

    # 1. Try exact match in comprehensive phrase translations (highest priority)
    if norm_text in NORM_PHRASES:
        return NORM_PHRASES[norm_text]
    # Also try with both fixed forms (rewall→firewall already in NORM_PHRASES side)
    raw_norm = text.lower().rstrip('.').strip()
    raw_norm = re.sub(r'\s+', ' ', raw_norm)
    if raw_norm in NORM_PHRASES:
        return NORM_PHRASES[raw_norm]

    # 2. Try exact phrase match in legacy PHRASE_MAP
    for phrase, trans in SORTED_PHRASES:
        if text_no_period.lower() == phrase.lower().rstrip('.'):
            return trans
        if text.lower() == phrase.lower():
            return trans

    # 3. Try term-only match for short options
    if text_no_period in TERM_MAP:
        return TERM_MAP[text_no_period]

    # 3. For longer text, do phrase replacement first (for partial matches)
    translated = text
    for phrase, trans in SORTED_PHRASES:
        if len(phrase) > 20:  # Only use long phrases for partial match
            translated = re.sub(re.escape(phrase), trans, translated, flags=re.IGNORECASE)

    # 4. Then apply term replacements for remaining English terms
    for en_term, zh_term in SORTED_TERMS:
        pattern = r'\b' + re.escape(en_term) + r'\b'
        translated = re.sub(pattern, zh_term, translated, flags=re.IGNORECASE)

    # 5. Translate common connecting English words
    common_words = {
        r'\bAdd\b': '加入',
        r'\bDocument\b': '記錄',
        r'\bDocumenting\b': '記錄',
        r'\bConfigure\b': '設定',
        r'\bConfiguring\b': '設定',
        r'\bImplement\b': '實施',
        r'\bImplementing\b': '實施',
        r'\bEnable\b': '啟用',
        r'\bEnabling\b': '啟用',
        r'\bDisable\b': '停用',
        r'\bDisabling\b': '停用',
        r'\bRemove\b': '移除',
        r'\bSend\b': '送出',
        r'\bSending\b': '送出',
        r'\bJoin\b': '加入',
        r'\bUpdate\b': '更新',
        r'\bUpdating\b': '更新',
        r'\bTest\b': '測試',
        r'\bTesting\b': '測試',
        r'\bUpgrade\b': '升級',
        r'\bUpgrading\b': '升級',
        r'\bMonitor\b': '監控',
        r'\bMonitoring\b': '監控',
        r'\bReview\b': '檢視',
        r'\bReviewing\b': '檢視',
        r'\bInvestigate\b': '調查',
        r'\bInvestigation\b': '調查',
        r'\bIncrease\b': '提升',
        r'\bIncreasing\b': '提升',
        r'\bDecrease\b': '降低',
        r'\bReduce\b': '降低',
        r'\bReducing\b': '降低',
        r'\bInclude\b': '包含',
        r'\bIncluding\b': '包含',
        r'\bExclude\b': '排除',
        r'\bRequire\b': '要求',
        r'\bRequirement\b': '要求',
        r'\bRequirements\b': '要求',
        r'\bPolicy\b': '政策',
        r'\bPolicies\b': '政策',
        r'\bUser\b': '使用者',
        r'\bUsers\b': '使用者',
        r'\bEmployee\b': '員工',
        r'\bEmployees\b': '員工',
        r'\bAccount\b': '帳號',
        r'\bAccounts\b': '帳號',
        r'\bPassword\b': '密碼',
        r'\bPasswords\b': '密碼',
        r'\bSystem\b': '系統',
        r'\bSystems\b': '系統',
        r'\bServer\b': '伺服器',
        r'\bServers\b': '伺服器',
        r'\bNetwork\b': '網路',
        r'\bDevice\b': '裝置',
        r'\bDevices\b': '裝置',
        r'\bSoftware\b': '軟體',
        r'\bHardware\b': '硬體',
        r'\bData\b': '資料',
        r'\bLog\b': '日誌',
        r'\bLogs\b': '日誌',
        r'\bLogging\b': '記錄',
        r'\bAlert\b': '警報',
        r'\bAlerts\b': '警報',
        r'\bAlerting\b': '告警',
        r'\bReport\b': '報告',
        r'\bReports\b': '報告',
        r'\bReporting\b': '報告',
        r'\bAccess\b': '存取',
        r'\bRemote access\b': '遠端存取',
        r'\bRemote\b': '遠端',
        r'\bLocal\b': '本地',
        r'\bExternal\b': '外部',
        r'\bInternal\b': '內部',
        r'\bDefault\b': '預設',
        r'\bCompany\b': '公司',
        r'\bCustomer\b': '客戶',
        r'\bCustomers\b': '客戶',
        r'\bOrganization\b': '組織',
        r'\bOrganization\'s\b': '組織的',
        r'\bAllow\b': '允許',
        r'\bAllowing\b': '允許',
        r'\bAllowed\b': '允許',
        r'\bDeny\b': '拒絕',
        r'\bDenied\b': '拒絕',
        r'\bBlock\b': '阻擋',
        r'\bBlocking\b': '阻擋',
        r'\bAdded\b': '加入',
        r'\bRemoved\b': '移除',
        r'\bChange\b': '變更',
        r'\bChanged\b': '變更',
        r'\bChanges\b': '變更',
        r'\bChanging\b': '變更',
        r'\bRequest\b': '請求',
        r'\bRequests\b': '請求',
        r'\bRequesting\b': '請求',
        r'\bEnvironment\b': '環境',
        r'\bProduction\b': '生產環境',
        r'\bNon-production\b': '非生產',
        r'\bSignatures\b': '簽章',
        r'\bSignature\b': '簽章',
        r'\bIntrusion prevention\b': '入侵防護',
        r'\bIntrusion detection\b': '入侵偵測',
        r'\bPrior to\b': '在...前',
        r'\bAbove\b': '在...上方',
        r'\bBelow\b': '在...下方',
        r'\bBefore\b': '在...前',
        r'\bAfter\b': '在...後',
    }
    for pattern, replacement in common_words.items():
        translated = re.sub(pattern, replacement, translated, flags=re.IGNORECASE)

    return translated


def translate_all_options():
    """Process all PDF questions and generate option translations"""
    with open("pdf_questions_clean.json", "r", encoding="utf-8") as f:
        pdf_qs = json.load(f)

    translated_opts = {}
    for num_str, q in pdf_qs.items():
        translated_opts[int(num_str)] = [translate_option(opt) for opt in q["options"]]

    with open("translated_options.json", "w", encoding="utf-8") as f:
        json.dump(translated_opts, f, ensure_ascii=False, indent=2)

    print(f"Translated options for {len(translated_opts)} questions")
    return translated_opts


if __name__ == "__main__":
    translate_all_options()
