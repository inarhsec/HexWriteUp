---
description: >-
  Cisco Introduces the First Firewall in the market the Adaptive security
  Appliances.
icon: block-brick-fire
---

# Cisco ASA

### Initial Configuration

```
show interface ip brief
show route ip
show running-config
```



Interface Configuration

```
interface gig 0/0
no shutdown
ip address <address>
nameif <interface_name> (e.g., inside, outside, or DMZ)
security-level <level>
```

*

    **Security Levels**:

    * "inside" default level: 100 (most trusted)
    * "outside" default level: 0 (least trusted)
    * DMZ can be assigned a custom security level.
* &#x20;"security levels" on ASA range from 0 (least trusted) to 100 (most trusted).

Static Routing

{% code overflow="wrap" %}
```
route <nameif> <destination_ip> <subnet_mask> <next_hop_ip>
route inside 192.168.1.0 255.255.255.0 192.168.100.1
route dmz 172.16.1.1 255.255.255.0 192.168.100.
```
{% endcode %}

Clear Config

```
clear configuration all
clear configuration access-list
```

Static Route

```
route inside  192.168.1.0 (IP) 255.255.255.0 (subnet) 192.168.100.1 (next-hop)
```



Default Route

* Syntax: `route <interface> 0.0.0.0 0.0.0.0 <next_hop_ip>`
* Example: `route outside 0.0.0.0 0.0.0.0 200.1.10.1`
* **Note**: Only one default route can be applied per route table.

View Full configuration

```
more system : running-configuration
```

### Dynamic Routing Authentication

> Routing authentication because of DOS or DDOS of custom routing packet generate.

RIP on Router

Key Chain Configuration

```
key chain (name) KEY
key 1
key-string (password)
```

RIP Configuration

```
routing rip
network (192.168.1.0)
version 2
```

RIP on Firewall

```
interface ethernet 0/0
ip rip authentication mode md5
ip rip authentication key-chain KEY

interface gig 0/0
rip authentication key (password) keyid 1
rip authentication mode md5

```

Routing RIP

```
router rip
network 192.168.1.0
version 2
```

EIGRP Authentication

* Firewall doesn't support wildcard.

```
interface gig 0/2
authentication key eigrp 100 password (password) key-id 1
authentication mode eigrp 100 md5
```

EIGRP ROUTING on Router

```
router eigrp 100
network (192.168.1.0)
```

KEY Chain

```
key chain KEY
key 1
key-string (password)
```

KEY on interface

```
interface ethernet 0/0
ip authentication mode eigrp 100 md5
ip authentication key-chain eigrp 100 KEY
```

Apply eigrp on Router&#x20;

```
router eigrp 100
network 192.168.1.0 0.0.0.255
```



OSFP Authentication

Firewall OSFP

```
router ospf 100
network 192.168.1.0 255.255.255.0
area 0
```

OSFP on Interface

```
interface eth 0/0
ospf message-digest key 1 md5 (password)
ospf authentication message-digest
```



ROUTER OSPF

KEY

```
key chain KEY
key 1
key-string (password)
```

Router OSFP

```
router ospf 100
network 200.1.1.1 0.0.0.255 area 0
```



### Redistribution

RIP

```
router rip
redistribution eigrp 100 metric 1
redistribution ospf 100 metric 1
redistribution static
```

EIGPR&#x20;

{% code overflow="wrap" %}
```
router eigrp 100
redistribution rip metric (1 lakh) 1,00,000 (fastethernet) 10 255 (load balance) 255 (relibitly) 1500 (MTU)
same for OSPF
same for static
```
{% endcode %}

OSPF

```
router ospf 100
redistribute rip subnet
redistribute eigrp 100 subnet
resdistribution static subnet
```



### &#x20;Packet Flow in Cisco ASA

1. **Basic Rules for Packet Flow**:
   * **High Security to Low Security**: Traffic is allowed by default. For TCP/UDP, the ASA creates a stateful entry to track the session.
   * **Low Security to High Security**: Denied by default unless permitted by an Access Control List (ACL).
   * **Same Security Level**: Denied by default unless `same-security-traffic permit inter-interface` is enabled.
2. **How the Firewall Processes Incoming Packets**:
   * The firewall evaluates packets through the following stages:
     1. **Routing Table**: Determines the path based on destination IP.
     2. **Stateful Table**: Checks if there’s an existing entry for the session, allowing established sessions without further ACL checks.
     3. **ACL**: Applies the configured ACL rules if there’s no entry in the stateful table.
     4. **NAT**: Translates private IPs to public IPs if needed.
3.  **TCP/UDP Packet Processing** :

    **Initial SYN Packet (From Sender)**

    * **Routing Table**: The firewall consults its routing table to determine the next hop for the destination IP.

    ```
    source address: 10.1.1.4
    source port: RANDOM
    source MAC address: LAN MAC
    Destination address: 172.16.1.1
    destination port: 443
    destincation mac address: WAN MAC
    TCP : ACK
    ```

    * **ACL**: Evaluates packet against the configured ACLs on the interface.
    * **NAT**: Checks if the packet requires IP translation.
    * **Stateful Table**: If permitted, the firewall creates an entry in the stateful table to track the session. This entry allows the return SYN-ACK packet without re-evaluating ACLs.

    **SYN-ACK Packet (Returning to Sender)**

    * **Routing Table**: Determines the path based on the destination IP.

    ```
    source address: 10.1.1.4
    source port: RANDOM
    source MAC address: LAN MAC
    Destination address: 172.16.1.1
    destination port: 443
    destincation mac address: WAN MAC
    TCP : SYN-ACK
    ```

    * **Stateful Table**: Finds the session entry created by the initial SYN packet, allowing the return packet.
    * **ACL**: Bypassed since the session is tracked.
    * **NAT**: Translates back if required.

    **ACK Packet (Completing the Three-Way Handshake)**

    *   **Routing Table**: Determines the route for the packet.source address: 10.1.1.4

        ```
        source port: RANDOM
        source MAC address: LAN MAC
        Destination address: 172.16.1.1
        destination port: 443
        destincation mac address: WAN MAC
        TCP : ACK
        ```



    * **Stateful Table**: The session entry is used to confirm it as part of an established connection.
    * **ACL**: Not checked due to stateful table entry.
    * **NAT**: Applies if configured.

    **Packet Details (Example)**:



    ```
    Source Address: 10.1.1.4
    Source Port: Random
    Source MAC Address: LAN MAC
    Destination Address: 172.16.1.1
    Destination Port: 443
    Destination MAC Address: WAN MAC
    Protocol: TCP (ACK)
    ```



    **Stateful Table**: The firewall sees the table entry and permits the packet without checking ACL or NAT settings again.
4.  **ICMP Packet Processing**:

    **High Security to Low Security Level**

    * **ECHO Packet**:
      * **Routing Table**: Determines the path.
      * **Stateful Table**: No entry created for ICMP by default.
      * **ACL**: Permitted by default for high-to-low traffic.
      * **NAT**: Applies if configured.
    * **ECHO-REPLY Packet (Return)**:
      * **Routing Table**: Determines the path.
      * **Stateful Table**: No entry in table since ICMP is stateless by default.
      * **ACL**: Denied by default for low-to-high traffic unless explicitly permitted.

    **Low Security to High Security Level**

    * **Initial Packet**:
      * **Routing Table**: Determines the path.
      * **ACL**: Denied by default (low-to-high traffic) unless explicitly permitted by a custom ACL.
      * **NAT**: Applies if the ACL allows the packet.
5. **Three-Way Handshake for Same Security Level Traffic**:
   * **Routing Table**: Determines the packet’s path.
   * **Stateful Table**: No session entry initially, as the firewall doesn’t create a table entry until the first packet is permitted.
   * **ACL**: Denied by default for same security level, unless `same-security-traffic permit inter-interface` is enabled.
   * Once allowed, the firewall will permit TCP/UDP packets based on the stateful table entry.
6. **Custom Policy for ICMP Stateful Inspection**:
   * By default, ICMP traffic does not create a stateful entry. To enable stateful ICMP tracking, configure a custom policy.
   *   **Configuration**:

       ```shell
       policy-map global-policy
         class inspection default
           inspect icmp
       ```
   * **Effect**: This configuration enables ICMP stateful inspection. If the initial ICMP packet is permitted by ACL, the firewall creates a stateful table entry for the session.
7. **Example: Processing a Low Security to High Security Packet (TCP/UDP)**
   * **Routing Table**: Directs the packet to the intended destination.
   * **Stateful Table**: Checks for an existing session entry; if none, it moves to ACL.
   * **ACL**: Denied by default for low-to-high traffic unless overridden by a custom rule.
   * **NAT**: Applies translation only if the ACL permits the packet.
   * **If ACL Allows**: The firewall creates an entry in the stateful table after the initial SYN packet. Future SYN-ACK packets from the destination will be permitted based on this entry without re-checking the ACL.
8. **Example: Detailed ICMP Flow with Custom Policy**
   * **Initial ECHO Packet**:
     * **Routing Table**: Finds the next hop.
     * **ACL**: Permitted if custom rule exists for low-to-high ICMP traffic.
     * **Stateful Table**: An entry is created if `inspect icmp` is enabled, allowing the response.
   * **ECHO-REPLY Packet**:
     * **Stateful Table**: Finds the entry and allows the packet back without additional ACL checks.



### ACCESS LIST

```
access-list OUT-IN extended permit tcp any host 172.16.1.1 eq https
access-group OUT-IN interface outside
```

### CUSTOM CRAFTED PACKET

```
packet-tracer input outside tcp 200.1.1.1 3 34532 (random port) 172.16.1.1 443
```

### Protocl TIMEOUT

* TCP has timeout  1 hours
* UDP has 2 mintues&#x20;
* ICMP has 2 second (that why in ICMP, Firewall don't make statefull table.)

FLAGS

> Its menas its show what is going on, Connection state

* UI0B&#x20;
  * U = Up
  * I = inbound
  * O = data
  * B = Packet comes form outside SYN.
* Idle Time = Nothing Happend.
* Uptime = These much time happend.
* Timeout = These limit after.

ACCESS-LIST EXAMPLE.

{% code overflow="wrap" %}
```
# Creating Access-List
access-list IN-OUT extended permit tcp 192.168.121.1 host 200.1.1.1 eq ssh
access-list IN-OUT extended permit icmp host 192.168.121.1 host 200.1.1.1 echo
access-list IN-OUT extended deny ip any any

#Applying on interface
access-group IN-OUT in interface inside
```
{% endcode %}



TIME ACL

> Its timeACL its hints access list with time.

{% code overflow="wrap" %}
```
show clock
time-range BLOCK-TIME
    periodic daily 00:00 to 08:59
    periodic daily 17:00 to 23:59

access-list IN-OUT extended deny tcp 192.168.10.0 255.255.255.0 any eq http time-range BLOCK-TIME
access-list IN-OUT extended permit ip any any
access-group IN-OUT in interface inside

clock set 00:00:00 1 Jan 2024
```
{% endcode %}





OBJECT / OBJECT GROUP

> object is an single entry.
>
> its has two type Network and Service.

Network Object

```
object network MSIPC
    host 200.1.1.1
objet network LAN
    subnet 192.168.1.0

Access-List
access-list IN-OUT extended permit tcp object LAN object MSIPC eq 443
access-group IN-OUT in interface inside
```

* If any changes in network need to be done its can be change in object its auto pull in the access-list.
* Name can't be changed because its already applied that name in ACL so be carrefull to write name

Object Service

```
object service TCP-SSH
    service tcp destination eq ssh
object network Server
    host 200.1.1.3

Access List
access-list IN-OUT extended permit object TCH-SSH object MSIPC object Server
```



OBJECT GROUP

> Its an combine entry
>
> Its the combination of multiply object.

```
object-group TCP-SERVER
    object-server object TCP-SSH
    object tcp destination eq http 
```

*   ACL can be IP BASE, USER BASE, MACHINE BASE.

    * ICMP TYPE  provide all icmp service like echo, echo-reply host undertination etc. it help to search ICMP code (code based)  protocol is use to combine multiply protocol like TCP, UDP OSPF etc.
    * User its verify and permit or deny based on username its not IP adddress based ACL to work this need NAC (ISE) or AD to verify username and permit or deny based on username.

    &#x20;

```
http server enable
http server enable 443
http 192.168.1.1 255.255.255.0 INSIDE
username admin passwrod admin privilege 15
aaa authentication http console LOCAL
aaa authentication telnet
```



### UPLOADING ASDM&#x20;

```
show disk0:
show flash:
show asdm image

copy http:disk0
192.168.1.1
asdm 7.9.bin
asdm image disk0:/asdm7.9.bin
```



## DHCP IN FIREWALL

* d mean dynamic.

```
dhcpd address 192.168.1.1-192.168.1.253 inside
dhcpd dns 8.8.8.8
dhcpd domain google.com
dhcpd enable inside

show running-config dhcpd
show dhcpd binding
```

FIREWALL ON STICK

```
interface gig 0/0.1
no shutdown

interface gig 0/0.1
vlan 10
no shutdown
nameif inside
ip address 192.168.1.1 255.255.255.0 


Apply ACL
```

## NAT FIREWALL

> ASA Firewall NAT table also known as KTABLE

* to view statfull table.

```
show connection long
```



### STATIC NAT

* its one to one maping
* its has a feature of by directional
* no timeout.

NAT Means REALIP (PRIVATE IP ) to MAP IP

* POLICY NAT
* DESTINATION NAT
* PORT
* AUTO NAT
* MANUL NAT
* OBJECT NAT
* TWICE NAT
* PAT STATIC
* PAT DYNAMIC (timeout 30 second)



### ONE TO ONE MAPPING

```
object network internetpc
    host
object network dellserver1
    host
object network dellservermap
    host
nat (dmz,outside) source static dellserver1 dellservermap
```



### PAT (Many To One)

```
object network LAN
    subnet 192.168.1.0 255.255.255.0
nat (inside,outside) source dynamic  LAN interface
```



### DYNAMIC NAT

```
object-group network ITPC
    network host 192.168.1.1
    netowrk host 192.168.1.2

object network ITPCPUBLIC
    range 200.1.1.1-200.1.1.5

net (inside,outside) source dynamic ITPCPUBLIC

show nat details
timeout connec  00:50:00 TCP
timeout xlate   00:40:00
timeout part xlate  00:40:00
```

* When the connection is close then the nat time out will start for dynamic NAT.

### STATIC NAT

* Upto 65535 into One IP ADDRESS.
* It by directional
* it has only one public IP.

```
object network saleserver
object network markerserver
```



### DYNAMIC PAT

* PAT pool with custom IP Address



```
object network LAN
    subnet 192.168.1.0 255.255.255.0
object network LANPUBLIC
    host 200.1.1.1

nat (inside,outside) source LAN LANPUBLIC
```



### PAT POOL

```
object-group network LANPATPOOL
    network-object host 200.1.1.3
    network-object host 200.1.1.4

nat (inside,outside) source LANPATPOOL LANPATPOOL

```



### POLICY NAT

* Static Policy NAT (MAP Service and HINT destination).

```
object network PC
    host 192.168.1.1

object network PCPUBLIC
    host 200.1.1.5
    
object service TCPSSH
    service tcp destination eq ssh
    
nat (inside,outside) source static PC PCPUBLIC
```



### DESTINATION NAT

* Convert private to Public , But blind the destination if destination is correct (mathc then get the public IP)
* Not check service destination.

{% code overflow="wrap" %}
```
object network PCPUBIP
    network host 200.1.1.1

object network server
    network host 200.1.1.2

nat (inside,outside) source state PCPUBIP destination static server(publicIP) server(mapping means server private )
```
{% endcode %}



### STATIC PAT

* Port forwarding, port redirection many to one its by directional is to hide ports.

```
object network WEBSERVER
    network 172.16.50.80
    
object network DCMAP
    network 200.1.1.1

object service TCPTELNET
    service object tcp source eq telnet

object service webservermapservice
    service tcp source eq 2001

object service emailservermap
    service tcp source eq 2003
    
object network emailserver
    network 172.16.50.25
    
nat (dmz,outside) source static WEBSERVER DCMP service TCPTELNET WEBSERVER service
nat (dmz,outside) source static emailserver DCMAP service tcp
```



* Source Service means traffic comes form outside firewall under that is form outisde so its convert into source port.
* NAT has 3 section.

Section 1 known as Manual NAT / Twice NAT.

* its done in config mode
* &#x20;config#nat

Section 2

* known as auto or object

```
object network emailreal
    host 172.16.50.1 

nat (dmz,outside) static dynamic email/servermapip
```

* Only static nat dynamic PAT (ALL PAT TYPE).
* Not destination NAT.

Section 3

* Known as after auto
* its a part of manul NAT

```
nat (dmzoutside) after-auto source static dellserver1 dellservermap
```



## URPF (Unicast Reverse Path Forwarding)

* its provide security form IP spoofing its check the source IP is there in his network route and if not its denied the packet.

```
ip verify reverse-path interface inside

interface ethernet 0
no shutdown
channel-group 1 mode active

interface ethernet 3
no shutdown
channel-group 1 mode active

interface port-channel 1
no shutdown
ip address
nameif

show interface port-channel 1 details
```



## REDUNDANT

> Redundnat has two mode active and passive created upto 8 redudant group.

```
interface ethernet 0
    no shutdown

interface redundant 1
    member-int interface gig 0
    member-interfac gig 1
    nameif outside
    ip address 200.1.1.1 255.255.255.0
```



* So if anything happend to active member standby will take his place, but when active is back its have to focus full entry cmd.

```
redundant-interface redundant 1 active-member gig 0/3
```



LOGGING IN FIREWALL

* Install KIWI SYSLOG SERVER VERSION

```
show logging
logging enable
logging buffered information (means its save in memory)
logging trap information (means syslock server)
logging host inside 192.168.1.1 (its has some 7 layer)
logging console information
```

* Buffered size are in bytes 4096 and customize it.

```
logging buffered-size 6000
```

* Console

```
logging enable
logging console information
```

* This message willl show in console and its hand to write and when message is coming).



### BUFFERED

```
logging enable
logging buffered information
```

* Means its save in memory an attack can happen and the firewall might get legged)

```
logging enable
logging map information
logging host inside 192.168.1.1
```

* Class means advance message it provide single feature message.

```
logging class vpn tran error
logging class ospf console information
```



### LIST

* multiplt message make list on the requirement.

```
logging list monitor level error class session
logging list monitor level error class vpn
logging list monitor level error class ospf
```

* Firewall will send email to receiver enable (email logging)&#x20;

Receiver email

```
logging recipient-address hasah@ccn.in
```

* Now forms address means sender

```
logging from-address syslog @hexmail.in
```



* smpt-server will (DNS) check and forward the message

```
snmp-server 172.15.50.25
logging mail monitor
```



## SLA (Service Level Agreement)

* Its two or more connection
* Track: feature / service which send packet to check the connection is up or NAT if connection is down it will change the connection with given timeout.
* Track work under RSR protocol.

```
sla monitor 1
    sla monitor 1 type echo protocol ip icmp echo 200.1.20.1 interface outside
    timeout 5000 (write in millisecond)
    frequency

sla monitor schedule 1 life forever start-time now
    track 100 rtr 1 reachablility

route outside 0.0.0.0 0.0.0.0 200.1.20.1 1 track 100
route outside 0.0.0.0 0.0.0.0 20..1.30.1 10
```



### ICMP Attack Security

* ICMP permission PC will not ping the firewall but firewall can ping the PC.

```
icmp permit any echo-reply inside
icmp permit any echo-reply dmz
icmp permit any echo-reply outside
```



## PASSWORD RECOVERY

### ROUTER PASSWORD RECOVERY

> In the BOOT PROCESS ( Breack IT)
>
> CTRL + PAUSE BREACK

* When the image is decompressing then press CTRL + PAUSE BREAK

In Show version

> Configuration number
>
> 0x2102 MAIN
>
> By pass help is the seconding
>
> 0x2142

* How ill be in Rommon Mode ( read only memory monitor)

```
rommon:confreg 0x2142
rommon:reset
```

* Now the router will bypass but the preview data will be stored in router memory.

```
start-config
```

* And copy perviews config by.

```
copy startup-config running-config
```

* Now its be perviews config.

```
enable secret admin@123
username admin privilge 15 secret admin@!23

config-register 0x2102
write memory
```

### SWITCH PASSWORD RECOVERY

* Press mode 3 times in switch.

```
flash_init
dir flash
```

* Now have to cahnge config text because all perviews is saved in config text

```
rename flash: config.text flash:config.text.old
boot
```

Switch will rebload.

```
rename flash: config.text.old  flash:config.text
copy flash:config.text running-config
username cisco privilige 15 password cisco
write memeory
```



### FAILOVER

> When a Device fail the backup device will start.
>
> Why device down: hardware fail, heated RAM, CPU, DOS/DDOS, sometime electrical issue.

Types

* Interface failover.
* Hardware failover.
  * Active/Standby
  * Active/Active (mostly this is used).

Failover Condition.

* Minimum two firewall.
* Same Model Number, RAM, CPU, Hardware, Interfaces.

Cluster Firewall all hardware and created logical.

<img src=".gitbook/assets/file.excalidraw (9).svg" alt="" class="gitbook-drawing">

LAN: Download all active conf and ping and monirtoring the active one.

LINK: Says connection will statefull Table.

if link cable is not there is called stateless failover.

```
ASAV1
interface gig 0/1
ip address 192.168.10.254 255.255.255.0 standby 192.168.10.253

interface gig 0/0
ip address 200.1.10.254 255.255.255.0 standby 200.1.10.253

int gig 0/3
no shutdown

failover Lan unit primary
failover lan interface ASAV1-ASAV2 gig 0/3
failover link ASAV1-ASAV2 gig 0/3
failover interface ip ASAV1-ASAV2 10.10.10.1 255.255.255.0 standby 10.10.10.2


failover

showfailover


ASAV2

int gig 0/3
no shutdown

failover Lan unit primary
failover lan interface ASAV1-ASAV2 gig 0/3
failover link ASAV1-ASAV2 gig 0/3
failover interface ip ASAV1-ASAV2 10.10.10.1 255.255.255.0 standby 10.10.10.2


failover

showfailover

```

Forcefully Active

```
failover active
no ip domain lookup
```

### Security Context/ Virtualization

> Like VMWARE divide into real hardware two company required firewall so one real firewall can divide upto 20 images.

```
show mode
```

> See Security contexnt do now multiply because its workon multi mode.

```
mode multiple
```

> Now admin Context will created first all do all interface "No Shutdown"

```
context C1
allocate-interface eth1
allocate-interface eth2
config-url disk:0/c1.cfg

context C2
allocate-interface eth1
allocate-interface eth2
config-url disk:0/c2.cfg

write memeory all
```

Now Changing

```
change to context c1
```

If you want to go to admin

Sometime admin interface can be deleted&#x20;

```
admin-context admin
context admin
config-url disk:0/admin.cfg
```

> Unique Interface means inside and outside get a interface but multiple means one interface and have subinterface. to remove

```
no context c1
no context c2

show disk0:
delete disk0:/c1.cfg
delete disk0:/c2.cfg
```

Unique Interface&#x20;

Same interface

C1 has eth1 eth0

C2 has eth1 eth0

* There is an error that comes is the IP address is different but the bith has same interface so the MAC address so the ARP has two interface but same MAC address so the system will not forward the packet.
* Multiple MAC address generate its generate unique MAC address.

```
Mac-address auto
    c1 interface eth2
    mac-address 0000:111:::
```

* Subinterface

```
Interface eth0
no shutdown

interface eth1.11
vlan 11

interface eth1.12
vlan 12

C1 
allocate-interface eth1.11
allocate-interface eth0

C2
allocate-interface eth1.12
allocate-interface eth0

ChangetoC1
interface eth1.11
ip address
nameif
security level
```

Active/Active

* Need multi context.
* ASA

eth1 >> C1 >> Interface Eth1 >> Outside Eth0&#x20;

eth2 >> C1 >> Interface Eth1 >> Outside Eth0

* First to failover to standby to get ASA2 the active config then ASA2

```
faukover group1
primary
preempt
```

`preempt` when a device is down this command hekp to if your problem is sovle the taks you job back.

```
exit
failover group2
secondary
prempy

context c1
join-failover group1

context c2
join-failover group2

NOW IP ADDRESS
```



### Modular Policy Framework

> 2 action 1 permit 2 deny traffic but have permit traffic with limits then you can do it on MPF like a fillering
>
> MPF is a security feature with controls and folloing packets with conditional work on L3 layer to L7 layer.

1. Classmao it identify the traffic tell to polciy map (L3-L7) monitor.
2. Policy-Map it will  take action on that.
3. Service-Policy active in interface.

ClassMap (name) LAN-to-dmzdell



To add Traffic

```
match port tcp eq 3 (basic command no source ip and destination IP)
```

Advance

* first make ACL

```
access-list lan-to-dell permit tcp 192.168.121.0 255.255.255.0 host 172.16.50.22 eq telnet
class-map lan-to-dmzdell1
match access-list lan-to-dell1
```

Now to control

```
pmap# policy-map in-pmz-out
pmap# class lam-to-dell1
pmap-c# set connection per-client-max 1
```

now to active (like we active access-group)

```
config#service-policy in-dmz-out interface inside
```



Framework

* All these on connected

```
per-client-max 1 (only 1 tab will open with one IP)
pmap-c# set connection conn-max1 (mean only one machine can connect)
#set connection conn-max2 per-client-max 1
#policy (control conn with size)
#policy input incoming traffic form outside client can send output (mostly it apply in dmz because we are to see blocking LAN
# access-list lan-to-smtp extended permit tcp 192.168..12.0 255.255.255.0 host 172.16.50.25 eq smpt

#class-map email-class
match access-list lan-to-smtp
policy map dmz-out
class email-class
policy output 8000000


config#service -policy dmz-out interface dmz
```

DOS/DDOS

```
access-list dos-ddos extended permit tcp only host 172.16.50.80 eq https

class-map dos-ddos-class
match access-list dos-ddos

policy-map out-dmz
class dos-ddos-class
set connection embroynic-conn-max 5 per-client mac 1

service-policy out-dmz interface outside

#TO DELETE KDY
crypto ket zeroize rsa (KEYNAME)
```

URL FILERING

> first you have to make reqest in http,https packet there is an header with website name on that on header there is an regex fidd firewall will scan header

```
regex web1 facebook.com
regex web2 youtube.com

class-map type regex match-any BLOCKSITE
match web1
match web2
```

NOW SCAN monitor regex.

```
class-map type inspect http macth-any http-class
match request header host regex class BLOCKSITE
policy-map type insect htto HTTPPOLICYMAP

class HTTPCLASS
reset logs

class-map PORT80
match access-list

policy-map inoutdmz
class PORT80


service-policy inoutdmz interface inside
```

