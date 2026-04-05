# README

## Starting point

Start the machine by downloading the OpenVPN file provided by HTB.

```bash
sudo openvpn <file.ovpn>
```

{% stepper %}
{% step %}
### How many TCP ports are open?

**Answer:** 2
{% endstep %}

{% step %}
### What is the domain of the email address provided in the "Contact" section of the website?

**Answer:** thetoppers.htb
{% endstep %}

{% step %}
### In the absence of a DNS server, which Linux file can we use to resolve hostnames to IP addresses in order to be able to access the websites that point to those hostnames?

**Answer:** `/etc/hosts`

* In the absences of DNS server I manually added the Ip address into my machine so that won’t be problematic in future if any brut forcing happens.
* So that when the thetopper.htb name used in sub domain enumeration its converted into IP address and it works in IP address not in name.
{% endstep %}

{% step %}
### Which sub-domain is discovered during further enumeration?

**Answer:** s3.thetoppers.htb

* Used Gobuster to sub-domain enumeration.
{% endstep %}

{% step %}
### Which service is running on the discovered sub-domain?

**Answer:** Amazon S3
{% endstep %}

{% step %}
### Which command line utility can be used to interact with the service running on the discovered sub-domain?

**Answer:** awscli
{% endstep %}

{% step %}
### Which command is used to set up the AWS CLI installation?

**Answer:** `aws configure`

* Configure the access key if you want by creating an account in aws.
{% endstep %}

{% step %}
### What is the command used by the above utility to list all of the S3 buckets?

**Answer:** `aws s3 ls`
{% endstep %}

{% step %}
### This server is configured to run files written in what web scripting language?

**Answer:** PHP

* Identified by wappalyzer
{% endstep %}
{% endstepper %}

## Submit flag

**Answer:** `a980d99281a28d638ac68b9bf9453c2b`

* Some reverse PHP shell to get the initially access and upload the shell via `aws s3 cp`

Ifconfig and the attacker IP address in PHP code.
