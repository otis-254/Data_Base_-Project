import sqlite3
import json 
from pathlib import Path 



Students = json.loads(Path("Students").read_text())
print(Students)

with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Students VALUES(?, ?, ?, ?, ?)"
    for Student in Students: 
        conn.execute(command, tuple(Student.values()))
    conn.commit()