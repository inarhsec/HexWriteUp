# SD-WAN Rules

SD-WAN rules (also called **services**) control **path selection** in FortiGate. They determine how specific traffic is dynamically steered to the best available link or routed through a selected path.

Rules define:

* The **strategy** FortiGate uses for selecting the outbound interface.
* The **SLA checks** that must be satisfied.
* The **criteria** (source, destination, application, protocol, etc.) for matching traffic.

If no SD-WAN rule matches, the **implicit rule** applies, and traffic is routed using standard routing (ECMP may apply).\
Like **policy routes**, rules are evaluated top to bottom (**first match wins**).

### 1.1 SD-WAN Strategies Overview

FortiGate supports **four SD-WAN strategies** for selecting outgoing interfaces:

1. **Manual**
2. **Best Quality**
3. **Lowest Cost (SLA)**
4. **Maximize Bandwidth (S**

### 1.2 Manual Strategy

* **Description:**
  * No SLA or health checks.
  * Selection is based only on **interface preference**.
  * First available interface is used.
  * If the preferred interface fails, FortiGate moves to the next one.
* **Lab Example**:

```bash
config system sdwan
    config service
        edit 1
            set name "Manual-Rule"
            set dst "all"
            set src "all"
            set priority-members 2 1
        next
    end
# diagnose sys sdwan service 1
```



### 1.3 Best Quality Strategy

* **Description:**
  * Selects the best-performing link based on **SLA metrics**.
  * Default quality threshold = **10%**.
  * Supported criteria:
    * Latency
    * Jitter
    * Packet Loss
    * Bandwidth (Upstream / Downstream / Bi-directional)
    * Custom weighted profile
* **Lab Example**:

```bash
config system sdwan
    config service
        edit 2
            set name "BestQuality"
            set mode priority
            set dst "all"
            set src "all"
            set health-check "ping"
            set link-cost-factor packet-loss
            set priority-members 1 2
        next
    end
# diagnose sys sdwan service 2
```

* **Verification:**
  * SLA monitors (8.8.8.8 / 1.1.1.1).
  * WAN1 is preferred until packet loss exceeds 10%.

### 1.4 Lowest Cost (SLA) Strategy

* **Description:**
  * Chooses the **lowest cost link** that satisfies SLA.
  * If multiple links meet SLA:
    * First compare **cost values**.
    * If costs are equal, use **priority order**.
* **Lab Example**:

```bash
config system sdwan
    config service
        edit 3
            set name "LowestCost"
            set mode sla
            set dst "all"
            set src "all"
            config sla
                edit "ping"
                    set id 1
                next
            end
            set priority-members 2 1
        next
    end
# diagnose sys sdwan service 3
```

* **Verification:**
  * Both WAN1 & WAN2 have cost=0 → WAN2 is preferred (order).
  * Changing WAN2 cost to 5 → WAN1 (cost=0) is preferred.

### 1.5 Maximize Bandwidth (SLA) Strategy

* **Description:**
  * Uses **all SLA-satisfied links simultaneously**.
  * Provides **load balancing** across links.
  * **Cost and priority are ignored**.
  * Supported load balancing algorithms:
    * Round-robin (default)
    * Source-IP based
    * Source-Destination IP based
    * Inbound bandwidth
    * Outbound bandwidth
    * Bi-directional bandwidth
* **Lab Example**:

```bash
config system sdwan
    config service
        edit 4
            set name "MaximizeBW"
            set mode load-balance
            set dst "all"
            set src "all"
            config sla
                edit "ping"
                    set id 1
                next
            end
            set priority-members 1 2
        next
    end
# diagnose sys sdwan service 4
```

* **Verification:**
  * If WAN1 & WAN2 meet SLA → traffic distributed across both.
  * If only one meets SLA → only that link is used.

### 1.6 Verification & Monitoring

* **GUI:**
  * `Network > SD-WAN > Rules` (Hit counts, Interface selection).
  * `Log & Report > Forward Traffic` (Interface usage).
  * `Network > SD-WAN > Performance SLAs` (SLA results).
* **CLI Commands:**

```bash
diagnose sys sdwan service <id>
diagnose sys sdwan health-check
```

