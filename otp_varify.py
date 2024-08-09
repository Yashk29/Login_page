#!/usr/bin/env python3

import cgi
import sqlite3

# Print HTTP headers
print("Content-Type: text/html\n")

# Get form data
form = cgi.FieldStorage()
email = form.getvalue("remail")
otp = form.getvalue("OTP")

# SQLite database connection
db = sqlite3.connect('/path/to/your/database.db')
cursor = db.cursor()

# Update OTP in database (or you might want to check it instead)
cursor.execute("UPDATE user_data SET user_otp = ? WHERE email = ?", (otp, email))
db.commit()

# Close database connection
db.close()

# Redirect to next page
print('<head><meta http-equiv="refresh" content="0;URL=\'next_page.html\'" /></head>')

