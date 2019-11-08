import sqlite3
from sqlite3 import Error

def sql_connection():
	try:
 		con = sqlite3.connect('mydatabase.db')
 		return con
	except Error:
		print(Error) 
 
def sql_table(con):
 	cursorObj = con.cursor()
 	cursorObj.execute("CREATE TABLE student(id integer PRIMARY KEY, name text, department text, sem integer)")
 	con.commit()
 
con = sql_connection()

#sql_table(con)

def sql_insert(con,entities):
	cursorObj = con.cursor()
	cursorObj.execute('INSERT INTO student(id, name, department, sem) VALUES(?, ?, ?, ?)', entities)
	con.commit()
 
entities = (1, 'Andrew', 'CSE', 5)
entities1=(2,'ABC','CSE',7)
sql_insert(con, entities1)

def displaystudent(con,sid):
	cursorObj = con.cursor()
	cursorObj.execute('SELECT * FROM student where id={0}'.format(sid))
	row=cursorObj.fetchall()
	print("ID: ",row[0][0])
	print("Name: ",row[0][1])
	print("Department: ",row[0][2])
	print("Sem: ",row[0][3])

	
displaystudent(con,1)

def updation(con,sem,sid):
	cursorObj = con.cursor()
	cursorObj.execute('UPDATE student SET sem = {0} where id = {1}'.format(sem,sid))
	con.commit()

def deletestudent(con,sid):
	cursorObj = con.cursor()
	cursorObj.execute('DELETE FROM student where id={0}'.format(sid))
	con.commit()

deletestudent(con,1)

def displayall():
	con.row_factory=sqlite3.Row
	cursorObj = con.cursor()
	cursorObj.execute('SELECT * FROM student')
	allrows=cursorObj.fetchall()
	for row in allrows:
		print('ID: {0} \nName: {1}\nDepartment: {2}\nSem: {3}'.format(row['id'],row['name'],row['department'],row['sem']))
displayall()
	
