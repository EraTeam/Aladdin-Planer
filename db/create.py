"""
    Create.PY
    This script is responsible for creating the basic database structure. 
    Run it on your server/machine before your launch the flask application.
"""

import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = sqlite3.connect(db_file)
    cur = conn.cursor()    
    cur.execute('CREATE TABLE users(username TEXT, email TEXT, password TEXT, userHash TEXT)')  
    cur.execute('CREATE TABLE projects(active INT, title TEXT, description TEXT, date TEXT)')
    cur.execute('CREATE TABLE projectCards(projectId INT, active INT, title TEXT, description TEXT, date TEXT);')  


create_connection("base.db")