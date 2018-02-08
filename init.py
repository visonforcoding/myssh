# coding=utf-8
import sqlite3
import os

db = os.path.join(os.getcwd(), 'server.db')

conn = sqlite3.connect(db)

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE server
             (id integer PRIMARY KEY AUTOINCREMENT,host varchar(20), port integer, user varchar(20) null, pwd varchar(64) null)''')

# Insert a row of data
# c.execute(
#     "INSERT INTO server (host,port,user,pwd) VALUES ('127.0.0.1',22,'root','vagrant')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
