# Nexus\_vPC\_Config\_v2



{% file src="../.gitbook/assets/Nexus_vPC_Config_v2.docx" %}

Nexus 1 + Nexus 2 | Exact Port Assignments from Your Document | Fortigate + Servers + PA\
Netmagic Datacenter | Hassan | Draft — Verify before applying

{% hint style="danger" %}
**CRITICAL** — DRAFT — All port numbers taken directly from your port assignment document. Verify physical cabling before applying.
{% endhint %}

## Port Assignment Reference

```
! Topology layer summary:
! [SERVER1]          [SERVER2]
!     |                  |
!  vPC trunk          vPC trunk
!     |                  |
! [NEXUS 1] <--vPC-->\ [NEXUS 2]   (Keepalive: 10.10.10.1/2)
! LAN: 172.27.8.0/24
!     |                  |
!  FW LACP + FS MCLAG
!     |                  |
! [FGCORE1]         [FGCORE2]     (Fortigate Core L3)
!     |                  |
!  FW LACP + FS MCLAG
! LAN: 172.27.8.0/24
!     |                  |
! [FGSW1]           [FGSW2]       (Fortigate SW)
!     |                  |
!  FS MCLAG + PA LACP
!     |                  |
! [PA PARAM 1] [PA PARAM 2] (Palo Alto)
```

## Port Assignment Plan

{% hint style="info" %}
Adjust these port numbers to match your actual Nexus hardware slot/port layout.
{% endhint %}

```
! ============================================================
! PORT ASSIGNMENT — NEXUS 1 & NEXUS 2 (symmetric)
! ============================================================

! Ethernet1/49-50 = vPC Peer-Link (ISL between Nexus1 <-> Nexus2 Po50)
! Ethernet1/47-48 = vPC Keep-alive (Po100, 10.10.10.1/2 Po 48)
! Ethernet1/46    = Fortigate Core1 (Po46 on Nexus1 / Po46 on Nexus2)
! Ethernet1/45    = Fortigate Core2 (Po45 on Nexus1 / Po45 on Nexus2)

! Ethernet1/4-5   = SERVER SW Po2 dual-home (Po104 on Nexus1 / Po104 on Nexus2)
! Ethernet1/6-7   = SERVER SW Po3 dual-home (Po105 on Nexus1 / Po105 on Nexus2)
! Ethernet1/8-9   = SERVER SW Po4 dual-home (Po106 on Nexus1 / Po106 on Nexus2)
! Ethernet1/10-11 = SERVER SW Po5 dual-home (Po107 on Nexus1 / Po107 on Nexus2)
! Ethernet1/12-13 = SERVER SW Po6 dual-home (Po108 on Nexus1 / Po108 on Nexus2)
! Ethernet1/14-15 = SERVER SW Po7 dual-home (Po109 on Nexus1 / Po109 on Nexus2)
! Ethernet1/16-17 = SERVER SW Po8 dual-home (Po110 on Nexus1 / Po110 on Nexus2)
! Ethernet1/18-19 = SERVER SW Po9 dual-home (Po111 on Nexus1 / Po111 on Nexus2)
! Ethernet1/20-21 = SERVER SW Po10 dual-home (Po112 on Nexus1 / Po112 on Nexus2)
! Ethernet1/22-23 = SERVER SW Po11 dual-home (Po113 on Nexus1 / Po113 on Nexus2)

! Loopback0 = NTP/SNMP source
! Loopback1 = 172.27.7.1/30 (replicated from CBS)
```

## Section 1 — Feature Enables (Both Switches — Apply First)

{% hint style="info" %}
Enable features BEFORE any interface or vPC config. `feature vpc` must be present before configuring vpc domain.
{% endhint %}

{% tabs %}
{% tab title="NEXUS 1" %}
```
hostname Netmagic-Nexus1
feature lacp
feature vpc
feature interface-vlan
feature lldp
feature ssh
feature snmp
feature hsrp
ip routing
no feature telnet
```
{% endtab %}

{% tab title="NEXUS 2" %}
```
hostname Netmagic-Nexus2
feature lacp
feature vpc
feature interface-vlan
feature lldp
feature ssh
feature snmp
feature hsrp
ip routing
no feature telnet
```
{% endtab %}
{% endtabs %}

## Section 2 — vPC Domain, Dual Keepalive & Peer-Link (Po50)

{% hint style="danger" %}
Keepalive links (E1/47 + E1/48) MUST be UP and both IPs reachable BEFORE Po50 peer-link comes up. Bring up keepalives first, verify reachability, then bring up Po50.
{% endhint %}

{% hint style="info" %}
Dual keepalive: primary 10.10.10.x on E1/47, secondary 20.20.20.x on E1/48. NX-OS uses primary by default. Secondary is fallback.
{% endhint %}

{% hint style="warning" %}
Mask corrected to /30 (255.255.255.252) on both sides — your document showed /24 on Nexus2 side which would overlap with other subnets.
{% endhint %}

### NEXUS 1 — Keepalive Links (E1/47, E1/48)

```
interface Ethernet1/47
  description vPC-Keepalive-PRIMARY-10.10.10.x
  no switchport
  ip address 10.10.10.1 255.255.255.252
  no shutdown

interface Ethernet1/48
  description vPC-Keepalive-SECONDARY-20.20.20.x
  no switchport
  ip address 20.20.20.1 255.255.255.252
  no shutdown
```

### NEXUS 1 — vPC Domain 10

```
vpc domain 10
  peer-keepalive destination 10.10.10.2 source 10.10.10.1
  peer-keepalive destination 20.20.20.2 source 20.20.20.1
  peer-gateway
  auto-recovery
  auto-recovery reload-delay 360
  delay restore 150
  ip arp synchronize
```

### NEXUS 1 — Peer-Link Po50 (E1/49 + E1/50)

```
interface port-channel50
  description vPC-Peer-Link-ISL-to-Nexus2
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  spanning-tree port type network
  vpc peer-link
  no shutdown

interface Ethernet1/49
  description vPC-ISL-to-Nexus2-MemberA
  switchport
  switchport mode trunk
  channel-group 50 mode active
  no shutdown

interface Ethernet1/50
  description vPC-ISL-to-Nexus2-MemberB
  switchport
  switchport mode trunk
  channel-group 50 mode active
  no shutdown
```

### NEXUS 2 — Keepalive Links (E1/47, E1/48)

```
interface Ethernet1/47
  description vPC-Keepalive-PRIMARY-to-Nexus1
  no switchport
  ip address 10.10.10.2 255.255.255.252
  no shutdown

interface Ethernet1/48
  description vPC-Keepalive-SECONDARY-to-Nexus1
  no switchport
  ip address 20.20.20.2 255.255.255.252
  no shutdown
```

### NEXUS 2 — vPC Domain 10

```
vpc domain 10
  peer-keepalive destination 10.10.10.1 source 10.10.10.2
  peer-keepalive destination 20.20.20.1 source 20.20.20.2
  peer-gateway
  auto-recovery
  auto-recovery reload-delay 360
  delay restore 150
  ip arp synchronize
```

### NEXUS 2 — Peer-Link Po50 (E1/49 + E1/50)

```
interface port-channel50
  description vPC-Peer-Link-ISL-to-Nexus1
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  spanning-tree port type network
  vpc peer-link
  no shutdown

interface Ethernet1/49
  description vPC-ISL-to-Nexus1-MemberA
  switchport
  switchport mode trunk
  channel-group 50 mode active
  no shutdown

interface Ethernet1/50
  description vPC-ISL-to-Nexus1-MemberB
  switchport
  switchport mode trunk
  channel-group 50 mode active
  no shutdown
```

## Section 3 — VLAN Database (Identical on Both Switches)

```
! ============================================================
! VLAN DATABASE
! ============================================================
vlan 11
  name BASE-VLAN
vlan 12
  name DATABASE-VLAN
vlan 13
  name ANCILLARY-VLAN
vlan 14
  name HSM-VLAN
vlan 15
  name PMP-VLAN
vlan 16
  name NAS-VLAN
vlan 20
  name ATM-VLAN
vlan 21
  name CARD-MGMT-VLAN
vlan 22
  name ECOMMERCE-VLAN
vlan 23
  name WEB-SERVERS-VLAN
vlan 24
  name IMPS-SWITCH
vlan 25
  name IMPS-WEB
vlan 26
  name IMPS-EXTERNAL
vlan 27
  name UPI-SWITCH
vlan 28
  name UPI-WEB
vlan 29
  name UPI-EXTERNAL
vlan 30
  name BBPS-SWITCH
vlan 31
  name BBPS-WEB
vlan 32
  name BBPS-INTERNAL
vlan 33
  name FUTURE-USE
vlan 34
  name AEPS-EKYC
vlan 35
  name WEB-EKYC
vlan 36
  name CBS
vlan 37
  name BBPS-INTERNAL-2
vlan 38
  name FUTURE-USE-2
vlan 39
  name UAT-OOB
vlan 40
  name UAT
vlan 41
  name PAPG
vlan 45
 name L2-ONLY
```

## Section 4 — Spanning Tree

{% hint style="danger" %}
Set STP priority BEFORE any trunk comes up. Nexus 1 = primary root (4096), Nexus 2 = secondary root (8192).
{% endhint %}

### NEXUS 1 — STP Primary Root

```
spanning-tree mode rapid-pvst
spanning-tree vlan 1-39,45 root primary
```

### NEXUS 2 — STP Secondary Root

```
spanning-tree mode rapid-pvst
spanning-tree vlan 1-39,45 root secondary
```

## Section 5 — Fortigate Core 1 & 2 (E1/46 → Po46, E1/45 → Po45)

{% hint style="info" %}
Single physical port per Nexus per Fortigate (E1/46 for FGCore1, E1/45 for FGCore2). vPC provides redundancy across the two Nexus switches. If you need per-switch port-channel resilience, add a second port per Fortigate and bundle.
{% endhint %}

### Fortigate Core 1 — Po46, vPC 46

#### NEXUS 1

```
interface port-channel46
  description FGCore1-vPC46
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 46
  no shutdown

interface Ethernet1/46
  description FGCore1-Link-Nexus1
  switchport
  switchport mode trunk
  channel-group 46 mode active
  no shutdown
```

#### NEXUS 2

```
interface port-channel46
  description FGCore1-vPC46
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 46
  no shutdown

interface Ethernet1/46
  description FGCore1-Link-Nexus2
  switchport
  switchport mode trunk
  channel-group 46 mode active
  no shutdown
```

### Fortigate Core 2 — Po45, vPC 45

#### NEXUS 1

```
interface port-channel45
  description FGCore2-vPC45
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 45
  no shutdown

interface Ethernet1/45
  description FGCore2-Link-Nexus1
  switchport
  switchport mode trunk
  channel-group 45 mode active
  no shutdown
```

#### NEXUS 2

```
interface port-channel45
  description FGCore2-vPC45
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 45
  no shutdown

interface Ethernet1/45
  description FGCore2-Link-Nexus2
  switchport
  switchport mode trunk
  channel-group 45 mode active
  no shutdown
```

## Section 6 — Server Port-Channels Po104–Po113 (E1/4–E1/23)

{% hint style="info" %}
Each server is dual-homed across Nexus 1 and Nexus 2. The same port-channel number and vPC number are used on both switches. Po110 and Po111 use lacp rate fast (was 'lacp timeout short' on CBS for FSNETNTX1127/1128).
{% endhint %}

{% hint style="warning" %}
Server-side NIC bonding must be LACP (mode 4 / 802.3ad on Linux, LACP on VMware ESXi) before cutover. Verify before connecting.
{% endhint %}

### FSNETNTX1121 — Po104, vPC 104 (Ethernet1/4 + Ethernet1/5)

#### NEXUS 1

```
interface port-channel104
  description FSNETNTX1121-vPC104
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 104
  no shutdown

interface Ethernet1/4
  description FSNETNTX1121-Link1-Nexus1
  switchport
  switchport mode trunk
  channel-group 104 mode active
  no shutdown

interface Ethernet1/5
  description FSNETNTX1121-Link2-Nexus1
  switchport
  switchport mode trunk
  channel-group 104 mode active
  no shutdown
```

#### NEXUS 2

```
interface port-channel104
  description FSNETNTX1121-vPC104
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 104
  no shutdown

interface Ethernet1/4
  description FSNETNTX1121-Link1-Nexus2
  switchport
  switchport mode trunk
  channel-group 104 mode active
  no shutdown

interface Ethernet1/5
  description FSNETNTX1121-Link2-Nexus2
  switchport
  switchport mode trunk
  channel-group 104 mode active
  no shutdown
```

### FSNETNTX1122 — Po105, vPC 105 (Ethernet1/6 + Ethernet1/7)

#### NEXUS 1

```
interface port-channel105
  description FSNETNTX1122-vPC105
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 105
  no shutdown

interface Ethernet1/6
  description FSNETNTX1122-Link1-Nexus1
  switchport
  switchport mode trunk
  channel-group 105 mode active
  no shutdown

interface Ethernet1/7
  description FSNETNTX1122-Link2-Nexus1
  switchport
  switchport mode trunk
  channel-group 105 mode active
  no shutdown
```

#### NEXUS 2

```
interface port-channel105
  description FSNETNTX1122-vPC105
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 105
  no shutdown

interface Ethernet1/6
  description FSNETNTX1122-Link1-Nexus2
  switchport
  switchport mode trunk
  channel-group 105 mode active
  no shutdown

interface Ethernet1/7
  description FSNETNTX1122-Link2-Nexus2
  switchport
  switchport mode trunk
  channel-group 105 mode active
  no shutdown
```

### FSNETNTX1123 — Po106, vPC 106 (Ethernet1/8 + Ethernet1/9)

#### NEXUS 1

```
interface port-channel106
  description FSNETNTX1123-vPC106
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 106
  no shutdown

interface Ethernet1/8
  description FSNETNTX1123-Link1-Nexus1
  switchport
  switchport mode trunk
  channel-group 106 mode active
  no shutdown

interface Ethernet1/9
  description FSNETNTX1123-Link2-Nexus1
  switchport
  switchport mode trunk
  channel-group 106 mode active
  no shutdown
```

#### NEXUS 2

```
interface port-channel106
  description FSNETNTX1123-vPC106
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 106
  no shutdown

interface Ethernet1/8
  description FSNETNTX1123-Link1-Nexus2
  switchport
  switchport mode trunk
  channel-group 106 mode active
  no shutdown

interface Ethernet1/9
  description FSNETNTX1123-Link2-Nexus2
  switchport
  switchport mode trunk
  channel-group 106 mode active
  no shutdown
```

### FSNETNTX1124 — Po107, vPC 107 (Ethernet1/10 + Ethernet1/11)

#### NEXUS 1

```
interface port-channel107
  description FSNETNTX1124-vPC107
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 107
  no shutdown

interface Ethernet1/10
  description FSNETNTX1124-Link1-Nexus1
  switchport
  switchport mode trunk
  channel-group 107 mode active
  no shutdown

interface Ethernet1/11
  description FSNETNTX1124-Link2-Nexus1
  switchport
  switchport mode trunk
  channel-group 107 mode active
  no shutdown
```

#### NEXUS 2

```
interface port-channel107
  description FSNETNTX1124-vPC107
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 107
  no shutdown

interface Ethernet1/10
  description FSNETNTX1124-Link1-Nexus2
  switchport
  switchport mode trunk
  channel-group 107 mode active
  no shutdown

interface Ethernet1/11
  description FSNETNTX1124-Link2-Nexus2
  switchport
  switchport mode trunk
  channel-group 107 mode active
  no shutdown
```

### FSNETNTX1125 — Po108, vPC 108 (Ethernet1/12 + Ethernet1/13)

#### NEXUS 1

```
interface port-channel108
  description FSNETNTX1125-vPC108
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 108
  no shutdown

interface Ethernet1/12
  description FSNETNTX1125-Link1-Nexus1
  switchport
  switchport mode trunk
  channel-group 108 mode active
  no shutdown

interface Ethernet1/13
  description FSNETNTX1125-Link2-Nexus1
  switchport
  switchport mode trunk
  channel-group 108 mode active
  no shutdown
```

#### NEXUS 2

```
interface port-channel108
  description FSNETNTX1125-vPC108
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 108
  no shutdown

interface Ethernet1/12
  description FSNETNTX1125-Link1-Nexus2
  switchport
  switchport mode trunk
  channel-group 108 mode active
  no shutdown

interface Ethernet1/13
  description FSNETNTX1125-Link2-Nexus2
  switchport
  switchport mode trunk
  channel-group 108 mode active
  no shutdown
```

### FSNETNTX1126 — Po109, vPC 109 (Ethernet1/14 + Ethernet1/15)

#### NEXUS 1

```
interface port-channel109
  description FSNETNTX1126-vPC109
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 109
  no shutdown

interface Ethernet1/14
  description FSNETNTX1126-Link1-Nexus1
  switchport
  switchport mode trunk
  channel-group 109 mode active
  no shutdown

interface Ethernet1/15
  description FSNETNTX1126-Link2-Nexus1
  switchport
  switchport mode trunk
  channel-group 109 mode active
  no shutdown
```

#### NEXUS 2

```
interface port-channel109
  description FSNETNTX1126-vPC109
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 109
  no shutdown

interface Ethernet1/14
  description FSNETNTX1126-Link1-Nexus2
  switchport
  switchport mode trunk
  channel-group 109 mode active
  no shutdown

interface Ethernet1/15
  description FSNETNTX1126-Link2-Nexus2
  switchport
  switchport mode trunk
  channel-group 109 mode active
  no shutdown
```

### FSNETNTX1127 — Po110, vPC 110 (Ethernet1/16 + Ethernet1/17)

#### NEXUS 1

```
interface port-channel110
  description FSNETNTX1127-vPC110
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 110
  no shutdown

interface Ethernet1/16
  description FSNETNTX1127-Link1-Nexus1
  switchport
  switchport mode trunk
  lacp rate fast
  channel-group 110 mode active
  no shutdown

interface Ethernet1/17
  description FSNETNTX1127-Link2-Nexus1
  switchport
  switchport mode trunk
  lacp rate fast
  channel-group 110 mode active
  no shutdown
```

#### NEXUS 2

```
interface port-channel110
  description FSNETNTX1127-vPC110
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 110
  no shutdown

interface Ethernet1/16
  description FSNETNTX1127-Link1-Nexus2
  switchport
  switchport mode trunk
  lacp rate fast
  channel-group 110 mode active
  no shutdown

interface Ethernet1/17
  description FSNETNTX1127-Link2-Nexus2
  switchport
  switchport mode trunk
  lacp rate fast
  channel-group 110 mode active
  no shutdown
```

### FSNETNTX1128 — Po111, vPC 111 (Ethernet1/18 + Ethernet1/19)

#### NEXUS 1

```
interface port-channel111
  description FSNETNTX1128-vPC111
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 111
  no shutdown

interface Ethernet1/18
  description FSNETNTX1128-Link1-Nexus1
  switchport
  switchport mode trunk
  lacp rate fast
  channel-group 111 mode active
  no shutdown

interface Ethernet1/19
  description FSNETNTX1128-Link2-Nexus1
  switchport
  switchport mode trunk
  lacp rate fast
  channel-group 111 mode active
  no shutdown
```

#### NEXUS 2

```
interface port-channel111
  description FSNETNTX1128-vPC111
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 111
  no shutdown

interface Ethernet1/18
  description FSNETNTX1128-Link1-Nexus2
  switchport
  switchport mode trunk
  lacp rate fast
  channel-group 111 mode active
  no shutdown

interface Ethernet1/19
  description FSNETNTX1128-Link2-Nexus2
  switchport
  switchport mode trunk
  lacp rate fast
  channel-group 111 mode active
  no shutdown
```

### SERVER-SW-9 — Po112, vPC 112 (Ethernet1/20 + Ethernet1/21)

#### NEXUS 1

```
interface port-channel112
  description SERVER-SW-9-vPC112
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 112
  no shutdown

interface Ethernet1/20
  description SERVER-SW-9-Link1-Nexus1
  switchport
  switchport mode trunk
  channel-group 112 mode active
  no shutdown

interface Ethernet1/21
  description SERVER-SW-9-Link2-Nexus1
  switchport
  switchport mode trunk
  channel-group 112 mode active
  no shutdown
```

#### NEXUS 2

```
interface port-channel112
  description SERVER-SW-9-vPC112
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 112
  no shutdown

interface Ethernet1/20
  description SERVER-SW-9-Link1-Nexus2
  switchport
  switchport mode trunk
  channel-group 112 mode active
  no shutdown

interface Ethernet1/21
  description SERVER-SW-9-Link2-Nexus2
  switchport
  switchport mode trunk
  channel-group 112 mode active
  no shutdown
```

### SERVER-SW-10 — Po113, vPC 113 (Ethernet1/22 + Ethernet1/23)

#### NEXUS 1

```
interface port-channel113
  description SERVER-SW-10-vPC113
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 113
  no shutdown

interface Ethernet1/22
  description SERVER-SW-10-Link1-Nexus1
  switchport
  switchport mode trunk
  channel-group 113 mode active
  no shutdown

interface Ethernet1/23
  description SERVER-SW-10-Link2-Nexus1
  switchport
  switchport mode trunk
  channel-group 113 mode active
  no shutdown
```

#### NEXUS 2

```
interface port-channel113
  description SERVER-SW-10-vPC113
  switchport
  switchport mode trunk
  switchport trunk allowed vlan 1-39,45
  vpc 113
  no shutdown

interface Ethernet1/22
  description SERVER-SW-10-Link1-Nexus2
  switchport
  switchport mode trunk
  channel-group 113 mode active
  no shutdown

interface Ethernet1/23
  description SERVER-SW-10-Link2-Nexus2
  switchport
  switchport mode trunk
  channel-group 113 mode active
  no shutdown
```

## Section 7 — SVI Routing + HSRP (All 31 VLANs)

{% hint style="info" %}
Nexus 1 = HSRP active (priority 110 + preempt) for all VLANs. Nexus 2 = standby (priority 100). HSRP virtual IP (.1) is what all downstream devices use as their default gateway. With peer-gateway enabled, both Nexus switches can forward regardless of HSRP state.
{% endhint %}

{% hint style="warning" %}
HSRP virtual IPs (.1 per subnet) replace the old CBS SVI IPs (.1 per subnet) — the gateway address hosts use is unchanged. Only the physical Nexus IPs (.2 and .3) are new.
{% endhint %}

{% hint style="danger" %}
Update Fortigate and Palo Alto interface gateway config to use .1 virtual IPs (which is what the CBS had). No change needed on hosts — same gateway.
{% endhint %}

### NEXUS 1 — All SVIs (HSRP Active)

```
! ============================================================
! SVIs + HSRP — NEXUS 1 (Active, priority 110, preempt)
! Physical IP: .2 | HSRP Virtual: .1
! ============================================================

interface Vlan1
  ip address 172.27.8.30 255.255.255.0
  hsrp version 2
  hsrp 1
    ip 172.27.8.1
    priority 110
    preempt
  no shutdown

interface Vlan10
  ip address 172.27.10.2 255.255.255.0
  hsrp version 2
  hsrp 10
    ip 172.27.10.1
    priority 110
    preempt
  no shutdown

interface Vlan11
  ip address 172.27.11.2 255.255.255.0
  hsrp version 2
  hsrp 11
    ip 172.27.11.1
    priority 110
    preempt
  no shutdown

interface Vlan12
  ip address 172.27.12.2 255.255.255.0
  hsrp version 2
  hsrp 12
    ip 172.27.12.1
    priority 110
    preempt
  no shutdown

interface Vlan13
  ip address 172.27.13.2 255.255.255.0
  ipv6 address 2401:8800:c13:2::85/126
  hsrp version 2
  hsrp 13
    ip 172.27.13.1
    priority 110
    preempt
  no shutdown

interface Vlan14
  ip address 172.27.14.2 255.255.255.0
  hsrp version 2
  hsrp 14
    ip 172.27.14.1
    priority 110
    preempt
  no shutdown

interface Vlan15
  ip address 172.27.15.2 255.255.255.0
  hsrp version 2
  hsrp 15
    ip 172.27.15.1
    priority 110
    preempt
  no shutdown

interface Vlan16
  ip address 172.27.16.2 255.255.255.0
  hsrp version 2
  hsrp 16
    ip 172.27.16.1
    priority 110
    preempt
  no shutdown

interface Vlan17
  ip address 172.27.17.2 255.255.255.0
  hsrp version 2
  hsrp 17
    ip 172.27.17.1
    priority 110
    preempt
  no shutdown

interface Vlan18
  ip address 172.27.18.2 255.255.255.0
  hsrp version 2
  hsrp 18
    ip 172.27.18.1
    priority 110
    preempt
  no shutdown

interface Vlan19
  ip address 172.27.19.2 255.255.255.0
  hsrp version 2
  hsrp 19
    ip 172.27.19.1
    priority 110
    preempt
  no shutdown

interface Vlan20
  ip address 172.27.20.2 255.255.255.0
  hsrp version 2
  hsrp 20
    ip 172.27.20.1
    priority 110
    preempt
  no shutdown

interface Vlan21
  ip address 172.27.21.2 255.255.255.0
  hsrp version 2
  hsrp 21
    ip 172.27.21.1
    priority 110
    preempt
  no shutdown

interface Vlan22
  ip address 172.27.22.2 255.255.255.0
  hsrp version 2
  hsrp 22
    ip 172.27.22.1
    priority 110
    preempt
  no shutdown

interface Vlan23
  ip address 172.27.23.2 255.255.255.0
  ipv6 enable
  hsrp version 2
  hsrp 23
    ip 172.27.23.1
    priority 110
    preempt
  no shutdown

interface Vlan24
  ip address 172.27.24.2 255.255.255.0
  hsrp version 2
  hsrp 24
    ip 172.27.24.1
    priority 110
    preempt
  no shutdown

interface Vlan25
  ip address 172.27.25.2 255.255.255.0
  hsrp version 2
  hsrp 25
    ip 172.27.25.1
    priority 110
    preempt
  no shutdown

interface Vlan26
  ip address 172.27.26.2 255.255.255.0
  hsrp version 2
  hsrp 26
    ip 172.27.26.1
    priority 110
    preempt
  no shutdown

interface Vlan27
  ip address 172.27.27.2 255.255.255.0
  ipv6 enable
  hsrp version 2
  hsrp 27
    ip 172.27.27.1
    priority 110
    preempt
  no shutdown

interface Vlan28
  ip address 172.27.28.2 255.255.255.0
  hsrp version 2
  hsrp 28
    ip 172.27.28.1
    priority 110
    preempt
  no shutdown

interface Vlan29
  ip address 172.27.29.2 255.255.255.0
  hsrp version 2
  hsrp 29
    ip 172.27.29.1
    priority 110
    preempt
  no shutdown

interface Vlan30
  ip address 172.27.30.2 255.255.255.0
  hsrp version 2
  hsrp 30
    ip 172.27.30.1
    priority 110
    preempt
  no shutdown

interface Vlan31
  ip address 172.27.31.2 255.255.255.0
  hsrp version 2
  hsrp 31
    ip 172.27.31.1
    priority 110
    preempt
  no shutdown

interface Vlan32
  ip address 172.27.32.2 255.255.255.0
  hsrp version 2
  hsrp 32
    ip 172.27.32.1
    priority 110
    preempt
  no shutdown

interface Vlan33
  ip address 172.27.33.2 255.255.255.0
  hsrp version 2
  hsrp 33
    ip 172.27.33.1
    priority 110
    preempt
  no shutdown

interface Vlan34
  ip address 172.27.34.2 255.255.255.0
  hsrp version 2
  hsrp 34
    ip 172.27.34.1
    priority 110
    preempt
  no shutdown

interface Vlan35
  ip address 172.27.35.2 255.255.255.0
  hsrp version 2
  hsrp 35
    ip 172.27.35.1
    priority 110
    preempt
  no shutdown

interface Vlan36
  ip address 172.27.36.2 255.255.255.0
  hsrp version 2
  hsrp 36
    ip 172.27.36.1
    priority 110
    preempt
  no shutdown

interface Vlan37
  ip address 172.27.37.2 255.255.255.0
  ipv6 address 2401:8800:c13:2::91/124
  hsrp version 2
  hsrp 37
    ip 172.27.37.1
    priority 110
    preempt
  no shutdown

interface Vlan38
  ip address 172.27.38.2 255.255.255.0
  hsrp version 2
  hsrp 38
    ip 172.27.38.1
    priority 110
    preempt
  no shutdown

interface Vlan39
  ip address 172.27.39.2 255.255.255.0
  hsrp version 2
  hsrp 39
    ip 172.27.39.1
    priority 110
    preempt
  no shutdown

! VLAN 45 — L2 only, no SVI

ip default-gateway 172.27.8.1
```

### NEXUS 2 — All SVIs (HSRP Standby)

```
! ============================================================
! SVIs + HSRP — NEXUS 2 (Standby, priority 100)
! Physical IP: .3 | HSRP Virtual: .1 (same as Nexus1)
! ============================================================

interface Vlan1
  ip address 172.27.8.31 255.255.255.0
  hsrp version 2
  hsrp 1
    ip 172.27.8.1
    priority 100
  no shutdown

interface Vlan10
  ip address 172.27.10.3 255.255.255.0
  hsrp version 2
  hsrp 10
    ip 172.27.10.1
    priority 100
  no shutdown

interface Vlan11
  ip address 172.27.11.3 255.255.255.0
  hsrp version 2
  hsrp 11
    ip 172.27.11.1
    priority 100
  no shutdown

interface Vlan12
  ip address 172.27.12.3 255.255.255.0
  hsrp version 2
  hsrp 12
    ip 172.27.12.1
    priority 100
  no shutdown

interface Vlan13
  ip address 172.27.13.3 255.255.255.0
  ipv6 address 2401:8800:c13:2::85/126
  hsrp version 2
  hsrp 13
    ip 172.27.13.1
    priority 100
  no shutdown

interface Vlan14
  ip address 172.27.14.3 255.255.255.0
  hsrp version 2
  hsrp 14
    ip 172.27.14.1
    priority 100
  no shutdown

interface Vlan15
  ip address 172.27.15.3 255.255.255.0
  hsrp version 2
  hsrp 15
    ip 172.27.15.1
    priority 100
  no shutdown

interface Vlan16
  ip address 172.27.16.3 255.255.255.0
  hsrp version 2
  hsrp 16
    ip 172.27.16.1
    priority 100
  no shutdown

interface Vlan17
  ip address 172.27.17.3 255.255.255.0
  hsrp version 2
  hsrp 17
    ip 172.27.17.1
    priority 100
  no shutdown

interface Vlan18
  ip address 172.27.18.3 255.255.255.0
  hsrp version 2
  hsrp 18
    ip 172.27.18.1
    priority 100
  no shutdown

interface Vlan19
  ip address 172.27.19.3 255.255.255.0
  hsrp version 2
  hsrp 19
    ip 172.27.19.1
    priority 100
  no shutdown

interface Vlan20
  ip address 172.27.20.3 255.255.255.0
  hsrp version 2
  hsrp 20
    ip 172.27.20.1
    priority 100
  no shutdown

interface Vlan21
  ip address 172.27.21.3 255.255.255.0
  hsrp version 2
  hsrp 21
    ip 172.27.21.1
    priority 100
  no shutdown

interface Vlan22
  ip address 172.27.22.3 255.255.255.0
  hsrp version 2
  hsrp 22
    ip 172.27.22.1
    priority 100
  no shutdown

interface Vlan23
  ip address 172.27.23.3 255.255.255.0
  ipv6 enable
  hsrp version 2
  hsrp 23
    ip 172.27.23.1
    priority 100
  no shutdown

interface Vlan24
  ip address 172.27.24.3 255.255.255.0
  hsrp version 2
  hsrp 24
    ip 172.27.24.1
    priority 100
  no shutdown

interface Vlan25
  ip address 172.27.25.3 255.255.255.0
  hsrp version 2
  hsrp 25
    ip 172.27.25.1
    priority 100
  no shutdown

interface Vlan26
  ip address 172.27.26.3 255.255.255.0
  hsrp version 2
  hsrp 26
    ip 172.27.26.1
    priority 100
  no shutdown

interface Vlan27
  ip address 172.27.27.3 255.255.255.0
  ipv6 enable
  hsrp version 2
  hsrp 27
    ip 172.27.27.1
    priority 100
  no shutdown

interface Vlan28
  ip address 172.27.28.3 255.255.255.0
  hsrp version 2
  hsrp 28
    ip 172.27.28.1
    priority 100
  no shutdown

interface Vlan29
  ip address 172.27.29.3 255.255.255.0
  hsrp version 2
  hsrp 29
    ip 172.27.29.1
    priority 100
  no shutdown

interface Vlan30
  ip address 172.27.30.3 255.255.255.0
  hsrp version 2
  hsrp 30
    ip 172.27.30.1
    priority 100
  no shutdown

interface Vlan31
  ip address 172.27.31.3 255.255.255.0
  hsrp version 2
  hsrp 31
    ip 172.27.31.1
    priority 100
  no shutdown

interface Vlan32
  ip address 172.27.32.3 255.255.255.0
  hsrp version 2
  hsrp 32
    ip 172.27.32.1
    priority 100
  no shutdown

interface Vlan33
  ip address 172.27.33.3 255.255.255.0
  hsrp version 2
  hsrp 33
    ip 172.27.33.1
    priority 100
  no shutdown

interface Vlan34
  ip address 172.27.34.3 255.255.255.0
  hsrp version 2
  hsrp 34
    ip 172.27.34.1
    priority 100
  no shutdown

interface Vlan35
  ip address 172.27.35.3 255.255.255.0
  hsrp version 2
  hsrp 35
    ip 172.27.35.1
    priority 100
  no shutdown

interface Vlan36
  ip address 172.27.36.3 255.255.255.0
  hsrp version 2
  hsrp 36
    ip 172.27.36.1
    priority 100
  no shutdown

interface Vlan37
  ip address 172.27.37.3 255.255.255.0
  ipv6 address 2401:8800:c13:2::91/124
  hsrp version 2
  hsrp 37
    ip 172.27.37.1
    priority 100
  no shutdown

interface Vlan38
  ip address 172.27.38.3 255.255.255.0
  hsrp version 2
  hsrp 38
    ip 172.27.38.1
    priority 100
  no shutdown

interface Vlan39
  ip address 172.27.39.3 255.255.255.0
  hsrp version 2
  hsrp 39
    ip 172.27.39.1
    priority 100
  no shutdown

! VLAN 45 — L2 only, no SVI

ip default-gateway 172.27.8.1
```

## Section 8 — Loopback Interfaces

### NEXUS 1

```
interface loopback0
  description NTP-SNMP-Source-Nexus1
  ip address 172.27.7.1 255.255.255.252
  no shutdown

interface loopback1
  description Replicated-CBS
  ip address 172.27.7.5 255.255.255.252
  no shutdown
```

### NEXUS 2

```
interface loopback0
  description NTP-SNMP-Source-Nexus2
  ip address 172.27.7.2 255.255.255.252
  no shutdown

interface loopback1
  description Replicated-CBS
  ip address 172.27.7.6 255.255.255.252
  no shutdown
```

## Section 9 — Management Plane (Both Switches)

### NTP

```
ntp server 172.27.13.11 use-vrf default
ntp server 172.27.13.12 use-vrf default
ntp source-interface loopback0
clock timezone IST 5 30
```

### Syslog

```
logging server 172.27.13.13
logging server 172.27.13.14
logging server 172.27.13.29
logging level default 6
logging console 2
logging timestamp milliseconds
logging source-interface loopback0
```

### SNMP

```
snmp-server community FSNET ro
snmp-server host 172.27.13.14 version 2c FSNET
snmp-server host 172.27.13.19 version 2c FSNET
snmp-server host 172.27.13.191 version 2c FSNET
snmp-server location "Netmagic Datacenter"
snmp-server contact "Nikhil Kadam"
```

### Users, SSH & Banner

{% hint style="danger" %}
Replace `<ENCRYPTED\>` with actual encrypted hashes. Never store plaintext passwords in config.
{% endhint %}

```
username cnfmgr    password 5 <ENCRYPTED\> role network-admin
username fsnetrw   password 5 <ENCRYPTED\> role network-admin
username nikhil.k  password 5 <ENCRYPTED\> role network-admin
username ajinkya.b password 5 <ENCRYPTED\> role network-admin

feature ssh
ssh key rsa 2048
no feature telnet

line console
  exec-timeout 5

line vty
  exec-timeout 5
  transport input ssh

banner motd #
AUTHORIZED ACCESS ONLY
DISCONNECT ASAP IF YOU ARE NOT AUTHORISED
ACCESS MONITORED AND RECORDED
#
```

## Section 10 — Post-Cutover Verification

{% hint style="info" %}
Run in order. vPC must be healthy before connecting any downstream device.
{% endhint %}

{% stepper %}
{% step %}
### Step 1 — vPC health

Run FIRST on both switches.

```
show vpc
show vpc brief
show vpc peer-keepalive
show vpc consistency-parameters global
show vpc role
```
{% endstep %}

{% step %}
### Step 2 — Port-channels

```
show port-channel summary
show lacp neighbor
show lacp counters
```
{% endstep %}

{% step %}
### Step 3 — STP root confirmation

```
show spanning-tree summary
show spanning-tree vlan 1 detail
```
{% endstep %}

{% step %}
### Step 4 — SVIs and HSRP

```
show ip interface brief
show hsrp brief
show ip route
```
{% endstep %}

{% step %}
### Step 5 — VLAN membership

```
show vlan brief
```
{% endstep %}

{% step %}
### Step 6 — NTP

```
show ntp peer-status
show clock
```
{% endstep %}

{% step %}
### Step 7 — Connectivity

```
ping 172.27.8.31 source-interface Vlan1
ping 172.27.13.13 source-interface Vlan13
ping 172.27.13.11 source-interface loopback0
```
{% endstep %}

{% step %}
### Step 8 — LLDP neighbors

```
show lldp neighbors
show lldp neighbors detail
```
{% endstep %}

{% step %}
### Step 9 — Transceiver health

```
show interface transceiver
```
{% endstep %}

{% step %}
### Step 10 — Error counters baseline

```
show interface counters errors
```
{% endstep %}
{% endstepper %}

Netmagic Nexus vPC Config v2 | Draft | Hassan | E1/45-46=FGCore, E1/47-48= Keepalive, E1/49-50=ISL Po50, E1/4-23=Servers Po104-113 | Verify before applying
