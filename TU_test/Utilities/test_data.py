"""
Test Data for Login Module
"""

from Utilities.config import Config

# ==========================================
# Valid Credentials
# ==========================================

valid_login = {
    "email": Config.VALID_EMAIL,
    "password": Config.VALID_PASSWORD
}

# ==========================================
# Invalid Credentials
# ==========================================

invalid_password = {
    "email": Config.VALID_EMAIL,
    "password": "WrongPassword@123"
}

invalid_email = {
    "email": "invalid@example.com",
    "password": Config.VALID_PASSWORD
}

invalid_email_password = {
    "email": "invalid@example.com",
    "password": "WrongPassword@123"
}

# ==========================================
# Blank Fields
# ==========================================

blank_email = {
    "email": "",
    "password": Config.VALID_PASSWORD
}

blank_password = {
    "email": Config.VALID_EMAIL,
    "password": ""
}

blank_both = {
    "email": "",
    "password": ""
}

# ==========================================
# Invalid Email Format
# ==========================================

invalid_email_format = {
    "email": "abc123",
    "password": Config.VALID_PASSWORD
}

# ==========================================
# Long Input
# ==========================================

long_email = {
    "email": "a"*250 + "@gmail.com",
    "password": Config.VALID_PASSWORD
}

long_password = {
    "email": Config.VALID_EMAIL,
    "password": "A"*300
}

# ==========================================
# SQL Injection
# ==========================================

sql_email = {
    "email": "' OR '1'='1",
    "password": Config.VALID_PASSWORD
}

sql_password = {
    "email": Config.VALID_EMAIL,
    "password": "' OR '1'='1"
}

# ==========================================
# XSS
# ==========================================

xss_email = {
    "email": "<script>alert(1)</script>",
    "password": Config.VALID_PASSWORD
}

xss_password = {
    "email": Config.VALID_EMAIL,
    "password": "<script>alert(1)</script>"
}