# README

## Starting Point

* Start the machine by downloading the OpenVPN file provided by HTB.

```bash
#sudo openvpn <file.ovpn>
```

{% stepper %}
{% step %}
### What Nmap scanning switch employs the use of default scripts during a scan?

Answer: `-sC`
{% endstep %}

{% step %}
### What service version is found to be running on port 21?

Answer: `vsftpd 3.0.3`
{% endstep %}

{% step %}
### What FTP code is returned to us for the "Anonymous FTP login allowed" message?

Answer: `230`
{% endstep %}

{% step %}
### After connecting to the FTP server using the ftp client, what username do we provide when prompted to log in anonymously?

Answer: `anonymous`
{% endstep %}

{% step %}
### After connecting to the FTP server anonymously, what command can we use to download the files we find on the FTP server?

Answer: `get`
{% endstep %}

{% step %}
### What is one of the higher-privilege sounding usernames in `allowed.userlist` that we download from the FTP server?

Answer: `admin`
{% endstep %}

{% step %}
### What version of Apache HTTP Server is running on the target host?

Answer: `Apache httpd 2.4.41`
{% endstep %}

{% step %}
### What switch can we use with Gobuster to specify we are looking for specific filetypes?

Answer: `-x`
{% endstep %}

{% step %}
### Which PHP file can we identify with directory brute force that will provide the opportunity to authenticate to the web service?

Answer: `login.php`
{% endstep %}

{% step %}
### Submit Flag

Answer: `c7110277ac44d78b6a9fff2232434d16`
{% endstep %}
{% endstepper %}
