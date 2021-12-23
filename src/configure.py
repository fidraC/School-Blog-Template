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
    salt = sha256(urandom(60)).hexdigest().encode('utf-8')
    m = pbkdf2_hmac('sha256', bytes(plaintext, 'utf-8'), salt, 200000)
    hash = hexlify(m)
    return (salt + hash).decode('utf-8')


def db_config(admin_accounts):
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    #Clear admins
    cur.execute('DELETE FROM admin_accounts')
    # Root password = ROOTadmin16! (Change for production)
    for account in admin_accounts:
        cur.execute('INSERT INTO admin_accounts (username, password_hash, department) VALUES (?, ?, ?)',
                    (account['username'], getHash(account['password']), account['department']))

    connection.commit()
    connection.close()

def html_config(school_name):
    admin_base = open('templates/index_templates/admin.html', 'r').read().replace('school_name_var', school_name)
    open('templates/admin/base.html', 'w').write(admin_base)
    defaults_base = open('templates/index_templates/default.html', 'r').read().replace('school_name_var', school_name)
    open('templates/defaults/base.html', 'w').write(defaults_base)

print(version)
db_config(admin_accounts)
html_config(school_name)
