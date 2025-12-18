# Phishing Email Analysis – Sample 1 (Bank Impersonation)

## 📌 Overview
This report documents the analysis of a phishing email that impersonates
a banking institution (SBI). The email attempts to create urgency and
trick the recipient into clicking a suspicious link to "verify" their
account details.

---

## 📧 Email Summary
- **Impersonated Brand:** State Bank of India (SBI)
- **Attack Type:** Phishing (Credential Harvesting)
- **Delivery Method:** Email
- **User Action Requested:** Click a link and verify account

---

## 🚩 Identified Red Flags
- Fake sender domain not associated with SBI
- Use of urgency and fear-based language
- Generic greeting (“Dear Customer”)
- Suspicious URL with multiple subdomains
- Uncommon country TLD (.ru) for an Indian bank

---

## 🔗 URL & Domain Analysis

### 🔍 VirusTotal Analysis
- **Tool Used:** VirusTotal
- **URL Checked:** `http://sbi-secure-login.verify-user.ru`
- **Result:** 0/98 security vendors flagged the URL
- **Analyst Note:**  
  VirusTotal is reputation-based. A clean result does not confirm
  legitimacy, especially for newly created or short-lived phishing URLs.

### 🌐 MXToolbox Analysis
- **Tool Used:** MXToolbox SuperTool
- **Domain Checked:** `sbi-secure-login.verify-user.ru`
- **Result:** HTTP Connect failed – domain could not be resolved
- **Analyst Note:**  
  Phishing campaigns often use temporary or disposable domains.
  Legitimate banking domains maintain stable and resolvable DNS records.

---

## 🧠 Analyst Assessment
Despite no detections from automated tools, multiple contextual indicators
confirm this email as a phishing attempt. Domain structure, brand
impersonation, and social engineering techniques strongly suggest
malicious intent.

---

## 🛡️ MITRE ATT&CK Mapping
- **T1566** – Phishing  
- **T1566.002** – Spearphishing Link  

---

## ✅ Final Verdict
🚨 **Confirmed Phishing Email**

---

## 📸 Supporting Evidence
Screenshots from VirusTotal and MXToolbox analysis are available in the
`screenshots/` directory for reference.
