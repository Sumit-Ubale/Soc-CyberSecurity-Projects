# Phishing Email Analysis – Sample 2 (Microsoft Impersonation)

## 📌 Overview
This report analyzes a phishing email impersonating Microsoft Support.
The email attempts to trick users into updating their password by
creating urgency and redirecting them to a malicious-looking login page.

---

## 📧 Email Details
- **From:** Microsoft Support <support@m1crosoft-security.com>
- **Subject:** Action Required: Password Expiry Notice
- **Attack Type:** Phishing (Credential Harvesting)

---

## 🚩 Identified Red Flags
- Misspelled sender domain (`m1crosoft` instead of `microsoft`)
- Sender domain not associated with official Microsoft infrastructure
- Urgency-based language (“Action Required”, “expire today”)
- Suspicious external login URL
- Generic sign-off (“Microsoft Security Team”)

---

## 🔗 URL & Domain Analysis

### 🔍 VirusTotal Analysis
- **Tool Used:** VirusTotal
- **URL Checked:** `http://login-microsoft.verify-account[.]net`
- **Result:** 7/98 security vendors flagged the URL as malicious
- **Detection Type:** Phishing / Malicious
- **Analyst Note:**  
  Multiple security vendors identified this URL as phishing,
  confirming malicious intent and credential harvesting behavior.

### 🌐 MXToolbox Analysis
- **Tool Used:** MXToolbox SuperTool
- **Domain Checked:** `login-microsoft.verify-account.net`
- **Result:** HTTP Connect failed – domain could not be resolved
- **Analyst Note:**  
  Phishing campaigns often use short-lived or disposable domains.
  Legitimate Microsoft login services use stable domains such as
  `login.microsoftonline.com`.

---

## 🧠 Analyst Assessment
This email demonstrates clear phishing behavior through brand
impersonation, deceptive domain usage, and urgency tactics. Combined
results from VirusTotal and MXToolbox strongly confirm this as a phishing
attempt.

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
`screenshots/` directory.
