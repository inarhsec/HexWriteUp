# CTF 9 Insecuria

### 2.0 Introduction

* This involves the CTF Machine name ‘Machine Name’.

### 3.0 Independent Challenges

#### 3.1 Target 1 (IP Address)

#### 3.2 Network Service Enumeration

* Server IP Address
* Open PORTs
* IP Address (192.168.100.129)
* Port number (21,80,)

**Nmap Scan Result**

* Found these open ports in Nmap Scan.

#### 3.3 Enumeration

{% stepper %}
{% step %}
### FTP Enumeration

* `#passive` (to off the notification)
{% endstep %}

{% step %}
### Found the pub directory

* So there is a PUB directory and an FTP service running were read and write files are available.
{% endstep %}

{% step %}
### Web service on port 80

* On port 80 a normal IIS Microsoft service is running.
* And the `/pub` directory is unaccessable.
{% endstep %}

{% step %}
### Access the uploaded FTP file

* Then try to access the uploaded file of FTP.
* It works the ftp files are mounted or link with Microsoft IIS.
* So the IIS execute ASP and ASPX files, it can leverage to get reverse shell.
* Found some local ASP shells.
{% endstep %}

{% step %}
### Upload the shell.aspx file

Put the shell.aspx using ftp

* Read the shell and found it required x-forwarded header to shell to work,
* It give the reverse shell of it own 127.0.0.1 and redirected into web page.
* Use revshell to get the reverse shell.
{% endstep %}

{% step %}
### Try PowerShell payloads

* Try powershell payload from powershell #1 till powershell #3 base64.

A user is in system directory weird
{% endstep %}
{% endstepper %}

#### 3.5 Privileged Escalation - (Name of the Vulnerability).

* Vulnerability Explanation:
* Vulnerability Fix:
* Severity: Level.

#### Steps to Reproduce

{% stepper %}
{% step %}
### Analyze the issue

* the analysed issue.
* Try load powershell and powershell\_execute to exeute winpeas for privileges escation and the shell and powershell `-ExecutionPolicy Bypass -File .\winPEAS.ps1` works or `./winpeas.exe`
{% endstep %}

{% step %}
### Interesting Services -non Microsoft-

? Check if you can overwrite some service binary or perform a DLL hijacking, also check for unquoted paths https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services

```
=================================================================================================

WinSMS(Dolsin Business Solutions - WinSMS)[C:\Program Files (x86)\WinSMS\WinSMS.exe] - Autoload - No quotes and Space detected

File Permissions: Everyone [AllAccess]

Possible DLL Hijacking in binary folder: C:\Program Files (x86)\WinSMS (Everyone [AllAccess])

=================================================================================================

RegPath: HKLM\Software\Microsoft\Windows\CurrentVersion\Run

Key: VMware User Process

Folder: C:\Program Files\VMware\VMware Tools

File: C:\Program Files\VMware\VMware Tools\vmtoolsd.exe -n vmusr (Unquoted and Space detected)

=================================================================================================

RegPath: HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders

Key: Common Startup

Folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup (Unquoted and Space detected)

=================================================================================================

RegPath: HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders

Key: Common Startup

Folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup (Unquoted and Space detected)

=================================================================================================

RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon

Key: Shell

Folder: None (PATH Injection)

File: explorer.exe

=================================================================================================

RegPath: HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot

Key: AlternateShell

Folder: None (PATH Injection)

File: cmd.exe

=================================================================================================

RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Font Drivers

Key: Adobe Type Manager

Folder: None (PATH Injection)

File: atmfd.dll

=================================================================================================

RegPath: HKLM\Software\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Font Drivers

Key: Adobe Type Manager

Folder: None (PATH Injection)

File: atmfd.dll

=================================================================================================

RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32

Key: aux

Folder: None (PATH Injection)

File: wdmaud.drv

=================================================================================================

=================================================================================================

RegPath: HKLM\Software\Classes\htmlfile\shell\open\command

Folder: C:\Program Files\Internet Explorer

File: C:\Program Files\Internet Explorer\iexplore.exe %1 (Unquoted and Space detected)

=================================================================================================

=================================================================================================

RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls

Key: _wow64cpu

Folder: None (PATH Injection)

File: wow64cpu.dll

=================================================================================================

RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls

Key: _wowarmhw

Folder: None (PATH Injection)

File: wowarmhw.dll

=================================================================================================

Folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup

File: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\desktop.ini (Unquoted and Space detected)

=================================================================================================

Folder: C:\windows\tasks

FolderPerms: Authenticated Users [WriteData/CreateFiles]

=================================================================================================

Folder: C:\windows\system32\tasks

FolderPerms: Authenticated Users [WriteData/CreateFiles]
```

* So this service is allowed for everyone. WinSMS.exe
{% endstep %}

{% step %}
### Service payload and replacement

* Try .exe payload on winsms but no luck
* Created an exe-service payload

Copy the original one to backname

Remove the original winsms and upload the payload

Reload the system

Background the sessions
{% endstep %}

{% step %}
### Privilege escalation achieved

Got the privileges escalated.
{% endstep %}

{% step %}
### SSH

Ssh
{% endstep %}
{% endstepper %}

#### 3.6 Post Exploitation (Local or Proof Flags).

* System proof Screenshot.
* Final Proof Flags.
* Goodies.

#### 3.7 Failed Attempted
