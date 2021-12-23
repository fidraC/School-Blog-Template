import sqlite3
from shutil import rmtree
from os import mkdir, urandom
import json
from hashlib import pbkdf2_hmac, sha256
from sys import version
from binascii import hexlify

config = str(open('config.json', 'r').read())
config_json = json.loads(config)
school_name = config_json['school_name']
admin_accounts = config_json['admin_accounts']


def getHash(plaintext):
    salt = str(sha256(urandom(60)).hexdigest() + "endofsalt").encode('utf-8')
    m = pbkdf2_hmac('sha256', bytes(plaintext, 'utf-8'), salt, 200000)
    hash = hexlify(m)
    return (salt + hash).decode('utf-8')


def db_config(admin_accounts):
    connection = sqlite3.connect('database.db')

    with open('db_config.sql') as f:
        connection.executescript(f.read())
    cur = connection.cursor()
    # Root password = ROOTadmin16! (Change for production)
    for account in admin_accounts:
        cur.execute('INSERT INTO admin_accounts (username, password_hash, department) VALUES (?, ?, ?)',
                    (account['username'], getHash(account['password']), account['department']))

    connection.commit()
    connection.close()

def file_reset():
    rmtree("static/img/preview_imgs")
    mkdir("static/img/preview_imgs")
    rmtree("uploads/markdown_files")
    mkdir("uploads/markdown_files")

def html_config(school_name):
    admin_base = open('templates/index_templates/admin.html', 'r').read().replace('school_name_var', school_name)
    open('templates/admin/base.html', 'w').write(admin_base)
    defaults_base = open('templates/index_templates/default.html', 'r').read().replace('school_name_var', school_name)
    open('templates/defaults/base.html', 'w').write(defaults_base)

print(version)
db_config(admin_accounts)
file_reset()
html_config(school_name)
