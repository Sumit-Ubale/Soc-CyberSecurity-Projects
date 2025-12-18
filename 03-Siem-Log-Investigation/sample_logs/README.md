# Sample Logs Overview

This project analyzes authentication logs generated from a **live Ubuntu Server**
and ingested into **Splunk SIEM** for security monitoring and investigation.

## Log Source
- **File:** `/var/log/auth.log`
- **Operating System:** Ubuntu Server

## Log Type
- SSH authentication events
- Failed login attempts
- Unauthorized access attempts

## Log Ingestion
- Logs were forwarded in real time from the Ubuntu server to Splunk
- Analysis was performed using Splunk Search & Reporting

## Security Note
Raw authentication logs are **intentionally not included** in this repository
to avoid exposing sensitive system and user information.

Instead, this project demonstrates:
- Detection logic using Splunk SPL queries
- Alert rule creation for SSH brute-force attacks
- Investigation evidence through screenshots

This approach follows **real-world SOC best practices** for handling sensitive log data.
