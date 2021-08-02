# backend of the app. 
import sqlite3

def connect():
    conn = sqlite3.connect("chromebooks.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS chromebook(id INTEGER PRIMARY KEY, en_date TEXT, en_sname TEXT, en_grade INTEGER, en_class TEXT, en_pname TEXT, en_psign TEXT, en_cin TEXT, en_ccn TEXT)")
    conn.commit()
    conn.close()

def insert(en_date,en_sname,en_grade,en_class,en_pname,en_psign,en_cin,en_ccn):
    conn = sqlite3.connect("chromebooks.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO chromebook VALUES (NULL,?,?,?,?,?,?,?,?)",(en_date,en_sname,en_grade,en_class,en_pname,en_psign,en_cin,en_ccn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("chromebooks.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM chromebook")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(en_date ='',en_sname ='',en_grade ='',en_class='',en_pname='',en_psign='',en_cin='',en_ccn=''):
    conn = sqlite3.connect("chromebooks.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM chromebook WHERE en_date=? OR en_sname=? OR en_grade=? OR en_class=? OR en_pname=? OR en_psign=? OR en_cin=? OR en_ccn=?",(en_date,en_sname,en_grade,en_class,en_pname,en_psign,en_cin,en_ccn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("chromebooks.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM chromebook WHERE id=?",(id,))
    conn.commit()
    conn.close()


def update(id,en_date,en_sname,en_grade,en_class,en_pname,en_psign,en_cin,en_ccn):
    conn = sqlite3.connect("chromebooks.db")
    cur = conn.cursor()
    cur.execute("UPDATE chromebook SET en_date=?, en_sname=?, en_grade=?, en_class=?, en_pname=?, en_psign=?, en_cin=?, en_ccn=? WHERE id=?",(en_date,en_sname,en_grade,en_class,en_pname,en_psign,en_cin,en_ccn,id))
    conn.commit()
    conn.close()

connect()