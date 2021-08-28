from flask import Flask, jsonify, request, render_template, session, url_for, redirect
import psycopg2
import hashlib

salt = "$2b$12$qhhAzmN.Y5voEH79W9BzYe".encode("utf-8")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'akeysosessionwillworkakeysosessionwillwork'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_SECURE'] = False

conn = psycopg2.connect("dbname=notetoself user=notetoself")

@app.route("/")
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        check_creds(username, password)
        if check_creds(username, password) == True:
            session['logged_in'] = 1
            session['username'] = username
            session['userid'] = get_user_id(username)
            return redirect(url_for('index'))
        else:
            return render_template('login.html')

    elif request.method == "GET":
        if session.get('logged_in', None) == 1:
            return redirect(url_for('list_notes'))
        else:
            return render_template('login.html')

    return render_template('login.html')

@app.route("/list")
def list_notes():
    userid = session['userid']
    cur = get_cursor()
    cur.execute('select * from note where userid = {}'.format(userid))
    data = cur.fetchall()
    return jsonify(data)

@app.route("/delete/<noteid>")
def delete_note(noteid):
    if check_note_owner(noteid, session.get('userid')):
        cur = get_cursor()
        q = 'delete from note where id = {}'.format(noteid)
        cur.execute(q)
        conn.commit()
    else:
        return redirect(url_for('list_notes'))
    return redirect(url_for('list_notes'))

@app.route("/update", methods=['GET', 'POST'])
def update_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        noteid = request.form['noteid']
        q = """update note set title = '{}', content = '{}' where id = {}""".format(title, content, noteid)
        c = get_cursor()
        c.execute(q)
        return redirect(url_for('list_notes'))
    elif request.method == 'GET':
        return render_template('update.html')


def get_cursor():
    cur = conn.cursor()
    return cur

def get_user_id(username):
    c = get_cursor()
    q = """select id from "user" where username = '{}'""".format(username)
    c.execute(q)
    res = c.fetchone()[0]
    return res

def check_creds(username, password):
    m = hashlib.sha256(password.encode("utf-8"))
    hash = m.hexdigest()
    c = get_cursor()
    q = '''select password from "user" where username = '{}';'''.format(username)
    c.execute(q)
    result = c.fetchone()[0]
    if result == hash:
        return True
    else:
        return False

def check_note_owner(noteid, userid):
    cur = get_cursor()
    # Check userid for note
    cur.execute('select userid from note where id = {}'.format(noteid))
    rs = cur.fetchone()[0]
    # Does userid match the one on the note?
    print(userid, rs)
    if userid == rs:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
