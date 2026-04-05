# CTF 4 AutoPWN

### 1.0 Team Information

### 2.0 Introduction

* This involves the CTF Machine name `AutoPWN`.

### 3.0 Independent Challenges

#### 3.1 Target 1 (192.168.100.134)

#### 3.2 Network Service Enumeration

* Server IP Address
* Open PORTs
* IP Address (192.168.1.1)
* Port number (135, 139, 445)

**Nmap Scan Result**

* Found these open ports in Nmap Scan.
  * Results shows that the operating system is windows and the SMB file sharing service of windows is running.

#### 3.3 Enumeration

* TTL Value of OS identification.
* TTL `128` means its windows.
* Nbtscan
* WhatWEB.
* NSE for RDP.
* Fuzz the application for smb services.
  * SMBClinet
* There is a user `rob`
* Login into smbclinet.
* There is secre.txt which has rob password.
* Login using crackmapexec which currently know as netexec.
* SMBMAP
  * Anonymous Sessions
* Null Sessions not found.
* Burpsuite listing.
* On the internet Stuff.

#### 3.4 Initials Access - (SMB is publicly open)

* Vulnerability Explanation: SMB is windows files sharing service which doesn’t authenticated the user and has null session and anonymous session open the critical part is the password is available in text format in smb directory.
* Vulnerability Fix:
* Severity: medium

#### Steps to Reproduce

* Analysed the issue.
  * SMB is publicly open which has `.secert.txt`, which has the output contain password.
* Try to bypass Fail Or successful.
* Fuzzing the application of WinRM.
* Login using `R0bth3r0bb3r`

#### 3.5 Privileged Escalation - (HKEY\_USER registery Publicyly open)

* Vulnerability Explanation:
  * Register is some configuration files which is saved. Its stored session management files in registesty which also know as special folder with limit types of files like configuration of software and application etc
* Vulnerability Fix: need to be disclose for user.
* Severity: crtitical.

#### Steps to Reproduce

* the analysed issue.
* Downlaoding winpeas windows to enumerate the Windows os.
  * Its can be download by direct download of wget or hosting a python server.
* In evil-winrm execute the command to get sanitized output of winrm

```powershell
powershell -ep bypass
.\winpeas.ps1
```

**Example:**

* Ls "hklm (h key local machine)\software\microsoft\window nt\current version"
* Get-itemsproperty "hklm (h key local machine)\software\microsoft\window nt\current version\winlogon"
* Get itempropety"hklm (h key local machine)\software\microsoft\window nt\current version" | select defualt\*
* Links
* R0bth3A

#### 3.6 Post Exploitation (Local or Proof Flags)

* System proof Screenshot.
* Final Proof Flags.
* Goodies.

#### 3.7 Failed Attempted

### Acknowledgement
