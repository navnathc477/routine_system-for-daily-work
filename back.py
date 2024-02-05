import sqlite3

def connect():
    conn = sqlite3.connect('Routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Routine ( date text , time text , study text, hour integer , note text , log text)")
    conn.commit()
    conn.close()

def insert(date , time , study , hour , note , log):
    conn = sqlite3.connect('Routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO Routine VALUES (?,?,?,?,?,?)" , (date , time , study , hour , note , log))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('Routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(time):
    conn = sqlite3.connect('Routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM Routine WHERE time=? ", (time,))
    conn.commit()
    conn.close()

def search(date='' , time='' , study='' , hour='' , note='' , log=''):
    conn = sqlite3.connect('Routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Routine WHERE date=?  OR time=? OR study=? OR hour=? OR note=? OR log=?" , (date , time , study , hour , note , log))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
