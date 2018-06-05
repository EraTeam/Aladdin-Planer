import sqlite3
import hashlib
import datetime
import logging

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

def verifyUsername(username):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=?", (username, ))
    conn.commit()
    rows = cur.fetchall()

    if not rows:
        return False
    else:
        return True

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


def getUserInformation(hash):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE userHash=?", (hash, ))    
    conn.commit()
    rows = cur.fetchall()

    if not rows:
        return False
    else:
        return rows
    

def getActiveProjects():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT rowid, * FROM projects WHERE active = 1")
    conn.commit()
    rows = cur.fetchall()

    if not rows:
        return False
    else:
        return rows


def createNewProject(title, description):

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H-%M")    

    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO projects(active, title, description, date) VALUES(1, ?, ?, ?)",
        (title, description, timestamp)
    )
    conn.commit()

    return True



def validateProject(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT rowid, active FROM projects WHERE rowid=?", (id, ))    
    conn.commit()
    rows = cur.fetchall()

    if not rows:
        return False
    else:
        if rows[0][1] is 1:
            return True
        else:
            return False


def getProjectCards(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM projectCards WHERE projectId=?", (id, ))    
    conn.commit()
    rows = cur.fetchall()

    if not rows:
        return False
    else:
        return rows


def createProjectCards(id, title, description):

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H-%M")    

    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO projectCards(projectId, active, title, description, date) VALUES(?, 1, ?, ?, ?)",
        (id, title, description, timestamp)
    )
    conn.commit()

    return True


def updateUser(username, password, email, sessionhash):
    if username != "" and password != "" and email != "" and not checkIfUserExists(username, sessionhash):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE users SET username=?, password=?, email=? WHERE userHash=?",
                    (username, password, email, sessionhash))
        conn.commit()
        return True
    else:
        return False

def checkIfUserExists(username, sessionhash):
    conn = connect_db()
    cur = conn.cursor()

    users = cur.execute("SELECT username FROM users")
    for user in users:
        if username in user:
            return True

    return False


