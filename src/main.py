#Imports
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, make_response, session
from flask.ext.session import Session
from werkzeug.exceptions import abort
import os.path
from hashlib import md5
from werkzeug.utils import secure_filename

#Configs
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c40a650584b50cb7d928f44d58dcaffc'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = "0de03e1a949f142951868617004aa54b"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

#Utility functions
def getMD5(plaintext):
    m = md5()
    m.update(plaintext.encode('utf-8'))
    hash = str(m.hexdigest())
    return hash

#App functions
def authenticate_admin(username, hashpass):
    #Connect to sql database and get username and password
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    dbhash = str(cur.execute('SELECT password_hash FROM admin_accounts WHERE username = ?', (username,)).fetchone())
    if hashpass == dbhash:
        return True
    else:
        return False
#App routes
    #Admin login
@app.route('/admin/login')
def admin_login():
    if 'admin_id' not in session:
        if request.method == 'GET':
            return render_template('admin/login.html')
        elif request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            hashpass = getMD5(password)
            correct = authenticate_admin(username, hashpass)
            if correct == True:
                session['admin_id'] = username
                flash('Logged in')
                return redirect(url_for('admin_index'))
            elif correct == False:
                flash('Incorrect username or password')
                return redirect(url_for('admin_login'))
            else:
                flash('Error')
                return redirect(url_for('admin_login'))

    #Admin index
@app.route('/admin', methods=('GET', 'POST'))
def admin_index():
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))
    elif 'admin_id' in session:
        if request.method == 'GET':
            return render_template('admin/index.html')
        #Administrative actions
        elif request.method == 'POST':
            action = request.form['action']
            #Deleting comments, banning users from commenting, etc
        return redirect(url_for('admin_index'))
    else:
        flash('Error')
        redirect(url_for('admin_index'))
