"""
Entradas --> 4 entradas de valor float, 3 son las ventas de cada departamento y uno el sueldo de los vendedores
Departamento 1 --> float --> a
Departamento 2 --> float --> b 
Departamento 3 --> float --> c
Sueldo --> float --> d

Salidas --> 3 valores float que es el sueldo de los vendedores de los departamentos
Departamento 1 --> float --> e
Departamento 2 --> float --> f 
Departamento 3 --> float --> g

"""

# Entradas
a = float(input("\nDime la ventas del departamento 1 "))
b = float(input("Dime la ventas del departamento 2 "))
c = float(input("Dime la ventas del departamento 3 "))
d = float(input("Dime el sueldo de los vendedores "))

# Caja negra 
Tot = (a + b + c)*.33

if a > Tot:
    e = d + d*.20 
else:
    e = d
    
if b > Tot:
    f = d + d*.20 
else:
    f = d
    
if c > Tot:
    g = d + d*.20 
else:
    g = d
    
print(f"\nEl sueldo para el departamento 1: {e}\nEl sueldo para el departamento 2: {f}\nEl sueldo para el departamento 3: {g}\n")
