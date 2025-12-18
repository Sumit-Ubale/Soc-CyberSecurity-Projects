## 🔍 Findings
During the analysis period, multiple failed SSH login attempts were observed.
Several source IP addresses attempted repeated authentication attempts against
the Ubuntu server. One IP address generated an unusually high number of failed
login events within a short time window, clearly indicating automated
brute-force behavior 🤖. The attack attempts primarily targeted common and
invalid usernames, including `root`.

---

## ⚔️ Attack Analysis
The observed activity was identified as an **SSH brute-force attack** conducted
through network-based authentication attempts 🌐. The attack pattern consisted
of high-frequency failed login attempts originating from the same source IP
address. No successful authentication events were detected during the
investigation, indicating that the attack did not result in account compromise.

---

## 🧭 MITRE ATT&CK Mapping
The detected activity maps to the following MITRE ATT&CK techniques:
- **T1110 – Brute Force**
- **T1021.004 – Remote Services: SSH**

---

## 🚨 Severity and Impact
The incident was assessed as **Medium severity** ⚠️ due to repeated unauthorized
authentication attempts. While no accounts were compromised, continued
brute-force activity could increase the risk of credential exposure if
preventive controls are not properly enforced.

---

## 🛠️ Alert Rule Implementation
An automated detection rule was implemented in **Splunk SIEM** to identify
similar SSH brute-force attempts in near real time ⏱️.

**Alert Configuration:**
- **Alert Name:** SSH Brute Force Attack Detected  
- **Alert Type:** Scheduled  
- **Execution Frequency:** Every 5 minutes  
- **Trigger Condition:** Number of results greater than zero  
- **Severity:** Medium  

This alert enables continuous monitoring and ensures early detection of
SSH brute-force activity 🔔.

---

## 🛡️ Recommendations
To mitigate similar attacks in the future, the following actions are recommended:
- Enforce strong password policies 🔐
- Disable direct root login over SSH 🚫
- Implement SSH key-based authentication 🔑
- Apply rate limiting or account lockout controls ⏳
- Enable Multi-Factor Authentication (MFA) ✅
- Monitor and block malicious IP addresses 🚧

---

## 📝 Conclusion
This project demonstrates a complete **SIEM-based SOC workflow**, including
log ingestion, detection logic creation, alert configuration, and incident
documentation 📊. The investigation highlights the importance of proactive
monitoring and effective alerting to protect systems from
authentication-based attacks.
