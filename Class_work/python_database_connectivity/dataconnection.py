# to import mysql.connector module
import mysql.connector

# establish connection with mysql
dataconnection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='032421@Papameayush',
    database='Studentmanagement'
)

# to create a cursor object
cursorobj = dataconnection.cursor()

# writing insert query
sql_query = "INSERT INTO student VALUES(%s,%s,%s,%s)"

""" 
put the values to be inserted
Stdid = 'std101'
Stdname = 'Anil'
Standard = '10th'
age = 15
values = (Stdid,Stdname.Standard,age)

#to execute the query 
cursorobj.execute(sql_query , values)"""


# multiple records to be inserted
values = [
    ('std102', 'Rahul', '9th', 14),
    ('std103', 'Priya', '10th', 15),
    ('std104', 'Neha', '8th', 13),
    ('std105', 'Aman', '9th', 14)
]

# execute the query for multiple records
cursorobj.executemany(sql_query, values)

# commit the changes
dataconnection.commit()

# check how many records are inserted
if cursorobj.rowcount > 0:
    print(cursorobj.rowcount, "Records Inserted Successfully")
else:
    print("Unable to insert records")

# close cursor object
cursorobj.close()

# close connection object
dataconnection.close()