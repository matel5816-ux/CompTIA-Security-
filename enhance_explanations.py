#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate detailed, beginner-friendly explanations for all 605 questions.

Strategy:
1. Identify the correct answer concept from English option text
2. Look up concept definition from vocabulary database (250+ Security+ terms)
3. Generate structured explanation:
   - 正確答案: X (translation)
   - 概念定義: what it is and how it works
   - 為何正確: why this answer fits the scenario
   - 其他選項分析: brief reason why each wrong option doesn't fit
"""
import json
import re
from vocabulary import VOCABULARY


# Patterns to detect common question scenarios for tailored explanations
SCENARIO_PATTERNS = {
    # Pattern: (regex on EN question, scenario_key)
    r'\bsocial engineering\b.*\bemail|phishing|smishing|vishing': 'social_eng_email',
    r'\bemployee.*click.*link|fraudulent|fake': 'phishing_click',
    r'\bcompliance|regulation|GDPR|HIPAA|PCI': 'compliance',
    r'\bbackup|recovery|RTO|RPO|disaster': 'dr_backup',
    r'\bencrypt|TLS|SSL|VPN|certificate': 'encryption',
    r'\bMFA|multifactor|authentication': 'auth',
    r'\bfirewall|IDS|IPS|WAF|NGFW': 'network_defense',
    r'\bSIEM|EDR|DLP|threat hunting|forensic': 'security_ops',
    r'\bvulnerability|patch|CVSS|CVE|scan': 'vuln_mgmt',
    r'\brisk|threat|impact|mitigate': 'risk_mgmt',
    r'\baudit|attestation|compliance|right.to.audit': 'audit_compliance',
    r'\bSSO|federation|Kerberos|OAuth|SAML': 'identity',
    r'\bcloud|IaaS|PaaS|SaaS|serverless|container': 'cloud',
    r'\bincident response|containment|eradication|chain of custody': 'incident_response',
    r'\bzero trust|least privilege|RBAC|access control': 'access_control',
    r'\bphysical|badge|CCTV|fence|mantrap|tailgating': 'physical',
    r'\bsupply chain|vendor|third.party|NDA|SOW|SLA': 'vendor',
}


def find_concept_in_text(text):
    """Find the most specific concept that appears in text"""
    text_lower = text.lower()
    # OCR fixes
    for fix_from, fix_to in [
        ('miscongurations', 'misconfigurations'),
        ('conguration', 'configuration'),
        ('rewall', 'firewall'),
        ('certicate', 'certificate'),
        ('overow', 'overflow'),
        ('tra c', 'traffic'),
    ]:
        text_lower = text_lower.replace(fix_from, fix_to)

    # Sort vocabulary keys by length (longest first) for specific matches
    sorted_terms = sorted(VOCABULARY.keys(), key=lambda x: -len(x))

    for term in sorted_terms:
        if ' ' in term or '-' in term or '/' in term:
            if term in text_lower:
                return VOCABULARY[term]
        else:
            # Use word boundaries for single words
            if re.search(r'\b' + re.escape(term) + r'\b', text_lower):
                return VOCABULARY[term]

    return None


def detect_scenario(en_q):
    """Detect the question scenario type"""
    en_lower = en_q.lower()
    for pattern, key in SCENARIO_PATTERNS.items():
        if re.search(pattern, en_lower):
            return key
    return 'general'


def generate_explanation(en_q, en_opts, answer_idx_list, zh_opts):
    """Generate a detailed, beginner-friendly explanation"""
    if not answer_idx_list:
        return "本題答案請參考英文題目。"

    answer_letters = [chr(65 + i) for i in answer_idx_list]
    letter_str = "、".join(answer_letters)

    # Get correct answer text (English) and Chinese
    correct_en = []
    correct_zh = []
    for i in answer_idx_list:
        if i < len(en_opts):
            correct_en.append(en_opts[i])
        if i < len(zh_opts):
            correct_zh.append(zh_opts[i])

    # Find concept for correct answer
    concept = None
    for en_text in correct_en:
        concept = find_concept_in_text(en_text)
        if concept:
            break

    # Build explanation parts
    parts = []

    # Part 1: 正確答案
    if len(answer_idx_list) > 1:
        # Multi-answer question
        parts.append(f"✅ **正確答案：{letter_str}**（{ '、'.join(correct_zh) }）。本題為多選題，需同時選出 {len(answer_idx_list)} 個選項。")
    else:
        parts.append(f"✅ **正確答案：{letter_str}**（{correct_zh[0] if correct_zh else correct_en[0]}）。")

    # Part 2: 概念說明 (from vocabulary)
    if concept:
        en_official, zh_official, desc = concept
        parts.append(f"📖 **概念：{en_official}（{zh_official}）** — {desc}。")

    # Part 3: 為何正確（基於 scenario）
    scenario = detect_scenario(en_q)
    why_correct = get_why_correct(scenario, correct_en[0] if correct_en else "", en_q)
    if why_correct:
        parts.append(f"💡 **為何此答案正確**：{why_correct}")

    # Part 4: 其他選項分析（簡短分析每個錯誤選項）
    if len(en_opts) > 1:
        wrong_analysis = []
        for i, opt in enumerate(en_opts):
            if i in answer_idx_list:
                continue
            opt_concept = find_concept_in_text(opt)
            if opt_concept:
                letter = chr(65 + i)
                zh_opt = zh_opts[i] if i < len(zh_opts) else opt
                en_off, zh_off, desc_short = opt_concept
                # Brief reason why this option doesn't fit
                wrong_reason = get_wrong_reason(en_off, scenario, en_q)
                if wrong_reason:
                    wrong_analysis.append(f"**{letter}. {zh_opt}**：{wrong_reason}")
                else:
                    wrong_analysis.append(f"**{letter}. {zh_opt}**：{desc_short.split('，')[0] if '，' in desc_short else desc_short}，與本題情境不完全吻合。")
            else:
                # No specific concept match
                letter = chr(65 + i)
                zh_opt = zh_opts[i] if i < len(zh_opts) else opt
                wrong_analysis.append(f"**{letter}. {zh_opt}**：與本題情境不符。")

        if wrong_analysis:
            parts.append("❌ **其他選項分析**：\n" + "\n".join("• " + w for w in wrong_analysis[:4]))

    return "\n\n".join(parts)


def get_why_correct(scenario, correct_text, en_q):
    """Return scenario-specific 'why this is correct' explanation"""
    correct_lower = correct_text.lower()

    # Specific common answers
    specific = {
        'sanitization': "Sanitization（資料淨化）是「安全清除資料但保留媒介可再利用」的標準做法，包含覆寫（Overwriting）、消磁（Degaussing）、密碼學擦除（Crypto-erase）等技術，符合 NIST 800-88 標準。可在合規前提下讓硬碟重新使用或捐贈。",
        'destruction': "Destruction（銷毀）是物理破壞硬碟使其無法再被使用（如壓碎、焚毀、剪碎）。比 Sanitization 更徹底但媒介無法再用，適用於最高機密資料。",
        'wiping': "Wiping（擦除）透過多次覆寫磁區使原資料不可復原，但保留磁碟可再使用。符合 NIST 800-88 標準的清除等級。",
        'degaussing': "Degaussing（消磁）使用強磁場破壞磁性媒介（HDD、磁帶）的儲存資料。對 SSD（固態硬碟）無效，因為 SSD 不靠磁性儲存。",
        'testing the policy in a non-production environment': "變更管理（Change Management）的標準做法是「先在非生產環境驗證」再部署到生產。可發現相容性問題、邊界案例、回退步驟，避免新規則直接衝擊業務。",
        'in a non-production environment': "變更管理（Change Management）要求變更必須先在非生產（測試/Staging）環境驗證，才能避免直接衝擊業務系統。這是 ITIL 變更管理的基本原則。",
        'documenting the new policy in a change request': "雖然變更請求文件化重要，但本身不能「防止」問題發生，只是事後審計用。Backout Plan 與測試才是防止問題的有效控制。",
        'organized crime': "有組織犯罪集團擁有龐大資金、技術人力與成熟運作模式，最容易被外國政府以資金「外包」執行國家利益相關的網路攻擊（如關鍵基礎設施攻擊、勒索軟體即服務 RaaS）。雖然 Nation-state 也常攻擊他國，但題目強調「被雇用」這個外包性質，更符合 Organized Crime。",
        'salting': "Salting（加鹽）是在密碼進行雜湊運算前加入一段隨機字串，使相同密碼產生不同雜湊值。這能有效抵禦彩虹表（Rainbow Table）攻擊，是密碼儲存的必備強化手段。",
        'phishing': "釣魚是透過偽造的電子郵件、簡訊或網站，誘騙受害者輸入帳密或敏感資訊。題目中員工點擊郵件連結進入假網站並輸入登入資料，正是 Phishing 的典型行為模式。",
        'jump server': "Jump Server（跳板伺服器）是位於 DMZ 或受控網段的中介伺服器，管理員必須先連線到跳板，再從跳板跳轉到目標網段。此設計可集中監控管理活動、減少攻擊面，是隔離敏感網段存取的業界標準做法。",
        'waf': "WAF（Web 應用防火牆）專門針對第 7 層（應用層）的攻擊，包含 SQL Injection、XSS、Buffer Overflow 等。傳統防火牆只看 L3/L4 標頭無法理解 HTTP 內容，無法有效阻擋應用層攻擊。",
        'multifactor authentication': "MFA 即使密碼被竊取，攻擊者仍需通過第二個獨立的驗證因素（如手機 OTP、硬體 Token、生物辨識）才能登入，能大幅降低憑證被盜後的危害。",
        'mfa': "MFA 即使密碼被竊取，攻擊者仍需通過第二個獨立的驗證因素才能登入。是預防憑證被盜用後仍能登入的最有效方案。",
        'sso': "SSO（Single Sign-On）允許使用者以一組憑證（例如企業網域帳號）存取多個應用系統，可同時達成「減少需維護的帳號數量」+「使用企業網域認證」兩個需求。",
        'sql injection': "SQL Injection 是攻擊者透過應用程式的輸入欄位注入惡意 SQL 命令的攻擊。利用資料庫缺乏輸入驗證、過寬權限、未過濾錯誤訊息等「設定不當」(misconfiguration)，達成資料外洩、竄改或刪除。防範方式：參數化查詢、輸入驗證、最小權限原則。",
        'tabletop exercise': "Tabletop（桌上演練）是參與者圍坐討論「假設情境」如何回應的紙上推演，不會衝擊實際系統，能訓練決策能力、釐清角色責任、發現流程漏洞。是讓事件回應團隊熟悉 IRP 的最佳方式。",
        'least privilege': "最小權限原則（Least Privilege）要求每個帳號/程序只擁有「執行其職責所必需的最低權限」。限制特定權限只給「真正需要的人員」是這個原則最直接的應用。",
        'zero trust': "零信任架構同時提供：（1）安全區段化（Microsegmentation）、（2）全企業統一的存取政策（基於身分+裝置+情境的條件式驗證）、（3）最小權限與微分段以縮小攻擊面。三者完全對應「安全區 + 全公司存取控制 + 縮小威脅範圍」的需求。",
        'tokenization': "Tokenization（代符化）用無意義的代符（token）取代敏感資料（如卡號），原始資料儲存於受保護的 vault。即使代符外洩，攻擊者也無法還原為真實資料。常用於 PCI DSS 信用卡資料保護。",
        'cvss': "CVSS（Common Vulnerability Scoring System）為漏洞提供 0–10 的量化分數，反映其嚴重度與可利用性（如攻擊向量、複雜度、所需權限、影響範圍）。是優先化修補的標準指標。CVE 只是漏洞編號（識別用）非評分系統。",
        'full disk encryption': "FDE（全磁碟加密，如 BitLocker、FileVault）加密整顆硬碟。即使筆電遺失或被竊，未通過開機驗證的話，任何取出硬碟讀取的嘗試都無法取得明文資料。是保護端點靜態資料的標準做法。",
        'preparation': "Preparation（準備階段）是 NIST 事件回應流程的「第一階段」，發生在事件之前：建立 IR 團隊、定義角色與職責、準備工具、執行訓練與桌上演練。其他階段（Detection、Containment、Recovery）都是事件發生後執行。",
        'web-based administration': "路由器強化（Hardening）的標準做法是停用未加密或非必要的管理通道，特別是 Web 管理介面通常含已知漏洞且加密強度不足。SSH 與 SNMPv3 是加密版本，應保留作為遠端管理；本地主控台則為帶外管理必需。",
        'chain of custody': "Chain of Custody（證據鏈）是數位鑑識的核心要求：記錄證據從蒐集、儲存到呈交法庭的「每一次轉手」，包含時間、人員、操作。確保證據完整性、可追溯且可被法庭採信。沒有完整證據鏈的證據在訴訟中可能被駁回。",
        'threat hunting': "Threat Hunting（威脅獵捕）是主動搜尋環境中尚未被自動化工具偵測的進階威脅與 TTPs（戰術/技巧/程序）。最適合針對「新手法」這類已知存在但偵測規則尚未涵蓋的未知威脅。",
        'cold site': "Cold Site（冷備站）只提供場地、電源與基本網路連線，所有硬體與資料都需在災難發生後運入與還原。雖然 RTO 較長（數天以上），但成本最低，符合「成本效益優先、可接受較長停機」的場景。",
        'hot site': "Hot Site（熱備站）與主站近即時同步資料，硬體與服務皆預先準備好可立即接管。雖然成本最高，但能達成最低 RTO（分鐘級）與最低 RPO（近零資料遺失），是高可用性的標準選擇。",
        'incident response': "事件回應（Incident Response）的標準流程包含偵測、分析、遏制、根除、復原、經驗教訓六個階段，目標是有系統地處理資安事件以最小化損害。",
        'rbac': "RBAC（Role-Based Access Control）依照員工的職位/角色分配權限。當員工調職或離職時可一次性更新其角色，避免 Privilege Creep（權限蠕變）。是企業最常用的存取控制模型。",
        'dlp': "DLP（資料外洩防護）可偵測機敏資料的特徵（如關鍵字、模式、機密標籤），在外傳時（郵件、上傳、USB、列印）觸發警報或阻擋。是針對「資料外洩」風險的專屬控制工具。",
        'siem': "SIEM 集中蒐集多源日誌（防火牆、伺服器、應用、雲端）、執行關聯分析、產生安全警報，並提供搜尋與儀表板介面。是 SOC（安全運營中心）的核心平台。",
        'edr': "EDR（端點偵測與回應）持續監控端點上的程序、檔案、網路與使用者行為，可即時偵測並回應惡意活動。是次世代防毒，能應對無檔案惡意軟體與進階威脅。",
    }

    # Try to match specific correct answers
    for key, explanation in specific.items():
        if key in correct_lower:
            return explanation

    # Default scenario-based explanations
    scenario_default = {
        'social_eng_email': "社交工程透過利用人性弱點（信任、權威壓力、緊急感）取得敏感資訊或誘導執行特定行為。本場景中的攻擊特徵明確符合該選項所描述的攻擊類型。",
        'phishing_click': "本題透過郵件連結與輸入登入資訊的情境符合此攻擊型態的典型行為。",
        'compliance': "合規要求組織遵守特定法律與標準。違反通常導致罰款、業務限制、訴訟與聲譽損害。",
        'dr_backup': "災害復原與業務持續性的核心是「在中斷時最小化影響」，本選項最符合題目強調的恢復需求（RTO/RPO/成本）。",
        'encryption': "加密保護資料的機密性。本選項提供符合題目需求的加密強度與適用情境。",
        'auth': "身分驗證確認使用者身分。多因素驗證（MFA）是阻擋憑證被盜後仍能登入的最有效控制。",
        'network_defense': "網路防禦工具各有其專屬層級與用途：防火牆過濾 L3/L4 流量、WAF 處理 L7 應用層、IDS/IPS 偵測攻擊模式。本選項對應題目情境的最佳防護層。",
        'security_ops': "資安運營工具（SIEM、EDR、DLP、SOAR）各有特定用途，需依場景選擇最符合的工具。",
        'vuln_mgmt': "弱點管理生命週期：發現 → 評估 → 優先化（依 CVSS）→ 修補 → 驗證 → 報告。本選項對應題目所處的階段。",
        'risk_mgmt': "風險管理四大策略：減緩（Mitigate）、規避（Avoid）、轉移（Transfer）、接受（Accept）。本選項符合題目情境的最佳策略。",
        'audit_compliance': "稽核活動需有完整文件與證據支援，第三方獨立稽核能提供客觀的合規證明。",
        'identity': "身分管理協議各有用途：SAML（企業 Web SSO）、OAuth（授權委派）、Kerberos（網域驗證）、LDAP（目錄查詢）。",
        'cloud': "雲端服務模型責任分擔不同：IaaS 客戶責任最大、SaaS 提供者責任最大。容器、無伺服器、IaC 解決不同雲端問題。",
        'incident_response': "事件回應六階段（NIST SP 800-61）：準備、偵測、分析、遏制、根除、復原、經驗教訓。每階段都有特定產出與責任。",
        'access_control': "存取控制原則：最小權限（只給必要權限）、職責分離（敏感任務分人執行）、零信任（永遠驗證）。",
        'physical': "實體安全控制：預防（門禁/Mantrap）、偵測（CCTV）、嚇阻（告示/照明）三類，可組合形成縱深防禦。",
        'vendor': "第三方/供應商風險管理透過合約（NDA/SLA/SOW）、稽核權、盡職調查等手段控管。",
        'general': "本選項是符合題目情境的最佳做法。建議參考英文原文與選項詳細比對，並查閱重要單字區的概念定義加深理解。",
    }

    return scenario_default.get(scenario, scenario_default['general'])


def get_wrong_reason(en_term, scenario, en_q):
    """Brief reason why a wrong-answer concept doesn't fit"""
    # Common wrong-answer reasons
    reasons = {
        'phishing': "Phishing 是廣義的釣魚攻擊，本題情境需要更具體的攻擊型態（如 Smishing/Whaling/BEC）。",
        'whistleblower': "吹哨者揭發內部不當行為，動機與題目情境不同。",
        'hacktivist': "駭客主義者為政治或社會理念進行攻擊，動機與題目情境（金錢/雇用）不同。",
        'unskilled attacker': "Script Kiddie 技術不足無法執行複雜的針對性攻擊。",
        'cve': "CVE 是漏洞「編號識別」，不是量化「嚴重度評分」（那是 CVSS）。",
        'cve common vulnerabilities and exposures': "CVE 是漏洞「編號識別」用，量化嚴重度的是 CVSS。",
        'aaa': "AAA（驗證/授權/稽核）是身分管理框架，與量化漏洞嚴重度無關。",
        'cert': "CERT 是緊急應變組織，與量化漏洞嚴重度無關。",
        'hot site': "Hot Site 即時同步但成本最高，與題目「成本效益優先」不符。",
        'warm site': "Warm Site 成本中等但仍需投資，題目強調成本最低時更傾向 Cold。",
        'cold site': "Cold Site 啟動時間長（數天），不符合「最低資料遺失/即時切換」需求。",
        'mobile site': "Mobile Site（行動備援）成本較高且機動性不適合本題情境。",
        'tls': "TLS 加密傳輸中資料（in transit），不保護靜態（at rest）資料。",
        'ssl': "SSL 已過時不安全，現代應使用 TLS 1.2/1.3。",
        'vpn': "VPN 加密傳輸中資料，不保護儲存在硬碟上的靜態資料。",
        'fde': "FDE 保護靜態資料，與本題的傳輸/驗證情境不符。",
        'edr': "EDR 是端點偵測回應，與本題的特定情境不完全對應。",
        'siem': "SIEM 集中日誌分析，並非本題場景最直接的解決方案。",
        'dlp': "DLP 防護資料外洩，與本題場景不完全對應。",
        'firewall': "傳統防火牆只看 L3/L4，無法處理應用層攻擊（需要 WAF）。",
        'ids': "IDS 只偵測警報無法阻擋，題目若需主動防禦則應選 IPS。",
        'memory injection': "記憶體注入是將惡意程式碼注入合法程序記憶體，與本題的資料庫攻擊情境不同。",
        'vm escape': "VM Escape 是從 Guest VM 突破到 Hypervisor，與本題情境不同。",
        'buffer overflow': "緩衝區溢位是寫入超過緩衝區大小造成記憶體破壞，與本題的資料庫設定問題不同。",
    }
    en_term_lower = en_term.lower()
    for key, reason in reasons.items():
        if key in en_term_lower:
            return reason
    return None


def main():
    # Load data
    with open("pdf_questions_clean.json", "r", encoding="utf-8") as f:
        pdf_qs = json.load(f)
    with open("translated_options.json", "r", encoding="utf-8") as f:
        trans_opts = json.load(f)

    # Load existing manual corrections (don't override these)
    try:
        from translation_corrections import CORRECTIONS
        manual_corrected = set(CORRECTIONS.keys())
    except ImportError:
        manual_corrected = set()

    result = {}
    for num_str, q in pdf_qs.items():
        num = int(num_str)
        if num in manual_corrected:
            # Skip - use manual correction
            continue

        zh_opts = trans_opts.get(num_str, [])
        explanation = generate_explanation(
            q["q"], q["options"], q["answer"], zh_opts
        )
        result[num_str] = explanation

    with open("enhanced_explanations.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Generated {len(result)} enhanced explanations")


if __name__ == "__main__":
    main()
