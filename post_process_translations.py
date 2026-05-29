#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Post-process Google translations to fix:
1. Duplicate words (電子電子郵件 → 電子郵件)
2. Simplified Chinese remnants (forced s2tw conversion)
3. OCR artifacts that translated literally (con guration → 設定)
4. Apply Taiwan-standard technical terms
"""
import json
import re
from opencc import OpenCC

cc = OpenCC('s2tw')


# Duplicate word cleanup patterns
DUPLICATE_FIXES = [
    # "X X" patterns where X is a word that got duplicated
    (r'電子電子郵件', '電子郵件'),
    (r'電子電郵', '電子郵件'),
    (r'郵件郵件', '郵件'),
    (r'資料資料', '資料'),
    (r'資訊資訊', '資訊'),
    (r'伺服伺服器', '伺服器'),
    (r'網路網路', '網路'),
    (r'系統系統', '系統'),
    (r'憑證憑證', '憑證'),
    (r'防火防火牆', '防火牆'),
    # Spacing issues
    (r' +', ''),  # remove extra spaces between Chinese chars (but be careful with EN terms)
]


# OCR artifacts that snuck through (English fragments left in Chinese)
OCR_ARTIFACTS = [
    # "con guration" (config with dropped fi) translated to Chinese leaves "con" or weird mix
    (r'con guration', '設定'),
    (r'con guring', '設定'),
    (r'con gure', '設定'),
    (r'con gured', '已設定'),
    (r'防火牆 con guration', '防火牆設定'),
    (r'防火牆配置', '防火牆設定'),
    # OCR artifacts that translation didn't fix
    (r'網路 tra c', '網路流量'),
    (r'tra c', '流量'),
    (r'rewall', '防火牆'),
    (r'over ow', '溢位'),
    (r'overow', '溢位'),
    # Mainland Chinese terms that opencc may miss
    (r'遠程', '遠端'),
    (r'臺', '台'),  # Taiwan uses 台 more commonly in modern usage
    (r'配置', '設定'),  # Mainland uses 配置, Taiwan uses 設定 for "configure"
]


# Cleanup duplicate trailing parentheticals like "X (Y) (Y)" → "X (Y)"
def cleanup_duplicate_parens(text):
    """Remove duplicate parentheticals (with or without space between)"""
    # Repeat until stable - handle chains like "(X)(X)(X)" or "(X) (X) (X)"
    for _ in range(5):
        prev = text
        # Pattern: "(X) (X)" with space → "(X)"
        text = re.sub(r'\(([^()]+)\) \(\1\)', r'(\1)', text)
        # Pattern: "(X)(X)" without space → "(X)"
        text = re.sub(r'\(([^()]+)\)\(\1\)', r'(\1)', text)
        if text == prev:
            break
    return text


# Technical term standardization (Taiwan industry standard)
TERM_STANDARDIZE = [
    # Map Simplified or alternate translations to Taiwan standard
    (r'結構化查詢語言注入', 'SQL 注入'),
    (r'結構化查詢語言', 'SQL'),
    (r'資料庫錯誤配置', '資料庫錯誤設定'),
    (r'錯誤配置', '錯誤設定'),
    # Force s2tw for any remaining mainland terms
    (r'網絡', '網路'),
    (r'信息', '資訊'),
    (r'軟件', '軟體'),
    (r'硬件', '硬體'),
    (r'數據庫', '資料庫'),
    (r'數據', '資料'),
    (r'用戶', '使用者'),
    (r'賬號', '帳號'),
    (r'賬戶', '帳號'),
    (r'端口', '連接埠'),
    (r'內存', '記憶體'),
    (r'存儲', '儲存'),
    (r'計算機', '電腦'),
    (r'服務器', '伺服器'),
    (r'登錄', '登入'),
    (r'鏈接', '連結'),
    (r'防火墻', '防火牆'),
    (r'墻', '牆'),
    (r'磁盤', '磁碟'),
    (r'硬盤', '硬碟'),
    (r'文件', '檔案'),
    (r'視頻', '影片'),
    (r'移動設備', '行動裝置'),
    (r'移動裝置', '行動裝置'),
    (r'多因素身份驗證', '多因素驗證 (MFA)'),
    (r'雙因素身份驗證', '雙因素驗證 (2FA)'),
    (r'單點登入', '單一登入 (SSO)'),
    (r'單點登錄', '單一登入 (SSO)'),
    (r'勒索軟件', '勒索軟體 (Ransomware)'),
    (r'惡意軟件', '惡意軟體 (Malware)'),
    (r'下一代防火牆', '次世代防火牆 (NGFW)'),
    (r'災難復原', '災害復原'),
    (r'災難恢復', '災害復原'),
    (r'業務連續性', '業務持續性'),
    (r'桌面演練', '桌上演練 (Tabletop)'),
    (r'桌面練習', '桌上演練 (Tabletop)'),
    (r'紅色團隊', '紅隊'),
    (r'藍色團隊', '藍隊'),
    (r'紫色團隊', '紫隊'),
    (r'公開金鑰基礎建設', 'PKI 公開金鑰基礎設施'),
    (r'公鑰基礎結構', 'PKI 公開金鑰基礎設施'),
    (r'公鑰基礎設施', 'PKI 公開金鑰基礎設施'),
    (r'公共金鑰基礎設施', 'PKI 公開金鑰基礎設施'),
    (r'公共金鑰基礎建設', 'PKI 公開金鑰基礎設施'),
    (r'公共密鑰基礎設施', 'PKI 公開金鑰基礎設施'),
    (r'憑證取消清單', 'CRL 憑證撤銷清單'),
    (r'憑證撤銷清單', 'CRL 憑證撤銷清單'),
    (r'網路存取控制', 'NAC 網路存取控制'),
    (r'網路位址轉換', 'NAT 網路位址轉換'),
    (r'最小特權', '最小權限'),
    (r'最小特權原則', '最小權限原則 (Least Privilege)'),
    (r'最小權限原則', '最小權限原則 (Least Privilege)'),
    (r'職責分離', '職責分離 (Separation of Duties)'),
    (r'存取控制清單', 'ACL 存取控制清單'),
    (r'特權存取管理', 'PAM 特權存取管理'),
    (r'威脅獵捕', '威脅獵捕 (Threat Hunting)'),
    (r'威脅情報', '威脅情報 (Threat Intelligence)'),
    (r'通用漏洞評分系統', 'CVSS 漏洞評分系統'),
    (r'通用漏洞識別碼', 'CVE 通用漏洞編號'),
    (r'駭客主義者', '駭客主義者 (Hacktivist)'),
    (r'黑客主義者', '駭客主義者 (Hacktivist)'),
    (r'激進駭客', '駭客主義者 (Hacktivist)'),
    (r'激進黑客', '駭客主義者 (Hacktivist)'),
    (r'組織犯罪', '組織犯罪集團 (Organized Crime)'),
    (r'有組織犯罪', '組織犯罪集團 (Organized Crime)'),
    (r'民族國家', '民族國家 (Nation-State)'),
    (r'國家行為者', '民族國家 (Nation-State)'),
    (r'國家級行為者', '民族國家 (Nation-State)'),
    (r'內部威脅', '內部威脅 (Insider Threat)'),
    (r'告密者', '吹哨者 (Whistleblower)'),
    (r'吹哨者', '吹哨者 (Whistleblower)'),
    (r'勒索軟體即服務', 'Ransomware-as-a-Service (RaaS)'),
    (r'商業電子郵件入侵', 'BEC 商業電郵入侵'),
    (r'商業電郵入侵', 'BEC 商業電郵入侵'),
    (r'語音釣魚', '語音釣魚 (Vishing)'),
    (r'簡訊釣魚', '簡訊釣魚 (Smishing)'),
    (r'魚叉式釣魚', '魚叉式釣魚 (Spear Phishing)'),
    (r'網路釣魚', '釣魚 (Phishing)'),
    (r'網絡釣魚', '釣魚 (Phishing)'),
    (r'尾隨', '尾隨進入 (Tailgating)'),
    (r'肩窺', '肩窺 (Shoulder Surfing)'),
    (r'垃圾箱潛水', '翻垃圾蒐情 (Dumpster Diving)'),
    (r'冒充', '冒充 (Impersonation)'),
    (r'假借身分', '假借身分 (Pretexting)'),
    (r'假借身份', '假借身分 (Pretexting)'),
    (r'錯字搶註', '錯字搶註 (Typosquatting)'),
    (r'域名搶註', '錯字搶註 (Typosquatting)'),
    (r'水坑攻擊', '水坑攻擊 (Watering Hole)'),
    (r'蠻力攻擊', '蠻力破解 (Brute Force)'),
    (r'蠻力破解', '蠻力破解 (Brute Force)'),
    (r'暴力破解', '蠻力破解 (Brute Force)'),
    (r'字典攻擊', '字典攻擊 (Dictionary Attack)'),
    (r'密碼噴灑', '密碼噴灑 (Password Spraying)'),
    (r'憑證填充', '憑證填充 (Credential Stuffing)'),
    (r'憑證收集', '憑證收集 (Credential Harvesting)'),
    (r'重放攻擊', '重放攻擊 (Replay Attack)'),
    (r'會話劫持', '會話劫持 (Session Hijacking)'),
    (r'目錄遍歷', '目錄遍歷 (Directory Traversal)'),
    (r'命令注入', '命令注入 (Command Injection)'),
    (r'記憶體注入', '記憶體注入 (Memory Injection)'),
    (r'緩衝區溢出', '緩衝區溢位'),
    (r'緩衝區溢位', '緩衝區溢位 (Buffer Overflow)'),
    (r'中間人攻擊', '中間人攻擊 (MITM)'),
    (r'路徑攻擊', '中間人攻擊 (On-Path)'),
    (r'路徑上攻擊', '中間人攻擊 (On-Path)'),
    (r'反射型阻斷服務', '反射型 DoS (Reflected DoS)'),
    (r'反射拒絕服務', '反射型 DoS (Reflected DoS)'),
    (r'DNS 投毒', 'DNS 投毒 (DNS Poisoning)'),
    (r'DNS 中毒', 'DNS 投毒 (DNS Poisoning)'),
    (r'DNS 黑洞', 'DNS 黑洞 (DNS Sinkhole)'),
    (r'數位鑑識', '數位鑑識 (Forensics)'),
    (r'證據鏈', '證據鏈 (Chain of Custody)'),
    (r'監管鏈', '證據鏈 (Chain of Custody)'),
    (r'資料淨化', '資料淨化 (Sanitization)'),
    (r'數據清理', '資料淨化 (Sanitization)'),
    (r'資料分類', '資料分類 (Classification)'),
    (r'代符化', '代符化 (Tokenization)'),
    (r'資料遮罩', '資料遮罩 (Masking)'),
    (r'隱寫術', '隱寫術 (Steganography)'),
    (r'程式碼混淆', '程式碼混淆 (Obfuscation)'),
    (r'代碼混淆', '程式碼混淆 (Obfuscation)'),
    (r'加鹽', '加鹽 (Salting)'),
    (r'金鑰延展', '金鑰延展 (Key Stretching)'),
    (r'金鑰託管', '金鑰託管 (Key Escrow)'),
    (r'全磁碟加密', '全磁碟加密 (FDE)'),
    (r'全盤加密', '全磁碟加密 (FDE)'),
    (r'非對稱式加密', '非對稱式加密 (Asymmetric)'),
    (r'對稱式加密', '對稱式加密 (Symmetric)'),
    (r'雜湊運算', '雜湊 (Hashing)'),
    (r'雜湊', '雜湊 (Hashing)'),
    (r'氣隙網絡', '氣隙網路'),
    (r'氣隙網路', '氣隙網路 (Air Gap)'),
    (r'物理隔離網路', '氣隙網路 (Air Gap)'),
    (r'跳板伺服器', '跳板伺服器 (Jump Server)'),
    (r'跳板主機', '跳板主機 (Jump Host)'),
    (r'堡壘主機', '堡壘主機 (Bastion Host)'),
    (r'蜜罐', '蜜罐 (Honeypot)'),
    (r'蜜檔', '蜜檔 (Honeyfile)'),
    (r'連接埠安全', '連接埠安全 (Port Security)'),
    (r'網路分段', '網路分段 (Segmentation)'),
    (r'微分段', '微分段 (Microsegmentation)'),
    (r'容器化', '容器化 (Containerization)'),
    (r'虛擬化', '虛擬化 (Virtualization)'),
    (r'微服務', '微服務 (Microservices)'),
    (r'無伺服器', '無伺服器 (Serverless)'),
    (r'基礎設施即代碼', 'IaC 基礎設施即程式碼'),
    (r'基礎設施即程式碼', 'IaC 基礎設施即程式碼'),
    (r'基礎建設即程式碼', 'IaC 基礎設施即程式碼'),
    (r'業務影響分析', 'BIA 業務影響分析'),
    (r'業務持續性計畫', 'BCP 業務持續性計畫'),
    (r'業務持續性計劃', 'BCP 業務持續性計畫'),
    (r'災害復原計畫', 'DRP 災害復原計畫'),
    (r'災害復原計劃', 'DRP 災害復原計畫'),
    (r'災難復原計劃', 'DRP 災害復原計畫'),
    (r'災難恢復計劃', 'DRP 災害復原計畫'),
    (r'恢復時間目標', 'RTO 恢復時間目標'),
    (r'恢復點目標', 'RPO 恢復點目標'),
    (r'年度預期損失', 'ALE 年度預期損失'),
    (r'年度發生率', 'ARO 年度發生率'),
    (r'單次損失預期', 'SLE 單次損失預期'),
    (r'平均故障間隔', 'MTBF 平均故障間隔'),
    (r'平均修復時間', 'MTTR 平均修復時間'),
    (r'技術不熟練的攻擊者', '技術不熟練攻擊者 (Unskilled Attacker)'),
    (r'技術不熟練攻擊者', '技術不熟練攻擊者 (Unskilled Attacker)'),
    (r'不熟練的攻擊者', '技術不熟練攻擊者 (Unskilled Attacker)'),
    (r'業餘攻擊者', '技術不熟練攻擊者 (Unskilled Attacker)'),
    (r'腳本小子', 'Script Kiddie 技術不熟者'),
    (r'影子 IT', '影子 IT (Shadow IT)'),
    (r'影子資訊技術', '影子 IT (Shadow IT)'),
    (r'高級持續威脅', 'APT 進階持續性威脅'),
    (r'進階持續威脅', 'APT 進階持續性威脅'),
    (r'進階持續性威脅', 'APT 進階持續性威脅'),
    (r'高級持續性威脅', 'APT 進階持續性威脅'),
    (r'網路安全營運中心', 'SOC 安全運營中心'),
    (r'安全營運中心', 'SOC 安全運營中心'),
    (r'安全運營中心', 'SOC 安全運營中心'),
    (r'統一威脅管理', 'UTM 統合威脅管理'),
    (r'統合威脅管理', 'UTM 統合威脅管理'),
    (r'即時作業系統', 'RTOS 即時作業系統'),
    (r'物聯網', 'IoT 物聯網'),
    (r'工業控制系統', 'ICS 工業控制系統'),
    (r'自帶裝置', 'BYOD 自帶裝置'),
    (r'自帶設備', 'BYOD 自帶裝置'),
    (r'越獄', '越獄 (Jailbreaking)'),
    (r'旁路安裝', 'Side-loading 旁路安裝'),
    (r'側載', 'Side-loading 旁路安裝'),
    (r'側通道攻擊', '側通道攻擊 (Side-Channel)'),
    (r'側信道攻擊', '側通道攻擊 (Side-Channel)'),
    (r'入侵指標', 'IOC 入侵指標'),
    (r'安全資訊與事件管理', 'SIEM'),
    (r'安全資訊事件管理', 'SIEM'),
    (r'安全編排與自動化回應', 'SOAR'),
    (r'安全編排與自動化響應', 'SOAR'),
    (r'安全編排自動化回應', 'SOAR'),
    (r'端點偵測與回應', 'EDR'),
    (r'端點偵測回應', 'EDR'),
    (r'資料外洩防護', 'DLP'),
    (r'資料丟失防護', 'DLP'),
    (r'行動裝置管理', 'MDM'),
    (r'使用者行為分析', 'UEBA'),
    (r'使用者及實體行為分析', 'UEBA'),
    (r'網路應用程式防火牆', 'WAF Web 應用防火牆'),
    (r'網路應用防火牆', 'WAF Web 應用防火牆'),
    (r'Web 應用程式防火牆', 'WAF Web 應用防火牆'),
    (r'Web 應用防火牆', 'WAF Web 應用防火牆'),
    (r'入侵偵測系統', 'IDS 入侵偵測'),
    (r'入侵防護系統', 'IPS 入侵防護'),
    (r'入侵防禦系統', 'IPS 入侵防護'),
    (r'網域名稱系統', 'DNS'),
    (r'動態主機配置協定', 'DHCP'),
    (r'動態主機設定協定', 'DHCP'),
    (r'安全存取服務邊緣', 'SASE'),
    (r'軟體定義廣域網路', 'SD-WAN'),
    (r'軟體定義廣域網', 'SD-WAN'),
    (r'雲端存取安全代理', 'CASB'),
    (r'零信任網路存取', 'ZTNA 零信任網路存取'),
    (r'零信任', '零信任 (Zero Trust)'),
    (r'硬體安全模組', 'HSM 硬體安全模組'),
    (r'受信任平台模組', 'TPM'),
    (r'可信平台模組', 'TPM'),
    (r'時間型一次性密碼', 'TOTP 時間型一次性密碼'),
    (r'一次性密碼', 'OTP 一次性密碼'),
    (r'數位簽章', '數位簽章 (Digital Signature)'),
    (r'程式碼簽章', '程式碼簽章 (Code Signing)'),
    (r'憑證簽署請求', 'CSR 憑證簽署請求'),
    (r'線上憑證狀態', 'OCSP'),
    (r'憑證信任根', '信任根 (Root of Trust)'),
    (r'信任根', '信任根 (Root of Trust)'),
    (r'場勘', '場勘 (Site Survey)'),
    (r'場地勘查', '場勘 (Site Survey)'),
    (r'故障切換', '故障切換 (Failover)'),
    (r'故障轉移', '故障切換 (Failover)'),
    (r'熱備站', '熱備站 (Hot Site)'),
    (r'溫備站', '溫備站 (Warm Site)'),
    (r'冷備站', '冷備站 (Cold Site)'),
    (r'快照', '快照 (Snapshot)'),
    (r'地理分散', '地理分散 (Geographic Dispersion)'),
    (r'地理分布', '地理分散 (Geographic Dispersion)'),
    (r'準備階段', '準備階段 (Preparation)'),
    (r'遏制階段', '遏制階段 (Containment)'),
    (r'根除階段', '根除階段 (Eradication)'),
    (r'復原階段', '復原階段 (Recovery)'),
    (r'經驗教訓', '經驗教訓 (Lessons Learned)'),
    (r'法律保留', '法律保留 (Legal Hold)'),
    (r'資料保留', '資料保留 (Retention)'),
    (r'資料所有者', '資料所有者 (Data Owner)'),
    (r'資料保管者', '資料保管者 (Data Custodian)'),
    (r'資料控制者', '資料控制者 (Data Controller)'),
    (r'資料處理者', '資料處理者 (Data Processor)'),
    (r'資料主權', '資料主權 (Data Sovereignty)'),
    (r'資料駐留', '資料駐留 (Data Residency)'),
    (r'個人識別資訊', 'PII 個人識別資訊'),
    (r'受保護健康資訊', 'PHI 受保護健康資訊'),
    (r'盡職調查', '盡職調查 (Due Diligence)'),
    (r'盡職保密', '盡職保密 (Due Care)'),
    (r'差距分析', '差距分析 (Gap Analysis)'),
    (r'稽核權', '稽核權 (Right to Audit)'),
    (r'保密協議', 'NDA 保密協議'),
    (r'保密協定', 'NDA 保密協議'),
    (r'服務水準協議', 'SLA 服務水準協議'),
    (r'服務等級協議', 'SLA 服務水準協議'),
    (r'工作說明書', 'SOW 工作說明書'),
    (r'主服務協議', 'MSA 主服務協議'),
    (r'諒解備忘錄', 'MOU 諒解備忘錄'),
    (r'業務合作協議', 'BPA 業務合作協議'),
    (r'交戰守則', '交戰守則 (Rules of Engagement)'),
    (r'紅隊演練', '紅隊演練 (Red Team)'),
    (r'藍隊演練', '藍隊演練 (Blue Team)'),
    (r'紫隊演練', '紫隊演練 (Purple Team)'),
    (r'桌上演練', '桌上演練 (Tabletop)'),
    (r'漏洞獎金計畫', '漏洞獎金計畫 (Bug Bounty)'),
    (r'漏洞獎金', '漏洞獎金計畫 (Bug Bounty)'),
    (r'滲透測試', '滲透測試 (Penetration Test)'),
    (r'弱點掃描', '弱點掃描 (Vulnerability Scan)'),
    (r'弱點評估', '弱點評估 (Vulnerability Assessment)'),
    (r'漏洞掃描', '弱點掃描 (Vulnerability Scan)'),
    (r'漏洞評估', '弱點評估 (Vulnerability Assessment)'),
    (r'安全意識訓練', '安全意識訓練 (Security Awareness Training)'),
    (r'安全意識培訓', '安全意識訓練 (Security Awareness Training)'),
    (r'可接受使用政策', 'AUP 可接受使用政策'),
    (r'可接受使用原則', 'AUP 可接受使用政策'),
    (r'事件回應計畫', 'IRP 事件回應計畫'),
    (r'事件回應計劃', 'IRP 事件回應計畫'),
    (r'事件回應', '事件回應 (Incident Response)'),
    (r'變更管理', '變更管理 (Change Management)'),
    (r'變更控制', '變更控制 (Change Control)'),
    (r'回退計畫', '回退計畫 (Backout Plan)'),
    (r'回退計劃', '回退計畫 (Backout Plan)'),
    (r'維護時段', '維護時段 (Maintenance Window)'),
    (r'標準作業程序', 'SOP 標準作業程序'),
    (r'生命終期', '生命終期 (End of Life)'),
    (r'結束支援', '結束支援 (End of Support)'),
    (r'舊系統', '舊系統 (Legacy)'),
    (r'除役', '除役 (Decommissioning)'),
    (r'強化', '強化 (Hardening)'),
    (r'修補', '修補 (Patching)'),
    (r'基準', '基準 (Baseline)'),
    (r'規則調校', '規則調校 (Tuning)'),
    (r'誤判', '誤判 (False Positive)'),
    (r'漏報', '漏報 (False Negative)'),
    (r'剩餘風險', '剩餘風險 (Residual Risk)'),
    (r'固有風險', '固有風險 (Inherent Risk)'),
    (r'風險登記簿', '風險登記簿 (Risk Register)'),
    (r'風險矩陣', '風險矩陣 (Risk Matrix)'),
    (r'風險偏好', '風險偏好 (Risk Appetite)'),
    (r'風險容忍度', '風險容忍度 (Risk Tolerance)'),
    (r'風險門檻', '風險門檻 (Risk Threshold)'),
    (r'風險減緩', '風險減緩 (Mitigation)'),
    (r'風險接受', '風險接受 (Acceptance)'),
    (r'風險規避', '風險規避 (Avoidance)'),
    (r'風險轉移', '風險轉移 (Transfer)'),
    (r'單點故障', '單點故障 (SPOF)'),
    (r'單一故障點', '單點故障 (SPOF)'),
    (r'不可能的旅行', '不可能的旅行 (Impossible Travel)'),
    (r'條件式存取', '條件式存取 (Conditional Access)'),
    (r'條件存取', '條件式存取 (Conditional Access)'),
    (r'可信裝置', '可信裝置 (Trusted Devices)'),
    (r'即時存取', '即時權限 (Just-in-Time)'),
    (r'時段限制', '時段限制 (Time-of-Day)'),
    (r'時間型存取控制', '時間型存取控制 (Time-Based)'),
    (r'端點防護', '端點防護 (Endpoint Protection)'),
    (r'主機型防火牆', '主機型防火牆 (Host-based Firewall)'),
    (r'狀態檢查防火牆', '狀態檢查防火牆 (Stateful)'),
    (r'下一代 SIEM', '次世代 SIEM'),
    (r'監督控制和資料獲取', 'SCADA'),
    (r'監督和資料擷取', 'SCADA'),
    (r'監督與資料擷取', 'SCADA'),
]


def cleanup_duplicates(text):
    """Remove duplicate words like 電子電子郵件"""
    for pattern, replacement in DUPLICATE_FIXES:
        text = re.sub(pattern, replacement, text)
    return text


def fix_ocr_artifacts(text):
    """Fix OCR artifacts that snuck through"""
    for pattern, replacement in OCR_ARTIFACTS:
        text = re.sub(pattern, replacement, text)
    return text


def standardize(text):
    """Apply Taiwan-standard technical terms"""
    for pattern, replacement in TERM_STANDARDIZE:
        text = re.sub(pattern, replacement, text)
    # Remove duplicate parentheticals like "X (X)"
    for _ in range(3):  # Multiple passes for nested duplicates
        text = re.sub(r'([一-鿿\w]+(?: [一-鿿\w]+)*) \(\1\)', r'\1', text)
    # Remove "X (X" patterns (open paren but no close)
    return text


def process_translation(zh_text):
    """Full post-processing pipeline"""
    if not zh_text:
        return zh_text
    # Step 1: Force s2tw conversion (in case Google returned Simplified)
    zh_text = cc.convert(zh_text)
    # Step 2: Clean up duplicates
    zh_text = cleanup_duplicates(zh_text)
    # Step 3: Fix OCR artifacts in Chinese
    zh_text = fix_ocr_artifacts(zh_text)
    # Step 4: Standardize technical terms
    zh_text = standardize(zh_text)
    # Step 5: Remove duplicate parentheticals
    zh_text = cleanup_duplicate_parens(zh_text)
    return zh_text


def main():
    with open("google_translated_questions.json", "r", encoding="utf-8") as f:
        cache = json.load(f)

    print(f"Processing {len(cache)} translations...")

    for num_str, data in cache.items():
        # Always start from zh_raw (original Google output) for idempotency
        source = data.get("zh_raw") or data.get("zh", "")
        data["zh"] = process_translation(source)

    with open("google_translated_questions.json", "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

    print(f"Done! Updated {len(cache)} translations")


if __name__ == "__main__":
    main()
