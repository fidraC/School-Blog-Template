import sqlite3
from shutil import rmtree
from os import mkdir
import json
from hashlib import md5
from sys import version

config = str(open('config.json', 'r').read())
config_json = json.loads(config)
school_name = config_json['school_name']
admin_accounts = config_json['admin_accounts']


def getMD5(plaintext):
    m = md5()
    m.update(plaintext.encode('utf-8'))
    hash = str(m.hexdigest())
    return hash


def db_config(admin_accounts):
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    #Clear admins
    cur.execute('DELETE FROM admin_accounts')
    # Root password = ROOTadmin16! (Change for production)
    for account in admin_accounts:
        cur.execute('INSERT INTO admin_accounts (username, password_hash, department) VALUES (?, ?, ?)',
                    (account['username'], getMD5(account['password']), account['department']))

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
