import sqlite3
import json 
from pathlib import Path 



tests = json.loads(Path("tests").read_text())
print(tests)

with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO tests VALUES(?, ?, ?, ?, ?)"
    for Student in tests: 
        conn.execute(command, tuple(Student.values()))
    conn.commit()