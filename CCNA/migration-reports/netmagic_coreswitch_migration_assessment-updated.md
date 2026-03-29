# Netmagic\_CoreSwitch\_Migration\_Assessment Updated

{% file src="../.gitbook/assets/Netmagic_CoreSwitch_Migration_Assessment Updated (1).docx" %}

**Netmagic-CoreSwitch (CBS SX550X Stack) to Cisco Nexus**\
**Date:** 23-Mar-2026\
**Prepared by:** Hassan\
**Status:** Phase 1 – Assessment Complete

## 1. Device Identity & Hardware Inventory

### 1.1 Switch Identity

| Parameter           | Value                              |
| ------------------- | ---------------------------------- |
| Hostname            | Netmagic-CoreSwitch                |
| Platform            | Cisco CBS SX550X-24 (4-unit stack) |
| Firmware (Active)   | 2.5.9.13 (07-Jun-2022)             |
| Firmware (Inactive) | 2.5.5.47 (06-May-2020)             |
| Stack Units         | 4 x SX550X-24                      |
| Default Gateway     | 172.27.8.31                        |
| Management VLAN IP  | 172.27.8.30/24 (VLAN 1)            |
| Loopback1 IP        | 172.27.7.1/30                      |
| OOB Port            | Down (not used)                    |

### 1.2 Unit Serial Numbers

| Unit   | Model        | VID | Serial Number |
| ------ | ------------ | --- | ------------- |
| Unit 1 | SX550X-24-K9 | V04 | DNI262003G8   |
| Unit 2 | SX550X-24-K9 | V04 | DNI262003PE   |
| Unit 3 | SX550X-24-K9 | V04 | DNI262003PN   |
| Unit 4 | SX550X-24-K9 | V04 | DNI262003HW   |

### 1.3 SFP Transceivers

| Port     | PID         | Type               | VID | Serial Number |
| -------- | ----------- | ------------------ | --- | ------------- |
| te1/0/11 | 10G-Combo-C |                    |     | UP            |
| te1/0/23 | 10G-Combo-C |                    |     | Down          |
| te2/0/11 | 10G-Combo-C |                    |     | UP            |
| te2/0/23 | 10G-Combo-C |                    |     | Down          |
| te3/0/11 | SFP-10G-LR  | Single-mode 10G LR | V02 | ACW2607198R   |
| te3/0/23 | 10G-Combo-C |                    |     | Down          |
| te4/0/11 | SFP-10G-LR  | Single-mode 10G LR | V02 | ACW260903QL   |
| te4/0/23 | 10G-Combo-C |                    |     | Down          |

{% hint style="info" %}
Both SFPs are on Combo-F ports (te3/0/11, te4/0/11) used in Port-Channel 7 to IDC7-SW. Verify Nexus has compatible 10G-LR SFP slots.
{% endhint %}

## 2. CPU & Health Alert

CPU utilization is 100% across 5 seconds, 1 minute, and 5 minutes. The switch was maxed out at time of assessment. This is a serious pre-migration concern.

{% hint style="warning" %}
Action required before migration:

* Run `show processes cpu sorted` to identify top consumers
* Check if any broadcast storm, MAC flooding, or STP topology change is causing CPU spike
* Correlate with syslog for error conditions
* If CPU has been at 100% for extended periods, the switch may already be degraded — migration urgency increases
{% endhint %}

## 3. Port Status Analysis

### 3.1 Port Utilization Summary (from show interfaces status)

| Stack Unit       | Total Ports |   Up |                  Down (Free) | Notes                       |
| ---------------- | ----------: | ---: | ---------------------------: | --------------------------- |
| Unit 1 (te1/0/x) |          23 |   17 |              6 (te1/0/18–23) | te1/0/12 missing (stacking) |
| Unit 2 (te2/0/x) |          22 |   17 |      6 (te2/0/18-23 Combo-C) | te2/0/12 missing (stacking) |
| Unit 3 (te3/0/x) |          23 |   20 | 5 (te3/0/9-10) + te3/0/21-23 | SFP on te3/0/11 active      |
| Unit 4 (te4/0/x) |          23 |   20 | 2 (te4/0/9-10) + te4/0/21-23 | SFP on te4/0/11 active      |
| TOTAL            |          96 | \~74 |              \~14 truly free |                             |

te1/0/1 and te2/0/1 are UP but have NO config (no VLAN, no channel-group) — orphan ports. Clarify before migration.\
te1/0/23 and te2/0/23 are Combo-C, Down, and unconfigured. Check if reserved.

{% hint style="info" %}
Down ports that appear in VLAN 1 untagged member list (te3/0/9, te3/0/10, te3/0/12 etc.) are phantom entries — CBS adds unused ports to default VLAN.
{% endhint %}

### 3.2 Speed Negotiation Issues

Several ports are UP but negotiated at sub-10G speeds, indicating potential cabling or NIC issues:

| Port        | Negotiated Speed | Risk                                 |
| ----------- | ---------------: | ------------------------------------ |
| te1/0/1     |        1000 Mbps | May be intentional or old NIC        |
| te1/0/6     |        1000 Mbps | Broadcom host — check NIC capability |
| te1/0/14    |        1000 Mbps | Access VLAN 14 port                  |
| te1/0/15    |     100 Mbps (!) | CRITICAL — only 100M on a 10G port   |
| te1/0/16    |        1000 Mbps | Access VLAN 14                       |
| te1/0/17    |        1000 Mbps | Access VLAN 14                       |
| te2/0/1     |        1000 Mbps | No config assigned                   |
| te2/0/2     |        1000 Mbps | Part of Po2                          |
| te2/0/6     |        1000 Mbps | Trunk port, native VLAN 11           |
| te2/0/14–17 |        1000 Mbps | Access VLAN 14                       |
| te2/0/15    |     100 Mbps (!) | CRITICAL — 100M on 10G port          |

te1/0/15 and te2/0/15 are running at 100 Mbps. These connect to the same device (mirrored across stack). This is likely a legacy NIC or faulty cable. Resolve BEFORE migration — Nexus won't mask this.

## 4. LLDP Neighbors — Connected Devices

### 4.1 Layer 2 Switches

| Switch Port | Neighbor System Name | Neighbor Port | Type                                        |
| ----------- | -------------------- | ------------- | ------------------------------------------- |
| te1/0/2     | FS1GSW0832           | 1/xg26        | Bridge (FS Network Switch)                  |
| te2/0/2     | FS1GSW0832           | 2/g24         | Bridge (same FS switch, dual-homed via Po2) |

FS1GSW0832 is an FS-brand switch connecting via Po2. It dual-homes to both te1/0/2 and te2/0/2. This is your downlink aggregation switch.

### 4.2 Servers — Units 1 & 2 (Broadcom Dual 10GBase-T)

Ports te1/0/3–11, te2/0/3–11 are all connected to Broadcom Dual 10GBase-T NICs (`fw`: AFW\_214.0.245.0). These are server NICs, each appearing on mirror ports across Unit 1 and Unit 2 — indicating dual-homed server connections via port-channels or active-passive bonding.

### 4.3 Servers — Units 3 & 4 (Broadcom 57454 / NX-E)

| Server Name  | Ports (Unit 3) | Ports (Unit 4) | NIC Model                                        |
| ------------ | -------------- | -------------- | ------------------------------------------------ |
| FSNETNTX1121 | te3/0/1-2      | te4/0/1-2      | Broadcom 57454 OCP + PCIe eth0, eth1, eth4, eth5 |
| FSNETNTX1122 | te3/0/3-4      | te4/0/3-4      | Broadcom 57454 OCP + PCIe eth0, eth1, eth4, eth5 |
| FSNETNTX1123 | te3/0/5-6      | te4/0/5-6      | Broadcom 57454 OCP + PCIe eth0, eth1, eth4, eth5 |
| FSNETNTX1124 | te3/0/7-8      | te4/0/7-8      | Broadcom 57454 OCP + PCIe eth0, eth1, eth4, eth5 |
| FSNETNTX1125 | te3/0/13-14    | te4/0/13-14    | Broadcom 57454 OCP + PCIe eth0, eth1, eth4, eth5 |
| FSNETNTX1126 | te3/0/15-16    | te4/0/15-16    | Broadcom 57454 OCP + PCIe eth0, eth1, eth4, eth5 |
| FSNETNTX1127 | te3/0/17-18    | te4/0/17-18    | Broadcom NX-E + 57454 eth0, eth1, eth6, eth7     |
| FSNETNTX1128 | te3/0/19-20    | te4/0/19-20    | Broadcom NX-E + 57454 eth0, eth1, eth6, eth7     |

FSNETNTX1121–1128 are all dual-homed across Unit 3 and Unit 4. Each server uses 2 ports per unit (one OCP NIC eth0/1, one PCIe NIC). They connect via Po3–Po11. FSNETNTX1127/1128 appear as Bridge+Router (B,R) — these servers may have routing/gateway functions.

### 4.4 Uplink to IDC7-SW

| Switch Port | Neighbor                         | Neighbor Port | Channel | Type            |
| ----------- | -------------------------------- | ------------- | ------- | --------------- |
| te3/0/11    | IDC7-SW (MAC: 48:1b:a4:a5:8f:75) | te2/0/4       | Po7     | Bridge + Router |
| te4/0/11    | IDC7-SW (MAC: 48:1b:a4:a5:8f:75) | te1/0/4       | Po7     | Bridge + Router |

IDC7-SW is the upstream device (described as **Link-DC7** in Po7 config). This is your WAN/DC uplink — treat it as a critical path. Po7 uses the two SFP-10G-LR transceivers.\
Po7 has only 2 members (one SFP per unit). This is your only uplink to IDC7-SW — single point of failure if either SFP fails. Consider if Nexus design should have more uplink redundancy.

## 5. Port-Channel Configuration

### 5.1 Port-Channel Membership & Status

| Port-Channel | Status      | Members                                    | Mode              | Description                              |
| ------------ | ----------- | ------------------------------------------ | ----------------- | ---------------------------------------- |
| Po1          | Not Present | None                                       | —                 | Empty — safe to ignore                   |
| Po2          | Up 10G      | te1/0/2 (Active), te2/0/2 (Non-candidate!) | auto (PAgP)       | Link to FS1GSW0832                       |
| Po3          | Up 10G      | te3/0/1-2, te4/0/1-2                       | auto              | FSNETNTX1121                             |
| Po4          | Up 10G      | te3/0/3-4, te4/0/3-4                       | auto              | FSNETNTX1122                             |
| Po5          | Up 10G      | te3/0/5-6, te4/0/5-6                       | auto              | FSNETNTX1123                             |
| Po6          | Up 10G      | te3/0/7-8, te4/0/7-8                       | auto              | FSNETNTX1124                             |
| Po7          | Up 10G      | te3/0/11, te4/0/11                         | auto              | **Link-DC7** (IDC7-SW uplink via SFP-LR) |
| Po8          | Up 10G      | te3/0/13-14, te4/0/13-14                   | auto              | FSNETNTX1125                             |
| Po9          | Up 10G      | te3/0/15-16, te4/0/15-16                   | auto              | FSNETNTX1126                             |
| Po10         | Up 10G      | te3/0/17-18, te4/0/17-18                   | auto + LACP short | FSNETNTX1127                             |
| Po11         | Up 10G      | te3/0/19-20, te4/0/19-20                   | auto + LACP short | FSNETNTX1128                             |
| Po12–32      | Not Present | None                                       | —                 | All empty                                |

Po2 shows te2/0/2 as 'Non-candidate'. This means the second member is NOT actively forwarding. Po2 is effectively single-link to FS1GSW0832. Investigate before migration — may cause a traffic drop if te1/0/2 fails.\
All port-channels use mode `auto` (PAgP passive). NX-OS does NOT support PAgP. All channels must be converted to LACP (mode active/passive) on Nexus. Verify the far-end devices also support LACP.\
Load balancing method: `src-dst-mac`. On Nexus, default is also `src-dst-mac` for L2, but verify with `port-channel load-balance` on the specific Nexus model.\
Po10 and Po11 use `lacp timeout short` (fast hellos). Replicate this on Nexus: `lacp rate fast` under each member interface.

### 5.2 Server / Trunk / Uplink Port Mapping

**Unit 1 (te1/0/x) — Access & FS switch ports**

| Port     | Role                                             |
| -------- | ------------------------------------------------ |
| te1/0/1  | Orphan — no VLAN, UP 1G                          |
| te1/0/2  | Po2 → FS1GSW0832 (Misconfigured), UP 1G (active) |
| te1/0/3  | Trunk, native V11 → FS switch                    |
| te1/0/4  | Trunk, native V11 → FS switch                    |
| te1/0/5  | Trunk, native V11 → FS switch                    |
| te1/0/6  | Trunk, native V11 → FS switch                    |
| te1/0/7  | Trunk, native V11 → FS switch                    |
| te1/0/8  | Access VLAN 12 Broadcom NIC                      |
| te1/0/9  | Access VLAN 12 Broadcom NIC                      |
| te1/0/10 | Access VLAN 12 Broadcom NIC                      |
| te1/0/11 | Access VLAN 12 Combo-C, 10G                      |
| te1/0/12 | Stacking port (missing)                          |
| te1/0/13 | Access VLAN 12 Broadcom NIC                      |
| te1/0/14 | Access VLAN 14 UP 1G                             |
| te1/0/15 | Access VLAN 14 ONLY 100 Mbps!                    |
| te1/0/16 | Access VLAN 14 UP 1G                             |
| te1/0/17 | Access VLAN 14 UP 1G                             |
| te1/0/18 | Access VLAN 16 Down                              |
| te1/0/19 | Access VLAN 16 Down                              |
| te1/0/20 | Access VLAN 16 Down                              |
| te1/0/21 | Access VLAN 16 Down                              |
| te1/0/22 | Access VLAN 36 UP                                |
| te1/0/23 | Combo-C, Down No config                          |
| te2/0/1  | Palo Alto GW 172.27.8.31 — UP 1G                 |

**Unit 2 (te2/0/x) — Access & FS switch ports**

| Port     | Role                            |
| -------- | ------------------------------- |
| te2/0/2  | Po2 → FS1GSW0832 Non-candidate! |
| te2/0/3  | Trunk, native V11 → FS switch   |
| te2/0/4  | Trunk, native V11 → FS switch   |
| te2/0/5  | Trunk, native V11 → FS switch   |
| te2/0/6  | Trunk, native V11 UP 1G         |
| te2/0/7  | Trunk, native V11 → FS switch   |
| te2/0/8  | Access VLAN 12 Broadcom NIC     |
| te2/0/9  | Access VLAN 12 Broadcom NIC     |
| te2/0/10 | Access VLAN 12 Broadcom NIC     |
| te2/0/11 | Access VLAN 12 Combo-C, 10G     |
| te2/0/12 | Stacking port (missing)         |
| te2/0/13 | Access VLAN 12 Broadcom NIC     |
| te2/0/14 | Access VLAN 14 UP 1G            |
| te2/0/15 | Access VLAN 14 ONLY 100 Mbps!   |
| te2/0/16 | Access VLAN 14 UP 1G            |
| te2/0/17 | Access VLAN 14 UP 1G            |
| te2/0/18 | Access VLAN 16 Down             |
| te2/0/19 | Access VLAN 16 Down             |
| te2/0/20 | Access VLAN 16 Down             |
| te2/0/21 | Access VLAN 16 Down             |
| te2/0/22 | No config Down                  |
| te2/0/23 | Combo-C, Down No config         |

**Unit 3 (te3/0/x) — Access & FS switch ports**

| Port     | Role                             |
| -------- | -------------------------------- |
| te3/0/1  | Po3 → FSNETNTX1121 eth0 (OCP)    |
| te3/0/2  | Po3 → FSNETNTX1121 eth4 (PCIe)   |
| te3/0/3  | Po4 → FSNETNTX1122 eth0 (OCP)    |
| te3/0/4  | Po4 → FSNETNTX1122 eth4 (PCIe)   |
| te3/0/5  | Po5 → FSNETNTX1123 eth0 (OCP)    |
| te3/0/6  | Po5 → FSNETNTX1123 eth4 (PCIe)   |
| te3/0/7  | Po6 → FSNETNTX1124 eth0 (OCP)    |
| te3/0/8  | Po6 → FSNETNTX1124 eth5 (PCIe)   |
| te3/0/9  | Unused Down                      |
| te3/0/10 | Unused Down                      |
| te3/0/11 | Po7 → IDC7-SW SFP-10G-LR fiber   |
| te3/0/12 | Stacking / missing Not in config |
| te3/0/13 | Po8 → FSNETNTX1125 eth0 (OCP)    |
| te3/0/14 | Po8 → FSNETNTX1125 eth5 (PCIe)   |
| te3/0/15 | Po9 → FSNETNTX1126 eth1 (OCP)    |
| te3/0/16 | Po9 → FSNETNTX1126 eth4 (PCIe)   |
| te3/0/17 | Po10 → FSNETNTX1127 eth6 (NX-E)  |
| te3/0/18 | Po10 → FSNETNTX1127 eth1 (57454) |
| te3/0/19 | Po11 → FSNETNTX1128 eth1 (57454) |
| te3/0/20 | Po11 → FSNETNTX1128 eth6 (NX-E)  |
| te3/0/21 | Access VLAN 11 Standalone        |
| te3/0/22 | No config Down                   |
| te3/0/23 | Trunk (standalone) No Po         |

**Unit 4 (te4/0/x) — Redundant mirror of Unit 3 server links**

| Port     | Role                             |
| -------- | -------------------------------- |
| te4/0/1  | Po3 → FSNETNTX1121 eth0 (OCP)    |
| te4/0/2  | Po3 → FSNETNTX1121 eth5 (PCIe)   |
| te4/0/3  | Po4 → FSNETNTX1122 eth1 (OCP)    |
| te4/0/4  | Po4 → FSNETNTX1122 eth5 (PCIe)   |
| te4/0/5  | Po5 → FSNETNTX1123 eth1 (OCP)    |
| te4/0/6  | Po5 → FSNETNTX1123 eth5 (PCIe)   |
| te4/0/7  | Po6 → FSNETNTX1124 eth1 (OCP)    |
| te4/0/8  | Po6 → FSNETNTX1124 eth4 (PCIe)   |
| te4/0/9  | Unused Down                      |
| te4/0/10 | Unused Down                      |
| te4/0/11 | Po7 → IDC7-SW SFP-10G-LR fiber   |
| te4/0/12 | Stacking / missing Not in config |
| te4/0/13 | Po8 → FSNETNTX1125 eth4 (PCIe)   |
| te4/0/14 | Po8 → FSNETNTX1125 eth1 (OCP)    |
| te4/0/15 | Po9 → FSNETNTX1126 eth5 (PCIe)   |
| te4/0/16 | Po9 → FSNETNTX1126 eth0 (OCP)    |
| te4/0/17 | Po10 → FSNETNTX1127 eth0 (57454) |
| te4/0/18 | Po10 → FSNETNTX1127 eth7 (NX-E)  |
| te4/0/19 | Po11 → FSNETNTX1128 eth0 (57454) |
| te4/0/20 | Po11 → FSNETNTX1128 eth7 (NX-E)  |
| te4/0/21 | No config Down                   |
| te4/0/22 | No config Down                   |
| te4/0/23 | Trunk (standalone) No Po         |

### 5.3 Po3–Po11 Architecture (Server Dual-Homing)

Each server (FSNETNTX1121–1128) has 4 ports connected — 2 per stack unit, forming a 4-port channel. This is a cross-stack (cross-unit) port-channel, which is the CBS stack's equivalent of vPC.\
On Nexus, this cross-stack model must be redesigned. If deploying a single Nexus switch, the 4 ports become a standard port-channel. If deploying dual Nexus, use vPC — redesign required.

## 6. VLAN Database

### 6.1 Configured VLANs

| VLAN ID         | SVI IP Address    | IPv6 Enabled                  | Notes                                                         |
| --------------- | ----------------- | ----------------------------- | ------------------------------------------------------------- |
| 1 (Native/Mgmt) | 172.27.8.30/24    | Yes (2401:8800:c13:2::82/126) | Management VLAN                                               |
| 10              | 172.27.10.1/24    | No                            |                                                               |
| 11              | 172.27.11.1/24    | No                            | Used as native VLAN on uplinks te1/0/3-7, te2/0/3-7           |
| 12              | 172.27.12.1/24    | No                            | Access ports te1/0/8-11,13, te2/0/8-11,13; also on Po10,11,13 |
| 13              | 172.27.13.1/24    | Yes (2401:8800:c13:2::85/126) | Syslog/NTP/SNMP server subnet                                 |
| 14              | 172.27.14.1/24    | No                            | Access ports te1/0/14-17, te2/0/14-17                         |
| 15              | 172.27.15.1/24    | No                            | Trunked, no access ports assigned                             |
| 16              | 172.27.16.1/24    | No                            | Access ports te1/0/18-21, te2/0/18-21                         |
| 17–19           | 172.27.17-19.1/24 | No                            | Trunked only                                                  |
| 20              | 172.27.20.1/24    | No                            |                                                               |
| 21              | 172.27.21.1/24    | No                            | te3/0/21 is untagged VLAN 11 access (not 21)                  |
| 22–35           | 172.27.22-35.1/24 | No (23,27 have IPv6 enabled)  |                                                               |
| 36              | 172.27.36.1/24    | No                            | te1/0/22 is access VLAN 36                                    |
| 37              | 172.27.37.1/24    | Yes (2401:8800:c13:2::91/124) |                                                               |
| 38              | 172.27.38.1/24    | No                            |                                                               |
| 39              | 172.27.39.1/24    | No                            |                                                               |
| 45              | No SVI (L2 only)  | No                            | Trunked; no IP — L2-only VLAN                                 |

Total: 31 VLANs (VLAN 10–39 plus 45). All SVIs use /24 subnets in the 172.27.x.0/24 space.\
VLAN 1 is the management VLAN with IP — this is a security risk. Plan to migrate management to a dedicated VLAN on Nexus. VLAN 1 should be pruned from all trunks on Nexus.\
VLANs 15, 17–20, 24, 26, 28–31, 33, 35, 38 have SVIs with IPs but NO access ports. Verify these are in use via routing or trunked to downstream devices — otherwise candidates for cleanup.

## 7. Interface Configuration Mapping

### 7.1 Trunk Ports — Units 1 & 2 (te1/0/3–7, te2/0/3–7)

10 trunk ports (5 per unit) carrying all VLANs. Native VLAN = 11. These connect to the FS1GSW0832 switch (which in turn connects servers on U1/U2 via LLDP). Not in any port-channel.\
These 10 trunks to the same downstream switch are NOT bundled into port-channels. This is unusual and may create STP issues (multiple active trunks to same switch). Verify FS1GSW0832 side config. On Nexus, these should likely be bundled or properly pruned.

### 7.2 Access Port Summary

| VLAN               | Ports (Unit 1)              | Ports (Unit 2)              |           Count |
| ------------------ | --------------------------- | --------------------------- | --------------: |
| VLAN 11 (untagged) | te1/0/3-7 (native on trunk) | te2/0/3-7 (native on trunk) | 10 trunk native |
| VLAN 12            | te1/0/8-11, te1/0/13        | te2/0/8-11, te2/0/13        |        10 ports |
| VLAN 14            | te1/0/14-17                 | te2/0/14-17                 |         8 ports |
| VLAN 16            | te1/0/18-21                 | te2/0/18-21                 |         8 ports |
| VLAN 36            | te1/0/22                    | —                           |          1 port |
| VLAN 11 access     | —                           | te3/0/21 (Unit 3)           |          1 port |

### 7.3 Notable Unconfigured Ports

\| Port | Status | Issue | |---|---|---|---| | te1/0/1 | UP, 1G | No VLAN, no channel-group, no description — orphan | | te2/0/1 | UP, 1G | Same as te1/0/1 — orphan | | te1/0/23 | Down, Combo-C | No config — likely unused SFP combo slot | | te2/0/23 | Down, Combo-C | No config — likely unused | | te3/0/22 | Down | No config | | te4/0/22 | Down | No config |

## 8. Spanning Tree

STP mode: Rapid-PVST (rapid-pvst) — good, this translates directly to Nexus Rapid-PVST.\
STP priority: 4096 — this switch is the Root Bridge for all VLANs. Must preserve this on Nexus.

{% hint style="warning" %}
With STP priority 4096, this switch is the root for ALL VLANs. Nexus default priority is 32768. If Nexus is not explicitly configured with 4096, another device will win root election during cutover — causing a topology reconvergence and potential traffic blackhole.
{% endhint %}

{% hint style="info" %}
NX-OS command to set root: `spanning-tree vlan 1-39,45 priority 4096` or use `spanning-tree vlan X root primary`
{% endhint %}

## 9. Routing & Layer 3

### 9.1 IP Routing

The switch is acting as a Layer 3 switch (has SVIs for 31 VLANs). No explicit `ip routing` command found in CBS config — CBS enables routing implicitly when SVIs are assigned IPs.

{% hint style="info" %}
On NX-OS, you must explicitly enable `feature interface-vlan` and `ip routing` for SVI routing to work.
{% endhint %}

### 9.2 Default Gateway

\| Type | Address | Note | |---|---|---|---| | IPv4 Default Gateway | 172.27.8.31 | Upstream router — must be reachable on VLAN 1 or management VLAN on Nexus | | IPv6 Default Gateway | 2401:8800:c13:2::81 (VLAN 1) | IPv6 upstream | | Loopback1 IP | 172.27.7.1/30 | Used as SNTP source interface — replicate on Nexus |

No OSPF, BGP, or MPLS config found in this CBS switch. It is purely a Layer 3 access/distribution switch with static default routing. Confirm with upstream router (172.27.8.31) if any routing protocols need to be enabled on Nexus.

### 9.3 IPv6 Config

IPv6 is selectively enabled on VLANs 1, 13, 23, 27, 37. The /126 and /124 prefixes are from 2401:8800:c13:2::/64 range.

| VLAN    | IPv6 Address                      |
| ------- | --------------------------------- |
| VLAN 1  | 2401:8800:c13:2::82/126           |
| VLAN 13 | 2401:8800:c13:2::85/126           |
| VLAN 37 | 2401:8800:c13:2::91/124           |
| VLAN 23 | ipv6 enable (no explicit address) |
| VLAN 27 | ipv6 enable (no explicit address) |

{% hint style="info" %}
On NX-OS: use `ipv6 address ...` under each SVI. `ipv6 enable` without address enables link-local only — replicate as-is.
{% endhint %}

## 10. Management Plane

### 10.1 AAA / Users

RADIUS server config contains PLAINTEXT credentials in the config (radius server user commands with passwords visible). These must NOT be replicated in plaintext on Nexus. Use encrypted form or TACACS+.

| Username     | Privilege | Auth Method                 | Note                                     |
| ------------ | --------: | --------------------------- | ---------------------------------------- |
| cnfmgr       |        15 | Local (encrypted)           | Migrate to Nexus local user              |
| fsnetrw      |        15 | Local (encrypted)           | Migrate to Nexus local user              |
| nikhil.k     |        15 | Local (encrypted)           | Migrate                                  |
| ajinkya.b    |        15 | Local (encrypted)           | Migrate                                  |
| nikhil.kadam |        15 | RADIUS group 'Router Users' | Plain password in config — SECURITY RISK |
| yogesh.yerum |        15 | RADIUS group 'Router Users' | Plain password in config — SECURITY RISK |

### 10.2 SNMP

| Parameter        | Value                                     |
| ---------------- | ----------------------------------------- |
| SNMP Server      | Enabled                                   |
| Location         | Netmagic Datacenter                       |
| Contact          | Nikhil Kadam                              |
| Community        | FSNET (read-only)                         |
| Allowed Managers | 172.27.13.14, 172.27.13.19, 172.27.13.191 |
| View             | Default                                   |

{% hint style="info" %}
On Nexus: `feature snmp`, then replicate community and allowed hosts. Consider upgrading to SNMPv3 on Nexus.
{% endhint %}

### 10.3 Syslog

| Parameter       | Value                         |
| --------------- | ----------------------------- |
| Syslog Host 1   | 172.27.13.13                  |
| Syslog Host 2   | 172.27.13.14                  |
| Syslog Host 3   | 172.27.13.29                  |
| Buffer          | 500 messages, level debugging |
| Console logging | Critical only                 |

### 10.4 NTP / SNTP

| Parameter        | Value                  |
| ---------------- | ---------------------- |
| NTP Server 1     | 172.27.13.11           |
| NTP Server 2     | 172.27.13.12           |
| Source Interface | Loopback1 (172.27.7.1) |
| Timezone         | IN +5:30 (IST)         |

{% hint style="info" %}
CBS uses `sntp`; NX-OS uses `ntp`. Syntax changes: `ntp server 172.27.13.11 use-vrf management` on Nexus. Loopback source: `ntp source-interface loopback0`.
{% endhint %}

### 10.5 SSH & HTTP

SSH server is enabled — replicate on Nexus with `feature ssh`.\
HTTP server is DISABLED (no `ip http server`) — good security posture. Keep it disabled on Nexus.

{% hint style="info" %}
Exec timeout is 5 minutes on console, SSH, and telnet. Telnet is configured — consider disabling telnet on Nexus (use SSH only).
{% endhint %}

### 10.6 Security Banner

Login and exec banners are configured: `AUTHORIZED ACCESS ONLY / DISCONNECT ASAP IF YOU ARE NOT AUTHORISED / ACCESS MONITORED AND RECORDED`. Replicate on Nexus.

## 11. Security Config

| Feature                     | Current Status                | Nexus Action                                            |
| --------------------------- | ----------------------------- | ------------------------------------------------------- |
| CDP                         | Disabled (no cdp run)         | Keep disabled or enable selectively on Nexus            |
| Voice VLAN                  | Auto-triggered with OUI table | Re-evaluate need on Nexus                               |
| SYN Protection              | Mode: Report                  | Nexus has IP Source Guard / CoPP — replicate intent     |
| SSD (Secure Sensitive Data) | Enabled with passphrase       | Not applicable on Nexus — manage credentials separately |
| Port Security               | Not configured                | Opportunity to add on Nexus                             |
| 802.1X                      | Not configured                | Opportunity to add on Nexus                             |
| DHCP Snooping               | Not found in config           | Add on Nexus for server VLANs                           |
| ARP Inspection              | Not found in config           | Add on Nexus                                            |
| ACLs                        | Not found in config           | Opportunity to add on Nexus                             |

## 12. Feature Gap — CBS SX550X vs NX-OS

| Feature               | CBS SX550X            | Cisco NX-OS                                        | Action Required                     |
| --------------------- | --------------------- | -------------------------------------------------- | ----------------------------------- |
| Port-channel protocol | PAgP (mode auto)      | LACP only                                          | Change all to LACP — verify far end |
| STP mode              | Rapid-PVST            | Rapid-PVST / MST                                   | Direct migration, set priority 4096 |
| SNTP                  | sntp server           | ntp server                                         | Syntax change                       |
| IP routing            | Implicit              | Explicit (`ip routing` + `feature interface-vlan`) | Must configure explicitly           |
| Interface naming      | te1/0/1               | Ethernet1/1                                        | Full renaming needed                |
| Port-channel naming   | Po1                   | port-channel1                                      | Rename in configs                   |
| VRF                   | Not used              | vrf context                                        | Not needed unless multi-VRF planned |
| HSRP/VRRP             | Not configured        | Can use anycast GW with vPC                        | Plan if dual-Nexus                  |
| Stacking              | CBS stack (te1–4)     | vPC (if dual switch) or single chassis             | Architecture decision               |
| SSD                   | Cisco CBS specific    | Not applicable                                     | Remove from migration scope         |
| Voice VLAN OUI        | Supported             | Not natively same                                  | Re-evaluate VoIP design             |
| IPv6 enable           | ipv6 enable under SVI | ipv6 enable under SVI                              | Direct translation                  |
| RADIUS plaintext user | radius server user    | Not recommended                                    | Remove, use TACACS+ or local        |

## 13. Missing Data — Collect Before Migration

The following were not captured in this session and must be collected:

|  # | Missing Command / Data          | Why Needed                                                    |
| -: | ------------------------------- | ------------------------------------------------------------- |
|  1 | show spanning-tree detail       | Confirm root bridge, port roles, topology                     |
|  2 | show interfaces counters errors | Pre-migration baseline — CRC, drops, resets                   |
|  3 | show logging                    | Check recent errors, flaps, STP TCN events                    |
|  4 | show processes cpu sorted       | Identify cause of 100% CPU                                    |
|  5 | show mac address-table          | MAC count per VLAN — sizing for Nexus CAM table               |
|  6 | show ip route                   | Confirm routing table — static routes or dynamic              |
|  7 | show ip arp                     | ARP table — identify all active L3 endpoints                  |
|  8 | show interfaces counters        | Traffic baseline per port before migration                    |
|  9 | show environment all            | Fan, temperature, power supply health                         |
| 10 | show lacp neighbor detail       | Verify LACP state on Po10/Po11                                |
| 11 | FS1GSW0832 config               | Understand downlink switch before cutting Po2                 |
| 12 | IDC7-SW config                  | Understand uplink switch before cutting Po7 (critical uplink) |

## 14. Critical Risks Summary

|  # | Risk                                                      | Severity | Action                                 |
| -: | --------------------------------------------------------- | -------- | -------------------------------------- |
|  1 | CPU at 100% — switch may be unstable                      | CRITICAL | Diagnose before migration              |
|  2 | Po2 has non-candidate member — single link to FS switch   | HIGH     | Investigate and fix                    |
|  3 | PAgP used — Nexus only supports LACP                      | HIGH     | Convert all channels to LACP           |
|  4 | te1/0/15 & te2/0/15 running at 100 Mbps on 10G ports      | HIGH     | Fix cable/NIC before migration         |
|  5 | STP root priority 4096 — must be set on Nexus immediately | HIGH     | Set priority before any trunk comes up |
|  6 | VLAN 1 used as management with IP — security risk         | MEDIUM   | Plan management VLAN migration         |
|  7 | Plaintext RADIUS passwords in running config              | MEDIUM   | Remove, use encrypted auth             |
|  8 | No DHCP snooping or ARP inspection                        | MEDIUM   | Add on Nexus as security hardening     |
|  9 | Po7 is only uplink to IDC7-SW — single path               | HIGH     | Plan redundant uplink on Nexus         |
| 10 | IP routing implicit on CBS — must be explicit on NX-OS    | HIGH     | Must not forget or SVIs won't route    |
| 11 | 10 unbundled trunks to FS switch may cause STP issues     | MEDIUM   | Audit and bundle or prune              |

## 15. Recommended Nexus Migration In the Separate Configuration
