# FUNCTION PAGE FOR OPEATIONS ON THE nimreport database.

# SET UP FOR ALL
import sqlite3
import csv
import re
conn = sqlite3.connect('nimreport.sqlite')
print('nimreport database opened')
c = conn.cursor()

# PUT THE FUNCTION YOU WANT TO RUN HERE.

# create regexp function 
conn.create_function('regexp', 2, lambda x, y: 1 if re.search(x,y) else 0)

c.execute(
    "SELECT uid, sex, age, referrer, in_patient, on_call,  procedure_code, CLINICAL_TYPE, CLINICAL_DATA_ELEMENT, PROCEDURE, QUALITY, limited_by, PRIMARY_CONCLUSION, SECONDARY_CONCLUSION, INFORMATION_EFF_SCORE FROM nimreports;" ) 

result=c.fetchall()

# Write the ourput to a file.
with open('DataTo5224.txt', mode="wt", encoding='utf-8') as myfile:
    for lists in result:
        myfile.write('; '.join(str(list) for list in lists))
        myfile.write('\n')

# print('The answers are ', resul
# CLOSE AND FINISHt

conn.commit()
conn.close()
print('nimreport database closed')

##### PUT THE FUNCTIONS HERE ###
# Use cursor object 'exectute()' method to do SQL.
# c.execture("Put SQL line between the double quotes")

# SQL COMMANDS = SELECT
# SELECT uid , sex , age FROM nimreports
# SELECT DISTINCT uid FROM nimreports
# SELECT COUNT(DISTINCT uid) FROM nimreports    # this counts the number of types.
#
# SQL COMMANDS = WHERE
# SELECT uid FROM nimreports WHERE procedure_code='CURIT'   # NB text must be single quote but num not quotes.
# SELECT uid FROM nimreports WHERE procedure_code IN ('CURIT' , 'UUTR')  # IN allows range of options.
# Can also USE >, <, >=, <=, !=, BETWEEN , LIKE 's%' (means begins with s)
#
# Combine and use 'AND', 'OR' and 'NOT'
# SELECT on_call FROM nimreports WHERE procedure_code='CURIT' AND (referrer='ed' OR referrer='ef')
# SELECT on_call FROM nimreports WHERE NOT procedure_code='CURIT' AND NOT procedure_code='CURITC'
#
# UPDATE MULTIPLE RECORDS
# UPDATE nimreports SET uid='5127' WHERE uid='wythnos';
# will update the dates when you get it wrong!!


# c.execute(
#   "SELECT CLINICAL_DATA_ELEMENT, MAIN_FINDINGS FROM nimreports WHERE procedure_code IN ('UHIPB', 'UHIPR', 'UHIPL' )") 
# result=c.fetchall()

# Write the ourput to a file.
# with open('xxx', mode="wt", encoding='utf-8') as myfile:
#    for lists in result:
#        myfile.write('; '.join(str(list) for list in lists))
#        myfile.write('\n')