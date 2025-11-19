"""
Login System Security Analysis
This program demonstrates an AI-generated login system with security vulnerabilities,
analyzes the risks, and provides a secure version.
"""

import hashlib
import getpass
import os
import json
import re
from typing import Dict, Optional, Tuple, List
from collections import defaultdict

# ============================================================================
# INSECURE VERSION (What an AI might generate without security awareness)
# ============================================================================

def insecure_login_system():
    """
    INSECURE LOGIN SYSTEM - DO NOT USE IN PRODUCTION
    This demonstrates common security vulnerabilities that AI tools might introduce
    """
    print("\n" + "="*60)
    print("INSECURE LOGIN SYSTEM (AI-Generated Example)")
    print("="*60)
    
    # VULNERABILITY 1: Hardcoded credentials
    username = "admin"
    password = "password123"
    
    print("\n--- Attempting Login ---")
    user_input = input("Enter username: ")
    user_pass = input("Enter password: ")
    
    # VULNERABILITY 2: Plain text password comparison
    if user_input == username and user_pass == password:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials!")
        return False


# ============================================================================
# SECURITY ANALYSIS
# ============================================================================

def analyze_security_risks():
    """
    Analyzes the security risks in the insecure login system
    """
    print("\n" + "="*60)
    print("SECURITY RISK ANALYSIS")
    print("="*60)
    
    risks = [
        {
            "risk": "Hardcoded Credentials",
            "severity": "CRITICAL",
            "description": "Credentials are stored directly in the source code",
            "impact": "Anyone with access to source code can see credentials. Credentials cannot be changed without modifying code.",
            "vulnerability_location": "Lines 23-24: username = 'admin', password = 'password123'"
        },
        {
            "risk": "Plain Text Password Storage",
            "severity": "CRITICAL",
            "description": "Passwords are stored and compared in plain text",
            "impact": "Passwords are visible in memory and logs. If database is compromised, all passwords are exposed.",
            "vulnerability_location": "Line 30: Direct string comparison of plain text passwords"
        },
        {
            "risk": "No Password Hashing",
            "severity": "HIGH",
            "description": "No cryptographic hashing is applied to passwords",
            "impact": "Passwords can be easily extracted and reused. No protection against rainbow table attacks.",
            "vulnerability_location": "No hashing mechanism present"
        },
        {
            "risk": "No Rate Limiting",
            "severity": "MEDIUM",
            "description": "No protection against brute force attacks",
            "impact": "Attackers can make unlimited login attempts to guess passwords",
            "vulnerability_location": "No attempt limiting mechanism"
        },
        {
            "risk": "Weak Input Validation",
            "severity": "MEDIUM",
            "description": "No validation or sanitization of user input",
            "impact": "Potential for injection attacks or unexpected behavior",
            "vulnerability_location": "Lines 28-29: Direct use of user input without validation"
        },
        {
            "risk": "No Account Lockout",
            "severity": "MEDIUM",
            "description": "Failed login attempts are not tracked or limited",
            "impact": "Accounts can be targeted with brute force attacks indefinitely",
            "vulnerability_location": "No failed attempt tracking"
        },
        {
            "risk": "Credentials in Source Code",
            "severity": "CRITICAL",
            "description": "Credentials stored in version control",
            "impact": "If code is committed to Git, credentials become part of history permanently",
            "vulnerability_location": "Hardcoded values in source code"
        }
    ]
    
    print("\nDetected Security Risks:")
    print("-" * 60)
    
    for i, risk in enumerate(risks, 1):
        print(f"\n{i}. {risk['risk']} - [{risk['severity']}]")
        print(f"   Description: {risk['description']}")
        print(f"   Impact: {risk['impact']}")
        print(f"   Location: {risk['vulnerability_location']}")
    
    return risks


# ============================================================================
# SECURE VERSION
# ============================================================================

class SecureLoginSystem:
    """
    Secure Login System with best practices
    """
    
    def __init__(self, user_db_file: str = "users.json"):
        """
        Initialize the secure login system
        
        Args:
            user_db_file: Path to JSON file storing user credentials (hashed)
        """
        self.user_db_file = user_db_file
        self.failed_attempts = {}  # Track failed login attempts
        self.max_attempts = 3
        self.lockout_duration = 300  # 5 minutes in seconds
        self.load_user_database()
    
    def hash_password(self, password: str, salt: Optional[bytes] = None) -> Tuple[str, bytes]:
        """
        Hash a password using SHA-256 with salt
        
        Args:
            password: Plain text password
            salt: Optional salt (generated if not provided)
        
        Returns:
            Tuple of (hashed_password_hex, salt_bytes)
        """
        if salt is None:
            salt = os.urandom(32)  # Generate random salt
        
        # Combine password and salt
        password_bytes = password.encode('utf-8')
        salted_password = password_bytes + salt
        
        # Hash the salted password
        hash_object = hashlib.sha256(salted_password)
        hashed_password = hash_object.hexdigest()
        
        return hashed_password, salt
    
    def verify_password(self, password: str, hashed_password: str, salt: bytes) -> bool:
        """
        Verify a password against a stored hash
        
        Args:
            password: Plain text password to verify
            hashed_password: Stored password hash
            salt: Salt used for the stored hash
        
        Returns:
            True if password matches, False otherwise
        """
        computed_hash, _ = self.hash_password(password, salt)
        return computed_hash == hashed_password
    
    def load_user_database(self):
        """
        Load user database from JSON file
        Creates file with default admin user if it doesn't exist
        """
        if os.path.exists(self.user_db_file):
            with open(self.user_db_file, 'r') as f:
                self.users = json.load(f)
        else:
            # Create default admin user (password: SecurePass123!)
            default_password = "SecurePass123!"
            hashed, salt = self.hash_password(default_password)
            self.users = {
                "admin": {
                    "password_hash": hashed,
                    "salt": salt.hex(),  # Store salt as hex string
                    "failed_attempts": 0,
                    "locked_until": None
                }
            }
            self.save_user_database()
            print(f"\n[INFO] Created default admin user with password: {default_password}")
            print("[INFO] Please change this password in production!")
    
    def save_user_database(self):
        """Save user database to JSON file"""
        with open(self.user_db_file, 'w') as f:
            json.dump(self.users, f, indent=2)
    
    def is_account_locked(self, username: str) -> bool:
        """
        Check if account is locked due to too many failed attempts
        
        Args:
            username: Username to check
        
        Returns:
            True if account is locked, False otherwise
        """
        if username not in self.users:
            return False
        
        user = self.users[username]
        if user.get("locked_until") is None:
            return False
        
        # Check if lockout period has expired
        import time
        if time.time() < user["locked_until"]:
            return True
        else:
            # Lockout expired, reset
            user["locked_until"] = None
            user["failed_attempts"] = 0
            self.save_user_database()
            return False
    
    def record_failed_attempt(self, username: str):
        """
        Record a failed login attempt
        
        Args:
            username: Username that failed to login
        """
        import time
        
        if username not in self.users:
            return
        
        user = self.users[username]
        user["failed_attempts"] = user.get("failed_attempts", 0) + 1
        
        if user["failed_attempts"] >= self.max_attempts:
            user["locked_until"] = time.time() + self.lockout_duration
            print(f"\n[SECURITY] Account locked due to {self.max_attempts} failed attempts.")
            print(f"[SECURITY] Account will be unlocked in {self.lockout_duration // 60} minutes.")
        else:
            remaining = self.max_attempts - user["failed_attempts"]
            print(f"\n[WARNING] Invalid credentials. {remaining} attempt(s) remaining.")
        
        self.save_user_database()
    
    def reset_failed_attempts(self, username: str):
        """Reset failed attempts counter after successful login"""
        if username in self.users:
            self.users[username]["failed_attempts"] = 0
            self.users[username]["locked_until"] = None
            self.save_user_database()
    
    def validate_input(self, username: str, password: str) -> Tuple[bool, str]:
        """
        Validate user input
        
        Args:
            username: Username to validate
            password: Password to validate
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not username or not username.strip():
            return False, "Username cannot be empty"
        
        if not password:
            return False, "Password cannot be empty"
        
        if len(username) > 50:
            return False, "Username too long (max 50 characters)"
        
        if len(password) < 8:
            return False, "Password too short (minimum 8 characters)"
        
        if len(password) > 128:
            return False, "Password too long (max 128 characters)"
        
        # Check for potentially dangerous characters
        dangerous_chars = ['<', '>', '"', "'", '&', ';', '|', '`']
        if any(char in username for char in dangerous_chars):
            return False, "Username contains invalid characters"
        
        return True, ""
    
    def login(self, username: str, password: str) -> bool:
        """
        Perform secure login
        
        Args:
            username: Username
            password: Password
        
        Returns:
            True if login successful, False otherwise
        """
        # Validate input
        is_valid, error_msg = self.validate_input(username, password)
        if not is_valid:
            print(f"\n[ERROR] {error_msg}")
            return False
        
        # Check if user exists
        if username not in self.users:
            print("\n[ERROR] Invalid credentials")
            # Don't reveal that user doesn't exist (security through obscurity)
            return False
        
        # Check if account is locked
        if self.is_account_locked(username):
            import time
            user = self.users[username]
            locked_until = user["locked_until"]
            remaining_time = int(locked_until - time.time())
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            print(f"\n[ERROR] Account is locked. Try again in {minutes}m {seconds}s")
            return False
        
        # Verify password
        user = self.users[username]
        salt = bytes.fromhex(user["salt"])
        if self.verify_password(password, user["password_hash"], salt):
            self.reset_failed_attempts(username)
            print("\n[SUCCESS] Login successful!")
            return True
        else:
            self.record_failed_attempt(username)
            return False
    
    def register_user(self, username: str, password: str) -> bool:
        """
        Register a new user (for demonstration purposes)
        
        Args:
            username: Desired username
            password: Desired password
        
        Returns:
            True if registration successful, False otherwise
        """
        is_valid, error_msg = self.validate_input(username, password)
        if not is_valid:
            print(f"\n[ERROR] {error_msg}")
            return False
        
        if username in self.users:
            print("\n[ERROR] Username already exists")
            return False
        
        # Hash password and store
        hashed, salt = self.hash_password(password)
        self.users[username] = {
            "password_hash": hashed,
            "salt": salt.hex(),
            "failed_attempts": 0,
            "locked_until": None
        }
        self.save_user_database()
        print(f"\n[SUCCESS] User '{username}' registered successfully!")
        return True


# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """
    Main program that demonstrates insecure and secure login systems
    """
    print("\n" + "="*60)
    print("LOGIN SYSTEM SECURITY ANALYSIS PROGRAM")
    print("="*60)
    print("\nThis program demonstrates:")
    print("1. An insecure login system (AI-generated example)")
    print("2. Security risk analysis")
    print("3. A secure login system implementation")
    print("="*60)
    
    while True:
        print("\n" + "-"*60)
        print("MENU:")
        print("1. Demonstrate Insecure Login System")
        print("2. View Security Risk Analysis")
        print("3. Try Secure Login System")
        print("4. Register New User (Secure System)")
        print("5. Exit")
        print("-"*60)
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            insecure_login_system()
        
        elif choice == "2":
            analyze_security_risks()
            print("\n" + "="*60)
            print("SECURE PRACTICES IMPLEMENTED:")
            print("="*60)
            print("""
1. Password Hashing: Uses SHA-256 with salt for password storage
2. No Hardcoded Credentials: Credentials stored in external JSON file
3. Input Validation: Validates and sanitizes all user input
4. Rate Limiting: Implements account lockout after failed attempts
5. Secure Storage: Passwords never stored in plain text
6. Salt-based Hashing: Each password uses unique salt
7. Account Lockout: Temporary lockout after multiple failed attempts
8. Error Messages: Generic error messages to prevent user enumeration
            """)
        
        elif choice == "3":
            secure_system = SecureLoginSystem()
            print("\n" + "="*60)
            print("SECURE LOGIN SYSTEM")
            print("="*60)
            username = input("\nEnter username: ").strip()
            # Use getpass to hide password input
            password = getpass.getpass("Enter password: ")
            
            secure_system.login(username, password)
        
        elif choice == "4":
            secure_system = SecureLoginSystem()
            print("\n" + "="*60)
            print("REGISTER NEW USER (Secure System)")
            print("="*60)
            username = input("\nEnter username: ").strip()
            password = getpass.getpass("Enter password: ")
            confirm_password = getpass.getpass("Confirm password: ")
            
            if password != confirm_password:
                print("\n[ERROR] Passwords do not match!")
            else:
                secure_system.register_user(username, password)
        
        elif choice == "5":
            print("\nExiting program. Goodbye!")
            break
        
        else:
            print("\n[ERROR] Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()

