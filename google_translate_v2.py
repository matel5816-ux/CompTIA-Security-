#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch translate via googletrans (Google's free web API)
Returns Traditional Chinese directly (no opencc conversion needed)
"""
import json
import re
import os
import asyncio
import time
from googletrans import Translator


# OCR fixes with regex word boundaries (avoid false positives)
OCR_FIXES = [
    # Specific multi-word patterns
    (r'\boutbound tra c\b', 'outbound traffic'),
    (r'\binbound tra c\b', 'inbound traffic'),
    (r'\bnetwork tra c\b', 'network traffic'),
    (r'\bDNS tra c\b', 'DNS traffic'),
    (r'\bweb tra c\b', 'web traffic'),
    (r'\bemail tra c\b', 'email traffic'),
    (r'\bencrypted tra c\b', 'encrypted traffic'),
    (r'\bmalicious tra c\b', 'malicious traffic'),
    (r'\boutgoing tra c\b', 'outgoing traffic'),
    (r'\bincoming tra c\b', 'incoming traffic'),
    (r'\ball tra c\b', 'all traffic'),
    (r'\bthe tra c\b', 'the traffic'),
    # Standalone OCR-broken words
    (r'\bmiscongurations\b', 'misconfigurations'),
    (r'\bmisconguration\b', 'misconfiguration'),
    (r'\bconguring\b', 'configuring'),
    (r'\bconguration\b', 'configuration'),
    (r'\bcongurations\b', 'configurations'),
    (r'\bcongure\b', 'configure'),
    (r'\bcongured\b', 'configured'),
    (r'\bcongures\b', 'configures'),
    (r'\brewall\b', 'firewall'),
    (r'\brewalls\b', 'firewalls'),
    (r'\bcerticate\b', 'certificate'),
    (r'\bcerticates\b', 'certificates'),
    (r'\bclassication\b', 'classification'),
    (r'\bclassications\b', 'classifications'),
    (r'\bidentication\b', 'identification'),
    (r'\bnotication\b', 'notification'),
    (r'\bspecication\b', 'specification'),
    (r'\bverication\b', 'verification'),
    (r'\bunied\b', 'unified'),
    (r'\bcondentiality\b', 'confidentiality'),
    (r'\bcondential\b', 'confidential'),
    (r'\boverow\b', 'overflow'),
    (r'\boverows\b', 'overflows'),
    (r'\bworkow\b', 'workflow'),
    (r'\bworkows\b', 'workflows'),
    (r'\brmware\b', 'firmware'),
    (r'\bleless\b', 'fileless'),
    (r'\bspoong\b', 'spoofing'),
    (r'\bngerprint\b', 'fingerprint'),
    (r'\bngerprints\b', 'fingerprints'),
    (r'\bndings\b', 'findings'),
    (r'\bexltrated\b', 'exfiltrated'),
    (r'\bexltration\b', 'exfiltration'),
    (r'\bsimplied\b', 'simplified'),
    # Multi-word ff patterns
    (r'\bo ce\b', 'office'),
    (r'\ba ected\b', 'affected'),
    (r'\bdi erent\b', 'different'),
    (r'\bdi erence\b', 'difference'),
    (r'\be ort\b', 'effort'),
    (r'\be ect\b', 'effect'),
    (r'\bo er\b', 'offer'),
    (r'\bsta member\b', 'staff member'),
    (r'\bsta members\b', 'staff members'),
    # Context-specific fi fixes
    (r'\bight at\b', 'flight at'),
    (r'\bash drive\b', 'flash drive'),
    (r'\bnd the\b', 'find the'),
    (r'\bnd a\b', 'find a'),
    (r'\bnd an\b', 'find an'),
    (r'\bnds\b', 'finds'),
    (r'\bnding\b', 'finding'),
    (r'\brst\b', 'first'),
    (r'\beld\b', 'field'),
    (r'\belds\b', 'fields'),
    (r'\blter\b', 'filter'),
    (r'\bltering\b', 'filtering'),
    (r'\blters\b', 'filters'),
    (r'\bles\b', 'files'),
]


def fix_ocr(text):
    """Restore OCR-dropped fi/ff ligatures using regex with word boundaries"""
    for pattern, replacement in OCR_FIXES:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text


# Technical term standardization to match Taiwan industry standards
TERM_STANDARDIZE = [
    (r'結構化查詢語言注入', 'SQL 注入'),
    (r'結構化查詢語言', 'SQL'),
    (r'結構化查詢', 'SQL'),
    (r'跨站腳本攻擊', 'XSS 跨站腳本'),
    (r'跨站腳本', 'XSS 跨站腳本'),
    (r'跨站請求偽造', 'CSRF 跨站請求偽造'),
    (r'緩衝區溢出', '緩衝區溢位'),
    (r'網絡釣魚', '釣魚 (Phishing)'),
    (r'網路釣魚', '釣魚 (Phishing)'),
    (r'魚叉式釣魚', '魚叉式釣魚 (Spear Phishing)'),
    (r'語音釣魚', '語音釣魚 (Vishing)'),
    (r'簡訊釣魚', '簡訊釣魚 (Smishing)'),
    (r'簡訊網絡釣魚', '簡訊釣魚 (Smishing)'),
    (r'多因素身份驗證', '多因素驗證 (MFA)'),
    (r'多因素認證', '多因素驗證 (MFA)'),
    (r'雙因素身份驗證', '雙因素驗證 (2FA)'),
    (r'雙重身份驗證', '雙因素驗證 (2FA)'),
    (r'單點登入', '單一登入 (SSO)'),
    (r'單一登錄', '單一登入 (SSO)'),
    (r'勒索軟件', '勒索軟體 (Ransomware)'),
    (r'惡意軟件', '惡意軟體 (Malware)'),
    (r'入侵偵測系統', 'IDS 入侵偵測'),
    (r'入侵防禦系統', 'IPS 入侵防護'),
    (r'入侵防護系統', 'IPS 入侵防護'),
    (r'下一代防火牆', '次世代防火牆 (NGFW)'),
    (r'端點偵測與回應', 'EDR 端點偵測回應'),
    (r'安全資訊與事件管理', 'SIEM'),
    (r'資料外洩防護', 'DLP 資料外洩防護'),
    (r'資料丟失防護', 'DLP'),
    (r'災難復原', '災害復原'),
    (r'業務連續性', '業務持續性'),
    (r'零信任', '零信任 (Zero Trust)'),
    (r'桌面演練', '桌上演練 (Tabletop)'),
    (r'桌上練習', '桌上演練 (Tabletop)'),
    (r'紅色團隊', '紅隊'),
    (r'藍色團隊', '藍隊'),
    (r'紫色團隊', '紫隊'),
    (r'證據鏈', '證據鏈 (Chain of Custody)'),
    (r'監管鏈', '證據鏈 (Chain of Custody)'),
    (r'數位鑑識', '數位鑑識 (Forensics)'),
    (r'資料淨化', '資料淨化 (Sanitization)'),
    (r'資料清理', '資料淨化 (Sanitization)'),
    (r'數據清理', '資料淨化 (Sanitization)'),
    (r'代符化', '代符化 (Tokenization)'),
    (r'資料遮罩', '資料遮罩 (Masking)'),
    (r'數據遮罩', '資料遮罩 (Masking)'),
    (r'隱寫術', '隱寫術 (Steganography)'),
    (r'程式碼混淆', '程式碼混淆 (Obfuscation)'),
    (r'代碼混淆', '程式碼混淆 (Obfuscation)'),
    (r'加鹽', '加鹽 (Salting)'),
    (r'金鑰延展', '金鑰延展 (Key Stretching)'),
    (r'金鑰託管', '金鑰託管 (Key Escrow)'),
    (r'公開金鑰基礎建設', 'PKI 公開金鑰基礎設施'),
    (r'公開金鑰基礎設施', 'PKI 公開金鑰基礎設施'),
    (r'憑證撤銷清單', 'CRL 憑證撤銷清單'),
    (r'憑證簽署請求', 'CSR 憑證簽署請求'),
    (r'全磁碟加密', '全磁碟加密 (FDE)'),
    (r'全盤加密', '全磁碟加密 (FDE)'),
    (r'磁碟加密', '全磁碟加密 (FDE)'),
    (r'非對稱加密', '非對稱式加密'),
    (r'非對稱式加密', '非對稱式加密 (Asymmetric)'),
    (r'對稱加密', '對稱式加密'),
    (r'對稱式加密', '對稱式加密 (Symmetric)'),
    (r'雜湊運算', '雜湊 (Hashing)'),
    (r'網路存取控制', 'NAC 網路存取控制'),
    (r'網絡存取控制', 'NAC 網路存取控制'),
    (r'網路位址轉換', 'NAT 網路位址轉換'),
    (r'網路分段', '網路分段 (Segmentation)'),
    (r'網絡分段', '網路分段 (Segmentation)'),
    (r'微分段', '微分段 (Microsegmentation)'),
    (r'氣隙網絡', '氣隙網路'),
    (r'氣隙', '氣隙 (Air Gap)'),
    (r'跳板伺服器', '跳板伺服器 (Jump Server)'),
    (r'跳板主機', '跳板主機 (Jump Host)'),
    (r'堡壘主機', '堡壘主機 (Bastion Host)'),
    (r'蜜罐', '蜜罐 (Honeypot)'),
    (r'蜜檔', '蜜檔 (Honeyfile)'),
    (r'端口安全', '連接埠安全 (Port Security)'),
    (r'連接埠安全', '連接埠安全 (Port Security)'),
    (r'蠻力攻擊', '蠻力破解 (Brute Force)'),
    (r'暴力破解', '蠻力破解 (Brute Force)'),
    (r'字典攻擊', '字典攻擊 (Dictionary Attack)'),
    (r'密碼噴灑', '密碼噴灑 (Password Spraying)'),
    (r'憑證填充', '憑證填充 (Credential Stuffing)'),
    (r'憑證收集', '憑證收集 (Credential Harvesting)'),
    (r'重放攻擊', '重放攻擊 (Replay Attack)'),
    (r'回放攻擊', '重放攻擊 (Replay Attack)'),
    (r'會話劫持', '會話劫持 (Session Hijacking)'),
    (r'DNS 投毒', 'DNS 投毒 (DNS Poisoning)'),
    (r'DNS 中毒', 'DNS 投毒'),
    (r'DNS 黑洞', 'DNS 黑洞 (DNS Sinkhole)'),
    (r'錯字搶註', '錯字搶註 (Typosquatting)'),
    (r'域名搶註', '錯字搶註 (Typosquatting)'),
    (r'目錄遍歷', '目錄遍歷 (Directory Traversal)'),
    (r'命令注入', '命令注入 (Command Injection)'),
    (r'記憶體注入', '記憶體注入 (Memory Injection)'),
    (r'側通道攻擊', '側通道攻擊 (Side-Channel)'),
    (r'側信道攻擊', '側通道攻擊 (Side-Channel)'),
    (r'中間人攻擊', '中間人攻擊 (MITM)'),
    (r'路徑攻擊', '中間人攻擊 (On-Path)'),
    (r'路徑上攻擊', '中間人攻擊 (On-Path)'),
    (r'反射拒絕服務', '反射型 DoS (Reflected DoS)'),
    (r'反射型阻斷服務', '反射型 DoS (Reflected DoS)'),
    (r'駭客主義者', '駭客主義者 (Hacktivist)'),
    (r'黑客主義者', '駭客主義者 (Hacktivist)'),
    (r'激進駭客', '駭客主義者 (Hacktivist)'),
    (r'激進黑客', '駭客主義者 (Hacktivist)'),
    (r'組織犯罪', '組織犯罪集團 (Organized Crime)'),
    (r'有組織犯罪', '組織犯罪集團 (Organized Crime)'),
    (r'民族國家', '民族國家 (Nation-State)'),
    (r'內部威脅', '內部威脅 (Insider Threat)'),
    (r'吹哨者', '吹哨者 (Whistleblower)'),
    (r'告密者', '吹哨者 (Whistleblower)'),
    (r'技術不熟練的攻擊者', '技術不熟練攻擊者 (Unskilled Attacker)'),
    (r'腳本小子', 'Script Kiddie 技術不熟者'),
    (r'影子 IT', '影子 IT (Shadow IT)'),
    (r'進階持續性威脅', 'APT 進階持續性威脅'),
    (r'高級持續性威脅', 'APT 進階持續性威脅'),
    (r'勒索軟體即服務', 'Ransomware-as-a-Service (RaaS)'),
    (r'商業電子郵件入侵', 'BEC 商業電郵入侵'),
    (r'商業電郵入侵', 'BEC 商業電郵入侵'),
    (r'尾隨進入', '尾隨進入 (Tailgating)'),
    (r'尾隨', '尾隨進入 (Tailgating)'),
    (r'肩窺', '肩窺 (Shoulder Surfing)'),
    (r'翻垃圾蒐情', '翻垃圾蒐情 (Dumpster Diving)'),
    (r'垃圾箱潛水', '翻垃圾蒐情 (Dumpster Diving)'),
    (r'假借身份', '假借身分 (Pretexting)'),
    (r'假借身分', '假借身分 (Pretexting)'),
    (r'冒充', '冒充 (Impersonation)'),
    (r'仿冒', '冒充 (Impersonation)'),
    (r'水坑攻擊', '水坑攻擊 (Watering Hole)'),
    (r'威脅獵捕', '威脅獵捕 (Threat Hunting)'),
    (r'威脅情報', '威脅情報 (Threat Intelligence)'),
    (r'入侵指標', 'IOC 入侵指標'),
    (r'弱點掃描', '弱點掃描 (Vulnerability Scan)'),
    (r'漏洞掃描', '弱點掃描 (Vulnerability Scan)'),
    (r'弱點評估', '弱點評估 (Vulnerability Assessment)'),
    (r'漏洞評估', '弱點評估 (Vulnerability Assessment)'),
    (r'滲透測試', '滲透測試 (Penetration Test)'),
    (r'容器化', '容器化 (Containerization)'),
    (r'虛擬化', '虛擬化 (Virtualization)'),
    (r'微服務', '微服務 (Microservices)'),
    (r'無伺服器', '無伺服器 (Serverless)'),
    (r'基礎設施即代碼', 'IaC 基礎設施即程式碼'),
    (r'基礎建設即程式碼', 'IaC 基礎設施即程式碼'),
    (r'基礎設施即程式碼', 'IaC 基礎設施即程式碼'),
    (r'最小權限原則', '最小權限原則 (Least Privilege)'),
    (r'最小權限', '最小權限 (Least Privilege)'),
    (r'職責分離', '職責分離 (Separation of Duties)'),
    (r'基於角色的存取控制', 'RBAC 角色為基存取控制'),
    (r'角色為基的存取控制', 'RBAC 角色為基存取控制'),
    (r'存取控制清單', 'ACL 存取控制清單'),
    (r'特權存取管理', 'PAM 特權存取管理'),
    # Simplified→Traditional remnants
    (r'網絡', '網路'),
    (r'信息', '資訊'),
    (r'軟件', '軟體'),
    (r'硬件', '硬體'),
    (r'數據庫', '資料庫'),
    (r'數據', '資料'),
    (r'用戶', '使用者'),
    (r'帳戶', '帳號'),
    (r'賬號', '帳號'),
    (r'賬戶', '帳號'),
    (r'端口', '連接埠'),
    (r'內存', '記憶體'),
    (r'內部存儲', '記憶體'),
    (r'存儲', '儲存'),
    (r'計算機', '電腦'),
    (r'服務器', '伺服器'),
    (r'登錄', '登入'),
    (r'登入信息', '登入資訊'),
    (r'鏈接', '連結'),
    (r'點擊', '點擊'),
    (r'郵件', '電子郵件'),
    (r'電子郵件 ', '電子郵件'),
    (r'防火墻', '防火牆'),
    (r'墻', '牆'),
    (r'磁盤', '磁碟'),
    (r'硬盤', '硬碟'),
    (r'文件', '檔案'),
    (r'視頻', '影片'),
    (r'視訊', '影片'),
    (r'移動設備', '行動裝置'),
    (r'移動裝置', '行動裝置'),
    # Cleanup duplicate parentheticals (e.g., "SQL 注入 (SQL 注入)" → "SQL 注入")
]


def standardize_terms(zh_text):
    """Apply technical term standardization"""
    for pattern, replacement in TERM_STANDARDIZE:
        zh_text = re.sub(pattern, replacement, zh_text)
    # Remove duplicate parentheticals like "X (X)"
    zh_text = re.sub(r'([一-鿿\w]+(?: [一-鿿\w]+)*) \(\1\)', r'\1', zh_text)
    # Remove duplicate "X X" parentheticals like "SQL 注入 SQL 注入"
    return zh_text


async def main():
    with open("pdf_questions_clean.json", "r", encoding="utf-8") as f:
        pdf_qs = json.load(f)

    cache_file = "google_translated_questions.json"
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            cache = json.load(f)
        print(f"Loaded {len(cache)} cached translations")
    else:
        cache = {}

    sorted_keys = sorted(pdf_qs.keys(), key=lambda x: int(x))
    new_count = 0

    async with Translator() as translator:
        for i, num_str in enumerate(sorted_keys, 1):
            if num_str in cache and cache[num_str].get('zh'):
                # Skip already-cached entries (unless we want to re-translate)
                continue

            en_q = fix_ocr(pdf_qs[num_str]["q"])

            try:
                result = await translator.translate(en_q, dest='zh-tw')
                zh_raw = result.text
                zh_final = standardize_terms(zh_raw)
                cache[num_str] = {
                    "en": en_q,
                    "zh_raw": zh_raw,
                    "zh": zh_final
                }
                new_count += 1

                if new_count % 20 == 0:
                    with open(cache_file, "w", encoding="utf-8") as f:
                        json.dump(cache, f, ensure_ascii=False, indent=2)
                    print(f"[{i}/{len(sorted_keys)}] Q{num_str} saved (+{new_count})")

                # Small delay to be friendly
                await asyncio.sleep(0.3)

            except Exception as e:
                print(f"[{i}/{len(sorted_keys)}] Q{num_str} FAILED: {e}")
                with open(cache_file, "w", encoding="utf-8") as f:
                    json.dump(cache, f, ensure_ascii=False, indent=2)
                await asyncio.sleep(5)

    # Final save
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
    print(f"\nDone! Total: {len(cache)} translations (+{new_count} this run)")


if __name__ == "__main__":
    asyncio.run(main())
