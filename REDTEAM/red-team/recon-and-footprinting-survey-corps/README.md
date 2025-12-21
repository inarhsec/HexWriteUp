---
description: >-
  This guide contains all the required knowledge for performing a good
  enumeration and recon.
cover: ../../.gitbook/assets/RED-TEAM_RECON.jpeg
coverY: 18
---

# RECON AND FOOTPRINTING (SURVEY CORPS)

### <mark style="color:purple;">BugBounty VS Penetration Testing</mark> <a href="#bugbounty-vs-penetration-testing" id="bugbounty-vs-penetration-testing"></a>

> BugBounty&#x20;
>
> > Its Safe time for both Company and Hunter.
> >
> > Limited Scope like XSS, CSRF, RCE for Company.
> >
> > Saved Money
> >
> > No Time restriction for hunter.
> >
> > Case Levels
> >
> > > P4 has 100$
> > >
> > > P3 has 200$
> > >
> > > P2 has 500$
> > >
> > > P1 has 1000$
>
> Penetration Testing
>
> > Safe time.
> >
> > No Scope (Black & Grep HAT).
> >
> > Money Saveing.
> >
> > Time Sets.

### <mark style="color:purple;">Templates (Pending)</mark>

* The way report is write its  matters.
* write the report in helping format.
* write in a communication way in developer, because they are developers.
* No Warning and no threats.

> **Use GTP**
>
> > here dump the report remove confidential and vulnerability . thing and take what I want to break this down for a normal developer

{% hint style="info" %}
A Good Recon will get you where everyone is not looking.
{% endhint %}

## <mark style="color:purple;">RECONAISSANCE (Scout Regiment)</mark>

### What are we after ?

> APEX Domain -> www.<mark style="color:blue;">example.com</mark> -> rhanihasan.<mark style="color:blue;">gitbook.io</mark>
>
> > For every Domain the chance increased by 4X of hacking the target.
>
> SubDomain -> <mark style="color:blue;">www.</mark>example.com -> <mark style="color:blue;">rhanihasan.</mark>gitbook.io
>
> > For every subdomain the chance increased by 2X of hacking the target.
>
> Acquisition's & Shares
>
> IP Address
>
> Services
>
> Tech Intel

### <mark style="color:blue;">Domain</mark>[​](https://rhanihasan.github.io/cybersecurity/docs/CyberSecurity/CyberrSecurity360/Basic%20Enum,%20Info%20Gathering%20&%20Vulnerability%20Assessment#domain) <a href="#toc142346642" id="toc142346642"></a>

**A domain name is a unique address for a website that can be acquired. Usually, it consists of a website name and a domain name extension.**

### <mark style="color:blue;">FQND</mark>[​](https://rhanihasan.github.io/cybersecurity/docs/CyberSecurity/CyberrSecurity360/Basic%20Enum,%20Info%20Gathering%20&%20Vulnerability%20Assessment#fqnd) <a href="#toc142346649" id="toc142346649"></a>

* **A Fully Qualified Domain Name (FQDN) is the complete domain name for a specific computer, or host, on the internet.**
* **An FQDN looks like this: -**

> **myhost.example.com. ----> Fully Qualified Domain Name myhost ----> is the host located within the domain example.com (subdomain)**

#### <mark style="color:blue;">Types of Domain</mark>[​](https://rhanihasan.github.io/cybersecurity/docs/CyberSecurity/CyberrSecurity360/Basic%20Enum,%20Info%20Gathering%20&%20Vulnerability%20Assessment#types-of-domain) <a href="#toc142346643" id="toc142346643"></a>

* **Horizontal Domain**
* **Vertical Domain**

![Domain-vertical-horizontal](<../../.gitbook/assets/0 (2).png>)

#### <mark style="color:blue;">Horizontal Enumeration</mark>[​](https://rhanihasan.github.io/cybersecurity/docs/CyberSecurity/CyberrSecurity360/Basic%20Enum,%20Info%20Gathering%20&%20Vulnerability%20Assessment#horizontal-enumeration) <a href="#toc142346644" id="toc142346644"></a>

* **During a security assessment, our main aim is to find and list all the main websites owned by a single entity.**

#### <mark style="color:blue;">Vertical Enumeration</mark>[​](https://rhanihasan.github.io/cybersecurity/docs/CyberSecurity/CyberrSecurity360/Basic%20Enum,%20Info%20Gathering%20&%20Vulnerability%20Assessment#vertical-enumeration) <a href="#toc142346646" id="toc142346646"></a>

* **Vertical enumeration, or vertical domain correlation, is the process of discovering and connecting related websites that belong to the same organization or entity.**
* **Vertical Enumeration can be performed with the help of below methods. Which is**

### <mark style="color:blue;">Passive Information gathering</mark>.[​](https://rhanihasan.github.io/cybersecurity/docs/CyberSecurity/CyberrSecurity360/Basic%20Enum,%20Info%20Gathering%20&%20Vulnerability%20Assessment#passive-information-gathering) <a href="#toc142346647" id="toc142346647"></a>

* **Passive information gathering is based on other with whatever is asked**

{% hint style="info" %}
**Don’t trust the passive information because it is available to others for some logical reasons.**
{% endhint %}

#### <mark style="color:blue;">Subdomain enumeration</mark> <a href="#toc142346648" id="toc142346648"></a>

* **Subdomain enumeration is a crucial step in understanding the structure of a website. It involves finding and identifying smaller sections within a larger website. To put it simply, it's like exploring different sections or pages that are part of a main website. Subdomain Enumeration is a process of finding sub-domains associated to the root domain.**

**According to** [RFC 1034](https://tools.ietf.org/html/rfc1034),

> **"a domain is a subdomain of another domain if it is contained within that domain".**

![understanding-level-of-domain](<../../.gitbook/assets/2 (2).png>)

> **the More the subdomains = the More assets to look for vulnerabilities**



### <mark style="color:purple;">A Mis concept for me in Subdomain</mark>

* **"Subdomain"** is a term often misunderstood.
* It refers to a specific computer or host within a larger domain.&#x20;
* For example, **rhanihasan.gitbook.io** is a subdomain of **gitbook.io** Some people mistakenly think that any link to a web application hosted on a specific host is a subdomain, but this is not the case.
* For instance, if **rhanihasan.gitbook.io** \` does not have a web service hosted on it, sending web probes to it will not return any output.&#x20;
* However, **rhanihasan.gitbook.io** is still a valid subdomain of **gitbook.io**, and it may have other non-web services hosted on it, such as SSH or SMTP, which could be vulnerable to exploits.
* When collecting subdomains, it's important to first DNS resolve them using tools like amass or subfinder, [shuffledns](https://github.com/projectdiscovery/shuffledns) , [puredns](https://github.com/d3mondev/puredns)  rather than directly sending them to web probing tools like **httpx & httprobe**. This ensures that you are only focusing on valid and active subdomains.

