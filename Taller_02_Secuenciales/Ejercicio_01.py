"""
Entradas: 3 edades
Edad 1 --> int --> a
Edad 2 --> int --> b
Edad 3 --> int --> c
Salidas --> El promedio los valores (a,b,c)
Promedio --> int --> p 

"""

# Entradas
a = int(input("Dime la primera edad\n"))
b = int(input("Dime la primera edad\n"))
c = int(input("Dime la primera edad\n"))

# Caja negra
p = (a+b+c)/3

# Salidas
print(int(p))