# Fawn HTB

STARTING POINT Category.

* Start the machine by downloading the openvpn file that is provided by HTB. `sudo openvpn <filen.ovpn>`

{% stepper %}
{% step %}
### TASK 1

What does the 3-letter acronym FTP stand for?

Answer: File Transfer Protocol.
{% endstep %}

{% step %}
### TASK 2

Which port does the FTP service listen on usually?

Answer: 21.
{% endstep %}

{% step %}
### TASK 3

What acronym is used for the secure version of FTP?

Answer: SFTP.
{% endstep %}

{% step %}
### TASK 4

What is the command we can use to send an ICMP echo request to test our connection to the target?

Answer: PING.

* TTL Identification of OS
* It's Linux.
{% endstep %}

{% step %}
### TASK 5

From your scans, what version is FTP running on the target?

Answer: vsftpd 3.0.3.
{% endstep %}

{% step %}
### TASK 6

From your scans, what OS type is running on the target?

Answer: UNIX.
{% endstep %}

{% step %}
### Nmap NSE
{% endstep %}

{% step %}
### TASK 7

What is the command we need to run in order to display the `ftp` client help menu?

Answer: ftp –h.
{% endstep %}

{% step %}
### TASK 8

What is username that is used over FTP when you want to log in without having an account?

Answer: anonymous.
{% endstep %}

{% step %}
### TASK 9

What is the response code we get for the FTP message `Login successful`?

Answer: 230.
{% endstep %}

{% step %}
### TASK 10

What is the command used to download the file we found on the FTP server?

Answer: Get.

Use the `get <filename>` to download the file in initiator current directory OR GUI below
{% endstep %}
{% endstepper %}
