import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):

    conn = sqlite3.connect(db_file)
    cur = conn.cursor()    
    cur.execute('CREATE TABLE projects(active INT, title TEXT, description TEXT, date TEXT)')    


create_connection("base.db")