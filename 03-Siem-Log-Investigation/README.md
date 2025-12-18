# 🛡️ Basic SIEM Log Investigation – SSH Brute Force Detection

## 📌 Project Overview
This project demonstrates a **real-world SIEM investigation** using **Splunk** to
detect and analyze **SSH brute-force attacks** targeting a Linux system.

Authentication logs from a **live Ubuntu Server** were ingested into Splunk,
where suspicious login behavior was identified, analyzed, and automated
detection was implemented following **SOC best practices**.

---

## 🎯 Objectives
- Monitor Linux authentication logs using SIEM
- Detect SSH brute-force login attempts
- Identify attacker IP addresses and attack patterns
- Create an automated alert for early detection
- Document findings in a SOC-style investigation report

---

## 🛠️ Tools & Technologies
- **SIEM Platform:** Splunk Enterprise
- **Operating System:** Ubuntu Server
- **Log Source:** `/var/log/auth.log`
- **Log Type:** SSH authentication logs

---

## 🔍 Detection Summary
Multiple failed SSH login attempts were detected within short time windows.
Analysis revealed repeated authentication attempts from the same IP addresses,
indicating automated brute-force behavior 🤖.

A rule-based alert was created in Splunk to continuously monitor and detect
similar activity in near real time ⏱️.

---

## 🚨 Alert Details
- **Alert Name:** SSH Brute Force Attack Detected
- **Alert Type:** Scheduled
- **Execution Frequency:** Every 5 minutes
- **Trigger Condition:** Number of results > 0
- **Severity:** Medium ⚠️

This alert ensures early visibility of suspicious authentication activity
and supports proactive incident response.

---

## 🧠 Framework Mapping
The detected activity was mapped to the **MITRE ATT&CK Framework**:
- **T1110 – Brute Force**
- **T1021.004 – Remote Services: SSH**

---

## 📄 Documentation
- **Investigation_Report.md**  
  Contains detailed analysis, findings, detection logic, alert configuration,
  impact assessment, and mitigation recommendations.

- **Screenshots**  
  Evidence of log analysis, detection queries, and alert configuration
  from Splunk SIEM.

---

## 🏁 Conclusion
This project reflects a complete **SOC workflow**, including log ingestion,
threat detection, alert creation, and incident documentation 📊.

It highlights the importance of proactive monitoring and effective SIEM
alerting to protect systems from authentication-based attacks.

---

## 🚀 Skills Demonstrated
- SIEM log analysis
- Detection engineering
- Linux security monitoring
- MITRE ATT&CK mapping
- SOC-style reporting and documentation

---

## 👤 Author
**Sumit Ubale**  
Aspiring SOC Analyst | Cybersecurity Enthusiast  

- Hands-on experience with SIEM (Splunk)
- Linux authentication log analysis
- Detection engineering & alert creation
- MITRE ATT&CK–based threat analysis
