# Performance SLA (Health Checker)



## 12. Performance SLA&#x20;

Performance SLAs (also called **Health Checks**) monitor the quality of WAN links and detect link failures.\
They are critical for **SD-WAN Rules**, since they determine whether a link is available and if traffic should be steered to another path.

If a member fails its SLA threshold, its route is removed from the routing table and traffic is rerouted.

### 1. Introduction

* **Purpose:**
  * Continuously check link health (alive/dead).
  * Measure **latency, jitter, packet loss**.
  * Help SD-WAN rules make intelligent forwarding decisions.
* **SLA Targets:**
  * Define thresholds for acceptable link quality.
  * Example: Latency ≤ 10ms, Jitter ≤ 5ms, Packet loss ≤ 2%.
* **Protocols Available:**
  * **GUI (3 options):** Ping, HTTP, DNS.
  * **CLI (6+ options):** Ping, HTTP, DNS, TCP-echo, UDP-echo, TWAMP.
  * Additional: FTP, TCP-connect.

### 2 Probe Modes

1. **Active Mode**
   * FortiGate sends **continuous probes** to the SLA target (ICMP/HTTP/DNS, etc.).
   * Provides real-time monitoring but uses firewall resources.
2.  **Passive Mode**

    * FortiGate monitors **actual traffic sessions** to SLA destinations.
    * No continuous probe packets are sent.
    * Limitation: If no user traffic exists (e.g., client is offline), SLA cannot detect link issues.

    ```bash
    config system sdwan
        set passive-wan-health-measurement enable
    end
    ```
3. **Prefer Passive Mode**
   * Default to **Passive** monitoring if traffic exists.
   * If no traffic is detected for **3 minutes**, FortiGate switches to **Active probing**.
   * Automatically returns to Passive when traffic resumes.

### 3 Supported Protocols (CLI)

| Protocol    | Description                                                              |
| ----------- | ------------------------------------------------------------------------ |
| ping        | ICMP echo requests/replies to SLA target.                                |
| tcp-echo    | TCP echo packets to port 7 (echo service).                               |
| udp-echo    | UDP echo packets to port 7 (echo service).                               |
| http        | HTTP GET requests to a target server, optional string match in response. |
| dns         | DNS queries (A-record) to configured server.                             |
| twamp       | Two-Way Active Measurement Protocol (RFC 5357) – measures delay/jitter.  |
| tcp-connect | Establish full TCP connection to target, measure RTT.                    |
| ftp         | Connects to FTP server, tests upload/download (active or passive mode).  |

### 4 Link Status Parameters

* **Check Interval:** How often SLA probes are sent. (Default = 500ms)
* **Failures Before Inactive:** Number of failed probes before declaring link down. (Default = 5)
* **Restore After:** Number of successful probes before marking link as active again. (Default = 5)
* Prevents **link flapping**.

### 5 Labs

#### Active Mode Example

* **Setup:**
  * Probes: Ping 8.8.8.8, 1.1.1.1
  * Mode: Active
* **Verification:**
  * `diag sniffer packet any icmp 4` shows continuous pings from WAN1/WAN2.
  * When WAN2 packet loss = 50%, traffic shifts to WAN1.

**CLI Example:**

```bash
config system sdwan
    config health-check
        edit "ping"
            set server "8.8.8.8" "1.1.1.1"
            set protocol ping
            set interval 500
            set failtime 5
            set recoverytime 5
        next
    end
end
```

#### Passive Mode Example

* **Setup:**
  * Probe mode = Passive.
* **Verification:**
  * SLA results are derived from actual traffic sessions.
  * When WAN2 delay=200ms, jitter=200ms, packet loss=90%, SLA triggers failover to WAN1.

#### Prefer Passive Mode Example

* **Setup:**
  * Probe mode = Prefer Passive.
* **Verification:**
  * With no traffic, FortiGate switches to Active probing after 3 minutes.
  * Once traffic resumes, it switches back to Passive.

### 6 Verification & Monitoring

* **GUI:**
  * `Network > SD-WAN > Performance SLAs` (status, thresholds, targets).
  * Color coding (red = failed SLA).
* **CLI:**

```bash
diagnose sys sdwan health-check
diagnose sys sdwan service <id>
```

