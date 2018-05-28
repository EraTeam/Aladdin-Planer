import sqlite3
import hashlib
import datetime

def connect_db():
    conn = sqlite3.connect("db/base.db")
    return conn

def insert_new_user(username, email, password):
    conn = connect_db()
    cur = conn.cursor()

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H-%M")

    m = hashlib.md5()
    m.update(timestamp.encode('utf-8'))


    try:
        cur.execute('INSERT INTO users(username, email, password, userHash) VALUES(?, ?, ?, ?)', (username, email, password, m.hexdigest()))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except sqlite3.Error:
        return False



def get_registered_user(username, password):
    conn = connect_db()

    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    conn.commit()
    rows = cur.fetchall()

    if not rows:
        return False
    else:
        return rows


def verifyUserHash(hash):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE userHash=?", (hash, ))    
    conn.commit()
    rows = cur.fetchall()

    if not rows:
        return False
    else:
        return True