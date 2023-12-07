import sqlite3
database = sqlite3.connect("signins.db")
cursor = database.cursor()
cursor.execute('''
CREATE TABLE signins(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(100),
    password VARCHAR(20)
)
''')
database.commit()
