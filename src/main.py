#Imports
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, make_response, session
from flask.ext.session import Session
from werkzeug.exceptions import abort
import os.path
import hashlib
from werkzeug.utils import secure_filename

#Configs
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c40a650584b50cb7d928f44d58dcaffc'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = "0de03e1a949f142951868617004aa54b"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

#Utility functions


#App functions
def unauthenticated(route):
    return redirect(url_for('login'))

#App routes
@app.route('/admin', methods=('GET', 'POST'))
def admin():
    route = "/admin"
    if 'username' not in session:
        unauthenticated(route)
    elif 'username' in session:
        return render_template('admin.html')
