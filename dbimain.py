from tkinter import *
import sqlite3

con = sqlite3.connect('main.db')
cur = con.cursor()

#cur.execute('CREATE TABLE table1(productkey INTEGER primary key, product stringvar(20), productquantity REAL)')
#cur.execute('CREATE TABLE table2(mainkey INTEGER primary key, foreign key(eventkey) references table1(productkey), expirydate TEXT,  eventdate TEXT, eventquantity REAL)')


def create_db():
    cur.execute('CREATE TABLE table1(productkey INTEGER primary key, product stringvar(20))')
    cur.execute('CREATE TABLE table2(mainkey INTEGER primary key, foreign key(eventkey) references table1(productkey))')

class dbi():
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

create_db()