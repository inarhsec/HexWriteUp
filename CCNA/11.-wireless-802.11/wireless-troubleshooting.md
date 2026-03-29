# Wireless TroubleShooting

**Wireless troubleshooting**

**Problem statements**

1. **User Authentication Failures**
   * **Mitigation**
   * Gathering problem information like
     * User details
     * AD group
     * Time & frequency of the issue
     * Error messages on the end device if any
     * Network IP or MAC details of the end device
     * Authentication method
     * Recent changes
     * Log entries for the affected devices
     * NAD device the user trying to connect
   * Verify whether the problem is affecting a single user exclusively, impacting all users across the board, or if it's isolated to particular types of users.
   * Checking the user credentials
   * Evaluating the authentication logs on the RADIUS server
   * Checking the policy configuration
   * Checking on the identity or DHCP source connectivity
   * Review certificate validity & installation on client device
   * Network connectivity with the RADIUS server
   * Conduct a packet capture that mimics the problem, if feasible, to aid in additional troubleshooting and provide a reference for the TAC engineer.
2. **Guest Network Access Issues**
   * **Mitigation**
   * Verify whether the problem is affecting a single user exclusively, impacting all users across the board, or if it's isolated to particular types of users.
   * DHCP configuration & connectivity
   * Guest portal accessibility
   * Error messages on the end device if any
   * Test the access on different OS or device types
3. **Access point or switch (NAD) connectivity issue**
   * **Mitigation**
   * Checking physical connectivity
   * Verify PoE supply
   * Verify the status of the access point on its central dashboard
   * RADIUS server Integration review
   * RADIUS server config review
   * Capacity/high utilization verification
4. **Coverage issue**
   * **Mitigation**
   * Physical Ekahau passive survey
   * Access point mounting best practice verification

**Logs to be submitted to the TAC engineer at initial engagement**

1. **Aruba Clearpass**
   * Error screenshot from the Live monitoring > Access tracker
   * Configuration screenshot of the affected user’s policies, services & authentication methods
   * show tech-support
   * show license
   * show version
   * show server-status
   * show access-tracker all
   * show aaa server-status
   * show radius statistics
   * show logs
   * show endpoint
   * show certificates
   * show system-resources
2. **WLC**
   * show tech-support wireless
   * show wlan id
   * show wireless client mac-address \<H.H.H> detail
   * show ap summary
   * show aaa server status
3. **Cisco ISE**
   * ISE version details
   * show tech-support
   * show application status ise
   * Show version
   * show application server ise
   * show logging application ise.log level
   * show authentication sessions | include
   * show radius statistics
   * show radius profile
   * show radius summary
4. Client Devices Issue

* **Call Summary:**
* Reported Issue: Some Laptops intermittently not able to connect internet.<br>
* WLC Model:C9800-L-F-K9 | SW version: 17.9.3<br>
* Configuration:<br>

SSID Name: Star Team PC

Policy Profile Name : Star\_Team\_PC

Flex Central Switching                : DISABLED

Flex Central Authentication       : ENABLED

Flex Central DHCP                       : DISABLED

VLAN                              : 102

* cu taken RA trace log during the issue.<br>
* The RA trace logs did not include any evidence for the internet issue.<br>
* During the issue, the client showed that it was connected to Wi-Fi and that it could ping the gateway IP address. However, the internet is not working.<br>
* The following logs are required for further debugging if the issue re-occurs.<br>

**1. AP uplink switch port capture:**

**SPAN** capture – Mirroring the AP connected switch port to any free port on the switch and the free port need to be connected with Laptop with Wireshark app capturing interface.

**2. Client PC Wireshark trace for Wi-Fi interface.**

**3. Logs on AP CLI:**

exec time-out 0

\#config ap client-trace address add < Client MAC address >

\#config ap client-trace filter all enable

\#config ap client-trace output console-log enable

\#config ap client-trace start

\#term mon

\#Debug client

**4. RA trace from WLC GUI:**

Troubleshooting > Radioactive Trace log, add the mac-address of the client, and start the debug.

After seeing the issue, you can stop the debug and generate the trace file.

**Note:** Kindly provide the client internet disconnection timestamp while sharing the logs.
