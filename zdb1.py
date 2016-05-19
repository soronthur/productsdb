from tkinter import *
import sqlite3


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button=Button(frame,text='Open Db', fg='red', command = self.ouvrir)
        self.button.pack(side=LEFT)

        self.button2 = Button(frame, text = 'Create table', command = self.tabluh)
        self.button2.pack(side=LEFT)

        self.button3 = Button(frame, text = 'Close database', command = self.closedb)
        self.button3.pack(side=LEFT)

        self.button4 = Button(frame, text='Insert data', command=self.insertdb)
        self.button4.pack(side=LEFT)

        self.button5 = Button(frame, text='Print records', command=self.listar)
        self.button5.pack(side=LEFT)

        self.a = Entry(frame)
        self.a.pack(side=BOTTOM)

        self.b = Entry(frame)
        self.b.pack(side=BOTTOM)

        self.c = Entry(frame)
        self.c.pack(side=BOTTOM)




    def listar(self):
        self.con = sqlite3.connect('maddb.db')
        self.cur = self.con.cursor()
        self.cur.execute("SELECT * FROM xxx")
        print(self.cur.fetchall())


    def insertdb(self):
        self.con = sqlite3.connect('maddb.db')
        self.cur = self.con.cursor()
#        self.cur.execute("INSERT INTO xxx VALUES (7, 'Raz', 'Van')")
        a1 = self.a.get()
        b1=self.b.get()
        c1=int(self.c.get())
        self.cur.execute("INSERT INTO xxx (id, fn, ln) VALUES (?, ?, ?)", (c1, a1, b1))
        self.con.commit()


    def closedb(self):
        self.con = sqlite3.connect('maddb.db')
        self.con.close()


    def tabluh(self):
        self.con = sqlite3.connect('maddb.db')
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS xxx(id INTEGER, fn stringvar(10), ln stringvar(10))')
#        self.con.commit


    def ouvrir(self):
        self.con=sqlite3.connect('maddb.db')
        self.cur=self.con.cursor()

root = Tk()
root.title('Dbase Read/Write')
root.geometry('700x300')
app = App(root)
root.mainloop()

