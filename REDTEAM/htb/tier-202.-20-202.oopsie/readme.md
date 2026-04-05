# README

## Starting Point

* Start the machine by downloading the OpenVPN file provided by HTB.

```bash
sudo openvpn <filename.ovpn>
```

## Enumeration

* Nmap scan.

```bash
sudo nmap -sV -p -Pn --min-rate 1000 <target-ip>
```

* The TLL value refers to Linux.
* An Nmap scan reveals that there are two open ports: 22 and 80.
* Since port 80 is open, we can proceed to check the website hosted on that port.
* Nmap aggressive scan.

```bash
sudo –A –min-rate 1000 <target-ip>
```

* SearchSploit to see if there is any exploit.

```bash
sudo searchsploit OpenSSH 7.6
sudo searchsploit Apache httpd 2.4
```

## Tasks

{% stepper %}
{% step %}
#### With what kind of tool can intercept web traffic?

Answer: proxy

* Let's use BurpSuite. Open Burpsuite and click on the Proxy tab.
* Turn off intercept.
* Click on Open Browser.
* In the URL bar, type `<target-ip>`.
* Go back to Burp and click on the Target tab.
{% endstep %}

{% step %}
#### What is the path to the directory on the webserver that returns a login page?

Answer: `/cdn-cgi/login`

* Found something interesting, a directory called `/cdn-cgi/login`.
{% endstep %}

{% step %}
#### What can be modified in Firefox to get access to the upload page?

Answer: cookie
{% endstep %}

{% step %}
#### What is the access ID of the admin user?

Answer: `34322`

* Open our browser from our VM and, in the URL bar, go to:

```
http://<target-ip>/cdn-cgi/login
```

* I do not know any credentials, but there is a link **"Login as Guest"**.
* Click on **"Login as Guest"**.
* Logged in as user guest, access ID `2233`.
* The URL is like this:

```
http://<target-ip>/cdn-cgi/login/admin.php?content=accounts&id=2
```

**OR**

* Upon crawling the website, no other sensitive directories or information were found.
* A login page was present, but no credentials were available.
* Instead of attempting brute force with intruder, let's try using the credentials discovered on the previous box called Archetype.
* The password `"MEGACORP_4dm1n!!"` from the Archetype box history successfully granted access.
* After logging in, it was observed that there is an upload page.
* However, attempting to visit the upload page resulted in an error, stating the need for super admin privileges.
* Further exploration of the site unveiled interesting information on the Repair Management System page.
* What if we were to change `&id=2` into `&id=1`?
* Let's try changing the URL at the end and press Enter:

```
http://<target-ip>/cdn-cgi/login/admin.php?content=accounts&id=1
```

* There is a user named admin with the access ID `34322`.
* Which we were not supposed to see. This vulnerability indicates a weakness in the target machine's security called Broken Access Control, often referred to as IDOR.
* Additionally, the guest user has an access ID of `2233`.
* Got the superadmin id `34322`.
{% endstep %}

{% step %}
#### On uploading a file, what directory does that file appear in on the server?

Answer: `/uploads`

* Click on the Uploads tab on the website:
* The action requires super admin rights for file uploads to the target machine.
* This implies that with super admin rights, one would have the capability to upload files.
* To access the web page's developer tools, right-click on the page and select **Inspect** (shortcut: Q). Within the developer tools, navigate to the Storage tab, where we can locate a cookie.
* Currently, we are logged in as the user **guest** with an access ID of `2233`.
* The idea is to modify the cookie so that we appear as the user **admin** with an access ID of `34322`.
* Let's proceed by replacing `"guest"` with `"admin"` and `"2233"` with `"34322"` in the cookie.
* Now refresh the uploads page and we now get the following.
* We are now admin and we can now upload files!
* Uploading a reverse shell.
* Type `"webshell"`.
* After that type `"php"`.
* It gives output in the form of a php reverse shell.

To make the necessary changes, follow these steps:

1. Scroll down until you find the variables `$ip` and `$port`.
2. Update the IP by replacing `"127.0.0.1"` with the IP address of your virtual machine. If you're unsure of your VM's IP, open a new command prompt window and type `"ifconfig tun0"` to retrieve it.
3. Modify the port by replacing `"1234"` with `"4444"`. This change will correspond to the port we'll use when setting up Netcat later on.

* Trigger the shell.
* Got the shell.
{% endstep %}

{% step %}
#### What is the file that contains the password that is shared with the robert user?

Answer: `db.php`

```bash
cd /var/www/html/cdn-cgi/login
```

Gooodies

```php
<?php

$conn = mysqli_connect('localhost','robert','M3g4C0rpUs3r!','garage');

?>
```
{% endstep %}

{% step %}
#### What executible is run with the option "-group bugtracker" to identify all files owned by the bugtracker group?

Answer: `find`

* Initially access with SSH.
* Uploaded the LinPEAS for Linux Enumeration.
* Got no luck in LinPEAS.
{% endstep %}

{% step %}
#### Regardless of which user starts running the bugtracker executable, what user privileges will use to run?

Answer: `root`

* Used the ID to verify the user.

```bash
id
```

To identify any misconfigured SUID (SetUID) or binaries utilizing root privileges, the following steps can be taken:

1. Run the command:

```bash
find / -type f -perm /4000 2>/dev/null
```

to locate files with SUID permissions.

2. Execute the command:

```bash
find / -type f -perm /2000 2>/dev/null
```

to find files with SGID (SetGid) permissions.

These commands will help identify files with elevated permissions that may pose potential security risks.
{% endstep %}

{% step %}
#### What SUID stands for?

Answer: `set owner user id`
{% endstep %}

{% step %}
#### What is the name of the executable being called in an insecure manner?

Answer: `cat`

```bash
./bugtracker
```

Submit user flag

Answer: `f2c74ee8db7983851ab2a96a44eb7981`

```
f2c74ee8db7983851ab2a96a44eb7981
```

Submit root flag

Answer: `af13b0bee69f8a877c3faf667f7beacf`

* The bash bugtracker is utilizing the `cat` binary with root privileges.
* To exploit this, a path has been added, specifically `"/tmp/"`.
* A new `cat` binary has been created that provides a shell (`/bin/bash`).
* The new `cat` binary has been given execute permission.
* As a result, the bugtracker will now prioritize the attacker's path (`/tmp`) over the developer's path.
* Enter the `/usr/bin/bugtracker` to proceed with this exploit.
* Since `/bin/bash` is not available, an alternative path can be used, such as `/bin/sh`.
* However, using `/bin/sh` did not work as expected.
* Instead, a directory traversal technique is employed, leveraging the `cat` binary.
* The command used is `../root.txt` to traverse to the parent directory and access the file named `root.txt`.
{% endstep %}
{% endstepper %}
