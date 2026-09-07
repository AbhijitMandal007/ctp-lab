import sqlite3

con=sqlite3.connect("employee.db")
cur=con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS 
employee(id INTEGER PRIMARY KEY,
name TEXT,
designation TEXT,
dept TEXT,
salary REAL)""")

cur.execute("INSERT INTO employee VALUES(?,?,?,?,?)",(1,"ABHIJIT","HR","AI",25000))
cur.execute("INSERT INTO employee VALUES(?,?,?,?,?)",(2,"SUROJ","DATA SCIENTIST","AI",250000))
cur.execute("INSERT INTO employee VALUES(?,?,?,?,?)",(3,"DEBARKA","MANAGER","IT",10000000000))
cur.execute("INSERT INTO employee VALUES(?,?,?,?,?)",(4,"BINIT","SDE","IT",250000))

#Read Operations 
cur.execute("SELECT * FROM employee")
print(cur.fetchall(),"\n")

#Update Operations
cur.execute("UPDATE employee SET salary=? WHERE  id=?",(60000000,1))

#Delete Operations
cur.execute("DELETE FROM employee WHERE id=?",(1,))

con.commit()
con.close()