# ADD A WEEKS REPORTS CONVERTED INTO CSV INTO THE DATABASE.

# Direct technique. Add from the CSV

import sqlite3
import csv

# Instantiate the connection and cursor objects.

conn = sqlite3.connect('nimreport.sqlite')
c = conn.cursor()

with open('wythnos.csv', 'r') as file:
    num_reports = 0
    for row in file:
        # print(row.split(','))  = useful for debugging
        c.execute("INSERT INTO nimreports VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row.split(";"))
        conn.commit()
        num_reports += 1

    conn.close()
    print('\n{} Reports entered'.format(num_reports))
    print(f'\n{num_reports} Reports entered')


# File to add new weeks work into the database.
# import sqlite3
# import pandas as pd

# create the connection object.
# conn = sqlite3.connect('mytrialdatabase.db')

# create the cursor object.
# c = conn.cursor()

# append the new CSV to the db.
# Here assuming the data table is called table name
# Using Pandas as the way to go
# df = pd.read_csv('wythnos.csv')
# df.to_sql('table_name', conn, if_exists='append', index=FALSE)

# ALWAYS save and then close it at the end
# conn.commit()
# conn.close()
