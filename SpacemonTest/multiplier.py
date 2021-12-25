import sqlite3
from sqlite3.dbapi2 import Cursor
planet11=[]
planet22=[]

def connection():
    a = sqlite3.connect('Table1.db')
    return a

'''def insert(a):
    planet1 = input("Enter spacemon(planet) of roster1: ")
    planet11.append(planet1)
    planet2 = input("Enter spacemon(planet) of roster2: ")
    planet22.append(planet2)
'''    


def retrieve(a):
    
    xx=int(input("Enter planet in row:"))
    yy=int(input("Enter planet in coloum:"))

    cursor = a.cursor()
    B1 = "SELECT * FROM TABLE1 WHERE att_def=?"
   # B2 = "SELECT * FROM TABLE1 WHERE Venus=? "
    #B3 = "SELECT * FROM TABLE1 WHERE Earth=? "
    #B4 = "SELECT * FROM TABLE1 WHERE Mars=? "

    BB1 = "SELECT * FROM TABLE1 WHERE Mercury=?"
    BB2 = "SELECT * FROM TABLE1 WHERE Venus=? "
    BB3 = "SELECT * FROM TABLE1 WHERE Earth=? "
    BB4 = "SELECT * FROM TABLE1 WHERE Mars=? "

    A1 = cursor.execute(B1,(xx))
    A2 = cursor.execute(BB1,BB2,BB3,BB4(yy))
 

    Y = cursor.fetchall()
    print(Y)
    

x=connection()
print(retrieve(x))


    