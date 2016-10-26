__author__ = 'howcum'
import sqlite3

conn = sqlite3.connect('mydatabase.db')
print ("Opened database successfully")
conn.execute("PRAGMA busy_timeout = 5000")
conn.execute('''CREATE TABLE `Teacher` ( `username` TEXT NOT NULL UNIQUE, `password` TEXT, `Name` TEXT, PRIMARY KEY(`username`) );''')
print ("Table created successfully")
conn.commit()
conn.close()