# MILTECH Techaya Switch — DHCP Troubleshooting Field Guide

**Offline reference — ping works, DHCP doesn't**

---

## 0. IMMEDIATE FALLBACK — Get devices talking right now, no DHCP needed

Since ping already works, IP routing between your devices is fine. You can bypass DHCP entirely by assigning static IPs manually.

**Step 1 — Find a valid address range.** On a device that _can_ currently ping others, run one of:

- Windows: `ipconfig /all` and `route print`
- Linux/Mac: `ip addr` and `ip route` (or `route -n`)

Note the subnet (e.g. `192.168.105.x /24`) and the default gateway address.

**Step 2 — Assign static IPs to the devices that fail DHCP.** Pick an unused address in the same subnet as the gateway you found, and set the same subnet mask and gateway.

- **Windows:** Control Panel → Network → Adapter Properties → IPv4 → "Use the following IP address." Enter IP, subnet mask, gateway. DNS can be left blank or set to the gateway.
- **Windows (CLI, faster):**
    
    ```
    netsh interface ip set address "Ethernet" static 192.168.105.50 255.255.255.0 192.168.105.1
    ```
    
- **Linux:**
    
    ```
    sudo ip addr add 192.168.105.50/24 dev eth0sudo ip route add default via 192.168.105.1
    ```
    

Give every device that needs to talk to each other an address in the **same** subnet/VLAN if possible. This sidesteps the DHCP/VLAN issue completely and is the most reliable option if you're short on time.

---

## 1. Identify your exact model

Check the chassis label/engraving. The MILTECH family varies significantly by model:

|Model|Type|Notes|
|---|---|---|
|MILTECH 304 / 308|Basic switch, 8x 10/100|Limited/no IP management on some variants|
|MILTECH 908|8-port managed L2|DHCP relay/option 82 is an **optional** feature, only on part number 1-908-101|
|MILTECH 9012 / 9012C / 9012C/G|12-port managed L2/L3 switch + internal SBC running Linux + Cisco IOS router|Full router-on-a-stick topology, see below|
|MILTECH 9022|12x copper + 4x fiber, L3 managed|Static/RIPv1/v2/OSPF routing|
|MILTECH 9028|12-port, IP67|Managed L2/L3|

If you can't find a label, the **default management IP `192.168.1.111` (mask `255.255.255.0`)** is common across most managed variants — try that first.

---

## 2. Default management access

|Access method|Setting|
|---|---|
|Web / Telnet|`192.168.1.111` / `255.255.255.0` (switch management)|
|Serial (switch side)|Connect to physical Port #1, RS-232, **115200 baud, 8 data bits, No parity, 1 stop bit, No flow control**|
|Switch login|Username: `admin`, Password: _(blank — just press Enter)_|
|Secondary switch IP (9012C/G only, for SBC reachability)|`192.168.101.254` / `255.255.255.0`|
|SBC (Linux) login (9012C/G only)|Username: `root`, Password: `123456`|
|Cisco router CLI access (9012C/G only)|From Linux prompt type `cisco`, press Enter, then `enable`, password `cisco`|

If `admin` with a blank password doesn't work, the unit may have been previously configured with a custom password — in that case the static-IP fallback in Section 0 is your best bet without a factory reset.

---

## 3. Root cause: why ping works but DHCP doesn't (VLAN-per-port design)

On the managed 9012-family units, **each physical port ships on its own separate VLAN by default**:

```
Port 1  = VLAN 1   (gateway 192.168.101.1)
Port 2  = VLAN 2   (gateway 192.168.102.1)
Port 3  = VLAN 3   (gateway 192.168.103.1)
...
Port 11 = VLAN 11  (gateway 192.168.111.1)
Port 12 = Trunk to internal router/SBC (carries all VLANs)
```

An internal router (Cisco IOS on the SBC) routes **unicast** traffic between these VLANs — which is why ping across ports/VLANs works. But DHCP relies on **broadcast** traffic, which does not cross VLAN boundaries by itself. If your DHCP server is on a different port/VLAN than the client that's failing, the DHCP broadcast simply never reaches it — even though the router would happily route a ping between them.

**Fix, if you have management access:** configure a DHCP relay (Cisco term: `ip helper-address`) on the router subinterface for the client's VLAN, pointing at the DHCP server's real IP address:

```
interface Ethernet0/0.3          ! example: VLAN 3 (Port 3)
 ip helper-address 192.168.105.10  ! real IP of your DHCP server
```

Do this for every VLAN/port that needs DHCP from a server sitting on a different port.

**Fix, if you don't have time/access to configure this:** physically move the DHCP server and the affected client onto the same port group/VLAN, or just use the static-IP fallback in Section 0.

---

## 4. Quick diagnostic checklist

1. **Confirm it's really DHCP failing.** Check the device's address — `169.254.x.x` (Windows/most OSes) confirms DHCP timed out and the device self-assigned. No address at all, or an old static one, means something different is going on.
2. **Check which physical ports** the DHCP server and the failing client are plugged into.
3. **If on different ports** → almost certainly the VLAN/relay issue above.
4. **If on the same port/VLAN and still failing**, check for:
    - DHCP snooping enabled with the server's port marked "untrusted"
    - Spanning-tree port stuck in blocking/listening state (wait 30-60s after plugging in, or check port status)
    - Broadcast storm control throttling DHCP broadcasts
    - A port administratively shut down in the switch config
    - An ACL or firewall rule blocking UDP ports 67/68
5. **Hardware-level** (no config access needed):
    - Check the per-port Link/Activity LED — solid/flashing = physical link is up
    - Swap the cable and/or try a different port
    - Power-cycle in order: DHCP server device → switch → end devices, ~30 sec between each

---

## 5. Hard reset (last resort, 9012C/G only)

There's a physical reset function on Port #3:

- **Momentary** contact between Reset pin (M) and GND (L): graceful shutdown of the whole unit (switch + SBC). A second momentary contact powers it back up.
- **Holding for over 3 seconds**: forces a hard shutdown of switch and SBC. You'll need to disconnect and reconnect power afterward to bring it back up.

This does **not** reset configuration to factory defaults by itself — it's a power-cycle mechanism, not a config wipe. Use it if the unit is unresponsive, not as a way to clear settings.

---

## Summary — fastest path under time pressure

1. Try static IPs (Section 0) to get connectivity working immediately, regardless of root cause.
2. If you have a few minutes, log into management (Section 2) and check port-to-VLAN mapping (Section 3) — that's the most likely cause given the symptom.
3. If access fails or there's no time, keep DHCP server and critical clients on the same physical port/VLAN group as a structural workaround.