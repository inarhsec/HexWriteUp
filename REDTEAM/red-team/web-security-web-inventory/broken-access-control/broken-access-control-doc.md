# Broken Access Control Doc

## Authorization

* “What privilege the user have”
* “Who the user say user is”

## Session

* After the user is authenticated, user cant provide password at every page when the user visits that why the Server create a session ID.
* Manage authorization on every pages which the user don’t need to authorized everytime with password the server create Session ID which works like passworf in UserID Database.

## Access Control

* The User is authorized to perform certain task/action.

## Types of Access Control

### Vertical Access Control

* Used to restrict access to functions not available for other users in the organization.
* It's like a ladder getting the access of normal user to administrator user.

### Horizontal Access Control

* Enable different user to access similar resource types.
* Getting the access of (unauthorized) normal user 2 from normal user 1.

### Context Dependent Access Control

* Restrict access to functionality and resources based on the state of application or the user interaction with it.

All This leads to Broken Access Control.

## What is Broken Access Control

When users can act outside of their intended permissions.

### Vertical Privilege Escalation

* When an attacker gains access to privileges functionality that they are not permitted to access
* It's like a ladder getting the access of normal user to administrator user.

### Horizontal Privilege Escalation

* When an attacker gain access to resources belonging to another users of the same privilege level.

## Access Control Vulnerabilities

* When access control are implemted on some of the stages/steps but ignored on others because attackers are not going to follow the exacts sequence developer want to of steps they are going to see if it didn’t put certain access control rules on steps where its lowest.
* Others
* Bypassing access control by modification of URLs parameters
* Access the APIs with missing access control on the POST , PUT and DELETE methods
* Manipulating Meta Data, replaying or tampering with JSON web Token or Cookie.

## Impact of Access Control Vulnerabilities

* Confidentially:- Access to other user data
* Integrity:- Access to update other user data
* Availability: - Access to Delete user and user data.

## BlackBox Testing

* Map The Application.
* Understand the access control and the implemented for each privilege level.
* Manipulate parameter that are is used to make access control decisions in the backend.
* Automate testing using burpsuite extension like Authorize.

## Exploit

* Depends on the type of access control vulnerability
* Manipulated the vulnerable field and parameters.

## Automated Exploit Tool

* That curl the web application and looks for Vulnerabilities and likely missed the Vulnerabilites.
  * BurpSuite
  * Arachni
  * WAPZ
  * WAPITI
  * Acunetix
  * W3af

## Prevention

* Verifield access control
* Except for public resources, deny access by default.
* Apply the least privilege.
