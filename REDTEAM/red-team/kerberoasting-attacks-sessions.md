# Kerberoasting Attacks SESSIONS

## Kerberos

* Kerberos is a network authentication protocol used to verify the user or machine and protect the access of the application.
* It is mostly used in Active Directory.
* It uses UDP port 88.
* It is installed by default within the domain or forest, which requires Active Directory Domain Service.
* Kerberos is a mutual authentication protocol which verifies user and server before session using a ticket system.

## Terminologies

* **Client:** A normal user who wants to access the service.
* **KDC (Key Distribution Centre):** The authenticator and heart of Kerberos. It supplies tickets and generates session keys that allow users to authenticate to the servers.
  * There are two servers stored in KDC:
    * **Authentication Server:** Confirms the known user is making a request and gives TGT.
    * **Ticket Granting Server:** Confirms that user is making a request to a known service and gives tickets.
  * The KDC uses the Active Directory Domain Service database as its security account database.
* **Application Server:** Any application server such as SQL.
* There are lots of messages passed back and forth between the user, authentication server, ticket granting server, and the services where some messages are plaintext and some are encrypted.
* **Types of message**
  * **Authentication:** Contains the session key of the client and server.
  * **Tickets:** Contain information like client ID, service ID, timestamp, TTL, etc., all encrypted using server key.
* **TGT (Ticket Granting Ticket):** Ticket needed for requesting TGS from KDC.
* **TGS (Ticket Granting Service):** Ticket need for authentication against a service.
* **SPN (Service Principal Name):** A finder for service.

## Kerberos authentication flow

{% stepper %}
{% step %}
### Client requests access

Start with the user sending message to authentication server: "Hey I like to access the server."

Message:
{% endstep %}

{% step %}
### Authentication server returns a TGT

The Authentication server verifies the request is coming from a known/authorized user and generates a TGT encrypted with the user's secret key.

The tgs session key is decrypted by using the user correct password.

> Note: the user cannot decrypt the TGS secret key.
{% endstep %}

{% step %}
### User sends the TGT to TGS

The user decrypted the message and create new message with TGT to TGS.
{% endstep %}

{% step %}
### TGS validates the request and creates a service ticket

It start with the unencrypted service id and validate in the database with the authenticator if its in the list.

Use the TGT to decrypt the TGS secret key.

Now use the TGS session key to decrypt the user authenticator message.

Its add in the TGS cache if its not there.

The TGS decrypted the packet perform validation and generate a service ticket with another message send to user.

A random symmetric service session key.

Note the user cannot decrypt the service secret key.
{% endstep %}

{% step %}
### User sends the authenticator and service ticket to the service

The user decrypted the message and create the authenticator message and send the user authenticator and the service ticket to the service.

The user decrypted the message, create the authenticator message where the user authenticatation ticket.
{% endstep %}

{% step %}
### Service validates and returns the final authenticator

The service does its own decryption and validation.

Check the service cache if not then added.

The service session key is already send by TGS now the user decrypted it.

The final authenticator message is send back to the user this allow the user and server to authenticate each other.
{% endstep %}
{% endstepper %}

## Workflow

## TGT

## Wireshark packet flow

Edit>> preference>> protocol >> KRB5 >> check KRB5

{% stepper %}
{% step %}
### Packet number 1

The client sends an AS-REQ to the AS. The packet includes the headers below.

* pdata: It is called Pre-Authentication data. The client inserts a time stamp here and encrypt it with the client password. The goal is to avoid replay attacks. From screenshot below, it can be seen this value is empty in the packet number 1.
* cname: It contains the user(client) name to be authenticated.
* realm: It is the domain name.
* sname: This field contains the service name being requested.
* till: It includes the requested expiration time of the ticket being requested.
* etype: The encryption types that client supports.
{% endstep %}

{% step %}
### Packet number 2

Since the client did not include the Pre-Authentication data, AS replies with an error code, asking for Pre-Authentication data.
{% endstep %}

{% step %}
### Packet number 3

The client reconstructs an AS-REQ with Pre-Authentication data this time and sends it to the AS. The following output marked with blue color shows decrypted Pre-Authenticated data which contains a timestamp.
{% endstep %}

{% step %}
### Packet number 4

The AS replies with an AS-REP packet. The packet contains an encrypted TGT and a session key. As it is seen below, since the TGT is encrypted with AS master key, the client is not able to decrypt it. Wireshark marks unencrypted packet with yellow color while showing the decrypted parts with blue color. The client decrypts the session key with its password.
{% endstep %}

{% step %}
### Packet number 5

After receiving the TGT, the client makes a request (TGS-REQ) to TGS. The request contains TGT and an authenticator which is encrypted with the client’s session key. With this request, the client asks the server for a service ticket. When the TGS receives the request, it decrypts the TGT with master key shared with AS.
{% endstep %}

{% step %}
### Packet number 6

The TGS constructs a service ticket and encrypts it with another secret key which is shared between TGS and the File Server. The service ticket includes information such as service name, client id, expiry date, a new session key, the client’s address etc. One copy of the new session key is encrypted with client’s session key and inserted into the reply.
{% endstep %}
{% endstepper %}
