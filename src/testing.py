import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

output = cur.execute("SELECT * FROM admin_accounts WHERE username = ?", ("root",)).fetchall()
print(output[0][0])

