# Juniper Switch Networks

JUNOS is JUNIPER OPERATING SYSTEM.

## Junos OS

* Junos OS is the single operating system that comes under both physical and virtual devices regarding the device module.

The software release are in `M.nzb.s`

* `M` is major and minor
* `n` indicated the release number
* `Z` is release type
* `B` is build number
* `S` is spin numbers

The separation of control and forwarding plan is the key reason why JUNOS OS support multiple options.

## Routing Engine

It is the brain which is responsible for protocol.

The routing Engine maintain the routing table also known as routing information based RIB.

## Juniper Modes

Juniper CLI has two modes:

* **Operation mode** — the cmd works that operate the device (`ping 8.8.8.`)
* **Configuration mode** — the device OS is configure using the command `configure`

## Juniper Commands

* Use the `help` command to lean about others commands and `?` to view options
* Search for valid command `help apropos`
* Get more information on feature and configuration task `help topic`
* Enter in linux shell `start shell`

## Configuration Hierarchy

* `SYSTEM >> LOGIN >> USER`
* `SYSTEM >> SERVICES`
* `INTERFACE >> GE0/0/0`
* `INTERFACE >> IRB >> UNIT 10`

## Commands

* Operation mode: `show configuration`
* Configuration mode: `show`
* Match line of output: `show | match vlan 10`
* Exclude line of output: `show | execpt vlan 10`
* Match: `| match "valu1 | "valu2"`
* Run an operational command from config mode (like Cisco `do` command): `run ping`
* Set some configuration: `set system hostname JUNOSSWITCH`
* Remove some configuration (like `no` in Cisco): `delete system hostname JUNOSSWITCH`
* Note: Configuration doesn't apply when changes is done. its use `commit`
* Apply configuration and save it to disk: `commit`
* Show interfaces and IP (like `show ip interface brief` in Cisco): `show interface terse`

## Interface Type

* `ge` = gigabit ethernet
* `xe` = 10G ethernet
* `et/xle/fte` = 40G ethernet
* `ae` = aggregate ethernet (LAG or Etherchannel)
* `vlan` or `irb` = a logical interface based on vlan

Cisco `show ip interface brief`

Juniper `show interfaces terse`

Type notation: `X/Y/Z`

* `X` = FPC (Line Card)
* `Y` = Module or Slot
* `Z` = port number

## Management Interface

* `fxp0` = physical management interface on router
* `em0` = internal ports of router
* `me0` = physical management interface on switch
* `vme0` = virtual management for switch (A Switch stack)

## Special Interface

* `pimd/pime` = special special interface for multicast
* `dsc` = discard interface
* `ipip / gre` = used to create tunnel interfaces

## Interface Hierarchy

* `INTERFACE >> UNIT >> FAMILY >> SETTINGS`
* `INTERFACE` = physical interface
* `UNIT` = logical parameter
* `FAMILY` = IPV4/IPV6 , ethernet switching ,
* `SETTING` = IP Address, Port mode (Access or trunk) vlan

## Loopback Interface Configuration

`configuration mode`

```bash
set interface lo0 unit 0 family inet address 10.10.10.10/24
set interface lo0 description "TEST"
```

Rename for changing UNIT:

```bash
rename interface lo0 unit 100 unit 0
```

* Juniper has a concept of primary and preferred IP

| Cisco                                                                                                           | Juniper                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `interface loopback0<br>ip address 10.10.10.10 255.255.255.0<br>ip address 20.20.20.20 255.255.255.0 secondary` | `set interface lo0 unit 0 famliy inet address 10.10.10.10/24 primary<br><br>set intface lo0 unit 0 famliy inet address 20.20.20.20/24 preferred` |

Interface show: `show interfaces ge-0/0/0`

Show a lot of info of interface: `show interfaces ge-0/0/0 extensive`

Disable interface (like `shutdown`): `set interface ge-0/0/0 disbale`

Delete disable interface (like `no shutdown`): `delete interfaces ge-0/0/0 disable`

Deactivate configuration: `deactivate config ge-0/0/1`

## VLAN Configuration

Define VLAN: `set vlan NAME vlan-id ID`

`show vlans`

### Access and Trunk

Old:

```bash
set interfaces <INT> unit 0 family ethernet-switching port-mode access/trunk
```

New:

```bash
set interfaces <INT> unit 0 famoly ethernet-switching interface-mode access/trunk
```

## Copy Configuration

```bash
copy <exisiting-statement> to <new-statement>
copy interfaces ge-0/0/1 to ge-0/0/2
```

## Subinterfaces

To do enable vlan tagging:

```bash
set interfaces  ge-0/0/1 vlan-tagging
delete interfaces ge-0/0/1 unit 0
set interfaces ge-0/0/1 unit 0 vlan-id 10
```

## SVI

{% tabs %}
{% tab title="Cisco" %}
```bash
interface vlan 100
ip address 10.10.10.10 255.255.255.0
```
{% endtab %}

{% tab title="Juniper Old" %}
```bash
set interface irb unit 100 family inet address 10.10.10.10/24
set vlan test l3-interface irb.100
```
{% endtab %}

{% tab title="Juniper New" %}
```bash
set interface vlan unit 100 family inet address 10.10.10.10/24
set vlan test l3-interface irb.100
```
{% endtab %}
{% endtabs %}

## Voice Configuration

### Voice VLAN

Define voice vlan:

```bash
set vlan voice vlan-id 10
```

Apply the voice vlan to port:

```bash
set switch-options voip interface ge-0/0/0 vlan voice
```

OR

```bash
set ethernet-switching-options voip interface ge-0/0/0 vlan voice
```

### Power over Ethernet

```bash
set poe interface all
```

### LLDP and LLDP-MED

```bash
set protocol lldp-med interface all
```

## Active and Candidate

* **Active** = configuration that is running now
* **Candidate** = configuration we are preparing not active yet

`commit` moves the candidate config to active config.

The location of the candidate is:

```bash
/var/rundb/juniper.data
```

Compare the active and candidate config using `show | compare`

And config check `command cbecm`

Add comment to the commit `commit comment TEXT` it will help in rollback

## Configuration Groups

Configuration groups are reuable of configuration.

Create groups:

```bash
set group <name> <config>
edit group
edit TEST-GROUP
```

Add config:

```bash
set system service netconf ssh
```

Show command:

```bash
show | compare
```

Apply it:

```bash
set apply-group TEST-GROUP
```

If you view config it will not display that is because this config is inherited:

```bash
show | display inheritance
```

## Authentication

Create a user:

```bash
set system login user <username> authentication plain-text password
```

Set a class/privilges:

```bash
set system login user <username> class super-user
```

## External Authentication

### Radius Server

```bash
set system raduis-server 10.10.10.10 port 1812 secret <password> source-address x.x.x.x
```

Configuration fallback:

```bash
set system authentication-order [ radius tacpplus passsword ]
```

**NOTE**: JUNIOS will automatically fallback to local user if needed.
