#Flask
from flask import *
from flask_session import Session
#Production
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
#Utilities
from hashlib import md5
import sqlite3
#import markdown
import markdown
#Websocket
from flask_socketio import SocketIO, emit, disconnect
from threading import Lock

#Configs
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c40a650584b50cb7d928f44d58dcaffc'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = "0de03e1a949f142951868617004aa54b"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
#Socket
async_mode = None
socket_ = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

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
    conn.close()
    if hashpass == dbhash:
        return True
    else:
        return False
def stt_post_to_db(post_title, post_description, post_preview, post_content):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO STTposts (title, description, preview, content) VALUES (?,?,?,?)', (post_title, post_description, post_preview, post_content))
    conn.commit()
    conn.close()
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

    #Testing for posts
@app.route('/STT/posts/<string:post_id>')
def render_post(post_id):
    try:
        filename = "markdown_files/STT/"+post_id+"/index.md"
        markdown_file = open(filename, 'r').read()
        content = markdown.markdown(markdown_file)
    except Exception as e:
        content = "Error"
    return content
    #Testing for uploading posts
@app.route('/STT/new_post', methods=('GET', 'POST'))
def new_post():
    if request.method == 'GET':
        return render_template('STT/new_post.html')
    elif request.method == 'POST':
        post_title = request.form['post_title']
        post_description = request.form['post_description']
        post_preview = request.files['post_preview'].read()
        post_content = request.files['post_content'].read()
        stt_post_to_db(post_title, post_description, post_preview, post_content)
        flash("Success")
        return redirect(url_for('new_post'))
#Run app
if __name__=="__main__":
    app.run(debug=True)
