# CTF 5. EscalateMe

### 1.0 Team Information

### 2.0 Introduction

* This involves the CTF Machine name ‘EscalateMe.

### 3.0 Independent Challenges

#### 3.1 Target 1 (192.168.100.135)

#### 3.2 Network Service Enumeration

* Server IP Address
* Open PORTs
* IP Address (192.168.100.135)
* Port number (80,111,139,445,2049, RPC Services)
* Nmap Scan Result
* Found these open ports in Nmap Scan.

#### 3.3 Enumeration

* Netdiscover
* NSE.
* Fuzz the application.
  * There is shell.php in web application
* Burpsuite listing.
* On the internet Stuff.

#### 3.4 Initials Access - (Publicy open php shell).

* Vulnerability Explanation:
* Vulnerability Fix:
* Severity: Level

**Steps to Reproduce**

* Analysed the issue.
* Try to bypass Fail Or successful.
  * Used the online resever shell generator to get the local access with encodeing

#### 3.5 Privileged Escalation - (Custom binary is vulnerably to path injection ).

* Vulnerability Explanation: there is custom binary which is /user/home/script which works similar like linux ‘ls’ but its has root privilege in execution and in that there is no path define for custom binary.
* Vulnerability Fix: a normal user doesn’t have the privilege to add path.
* Severity: Level.

**Steps to Reproduce**

* the analysed issue.
  * Find the binary which has SUID and redirect the saved output to /dev/null is nothings.
* There is custom id /user/home/script works like ‘ls’

Checking if this script has SUID.

There is SUID means the process is running in the backend there are ways to find the process and path one by manual and second by automation like pspy

To download pspy which done direct from interent using wget or by hosting a python server.

Give the execution permission.

```bash
chmod +x pspy64
```

Use the whoami binanry and replace it with ls binary using path injection

Create and upload a custome bash script which uses SUID with the `#bash -p`

<details>

<summary>Q: What is bash -p?</summary>

A: The -p option in bash is used to prevent the running of the startup files (.bashrc and .bash\_profile) when the shell is invoked as a login shell. This can be useful when you want to avoid running any commands or configurations from these files.

</details>

#### 3.6 Post Exploitation (Local or Proof Flags).

* System proof Screenshot.
* Final Proof Flags.
* Goodies.

#### 3.7 Failed Attempted

### Acknowledgement
