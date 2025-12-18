import re
import hashlib
from datetime import datetime

# Common weak passwords list
COMMON_PASSWORDS = [
    "password", "123456", "admin", "qwerty", "letmein", "welcome"
]

LOG_FILE = "password_audit.log"

def hash_password(password):
    """Return SHA-256 hash of the password"""
    return hashlib.sha256(password.encode()).hexdigest()

def log_attempt(password, status):
    """Save password attempt securely in log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    password_hash = hash_password(password)

    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} | {status} | {password_hash}\n")

def check_password_strength(password):
    if not password:
        return False, "Password cannot be empty."

    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if password.lower() in COMMON_PASSWORDS:
        return False, "Password is too common."

    if not re.search(r"[A-Z]", password):
        return False, "Add at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Add at least one lowercase letter."

    if not re.search(r"\d", password):
        return False, "Add at least one number."

    if not re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/]", password):
        return False, "Add at least one special character."

    return True, "Password meets security policy."


# ---------------- MAIN PROGRAM ----------------

print("🔐 Password Policy Enforcer (Audit Enabled)")
print("All attempts are securely logged.\n")

try:
    while True:
        password = input("Enter password: ").strip()

        is_valid, message = check_password_strength(password)

        if is_valid:
            print(f"✅ {message}")
            log_attempt(password, "ACCEPTED")
            break
        else:
            print(f"❌ {message}")
            log_attempt(password, "REJECTED")
            print("Please try again.\n")

except KeyboardInterrupt:
    print("\n⚠️ Program interrupted by user. Exiting safely.")

except Exception as error:
    print(f"🚨 Critical error occurred: {error}")
