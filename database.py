import sqlite3
import pandas as pd

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE components (id INTEGER PRIMARY kEY AUTOINCREMENT, name TEXT, part TEXT, description TEXT, project TEXT, location INT)')

df = pd.DataFrame()
print("Table created successfully")
conn.close()
