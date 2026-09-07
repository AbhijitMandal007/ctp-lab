import sqlite3

con=sqlite3.connect("student.db")
cur=con.cursor()

con.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER,name TEXT,dept TEXT,cgpa REAL)")

id=int(input("ID : "))
name=input("Name : ")
dept=input("Department : ")
cgpa=float(input("CGPA : "))

cur.execute("INSERT INTO student VALUES(?,?,?,?)",(id,name,dept,cgpa))

con.commit()

for x in cur.fetchall():
    print(x)

con.close()