from tkinter import *
import sqlite3 as ddb
con = ddb.connect('mydb.db')
con.row_factory=ddb.Row
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS t1(one integer, two integer)')



for i in range(1, 10):
    cur.execute('INSERT INTO t1 VALUES (?, ?)', (i*10, i/10))


cur.execute('INSERT INTO t1 VALUES (11, 22)')
cur.execute('SELECT * FROM t1')
rows = cur.fetchall()
for r in rows:
    print("%s %i" % (r["one"],r["two"]))

con.close()
