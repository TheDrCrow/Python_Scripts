# Code to create the report database and to create the reports table with the right colunns.
import sqlite3

# create connection objecct by doing so it creates the database.
conn = sqlite3.connect("nimreport.sqlite")

# create the cursor object
c = conn.cursor()

# create the table of nimreports with the appropriate headings.
c.execute(""" CREATE TABLE nimreports (
							uid INTEGER,
							sex TEXT,
							age TEXT,
							referrer TEXT,
							in_patient TEXT, 
							on_call TEXT, 
							q_score TEXT, 
							procedure_code TEXT,
							CLINICAL_TYPE TEXT,
							CLINICAL_DATA_ELEMENT TEXT,
							CLINICAL_NOTES TEXT,
							PROCEDURE TEXT,
							QUALITY TEXT,
							Limited_by TEXT, 
							COMPARISON TEXT,
							Showing TEXT,
							MAIN_FINDINGS TEXT,
							INCIDENTAL_FINDINGS TEXT, 
							IMPRESSION TEXT, 
							PRIMARY_CONCLUSION TEXT, 
							SECONDARY_CONCLUSION TEXT, 
							INFORMATION_EFF_SCORE INTEGER, 
							INFORMATION_NOTES TEXT
							);

""")

# Commit and close
conn.commit()
conn.close()
