import sqlite3



con=sqlite3.connect('adbgb.db')
cur = con.cursor()


def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS wrkrs(id integer primary key, fn varchar(15), ln varchar(15))')
    con.commit()


create_table()
con.close()



