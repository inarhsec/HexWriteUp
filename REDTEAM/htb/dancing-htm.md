# Dancing HTM

**STARTING POINT Category.**

* Start the machine by downloading the openvpn file that is provided by HTB.
* `#sudo openvpn <filen.ovpn>`

## TASK 1

<details>

<summary>What does the 3-letter acronym SMB stand for?</summary>

**Answer:** Server message block

</details>

## TASK 2

<details>

<summary>What port does SMB use to operate at?</summary>

**Answer:** 445

**Nmap –sV Scan**

</details>

## TASK 3

<details>

<summary>What is the service name for port 445 that came up in our Nmap scan?</summary>

**Answer:** microsoft-ds

</details>

## TASK 4

<details>

<summary>What is the 'flag' or 'switch' that we can use with the smbclient utility to 'list' the available shares on Dancing?</summary>

**Answer:** -l

_L for List and –N for Null_

</details>

## TASK 5

<details>

<summary>How many shares are there on Dancing?</summary>

**Answer:** 4

</details>

## TASK 6

<details>

<summary>What is the name of the share we are able to access in the end with a blank password?</summary>

**Answer:** workshares

</details>

## TASK 7

<details>

<summary>What is the command we can use within the SMB shell to download the files we find?</summary>

**Answer:** get

Initially access using smbmap,

The ‘LS’ output is too large using the ‘smbmap recurve’ command to ‘get’ the flag into the attacker current directory.

Kill the smbmap terminal to see the get output results

**SUBMIT FLAG**

**Answer:** `5f61c10dffbc77a704d76016a22f1664`

</details>
