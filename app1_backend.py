# backend of the app. 
import sqlite3

class Database:

    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS chromebook(id INTEGER PRIMARY KEY, en_date TEXT, en_sname TEXT, en_grade INTEGER, en_class TEXT, en_pname TEXT, en_psign TEXT, en_cin TEXT, en_ccn TEXT)")
        self.conn.commit()
        #we will leave the database open here.

    def insert(self,en_date,en_sname,en_grade,en_class,en_pname,en_psign,en_cin,en_ccn):
        self.cur.execute("INSERT INTO chromebook VALUES (NULL,?,?,?,?,?,?,?,?)",(en_date,en_sname,en_grade,en_class,en_pname,en_psign,en_cin,en_ccn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM chromebook")
        rows = self.cur.fetchall()
        return rows


    def search(self,en_date ='',en_sname ='',en_grade ='',en_class='',en_pname='',en_psign='',en_cin='',en_ccn=''):
        self.cur.execute("SELECT * FROM chromebook WHERE en_date=? OR en_sname=? OR en_grade=? OR en_class=? OR en_pname=? OR en_psign=? OR en_cin=? OR en_ccn=?",(en_date,en_sname,en_grade,en_class,en_pname,en_psign,en_cin,en_ccn))
        rows = self.cur.fetchall()
        return rows


    def delete(self,id):
        self.cur.execute("DELETE FROM chromebook WHERE id=?",(id,))
        self.conn.commit()


    def update(self,id,en_date,en_sname,en_grade,en_class,en_pname,en_psign,en_cin,en_ccn):
        self.cur.execute("UPDATE chromebook SET en_date=?, en_sname=?, en_grade=?, en_class=?, en_pname=?, en_psign=?, en_cin=?, en_ccn=? WHERE id=?",(en_date,en_sname,en_grade,en_class,en_pname,en_psign,en_cin,en_ccn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()