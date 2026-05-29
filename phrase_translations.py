#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive phrase translation dictionary for SY0-701 options.
Maps English option text -> faithful Chinese translation.
Use exact-match lookup before falling back to term replacement.
"""

PHRASE_TRANSLATIONS = {
    # DNS Sinkhole options
    "A DNS sinkhole can be set up to attract potential attackers away from a company's productive infrastructure.":
        "可設置 DNS 黑洞將潛在攻擊者從公司正式基礎設施引開",
    "A DNS sinkhole can be used to capture traffic to known-malicious domains used by attackers.":
        "DNS 黑洞可攔截到已知惡意域名的流量",
    "A DNS sinkhole can be used to draw employees away from known-good websites to malicious ones.":
        "DNS 黑洞可將員工從已知正常網站引導到惡意網站",
    "Attackers can see a DNS sinkhole as a highly valuable resource to identify a company's secure assets.":
        "攻擊者可能將 DNS 黑洞視為識別公司安全資產的寶貴資源",

    # Vendor / supply chain
    "A SOW had not been agreed to by the client.": "客戶未同意工作說明書 (SOW)",
    "A WO had not been mutually approved.": "工單 (WO) 未經雙方核可",
    "A required NDA had not been signed.": "必要的保密協議 (NDA) 未簽署",
    "A thorough analysis of the supply chain": "徹底的供應鏈分析",
    "A legally enforceable corporate acquisition policy": "具法律效力的企業併購政策",
    "A right to audit clause in vendor contracts and SOWs": "供應商合約與 SOW 中的稽核權條款",
    "An in-depth penetration test of all suppliers and vendors": "對所有供應商進行深入滲透測試",
    "Supply chain analysis": "供應鏈分析",
    "Supply chain compromise": "供應鏈攻擊",
    "Supply chain vendor": "供應鏈供應商",
    "Third-party audit": "第三方稽核",
    "Third-party audit report": "第三方稽核報告",
    "Third-party risk assessment documentation": "第三方風險評估文件",
    "Third-party vendor": "第三方供應商",

    # Cryptography
    "A cryptographic collision was detected.": "偵測到密碼學雜湊碰撞",
    "Certificate authority linking": "憑證機構連結",
    "Certificate revocation list": "憑證撤銷清單 (CRL)",
    "Elliptic curve cryptography": "橢圓曲線加密 (ECC)",
    "Encryption ensures data integrity, while hashing ensures data confidentiality.":
        "加密確保完整性，雜湊確保機密性（錯誤敘述）",
    "Encryption protects data in transit, while hashing protects data at rest.":
        "加密保護傳輸中資料、雜湊保護靜態資料（錯誤敘述）",
    "Encryption replaces cleartext with ciphertext, while hashing calculates a checksum.":
        "加密把明文替換為密文，雜湊計算固定長度的校驗值",
    "Encryption uses a public-key exchange, while hashing uses a private key.":
        "加密使用公鑰交換、雜湊使用私鑰（錯誤敘述）",
    "Public key infrastructure": "公開金鑰基礎設施 (PKI)",
    "The use of block ciphers": "使用區塊加密法",
    "Weak cipher suites": "弱密碼套件",
    "Insecure key storage": "不安全的金鑰儲存",
    "Secure DNS cryptographic downgrade": "DNS 安全密碼降級",

    # Attacks
    "A dictionary attack was used to log in as the server administrator.":
        "使用字典攻擊登入伺服器管理員帳號",
    "A keylogger is installed on jsmith's workstation.": "在 jsmith 的工作站安裝鍵盤側錄程式",
    "A packet capture tool was used to steal the password.": "用封包擷取工具竊取密碼",
    "A process receives an unexpected amount of data, which causes malicious code to execute.":
        "程序收到非預期大量資料造成惡意程式碼執行（緩衝區溢位）",
    "A remote-access Trojan was used to install the malware.": "使用遠端存取木馬安裝惡意軟體",
    "A rootkit was deployed.": "Rootkit 已被部署",
    "A spraying attack was used to determine which credentials to use.": "使用密碼噴灑攻擊找出可用憑證",
    "A vulnerability has been exploited to deploy a worm to the server.": "弱點被利用部署蠕蟲到伺服器",
    "A web shell has been deployed to the server through the page.": "透過網頁部署 Web Shell 到伺服器",
    "A worm is propagating across the network.": "蠕蟲正在網路中傳播",
    "An attacker can access the hypervisor and compromise other VMs.":
        "攻擊者可存取 Hypervisor 並妥協其他 VM",
    "An attacker is attempting to brute force jsmith's account.": "攻擊者嘗試蠻力破解 jsmith 的帳號",
    "An executable is overwritten on the disk, and malicious code runs the next time it is loaded.":
        "磁碟上的執行檔被覆寫，下次載入時執行惡意程式",
    "Attackers have deployed a rootkit Trojan to the server over an exposed RDP port.":
        "攻擊者透過暴露的 RDP port 部署 Rootkit 木馬到伺服器",
    "Buffer overflow attack": "緩衝區溢位攻擊",
    "Business email compromise": "商業電郵入侵 (BEC)",
    "Bypassing the organization's DNS sinkholing": "繞過組織的 DNS 黑洞機制",
    "Exfiltrating data from fshare.int.complia.org": "從 fshare.int.complia.org 外洩資料",
    "Impersonation of business units through typosquatting": "透過錯字搶註冒充業務單位",
    "Malicious code is copied to the allocated space of an already running process.":
        "惡意程式碼被複製到執行中程序的記憶體配置空間（記憶體注入）",
    "Malicious insiders are using the server to mine cryptocurrency.": "惡意內部人員用伺服器挖礦",
    "Malicious instructions can be inserted into memory and give the attacker elevated privileges.":
        "可將惡意指令注入記憶體獲得提升的權限",
    "Pass-the-hash": "Pass-the-hash 攻擊",
    "Ransomware has been deployed in the domain.": "勒索軟體已在網域中部署",
    "Reflected denial of service": "反射型阻斷服務 (Reflected DoS)",
    "Sniffing via on-path position": "透過中間人位置進行流量竊聽",
    "The attacker created fileless malware that was hosted by the banking platform.":
        "攻擊者建立無檔案惡意軟體，由銀行平台代管",
    "The attacker performed a pass-the-hash attack using a shared support account.":
        "攻擊者使用共用支援帳號進行 Pass-the-hash 攻擊",
    "The attacker socially engineered the accountant into performing bad transfers.":
        "攻擊者透過社交工程誘使會計執行不當匯款",
    "The attacker utilized living-off-the-land binaries to evade endpoint detection and response.":
        "攻擊者利用 LotL 工具規避 EDR 偵測",
    "The software had a hidden keylogger.": "軟體含隱藏的鍵盤側錄程式",
    "The user's computer had a fileless virus.": "使用者電腦感染無檔案病毒",
    "Threat scope reduction": "縮小威脅範圍",
    "Two processes access the same variable, allowing one to cause a privilege escalation.":
        "兩個程序存取同一變數造成競爭條件並權限提升",
    "Unencrypted data can be read by a user who is in a separate environment.":
        "未加密的資料可被位於其他環境的使用者讀取",

    # Vulnerabilities
    "Open-source component usage": "開源元件使用",
    "Lack of new features": "缺少新功能",
    "Lack of security updates": "缺少安全更新",
    "Lack of source code access": "缺少原始碼存取",
    "Lack of vendor support": "缺少廠商支援",
    "Devices reaching end-of-life and losing support": "裝置到達 EOL 失去支援",
    "End-of-life support": "生命終期支援",
    "Use of insecure protocols": "使用不安全協定",
    "Software development life cycle": "軟體開發生命週期 (SDLC)",
    "Software development life cycle policy": "SDLC 政策",

    # Controls & responses
    "A snapshot of the file system was taken.": "對檔案系統建立快照",
    "Add a guest captive portal requiring visitors to accept terms and conditions.":
        "加入訪客強制門戶要求接受條款",
    "Add password complexity rules and increase password history limits": "增加密碼複雜度與歷史限制",
    "Adding a fake account to /etc/passwd": "在 /etc/passwd 加入假帳號",
    "Adding automated alerting when anomalies occur": "新增異常時自動告警",
    "Air gap the system.": "將系統氣隙隔離",
    "Allow each client the right to audit": "允許各客戶執行稽核",
    "Allow for new devices to be connected via WPS.": "允許新裝置透過 WPS 連線",
    "An MDM solution with conditional access": "MDM 搭配條件式存取",
    "An SSH server within the corporate LAN": "企業 LAN 內的 SSH 伺服器",
    "An RPO has not been determined.": "RPO 尚未定義",
    "Apply IP address reputation data.": "套用 IP 信譽資料",
    "Apply classifications to the data.": "對資料套用分類",
    "Apply patch management.": "套用修補管理",
    "Apply the patch to the system.": "對系統套用修補",
    "Approving the change after a successful deployment": "成功部署後核可變更",
    "Audit each domain administrator account weekly for password compliance.":
        "每週稽核網域管理員帳號密碼合規性",
    "Automated response actions": "自動化回應動作",
    "Background checks for new employees": "新員工背景調查",
    "Be alert to unexpected requests from familiar email addresses": "對熟悉郵箱的異常請求保持警覺",
    "Block access to cloud storage websites.": "阻擋雲端儲存網站存取",
    "Block all outbound traffic from the intranet.": "阻擋內網所有對外流量",
    "Block the URL shortener domain in the web proxy.": "在 Web 代理阻擋短網址域名",
    "Block traffic based on known malicious signatures.": "依已知惡意簽章阻擋流量",
    "Blocking command injections via a WAF": "用 WAF 阻擋命令注入",
    "Blocking that website on the endpoint protection software": "在端點防護軟體阻擋該網站",
    "Branch protection as part of the CI/CD pipeline": "在 CI/CD 管線實作分支保護",
    "Branch protection tests": "分支保護測試",
    "Bug bounty program": "漏洞獎金計畫",
    "Business continuity plan": "業務持續性計畫 (BCP)",
    "Business continuity planning": "業務持續性規劃",
    "Business impact analysis": "業務影響分析 (BIA)",
    "Building a load-balanced VPN solution with redundant internet": "建立含冗餘 ISP 的負載平衡 VPN",
    "Changing the remote desktop port to a non-standard number": "把 RDP port 改為非標準埠",
    "Check for recently terminated DBAs.": "檢查近期離職的 DBA",
    "Check host firewall logs.": "檢查主機防火牆日誌",
    "Check the policy on personal email at work.": "檢查工作個人郵件政策",
    "Check the users table for new accounts.": "檢查 users 表是否有新帳號",
    "Close unnecessary service ports.": "關閉不必要的服務 port",
    "Code scanning for vulnerabilities": "原始碼弱點掃描",
    "Collect and monitor all traffic exiting the network.": "收集並監控所有對外流量",
    "Collecting evidence of malicious activity": "蒐集惡意活動證據",
    "Combining relevant logs from multiple sources into one location":
        "將多來源相關日誌彙整到單一位置",
    "Company data can be accounted for when the employee leaves the organization.":
        "員工離職時可清點公司資料",
    "Compensating controls exist.": "存在補償控制",
    "Concurrent session usage": "並行會話使用",
    "Conduct a site survey.": "進行場勘",
    "Conduct a tabletop exercise with the team.": "與團隊執行桌上演練",
    "Conduct a tabletop exercise.": "進行桌上演練",
    "Conducting multiple security investigations in parallel": "同時進行多個資安調查",
    "Configure a RADIUS server to manage device authentication.": "設定 RADIUS 伺服器管理裝置驗證",
    "Configure all systems to log scheduled tasks.": "設定所有系統記錄排程工作",
    "Configure firewall rules to block external access to Internal resources.":
        "設定防火牆規則阻擋對內部資源的外部存取",
    "Configure the correct VLAN.": "設定正確的 VLAN",
    "Configure the perimeter IPS to block inbound HTTPS directory traversal traffic, and verify the signatures are updated daily.":
        "設定邊界 IPS 阻擋入向 HTTPS 目錄遍歷流量並每日更新簽章",
    "Configure the servers for high availability.": "為伺服器設定高可用性",
    "Configuring a SIEM tool to capture all web traffic": "設定 SIEM 工具擷取所有 Web 流量",
    "Configuring network load balancing for multiple paths": "為多路徑設定網路負載平衡",
    "Configuring the IPS to allow shopping": "設定 IPS 允許購物網站",
    "Connect the systems to an external authentication server": "將系統連到外部驗證伺服器",
    "Connecting dual PDUs to redundant power supplies": "將雙 PDU 連到冗餘電源",
    "Connecting the remote server to the domain and increasing the password length":
        "把遠端伺服器加入網域並加長密碼",
    "Cost-benefit analysis": "成本效益分析",
    "Create IDS policies to monitor domain controller access.": "建立 IDS 政策監控網域控制器存取",
    "Create a blocklist for all subject lines.": "為所有主旨建立阻擋名單",
    "Create a rule to block outgoing email attachments.": "建立規則阻擋外寄郵件附件",
    "Create additional training for users to recognize the signs of phishing attempts":
        "為使用者建立更多釣魚識別訓練",
    "Create custom scripts to aggregate and analyze logs.": "建立自訂腳本彙整分析日誌",
    "Create incident response and disaster recovery plans.": "建立事件回應與災害復原計畫",
    "Create or obtain a layout of the office.": "建立或取得辦公室平面圖",
    "Creating a GPO for all contract employees and setting time-of-day log-in restrictions":
        "為合約員工建立 GPO 並設定時段登入限制",
    "Creating a discretionary access policy and setting rule-based access for contract employees":
        "為合約員工建立 DAC 政策並設定規則為基的存取",
    "Creating a false text file in /docs/salaries": "在 /docs/salaries 建立假文字檔（蜜檔）",
    "Creating a firewall rule to allow HTTPS traffic": "建立防火牆規則允許 HTTPS 流量",

    # D/E
    "Develop phishing campaigns and notify the management team of any successes.":
        "進行釣魚演練並回報任何成功案例給管理層",
    "Data inventory and retention": "資料清冊與保留",
    "Deciding red and blue team rules of engagement": "決定紅藍隊的交戰守則",
    "Decrease the level of the web filter settings.": "降低 Web 過濾器設定等級",
    "Delete emails from unknown service provider partners.": "刪除來自未知服務商的郵件",
    "Define Group Policy on the servers.": "在伺服器上定義群組原則",
    "Defining and monitoring change management procedures": "定義並監控變更管理流程",
    "Deploy, establish, maintain": "部署 → 建立 → 維護",
    "Deploy, maintain, establish": "部署 → 維護 → 建立",
    "Deploying PowerShell scripts": "部署 PowerShell 腳本",
    "Deploying multiple large NAS devices for each host": "為每台主機部署多台大型 NAS",
    "Detecting insider threats using anomalous behavior recognition": "用異常行為辨識偵測內部威脅",
    "Determining the organization's ISP-assigned address space": "判斷組織 ISP 分配的位址空間",
    "Determining the root cause of the incident": "判定事件的根本原因",
    "Develop and provide training on data protection policies.": "制定並提供資料保護政策訓練",
    "Develop requirements for database encryption.": "制定資料庫加密的需求",
    "Developing procedures for employee onboarding and offboarding": "制定員工到職與離職程序",
    "Developing steps to mitigate the risks of the incident": "制定減緩事件風險的步驟",
    "Developing the incident response plan": "制定事件回應計畫",
    "Digital rights management": "數位版權管理 (DRM)",
    "Digitally signing the software": "對軟體進行數位簽章",
    "Disable the query.php script.": "停用 query.php 腳本",
    "Disablement of unused services": "停用未使用服務",
    "Disaster recovery plan": "災害復原計畫 (DRP)",
    "Disciplinary actions for users": "對使用者的紀律處分",
    "Disclosure of sensitive data through incorrect classification": "因分類錯誤洩漏敏感資料",
    "Discovering and documenting external considerations": "發現並記錄外部考量因素",
    "Domain name, PKI, GeoIP lookup": "網域名稱、PKI、GeoIP 查詢",
    "Dual control requirements for wire transfers": "電匯需雙人控制",
    "Due care and due diligence": "盡職保密與盡職調查",

    # E
    "Easier debugging of the system": "更容易除錯系統",
    "Email gateway to block phishing attempts": "Email Gateway 阻擋釣魚",
    "Email message: \"Click this link to get your free gift card.\"":
        "郵件內容：「點此連結領取免費禮品卡」",
    "Employees who open an email attachment receive messages demanding payment in order to access files.":
        "員工開啟郵件附件後收到付款要求才能存取檔案",
    "Enabling threat prevention features on the firewall": "在防火牆啟用威脅防護功能",
    "Encrypting databases containing sensitive data": "對含敏感資料的資料庫加密",
    "Encrypting sensitive data at rest and in transit": "對靜態與傳輸中的敏感資料加密",
    "Encrypting the system's hard drive": "加密系統硬碟",
    "End users will be required to consider the classification of data that can be used in product development.":
        "末端使用者須考量產品開發中可用資料的分類",
    "Endpoint detection and response": "端點偵測回應 (EDR)",
    "Enforcement of content filtering policies": "強制執行內容過濾政策",
    "Enforcing baseline configurations": "強制執行基準設定",
    "Ensure only TLS and other encrypted protocols are selected for use on the network.":
        "僅允許網路上使用 TLS 等加密協定",
    "Ensure that NAC is enforced on all network segments, and confirm that firewalls have updated policies to block unauthorized traffic.":
        "確保所有網段強制 NAC，並驗證防火牆政策已更新阻擋未授權流量",
    "Ensure the EDR software monitors for unauthorized applications that could be used by threat actors, and configure alerts for the security team.":
        "確保 EDR 監控未授權應用並對安全團隊發出告警",
    "Ensuring secure cookies are used": "確保使用安全 Cookie",
    "Environmental variables define cryptographic standards for the system and could cause vulnerabilities.":
        "環境變數定義系統密碼標準並可能造成漏洞",
    "Environmental variables will determine when updates are run and could mitigate the risk.":
        "環境變數決定何時執行更新，可減緩風險",
    "Escalate the issue to the SDLC team.": "將問題升級到 SDLC 團隊",
    "Establish, deploy, maintain": "建立 → 部署 → 維護",
    "Establish, maintain, deploy": "建立 → 維護 → 部署",
    "Establishing the backup and recovery procedures": "建立備份與還原程序",
    "Estimating the recovery time of systems": "估算系統的恢復時間",
    "Evaluate tools that identify risky behavior and distribute reports on the findings.":
        "評估能識別風險行為並產出報告的工具",
    "Evaluating the risk management plan": "評估風險管理計畫",
    "Execute the code in a sandbox.": "在沙箱中執行程式碼",
    "Executing regular phishing campaigns": "定期執行釣魚演練",

    # F
    "Familiarizing participants with the incident response process": "讓參與者熟悉事件回應流程",
    "File-based solution": "以檔案為基礎的方案",
    "Finding security gaps in the system": "找出系統的安全缺口",

    # G
    "Generate a hash of the files.": "為檔案產生雜湊值",
    "Government identification numbers": "政府識別號碼",
    "Guard rail script": "防護腳本",
    "Guard rails implementation": "實作防護機制",

    # H
    "Hackers' ability to obtain data from used hard drives": "駭客從報廢硬碟取得資料的能力",
    "Harden the virtual host.": "強化虛擬主機",
    "Having a backout plan when a patch fails": "修補失敗時有回退計畫",
    "High availability networking": "高可用性網路",
    "Hire a vendor to perform a penetration test": "聘僱廠商執行滲透測試",
    "Hiring more help desk staff": "增聘更多服務台人員",
    "Host-based firewall": "主機型防火牆",
    "Host-based firewalls": "主機型防火牆",

    # I
    "Identify embedded keys": "識別嵌入金鑰",
    "Identify the attacker's entry methods.": "識別攻擊者的入侵手法",
    "Identifying the communication strategy": "識別溝通策略",
    "Identity and access management": "身分與存取管理 (IAM)",
    "If a security incident occurs on the device, the correct employee can be notified.":
        "裝置發生資安事件時可通知正確員工",
    "If the certificate signing request is valid": "若 CSR 有效",
    "If the public key is configured": "若公鑰已設定",
    "If the root certificate is installed": "若根憑證已安裝",
    "If the wildcard certificate is configured": "若萬用字元憑證已設定",
    "Implement a new IPSec tunnel from internal resources.": "從內部資源建立新的 IPSec 隧道",
    "Implement a privileged access management solution.": "實作特權存取管理 (PAM) 方案",
    "Implement centralized authentication with proper password policies":
        "實作集中式驗證與適當的密碼政策",
    "Implement email security filters to prevent phishing emails from being delivered.":
        "實作郵件安全過濾器阻擋釣魚郵件投遞",
    "Implement security awareness training.": "實施安全意識訓練",
    "Implement vulnerability scanning of the company's systems.": "對公司系統實施弱點掃描",
    "Implementation of additional authentication factors": "實作額外的驗證因素",
    "Implementing SAML with federation to the contract employees' authentication server":
        "用 SAML 聯邦到合約員工的驗證伺服器",
    "Implementing an OAuth server and then setting least privilege for contract employees":
        "實作 OAuth 伺服器並為合約員工設定最小權限",
    "Implementing an incident reporting web page": "實作事件回報網頁",
    "Improved scalability of the system": "改善系統的可擴展性",
    "Improving security awareness training": "改善安全意識訓練",
    "In-memory environmental variable values can be overwritten and used by attackers.":
        "記憶體中的環境變數可被覆寫並被攻擊者利用",
    "Incident response procedure": "事件回應程序",
    "Including an \"allow any\" policy above the \"deny any\" policy":
        "在『deny any』政策上方加入『allow any』政策",
    "Including the date and person who reviewed the information in a report":
        "在報告中加入審查日期與人員",
    "Incorrect inventory data leading to a laptop shortage": "資產清冊錯誤導致筆電短缺",
    "Increased compartmentalization of the system": "增加系統的區隔程度",
    "Install a unified threat management appliance.": "安裝統合威脅管理 (UTM) 裝置",
    "Install endpoint management software on all systems": "在所有系統安裝端點管理軟體",
    "Install endpoint protection.": "安裝端點防護",
    "Introduce a campaign to recognize phishing attempts.": "推動釣魚識別意識活動",
    "It acts as a workforce multiplier.": "可作為人力倍增器",
    "It adds additional guard rails.": "新增額外的防護機制",
    "It removes technical debt.": "消除技術債",

    # L
    "Lead a simulated failover.": "執行模擬故障切換",
    "Limit the ability of user accounts to change passwords": "限制使用者帳號變更密碼的能力",
    "Limiting the affected servers with a load balancer": "用負載平衡器限制受影響的伺服器",
    "Limiting the use of third-party libraries": "限制使用第三方函式庫",
    "List of board members": "董事會成員名單",
    "Log in to each access point and check the settings.": "登入每個無線存取點檢查設定",
    "Logging controls should fail open.": "日誌控制應 Fail-open（失敗開放）",
    "Logical security controls should fail closed.": "邏輯安全控制應 Fail-closed（失敗關閉）",

    # M
    "Making a record of the events that occur in the system": "記錄系統中發生的事件",
    "Masking the username in a report to protect privacy": "在報告中遮罩使用者名稱以保護隱私",
    "Master service agreement": "主服務協議 (MSA)",
    "Mean time between failure": "平均故障間隔 (MTBF)",
    "Mean time between failures": "平均故障間隔 (MTBF)",
    "Mean time to repair": "平均修復時間 (MTTR)",
    "Measure cable lengths between access points.": "測量無線存取點之間的線材長度",
    "Methodically walk around the office noting Wi-Fi signal strength.":
        "有系統地在辦公室走動記錄 Wi-Fi 訊號強度",
    "Mobile application-generated, one-time passcode with facial recognition":
        "行動應用產生的一次性密碼搭配臉部辨識",
    "Modify the content of recurring training.": "修改定期訓練內容",
    "More regular account audits": "更定期的帳號稽核",
    "Move the system to a different network segment.": "把系統移到其他網段",

    # N
    "NGFW utilizing application inspection": "NGFW 搭配應用程式檢測",
    "Next-generation firewall": "次世代防火牆 (NGFW)",
    "Notify the applicable parties of the breach.": "通知違規所影響的各方",

    # O
    "Obtain and execute the malware in a sandbox environment and perform packet capture":
        "在沙箱中取得並執行惡意軟體並擷取封包",
    "Off-the-shelf software": "現成軟體",
    "Open public ledger": "公開帳本",
    "Open-source component usage": "開源元件使用",
    "Open-source intelligence": "開源情報 (OSINT)",

    # P
    "Peer review and approval": "同儕審查與核可",
    "Perform a risk assessment to classify the vulnerability.": "執行風險評估以分類漏洞",
    "Perform an annual self-assessment.": "每年進行自我評估",
    "Performing more phishing simulation campaigns": "進行更多釣魚模擬演練",
    "Performing regular vulnerability scans": "定期執行弱點掃描",
    "Performing social engineering as part of third-party penetration testing":
        "在第三方滲透測試中進行社交工程",
    "Performing static code analysis on the software": "對軟體執行靜態程式碼分析 (SAST)",
    "Periodically test the generators.": "定期測試發電機",
    "Personal application store access": "個人應用商店存取",
    "Phone authentication application": "手機驗證應用程式",
    "Physical location of the company": "公司的實體位置",
    "Place posters around the office to raise awareness of common phishing activities.":
        "在辦公室張貼海報提升常見釣魚活動的意識",
    "Placing the system in an isolated VLAN": "將系統放入隔離 VLAN",
    "Plain text email": "純文字郵件",
    "Producing IOC for malicious artifacts": "為惡意產物產生 IOC",
    "Product design process": "產品設計流程",
    "Public key infrastructure": "公開金鑰基礎設施 (PKI)",
    "Purchase and install security software.": "購買並安裝安全軟體",
    "Purchasing a low-cost SD-WAN solution for VPN traffic": "為 VPN 流量購買低成本 SD-WAN 方案",

    # Q
    "Quarantine all emails received and notify all employees.": "隔離所有收到的郵件並通知全體員工",
    "Query the file's metadata.": "查詢檔案的中繼資料 (Metadata)",
    "Quickly determining the impact of an actual security breach": "快速判定真實資安事件的影響",

    # R
    "Real-time operating system": "即時作業系統 (RTOS)",
    "Real-time recovery": "即時復原",
    "Recovery point objective": "恢復點目標 (RPO)",
    "Recovery time objective": "恢復時間目標 (RTO)",
    "Reduced complexity of the system": "降低系統複雜度",
    "Reduced cost of ownership of the system": "降低系統擁有成本 (TCO)",
    "Reestablishing the compromised system's configuration and settings":
        "重新建立被妥協系統的設定",
    "Refer to the change management policy.": "參考變更管理政策",
    "Refrain from clicking on images included in emails from new vendors":
        "避免點擊新供應商郵件中的圖片",
    "Regularly updating server software and patches": "定期更新伺服器軟體與修補",
    "Reimage the end user's machine.": "重新映像末端使用者機器",
    "Remote access points should fail closed.": "遠端存取應 Fail-closed",
    "Remove all user permissions from shares on the file server.":
        "從檔案伺服器共享中移除所有使用者權限",
    "Remove possible impediments to radio transmissions.": "移除無線訊號的可能阻礙",
    "Removing payment information from the servers": "從伺服器移除付款資訊",
    "Removing sensitive data from production systems": "從生產系統移除敏感資料",
    "Replacing sensitive data with surrogate values": "用代理值替換敏感資料 (代符化)",
    "Report the breach to the local authorities.": "向當地主管機關通報違規",
    "Reporting structure for the data privacy officer": "資料隱私長 (DPO) 的回報架構",
    "Request process for data subject access": "資料主體存取請求流程",
    "Require that invoices be sent as attachments": "要求發票以附件形式寄送",
    "Requiring a statement each week that no exceptions were noted":
        "每週要求一份「無例外」的聲明",
    "Requiring passwords with eight characters": "要求 8 字元密碼",
    "Restrict internet access for the employees who disclosed credentials.":
        "限制洩漏憑證員工的網路存取",
    "Retain all emails from the company to affected customers for an indefinite period of time.":
        "無限期保留公司寄給受影響客戶的所有郵件",
    "Retain any communications between security members during the breach response.":
        "保留違規回應期間安全成員的所有通訊",
    "Retain any communications related to the security breach until further notice.":
        "保留所有與違規相關通訊直到另行通知",
    "Retain the emails between the security team and affected customers for 30 days.":
        "保留安全團隊與受影響客戶的郵件 30 天",
    "Review access logs to determine the most active devices.": "檢視存取日誌找出最活躍的裝置",
    "Review the IPS logs and determine which command-and-control IPs were blocked.":
        "檢視 IPS 日誌判斷哪些 C2 IP 被阻擋",
    "Review the documents' data classification policy.": "檢視文件的資料分類政策",
    "Right-to-audit clause": "稽核權條款",
    "Risk identification": "風險識別",
    "Risk management process": "風險管理流程",
    "Role as controller or processor": "扮演控制者或處理者角色",
    "Role-based access control": "角色為基存取控制 (RBAC)",
    "Run vulnerability scans to check for systems and applications that are vulnerable to the new exploit.":
        "執行弱點掃描檢查易受新漏洞影響的系統與應用",

    # S
    "Safety controls should fail open.": "安全控制應 Fail-open",
    "Scan email traffic inline.": "對郵件流量進行串接掃描",
    "Scan the database server for malware.": "掃描資料庫伺服器的惡意軟體",
    "Scheduling vulnerable jobs in /etc/crontab": "在 /etc/crontab 排程具弱點的工作",
    "Search the executable for ASCII strings.": "在執行檔中搜尋 ASCII 字串",
    "Search the web server for ransomware notes.": "搜尋網頁伺服器是否有勒索訊息",
    "Searching and processing data to identify patterns of malicious activity":
        "搜尋並處理資料以識別惡意活動模式",
    "Secrets management configurations": "密鑰管理設定",
    "Secure configuration guide applicability": "安全設定指南適用性",
    "Securely store the documents on an air-gapped network.": "將文件安全存放於氣隙網路",
    "Security agent deployment": "安全代理部署",
    "Security analysts will be able to see the classification of data within a document.":
        "資安分析師可看到文件內資料的分類",
    "Security awareness training": "安全意識訓練",
    "Security procedure evaluation": "安全程序評估",
    "Security questions and a one-time passcode sent via email": "安全問題與郵件 OTP",
    "Self-assessment findings": "自評發現",
    "Send out periodic security reminders.": "發送定期安全提醒",
    "Send quarterly newsletters that explain the importance of password management.":
        "每季發送解釋密碼管理重要性的電子報",
    "Send the dead domain to a DNS sinkhole.": "將失效域名送到 DNS 黑洞",
    "Service-level agreement": "服務水準協議 (SLA)",
    "Service-level agreements": "服務水準協議 (SLA)",
    "Service-level expectations": "服務水準預期",
    "Set the maximum data retention policy.": "設定最長資料保留政策",
    "Set up a WAP to allow internal access from public networks.": "設置 WAP 讓內部可從公網存取",
    "Setting firewall rules to allow traffic from any port to that destination":
        "設定防火牆規則允許任意 port 流量到該目的地",
    "Setting up a VPN and placing the jump server inside the firewall":
        "設置 VPN 並把跳板伺服器放在防火牆內",
    "Setting weak passwords in /etc/shadow": "在 /etc/shadow 設定弱密碼（蜜餌）",
    "Smart card with PIN and password": "智慧卡搭配 PIN 與密碼",
    "Someone you know": "你認識的人 (錯誤的 MFA 因素)",
    "Something you exhibit": "你展現的東西 (Inherent 因素)",
    "Something you have": "你擁有的東西 (Possession 因素)",
    "Somewhere you are": "你所在位置 (Location 因素)",
    "Standardizing security incident reporting": "標準化資安事件通報",
    "Static code analysis": "靜態程式碼分析 (SAST)",
    "Stronger authentication of the system": "更強的系統驗證",

    # T
    "Tap and monitor the email feed.": "Tap 並監控郵件流",
    "Testing input validation on the user input fields": "測試使用者輸入欄位的輸入驗證",
    "The MOU had basic clauses from a template.": "MOU 僅含範本的基本條款",
    "The administrator needs to increase the TLS version on the organization's RA.":
        "管理員需提升組織 RA 的 TLS 版本",
    "The administrator needs to install the server certificate into the local truststore.":
        "管理員需將伺服器憑證安裝到本地信任根",
    "The administrator should allow SAN certificates in the browser configuration.":
        "管理員應在瀏覽器設定允許 SAN 憑證",
    "The administrator should request that the secure LDAP port be opened to the server.":
        "管理員應請求對伺服器開啟安全 LDAP port",
    "The compatibility of the TLS version": "TLS 版本的相容性",
    "The contents of environmental variables could affect the scope and impact of an attack.":
        "環境變數的內容可能影響攻擊的範圍與影響",
    "The device is configured to use cleartext passwords.": "裝置設定為使用明文密碼",
    "The end user changed the file permissions.": "末端使用者變更了檔案權限",
    "The equipment MTBF is unknown.": "設備 MTBF 未知",
    "The organization will have the ability to create security requirements based on the data type.":
        "組織能依資料類型制定安全要求",
    "The policy will result in the creation of access levels for each level of classification.":
        "政策會為各分類層級建立存取等級",
    "The security team will be able to send user awareness training to the appropriate teams.":
        "資安團隊能對適當團隊發送使用者意識訓練",
    "The system has vulnerabilities that are not being detected.": "系統有未被偵測的漏洞",
    "The system has vulnerabilities, and a patch has not yet been released.":
        "系統有漏洞且修補尚未發布",
    "The time to remediate vulnerabilities that do not exist is excessive.":
        "修補不存在漏洞耗時過多",
    "The user jsmith's account has been locked out.": "使用者 jsmith 的帳號已被鎖定",
    "Threat intelligence feed": "威脅情報來源",
    "Time-based logins": "時間型登入",
    "To activate the license for the file": "為檔案啟用授權",
    "To address audit findings": "處理稽核發現",
    "To allow for business insurance to be purchased": "讓商業保險可被購買",
    "To analyze code for defects that could be exploited": "分析程式碼中可能被利用的缺陷",
    "To automate the reduction of duplicated data": "自動化減少重複資料",
    "To calculate the checksum of the file": "計算檔案的校驗值",
    "To collect remediation response times": "蒐集補救回應時間",
    "To continuously the monitor hardware inventory": "持續監控硬體清冊",
    "To defend against insider threats altering banking details": "防禦內部威脅竄改銀行明細",
    "To determine the cost associated with patching systems": "判定修補系統的相關成本",
    "To determine the impact in the event of a breach": "判定違規事件的影響",
    "To discover which systems have been affected": "發現哪些系統受影響",
    "To eliminate false positives from a vulnerability scan": "消除弱點掃描的誤判",
    "To ensure non-repudiation": "確保不可否認性",
    "To ensure that errors are not passed to other systems": "確保錯誤不被傳遞到其他系統",
    "To eradicate any trace of malware on the network": "根除網路上的所有惡意軟體痕跡",
    "To extend the length of time data can be retained": "延長資料可保留的時間",
    "To gather IoCs for the investigation": "為調查蒐集 IOC",
    "To hunt for active attackers in the network": "在網路中獵捕活躍的攻擊者",
    "To identify unused ports and services that should be closed":
        "識別應該關閉的未用 port 與服務",
    "To improve a system's resource utilization": "改善系統的資源利用率",
    "To manage data storage requirements better": "更好地管理資料儲存需求",
    "To meet compliance standards": "符合合規標準",
    "To mitigate risks associated with unencrypted traffic": "減緩未加密流量的相關風險",
    "To prevent future incidents of the same nature": "防止未來同類型事件再次發生",
    "To prevent unauthorized changes to financial data": "防止未授權變更財務資料",
    "To prioritize the remediation of vulnerabilities": "優先化漏洞修補",
    "To remediate technical debt": "補救技術債",
    "To test the integrity of the file": "測試檔案完整性",
    "To track the status of patching installations": "追蹤修補安裝的狀態",
    "To validate the authenticity of the file": "驗證檔案的真實性",
    "Transitioning the platform to an IaaS provider": "把平台轉移到 IaaS 供應商",
    "Transport Layer Security": "傳輸層安全 (TLS)",
    "Transport layer security": "傳輸層安全 (TLS)",
    "Tuning the DLP rule that detects credit card data": "調校偵測信用卡資料的 DLP 規則",
    "Two-factor authentication": "雙因素驗證 (2FA)",
    "UTM utilizing a threat feed": "UTM 搭配威脅情報來源",
    "Uninterruptible power supply": "不斷電系統 (UPS)",
    "Update policies and handbooks to ensure all employees are informed of the new procedures.":
        "更新政策與手冊讓員工知悉新程序",
    "Update the EDR policies to block automatic execution of downloaded programs.":
        "更新 EDR 政策阻擋下載程式自動執行",
    "Update the acceptable use policy.": "更新可接受使用政策 (AUP)",
    "Update the content of new hire documentation.": "更新新進員工文件內容",
    "Update the current version of the software.": "更新到最新版本的軟體",
    "Updating processes for sending wire transfers": "更新電匯流程",
    "Updating the categorization in the content filter": "更新內容過濾器的分類",
    "Upgrade end-of-support operating systems.": "升級結束支援的作業系統",
    "Use 802.1X on all devices connecting to wireless.": "對所有連線無線的裝置使用 802.1X",
    "Use Group Policy to enforce password expiration.": "用 GPO 強制密碼到期",
    "Use hexdump on the file's contents.": "對檔案內容使用 hexdump",
    "Use of insecure protocols": "使用不安全的協定",
    "Use the IR plan to evaluate the changes.": "用事件回應計畫評估變更",
    "User-based firewall policies can be correctly targeted to the appropriate laptops.":
        "使用者為基的防火牆政策可正確套用到對應筆電",
    "Users can be mapped to their devices when configuring software MFA tokens.":
        "設定軟體 MFA 令牌時可將使用者對應到其裝置",
    "Users can install software that is not on the manufacturer's approved list.":
        "使用者可安裝不在廠商核可清單內的軟體",
    "Using a cloud provider to create additional VPN concentrators":
        "用雲端供應商建立額外的 VPN 集中器",
    "Using a proxy for web connections from the remote desktop server":
        "對遠端桌面伺服器的 Web 連線使用代理",
    "Using a spreadsheet for tracking changes": "用試算表追蹤變更",
    "Using an automatic change control bypass for security updates":
        "對安全更新使用自動變更控制繞過",
    "Using compile flags": "使用編譯旗標",
    "Using least privilege": "使用最小權限",
    "Utilizing a web-application firewall": "使用 Web 應用防火牆 (WAF)",
    "VPN IP address, company ID, facial structure": "VPN IP、公司識別碼、臉部結構",
    "Validate the code signature.": "驗證程式碼簽章",
    "Validating the accuracy of the evidence collected during the investigation":
        "驗證調查中蒐集證據的準確性",
    "Verifying information when modifying wire transfer data": "修改電匯資料時驗證資訊",
    "Version control tool": "版本控制工具",
    "Virtualization and isolation of resources": "資源的虛擬化與隔離",
    "Voice and fingerprint verification with an SMS one-time passcode":
        "語音與指紋驗證搭配 SMS OTP",
    "Vulnerabilities with a lower severity will be prioritized over critical vulnerabilities.":
        "低嚴重度漏洞被優先於嚴重漏洞處理（錯誤）",
    "Weak cipher suites": "弱密碼套件",
    "Web application firewall": "Web 應用防火牆 (WAF)",
    "Web application firewalls": "Web 應用防火牆 (WAF)",
    "Web proxy for all remote traffic": "對所有遠端流量使用 Web 代理",
    "Web-based administration": "基於 Web 的管理",
    "When conducting penetration testing, the security team will be able to target the most important devices first.":
        "進行滲透測試時，安全團隊能優先針對最重要的裝置",

    # Misc
    "A disruption of business operations": "業務營運中斷",
    "A full inventory of all hardware and software": "所有硬體與軟體的完整清冊",
    "A jump host in the shared services security zone": "共享服務區的跳板主機",
    "A list of system owners and their departments": "系統所有者與其部門清單",
    "A secure email solution": "安全郵件解決方案",
    "A website-hosted solution": "Web 託管解決方案",
    "Acknowledgement and attestation": "確認與證明",
    "Analyze IPS and IDS logs to find the IP addresses used by the attacker for reconnaissance.":
        "分析 IPS/IDS 日誌找出攻擊者偵察用的 IP",
    "Analyze application logs to see how the malware attempted to maintain persistence.":
        "分析應用日誌看惡意軟體如何試圖維持持續性",
    "Analyze endpoint and application logs to see whether file-sharing programs were running.":
        "分析端點與應用日誌看是否有檔案分享程式運作",
    "Analyze external vulnerability scans and automated reports to identify the systems most likely to be attacked.":
        "分析外部弱點掃描與自動化報告識別最可能被攻擊的系統",
    "Analyze firewall and network logs for large amounts of outbound traffic to external IPs.":
        "分析防火牆與網路日誌找出對外大量流量",
    "Analyzing the log files of the system components": "分析系統元件的日誌檔",
    "Attempting to achieve initial access to the DNS server": "試圖獲得 DNS 伺服器的初始存取",
    "Common Vulnerabilities and Exposures": "通用漏洞編號 (CVE)",
    "Company URL, TLS certificate, home address": "公司 URL、TLS 憑證、住家地址",
    "Cloud shared storage": "雲端共享儲存",
    "Browser message: \"Your connection is not private.\"": "瀏覽器訊息：「您的連線不是私密連線」",
    "Client-based soon": "客戶端為基（即將）",
    "More regular account audits": "更定期的帳號稽核",

    # Buffer overflow / vuln types
    "Buffer overflow attack": "緩衝區溢位攻擊",

    # Q449 VM escape
    "Malicious instructions can be inserted into memory and give the attacker elevated privileges":
        "可將惡意指令注入記憶體並賦予攻擊者提升的權限",
    "Malicious instructions can be inserted into memory and give the attacker elevated privileges.":
        "可將惡意指令注入記憶體並賦予攻擊者提升的權限",

    # Q475 MFA
    "Voice and fingerprint verification with an SMS one-time passcode":
        "語音與指紋驗證搭配 SMS 一次性密碼",
    "Voice and ngerprint verication with an SMS one-time passcode":
        "語音與指紋驗證搭配 SMS 一次性密碼",

    # Q484 memory injection
    "An executable is overwritten on the disk, and malicious code runs the next time it is executed.":
        "磁碟上的執行檔被覆寫，下次執行時運行惡意程式碼",
    "An executable is overwritten on the disk, and malicious code runs the next time it is loaded.":
        "磁碟上的執行檔被覆寫，下次載入時運行惡意程式碼",

    # Q540 environmental variables
    "The contents of environmental variables could affect the scope and impact of an attack.":
        "環境變數的內容可能影響攻擊的範圍與衝擊",
    "In-memory environmental variable values can be overwritten and used by attackers.":
        "記憶體中的環境變數值可被覆寫並被攻擊者利用",
    "Environmental variables will determine when updates are run and could mitigate the risk.":
        "環境變數會決定何時執行更新並可減緩風險",
    "Environmental variables define cryptographic standards for the system and could cause vulnerabilities.":
        "環境變數定義系統的密碼學標準，可能造成漏洞",

    # Q562 Security governance
    "Assigning roles and responsibilities for owners, controllers, and custodians":
        "為擁有者、控制者、保管者分配角色與責任",

    # Q4 ACL syntax options (keep technical but add brief Chinese)
    "Access list outbound permit 0.0.0.0/0 0.0.0.0/0 port 53 Access list outbound deny 10.50.10.25/32 0.0.0.0/0 port 53":
        "允許 0.0.0.0/0→0.0.0.0/0 port 53；拒絕 10.50.10.25/32→0.0.0.0/0 port 53（邏輯顛倒）",
    "Access list outbound permit 0.0.0.0/0 10.50.10.25/32 port 53 Access list outbound deny 0.0.0.0/0 0.0.0.0/0 port 53":
        "允許 0.0.0.0/0→10.50.10.25/32 port 53；拒絕 0.0.0.0/0→0.0.0.0/0 port 53（方向錯誤）",
    "Access list outbound permit 0.0.0.0/0 0.0.0.0/0 port 53 Access list outbound deny 0.0.0.0/0 10.50.10.25/32 port 53":
        "允許 0.0.0.0/0→0.0.0.0/0 port 53；拒絕 0.0.0.0/0→10.50.10.25/32 port 53（方向錯誤）",
    "Access list outbound permit 10.50.10.25/32 0.0.0.0/0 port 53 Access list outbound deny 0.0.0.0/0 0.0.0.0/0 port 53":
        "允許 10.50.10.25/32→0.0.0.0/0 port 53；拒絕 0.0.0.0/0→0.0.0.0/0 port 53（正確：只允許特定來源 DNS）",
    "access-list inbound deny ip source 0.0.0.0/0 destination 10.1.4.9/32":
        "ACL：拒絕 0.0.0.0/0 → 10.1.4.9/32 (任何來源到該目的地)",
    "access-list inbound deny ip source 10.1.4.9/32 destination 0.0.0.0/0":
        "ACL：拒絕 10.1.4.9/32 → 0.0.0.0/0 (該來源到任何目的地)",
    "access-list inbound permit ip source 0.0.0.0/0 destination 10.1.4.9/32":
        "ACL：允許 0.0.0.0/0 → 10.1.4.9/32",

    # Q6 BEC scenarios (full descriptions)
    "An employee receives a gift card request in an email that has an executive's name in the display field of the email.":
        "員工收到顯示主管姓名的郵件要求禮品卡",
    "Employees who open an email attachment receive messages demanding payment in order to access files.":
        "員工開啟郵件附件後收到付款要求才能存取檔案",
    "A service desk employee receives an email from the HR director asking for log-in credentials to a cloud administrator account.":
        "服務台員工收到來自 HR 主管的郵件，要求雲端管理員帳號登入憑證",
    "An employee receives an email with a link to a phishing site that is designed to look like the company's email portal.":
        "員工收到郵件含連結到偽裝成公司郵件入口的釣魚網站",

    # Q11 CEO smishing responses
    "Cancel current employee recognition gift cards.": "取消現行員工獎勵禮品卡",
    "Add a smishing exercise to the annual company training.": "在年度公司訓練中加入簡訊釣魚演練",
    "Issue a general email warning to the company.": "向公司發出一般性郵件警告",
    "Have the CEO change phone numbers.": "讓 CEO 更換電話號碼",
    "Conduct a forensic investigation on the CEO's phone.": "對 CEO 手機進行鑑識調查",
    "Implement mobile device management.": "實施行動裝置管理 (MDM)",

    # Q18 Zero Trust data plane
    "Secured zones": "安全區域",
    "Subject role": "主體角色",
    "Adaptive identity": "自適應身分",
    "Threat scope reduction": "縮小威脅範圍",
    "Policy engine": "政策引擎",
    "Policy administrator": "政策管理員",
    "Policy enforcement point": "政策執行點 (PEP)",
    "Policy decision point": "政策決策點 (PDP)",
    "PEP": "PEP 政策執行點",
    "PDP": "PDP 政策決策點",

    # Common attack vector options
    "Watering-hole": "水坑攻擊",
    "Watering hole": "水坑攻擊",
    "Drive-by": "Drive-by 路過下載",
    "Drive-by download": "Drive-by 路過下載",
    "Phishing campaign": "釣魚演練",

    # Common ZT components
    "Federation": "聯邦身分",
    "Identity proofing": "身分驗證",
    "Identity proofng": "身分驗證",
    "Default password changes": "更改預設密碼",
    "Password manager": "密碼管理器",
    "Password complexity": "密碼複雜度",
    "Open authentication": "Open Authentication",

    # Common DR strategies
    "Hot": "熱備站 (Hot site)",
    "Warm": "溫備站 (Warm site)",
    "Cold": "冷備站 (Cold site)",

    # Common single-word options
    "Phishing": "釣魚攻擊",
    "Vishing": "語音釣魚",
    "Smishing": "簡訊釣魚",
    "Whaling": "鯨釣 (針對高層)",
    "Pretexting": "假借身分",
    "Impersonation": "冒充",
    "Impersonating": "冒充",
    "Tailgating": "尾隨進入",
    "Typosquatting": "錯字搶註",
    "Misinformation": "假訊息",

    # Common physical/zone options
    "Air gapped": "氣隙網路",
    "Air-gapped": "氣隙網路",
    "DMZ": "DMZ 非軍事區",
    "Subnet": "子網",
    "Container": "容器",
    "Containers": "容器",
    "Containerization": "容器化",
    "Microservices": "微服務",
    "Monolithic code": "巨型應用 (Monolithic)",
    "Microsegmentation": "微分段",

    # Single-word controls
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

    # Risk strategies
    "Avoid": "規避 (Avoid)",
    "Accept": "接受 (Accept)",
    "Transfer": "轉移 (Transfer)",
    "Mitigate": "減緩 (Mitigate)",
    "Acceptance": "接受",
    "Avoidance": "規避",
    "Mitigation": "減緩",
    "Transference": "轉移",

    # Threat actors
    "Hacktivist": "駭客主義者",
    "Whistleblower": "吹哨者",
    "Organized crime": "組織犯罪集團",
    "Unskilled attacker": "技術不熟練攻擊者",
    "Nation-state": "民族國家",
    "Insider threat": "內部威脅",
    "Insider": "內部人員",
    "Shadow IT": "影子 IT",

    # Common short terms
    "Tokenization": "代符化",
    "Masking": "資料遮罩",
    "Steganography": "隱寫術",
    "Encryption": "加密",
    "Hashing": "雜湊",
    "Obfuscation": "程式碼混淆",
    "Authentication": "驗證",
    "Authorization": "授權",
    "Identification": "識別",
    "Compromise": "妥協",
    "Retention": "保留",
    "Analysis": "分析",
    "Inventory": "資產清冊",
    "Salting": "加鹽",
    "Sanitization": "資料淨化",
    "Destruction": "銷毀",
    "Classification": "資料分類",
    "Acquisition": "證據擷取",
    "Containment": "遏制",
    "Recovery": "復原",
    "Preparation": "準備",
    "Eradication": "根除",
    "Detection": "偵測",
    "Lessons learned": "經驗教訓",
    "Tuning": "規則調校",
    "Wired": "有線",
    "Wireless": "無線",
    "Sensitive": "敏感",
    "Confidential": "機密",
    "Public": "公開",
    "Private": "私有",
    "Restricted": "受限",
    "Critical": "關鍵",

    # Common options for short questions
    "Federation": "聯邦身分",
    "Salting": "加鹽",
    "Key stretching": "金鑰延展",
    "Data masking": "資料遮罩",
    "Brand impersonation": "品牌冒充",
    "SSO": "SSO 單一登入",
    "LEAP": "LEAP",
    "MFA": "MFA 多因素驗證",
    "PEAP": "PEAP",
    "Jump server": "跳板伺服器",
    "RADIUS": "RADIUS",
    "HSM": "HSM 硬體安全模組",
    "Load balancer": "負載平衡器",
    "NGFW": "NGFW 次世代防火牆",
    "WAF": "WAF Web應用防火牆",
    "TLS": "TLS",
    "SD-WAN": "SD-WAN",
    "Permissions assignment": "權限指派",
    "Access management": "存取管理",
    "Password complexity": "密碼複雜度",
}
