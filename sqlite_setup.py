import sqlite3
import datetime
#current_time = datetime.datetime.now()

conn = sqlite3.connect("/home/pi/Desktop/Physical Computing/Testatkarte0/LED.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS tblLED (
        LID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        is_on BOOLESH,
        zeit_stempel DATETIME
    )""")

#c.execute(f"INSERT INTO tblLED VALUES (null, '{current_time}', 'Andersen')")
c.execute(f"SELECT * FROM tblLED")
inhalt = c.fetchall()
print(inhalt)
conn.commit()

conn.close()