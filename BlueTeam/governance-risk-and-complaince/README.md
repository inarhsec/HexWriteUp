---
icon: building-columns
---

# Governance Risk And Complaince

## Governance Risk And Complaince.

* Governance: A rule which check the company is following the rules that match company goals.
  * Example: A principle make school rule for better enviroment.
  * Anology: MANAGE ALL THE THINGS (People, things) by managing.
* Risk: A Risk which impact my company.
  * Example: A PT Teacher check the playground is safe to play.
* Complaince: A policies and produces(Laws and regulations) which my company is using (like ISO,PCI-DSS).
  * Example: making sure the to learn all subjects
* G >> A Principle (Controling something). >> Certain amount approved by bank person.
* R: >> A playground which is safe to play. >> where 2 step verification is neede
* C >> LAW (Subject to teach) >> Follow rules by keeping records of all the approvals.

### Governance

* MANAGE ALL THE THINGS.
* where any thing start any migration anything its should have **STRATEGY (A ROAD , A PLAN OF ACTION).**
  * Strategy (a Road like Plan of action).
  * Policy ( What need to be done) >> (the policy tells why this rule matters).
  * Responsibility.
  * RISK.
* Understand the business requrement (visibility and everything).
* Build information strategy.
  * its talked about 5 years plan.
  * What the list of activities.
  * who is responsibile for thier things.
  * Risk management.
  * its will the 5 year plan in which it talk about the list of initiative, planning to do list , used in the organization.
  * then create the rsponsibility MATRIX (RACI). (**WHO DOES WHAT**).
  * Conduct risk assessmen (how to conduct ?).
  * Create program management. (security Program from information stratgey >> A tactical ) >> HOW ?
  * Then using that tactic build MATRIX.
  * POLICY >> RULE >> like wakeup for morning.
  * STANDARD >> defination >> like 7.00 PM is morning standard set.
  * ROLE and Responsibilties. >> So that form UPPER TO LOWER everyone know.
  * PROCEDURE is like ROUTIN to do.
  * Accountability and oversignt >> Check the report to get visibility.

Type of Governance.

CEO >> Organization Strategy.

CIO >> Information technology Strategy.

CISO >> Information security Strategy.

Security Manager >> Information security tactical planning.

Security Team >> Information security operation planning.

* **WITHOUT GOVERNANCE THERE IS NO IMPLEMENTATION.(ITS CHECK WHAT ARE THE RISK IN THAT IMPLEMENTATION).**
* Coperate Governance : Accountable for everything (The Founder of GRC).
* IT Governance: Align the planning with Coperate Governance.
* Information security Governance: Protect the assests. Data. RISK assessment.

Regulation >> LAWS >> As per the regulations.

* The REGULATION Cannot be change, (The policy has to be adjust as per the REGULATION with the stakeholders). AND THE STAKE HOLDERS NEED REGULATION.

THREE WINGS OF GRC.



<figure><img src="../.gitbook/assets/Fin Flow.drawio.png" alt=""><figcaption></figcaption></figure>

#### 1. What is **AEPS** (in very simple words)**AEPS = Aadhaar Enabled Payment System**

It is a payment system that allows customers to do banking transactions using:

* **Aadhaar number**
* **Fingerprint / biometric**
* **Bank name**

#### Examples of AEPS transactions

* Cash withdrawal
* Balance enquiry
* Mini statement
* Cash deposit

&#x20;No ATM card, no PIN — **Aadhaar + biometric** is enough.

***

#### 2. What is an **AEPS Switch**

Think of an **AEPS switch like a traffic police system** for AEPS transactions.

#### Simple flow

```
Customer → Micro-ATM → AEPS Switch → NPCI → Bank → Response back
```

The **AEPS switch**:

* Routes transactions to the correct bank
* Talks securely with NPCI & UIDAI
* Handles authentication responses
* Logs transactions
* Applies security controls

***

#### 3. Why **Finacus AEPS Switch** is used

**Finacus** is a technology provider that offers a **certified AEPS switch**.

Organizations use **Finacus AEPS switch** because:

* Building your own AEPS switch is **complex and risky**
* UIDAI & NPCI require **strict security and compliance**
* Finacus already provides:
  * UIDAI-compliant architecture
  * Encryption, HSM integration
  * Audit-ready systems
  * NPCI & UIDAI certifications

&#x20;So instead of reinventing the wheel, institutions use **Finacus**.

***

#### 4. Who are AUA / KUA (important for understanding the letter)

* **AUA (Authentication User Agency)**\
  → Entity that sends Aadhaar authentication requests
* **KUA (KYC User Agency)**\
  → Entity that uses Aadhaar for KYC
* **Sub-AUA / Sub-KUA**\
  → Downstream partners (BCs, fintechs, service providers)

If you use AEPS → **you are touching Aadhaar authentication** → UIDAI rules apply.



### ECOM

```
Ecom : is an service wich mapped the Application (service for the
shopping / buying) like Amazon has the option to
to using the Bank App (How it works) if the Bank app
how the Ecom Service to do the payment , where

MI code define the category of which Ecom service payment

Public  →→  GPS  →→  FinTech

Ecom
• where only payment done by website thro Bank card is use


```

### AEPS

#### AEPS (Aadhar Enabled Payment System)

• it a payment system that allows customer to do banking transaction\
with adhar number, Fingerprint, Bankname.

Customer → ATM → AEPS Switch → NPCI → Bank → Response back.

AUA → Send adhar authentication request.

KUA → User Agency → User Aadhar for KYC.

Sub AUA / KUA is Downstream partners.



### PAPG Flow

Payments initiated via UPI are collected in the PG’s HDFC collection account, processed in night batches, held in escrow for defined days, charges are deducted, and finally settled to the merchant using bank APIs integrated with the pay vertical API

```
           SK  →  UPA
                 |
                 |  @ details
                 v
      HDFC – Collection Account
      (This is PG collection account)
                 |
                 |  Night Batch
                 v
           Merchant Bank Account
                 |
                 |
 No. of days forwarded to Escrow (i.e.) Account
                 |
                 |
    Fees (Govt / misc charges deducted)
                 |
                 v
 Bank API integrated to Pay Vertical API
            (API / ICL)
```

* SK → UPA
* @ details
* HDFC collection account
* Night batch
* Merchant bank account
* Escrow holding
* Fees deduction
* Bank API → Pay vertical API

```
[ SK / User ]
      |
      |  UPI Payment (with details)
      v
[ Payment Gateway ]
      |
      v
[ HDFC Collection Account ]
      |   (PG Collection Account)
      |
      |  Night Batch Processing
      v
[ Merchant Bank Account ]
      |
      |  Escrow Holding (T+N Days)
      |
      |  Govt / PG Fees Deduction
      v
[ Bank APIs ]
      |
      v
[ Pay Vertical API (API / ICL) ]


```



### GPRS (The Heart)

the GPRS is the Public hosted web service to bank side\
through NATING from API

where the GPRS webconfig has configuration to get the\
Produced Data switch database. (UPI & ISO DB) on status\
to finance switch Monitor and using on product switch DB\
(UPI & ISO DB) for transactions & then response with status\
to give the response as needed from GPRS (customer input)

it get the information for another environment (CBS, NPCI, ATM)\
if it does't match.



### Database

Database (securing indexing) And Query optimizations.

• Finacus follow indexing and query optimizations, thru purging\
or 04 days of Month (every Month), the DB team remove the table\
to old with table, then the table has some data with the intern\
of Bank downtime. then will start the purging in which add the\
indexing to the table, then after adding the indexing feature Move / copy\
the 15 day data to that table, where thru indexing the\
query is optimized where after index in that data we searched\
the query of any Number of result is fast.



### EFRM

#### 1. Fraud Risk Monitoring (NPCI)

* Fraud risk rules are **defined and provided by NPCI**
* NPCI fraud rules work similar to **SIEM use cases**
* NPCI shares:
  * Risk parameters
  * Fraud indicators
  * Monitoring logic
* These rules are used to **identify suspicious transactions**

***

#### 2. Bank’s Responsibility in Fraud Monitoring

* NPCI provides **fraud response data** to the bank
* The bank:
  * Reviews NPCI fraud responses
  * Monitors risk trends
  * Takes actions based on risk level
* Bank is responsible for:
  * Risk monitoring
  * Alerts
  * Reports
  * Decision-making on fraud cases

***

#### 3. Finacus Role (Important Clarification)

* Finacus:
  * Monitors **successful and declined transactions**
  * Ensures correct transaction processing
* Finacus **does NOT**:
  * Perform fraud analysis
  * Analyze transaction behavior
  * Make fraud decisions
* Fraud analysis is **not part of Finacus scope**

