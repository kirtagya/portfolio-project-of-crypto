from msilib import Table
import sqlite3
from venv import create

from matplotlib.pyplot import table
con=sqlite3.connect('Mycompany.db')
cObj=con.cursor()
# cObj.execute("CREATE TABLE Employ(id INTEGER PRIMARY KEY,name TEXT,salary INTEGER REAL,department TEXT, position TEXT)") 
# con.commit()
# cObj.execute("Insert into Employ VALUES(2,'ashish',75000,'c','developer')")
# con.commit()
# cObj.execute("update employ set department='python' where id =2")
# con.commit()
# cObj.execute("select * from employ")
# result=cObj.fetchall()
# print(result)
cObj.execute("delete from employ where name=?",('ashish',) )
con.commit()
cObj.close()
con.close() 