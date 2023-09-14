# DELETE SELECTED REPORTS FROM THE DATABASE.

# Direct technique. Add from the CSV

import sqlite3
import csv

# Instantiate the connection and cursor objects.

conn = sqlite3.connect('nimreport.sqlite')
c = conn.cursor()
print('Database opened')
# Delete action 
c.execute("DELETE FROM nimreports WHERE uid= '5221'")

conn.commit()
conn.close()

print('Reports deleted')