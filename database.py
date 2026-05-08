import sqlite3
import pandas as pd
from datetime import datetime

# This function sets up the "Notebook"
def init_db():
    conn = sqlite3.connect('urban_pulse.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS incidents 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  timestamp TEXT, 
                  location TEXT, 
                  severity TEXT)''')
    conn.commit()
    conn.close()

# This function writes to the "Notebook"
def add_incident(location, severity):
    conn = sqlite3.connect('urban_pulse.db')
    c = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO incidents (timestamp, location, severity) VALUES (?, ?, ?)", 
              (now, location, severity))
    conn.commit()
    conn.close()

# This function reads the "Notebook"
def get_all_incidents():
    conn = sqlite3.connect('urban_pulse.db')
    df = pd.read_sql_query("SELECT * FROM incidents ORDER BY timestamp DESC", conn)
    conn.close()
    return df