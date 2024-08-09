#!/usr/bin/env python3

import cgi
import smtplib
import sqlite3
import random
import math

# Print HTTP headers
print("Content-Type: text/html\n")

# Get form data
form = cgi.FieldStorage()
username = form.getvalue("usrnm")
email = form.getvalue("email")
password = form.getvalue("password")
cpassword = form.getvalue("cpassword")

# Generate OTP
def generate_otp():
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    otp = ''.join(random.choice(string) for _ in range(6))
    return otp

otp = generate_otp()

# SQLite database connection
db = sqlite3.connect('/path/to/your/database.db')
cursor = db.cursor()

# Insert user data and OTP into database
cursor.execute("""
    INSERT INTO user_data (username, email, password, otp) 
    VALUES (?, ?, ?, ?)
""", (username, email, password, otp))
db.commit()

# Send OTP via email
from_email = "your_email@gmail.com"
app_password = "your_app_password"
to_email = email
subject = "Your OTP Code"
message = f"Your OTP code is {otp}"

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login(from_email, app_password)
    smtp.sendmail(from_email, to_email, f"Subject:{subject}\n\n{message}")

# Close database connection
db.close()

# Redirect to OTP verification page
print('<head><meta http-equiv="refresh" content="0;URL=\'otp.html\'" /></head>')

