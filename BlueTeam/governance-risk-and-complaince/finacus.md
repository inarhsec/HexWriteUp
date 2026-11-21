# Finacus

## Policy DOCUMENT

### INFRASTRUCTURE and design document.

* Nessus and Zenmap PT Tools.
* Used sarbras SFTP.

### Information Securty Policy v1

Aims >> is CIA and ISO27001.

4. SCOPE >> IT Policy apply to all FINACUS SOLUTION.

7.KEY Risk Indicator and Key Performance Indicator.

* Incidents: How often bad thing happend.
* TTD: how fast we see the bad thing.
* TTR: how fast we fix the bad thing.
* Access attempt: who trying to break in.
* Patch Compliance: how many open holes we left.
* Third party : how risky our vendors are.
* Phisping: how easily staff can be fooled.
* Data Loss: if sensitive data escape.

Key Proformace Indicator.

* Policy Compliance: rule followed.
* Awareness: People trained.
* Patching: hole fixed fast.
* SOC: alerts handled well
* Hardedning: strong systems
* Controls coverge
* Audit closure: fixes done.

Incident Response Policy.

* Classify : How bad is it.
* Assign: Who does what.
* Detect and report: how we find it, how we log in.
* Communicate: who we tell how we tell them.

### IT Policy

Overwire and Objective:

* Why does Finacus have an IT Policy :
* because its should have all the standard document process and maintain that process that why we have.

Scope:

* you’ll check if _everyone in this scope has actually signed or acknowledged the policy._
* its cover all the IT department and persons. Why not all the department.

Policy Statement

* Follow complaince standard.
* Use IT resources Responsibly.
* User access control.
* Report Incident.
* Awareness Training.

Role and Responsibilities.

Who is accountable if policy is not followed

#### **Comparison with IT Security & Cybersecurity Policy**

* IT Policy = **umbrella (governance, usage, procurement, asset mgmt).**
* IT Security Policy = **subset (access control, encryption, password mgmt).**
* Cybersecurity Policy = **threat-focused (malware, phishing, monitoring).**

In the information Security policy its cover.

* mention all the list with is coverd in IT.
* The KRI and KPI (KRI is the risk which is impact to finacus. and the KPI is the how many risk we have known and closed.
* there are access control policy which is RBAC, RBAC review , MFA, PAM, and its have the topic and overwiew of policy which come undes IT.

In the information security policy its coverd all the DATA related to Finacus and in the IT security Policy as IT is the backbone of any organization its has its own policy which cover the Infrasturture.

Cybersecurity Policy.

* Overview : its protect the CIA with the adopt aproch.
* Role and responsibilites: Its defined its role to every stakeholder as need in cybersecurity part.
* its policy has same as IT security policy but have some points like Vulnerability management , Encryption policy , Change management, patch management.SSDP( i dont know what is SSDP), MDM and Awareness training.

Quality Management System

* How the work is done with constantly.
* overview: Its should updated all the thing.
* scope : all business processes that impact product/service quality
* Quality Objective: define the SLA and the percentage for the day to day thing.
* Principle : follows the **ISO 9001:2015 standart (which i dont know sadly)**
  * its take customer review, and leadership have clear focus with the review meeting.
* RACI:its has its RCAI to every document to maintain and more.
* Key process:
  * requirement : its define what are the requirement for this process.
  * SDDL : mention the framework of project management.
  * how Finacus ensures quality in every service/project.

Assets Classification and Inventory (Management) Policy.

* Overview: its insured that assest are proper there and maintained. (what assets we have and how its secured.)
  * Classify, manage and protect assets.
    * Protect where control are applied like
    * A customer UPI database is high classification >> Protect with encryption and RBAC, MFA and firewall.
* Scope:
  * **Tangible assets** (hardware, infra).
  * **Intangible assets** (IP, brand).
  * **Financial assets** (funds, accounts).
  * **Information assets** (data, documents, software).

Policy statement

* Assets much be label with CIA
* control must be used.
* Overall assest lifecycle much be maintain like Employee laptop → Allocated with IT checklist → Used securely with antivirus → When resigned → Data wiped + asset logged as disposed.
* Retention and disposal must be followed as per Complaince.

Procedures.

* every assest must have an owner and the owner should decide the CIA.

Assest Procurement(Getting Something) and Disposal Policy

* Overviwe: Its the policy for getting the assets and disposing the assest.
  * Procurement(BUYING):
    * check if the new assest based on the operational requirement
    * check to have financial and approvals.
    * check the transparent for getting the vendors. and the acquistion and documentation should be maintain with the assest register.
  * Asset disposal.
    * Check the asseset is damaged or no need because the disposal. also whether its can resale or donate before disposal.

Change management (in this there is no metion of two level of approval)

Overviwe : any modification happen goes thoru change management process.

Scope: any changes of application, infrasture,business has to go thoru change management system.

Change approval authorization types.

Policy 008 Cryptography.

Overviwer: its an policy which set the rule of encryptions.

* Cryptographic are generate using FIPS 140 Compliant modules.
* its follows the PCI-DSS and PA-DSS standard and the RBI Advisories.
* An inventory of Hardware security Modules and Secure Crytpographic Devices for key management.

Policy 009 Adhar Policy

Overviwer: its an policy for adhar card collection and stoarging secure information of adhar card.

* Collection : its collect the biomeritc and detailts of authentication. and used the data under the Aadhar Act 2016..
* adhar card number must be masked when display or stored.
* Authentication and complaince is Digital personal data protection act 2023.

Policy 010 A Data Policy

Overview:its rule for all the data protection processing activitly.

Policy 010 B Data Policy (Backup/stoarge/archival/retention.

the objective of this policy is to ensure the integrity and availability (recoveryable)

* Backup operaetions are encrypted and backup checklists
* All the data is is accessible for one year period then its goes to Archived (NAS).
* the logs are retention and the period off 2 years with the types of event logs, CCTV logs and transcation logs (10 Years).

Policy 011 C Data Privacy Policy for PII.

its the policy for PII data and third party information.

* Data at rest is encrypted. and Data in transit with SSL 2048 Encryption. where application is AES algo. also the NPCI standard of TLS 1.2 and SSL 3.
* Sensitive personal information the finacus doesn’t store the card details.
* Information sharing and disclosure.
* Cookies : any finacus website cookie is contained.
* its has appointed the GRC officer.

Policy 012 Network Management (Network Security Policy)

* Its apply all the network related in Finacus.
* The NOS Network Operation system is adhere to Minimum Baseline security standard.
* As per RBI Adviosries defence in depth is in place with protecting enclave boundaries (Network Perimeters) and securing the internal computing enviroment.

Policy 013 Physical and Enviroment Policy

* Its an for physical and enviroment to protect against the fire,flood and physical security. where the physical entry controls and all.
* this policy has everything related to physical entry to finacus solution even if its new joiny or visitor.
* the Secure ares of server access controls. for the server and the storage media.

Policy 014 Third Party Vendors Policy.

* This all to the vendors for finacus.

Policy 015 Incident Mgmt Policy

* its an policy to any kind of incidents with theSeverity levels.

Policy 016 Malicious code antivirus policy

* this policy apply to all the emyploye and assests to finacus solution.
* daily av monitoring the Av installation and the AV policy. of Sophos AV. where Email and Web filering is used.
* the AV logs retention period is 3 mouths.

Policy 017 Patch Management Policy.

Its to find, test deploy and verification of software patches and updates.

* Its the quartley review by the local IT Team.

Policy 018 Information (data) Tranfer Policy

its the policy to have data/information should be protected CIA throu lifecycle.

its the policy where it said that data in transmit and data at rest should be encrypted.

Policy 019 Logical Access Policy

its the policy which defined the rules for User access Controls, which focus on user has the least access with need to know access with the records.

* Has the password policy. with the MFA.

Policy 020 Email Poicy.

*

ATM Switch:

Its the software server on windows where its forward and recevie the transcation.

* the vendous are Nokia and H3h
* **PVCs (Permanent Virtual Circuits)** and **SVCs (Switched Virtual Circuits)**
  * PVCs is the static Path which remain active untill its removed.
  * SVCs is created dynamicaly such as an trancation request comein and out and then removed afterward.
* Configuration
  * Enable ATM interface on router and switch
  * Create PVCs specifying VPI/VCI pairs (Today, most banks/Fintechs (including Finacus) use IP/MPLS networks, not ATM cells, so you won’t configure VPI/VCI yourself.)
  * Match configurations across endpoints
  * Use point-to-multipoint PVCs if supported

***

PCI DSS - its has three type of forms. to complete the PCI DSS.

* **ROC** = the **full exam paper** (detailed answers checked by auditor).
* **AOC** = the **mark sheet** (auditor signs “passed” or “failed”).
* **COC** = the **trophy/certificate** you show everyone that you passed PCI DSS.<br>



### Finacus Assesment



Finacus

* Local AD Password Policy doen't work i can have 11 Charactes password.
* updated the policy document control from 1.2,2.1,2.1 to different version.
* Bank Specific Diagram. (At least Name should be there(
* Physical and enviroment report monthly bases (Proactive details like RACK and Tempature).
* Network Diagram updates for Vlan 30 BBPS and PA880 should be removed.
* Change Management Policy Type of Changes must be defined. (High/Low).
* Change Management Procuduce Need to Change CRIM full form to correct One.
* outward Asset Resgiter is not updated.
* HR Policy Need to ADD timeline TAT for How many days BGV Should complete
  * need to change the 10days TAT to 60 Days (Exluding Adhar verification). BGV SLA not define.
* Diciplinary Process need to change because its only focus is in Information security Why ? and NO TAT defined its should cover other things
* Conduct Pestle Analysis in BIA and share the updated BIA report.
* BCP clause in the sla agreement.
  * Date when the persion signed.
  * Fequence of BCP Drill like 6 monthly
* Data Back Policy 10\_B in that 12.1 if the local.finacus backups are hardcopy PII data its destory.(should add another column for timeline.
* Should have different awareness traning for DATA PRIVACY with assessent.
* Patch Management policy 7.0 (General patch updates should be n-1).
* Session timeout is to be low in PA.
* Change Management Policy need to add type of changes, Policy should have classification. and Change Management Procuduce should have TAT with serverity.
* Need to Add PA 1410 in scope.
* Should have ewaste certificate.
* Data center Disk drill to ewaste not to keepit.
* SOC AV and DLP is not configured in Many devices.
  * SOC AV there are some PC with 2 year not scanned.
  * SOC AV and DLP policy is not proper configured.

***

The following updates are required in existing policies and procedures:

* Cryptographic Policy – Add section explaining the process of DEX and MEX.
* PCI S3 – Roles and Responsibilities – Include additional responsibilities.
* Training and Awareness PPT
* Add Social Engineering under common threats.
* Include Secure Coding (OWASP) practices to be followed by developers.
* Card Encryption SOP – Create/update SOP for card data encryption.
* Asset Management Policy – Specify that asset management is handled through Patch Manager Pro.
* Cardholder Data Handling Procedure – Update procedure to cover ATM, ECOM, POS and related environments.
* Retention Policy – Add details on the post-deletion process, including how data is securely deleted.
* Logical Access Policy
* Update minimum password length from 8 to 12 characters.
* Modify Section 7.3 approval process to: InfoSec → CTO.
* PCI DSS Charter (Quarterly Compliance Review) – Add the following points:
* User Access Review
* Half-Yearly Scope Sheet Review
* Annual Training
* Third-Party Risk Assessment
* Refrence of Restoration test process in the BCP procedure but document is not available.



