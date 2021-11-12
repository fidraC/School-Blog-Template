#Flask
from flask import *
#Production
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
#Utilities
from hashlib import md5
import sqlite3
from random import randint
#import markdown
import markdown

#Configs
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c40a650584b50cb7d928f44d58dcaffc'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = "0de03e1a949f142951868617004aa54b"
ALLOWED_IMG_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

#Utility functions
def getMD5(plaintext):
    m = md5()
    m.update(plaintext.encode('utf-8'))
    hash = str(m.hexdigest())
    return hash
def normalizeDB(text):
    text = text.replace("('", "")
    text = text.replace("',)", "")
    text = text.replace("\\n", '\n')
    text = text.replace('(#")', "")
    text = text.replace('",)', "")
    return text
#App functions
def authenticate_admin(username, hashpass):
    #Connect to sql database and get username and password
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    dbhash = normalizeDB(str(cur.execute('SELECT password_hash FROM admin_accounts WHERE username = ?', (username,)).fetchone()))
    admin_department = normalizeDB(str(cur.execute('SELECT department FROM admin_accounts WHERE username = ?', (username,)).fetchone()))
    conn.close()
    if hashpass == dbhash:
        return True, admin_department
    else:
        print("username: " + username)
        print("dbhash: " + dbhash)
        print("hashpass: " + hashpass)
        return False, None
def post_to_db(post_title, post_description, post_preview, post_content, department):
    try:
        preview_filename = post_preview.filename
        preview_file_ext = preview_filename.rsplit('.', 1)[1].lower()
        preview_filePath = 'uploads/preview_imgs/' + getMD5(preview_filename) + str(randint(0,999)) + '.' + preview_file_ext
        post_preview.save(preview_filePath)
    except Exception as e:
        filePath = None
    try:
        markdown_filename = post_content.filename
        markdown_file_ext = markdown_filename.rsplit('.', 1)[1].lower()
        markdown_filePath = 'uploads/markdown_files' + getMD5(markdown_filename) + str(randint(0,999)) + '.' + markdown_file_ext
        post_content.save(markdown_filePath)
    except Exception as e:
        markdown_filePath = None
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO posts (title, description, preview, content, department) VALUES (?,?,?,?,?)',
     (post_title, post_description, preview_filePath, markdown_filePath, department))
    conn.commit()
    conn.close()
def get_post_content(post_id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    filePath = normalizeDB(str(conn.execute('SELECT content FROM posts WHERE id = ?', (post_id,)).fetchone()))
    conn.close()
    if filePath != "None":
        try:
            f = open(filePath, 'r')
            content = f.read()
            markdown_content = markdown.markdown(content)
        except Exception as e:
            markdown_content = 'Error'
        return markdown_content
    else:
        return 'Error'
def dbConnect():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
#App routes
@app.route('/logout')
def logout():
    try:
        if 'admin_id' in session:
            session.pop('admin_id')
            session.pop('admin_department')
        if 'client_id' in session:
            session.pop('client_id')
            flash("Logged out")
    except Exception as e:
        flash("Not signed in")
    return redirect(url_for('index'))

#Client
@app.route('/')
def index():
    return "Nothing here yet"
#Posts index page
@app.route('/posts')
def post_index():
    conn - dbConnect()
    posts_data = conn.execute('SELECT title, description, preview, department, created FROM posts').fetchall()
    return render_template('posts/index.html', posts_data = posts_data)
#Main post page
@app.route('/posts/<:string:post_id>')
def post_page(post_id):
    conn = dbConnect()
    post_data = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    return render_template('posts/post_page.html', post_data = post_data)

#Post content
@app.route('/posts/content/<string:post_id>')
def render_post_content(post_id):
    markdown_content = get_post_content(post_id)
    return markdown_content
#Admin
@app.route('/admin/login', methods=('GET','POST'))
def admin_login():
    if 'admin_id' not in session:
        if request.method == 'GET':
            return render_template('admin/login.html')
        elif request.method == 'POST':
            username = str(request.form['username'])
            password = request.form['password']
            hashpass = getMD5(password)
            correct, department = authenticate_admin(username, hashpass)
            if correct == True:
                session['admin_id'] = username
                session['admin_department'] = department
                flash(str('Logged in as ' + username + ' in the ' + department + ' department'))
                return redirect(url_for('admin_index'))
            elif correct == False:
                flash('Incorrect username or password')
                return redirect(url_for('admin_login'))
            else:
                flash('Error')
                return redirect(url_for('admin_login'))
    else:
        flash("Already logged in")
        return redirect(url_for('admin_index'))

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
    #Testing for uploading posts
@app.route('/admin/new_post', methods=('GET', 'POST'))
def new_post():
    if 'admin_id' in session:
        if request.method == 'GET':
            return render_template('admin/new_post.html', department = session['admin_department'])
        elif request.method == 'POST':
            post_title = request.form['post_title']
            post_description = request.form['post_description']
            post_preview = request.files['post_preview']
            post_content = request.files['post_content']
            department = request.form['post_department']
            post_to_db(post_title, post_description, post_preview, post_content, department)
            flash("Success")
            return redirect(url_for('new_post'))
    else:
        return redirect(url_for('admin_login'))
#Run app
if __name__=="__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
