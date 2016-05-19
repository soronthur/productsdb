import sqlite3
import time
import datetime
import random


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot (unix REAL, datestamp TEXT, keyword TEXT, value REAL)')


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(87435943543, '2016-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?,?,?,?)", (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    c.execute("SELECT * FROM stuffToPlot WHERE unix > 1463563375")
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print (row[1])

def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]

    c.execute('UPDATE stuffToPlot SET value = 111 WHERE value = 5')
    [print(row) for row in c.fetchall()]
    c.execute('DELETE FROM stuffToPlot WHERE value = 7')
    conn.commit()


#create_table()
#data_entry()

#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)

#read_from_db()
del_and_update()
c.close()
conn.close()