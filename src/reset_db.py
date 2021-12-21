import sqlite3
from shutil import rmtree
from os import mkdir
connection = sqlite3.connect('database.db')

with open('db_config.sql') as f:
    connection.executescript(f.read())
cur = connection.cursor()
#Root password = ROOTadmin16!
cur.execute('INSERT INTO admin_accounts (username, password_hash, department) VALUES (?, ?, ?)',
    ('root', '7f2c06514be0f80aefcb494e1a6c9c2c', 'root'))

connection.commit()
connection.close()

rmtree("static/img/preview_imgs")
rmtree("uploads/markdown_files")
mkdir("static/img/preview_imgs")
mkdir("uploads/markdown_files")
