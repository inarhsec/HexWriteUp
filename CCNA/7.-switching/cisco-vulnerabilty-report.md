# Cisco Vulnerabilty Report

Hi Team ,

Acknowledged .

Also to inform you for future reference ,you can check vulnerabilities hitting on any ios/ios-xe release by following 3 simple steps

Use the link Cisco ios checker below -

[https://tools.cisco.com/security/center/softwarechecker.x](https://tools.cisco.com/security/center/softwarechecker.x)

Step 1: On the Cisco ios checker, select your release / ios-xe version running on the device.

Step 2: Click on continue and select option 'All' under Security advisory impact rating.

Step 3: You will find all lists of vulnerabilities hitting the ios-xe and their fixed/not impacted release.

The customer, Hassan from GADCHIROLI DISTRICT CENTRAL CO OPERATIVE BANK LTD, is facing security vulnerabilities on their Catalyst C1300 switch series. These vulnerabilities require advice on mitigation, and some may necessitate a device restart. The customer has provided configuration details and a sheet outlining the vulnerabilities.\
The customer, GADCHIROLI DISTRICT CENTRAL COOPERATIVE BANK LTD, is experiencing vulnerabilities with their C1300 Switch Series. The specific vulnerabilities reported are: .bash\_history files being disclosed via the web server, the web server using basic authentication without HTTPS, and ICMP timestamp request remote date disclosure. These issues could potentially expose sensitive information and compromise network security. The software version in use is Active-image: flash://system/images/image\_4.1.3.36.bin

Technical Indicators:

* SSL Self-Signed Certificate
* SSL Certificate Cannot Be Trusted
* OpenSSH < 7.6 Vulnerability
* OpenSSH < 9.3p2 Vulnerability
* OpenSSH < 9.6 Multiple Vulnerabilities
* SSH Terrapin Prefix Truncation Weakness (CVE-2023-48795)
* Web Server Allows Password Auto-Completion
* .bash\_history Files Disclosed via Web Server
* Web Server Uses Basic Authentication Without HTTPS
* ICMP Timestamp Request Remote Date Disclosure

## VULNERABILITY CHECKER

Thank you for providing the required output.

From the provided output i can see you are running on 17.12.4 on both the switches.

Kindly find the below link of software checker page for 17.12.4 version:

[https://sec.cloudapps.cisco.com/security/center/softwarechecker.x?productSelected=ios\_xe\&selectedMethod=A\&captchaPage=true\&platformCode=NA\&versionNamesSelected=17.12.4\&allAdvisoriesSelectedByTree=N\&advisoryType=0\&iosBundleId=cisco-sa-20250326-bundle\&isFewCheckBoxChecked1=false\&isNoneCheckBoxsChecked1=true#\~onStep3](https://sec.cloudapps.cisco.com/security/center/softwarechecker.x?productSelected=ios_xe\&selectedMethod=A\&captchaPage=true\&platformCode=NA\&versionNamesSelected=17.12.4\&allAdvisoriesSelectedByTree=N\&advisoryType=0\&iosBundleId=cisco-sa-20250326-bundle\&isFewCheckBoxChecked1=false\&isNoneCheckBoxsChecked1=true#~onStep3)

Now i can see multiple vulnerabilities that you mentioned are present on this version.

![](https://mail.google.com/mail/u/0?ui=2\&ik=cc35147232\&attid=0.3\&permmsgid=msg-f:1832646139194382711\&th=196eddf42dac1977\&view=fimg\&fur=ip\&permmsgid=msg-f:1832646139194382711\&sz=s0-l75-ft\&attbid=ANGjdJ-70dCCZfx_qME_gY2_kelKll7TOxZm9YEenamdquMjDQ4GrC17BJuiRDhxlOQVVue5UDvaLazx3h4_yt62MKRKusHEeWip2BEuJ9iBvjGOSm9ozsJhTYy2W8Q\&disp=emb\&zw)

From the software checker we can only see the above mentioned vulnerabilities present on the version 17.12.4 , any other 3rd party vendor if reports a vulnerability on this version which is not present on the software checker page , we can discard that.

Kindly go to the software checker link and open the vulnerabilities one by one.

Go to the affected products heading and check if your devices are in the mentioned list of affected prodcuts or not.

For example CV-2025-20182 , refer the link below:

[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-multiprod-ikev2-dos-gPctUqv2](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-multiprod-ikev2-dos-gPctUqv2)

![](https://mail.google.com/mail/u/0?ui=2\&ik=cc35147232\&attid=0.4\&permmsgid=msg-f:1832646139194382711\&th=196eddf42dac1977\&view=fimg\&fur=ip\&permmsgid=msg-f:1832646139194382711\&sz=s0-l75-ft\&attbid=ANGjdJ9o9SbzvZ_kEOVvOF-zfGeMvCCsPqtbn07Q1Tfl_zVD1TqhgpbfURnum4ScukxkcS9LGbV7H-JLmbkwEda2SUxiU4EU3Dfkdd0vYndhnmm-M60wg9n50SwblbE\&disp=emb\&zw)

As you can see the products which have the above configuration are impacted by this vulnerability.

If your device does not have the above configuration , the switch is not impacted by the vulnerability.

Similalry you can check for the other vulnerabilities.

Kindly check the cisco software checker link below:

Please ask if you have any further queries.

[https://sec.cloudapps.cisco.com/security/center/softwarechecker.x?productSelected=ios\_xe\&selectedMethod=A\&captchaPage=true\&platformCode=NA\&versionNamesSelected=17.12.5\&allAdvisoriesSelectedByTree=N\&advisoryType=0\&iosBundleId=cisco-sa-20250326-bundle\&isFewCheckBoxChecked1=false\&isNoneCheckBoxsChecked1=true#\~onStep3](https://sec.cloudapps.cisco.com/security/center/softwarechecker.x?productSelected=ios_xe\&selectedMethod=A\&captchaPage=true\&platformCode=NA\&versionNamesSelected=17.12.5\&allAdvisoriesSelectedByTree=N\&advisoryType=0\&iosBundleId=cisco-sa-20250326-bundle\&isFewCheckBoxChecked1=false\&isNoneCheckBoxsChecked1=true#~onStep3)

[https://sec.cloudapps.cisco.com/security/center/publicationListing.x](https://sec.cloudapps.cisco.com/security/center/publicationListing.x)
