""" 
Entradas --> 1 valor int que es el salario de la personas
Salario --> float --> a

Salidas: 1 valor int que será el nuevo sueldo del trabajador
Salario neto --> float --> b
"""

# Entradas 
a =float(input("\nDime tu salario actual "))

# Caja negra 
if a < 900000: 
    b = (a * 0.15) + a
else:
    b = (a * 0.12) + a
    
# Salidas 
print("Tu salario neto es de",b,"\n")