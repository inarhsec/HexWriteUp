---
description: >-
  Switching is process to forward packets coming in from one port to a port
  leading towards the destination.
cover: ../.gitbook/assets/SWITCHING_LOGO.png
coverY: 0
---

# 7. SWITCHING

### <mark style="color:purple;">Switch</mark>

> A switch is a Network Device operate under Layer 2 (Data Link Layer) of the OSI Model. Nowadays the Switches are evolve to L3 Switches.

> Its design to connect devices within the same local Network, Such as computer, Printers, And other Networked Devices.

> Switches use MAC Address and ARP to Forwarded data.

### <mark style="color:purple;">Ethernet Frame</mark>

> Ethernet frame is a packet that include ethernet headers.
>
> The minimum frame size is 64 bytes including the header packets in that there is desitnation MAC address, source MAC Address and Types etc. And to detect error Frame Check Sequence(FCS) is used.

### <mark style="color:purple;">**Switch Functions**</mark>

1. **Address Learning:** Switches learn MAC addresses by observing the source MAC address of incoming frames. They build and maintain a MAC address table.
2. **Forwarding Messages:** Switches use the MAC address table to make forwarding decisions. They forward frames only to the appropriate destination port.
3. **Loop Avoidance:** Switches use the Spanning Tree Protocol (STP) to prevent network loops, which can cause broadcast storms and network instability.

### <mark style="color:purple;">**Why Switches Are Essential**</mark>

* Switches provide efficient and fast data forwarding within LANs, reducing network congestion and improving performance.
* They enable devices to communicate directly with each other, minimizing unnecessary network traffic.
* Switches allow the segmentation of LANs into VLANs (Virtual LANs), improving network security and management.
* By learning MAC addresses, switches create efficient paths for data transmission, reducing broadcast domains.
* STP ensures network reliability by preventing loops and redundant paths.

### <mark style="color:purple;">**Initials Configurations**</mark>

| Step                              | Description                                                                                                                                                                        |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Power Up the Devices              | Ensure all network devices are powered on and operational.                                                                                                                         |
| Connect to the Device via Console | Use terminal emulation software (e.g., PuTTY or SecureCRT) to establish a console connection to the network switch through the COM port.                                           |
| Privilege Levels                  | By default, users may have privilege level 0, requiring a username and password for access.                                                                                        |
| Enable Mode                       | Enter enable mode (user/enable mode) using the "`enable`" command to gain elevated privileges.                                                                                     |
| Interface Information             | - To view all interfaces and their status: use the "show ip interface brief" command. - To view details of a specific interface: use `show ip interface <interface>`               |
| Configuration Mode                | Enter global configuration mode using commands like "`configure terminal`" or "`conf t`." This mode provides full access with privilege level 15.                                  |
| Using "do" with Commands          | While in configuration mode, you can use show commands by prefixing them with "`do`," such as "`do show ip int brief.`"                                                            |
| Interface Configuration           | Configure interface settings (e.g., speed, duplex, description) using commands like: - `interface <interface>` - `speed <speed>` - `duplex <duplex>` - `description <description>` |
| Selecting Multiple Interfaces     | Use the "`interface range`" command to select and configure multiple interfaces simultaneously.                                                                                    |
| Set Switch Hostname               | Assign a name to the switch using the `hostname <name>` command.                                                                                                                   |
| Banner Message                    | Create a banner message that users see when they log in.                                                                                                                           |
| Console Password                  | Set a password for console access using the "`line console 0`" command.                                                                                                            |
| Enable Telnet                     | Configure virtual lines (vty) for Telnet access.                                                                                                                                   |
| Management IP Address             | Assign an IP address to the management interface (usually VLAN 1).                                                                                                                 |
| Set Passwords                     | Set an enable secret password for privileged mode.                                                                                                                                 |
| Set Default Gateway               | Configure the default gateway.                                                                                                                                                     |
| Clear Configurations              | To delete all configurations, use the "`write erase`" command.                                                                                                                     |
| Disable DNS Lookup                | Use "`no ip domain lookup`" to disable DNS lookups.                                                                                                                                |
| Enable IP Routing (L3 Switch)     | Configure IP routing on Layer 3 switches.                                                                                                                                          |
| Save Configurations               | Save configurations to memory or copy them to a TFTP server.                                                                                                                       |
| Check Interface Configurations    | Use "show run" to view running configurations.                                                                                                                                     |
| Check Time                        | View the switch's current time with `"show clock`."                                                                                                                                |
| Change Time                       | Set the time with the "`clock set`" command.                                                                                                                                       |
| Change Timezone                   | Configure the timezone using "`clock timezone`"                                                                                                                                    |
| Interface Shutdown/No Shutdown    | Use "`shutdown`" and "`no shutdown`" to disable/enable an interface.                                                                                                               |
| Interface Access Mode             | Set an interface to access mode with "`switchport mode access`."                                                                                                                   |
| Interface Trunk Mode              | Set an interface to trunk mode with "`switchport mode trunk`."                                                                                                                     |
| DTP Modes                         | Configure Dynamic Trunking Protocol (DTP) modes.                                                                                                                                   |
| Check ARP Table                   | View the Address Resolution Protocol (ARP) table with "show ip arp."                                                                                                               |
| Encapsulation                     | Configure encapsulation for interfaces using "switchport trunk encapsulation dot1q."                                                                                               |

## <mark style="color:purple;">**Virtual Local Area Network**</mark>



| Topic                                          | Description                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What is VLAN (Virtual Local Area Network)?** | <p>VLAN, or Virtual Local Area Network, enhances network security by creating virtual partitions within a network. It isolates and segregates network traffic, making it act as a virtual wall between different parts of a network.<br>There are 4094 Vlan and VLAN 1 is default in switches.</p> |
| **Why Use VLANs?**                             | VLANs are used to improve network security and organization. They help segment a network into isolated parts, allowing different departments or groups to share the same network infrastructure while keeping their data separate and secure.                                                      |
| **Inter-Switch Link (ISL)**                    | **IEEE 802.1Q (Dot1q)**                                                                                                                                                                                                                                                                            |
| **Protocol Type**                              | Cisco Proprietary                                                                                                                                                                                                                                                                                  |
| **Header Modification**                        | Adds a proprietary 26-byte header to Ethernet frames, containing VLAN information.                                                                                                                                                                                                                 |
| **Compatibility**                              | Primarily used within Cisco environments; not compatible with non-Cisco devices.                                                                                                                                                                                                                   |
| **Supported VLANs**                            | Supports up to 1000 VLANs, suitable for large-scale networks.                                                                                                                                                                                                                                      |
| **Native VLAN**                                | Does not include Vlan Tags Used for managments purpose.                                                                                                                                                                                                                                            |
| **Tagging Process**                            | VLAN tagging occurs with the addition of a proprietary header at Layer 2.                                                                                                                                                                                                                          |
| **Dynamic Trunking Protocol (DTP)**            | **Three DTP modes**: Auto, Desirable, No Negotiate. Auto waits for commands from the other switch, Desirable initiates trunking, No Negotiate disables DTP.                                                                                                                                        |

### <mark style="color:blue;">Configuration of Vlans on Cisco Switch</mark>

#### <mark style="color:blue;">Access Port</mark>

> An Access port is switch port that can be a member of one VLAN.
>
> 1. Create a VLAN in the switch.
> 2. Add the VLAN into switch Ports.

{% code title="Create a Vlan" %}
```
SwitchX(config)# vlan 10
```
{% endcode %}

{% code title="Name the VLAN" %}
```
SwitchX(config-vlan)# name MGMT
```
{% endcode %}

> Now the VLAN is configured in switch, Assign the VLAN to port.

{% code title="Assiging the VLAN" %}
```
Switch(config)# interface Ethernet 0/0
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
```
{% endcode %}

> Some versions of Cisco switches automatically create the VLAN in the VLAN Database when you assign an access port to a VLAN

```
Switch(config)# interface Ethernet 0/1
Switch(config-if)# switchport mode access	
Switch(config-if)# switchport access vlan 30
% Access VLAN does not exist. Creating vlan 30
```

#### <mark style="color:blue;">Trunk Ports</mark>

> A trunk port that carry more then one VLAN.

```
Switch(config)# interface Ethernet1/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk encapsulation dot1q
```

#### <mark style="color:blue;">Native VLAN</mark>

> Its a VLAN which is not tagged or untagged in the TRUNK Port.

{% code title="Native Vlan" %}
```
Switch(config)# interface Ethernet 1/1
Switch(config-if)# switchport trunk native vlan 2
```
{% endcode %}

#### <mark style="color:blue;">Allowed VLAN</mark>

> Particular VLAN is allowed on the interface.

```
Switch(config)# interface Ethernet 2/1
Switch(config-if)# switchport trunk allowed vlan 10,20
Switch(config-if)# switchport trunk allowed vlan all
```

#### <mark style="color:blue;">Show command</mark>

> View the VLAN and interface configuration.

```
Switch# show vlan brief
Switch# show interfaces trunk
Switch# show interfaces Ethernet 0/1 switchport
Switch# show running-config interface Ethernet 1/1

Switch#show interfaces status
interface Ethernet1/1
 switchport trunk encapsulation dot1q
 switchport trunk native vlan 2
 switchport trunk allowed vlan 1-10,20-4094
 switchport mode trunk
end 
```



{% hint style="info" %}
In Cisco and Fitpipe Vlan 0 is used for QOS Configuration and VLAN 1 is used as default with untagged VLAN.\
But in Juniper VLAN 0 is used a default VLAN and VLAN 1 is used as a custom VLAN.
{% endhint %}

## <mark style="color:purple;">**VLAN Trunking Protocol**</mark>

| **VTP (VLAN Trunking Protocol)** | **Description**                                                                                                                                      |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purpose**                      | Simplifies VLAN configuration in networks with multiple switches by allowing one switch to configure VLANs and share that configuration with others. |
| **VTP Server Mode**              |  Default mode for all switches. - Can create, modify, and delete VLANs.                                                                              |
| **VTP Client Mode**              |  Cannot create or modify VLANs. - Receives VLAN information from VTP Servers.                                                                        |
| **VTP Transparent Mode**         |  Does not store VLAN information locally. - Passes VTP Server's VLAN configurations to connected switches.                                           |
| **Configuration (Server Mode)**  |  Set switch as a VTP Server: `vtp mode server` - Define VTP domain: `vtp domain Shadow` - Set VTP password: `vtp password ShadowGuardain`            |
| **Configuration (Client Mode)**  |  Set switch as a VTP Client: `vtp mode client` - Specify VTP domain: `vtp domain Shadow` - Set VTP password: `vtp password ShadowGuardain`           |

### <mark style="color:blue;">Configuration Of VTP on Cisco Switch</mark>

{% code title="Server Configuration" %}
```
Switch(config)#vtp domain CCNA
Changing VTP domain name from NULL to CCNA

SW1(config)#vtp password cisco
Setting device VLAN database password to cisco
```
{% endcode %}

{% hint style="info" %}
{% code overflow="wrap" %}
```
The default VTP mode on Cisco switches is the server mode, so the command vtp mode server wasn’t necessary in the SW1 configuration.
Now need to configure SW2 and SW3 as VTP clients.
```
{% endcode %}
{% endhint %}

{% code title="Client Configuration" %}
```
Switch(config)#vtp mode client 
Setting device to VTP CLIENT mode.

Switch(config)#vtp domain CCNA 
Changing VTP domain name from NULL to CCNA
```
{% endcode %}

## <mark style="color:purple;">Etherchannel</mark>

Etherchannel is a method used for link aggregation and redundancy in the network configuration.

Its operates under **IEEE 802.3ad**, which defines link aggregation

EtherChannel bundles multiple physical Ethernet links into a single logical link. This allows for increased bandwidth and provides redundancy, but the balancing depends on the hashing algorithm based on MAC, IP, or layer 4 headers, and not all traffic will equally use the bandwidth.

### <mark style="color:blue;">**Conditions**</mark>

* The switch must support IEEE 802.1 AD Standard.
* All cables in the EtherChannel bundle must have the same speed; mixing different cable speeds is not supported.

### <mark style="color:blue;">**TYPES**</mark>

#### <mark style="color:blue;">**LACP (Link Aggregation Control Protocol):**</mark>

* LACP stands for Link Aggregation Control Protocol it is an **open standard** defined by **IEEE 802.3ad (**&#x76;endor-neutra&#x6C;**),** which is used to establish and manage EtherChannels .
* LACP enables the combination of multiple network connections in parallel, improving performance and redundancy.

#### <mark style="color:blue;">MODE</mark>

* **Active Mode:** The device actively tries to make a connection by sending "hello" messages (LACP packets) to other devices on the network. If the other side responds, they create a connection.
* **Passive Mode:** The device waits for the other side to say "hello" first. It will connect if it receives the right message. But, if both sides are waiting (both in passive mode), nothing will happen because neither is sending the first message.
* **ON Mode**: Both devices connect without sending any "hello" messages or checks. This is a static EtherChannel configuration, meaning no protocols like LACP or PAgP are used to negotiate the connection. Both sides must be manually configured to use ON mode for the EtherChannel to work.

Configure EtherChannel on both switches

```
# On Switch 1
interface range gigabitEthernet 0/1 - 2
no shutdown
channel-group 1 mode active
exit

# On Switch 2
interface range gigabitEthernet 0/1 - 2
no shutdown
channel-group 1 mode passive
exit

Static (ON) Mode (No negotiation protocol)
# On both switches
interface range gigabitEthernet 0/1 - 2
no shutdown
channel-group 1 mode on
exit

#On Port-Channel Interface as trunk Interface
interface port-channel 1
switchport mode trunk
switchport mode trunk encapsulation dot1q
no shutdown
exit

#On Port-Channel Interface as Access Interface
interface port-channel 1
no shutdown
switchport mode access
switchport access vlan 1
exit
```

* Switch 1 is configured in `active` mode (it actively sends LACP packets). Switch 2 is in `passive` mode (it waits for LACP packets from Switch 1).
* Both sides are manually configured to establish the EtherChannel without using any negotiation protocols.

#### <mark style="color:blue;">PAgP (Cisco Proprietary)</mark>

Its same as LACP but only works on Cisco devices.

#### <mark style="color:blue;">Mode</mark>

* **Desirable Mode**: Actively tries to negotiate the EtherChannel.
* **Auto Mode**: Passively waits for the other device to negotiate the EtherChannel.
* **ON Mode** : Statically bundles the interfaces into an EtherChannel. This is a manual configuration and should be consistent on both ends of the link.

#### <mark style="color:blue;">**PAgP Configuration**</mark> <mark style="color:blue;"></mark><mark style="color:blue;">(Cisco-only environments)</mark>

```
# On Switch 1
interface range gigabitEthernet 0/1 - 2
no shutdown
channel-group 1 mode desirable
exit

# On Switch 2
interface range gigabitEthernet 0/1 - 2
no shudown
channel-group 1 mode auto
exit

Static (ON) Mode (No negotiation protocol)
# On both switches
interface range gigabitEthernet 0/1 - 2
no shutdown
channel-group 1 mode on
exit

#On Port-Channel Interface as trunk Interface
interface port-channel 1
switchport mode trunk
switchport mode trunk encapsulation dot1q
no shutdown
exit

#On Port-Channel Interface as Access Interface
interface port-channel 1
no shutdown
switchport mode access
switchport access vlan 1
exit

```

* Switch 1 is set to `desirable` mode, actively negotiating the EtherChannel. Switch 2 is in `auto` mode, waiting for Switch 1 to initiate the channel.
* Both sides are manually configured to establish the EtherChannel without using any negotiation protocols.

#### <mark style="color:blue;">Show Commands</mark>

```
show etherchannel summary
show interfaces port-channel
show lacp neighbor



```

## <mark style="color:purple;">CDP (Cisco Discovery Protocol) and LLDP (Link Layer Discovery Protocol)</mark>

**CDP (Cisco Discovery Protocol)** and **LLDP (Link Layer Discovery Protocol)** are Layer 2 protocols used for discovering neighboring devices and gathering important device information within a network.

* **CDP**: Cisco proprietary, typically used in Cisco environments but may work with some non-Cisco devices.
* **LLDP**: An open standard defined by IEEE 802.1AB, supported by various network vendors, making it useful in multi-vendor environments.

### <mark style="color:blue;">Cisco Discovery Protocol</mark>

* **Developed by**: Cisco Systems.
* **Functionality**: Discovers Cisco and, in some cases, non-Cisco devices. CDP shares information such as device type, hostname, IP address, interface details, and even VLAN and PoE capabilities.
* **Layer**: Operates at Layer 2 (Data Link Layer) of the OSI model.
* **Common Uses**: Gathering details about neighboring Cisco devices, IP phones, and managing VoIP deployments.

### <mark style="color:blue;">Link Layer Discovery Protocol</mark>

* **Defined by**: IEEE 802.1AB.
* **Functionality**: Allows devices from different vendors to exchange information. LLDP provides details such as system name, description, port information, VLAN, PoE capabilities, and more.
* **Layer**: Operates at Layer 2 (Data Link Layer).
* **Common Uses**: Managing multi-vendor environments, VoIP deployments, and identifying network topology.

{% hint style="info" %}
These protocols help network administrators discover and understand the topology of their networks by providing information about directly connected devices.&#x20;
{% endhint %}

### <mark style="color:blue;">Configure CDP</mark>

**Enable CDP**

```
Switch# configure terminal
Switch(config)# cdp run

```

**Enable or Disbale CDP in Interface.**

```
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# no cdp enable  # Disable CDP on this interface

```

**Adjusting Timers and Hold Time**

```
Switch(config)# cdp timer 60        # Send CDP updates every 60 seconds
Switch(config)# cdp holdtime 180    # Retain CDP information for 180 seconds
```

**Show command**

```
Switch# show cdp neighbors
Switch# show cdp neighbors detail
```

### <mark style="color:blue;">Configure LLDP</mark>

**Enable LLDP Globally**

```
Switch# configure terminal
Switch(config)# lldp run

```

**LLDP Interface Configuration:**

```
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# no lldp transmit   # Disable LLDP transmit on this interface
Switch(config-if)# no lldp receive    # Disable LLDP receive on this interface

```

**Show command**

```
Switch# show lldp neighbors
Switch# show lldp neighbors detail
```

## <mark style="color:purple;">**Spanning Tree Protocol (STP):**</mark>

Spanning Tree Protocol (STP) is a network protocol used to prevent loops in Ethernet networks, particularly in bridged or switched networks. STP ensures that there is only one logical path between all destinations on the network, preventing broadcast storms and other issues that can arise from network loops.

<mark style="color:blue;">**Phases of STP:**</mark>

1. **Election of Root and Bridge ID:**
   * In the initial phase, switches elect a Root Bridge. The Root Bridge serves as the central reference point for the entire STP network.
   * Each switch has a Bridge ID, which includes a priority value and a MAC address.
   * By default, the Bridge ID priority on Cisco switches is 32768 for all VLANs. This priority remains the same for every VLAN unless explicitly configured otherwise. The value 32769 is incorrect and can lead to misunderstanding.
   * The switch with the lowest Bridge ID becomes the Root Bridge.
   * If multiple switches have the same Bridge ID, the switch with the lowest MAC address is elected as the Root Bridge.
   * Bridge Protocol Data Units (BPDU) packets are used for Root Bridge election.

{% hint style="info" %}
32768 if SYN Count then 32769 +  1 increase with Vlan Counts Becasue Best Devices has the Lowest Bridge ID
{% endhint %}

2. **Election of Root Port:**
   * Each switch determines its best path (Root Port) to reach the Root Bridge.
   * The best path is determined based on the lowest cumulative cost (port cost) to reach the Root Bridge.
   * Port costs are assigned based on link speeds. For example, FastEthernet has a lower cost than Ethernet.
   * The switch with the lowest cumulative cost to reach the Root Bridge becomes the Root Port.

| Linkspeed         | Speed    | Post Cost |
| ----------------- | -------- | --------- |
| Ethernet          | 10 MBPS  | 100       |
| FastEthernet      | 100 MBPS | 19        |
| GigabitEthernet   | 1 GBPS   | 4         |
| 10GigabitEthernet | 10 GBPS  | 2         |

3. **Blocking Ports:**
   * After determining the Root Bridge and Root Port, STP identifies and blocks certain ports to prevent loops.
   * Ports on non-Root Bridges that are not part of the best path to the Root Bridge are blocked.
   * Blocked ports do not forward traffic but are in a "listening and learning" state.

**STP Process:**

* STP has multiple phases, but the time it takes is based on timers. Specifically, **15 seconds for Listening** and **15 seconds for Learning**, but the total convergence time could be more depending on the network size and spanning tree configuration. 30 seconds is the default time, but this can be changed.
* The first 15 seconds are in the "listening" mode, where switches receive BPDU packets and exchange information.
* The next 15 seconds are in the "learning" mode, during which switches determine the Root Bridge and Root Port.
* Once the Root Bridge and Root Port are identified, the remaining ports are blocked to prevent loops.

STP is crucial for network stability and redundancy in Ethernet networks. It ensures that even in complex network topologies, there is a single logical path to reach each destination, preventing data collisions and broadcast storms.

### <mark style="color:blue;">Configuration</mark>

**Root Bridge Election Configuration**

```
Switch(config)# spanning-tree vlan <vlan-id> priority 4096
```

**Root Port Election**

```
Switch(config-if)# spanning-tree vlan <vlan-id> cost <value>
```

**Blocking And Listening States**

```
Switch(config)# spanning-tree vlan <vlan-id> forward-time <time>
```

## <mark style="color:purple;">**Cisco Nexus**</mark>

## <mark style="color:purple;">**Virtual Port Channel**</mark>

## &#x20;<mark style="color:purple;">**HSRP AND VRRP**</mark>



### Switch Nexus Migration

> This is the Basic Introduction/setpup of Any Switch mostly Cisco Lower model Switch to Nexus Migration.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

#### Phase 1 — Physical Inventory

What hardware do you actually have, and what can the Nexus replace.

```
show version
show inventory
show interfaces status
show interfaces | include (line|Hardware|MTU|BW|duplex|speed|input|output)
show cdp neighbors detail
show lldp neighbors detail
```

Things to capture: total port count, SFP vs copper, module types, current IOS-XE version, serial numbers for asset records, uplink interfaces and their speeds (1G/10G/25G/40G).

**Free ports check:**

```
show interfaces status | include notconnect
show interfaces status | include err-disabled
```

Document every notconnect and err-disabled port — these are your unused ports. Also note which are in use but have no MAC learned (inactive devices).

***

#### Phase 2 — Architecture Review

Where does this switch sit in the network hierarchy?

```
show cdp neighbors detail
show lldp neighbors detail
show spanning-tree summary
show spanning-tree detail
show ip route summary
```

Ask yourself: is this C1300 acting as access, distribution, or core? Is it single-homed or dual-homed? Does it peer with a router or is it purely L2? This decides which Nexus model fits (9k access vs distribution).

***

#### Phase 3 — Interface & VLAN Configuration

This is the most tedious part — every port's config must be mapped.

```
show running-config
show vlan brief
show vlan id <id>
show interfaces trunk
show interfaces switchport
show mac address-table
show mac address-table count
```

For each interface, capture: mode (access/trunk), native VLAN, allowed VLANs, speed/duplex, description, shutdown state, any service policies applied.

**VLAN mapping table to build:**

| VLAN ID | Name | Ports | Purpose | Map to Nexus? |
| ------- | ---- | ----- | ------- | ------------- |

***

#### Phase 4 — Port-Channel / LAG

```
show etherchannel summary
show etherchannel detail
show etherchannel port
show lacp neighbor
show lacp counters
show pagp neighbor
```

Note every port-channel: member interfaces, protocol (LACP/PAgP/static), mode (active/passive/on), load-balancing hash method, min-links configured. On Nexus, these migrate to `port-channel` with `vpc` if dual-homed — big design decision.

***

#### Phase 5 — Routing Protocols & Layer 3

```
show ip protocols
show ip ospf
show ip ospf neighbor
show ip ospf database summary
show ip bgp summary
show ip bgp
show ip route
show ip route ospf
show ip route bgp
show ip route static
show ip interface brief
show ip interface
show interfaces vlan
```

**For SVIs specifically:**

```
show ip interface vlan <id>
show running-config | section interface Vlan
```

Document every SVI, its IP, VRF membership, helper addresses (DHCP relay), and HSRP/VRRP config:

```
show standby brief
show standby detail
show vrrp brief
```

***

#### Phase 6 — MPLS (Critical if you have WAN PE/CE)

```
show mpls interfaces
show mpls ldp neighbor
show mpls ldp bindings
show mpls forwarding-table
show ip vrf
show ip vrf detail
show ip route vrf <name>
show ip bgp vpnv4 all summary
show mpls traffic-eng tunnels
```

Note: Cisco Catalyst 1300 is primarily an access/SMB switch — if it's doing MPLS, double-check whether it's the CE or if there's a separate router (ISR/ASR) upstream. Nexus 9k NX-OS supports MPLS but this needs careful platform selection (not all Nexus lines support full MPLS).

***

#### Phase 7 — Spanning Tree

```
show spanning-tree
show spanning-tree summary
show spanning-tree detail
show spanning-tree vlan <id>
show spanning-tree vlan <id> detail
show spanning-tree blockedports
```

Capture: STP mode (PVST+, RSTP, MSTP), root bridge per VLAN, port roles (root/designated/alternate/backup), timers, portfast status, BPDU guard/filter ports. On Nexus you'll move to Rapid-PVST or MST — root placement strategy must be re-evaluated, especially with vPC.

***

#### Phase 8 — QoS

```
show policy-map
show policy-map interface
show class-map
show mls qos
show mls qos interface
show mls qos maps
```

Capture every policy-map, class-map, DSCP markings, queuing behavior. Nexus uses MQC similarly but the queue architecture is different — especially on 9k line cards.

***

#### Phase 9 — Security Policies

```
show ip access-lists
show access-lists
show running-config | section ip access-list
show port-security
show port-security interface <int>
show dot1x all
show dot1x statistics
show authentication sessions
show authentication sessions interface <int>
show ip dhcp snooping
show ip dhcp snooping binding
show ip dhcp snooping statistics
show ip arp inspection
show ip arp inspection statistics
show storm-control
```

Every ACL, 802.1X policy, DHCP snooping config, and ARP inspection rule must be documented and converted to NX-OS equivalents.

***

#### Phase 10 — Management Plane

```
show running-config | section ntp
show ntp status
show ntp associations
show running-config | section snmp
show running-config | section logging
show running-config | section aaa
show running-config | section tacacs
show running-config | section radius
show running-config | section username
show privilege
show users
```

Capture: NTP servers, SNMP community strings and v3 users, syslog destinations, AAA config (TACACS/RADIUS servers, method lists), local user accounts.

***

#### Phase 11 — Logs and Error Baseline

This is your health snapshot before migration — compare this post-migration.

```
show interfaces counters errors
show interfaces counters
show logging
show log | include (ERR|WARN|CRIT|down|up|flap)
show interfaces | include (error|reset|ignored|overrun|abort)
show environment all
show environment power
show environment temperature
show environment fan
show processes cpu history
show processes memory sorted
show platform resources
```

Look specifically for: CRC errors, input/output drops, interface flaps in logs, any hardware alarm, high CPU processes. These are existing problems that must not get carried into the new switch.

***

#### Phase 12 — Feature Gap Analysis (C1300 IOS-XE → NX-OS)

Key differences to plan for:

| Feature          | C1300 IOS-XE    | NX-OS (Nexus)                                |
| ---------------- | --------------- | -------------------------------------------- |
| STP              | PVST+ / RSTP    | Rapid-PVST / MST                             |
| Port-channel     | EtherChannel    | Port-channel + vPC                           |
| L3 routing       | standard IOS    | NX-OS (similar but different syntax)         |
| MPLS             | limited on 1300 | Nexus 9k supports, needs license             |
| AAA              | IOS AAA         | NX-OS AAA (same TACACS but different syntax) |
| Interface naming | Gi1/0/1         | Ethernet1/1                                  |
| VRF              | ip vrf          | vrf context                                  |
| HSRP             | supported       | use HSRP or move to vPC+anycast gateway      |
| QoS              | MLS QoS / MQC   | NX-OS MQC                                    |

***

#### Phase 13 — Cutover & Rollback Plan

Before cutover day, prepare:

1. Full `show running-config` saved to TFTP/SCP off-device
2. Cable labeling per port (photo every patch panel / switch face)
3. MAC-to-IP-to-port mapping exported
4. Change window defined (low-traffic period)
5. Rollback trigger defined (X minutes of outage = rollback)
6. Nexus staging config pre-tested in lab (PNetLab is perfect for this)
7. Console access confirmed on Nexus before pulling C1300



## <mark style="color:purple;">**Cisco Nexus Migration Report**</mark>

{% file src="../.gitbook/assets/Nexus_vPC_Config_v2.pdf" %}

{% file src="../.gitbook/assets/Netmagic_CoreSwitch_Migration_Assessment Updated.pdf" %}

{% file src="../.gitbook/assets/Netmagic_CoreSwitch_Migration_Assessment Updated.docx" %}

{% file src="../.gitbook/assets/Nexus_vPC_Config_v2.docx" %}



## <mark style="color:purple;">**Aruba HPE Networking and Cisco CLI Reference**</mark>

{% hint style="info" %}
The commands and options may vary based on the specific features and versions of the devices. Please refer to the respective documentation for accurate and up-to-date information
{% endhint %}

**Comparing View and Configuration Prompts**

| Context Legend                              | ProVision            | Comware     | Cisco            |
| ------------------------------------------- | -------------------- | ----------- | ---------------- |
| U = User Exec / User View                   | `ProVision>`         | `<Comware>` | `Cisco>`         |
| P = Privileged Exec                         | `ProVision#`         | `Nulll`     | `Cisco#`         |
| S = System View (equal to Priviledged Exec) | `Null`               | `[Comware]` | `Null`           |
| C = Configuration                           | `ProVision(config)#` | `[Comware]` | `Cisco(config)#` |

**Comparing Frequently Used Commands**

| ProVision                                     | Comware 5                                 | Comware                        | Cisco                                   |
| --------------------------------------------- | ----------------------------------------- | ------------------------------ | --------------------------------------- |
| `ProVision(config)# console inactivity-timer` | `[Comware]user-interface aux 0`           | `Same`                         | `Cisco(config)#line console 0`          |
| `ProVision# show tech`                        | `<Comware>display diagnostic-information` | `Same`                         | `Cisco#show tech-support`               |
| `ProVision(config)# lldp run`                 | `[Comware5]lldp enable`                   | `[Comware7]lldp global enable` | `Cisco(config)#lldp run`                |
| `untagged`                                    | `access`                                  | `Same`                         | `access`                                |
| `tagged`                                      | `trunk`                                   | `Same`                         | `trunk`                                 |
| `trunk`                                       | `bridge aggregation`                      | `Same`                         | <p></p><p><code>etherchannel</code></p> |

**Comparing Frequently Used Commands**

| Operating System | ProVision                | Comware                                                              | Cisco                         |
| ---------------- | ------------------------ | -------------------------------------------------------------------- | ----------------------------- |
| U                | `enable`                 | U `system-view`                                                      | U `enable`                    |
| P                | `configure`              | U `system-view (configuration mode is same as being at System View)` | U `configure terminal`        |
| U/P/C            | `show flash`             | U `dir`                                                              | U/P `show flash`              |
| U/P/C            | `show version`           | U/S `display version`                                                | U/P `show version`            |
| P/C              | `show run`               | U/S `display current-configuration`                                  | `P show run`                  |
| P/C              | `show config`            | U/S `display saved-configuration`                                    | P `show start`                |
| U/P/C            | `show history`           | U/S `display history`                                                | U/P `show history`            |
| U/P/C            | `show logging`           | U/S `display info-center`                                            | `U/P show logging`            |
| U/P/C            | `show ip route`          | U/S `display ip routing-table`                                       | U/P `show ip route`           |
| U/P/C            | `show ip`                | U/S `display ip interface brief`                                     | U/P `show ip interface brief` |
| U/P/C            | `show interface brief`   | U/S `display interface brief`                                        | U/P `show interfaces status`  |
| P/C              | `erase startup-config`   | U `reset saved`                                                      | P `erase start`               |
| P/C              | `show config <filename>` | U `more <filename>`                                                  | P `more flash:/<filename>`    |
| P/C              | `reload`                 | U `reboot`                                                           | P `reload`                    |
| P/C              | `write memory`           | U/S `save`                                                           | P `write memory`              |
| P                | `show tech`              | U/S `display diagnostic-information`                                 | U/P `show tech-support`       |
| U/P/C            | `show`                   | U/S `display`                                                        | U/P `show`                    |
| U/P/C            | `no`                     | U/S `undo`                                                           | P `no`                        |
| C                | `end`                    | S `return`                                                           | C `end`                       |
| U/P/C            | `exit`                   | U/S `quit`                                                           | U/P/C `exit`                  |
| P/C              | `erase`                  | U/S `delete`                                                         | P `erase`                     |
| P/C              | `copy`                   | U `copy/tftp`                                                        | P `copy`                      |
| C                | `hostname`               | S `sysname`                                                          | C `hostname`                  |
| C                | `logging`                | S `info-center`                                                      | C `logging`                   |
| C                | `router rip`             | S `rip`                                                              | C `router rip`                |
| C                | `router ospf`            | S `ospf`                                                             | C `router ospf`               |
| C                | `ip route`               | S `ip route-static`                                                  | C `ip route`                  |
| C                | `access-list`            | S `acl`                                                              | C `access-list`               |

**Management Access**

| Context                                       | ProVision            | Comware       | Cisco            |
| --------------------------------------------- | -------------------- | ------------- | ---------------- |
| User Exec / User View                         | `ProVision>`         | `<Comware>`   | `Cisco>`         |
| Privileged Exec                               | `ProVision#`         |               | `Cisco#`         |
| System View (return to User View with Ctrl+Z) |                      | `system-view` |                  |
| Configuration                                 | `ProVision(config)#` | `[Comware]`   | `Cisco(config)#` |

**Configuration Access**

| Context         | ProVision              | Comware                             | Cisco                       |
| --------------- | ---------------------- | ----------------------------------- | --------------------------- |
| Privileged Exec | `ProVision# configure` | No specific command, see note below | `Cisco# configure terminal` |
| Configuration   | `ProVision(config)#`   | `[Comware]`                         | `Cisco(config)#`            |

**Console Access—Baud Rate**

| Context       | ProVision                                | Comware                                                    | Cisco                                                        |
| ------------- | ---------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| Configuration | `ProVision(config)# console baud-rate ?` | `[Comware]user-interface aux 0` `[Comware-ui-aux0]speed ?` | `Cisco(config)# line console 0``Cisco(config-line)# speed ?` |

**Console Access—Baud Rate**

| Context       | ProVision                                | Comware                                   | Cisco                                                         |
| ------------- | ---------------------------------------- | ----------------------------------------- | ------------------------------------------------------------- |
| Configuration | `ProVision(config)# console baud-rate ?` | `[Comware]user-interface aux 0` `speed ?` | `Cisco(config)# line console 0` `Cisco(config-line)# speed ?` |

**Reload & Timed Reload**

| Context                      | ProVision                                                                                                                                    | Comware5                            | Cisco                 |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | --------------------- |
| Reload Command               | `ProVision# reload`                                                                                                                          | `<Comware5>reboot`                  | `Cisco#reload`        |
| Reload Options               | `ProVision# reload ?`                                                                                                                        | `<Comware5>reboot ?`                | `Cisco#reload ?`      |
| Timed Reload                 | `ProVision# reload <Comware5>schedule reboot ?`                                                                                              | `<Comware5>schedule reboot ?`       |                       |
| Show Reload Status           | `ProVision# show reload ?`                                                                                                                   | `<Comware5>display schedule reboot` | `Cisco#show reload`   |
| Cancel Reload                | `ProVision(config)# no reload`                                                                                                               | `<Comware5>undo schedule reboot`    | `Cisco#reload cancel` |
| Additional Comware7 Commands | `<Comware7>reboot`, `<Comware7>reboot ?`, `<Comware7>scheduler reboot ?`, `<Comware7>display scheduler ?`, `<Comware7>undo scheduler reboot` |                                     |                       |

**USB**

| Context           | ProVision                | Comware5                 | Cisco                                                 |
| ----------------- | ------------------------ | ------------------------ | ----------------------------------------------------- |
| USB Feature       | not an available feature | not an available feature |                                                       |
| Comware7 Commands | `ProVision# dir`         | `<Comware7>dir usba0:/`  | `ProVision# show usb-port` `Cisco#display device usb` |

**System and Environment**

| Context                 | ProVision                             | Comware                                                             | Cisco                                      |
| ----------------------- | ------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------ |
| Show System Information | `ProVision# show system information`  | `<Comware>display device manuinfo``<Comware>display device verbose` | `Cisco#show inventory``Cisco#show version` |
| Show Modules            | `ProVision# show modules`             |                                                                     |                                            |
| Show Fans               | `ProVision# show system fans`         | `<Comware>display fan`                                              | `Cisco#show env fan`                       |
| Show Power Supply       | `ProVision# show system power-supply` | `<Comware>display power`                                            | `Cisco#show env power`                     |
| Show Temperature        | `ProVision# show system temperature`  | `<Comware>display environment`                                      | `Cisco#show env temperature`               |

**Remote Management Sessions—Viewing**

| Context              | ProVision                | Comware                  | Cisco               |
| -------------------- | ------------------------ | ------------------------ | ------------------- |
| Show Telnet Sessions | `ProVision# show telnet` | `<Comware>display users` | `Cisco# show users` |

**Tech Support Information Output Listing**

| Context                       | ProVision              | Comware                                   | Cisco                     |
| ----------------------------- | ---------------------- | ----------------------------------------- | ------------------------- |
| Show Tech Support Information | `ProVision# show tech` | `<Comware>display diagnostic-information` | `Cisco#show tech-support` |

**Motd (Message of the Day)**

| Context       | ProVision                                                                          | Comware                                                                                | Cisco                                                                         |
| ------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Configuration | `ProVision(config)# banner motd #``Enter TEXT message. End with the character '#'` | `[Comware]header motd #``Please input banner content, and quit with the character '#'` | `Cisco(config)#banner motd #``Enter TEXT message. End with the character '#'` |

**Source Interface for Management Communications**

| Context                           | ProVision                                                                                                       | Comware                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Cisco                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Configuration                     | `ProVision(config)# ip source-interface ?`                                                                      | `Cisco(config)#ip <service> source-interface ?` `Cisco(config)#<service> source-interface ?`                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| IP Source Interface Configuration | `ProVision(config)# ip source-interface all 10.0.111.21` `ProVision(config)# ip source-interface syslog vlan 1` | `[Comware]info-center loghost source Vlan-interface 1` `[Comware]radius nas-ip 10.0.111.31` `[Comware]hwtacacs nas-ip 10.0.111.31` `[Comware]ftp client source interface Vlan-interface 1` `[Comware]tftp client source interface Vlan-interface 1` `[Comware]ntp source-interface Vlan-interface 100` `[Comware]telnet client source interface Vlan-interface 1` `[Comware]ssh client source interface Vlan-interface 1` `[Comware] sflow source ip 10.0.111.31` `[Comware]snmp-agent trap source Vlan-interface 1` | `Cisco(config)#logging source-interface vlan 1` `Cisco(config)#ip radius source-interface vlan 1` `Cisco(config)#ip tacacs source-interface vlan 1` `Cisco(config)#ip ftp source-interface vlan 1` `Cisco(config)#ip tftp source-interface vlan 1` `Cisco(config)#ip sntp source-interface vlan 1` `Cisco(config)#ip telnet source-interface vlan 1` `Cisco(config)#ip ssh source-interface vlan 1` `Cisco(config)#ip source-interface vlan 1` `Cisco(config)#ntp source vlan 1` `Cisco(config)#ip telnet source-interface vlan 1` `Cisco(config)#ip ssh source-interface vlan 1` `Cisco(config)#ip sflow source-interface vlan 1` `Cisco(config)#snmp-server source-interface traps vlan 1` |
| Show Source Interface             | `ProVision# show ip source-interface`                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

**Local User ID and Password, and Console Access**

| Context                                                   | ProVision                                                                                                                                             | Comware5                                                                                                                                                                                                     | Cisco                                                                                                                                                 |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enable Password                                           | `Cisco(config)#enable password 0 <password>`                                                                                                          | `[Comware5]super password level 3 simple password` `[Comware5]super password level 3 cipher password`                                                                                                        | `Cisco(config)#enable secret 0 <password>`                                                                                                            |
| Password Configuration                                    | `ProVision(config)# password manager user-name <name> plaintext <password>`                                                                           | `[Comware5]local-user <name>` `[Comware5-luser-manager]password simple <password>` `[Comware5-luser-manager]authorization-attribute level 3` `[Comware5-luser-manager]service-type terminal`                 | `Cisco(config)#username <name> privilege 15 password <password>`                                                                                      |
| Operator Password Configuration                           | `ProVision(config)# password operator user-name <name> plaintext <password>`                                                                          | `[Comware5]local-user <name>` `[Comware5-luser-operator]password simple <password>` `[Comware5-luser-operator]authorization-attribute level 1` `[Comware5-luser-manager]service-type terminal`               | `Cisco(config)#username <name> privilege 0 password <password>`                                                                                       |
| Console Authentication Configuration                      | Not applicable                                                                                                                                        | `[Comware5]user-interface aux 0` `[Comware5-ui-aux0]authentication-mode scheme`                                                                                                                              | `Cisco(config)#line console 0` `Cisco(config-line)#login local`                                                                                       |
| Console Authentication Configuration (Alternate)          | Not applicable                                                                                                                                        | `[Comware5]user-interface aux 0` `[Comware5-ui-aux0]authentication-mode password` `[Comware5-ui-aux0]set authentication password simple password`                                                            | `Cisco(config)#line console 0` `Cisco(config-line)#login` `Cisco(config-line)#password password`                                                      |
| Comware7 Console Authentication Configuration             | `[Comware7]super password role network-admin simple password` `[Comware7]super password role network-admin hash <hashtext password>`                  | `[Comware7]local-user manager` `[Comware7-luser-manager]password simple password` `[Comware7-luser-manager]authorization-attribute user-role network-admin` `[Comware7-luser-manager]service-type terminal`  | `[Comware7]user-interface aux 0` `[Comware7-line-aux0]authentication-mode scheme`                                                                     |
| Comware7 Console Authentication Configuration (Alternate) | `[Comware7]user-interface aux 0` `[Comware7-line-aux0]authentication-mode password` `[Comware7-line-aux0]set authentication password simple password` | `[Comware7]local-user <name>` `[Comware7-luser-manager]password simple <password>` `[Comware7-luser-manager]authorization-attribute user-role network-admin` `[Comware7-luser-manager]service-type terminal` | `[Comware7]user-interface aux 0` `[Comware7-line-aux0]authentication-mode password` `[Comware7-line-aux0]set authentication password simple password` |

**Protect Local Password**

| Context                                  | ProVision                                                      | Comware                                       | Cisco                                        |
| ---------------------------------------- | -------------------------------------------------------------- | --------------------------------------------- | -------------------------------------------- |
| Disable Password Clear on Front Panel    | `ProVision(config)# no front-panel-security password-clear`    | `<Comware>undo startup bootrom-access enable` | `Cisco(config)#no service password-recovery` |
| Disable Factory Reset on Front Panel     | `ProVision(config)# no front-panel-security factory-reset`     |                                               |                                              |
| Disable Password Recovery on Front Panel | `ProVision(config)# no front-panel-security password-recovery` |                                               |                                              |
| Show Front Panel Security Status         | `ProVision# show front-panel-security`                         | `<Comware>display startup`                    | `Cisco#show version`                         |

| Context                            | ProVision                                                                                   | Comware                                                                                                                                                           | Cisco                                                                                                                                                                                           |
| ---------------------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Minimum Password Length            | `ProVision(config)# password minimum-length 10`                                             | `[Comware]password-control enable` `[Comware]password-control length 10`                                                                                          | `Cisco(config)#aaa new-model` `Cisco(config)#password configuration-control` `Cisco(config-cc-policy)#min-length 10`                                                                            |
| Password Aging Configuration       | `ProVision(config)# password configuration aging` `[Comware]password-control length enable` |                                                                                                                                                                   | `Cisco(config-cc-policy)#max-length 10`                                                                                                                                                         |
| Password Composition Configuration | `ProVision(config)# password complexity all`                                                | `[Comware]password-control composition enable` `[Comware]password-control complexity same-character check` `[Comware]password-control complexity user-name check` | `Cisco(config-cc-policy)#numeric-count 2` `Cisco(config-cc-policy)#special-case 2` `Cisco(config-cc-policy)#upper-case 2` `Cisco(config-cc-policy)#lower-case 2` `Cisco(config-cc-policy)#exit` |
| User Password Configuration        |                                                                                             |                                                                                                                                                                   | `Cisco(config)#username manager privilege 15 common-criteria-policy pwcomplex password PA55word!^`                                                                                              |
| Show Password Configuration        | `ProVision# show password-configuration`                                                    | `[Comware]display password-control`                                                                                                                               | `Cisco#show aaa common-criteria policy name pwcomplex`                                                                                                                                          |

**File Copy and Boot Commands**

| Context                        | ProVision                                                  | Comware                                                                                                                          | Cisco                                                                          |
| ------------------------------ | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Show Flash Contents            | `ProVision# show flash`                                    | `<Comware>dir`                                                                                                                   | `Cisco#show flash:`                                                            |
| Show Version Information       | `ProVision# show version`                                  | `<Comware>display version`                                                                                                       | `Cisco#show version`                                                           |
| TFTP Copy from Server to Flash | `ProVision# copy tftp flash 10.0.100.111 K_15_16_0004.swi` | `<Comware>tftp 10.0.100.111 get A5500EI-CMW520-R2221P07.bin`                                                                     | `Cisco#copy tftp://10.0.100.111/c3750-advipservicesk9-mz.122-46.SE.bin flash:` |
| SFTP Copy from Server to Flash | `ProVision# copy sftp flash 10.0.100.111 K_15_16_0004.swi` | `<Comware>scp 10.0.100.111 get A5500EI-CMW520-R2221P07.bin`                                                                      | `Cisco#copy scp://10.0.100.111/c3750e-universalk9-mz.150-2.SE7.bin flash:`     |
| USB Copy to Flash              | `ProVision# copy usb flash K_15_16_0004.swi`               | `<Comware7>copy usba0:/5900_5920-CMW710-R2311P05.ipe flash:/5900_5920-CMW710-R2311P05.ipe` (Note: Comware5 does not support USB) | `ProVision# copy xmodem flash` (Note: Comware7 does not support xmodem)        |
| XMODEM Copy to Flash           | `<Comware>xmodem get flash:/`                              |                                                                                                                                  | `Cisco#copy xmodem: flash:`                                                    |
| Flash Copy to Secondary        | `ProVision# copy flash flash secondary`                    |                                                                                                                                  |                                                                                |
| TFTP Copy from Flash           | `ProVision# copy flash tftp 10.0.100.111 K_15_16_0004.swi` | `<Comware>tftp 10.0.100.111 put a5500ei-cmw520-r2221p07.bin`                                                                     | `Cisco#copy flash: tftp:`                                                      |
| SFTP Copy from Flash           | `ProVision# copy flash sftp 10.0.100.111 K_15_16_0004.swi` | `<Comware>scp 10.0.100.111 put a5500ei-cmw520-r2221p07.bin`                                                                      | `Cisco#copy flash: scp:`                                                       |
| USB Copy from Flash            | `ProVision# copy flash usb K_15_16_0004.swi`               | `<Comware7>copy flash:/5900_5920-CMW710-R2311P05.ipe usba0:/` (Note: Comware5 does not support USB)                              | `ProVision# copy flash xmodem`                                                 |
| Set Default Boot Image         | `ProVision# boot set-default flash primary`                | `<Comware>boot-loader file flash:/a5500ei-cmw520-r2221p07.bin slot 1 main`                                                       | `Cisco(config)# boot system flash:c3750-advipservicesk9-mz.122-46.SE.bin`      |

| Context                                       | ProVision                                                                       | Comware                                                                            | Cisco                                                                                                                                                                                                 |
| --------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Show Running Configuration                    | `ProVision# show running-config ?`                                              | `<Comware>display current-configuration ?`                                         | `Cisco#show running-config ?` (Note: must save current configuration, then copy file accordingly)                                                                                                     |
| Copy Running Configuration to TFTP            | `ProVision# copy running-config tftp 10.0.100.111 config2.cfg`                  | `<Comware>tftp 10.0.100.111 put comware_main.cfg comware_startup-config.cfg`       | `Cisco#copy running-config tftp://10.0.100.111/Cisco.cfg`                                                                                                                                             |
| Copy Running Configuration to SFTP            | `ProVision# copy running-config sftp 10.0.100.111 config2.cfg`                  | (Credentials prompt)                                                               | `Cisco#copy running-config scp:` (Address or name of remote host \[]? 10.0.100.111, Destination username \[manager]?, Destination filename \[Cisco.cfg]?, Password: \*\*\*\*\*\*\*\*)                 |
| Copy Running Configuration to USB             | `ProVision# copy running-config usb config2`                                    | (Not supported)                                                                    |                                                                                                                                                                                                       |
| Copy Running Configuration via XMODEM         | `ProVision# copy running-config xmodem`                                         |                                                                                    |                                                                                                                                                                                                       |
| Copy Startup Configuration to TFTP            | `ProVision# copy startup-config tftp 10.0.100.111 ProVision_startup-config.cfg` | `<Comware>backup startup-configuration to 10.0.100.111 comware_startup-config.cfg` | `Cisco#copy startup-config tftp://10.0.100.111/Cisco_startup-config.cfg`                                                                                                                              |
| Copy Startup Configuration to SFTP            | `ProVision# copy startup-config sftp 10.0.100.111 ProVision_startup-config.cfg` | (Credentials prompt)                                                               | `Cisco#copy startup-config scp:` (Address or name of remote host \[]? 10.0.100.111, Destination username \[manager]?, Destination filename \[Cisco\_startup-config.cfg]?, Password: \*\*\*\*\*\*\*\*) |
| Copy Configuration File to Multiple Locations | `ProVision# copy config config1 config config2`                                 | `<Comware>copy flash:/comware_main.cfg flash:/comware_main2.cfg`                   | `Cisco#copy flash:Cisco.cfg flash:Cisco_2.cfg`                                                                                                                                                        |
| Copy Configuration File to TFTP               | `ProVision# copy config config1 tftp 10.0.100.111 config1.cfg`                  | `<Comware>tftp 10.0.100.111 put comware_main.cfg comware_startup-config.cfg`       | `Cisco#copy flash:Cisco.cfg tftp://10.0.100.111/Cisco_2.cfg`                                                                                                                                          |
| Copy Configuration File to SFTP               | `ProVision# copy config config1 sftp 10.0.100.111 config1.cfg`                  | (Credentials prompt)                                                               | `Cisco#copy flash:Cisco.cfg scp:` (Address or name of remote host \[]? 10.0.100.111, Destination username \[manager]?, Destination filename \[Cisco.cfg]?, Password: \*\*\*\*\*\*\*\*)                |
| Erase Startup Configuration                   | `ProVision# erase startup-config`                                               | `<Comware>reset saved-configuration main`                                          | `Cisco#erase startup-config`                                                                                                                                                                          |
| Copy TFTP Startup Configuration               | `ProVision# copy tftp startup-config 10.0.100.111 config6.cfg`                  | `<Comware>tftp 10.0.100.111 get comware_main.cfg startup.cfg`                      | `Cisco#copy tftp://10.0.100.111/Cisco_config3.cfg config.text`                                                                                                                                        |
| Copy SFTP Startup Configuration               | `ProVision# copy sftp startup-config 10.0.100.111 config6.cfg`                  | (Credentials prompt)                                                               | `Cisco#copy scp: startup-config` (Address or name of remote host \[]? 10.0.100.111, Source username \[manager]?, Source filename \[]? Cisco\_startup-config.cfg, Password: \*\*\*\*\*\*\*\*)          |
| Copy TFTP Config File                         | `ProVision# copy tftp config config3 10.0.100.111 config3.cfg`                  | `<Comware>tftp 10.0.100.111 get comware_main3.cfg comware_main3.cfg`               | `Cisco#copy tftp://10.0.100.111/Cisco_config2.cfg flash:Cisco_config2.cfg`                                                                                                                            |
| Copy SFTP Config File                         | `ProVision# copy sftp config config3 10.0.100.111 config3.cfg`                  | (Credentials prompt)                                                               | `Cisco#copy scp: flash:` (Address or name of remote host \[]? 10.0.100.111, Source username \[manager]?, Source filename \[]? Cisco\_config2.cfg, Password: \*\*\*\*\*\*\*\*)                         |
| Show Configuration Files                      | `ProVision# show config files`                                                  | `<Comware>dir`                                                                     | `Cisco#show flash` / `Cisco#show boot`                                                                                                                                                                |
| Set Default Startup Configuration             | `ProVision# startup-default config config1`                                     | `<Comware>startup saved-configuration comware_main.cfg`                            | `ProVision# boot system flash primary config config1`                                                                                                                                                 |

**Logging Configuration**

| Context                  | ProVision                                 | Comware                                                | Cisco                                                      |
| ------------------------ | ----------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------- |
| Set Log Host             | `ProVision(config)# logging 10.0.100.111` | `[Comware]info-center loghost 10.0.100.111`            | `Cisco(config)# logging 10.0.100.111`                      |
| Set Log Host Facility    | `ProVision(config)# logging facility ?`   | `[Comware]info-center loghost 10.0.100.111 facility ?` | `Cisco(config)# logging facility ?`                        |
| Set Log Host Severity    | `ProVision(config)# logging severity ?`   |                                                        | `Cisco(config)# logging console ?`                         |
| Set Timestamp Format     |                                           | `[Comware]info-center timestamp loghost date`          | `Cisco(config)# service timestamps log datetime localtime` |
| Show Logging Information | `ProVision# show logging ?`               | `[Comware]display logbuffer ?`                         | `Cisco#show logging ?`                                     |

**NTP Configuration**

| Context                  | ProVision                                      | Comware5                                                                                           | Cisco                                                                               |
| ------------------------ | ---------------------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Set NTP Server           | `ProVision(config)# ntp server 10.0.100.251`   | `[Comware5]ntp-service unicast-server 10.0.100.251`                                                | `Cisco(config)#ntp server 10.0.100.251`                                             |
| Enable NTP               | `ProVision(config)# ntp enable`                | `[Comware5]ntp-service enable`                                                                     |                                                                                     |
| Set Time Sync Mode       | `ProVision(config)# timesync ntp`              |                                                                                                    |                                                                                     |
| Show NTP Associations    | `ProVision(config)# show ntp associations`     | `[Comware5]display ntp-service sessions`                                                           | `Cisco#show ntp associations`                                                       |
| Set Timezone             | `ProVision(config)# clock timezone us central` | `[Comware5] clock timezone US-Central minus 06:00:00`                                              | `Cisco(config)#clock timezone US-Cent -6`                                           |
| Set Daylight Saving Time | `ProVision(config)# clock summer-time`         | `[Comware5] clock summer-time US-Central one-off 02:00:00 03/08/2015 02:00:00 11/01/2015 01:00:00` | `Cisco(config)#clock summer-time US-Cent date mar 8 2015 02:00 nov 1 2015 02:00 60` |
| Show Current Time        | `ProVision# show time`                         | `[Comware5]display clock`                                                                          | `Cisco#show clock`                                                                  |
| Show NTP Status          | `ProVision# show ntp status`                   | `[Comware5]display ntp-service status`                                                             | `Cisco#show ntp status`                                                             |

| Context                                   | ProVision                                                                           | Comware                                                                                                         | Cisco                                                            |
| ----------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Set SNMP Version 1/2c (Default)           | `[snmp v1/v2c is default version]`                                                  | `[Comware]snmp-agent sys-info version v1 v2c`                                                                   | _No specific command for version setting_                        |
| Configure SNMP Host for Traps             | `ProVision(config)# snmp-server host 10.0.111.210 community private trap-level all` | `[Comware]snmp-agent target-host trap address udp-domain 10.0.111.210 udp-port 161 params securityname private` | `Cisco(config)#snmp-server host 10.0.111.210 version 2c private` |
| Set SNMP Community (Read-Only)            | `ProVision(config)# snmp-server community public operator restricted`               | `[Comware]snmp-agent community read public`                                                                     | `Cisco(config)#snmp-server community public ro`                  |
| Set SNMP Community (Read-Write)           | `ProVision(config)# snmp-server community private manager unrestricted`             | `[Comware]snmp-agent community write private`                                                                   | `Cisco(config)#snmp-server community private rw`                 |
| Set SNMP System Location                  | `ProVision(config)# snmp-server location Lab`                                       | `[Comware]snmp-agent sys-info location Lab`                                                                     | `Cisco(config)#snmp-server location Lab`                         |
| Set SNMP System Contact                   | `ProVision(config)# snmp-server contact Lab_Engr`                                   | `[Comware]snmp-agent sys-info contact Lab_Engr`                                                                 | `Cisco(config)#snmp-server contact Lab_Engr`                     |
| Disable SNMP System Information Version 3 | `[Comware]undo snmp-agent sys-info version v3`                                      | `[Comware]snmp-agent sys-info version v1 v2c`                                                                   | _No specific command for version setting_                        |
| Enable SNMP                               | `ProVision(config)# snmp-server enable`                                             | `[Comware]snmp-agent trap enable`                                                                               | `Cisco(config)#snmp-server enable traps`                         |
| Show SNMP Configuration                   | `ProVision# show snmp-server`                                                       | `[Comware]display snmp-agent sys-info` `[Comware]display snmp-agent community`                                  | `Cisco#show snmp` `Cisco#show snmp host`                         |

**SNMP Version 3 Configuration**

| Context                      | ProVision                                                                 | Comware                                                                                                       | Cisco                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Set SNMP Version 3 (Default) | `[snmp v3 is default version]`                                            | _No specific command for default version_                                                                     | _No specific command for default version_                                                |
| Enable SNMPv3                | `ProVision(config)# snmpv3 enable`                                        | `[Comware]snmp-agent group v3 <name> privacy`                                                                 | _No specific command for version setting_                                                |
| Create SNMPv3 User           | `ProVision(config)# snmpv3 user test auth md5 password priv des password` | `[Comware]snmp-agent usm-user v3 test managerpriv authentication-mode md5 password privacy-mode des password` | `Cisco(config)#snmp-server user test managerpriv v3 auth md5 password priv des password` |
| Create SNMPv3 Group          | `ProVision(config)# snmpv3 group managerpriv user test sec-model ver3`    | _No specific command for creating SNMPv3 group_                                                               | _No specific command for creating SNMPv3 group_                                          |
| Set SNMPv3 Target Address    | `ProVision(config)# snmpv3 targetaddress NMS params all 10.0.111.210`     | `[Comware]snmp-agent target-host trap address udp-domain 10.0.111.210 params securityname test v3 privacy`    | `Cisco(config)#snmp-server host 10.0.111.210 version 3 priv test`                        |
| Set SNMPv3 System Location   | `ProVision(config)# snmp-server location Lab`                             | `[Comware]snmp-agent sys-info location Lab`                                                                   | `Cisco(config)#snmp-server location Lab`                                                 |
| Set SNMPv3 System Contact    | `ProVision(config)# snmp-server contact Lab_Engr`                         | `[Comware]snmp-agent sys-info contact Lab_Engr`                                                               | `Cisco(config)#snmp-server contact Lab_Engr`                                             |
| Show SNMPv3 Enable Status    | `ProVision# show snmpv3 enable`                                           | _No specific command for showing SNMPv3 enable status_                                                        | _No specific command for showing SNMPv3 enable status_                                   |
| Show SNMPv3 Target Address   | `ProVision# show snmpv3 targetaddress`                                    | `[Comware]display snmp-agent sys-info`                                                                        | `Cisco#show snmp host`                                                                   |
| Show SNMPv3 User             | `ProVision# show snmpv3 user`                                             | `[Comware]display snmp-agent usm-user`                                                                        | `Cisco#show snmp user`                                                                   |
| Show SNMPv3 Group            | `ProVision# show snmpv3 group`                                            | `[Comware]display snmp-agent group`                                                                           | `Cisco#show snmp group`                                                                  |

**Telnet Configuration**

| Context                                | ProVision                                                                                                         | Comware                                                                                                           | Cisco                                                          |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Telnet Default Status                  | Enabled by default                                                                                                | Enabled by default                                                                                                | Disabled by default                                            |
| Enable Telnet Server                   | `ProVision(config)# telnet server enable`                                                                         | `[Comware5]telnet server enable`                                                                                  | Not applicable                                                 |
| Configure Local User for Telnet        | `ProVision(config)# local-user <name>` `ProVision(config-luser-manager)# service-type telnet`                     | `[Comware5]local-user <name>` `[Comware5-luser-manager]service-type telnet`                                       | Not applicable                                                 |
| Configure VTY Lines                    | `ProVision(config)# user-interface vty 0 15` `ProVision(config-ui-vty0-15)# authentication-mode scheme`           | `[Comware5]user-interface vty 0 15` `[Comware5-ui-vty0-15]authentication-mode scheme`                             | `Cisco(config)#line vty 0 15` `Cisco(config-line)#login local` |
| Configure Password for VTY Lines       | `ProVision(config-ui-vty0-15)# set authentication password simple password`                                       | `[Comware5-ui-vty0-15]set authentication password simple password`                                                | `Cisco(config-line)#password 0 password`                       |
| Configure Authentication for VTY Lines | `[Comware7]user-interface vty 0 63` `[Comware7-ui-vty0-63]authentication-mode scheme`                             | `[Comware7]user-interface vty 0 63` `[Comware7-ui-vty0-63]authentication-mode scheme`                             | Not applicable                                                 |
| Configure User Role and Password       | `[Comware7-ui-vty0-63]user-role network-admin` `[Comware7-ui-vty0-63]set authentication password simple password` | `[Comware7-ui-vty0-63]user-role network-admin` `[Comware7-ui-vty0-63]set authentication password simple password` | Not applicable                                                 |
| Show Telnet Sessions                   | `ProVision# show telnet`                                                                                          | `[Comware]display users`                                                                                          | `Cisco#show users`                                             |

| Context                                    | ProVision                                                          | Comware5                                                                                                                                                                                                                                 | Cisco                                                                                               |
| ------------------------------------------ | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Configure RADIUS Scheme                    | `[Comware5]radius scheme radius-auth`                              | `[Comware7]radius scheme radius-auth`                                                                                                                                                                                                    | `Cisco(config)#radius server radius-auth`                                                           |
| Configure RADIUS Server                    | `ProVision(config)#radius-server host 10.0.100.111 key password`   | `[Comware5-radius-radius-auth]primary authentication 10.0.100.111 key simple password` `[Comware5-radius-radius-auth]primary accounting 10.0.100.111 key simple password` `[Comware5-radius-radius-auth]user-name-format without-domain` | `Cisco(config)#radius-server host 10.0.100.111 auth-port 1812 acct-port 1813 key password`          |
| Configure AAA Authentication               | `ProVision(config)#aaa authentication console login radius local`  | `Cisco(config)#aaa authentication login default group radius local`                                                                                                                                                                      | `Cisco(config)#line vty 0 15` `Cisco(config-line)#login authentication default`                     |
| Configure AAA Enable Authentication        | `ProVision(config)#aaa authentication console enable radius local` | `Cisco(config)#aaa authentication enable default group radius local`                                                                                                                                                                     | `Cisco(config)#line vty 0 15` `Cisco(config-line)#enable authentication default group radius local` |
| Configure AAA Telnet Authentication        | `ProVision(config)#aaa authentication telnet login radius none`    | `Cisco(config)#aaa authentication login default group radius`                                                                                                                                                                            | `Cisco(config)#line vty 0 15` `Cisco(config-line)#login authentication default`                     |
| Configure AAA Telnet Enable Authentication | `ProVision(config)#aaa authentication telnet enable radius none`   | `Cisco(config)#aaa authentication enable default group radius`                                                                                                                                                                           | `Cisco(config)#line vty 0 15` `Cisco(config-line)#enable authentication default group radius`       |
| Configure AAA SSH Authentication           | `ProVision(config)#aaa authentication ssh login radius none`       | `Cisco(config)#aaa authentication login default group radius`                                                                                                                                                                            | `Cisco(config)#line vty 0 15` `Cisco(config-line)#login authentication default`                     |
| Configure AAA SSH Enable Authentication    | `ProVision(config)#aaa authentication ssh enable radius none`      | `Cisco(config)#aaa authentication enable default group radius`                                                                                                                                                                           | `Cisco(config)#line vty 0 15` `Cisco(config-line)#enable authentication default group radius`       |
| Configure AAA Web Authentication           | `ProVision(config)#aaa authentication web login radius none`       | Not applicable                                                                                                                                                                                                                           | Not applicable                                                                                      |
| Configure AAA Web Enable Authentication    | `ProVision(config)#aaa authentication web enable radius none`      | Not applicable                                                                                                                                                                                                                           | Not applicable                                                                                      |
| Show RADIUS Configuration                  | `ProVision#show radius`                                            | `[Comware5]display radius scheme`                                                                                                                                                                                                        | `Cisco#show aaa servers`                                                                            |

**Additional AAA Configuration for Privilege Mode**

| Context                               | ProVision                                                   | Comware                                             | Cisco                                     |
| ------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------- |
| **Configure AAA for Privilege Mode**  | `ProVision(config)#aaa authentication login privilege-mode` | No additional Comware RADIUS configuration required | `Cisco(config)#aaa authorization console` |
| **Configure AAA Exec Authorization**  | `Cisco(config)#aaa authorization exec default group radius` |                                                     |                                           |
| **Show Authentication Configuration** | `ProVision#show authentication`                             |                                                     |                                           |

**Authorization Commands Configuration**

| Context                                                                                    | ProVision                                             | Comware5                                                                        | Cisco                    |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------ |
| **Configure Authorization Commands (Requires special configuration on the RADIUS server)** | `ProVision(config)#aaa authorization commands radius` | `[Comware5]user-interface vty 0 15``[Comware5-ui-vty0-15]command authorization` | Not an available feature |
|                                                                                            |                                                       |                                                                                 |                          |
| **Show Authorization Configuration**                                                       | `ProVision#show authorization`                        |                                                                                 |                          |

**AAA Accounting Configuration**

| Context                                               | ProVision                                                    | Comware | Cisco                                                                  |
| ----------------------------------------------------- | ------------------------------------------------------------ | ------- | ---------------------------------------------------------------------- |
| **Configure AAA Accounting for Exec Commands**        | `ProVision(config)#aaa accounting exec start-stop radius`    |         | `Cisco(config)#aaa accounting exec default start-stop group radius`    |
| **Configure AAA Accounting for Network Commands**     | `ProVision(config)#aaa accounting network start-stop radius` |         | `Cisco(config)#aaa accounting network default start-stop group radius` |
| **Configure AAA Accounting for System Commands**      | `ProVision(config)#aaa accounting system start-stop radius`  |         | `Cisco(config)#aaa accounting system default start-stop group radius`  |
| **Configure AAA Accounting for Commands (Stop-Only)** | `ProVision(config)#aaa accounting commands stop-only radius` |         |                                                                        |
| **Show AAA Accounting Configuration**                 | `ProVision#show radius accounting`                           |         | `Cisco#show aaa user all``ProVision#show accounting sessions`          |

**TACACS Configuration**

| Context                                             | ProVision                                                          | Comware                                                                                                                                                                                                                                    | Cisco                                                                                                                                                                                                                                      |
| --------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Configure HWTACACS Scheme**                       | `ProVision(config)#hwtacacs scheme tacacs-auth`                    | `Comware5-hwtacacs-tacacs-auth` `primary authentication 10.0.100.111 key simple password` `primary authorization 10.0.100.111 key simple password` `primary accounting 10.0.100.111 key simple password` `user-name-format without-domain` | `Comware7-hwtacacs-tacacs-auth` `primary authentication 10.0.100.111 key simple password` `primary authorization 10.0.100.111 key simple password` `primary accounting 10.0.100.111 key simple password` `user-name-format without-domain` |
| **Configure TACACS Server**                         | `ProVision(config)#tacacs-server host 10.0.100.111 key password`   | `Comware5-hwtacacs-tacacs-auth` `tacacs-server host 10.0.100.111 key password`                                                                                                                                                             | `Comware7-hwtacacs-tacacs-auth` `tacacs-server host 10.0.100.111 key password`                                                                                                                                                             |
| **Configure AAA Authentication for Console Login**  | `ProVision(config)#aaa authentication console login tacacs local`  | `Cisco(config)#aaa authentication login default group tacacs+ local`                                                                                                                                                                       |                                                                                                                                                                                                                                            |
| **Configure AAA Authentication for Console Enable** | `ProVision(config)#aaa authentication console enable tacacs local` | `Cisco(config)#aaa authentication enable default group tacacs+ local`                                                                                                                                                                      |                                                                                                                                                                                                                                            |
| **Configure AAA Authentication for Telnet Login**   | `ProVision(config)#aaa authentication telnet login tacacs none`    | `Cisco(config)#aaa authentication login default group tacacs+`                                                                                                                                                                             |                                                                                                                                                                                                                                            |
| **Configure AAA Authentication for Telnet Enable**  | `ProVision(config)#aaa authentication telnet enable tacacs none`   | `Cisco(config)#aaa authentication enable default group tacacs+`                                                                                                                                                                            |                                                                                                                                                                                                                                            |
| **Configure AAA Authentication for SSH Login**      | `ProVision(config)#aaa authentication ssh login tacacs none`       | `Cisco(config)#aaa authentication login default group tacacs+`                                                                                                                                                                             |                                                                                                                                                                                                                                            |
| **Configure AAA Authentication for SSH Enable**     | `ProVision(config)#aaa authentication ssh enable tacacs none`      | `Cisco(config)#aaa authentication enable default group tacacs+`                                                                                                                                                                            |                                                                                                                                                                                                                                            |
| **Show TACACS Configuration**                       | `ProVision#show tacacs`                                            | `Comware5#display hwtacacs`                                                                                                                                                                                                                | `Comware7#display hwtacacs`                                                                                                                                                                                                                |
| **Show AAA Authentication Configuration**           | `ProVision#show authentication`                                    |                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                            |

**AAA Accounting Configuration for TACACS+**

| Context                                                         | ProVision                                                                          | Comware                                                                    | Cisco                     |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------- |
| **Configure AAA Accounting for Exec Commands**                  | `Not an available feature (Basic support only; no other specific feature support)` | `Cisco(config)#aaa accounting exec default start-stop group tacacs+`       |                           |
| **Configure AAA Accounting for Network Services**               |                                                                                    | `Cisco(config)#aaa accounting network default start-stop group tacacs+`    |                           |
| **Configure AAA Accounting for System Services**                |                                                                                    | `Cisco(config)#aaa accounting system default start-stop group tacacs+`     |                           |
| **Configure AAA Accounting for Commands at Privilege Level 15** |                                                                                    | `Cisco(config)#aaa accounting commands 15 default stop-only group tacacs+` |                           |
| **Show AAA User Information**                                   |                                                                                    |                                                                            | `Cisco#show aaa user all` |

| Context                                   | ProVision                                                                                                                                  | Comware5                                                                         | Cisco                                                                                                               |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Schedule Configuration Save Job**       | `ProVision(config)# job save-config at 01:00 "copy run tftp 10.0.100.111 provision.cfg"`                                                   | `[Comware5]job save-config`                                                      | `Cisco(config)#file prompt quiet` `[Comware5-job-save-config]view monitor`                                          |
| **Schedule Configuration Save with Kron** | `Cisco(config)#kron policy-list save-config` `[Comware5-job-save-config]time 1 one-off at 02:07 command tftp 10.0.100.111 put startup.cfg` | `Cisco(config-kron-policy)#cli` `copy run tftp://10.0.100.111/cisco-startup.cfg` | `Cisco(config)#kron occurrence saveconfig at 09:30 oneshot` `Cisco(config-kron-occurrence)#policy-list save-config` |
| **Display Scheduled Jobs**                | `ProVision# show job`                                                                                                                      | `[Comware5]display job save-config`                                              | `Cisco#show kron schedule`                                                                                          |
| **Display Scheduled Kron Jobs**           |                                                                                                                                            |                                                                                  | `[Comware7]display scheduler job` `[Comware7]display scheduler schedule`                                            |

**Configuring Interface Settings**

| Context                                 | ProVision                             | Comware                                                                                | Cisco                                                        |
| --------------------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Show Interfaces Brief**               | `ProVision# show interfaces brief`    | `<Comware>display interface brief`                                                     | `Cisco#show interfaces status`                               |
| **Show Detailed Interface Information** | `ProVision# show interfaces 1`        | `<Comware>display interface g1/0/1`                                                    | `Cisco#show interfaces g1/0/1`                               |
| **Enter Interface Configuration Mode**  | `ProVision(config)# interface 1`      | `[Comware]interface g1/0/1`                                                            | `Cisco(config)#interface g1/0/1`                             |
| **Set Interface Description**           | `ProVision(eth-1)# name link-to-core` | `[Comware-GigabitEthernet1/0/1]description link-to-core`                               | `Cisco(config-if)#description link-to-core`                  |
| **Set Interface Speed and Duplex**      | `ProVision(eth-1)# speed-duplex auto` | `[Comware-GigabitEthernet1/0/1]duplex auto` `[Comware-GigabitEthernet1/0/1]speed auto` | `Cisco(config-if)#duplex auto` `Cisco(config-if)#speed auto` |
| **Disable Interface**                   | `ProVision(eth-1)# disable`           | `[Comware-GigabitEthernet1/0/1]shutdown`                                               | `Cisco(config-if)#shutdown`                                  |
| **Enable Interface**                    | `ProVision(eth-1)# enable`            | `[Comware-GigabitEthernet1/0/1]undo shutdown`                                          | `Cisco(config-if)#no shutdown`                               |

{% hint style="info" %}
The interface numbers (1, g1/0/1) and configuration details may vary based on your network setup. Always refer to the respective documentation for accurate information
{% endhint %}

**Creating and Naming VLANs**

| Context                   | ProVision                        | Comware                      | Cisco                                         |
| ------------------------- | -------------------------------- | ---------------------------- | --------------------------------------------- |
| **Create VLAN 220**       | `ProVision(config)# vlan 220`    | `[Comware]vlan 220`          | `Cisco(config)#vlan 220`                      |
| **Name VLAN as "test"**   | `ProVision(vlan-220)# name test` | `[Comware-vlan220]name test` | `Cisco(config-vlan)#name test`                |
| **Show VLAN Information** | `ProVision# show vlans`          | `[Comware]display vlan`      | `Cisco#show vlan brief` `Cisco#show vlan all` |

Certainly! Here is the information without line breaks:

**Assigning Ports or Interfaces to VLANs**

**ProVision:**

* Create VLAN 220: `ProVision(config)# vlan 220`
* Name VLAN as "test": `ProVision(vlan-220)# name test`
* Assign Ports/Interfaces:
  * `ProVision(config)# vlan 220`
  * `ProVision(vlan-220)# tagged 6`
  * `ProVision(vlan-220)# untagged 4`

**Comware:**

* Create VLAN 220: `[Comware]vlan 220`
* Name VLAN as "test": `[Comware-vlan220]name test`
* Assign Ports/Interfaces:
  * `[Comware-GigabitEthernet1/0/6]port link-type trunk`
  * `[Comware-GigabitEthernet1/0/6]port trunk permit vlan 220`
  * `[Comware-vlan220]port g1/0/4`

**Cisco:**

* Create VLAN 220: `Cisco(config)#vlan 220`
* Name VLAN as "test": `Cisco(config-vlan)#name test`
* Assign Ports/Interfaces:
  * `Cisco(config)#interface g1/0/6`
  * `Cisco(config-if)#switchport trunk encapsulation dot1q`
  * `Cisco(config-if)#switchport trunk allowed vlan 220`
  * `Cisco(config-if)#switchport mode trunk`
  * `Cisco(config-if)#switchport nonegotiate`
  * `Cisco(config)#interface g1/0/4`
  * `Cisco(config-if)#switchport access vlan 220`
  * `Cisco(config-if)#switchport mode access`

**Show VLAN Information:**

* ProVision: `ProVision# show vlans` `ProVision# show vlans 220` `ProVision# show vlans 100` `ProVision# show vlans 1`
* Comware: `[Comware]display vlan` `[Comware]display vlan 220` `[Comware]display vlan 100` `[Comware]display vlan 1`
* Cisco: `Cisco#show vlan id 220` `Cisco#show vlan id 100` `Cisco#show vlan id 1`

**Show VLAN Port/Interface Details:**

* ProVision: `ProVision# show vlans ports 6 detail` `ProVision# show vlans ports 5 detail`
* Comware: `[Comware]display interface g1/0/6` `[Comware]display interface g1/0/5`
* Cisco: `Cisco#show interfaces g1/0/6 switchport` `Cisco#show interfaces g1/0/5 switchport`

```markdown
| Command                         | Description                      |
|---------------------------------|----------------------------------|
| `ProVision# show ip`            | Display IP information for interfaces |
| `[Comware]display ip interface brief` | Display IP information for interfaces |
| `Cisco#show ip interface brief` | Display IP information for interfaces |
```

| **Configuration Task**            | **ProVision**                                         | **Comware5**                                                                                                                                    | **Cisco**                                         |
| --------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **Enable DHCP Relay on VLAN 220** | `ProVision(config)# vlan 220`                         | `[Comware5]dhcp enable`                                                                                                                         | `Cisco(config)#interface vlan 220`                |
| **Configure IP Helper Address**   | `ProVision(vlan-220)# ip helper-address 10.0.100.251` | `[Comware5]interface Vlan-interface 220``[Comware5-Vlan-interface220]dhcp select relay``[Comware5-Vlan-interface220]dhcp relay server-select 1` | `Cisco(config-if)#ip helper-address 10.0.100.251` |
| **Show IP Helper Address**        | `ProVision# show ip helper-address vlan 220`          | `[Comware5]display dhcp relay all`                                                                                                              | `Cisco#show ip interface vlan 220`                |
| **Show DHCP Relay Information**   | `ProVision# show dhcp-relay`                          | `[Comware5]display dhcp relay server-group 1`                                                                                                   | `[Comware5]display dhcp relay server-group 1`     |

| **Configuration Task**            | **Comware7**                                                                                                                                                                    |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enable DHCP Relay on VLAN 220** | `[Comware7]dhcp enable [Comware7]interface Vlan-interface 220 [Comware7-Vlan-interface220]dhcp select relay [Comware7-Vlan-interface220 dhcp relay server-address 10.0.100.251` |
| **Show DHCP Relay Information**   | `[Comware7]display dhcp relay server-address``[Comware7]display dhcp relay statistics interface Vlan-interface 220`                                                             |

| **Configuration Task**            | **ProVision**                                         | **Comware5**                                                                                                                                    | **Cisco**                                         |
| --------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **Enable DHCP Relay on VLAN 220** | `ProVision(config)# vlan 220`                         | `[Comware5]dhcp enable`                                                                                                                         | `Cisco(config)#interface vlan 220`                |
| **Configure IP Helper Address**   | `ProVision(vlan-220)# ip helper-address 10.0.100.251` | `[Comware5]interface Vlan-interface 220``[Comware5-Vlan-interface220]dhcp select relay``[Comware5-Vlan-interface220]dhcp relay server-select 1` | `Cisco(config-if)#ip helper-address 10.0.100.251` |
| **Show IP Helper Address**        | `ProVision# show ip helper-address vlan 220`          | `[Comware5]display dhcp relay all`                                                                                                              | `Cisco#show ip interface vlan 220`                |
| **Show DHCP Relay Information**   | `ProVision# show dhcp-relay`                          | `[Comware5]display dhcp relay server-group 1`                                                                                                   | `[Comware5]display dhcp relay server-group 1`     |

| **Configuration Task**            | **Comware7**                                                                                                                                                                    |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enable DHCP Relay on VLAN 220** | `[Comware7]dhcp enable [Comware7]interface Vlan-interface 220 [Comware7-Vlan-interface220]dhcp select relay [Comware7-Vlan-interface220 dhcp relay server-address 10.0.100.251` |
| **Show DHCP Relay Information**   | `[Comware7]display dhcp relay server-address``[Comware7]display dhcp relay statistics interface Vlan-interface 220`                                                             |

| **Configuration Task**            | **ProVision**                                         | **Comware5**                                                                                                                                    | **Cisco**                                         |
| --------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **Enable DHCP Relay on VLAN 220** | `ProVision(config)# vlan 220`                         | `[Comware5]dhcp enable`                                                                                                                         | `Cisco(config)#interface vlan 220`                |
| **Configure IP Helper Address**   | `ProVision(vlan-220)# ip helper-address 10.0.100.251` | `[Comware5]interface Vlan-interface 220``[Comware5-Vlan-interface220]dhcp select relay``[Comware5-Vlan-interface220]dhcp relay server-select 1` | `Cisco(config-if)#ip helper-address 10.0.100.251` |
| **Show IP Helper Address**        | `ProVision# show ip helper-address vlan 220`          | `[Comware5]display dhcp relay all`                                                                                                              | `Cisco#show ip interface vlan 220`                |
| **Show DHCP Relay Information**   | `ProVision# show dhcp-relay`                          | `[Comware5]display dhcp relay server-group 1`                                                                                                   | `[Comware5]display dhcp relay server-group 1`     |

| **Configuration Task**            | **Comware7**                                                                                                                                                                       |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enable DHCP Relay on VLAN 220** | `[Comware7]dhcp enable``[Comware7]interface Vlan-interface 220``[Comware7-Vlan-interface220]dhcp select relay``[Comware7-Vlan-interface220]dhcp relay server-address 10.0.100.251` |
| **Show DHCP Relay Information**   | `[Comware7]display dhcp relay server-address``[Comware7]display dhcp relay statistics interface Vlan-interface 220`                                                                |

| **Configuration Task**                 | **ProVision**                               | **Comware**                                                                                                                  | **Cisco**                                                                                                   |
| -------------------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Create Trunk Port/Link Aggregation** | `ProVision(config)# trunk 19-20 trk1 trunk` | `[Comware]interface Bridge-Aggregation 1``[Comware-Bridge-Aggregation1]description Trunk-link-to-ProVision`                  | `Cisco(config)#interface port-channel 1`                                                                    |
| **Assign VLANs to Trunk**              | `ProVision(config)# vlan 220 tagged trk1`   | `[Comware-Bridge-Aggregation1]port link-type trunk``[Comware-Bridge-Aggregation1]port trunk permit vlan 220`                 | `Cisco(config-if)#switchport trunk encapsulation dot1q``Cisco(config-if)#switchport trunk allowed vlan 220` |
| **Configure Individual Ports**         | `ProVision(config)# vlan 220 tagged trk1`   | `[Comware-GigabitEthernet1/0/23]port link-aggregation group 1``[Comware-GigabitEthernet1/0/24]port link-aggregation group 1` | `Cisco(config)#interface range g1/0/23 - 24``Cisco(config-if-range)#channel-group 1 mode on`                |
| **Show Trunk/Link Aggregation Status** | `ProVision# show trunks`                    | `[Comware]display link-aggregation summary``[Comware]display link-aggregation verbose`                                       | `Cisco#show etherchannel 1 summary`                                                                         |
| **Show VLAN Configuration**            | `ProVision# show vlans 220`                 | `[Comware]display vlan 220`                                                                                                  | `Cisco#show vlan name test`                                                                                 |
| **Show VLAN on Trunk/Port**            | `ProVision# show vlans ports trk1 detail`   | `[Comware]display vlan 220`                                                                                                  | `Cisco#show interfaces etherchannel`                                                                        |

| **Configuration Task**            | **ProVision**                                                                                            | **Comware**                                                                   | **Cisco**                                       |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------- |
| **Enable RIP**                    | `ProVision(config)# router rip``ProVision(rip)# enable`                                                  | `[Comware]rip 1`                                                              | `Cisco(config)#router rip`                      |
| **Specify VLAN for RIP**          | `ProVision(rip)# vlan 220 ip rip`                                                                        | `[Comware-rip-1]network 10.1.220.0`                                           | `Cisco(config-router)#network 10.1.220.0`       |
| **Specify RIP Version**           | `ProVision(rip)# version 2`                                                                              | `[Comware-rip-1]version 2`                                                    | `Cisco(config-router)#version 2`                |
| **Redistribute Connected Routes** | `ProVision(rip)# redistribute connected`                                                                 | `[Comware-rip-1]import-route direct`                                          | `Cisco(config-router)#redistribute connected`   |
| **Show RIP Configuration**        | `ProVision# show ip rip``ProVision# show ip rip interface vlan 220``ProVision# show ip rip redistribute` | `[Comware]display rip 1``[Comware]display rip 1 interface Vlan-interface 220` | `Cisco#show ip rip database``Cisco#show ip rip` |

**\*\* Single Area OSPFv2 Configuration\*\***

| **Configuration Task**     | **ProVision**                               | **Comware**                                                 | **Cisco**                                                  |
| -------------------------- | ------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------- |
| **Enable OSPF**            | `ProVision(config)# router ospf`            | `[Comware]ospf 1`                                           | `Cisco(config)#router ospf 1`                              |
| **Set Router ID**          | `ProVision(config)# ip router-id 10.0.0.21` | `[Comware-ospf-1]router-id 10.0.0.31`                       | `Cisco(config-router)#router-id 10.0.0.41`                 |
| **Specify Area 0**         | `ProVision(ospf)# area 0`                   | `[Comware-ospf-1-area-0.0.0.0]area 0`                       | `Cisco(config-router)#network 10.1.220.0 0.0.0.255 area 0` |
| **Configure OSPF on VLAN** | `ProVision(vlan-220)# ip ospf area 0`       | `[Comware-ospf-1-area-0.0.0.0]network 10.1.220.0 0.0.0.255` | `Cisco(config-router)#network 10.1.220.0 0.0.0.255 area 0` |
| **Redistribute Connected** | `ProVision(ospf)# redistribute connected`   | `[Comware-ospf-1]import-route direct`                       | `Cisco(config-router)#redistribute connected`              |

**Multiple Areas OSPFv2 Configuration**

| **Configuration Task**         | **ProVision**                         | **Comware**                                                 | **Cisco**                                                  |
| ------------------------------ | ------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------- |
| **Enable OSPF**                | `ProVision(config)# router ospf`      | `[Comware]ospf 1`                                           | `Cisco(config)#router ospf 1`                              |
| **Specify Area 1**             | `ProVision(ospf)# area 1`             | `[Comware-ospf-1]area 1`                                    | `Cisco(config-router)#network 10.1.100.0 0.0.0.255 area 1` |
| **Configure OSPF on VLAN 100** | `ProVision(vlan-100)# ip ospf area 1` | `[Comware-ospf-1-area-0.0.0.1]network 10.1.100.0 0.0.0.255` | `Cisco(config-router)#network 10.1.100.0 0.0.0.255 area 1` |
| **Specify Area 2**             | `ProVision(ospf)# area 2`             | `[Comware-ospf-1]area 2`                                    | `Cisco(config-router)#network 10.1.230.0 0.0.0.255 area 2` |
| **Configure OSPF on VLAN 230** | `ProVision(vlan-230)# ip ospf area 2` | `[Comware-ospf-1-area-0.0.0.2]network 10.1.230.0 0.0.0.255` | `Cisco(config-router)#network 10.1.230.0 0.0.0.255 area 2` |

**Show/Display OSPF Commands**

| **Show/Display OSPF Command**     | **ProVision**                        | **Comware**                       | **Cisco**                            |
| --------------------------------- | ------------------------------------ | --------------------------------- | ------------------------------------ |
| **Show OSPF Interfaces**          | `ProVision# show ip ospf interface`  | `[Comware]display ospf interface` | `Cisco#show ip ospf interface brief` |
| **Show OSPF Neighbors**           | `ProVision# show ip ospf neighbor`   | `[Comware]display ospf peer`      | `Cisco#show ip ospf neighbor`        |
| **Show OSPF Link-State Database** | `ProVision# show ip ospf link-state` | `[Comware]display ospf lsdb`      | `Cisco#show ip ospf database`        |

```bash
[Comware]acl number 2000
[Comware-acl-basic-2000]rule permit source 10.0.100.111 0.0.0.0
[Comware]acl number 2001 name std_acl
[Comware-acl-basic-2001-std_acl]rule permit source 10.0.100.111 0
[Comware]interface Vlan-interface 220
[Comware-Vlan-interface220]packet-filter 2000 inbound
[Comware]interface Vlan-interface 100
[Comware-Vlan-interface100]packet-filter 2001 inbound
```

**Cisco:**

```bash
Cisco(config)#ip access-list standard 1
Cisco(config-std-nacl)#permit 10.0.100.111 0.0.0.0
Cisco(config)#interface vlan 220
Cisco(config-if)#ip access-group 1 in
Cisco(config)#interface vlan 100
Cisco(config-if)#ip access-group std_acl in
```

**Extended or Advanced ACL**

**ProVision:**

```bash
ProVision(config)# ip access-list extended 100
ProVision(config-ext-nacl)# deny ip 10.1.220.0 0.0.0.255 10.0.100.111 0.0.0.0
ProVision(config-ext-nacl)# permit ip any any
ProVision(config)# ip access-list extended ext_acl
ProVision(config-ext-nacl)# deny ip 10.1.100.0/24 10.0.100.111/32
ProVision(config-ext-nacl)# permit ip any any
vlan 220
ProVision(config-ext-nacl)# quit
ProVision(vlan-220)# ip access-group 100 in
```

**Comware:**

```bash
[Comware]acl number 3000
[Comware-acl-adv-3000]rule deny ip source 10.1.220.0 0.0.0.255 destination 10.0.100.111 0
[Comware]acl number 3001 name ext_acl
[Comware-acl-adv-3001-ext_acl]rule deny ip source 10.1.100.0 0.0.0.255 destination 10.0.100.111 0
[Comware]interface Vlan-interface 220
[Comware-Vlan-interface220]packet-filter 3000 inbound
[Comware]interface Vlan-interface 100
[Comware-Vlan-interface100]packet-filter 3001 inbound
```

**Cisco:**

```bash
Cisco(config)#ip access-list extended 100
Cisco(config-ext-nacl)#deny ip 10.1.220.0 0.0.0.255 10.0.100.111 0.0.0.0
Cisco(config-ext-nacl)#permit ip any any
Cisco(config)#interface vlan 220
Cisco(config-if)#ip access-group 100 in
Cisco(config)#vlan 100
Cisco(config-if)#interface vlan 100
Cisco(config-if)#ip access-group ext_acl in
```

**QoS**

**ProVision:**

```bash
ProVision(config)# qos type-of-service diff-services
ProVision(config)# interface 5
ProVision(eth-5)# qos priority 6
ProVision(config)# vlan 230
ProVision(vlan-230)# qos priority 6
```

**Comware:**

```bash
[Comware]interface GigabitEthernet1/0/5
[Comware-GigabitEthernet1/0/5]qos trust dscp
[Comware]interface GigabitEthernet1/0/5
[Comware-GigabitEthernet1/0/5]qos priority 6
[Comware]traffic classifier any
[Comware-classifier-any]if-match any
[Comware]traffic behavior pri6
[Comware-behavior-pri6]remark dot1p 6
[Comware-behavior-pri6]accounting
[Comware]qos policy any-pri6
[Comware-qospolicy-any-pri6]classifier any behavior pri6
[Comware]qos vlan-policy any-pri6 vlan 230 inbound
```

**Cisco:**

```bash
Cisco(config)#mls qos
Cisco(config-if)#mls qos trust dscp
Cisco(config)#mls qos map dscp-cos 0 8 16 24 32 40 48 56 to 0
Cisco(config)#mls qos cos 6
Cisco(config)#interface vlan 230
Cisco(config-if)#mls qos cos 6
Cisco#show mls qos
```

**Rate Limiting**

**ProVision:**

```bash
ProVision(config)# interface 7
ProVision(eth-7)# rate-limit all in percent 10
ProVision(config)# interface 8
ProVision(eth-8)# rate-limit all out kbps 10000
```

**Comware5:**

```bash
[Comware5]interface GigabitEthernet1/0/8
[Comware5-GigabitEthernet1/0/8]qos lr outbound cir 10048
[Comware5]interface GigabitEthernet1/0/7
[Comware5-GigabitEthernet1/0/7]qos lr inbound cir 10048
```

**Cisco:**

```bash
Cisco(config)#ip access-list extended 130
Cisco(config-ext-nacl)#permit ip any any
Cisco(config)#class-map all_traffic
Cisco(config-cmap)#match access-group 130
Cisco(config)#policy-map rate_limit
Cisco(config-pmap)#class all_traffic
Cisco(config-pmap-c)#police 10000000 8000 exceed-action drop
Cisco(config)#interface g1/0/7
Cisco(config-if)#service-policy input rate_limit
Cisco(config-if)#srr-queue bandwidth limit 10
Cisco(config)#interface g1/0/8
Cisco(config-if)#service-policy output rate_limit
```

**PIM Sparse**

**ProVision:**

```bash
ProVision(config)# ip multicast-routing
ProVision(config)# router pim
ProVision(pim)# enable
ProVision(pim)# vlan 220
ProVision(vlan-220)# ip pim-sparse
ProVision(pim)# rp-address 10.1.220.1
ProVision(pim)# rp-candidate source-ip-vlan 220
ProVision(pim)# bsr-candidate source-ip-vlan 220
ProVision# show ip pim
ProVision# show ip mroute
```

**Comware5:**

```bash
[Comware5]multicast routing-enable
[Comware5]interface Vlan-interface 220
[Comware5-Vlan-interface220]pim sm
[Comware5-Vlan-interface220]pim
[Comware5-pim]static-rp 10.1.220.1
[Comware5-pim]c-rp Vlan-interface 220
[Comware5-pim]c-bsr Vlan-interface 220
[Comware5]display pim
[Comware5]display multicast routing-table
```

**Cisco:**

```bash
Cisco(config)#ip multicast-routing distributed
Cisco(config)#interface vlan 220
Cisco(config-if)#ip pim sparse-mode
Cisco(config-if)#exit
Cisco(config)#ip pim rp-address 10.1.220.1
Cisco(config)#ip pim rp-candidate vlan 220
Cisco(config)#ip pim bsr-candidate vlan 220
Cisco#show ip pim
Cisco#show ip mroute
```

**Comware7:**

```bash
[Comware7]multicast routing
[Comware7]interface Vlan-interface 220
[Comware7-Vlan-interface220]pim sm
[Comware7-Vlan-interface220]pim
[Comware7-pim]static-rp 10.1.220.1
[Comware7-pim]c-rp 10.1.220.1
[Comware7-pim]c-bsr 10.1.220.1
[Comware7]display pim
[Comware7]display multicast routing-table
```

**DHCP Snooping**

**ProVision:**

```bash
ProVision(config)# dhcp-snooping
ProVision(config)# dhcp-snooping authorized-server 10.0.100.251
ProVision(config)# dhcp-snooping database file tftp://10.0.100.111/ProVision_dhcp.txt
ProVision(config)# dhcp-snooping vlan 220
ProVision(config)# dhcp-snooping trust 1
ProVision# show dhcp-snooping
ProVision# show dhcp-snooping stats
```

**Comware5:**

```bash
[Comware5]dhcp-snooping
[Comware5]dhcp-snooping binding database filename Comware5_dhcp.txt
[Comware5]interface GigabitEthernet1/0/6
[Comware5-GigabitEthernet1/0/6]dhcp-snooping trust
[Comware5]display dhcp-snooping
[Comware5]display dhcp-snooping trust
[Comware5]display dhcp-snooping binding database
[Comware5]display dhcp-snooping packet statistics
```

**Cisco:**

```bash
Cisco(config)#ip dhcp snooping
Cisco(config)#ip dhcp snooping authorized-server 10.0.100.111
Cisco(config)#ip dhcp snooping database tftp://10.0.100.111/Cisco_dhcp.txt
Cisco(config)#ip dhcp snooping vlan 220
Cisco(config)#interface g1/0/6
Cisco(config-if)#ip dhcp snooping trust
Cisco#show ip dhcp snooping
Cisco#show ip dhcp snooping database
Cisco#show ip dhcp snooping statistics detail
```

**Comware7:**

```bash
[Comware7]dhcp snooping enable
[Comware7]dhcp snooping binding database filename url tftp://10.0.100.111/Comware7_dhcp.txt
[Comware7]interface GigabitEthernet1/0/6
[Comware7-GigabitEthernet1/0/6]dhcp snooping trust
[Comware7]interface GigabitEthernet1/0/4
[Comware7-GigabitEthernet1/0/4]dhcp snooping binding record
[Comware7]display dhcp snooping binding
[Comware7]display dhcp snooping trust
[Comware7]display dhcp snooping binding database
[Comware7]display dhcp snooping packet statistics
```

**DHCP Snooping and ARP Protect**

**ProVision:**

```bash
ProVision(config)# dhcp-snooping
ProVision(config)# arp-protect
ProVision(config)# arp-protect vlan 220
ProVision(config)# arp-protect trust 1
ProVision# show arp-protect
```

**Comware5:**

```bash
[Comware5]dhcp-snooping
[Comware5]interface GigabitEthernet1/0/6
[Comware5-GigabitEthernet1/0/6]arp detection trust
[Comware5]vlan 220
[Comware5-vlan220]arp detection enable
[Comware5]display arp detection
[Comware5]display arp detection statistics
```

**Cisco:**

```bash
Cisco(config)#ip dhcp snooping
Cisco(config)#ip arp inspection vlan 220
Cisco(config)#ip arp inspection trust
Cisco#show ip arp inspection
Cisco#show ip arp inspection interfaces
```

**Comware7:**

```bash
[Comware7] dhcp snooping enable
[Comware7]interface GigabitEthernet1/0/6
[Comware7-GigabitEthernet1/0/6]arp detection trust
[Comware7]vlan 220
[Comware7-vlan220]arp detection enable
[Comware7]display arp detection
[Comware7]display arp detection statistics
```

**Web or Portal Authentication**

**ProVision:**

```bash
ProVision(config)# radius-server host 10.0.100.111 key password
[Comware5]radius scheme <radius-auth>
[Comware5-radius-radius-auth]primary authentication 10.0.100.111 1812
[Comware5-radius-radius-auth]primary accounting 10.0.100.111 1813
[Comware5-radius-radius-auth]key authentication password
[Comware5-radius-radius-auth]user-name-format without-domain
[Comware5-radius-radius-auth]server-type extended
ProVision(config)# aaa port-access web-based 18
[Comware5]domain web-auth
[Comware5-isp-web-auth]authentication portal radius-scheme radius-auth
[Comware5-isp-web-auth]authorization portal radius-scheme radius-auth
[Comware5-isp-web-auth]accounting portal radius-scheme radius-auth
[Comware5-isp-web-auth]authorization portal radius-scheme radius-auth
ProVision(config)# aaa port-access web-based 18 unauth-vid 99
ProVision(config)# aaa port-access web-based 18 client-limit 5
ProVision(config)# ip device tracking
ProVision(config)# ip admission name web-auth-rule1 proxy http
ProVision(config)# ip admission auth-proxy-banner http
[Comware5] interface LoopBack12
[Comware5-LoopBack12]ip address 1.1.1.1 255.255.255.255
ProVision(config)#fallback profile fallback1
[Comware5]interface g1/0/18
[Comware5-GigabitEthernet1/0/18]port link-type hybrid
[Comware5-GigabitEthernet1/0/18]mac-vlan enable
[Comware5-GigabitEthernet1/0/18]portal local-server enable
[Comware5-GigabitEthernet1/0/18]portal domain web-auth
[Comware5-GigabitEthernet1/0/18]stp edged-port enable
ProVision(config-if)#dot1x pae authenticator
ProVision(config-if)#authentication fallback fallback1
ProVision(config-if)#authentication order webauth
ProVision(config-if)#authentication port-control auto
ProVision(config-if)#ip access-group web-auth-policy1 in
ProVision(config-if)#ip admission web-auth-rule1
ProVision(config-if)#switchport mode access
ProVision(config-if)#switchport access vlan 220
ProVision(config-if)#authentication auth-fail vlan 99
ProVision# show port-access web-based
[Comware5]display portal user all
ProVision# show port-access web-based clients
[Comware5]display connection access-type portal
[Comware5]display connection ucibindex 3
ProVision# show port-access web-based config 18
[Comware5]display portal connection statistics all
```

**Cisco:**

```bash
Cisco(config)#radius-server host 10.0.100.111 auth-port 1812 acct-port 1813 key password
Cisco(config)#radius-server attribute 8 include-in-access-req
Cisco(config)#radius-server vsa send authentication
Cisco(config)#aaa new-model
Cisco(config)#aaa authentication login default group radius
Cisco(config)#aaa authorization auth-proxy default group radius
Cisco(config)#ip arp inspection vlan 220
Cisco(config)#ip arp inspection trust
Cisco(config)#ip dhcp snooping
Cisco(config)#ip dhcp snooping authorized-server 10.0.100.251
Cisco(config)#ip dhcp snooping database file tftp://10.0.100.111/Cisco_dhcp.txt
Cisco(config)#ip dhcp snooping vlan 220
Cisco(config)#ip dhcp snooping trust
Cisco(config)#interface g1/0/6
Cisco(config-if)#ip dhcp snooping trust
Cisco(config)#ip device tracking
Cisco(config)#ip access-list extended web-auth-policy1
Cisco(config-ext-nacl)#permit udp any any
Cisco(config-ext-nacl)#permit tcp any any eq www
Cisco(config-ext-nacl)#deny ip any any
Cisco(config)#fallback profile fallback1
Cisco(config-fallback-profile)#ip access-group web-auth-policy1 in
Cisco(config-if)#ip admission web-auth-rule1
Cisco(config-if)#switchport mode access
Cisco(config-if)#switchport access vlan 220
Cisco(config-if)#portal local-server enable
Cisco(config-if)#dot1x pae authenticator
Cisco(config-if)#portal auth-fail vlan 99
Cisco(config-if)#authentication fallback fallback1
Cisco(config-if)#authentication order webauth
Cisco(config-if)#authentication port-control auto
Cisco(config-if)#stp edged-port enable
Cisco(config)#ip access-group web-auth-policy1 in
Cisco#show ip admission cache
Cisco#show authentication interface g1/0/18
```

```bash
Cisco(config)#monitor session 1 source interface g1/0/6 both
Cisco(config)#monitor session 1 destination interface g1/0/4 encapsulation replicate
Cisco#show monitor
Cisco#show monitor session 1
Cisco#show monitor session 1 detail
```

#### **Display Commands**

**ProVision commands**

```bash
show arp
show arp-protection
show arp-protection statistics
show arp ip-address
show flash
show time
show system information
show alias
show interface <port>
show interface <interface> rate
show cpu
No equivalent ProVision software command
show running-configuration
show running-configuration by-linenum
No equivalent ProVision software command
show current-configuration interface
show debug
No equivalent ProVision software command
No equivalent ProVision software command
No equivalent ProVision software command
display dhcp relay information all
display dhcp relay information interface Vlan-interface <vlan-id>
show dhcp-relay
show dhcp-snooping binding database
show dhcp-snooping information
show dhcp-snooping [ip ip_address]
show dhcp-snooping packet statistics
show dhcp-snooping trust
show tech
show ip dns domain
display dns domain dynamic
show ip dns < domain | server >
show port-access authenticator config
show port-access authenticator config [interface]
show port-access authenticator session counters [interface interface-list]
show port-access authenticator statistics [interface interface-list]
show system temperature
show system fans
show secure-mode
show gvrp statistics interface <port_list>
show gvrp timer interface <port_list>
show gvrp state interface <port_list> vlan <vlan-id>
show gvrp statistics
show gvrp status
display gvrp vlan-operation interface interface-type interfacenumber
show history-command
show tacacs
show accounting
display radius scheme
show rip
show rip interface
show rip process-id ip-address mask/mask-length
show rip process-id route
show rip process-id route peer ip-address
show rmon statistics
show route-policy
show saved-configuration
show saved-configuration by-linenum
show schedule reboot <after|at>
show sflow
show sflow sampling-polling <receiver table number>
show sflow slot <slot-number>
show snmp-agent host-public-key
show snmp-agent public-key local rsa public
show snmp-agent public-key peer
show radius
show radius host
show accoutning
show radius scheme
show ip check source
show ip community-list
display ip http
display ip https
show ip prefix-list
show lacp local
display link-aggregation load-sharing mode
display link-aggregation member-port
display link-aggregation summary
display link-aggregation verbose
display lldp local-information
display lldp local-information global
display lldp local-information interface interface-type interfacenumber
show lldp neighbor-information brief
show lldp neighbor-information list
show lldp neighbor-information list system-name <string>
show lldp stats
show lldp stats global
show lldp stats interface interface-type interface-number
show lldp status
show lldp status interface interface-type interface-number
show lldp tlv-config interface interface-type interface-number
show logging
display logfile buffer
display loopback-detection
show mac-address
display mac-address
show mac-address aging-time
display mac-address multicast
show port-access mac-based
show port-access mac-authentication
show port-access mac-authentication [interface …]
show system information
display memory
show uplink-failure-detection
display multicast forwarding-table
show ip mroute
display multicast routing-table
show ip pim rpf-override
display multicast routing-table static
display multicast rpf-info
show ip pim interface
display pim interface
show ip pim interface verbose
display pim join-prune
show ip pim neighbor
display pim neighbor
show ip pim neighbor <ip> verbose
display pim routing-table
display pim rp-info
show power-over-ethernet device
show power-over-ethernet interface
show power-over-ethernet interface power
show power-over-ethernet power-usage
show power-over-ethernet alarm
display poe-power switch state
display poe-power switch state
show port trunk
display power
display protocol-vlan
display protocol-vlan interface
show crypto host-public-key
show ip host-public-key
display public-key local rsa public
show ip client-public-key
display public-key peer
show radius
show radius host
show accoutning
display radius scheme
display rip
display rip interface
display rip process-id ip-address mask/mask-length
display rip process-id route
display rip process-id route peer ip-address
show rmon statistics
display rmon statistics
show route-policy
display route-policy
show saved-configuration
display saved-configuration
display saved-configuration by-linenum
display current-configuration
display current-configuration by-linenum
display current-configuration interface
display current-configuration
show ip source-lockdown bindings
display user-bind
show vlan
display vlan
show vrrp
display vrrp
show vrrp <interface-type> vrid <virtual routerid>
display vrrp interface <interface-type> vrid <virtual routerid>
show vrrp statistics
display vrrp statistics
show vrrp statistics global
display vrrp statistics interface <interface-type> vrid <virtual routerid>
show vrrp verbose
display vrrp vlan-operation interface interface-type interfacenumber
```

