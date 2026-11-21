# SD-WAN Load Balancing Methods



## SD-WAN Load Balancing Methods

SD-WAN load balancing distributes traffic across multiple WAN links, similar to **ECMP** (Equal Cost Multi-Path).

* **Default mode:** **Source IP based**.
* **Default algorithm:** **Round Robin**.
* Load balancing methods are **not applied to user-defined SD-WAN rules**, only to the **implicit SD-WAN rule**.

### Default Behavior

* Works like **ECMP**.
* All active member gateways of the SD-WAN interface are added to the routing table.
* If no explicit SD-WAN rule matches traffic, the **implicit rule** applies.
* Traffic is then balanced according to the configured **load-balance-mode**.

### Load Balancing Algorithms

FortiGate supports the following **load balancing algorithms**:

#### 1. Source IP Based (Default)

* All sessions from the same **source IP** are sent over the same link.
* Ensures session stickiness.
* Traffic is divided equally across members.

**CLI Example**:

```bash
config system sdwan
    set load-balance-mode source-ip-based
end
```

#### 2. Session / Weight Based

* Sessions are distributed according to **weights** assigned to each link.
* Higher weight = more sessions assigned.
* Called **weight-based** in CLI, shown as **Sessions** in GUI.

**CLI Example**:

```bash
config system sdwan
    set load-balance-mode weight-based
    config members
        edit 1
            set weight 80
        next
        edit 2
            set weight 20
        next
    end
end
```

* WAN1 gets \~80% of sessions, WAN2 gets \~20%.

#### 3. Spillover / Usage Based

* All traffic uses the first link until its **spillover threshold** is exceeded.
* New sessions spill over to the next link.
* Threshold can be set for **ingress** and **egress**.

**CLI Example**:

```bash
config system sdwan
    set load-balance-mode usage-based
    config members
        edit 1
            set spillover-threshold 1024
            set ingress-spillover-threshold 1024
        next
    end
end
```

#### 4. Source-Destination IP Based

* Traffic between a **source-destination IP pair** always uses the same link.
* Ensures stickiness for bi-directional flows (like VoIP calls).

**CLI Example**:

```bash
config system sdwan
    set load-balance-mode source-dest-ip-based
end
```

#### 5. Volume / Measured-Volume Based

* Distributes traffic based on **data volume** rather than session count.
* Useful when traffic volumes are uneven but session counts are balanced.

**CLI Example**:

```bash
config system sdwan
    set load-balance-mode measured-volume-based
    config members
        edit 1
            set volume-ratio 80
        next
        edit 2
            set volume-ratio 20
        next
    end
end
```

* WAN1 handles 80% of traffic volume, WAN2 handles 20%.

### &#x20;System Settings & Implicit Rule

* Without SD-WAN:
  * ECMP is controlled using `v4-ecmp-mode` under `config system settings`.
* With SD-WAN:
  * `v4-ecmp-mode` is hidden.
  * ECMP is replaced by `load-balance-mode` under `config system sdwan`.
  * Additional **Volume-based** option is available in SD-WAN mode.
* **Implicit Rule:**
  * If no explicit SD-WAN policy matches, FortiGate uses the **implicit rule**.
  * Traffic follows the **load-balance-mode** configured at SD-WAN level.

### Verification & Testing

* **GUI:**
  * `Network > SD-WAN > Rules` → Default Rule load balancing mode.
  * `Dashboard > FortiView Sessions` → Verify session distribution.
  * `Log & Report > Forward Traffic` → Check outgoing interface usage.
* **CLI Commands:**

```bash
diagnose sys sdwan service <id>
diagnose sys sdwan member
diagnose sniffer packet any icmp 4
get system session list
```

