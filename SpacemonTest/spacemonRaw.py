spacemon = int(input("Enter number of spacemon in rosters:"))
roster1=[]
roster2=[]
for i in range(spacemon):
    planet = input("Enter spacemon(planet) of roster1: ")
    energy = int(input("Enter Energy of spacemon: "))
    power = int(input("Enter power of spacemon:"))
    tuple1 = (planet,energy,power)
    roster1.append(tuple1)

for i in range(spacemon):
    planet2 = input("Enter spacemon(planet) of roster2: ")
    energy2 = int(input("Enter Energy of spacemon: "))
    power2 = int(input("Enter power of spacemon:"))
    spacemon2 = (planet2,energy2,power2)
    roster2.append(spacemon2)

print("roster1:",roster1)
print("roster2:",roster2)

type_mult = int(input("Enter type_mult:"))

damage = type_mult * power
print("Damage:",damage)

Oppo_Energy = energy2 - damage
print(Oppo_Energy)

Earth_energy = energy - Oppo_Energy

print("Remaining Earth's energy:",Earth_energy)


if Oppo_Energy < energy2:
    print("Earth wins against Mercury")

    power = roster2[1][2]
    type_mult2 = int(input("Enter type_mult:"))
    damage = type_mult2 * power
    oppo_energy = Earth_energy - damage

    if oppo_energy < Earth_energy:
        print("Earth is defeated and the competition end")
        print("False")
    else:
        print("Earth Wins:")
        print("True")
else:
    print("Earth is defeated")
    print("False")
    
