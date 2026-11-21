---
icon: building-columns
---

# SSCP

## Introduction.







* **Domain 1 – Security Concepts & Practices**: foundations, controls, defense-in-depth, change/configuration/asset management, social engineering, physical security, code of ethics.
* **Domain 2 – Access Controls**: IAAA, IAM, MFA and passwordless, SSO/RSO, authorization models, auditing/accounting, AD/LDAP, privileged access, trust and federation.
* **Domain 3 – Risk Identification, Monitoring & Analysis**: risk terms, identification and analysis, evaluation and response, reporting/monitoring, frameworks, architecture basics, vulnerability and security testing, SOC, logging, FIM, EDR/NDR/XDR/SOAR.
* **Domain 4 – Incident Response & Recovery**: threat types (malware, DoS/DDoS, MITM, app attacks), IR plan and metrics, evidence handling, DRP/BCP, recovery strategies, legal and privacy considerations.
* **Domain 5 – Cryptography**: symmetric and asymmetric crypto, hashing and salting, digital signatures and certificates, PKI, practical encryption uses, key management fundamentals, web of trust.
* **Domain 6 – Network & Communications Security**: OSI/TCP-IP, DNS, segmentation, email security, proxy/content filtering, RF and Bluetooth/NFC, IoT/edge, device placement, secure channel concepts.
*   **Domain 7 – Systems & Application Security**: endpoint hardening and tools, backup basics, secure SDLC, testing and secure coding, virtualization/containers and their security, enterprise computing and storage, cloud models and shared responsibility, data lifecycle/DLP/DRM/TPM, third-party and personnel security, SSAE/SOC reports.

    <br>

Use the Companion Excel to tick completion, log your confidence per lecture, and add one-line notes on what to review. If your confidence is low in a domain, filter the sheet and revisit those lectures first. Whether you choose the 3-month or 6-month plan, this roadmap keeps your progress visible and your study time focused where it matters most for the SSCP exam.



### Resource

{% file src=".gitbook/assets/SSCP_6_Month_Plan+-+Cyvitrix+Learning+Nov+2025.pdf" %}

{% file src=".gitbook/assets/SSCP_3_Month_Plan+-+Cyvitrix+Learning+Nov+2025.pdf" %}

{% file src=".gitbook/assets/SSCP+Companion+Tracker.xlsx" %}



## Domain 1 Security Concepts

Principle 1: Confidentiality\
Confidentiality restricts sensitive information to authorized users\
• Access limited to those with proper authorization\
Controls include encryption, access control, authentication\
• Principle of least privilege enforces minimal access\
Breach prevention via strong credentials and access reviews\
• Examples: passwords, multi-factor authentication, access audits\
Data remains unintelligible if encrypted without key\
• Encryption protects data even when compromised





Principle 2: Integrity\
Integrity ensures data accuracy, consistency.\
trustworthiness\
• Only authorized parties may alter information\
Unauthorized or accidental changes must be detected\
• Prompt response to changes is required\
Critical for environments with transaction-dependent\
decisions\
• Example: alterations have legal, economic impact in finance\
Preserved using hashing, signatures, audit trails,\
access lists\
• Enables detection and verification of changes





Principle 3: Availability\
Availability ensures data is accessible to authorized\
users\
• Required whenever resources are needed\
Addresses service disruptions and denial-of-service\
attacks\
• Examples include outages and attacks that limit access\
Achieved with redundancy, backup, disaster recovery\
plans\
• Solutions like failover clusters, load balancing, DR planning\
Maintenance, patching, capacity planning keep services\
operational\
• Prevents downtime and supports critical operations





Measuring Security Controls with the CIA Triad\
CIA triad benchmarks all security controls' effectiveness\
• Controls must support confidentiality, integrity, or availability\
Control evaluation considers triad contribution\
•Assessment focuses on triad element preservation\
Firewalls preserve confidentiality\
• Block unauthorized data access\
Other controls may support multiple triad objectives\
• Example: access control and audit logs for confidentiality, integrity





Ongoing Process and the D-A-D Triad\
Threats\
CIA triad implementation is a continuous, evolving process\
• The threat landscape and attacker tactics change constantly\
Attackers aim to undermine the CIA via the D-A-D triad\
• D-A-D: disclosure, alteration, denial\
Disclosure breaches confidentiality through unauthorized\
access\
• Leads to privacy issues or theft\
Alteration and denial attack integrity and availability\
• Include data tampering and service disruption



To Protect the CIA form DAD the Defence in Dept is in placed.

Defense in Depth: Layered Security\
Controls\
Organizations adopt defense in depth for layered\
protection\
• Combines multiple control types for triad coverage\
Technical controls: firewalls, IDS/IPS, encryption, anti-\
malware\
• Secures systems with technical solutions and configurations\
Administrative controls: policies, training, au\
response plans\
• Sets behavior standards and incident response\
Physical controls: security guards, biometric\
surveillance, access points\
• Protects physical assets and infrastructure



Supplementary Principles: Authenticity and\
Non-Repudiation\
Authenticity verifies true identity of users, devices, systems\
• Prevents impersonation and builds trust\
Authenticity maintained via biometrics, certificates, tokens\
• Used for secure authentication (e.g., VPN smart card)\
Non-repudiation ensures actions cannot be denied later\
• Mandatory for accountability, audits, dispute resolution\
Non-repudiation via signatures, audit logs, transaction approvals\
• Example: OTP and audit trail for online transactions
