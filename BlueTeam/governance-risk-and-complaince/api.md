# API

## API Inventory Process

### Technical Notes – API Extraction from ATM and IMPS WSDL Files

#### Objective

To identify SOAP API operations from the ATM and IMPS WSDL files using `xmlstarlet` on a Linux system for API inventory creation.

***

#### 1. ATM WSDL Extraction

#### Step 1 – Inspect the file

Command:

```bash
head atm_wsdl
```

#### Observation

The file contained an extra text line (`ATM`) before the `<wsdl:definitions>` element:

```
ATM
<wsdl:definitions ...
```

Since a valid XML document must begin with an XML declaration or root element, the extra line prevented `xmlstarlet` from parsing the file.

***

#### Step 2 – Create a cleaned WSDL

Command:

```bash
tail -n +2 atm_wsdl > atm_clean.wsdl
```

This removed the first line and created a valid XML/WSDL file.

***

#### Step 3 – Extract SOAP operations

Command:

```bash
xmlstarlet sel -t -m "//*[local-name()='operation']" -v "@name" -n atm_clean.wsdl
```

#### Extracted Operations

* OpenCBSSession
* RetreviveMiniStatement
* RetreiveBalances
* DoTransaction
* RetreiveCustDetailsByMobileNumber
* RetreiveCustDetailsByAccountNumber
* ProcessMobileNumberUpdation
* ProcessStatementRequest
* ProcessChequeBookRequest
* ProcessCardlessCashWithdrawalRequest
* ProcessMobileBankingRegistration
* DoFundsTransferTransaction
* Convert15DigitTo32DigitAccount
* ValidateAccountForCashDeposit
* ProcessCustomerValidation

Duplicate entries were observed because WSDL operations are defined in multiple sections (`portType` and `binding`).

***

#### Step 4 – Remove duplicates

Command:

```bash
xmlstarlet sel -t -m "//*[local-name()='operation']" -v "@name" -n atm_clean.wsdl | sort -u
```

This produced the unique list of SOAP API operations.

***

#### 2. IMPS WSDL Extraction

#### Step 1 – Inspect the file

Command:

```bash
head IMPS_wsdl
```

#### Observation

The file started directly with:

```xml
<wsdl:definitions ...>
```

No cleaning was required.

***

#### Step 2 – Extract SOAP operations

Command:

```bash
xmlstarlet sel -t -m "//*[local-name()='operation']" -v "@name" -n IMPS_wsdl
```

#### Extracted Operation

* ProcessGlobalRequest

The operation appeared twice because it was defined in both the `portType` and `binding` sections.

***

#### Step 3 – Remove duplicates

Command:

```bash
xmlstarlet sel -t -m "//*[local-name()='operation']" -v "@name" -n IMPS_wsdl | sort -u
```

#### Result

* ProcessGlobalRequest

***

#### 3. Additional Metadata Extraction

#### Extract Service Name

```bash
xmlstarlet sel -t -m "//*[local-name()='service']" -v "@name" -n <wsdl_file>
```

Examples:

* ATM WSDL → Returns the configured service name.
* IMPS WSDL → `ImpsGlobalInterface`

***

#### Extract Endpoint URL

```bash
xmlstarlet sel -t -m "//*[local-name()='address']" -v "@location" -n <wsdl_file>
```

Example (IMPS):

```
http://fslntuat1638.fslntuat.local/Sanmitra_IMPS_GlobalInterface/ImpsGlobalInterface.svc
```

***

#### Extract SOAP Actions

```bash
xmlstarlet sel -t -m "//*[local-name()='operation' and @soapAction]" -v "@soapAction" -n <wsdl_file>
```

Example (IMPS):

```
http://tempuri.org/IImpsGlobalInterface/ProcessGlobalRequest
```

***

#### 4. Summary

| WSDL File   | Cleaning Required                | Unique Operations Identified |
| ----------- | -------------------------------- | ---------------------------- |
| `atm_wsdl`  | Yes (removed leading `ATM` line) | 15                           |
| `IMPS_wsdl` | No                               | 1                            |

The extracted operation names represent the SOAP APIs exposed by each service and can be used to populate an API inventory. Duplicate operation names are expected in WSDL files because operations are commonly declared in both `portType` and `binding` definitions.







## Moblie API Extract

### 1. ripgrep

Install:

```
sudo apt install ripgrep
```

Find all HTTP endpoints:

```
rg "http://|https://|ServiceURL|BaseUrl|BaseAddress" .
```

Find all API calls:

```
rg "PostAsync|GetAsync|PutAsync|DeleteAsync|SendAsync|HttpClient" .
```

Find all service keys:

```
rg 'Key\s*=\s*"[^"]+"' .
```





## Technical Procedure: Reverse Engineering the Mobile Application API Architecture (FinMobility Xamarin/.NET)

This document provides the exact technical procedure used to reverse engineer the mobile application's API architecture from the source code. It is intended for API inventory creation, GRC documentation, and security assessment.

***

## Objective

Identify:

* Backend API endpoint(s)
* HTTP communication method
* Logical API operations
* Source files invoking each operation
* Overall API architecture

***

## Environment

| Item             | Value                    |
| ---------------- | ------------------------ |
| Operating System | Kali Linux               |
| Source Code      | FinMobility Xamarin/.NET |
| Analysis Tool    | `ripgrep (rg)`           |
| Shell            | Bash                     |

***

## Step 1 – Identify Backend Service URLs

### Command

```bash
rg -n "ServiceURL\s*=" FinMobilityCGGB/
```

### Output

```
FinMobility.HttpClient/TestApis.cs
19: RestClient.ServiceURL = "https://uat.finacuspayments.com:4443/RAJ_THA_MAH_IN_XAM_GPRS_V2_UAT/wa/api/process"

FinMobilityPlus/Globals/AppGlobals.cs
12: public static readonly string ServiceURL =
"https://uat.finacuspayments.com:4443/APGB_GUN_AP_IN_XAM_GPRS_UAT_V1/wa/api/process"

FinMobilityPlus/AppShell.xaml.cs
46: RestClient.ServiceURL = AppGlobals.ServiceURL;

FinMobilityPlus/App.xaml.cs
44: RestClient.ServiceURL = AppGlobals.ServiceURL;
```

### Finding

The application uses a centralized backend endpoint named:

```
https://uat.finacuspayments.com:4443/APGB_GUN_AP_IN_XAM_GPRS_UAT_V1/wa/api/process
```

***

## Step 2 – Search for Hardcoded HTTP/HTTPS URLs

### Command

```bash
rg -n "https://|http://" FinMobilityCGGB/
```

### Findings

Relevant API endpoints discovered:

```
https://uat.finacuspayments.com:4443/RAJ_THA_MAH_IN_XAM_GPRS_V2_UAT/wa/api/process

https://uat.finacuspayments.com:4443/APGB_GUN_AP_IN_XAM_GPRS_UAT_V1/wa/api/process
```

Additional URLs were identified but correspond to:

* Bank websites
* PDF documents
* WhatsApp links
* Calculator pages
* Test/demo endpoints

These are **not backend APIs**.

***

## Step 3 – Enumerate Logical API Keys

### Command

```bash
rg -n 'Key\s*=\s*"[^"]+"' FinMobilityCGGB/ | grep -v App.xaml
```

### Output and Mapping

| Key                        | File                                 | Purpose                          |
| -------------------------- | ------------------------------------ | -------------------------------- |
| TOKEN                      | RestClient.cs                        | Token generation                 |
| GetTokenKeyService         | RestClient.cs                        | Obtain token                     |
| LoginValidateOthersService | RestClient.cs                        | Login validation                 |
| ALLATM                     | ATMViewModel.cs                      | Retrieve ATM list                |
| ALLBRANCH                  | ATMViewModel.cs                      | Retrieve branch list             |
| MOBVAL                     | LoginViewModel.cs                    | Mobile validation                |
| MOBVAL                     | DashboardViewModel.cs                | Mobile validation                |
| MOBVAL                     | ChangePinViewModel.cs                | Mobile validation                |
| MOBVAL                     | CardDetailViewModel.cs               | Mobile validation                |
| MOBVAL                     | MobileNumberVerificationViewModel.cs | Mobile validation                |
| SIList                     | StandingInstructionViewModel.cs      | Standing instructions            |
| INQUIRE                    | SSschemeViewModel.cs                 | Social security inquiry          |
| ADD                        | SSschemeViewModel.cs                 | Social security enrollment       |
| LoanView                   | LoanviewViewModel.cs                 | Loan details                     |
| BILLERCATEGORY             | BBPSViewModel.cs                     | BBPS biller categories           |
| BBPSACDETAILS              | BBPSViewModel.cs                     | BBPS account details             |
| BENFDETAILS                | BBPSViewModel.cs                     | Beneficiary details              |
| FdView                     | AccountSummeryviewModel.cs           | Fixed deposit details            |
| FdView                     | FDRDOptionsViewModel.cs              | Fixed deposit details            |
| FAQService                 | FaqData.cs                           | FAQ retrieval                    |
| HISTORY                    | CardlessCashWithdrawalViewModel.cs   | Cardless cash withdrawal history |
| GET                        | OpenFDRDViewModel.cs                 | Generic GET request key          |

***

## Step 4 – Determine Communication Pattern

Inspection of `RestClient.cs` identified:

```
HttpMethod.Post
client.PostAsync(ServiceURL)
```

### Finding

All requests are transmitted using:

```
HTTP Method: POST
```

***

## Step 5 – Determine Authentication Flow

The following keys were identified inside `RestClient.cs`:

```
TOKEN

GetTokenKeyService

LoginValidateOthersService
```

### Finding

The mobile application performs:

1. Token acquisition
2. Authentication validation
3. Business API invocation

***

## Step 6 – Determine API Architecture

Unlike traditional REST APIs:

```
GET /balance
POST /login
POST /fundtransfer
```

the application uses **one physical endpoint**.

Architecture:

```
                Mobile Application

                       │

         ┌─────────────┼─────────────┐

         │             │             │

      MOBVAL        ALLATM      FAQService

         │             │             │

         └─────────────┼─────────────┘

                       │

               POST /wa/api/process

                       │

                Finacus Backend API

                       │

            Dispatches using "Key"
```

***

## Step 7 – Final API Inventory

| Endpoint          | Method | Logical API                | Source File                          |
| ----------------- | ------ | -------------------------- | ------------------------------------ |
| `/wa/api/process` | POST   | TOKEN                      | RestClient.cs                        |
| `/wa/api/process` | POST   | GetTokenKeyService         | RestClient.cs                        |
| `/wa/api/process` | POST   | LoginValidateOthersService | RestClient.cs                        |
| `/wa/api/process` | POST   | MOBVAL                     | LoginViewModel.cs                    |
| `/wa/api/process` | POST   | MOBVAL                     | DashboardViewModel.cs                |
| `/wa/api/process` | POST   | MOBVAL                     | ChangePinViewModel.cs                |
| `/wa/api/process` | POST   | MOBVAL                     | CardDetailViewModel.cs               |
| `/wa/api/process` | POST   | MOBVAL                     | MobileNumberVerificationViewModel.cs |
| `/wa/api/process` | POST   | ALLATM                     | ATMViewModel.cs                      |
| `/wa/api/process` | POST   | ALLBRANCH                  | ATMViewModel.cs                      |
| `/wa/api/process` | POST   | ALLBRANCH                  | ApplyForLoanViewModel.cs             |
| `/wa/api/process` | POST   | LoanView                   | LoanviewViewModel.cs                 |
| `/wa/api/process` | POST   | FdView                     | AccountSummeryviewModel.cs           |
| `/wa/api/process` | POST   | FdView                     | FDRDOptionsViewModel.cs              |
| `/wa/api/process` | POST   | FAQService                 | FaqData.cs                           |
| `/wa/api/process` | POST   | BILLERCATEGORY             | BBPSViewModel.cs                     |
| `/wa/api/process` | POST   | BBPSACDETAILS              | BBPSViewModel.cs                     |
| `/wa/api/process` | POST   | BENFDETAILS                | BBPSViewModel.cs                     |
| `/wa/api/process` | POST   | SIList                     | StandingInstructionViewModel.cs      |
| `/wa/api/process` | POST   | INQUIRE                    | SSschemeViewModel.cs                 |
| `/wa/api/process` | POST   | ADD                        | SSschemeViewModel.cs                 |
| `/wa/api/process` | POST   | HISTORY                    | CardlessCashWithdrawalViewModel.cs   |
| `/wa/api/process` | POST   | GET                        | OpenFDRDViewModel.cs                 |

***

## Final Technical Conclusion

The reverse engineering process established that the FinMobility application uses a **single HTTP POST endpoint** (`/wa/api/process`) as a gateway for all backend communication. Rather than exposing multiple REST URLs, the application selects business functionality by embedding a **logical operation identifier (`Key`)** such as `MOBVAL`, `ALLATM`, `FAQService`, or `LoanView` in the request payload. Static analysis of the source code identified the endpoint configuration, authentication-related operations (`TOKEN`, `GetTokenKeyService`, `LoginValidateOthersService`), and the principal business operation keys, providing a solid foundation for creating a GRC API inventory and conducting further security or compliance reviews.
