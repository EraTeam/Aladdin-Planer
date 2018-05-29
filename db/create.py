import sqlite3
from sqlite3 import Error
 
 #@TODO: Eine create.py zusammenfassen

def create_connection(db_file):

    conn = sqlite3.connect(db_file)
    cur = conn.cursor()    
    cur.execute('CREATE TABLE users(username TEXT, email TEXT, password TEXT, userHash TEXT)')    


create_connection("base.db")