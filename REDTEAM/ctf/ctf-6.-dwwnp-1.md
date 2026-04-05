# CTF 6. Dwwnp 1

### 1.0 Team Information

### 2.0 Introduction

* This involves the CTF Machine name ‘Machine Name’.

### 3.0 Independent Challenges

#### 3.1 Target 1 (192.168.100.138)

#### 3.2 Network Service Enumeration

* Server IP Address
* Open PORTs
* IP Address (192.168.100.138)
* Port number (22,80,3306)

**Nmap Scan Result**

* Found these open ports in Nmap Scan.

#### 3.3 Enumeration

* TTL Value of OS identification.
* Netdiscover
* NSE.
* Fuzz the application.
* Burpsuite listing.
* On the internet Stuff.

#### 3.4 Initials Access - (MYSQL Exploited to Null Session).

* Vulnerability Explanation: its not a vulnerability is a misconfiguration which the developer has forget to add password in MySQL session.
* Vulnerability Fix: The Backend service MYSQL has Null session, it should not be open if needed then strong password should be implement.
* Severity: Crtitical.

#### Steps to Reproduce

* Analysed the issue.
* Try to bypass Fail Or successful.

MYSQL NULL SESSION

`#mysql –h <target-ip> -u ‘root’`

Found the SSH Credentials

```
+----+----------+---------------------+

| id | username | password            |

+----+----------+---------------------+

|  1 | mistic   | testP@$$swordmistic |

+----+----------+---------------------+
```

Permission Checks

Login with SSH

#### 3.5 Privileged Escalation - (Misconfigured CronJob Using Root Privileges).

* Vulnerability Explanation: Cronjob is Executing with root privileges.
  * What is cronjob: Its a code with is specified task with done automated by request code on cron basics which are minutes to yearly.
* Vulnerability Fix: to mitigate this if the cron job is for user then it should be executed by user.
* Severity: Critical.

#### Steps to Reproduce

* the analysed issue.

Enumeration with Linpeas

https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses

Answer: /usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/mistic/.local/bin:/home/mistic/bin

Finding SUID Misconfiguration

```
sudo -l #Check commands you can execute with sudo

find / -perm -4000 2>/dev/null #Find all SUID binaries

sudo awk 'BEGIN {system("/bin/sh")}'

sudo find /etc -exec sh -i \;

sudo tcpdump -n -i lo -G1 -w /dev/null -z ./runme.sh

sudo tar c a.tar -I ./runme.sh a

ftp>!/bin/sh

less>! <shell_comand>
```

CronJob

What Is the time when is file is executing which is

So it every 3minutes

* There are serval ways to Privilege escalate.
  * Configure SUID Binary,
  * Upload a reverse shell. --> becuase the cronjob use root will get the shell on Root.
  * Cp /etc/shadow & passwd to /tmp --> Brute Force.
* Let go with the easy way first.
* Check this cronjob is Executed by root ? YES.
* Is mistic user has the permission to read write and execute the CronJob File ? YES
* Check if changeing the script is really effecting ? YES.

Wait for 3minutes and the files is created which mean user can aad the custom code.

* Now the SUID is binded with User.

#### Steps to Reproduce Way 2

* With Revershell.

Listing

* Injection Shell

After waiting for 3min got the reverse shell

#### 3.6 Post Exploitation (Local or Proof Flags).

* System proof Screenshot.
* Final Proof Flags.
  * Now the SUID is binded with User.
* Goodies.
* House Cleaning.

#### 3.7 Failed Attempted

* Brute forcing the /etc/shadow

```
root:$6$r1sunFHLbyfPzQMy$Zb.3q.qIxfhtYwUGmrWJUqgIfM/KmI.uifkCrYlOKMGYdGol1AuxNuVF38/eMR..evbET0phOBYOsRN9YtgcZ/::0:99999:7:::
```

### Acknowledgement
