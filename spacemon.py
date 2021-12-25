import sqlite3
from sqlite3.dbapi2 import Cursor

roster1=[]
roster2=[]

def connection():
    a = sqlite3.connect('Table1.db')
    return a

def createTable(a):
    a.execute('''CREATE TABLE TABLE1(att_def Text,Mercury INT, Venus INT, Earth INT, Mars INT)''')

def insert(a):
    a.execute("INSERT INTO Table1(att_def,Mercury,Venus,Earth,Mars) VALUES ('Mercury',1,2,1,0.5)")
    a.execute("INSERT INTO Table1(att_def,Mercury,Venus,Earth,Mars) VALUES ('Venus',0.5,1,2,1)")
    a.execute("INSERT INTO Table1(att_def,Mercury,Venus,Earth,Mars) VALUES ('Earth',1,0.5,1,2)")
    a.execute("INSERT INTO Table1(att_def,Mercury,Venus,Earth,Mars) VALUES ('Mars',2,1,0.5,1)")

def spacemonSim(roster1,roster2):

    spacemon = int(input("Enter number of spacemon in rosters:"))

    for i in range(spacemon):
        planet = input("Enter spacemon(planet) of roster1: ")
        energy = int(input("Enter Energy of spacemon: "))
        power = int(input("Enter power of spacemon:"))
        spacemon1 = (planet,energy,power)
        roster1.append(spacemon1)

    for i in range(spacemon):
        planet2 = input("Enter spacemon(planet) of roster2: ")
        energy2 = int(input("Enter Energy of spacemon: "))
        power2 = int(input("Enter power of spacemon:"))
        spacemon2 = (planet2,energy2,power2)
        roster2.append(spacemon2)
    competition(roster1,roster2)

def competition(roster1,roster2):

    type_mult = int(input("Enter type_mult from Table1:"))

    Power=roster1[0][2] #power of spacemon1 in roster1
    damage = type_mult * Power
    
    energy=roster2[0][1] #Energy of spacemon1 in roster2
    E1= energy - damage #Energy of planet in roster2 after damage

    EE1 = roster1[0][1] #Energy of spacemon1 in roster1
    EE2 = EE1 - E1 #Remaining Energy of spacemon1 in roster1

    if E1<EE1:
        #Second Match
        type_mult1 = int(input("Enter type_mult2 from Table1:"))

        Power2 = roster2[1][2] #Power of spacemon2 in roster2
        damage1 = type_mult1 * Power2

        E2 = EE2 - damage1 #Energy of spacemon1 in roster1 after damage

        EE3 = roster2[1][1] #Energy of spacemon2 in roster2

        if E2<EE3:
           # print("Roster1 is defeated.")
            S = "False:"
        else:
            #print("Roster1 is won.")
            S = "True"
            
    else:
        #print("Roster1 is defeated.")
        S="False"

    return S


x = connection()
#createTable(x)
#A1 = insert(x)
spacemonSim(roster1,roster2)
competition(roster1,roster2)
x.commit()
