# CTF 3. HappyCorp Refresh

### 1.0 Team Information

### 2.0 Introduction

* This involves the CTF Machine name ‘Happy Corp’.

### 3.0 Independent Challenges

#### 3.1 Target 1 (192.168.50.223/)

#### 3.2 Network Service Enumeration

* Server IP Address
* Open PORTs
* IP Address (192.168.1.1)
* Port number (22,80,111,2049,)

**Nmap Scan Result**

* Found these open ports in Nmap Scan.\
  Aggressive Scan

#### 3.3 Enumeration

* **NetDiscover**
  * Used to discover Hosts.
* TTL Value of OS identification.
* **WhatWEB.**
* **NSE.**
* Fuzz the application.
  * There is a robots.txt which output in admin.php which means php is configured.
* Fuzzing the directory
* **Burpsuite listing.**
* **Web Enumeration.**
  * Nikto
* Nuclei
* On the internet Stuff.

#### 3.4 Initials Access - (publicly open NFS and ssh key private).

* Vulnerability Explanation: NFS is publicly open and has a ssh private key.
* Vulnerability Fix:
* Severity: low

#### Steps to Reproduce

{% stepper %}
{% step %}
### Analysed the issue

* NFS
* NFS is a sharing file service for Linux OS, like smb for windows, similar to samba.
* Using the NFS ‘showmount’ which output in /home/karl \* , the star indicate that all files.
* Mounting the directory to Attacker files to view the /home/karl files.
* ‘Ls -la’ show the id of karl use which is ‘1001’, to read this file need a user which has ‘1001 id’
* Create a user which has ‘id 1001’ or change the user id.
{% endstep %}

{% step %}
### Try to bypass Fail Or successful

* Add the user with id 1001, access the file to read it,
* To read the ssh files keys copy it to ‘/tmp/’ directory and change the permission if needed.
{% endstep %}

{% step %}
### Find the password and convert the key

* Prompting for password means there is an encrypted used. So first the find the word which used in encrypting.
* The files is in ssh format convert it into crack able or brute forces format, Using ssh2john.
* After the conversion the brute forces methods can be applied.
* John the ripper
* Results is ‘sheep’ words.
{% endstep %}

{% step %}
### Access the shell

* After login , some commands are not working which results in limitation or restriction or prevention in shell which is ‘/bin/bash’.
* ‘ls -la /bin/bash’ results in custom ‘/bin/rbash/’ shells.
* Got the flags 1
{% endstep %}
{% endstepper %}

#### 3.5 Privileged Escalation - (cp is authorized to used root privileges.).

* Vulnerability Explanation: /bin/cp binary is authorized to used root privileges without root authentication.
* Vulnerability Fix:
* Severity: critical.

#### Steps to Reproduce

{% stepper %}
{% step %}
### the analysed issue

* Enumeration of Linux OS using LINPEAS.
* Finding the RED/YELLOW vector.
* Direct download in happycorp or host a server and download it,
{% endstep %}

{% step %}
### Identify the privilege escalation path

* Found the /bin/cp binary which uses the root privileges without authorization.
* View ‘ls -la /bin/cp ’ visible user and group the privileges of ‘bin/cp’.
{% endstep %}
{% endstepper %}

#### 3.6 Post Exploitation (Local or Proof Flags).

* System proof Screenshot.
* Final Proof Flags.
* Goodies.
  * SSH private key encrypted password is ‘sheep’

{% stepper %}
{% step %}
### Analysis the ‘/bin/cp’

* There are several ways to privileges escalations.
* Copy the attacker ssh authored\_key (id\_rsa.pub) and copy paste into the happycorp /root/directory. (using this method).
  * Copy the attacker id\_rsa.pub key
  * Copying it and making an authorized\_keys file using the karl user with privileges limited to read and write only for the karl user. This ensures that when it goes to the root user, it will have read and write access to the user group only
  * Creating a test directory, and within that, creating a .ssh directory. In that directory, echoing the authorized attacker key and setting permissions to allow only user read and write. After copying and pasting, the root now has authorized\_keys with user read and write permissions.

Now its copyied to /root.

Ssh to root using the attacker authorized\_keys.

* Got the flags 2
{% endstep %}

{% step %}
### The other ways are

* Copy the ‘/etc/shadow’ files and brute force.
  * NOTE: it is in the fail attempts.
* Add the attacker user credentials in sample ‘/etc/passwd’ files and copy to happycorp machine which results in rewrite in the origina; ‘/etc/passwd’
  * Cmd : hasanrehni:ghTC5HTjVd/7M:0:0:root:/root:/bin/bash
{% endstep %}
{% endstepper %}

#### 3.7 Failed Attempted

* Searchsploit
* Bruteforcing the ‘/etc/shadow’ files using John

### Acknowledgement
