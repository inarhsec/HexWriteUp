# Equal Cost Multi-Path (ECMP)

### 1. What is ECMP?

* **ECMP (Equal Cost Multi-Path)** allows multiple routes to the **same destination** with the **same cost (AD and priority)**.
* FortiGate then **load balances** traffic across these multiple next-hops.
* Considered **after policy routing** (policy routes override ECMP).
* Supported in **Static, OSPF, BGP**.
* Max ECMP paths on FortiGate: **255** (min = 1 disables ECMP).

### 2. How ECMP Works

* FortiGate installs multiple routes in the routing table if:
  * Same **destination**
  * Same **Administrative Distance (AD)**
  * Same **Priority**
* **Default ECMP behavior**: Source IP–based hashing.
* Failover: If one link goes down, FortiGate removes it from the routing table (requires **Link Health Monitor**).

### 3. ECMP Load Balancing Methods

| **Method**               | **Definition**                                                                                                                                 | **Example Config**                                                                                                                                                                    |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Source IP–based**      | <p>Default. Same source IP always uses the same path.<br><br>Inshort session that start at the same source use the same path all the time.</p> | `set v4-ecmp-mode source-ip-based`                                                                                                                                                    |
| **Source–Dest IP–based** | Same source–destination pair always uses the same path.                                                                                        | `set v4-ecmp-mode source-dest-ip-based`                                                                                                                                               |
| **Weight–based**         | Interfaces get weighted. Higher weight → more traffic.                                                                                         | <p><code>&#x3C;br>config router static&#x3C;br>edit 1&#x3C;br>set weight 10&#x3C;br>end&#x3C;br></code><br><code>set v4-ecmp-mode weight-based</code></p>                             |
| **Usage–based**          | An interface is used until its **threshold** is hit, then traffic spills over to another interface.                                            | `<br>config system settings<br>set v4-ecmp-mode usage-based<br>config system interface<br>edit port1<br>set spillover-threshold 5<br>edit port2<br>set spillover-threshold 10<br>end` |

### 4. Route Preference in Static Routing

* **Lower AD (Administrative Distance)** → preferred.
* If AD is equal → **lower priority** wins.
* If both are equal → ECMP load balancing is applied.
* Condition: ECMP requires **same AD + same priority**.

### 5. Primary & Backup Path

* **Example:** Customer wants **TATA 50 Mbps** as primary, **JIO 10 Mbps** as backup.
* Solution:
  * Set **lower AD or priority** for TATA.
  * Set **higher AD or priority** for JIO.
* JIO is used only if TATA fails.
* Recommended: Enable **Link Health Monitor** for proper failover.

### 6. ECMP Lab (Basic)

**Scenario**:

* WAN1 → Gateway `192.168.1.254` (Port1)
* WAN2 → Gateway `192.168.2.254` (Port2)
* Test Server: `8.8.8.8` (Ping)

**Steps**:

1. Configure **two default routes** (same AD & priority).
2. Verify routing table:



```
get router info routing-table static
```

1. Configure firewall policies:
   * LAN → WAN1
   * LAN → WAN2
2. Verify traffic in GUI:
   * **Dashboard → Network → Routing → Static**
   * **Log & Report → Forwarding Traffic**

**Result:**

* By default, ECMP uses **Source IP–based load balancing**.
* Changing to `source-dest-ip-based` will spread sessions across WAN1 & WAN2 based on different destinations.

### 7.Verification Commands

```
Policy Based Route : diagnose firewall proute list

Route Cache : diagnose ip rtcache list

Routing Table (All Active Routes): get router info routing-table all

Routing Table (Active & Inactive Routes): get router info routing-table database

Forwarding Information Base: get router info kernel
```

### 8. ECMP Lab (Load Balancing Methods)

#### Source IP–based

`config system settings`\
`set v4-ecmp-mode source-ip-based`\
`end`

Weight–based

`config system settings`\
`set v4-ecmp-mode weight-based`\
`end`

`config router static`\
`edit 1`\
`set weight 10`\
`next`\
`edit 2`\
`set weight 5`\
`end`

Usage–based

`config system settings`\
`set v4-ecmp-mode usage-based`\
`end`

`config system interface`\
`edit port1`\
`set spillover-threshold 5`\
`next`\
`edit port2`\
`set spillover-threshold 10`\
`end`

Verify usage spillover:

`diagnose netlink dstmac list port1`\
`diagnose netlink dstmac list port2`\
`get system session list`

Source–Dest IP–based

`config system settings`\
`set v4-ecmp-mode source-dest-ip-based`\
`end`

Verification commands:

`diagnose sniffer packet any icmp 4`\
`diagnose sys session clear`

