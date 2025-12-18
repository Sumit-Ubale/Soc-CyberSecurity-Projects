# 🔐 Password Policy Enforcer

The **Password Policy Enforcer** is a Python-based security tool designed to validate password strength and enforce basic yet effective password security rules.

This project helps identify and prevent the use of weak passwords that can lead to attacks such as **brute-force attacks, credential stuffing, and unauthorized access**.

---

## 🚀 Features

- Minimum password length enforcement
- Uppercase and lowercase letter validation
- Numeric character requirement
- Special character validation
- Detection of common weak passwords
- User-friendly validation feedback
- Continuous input loop until a strong password is provided
- Secure audit logging using SHA-256 hashing
- Error handling and safe program termination

---

## 🛡️ Security Approach

- Passwords are **never stored in plaintext**
- All password attempts are logged securely using **SHA-256 hashing**
- An audit log is maintained for monitoring accepted and rejected attempts
- Sensitive log files are excluded from version control using `.gitignore`

This approach follows **secure coding and defensive security best practices** commonly used in real-world applications.

---

## 🧠 SOC Perspective

From a **Security Operations Center (SOC)** point of view, password policy enforcement is a critical preventive control.  
This project demonstrates:

- Defensive security mindset
- Secure credential handling
- Input validation and error detection
- Audit trail creation for investigation and monitoring

Such controls are often reviewed during **security assessments, incident investigations, and compliance checks**.

---

## 🛠️ Technologies Used

- Python
- Regular Expressions (Regex)
- SHA-256 Hashing
- File Handling
- Error & Exception Handling

---

## 📌 Use Cases

- Login and signup systems
- Admin panels
- Security awareness demonstrations
- Beginner SOC and cybersecurity projects
- Secure coding practice

---

## 📄 Note

Audit log files may contain sensitive information and are intentionally excluded from this repository to follow security best practices.

---

## 👤 Author

**Sumit Ubale**  
Cybersecurity Student | SOC & VAPT Enthusiast
