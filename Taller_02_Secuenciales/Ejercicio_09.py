"""
Entradas --> 2 entradas de valor float que son las horas trabajadas y el pago por hora
Pago por hora --> float --> ph
Horas trabajadas --> float --> h 

Salidas --> 1 valor float que sería el sueldo neto sacando impuestos 
Sueldo neto --> float --> Neto 
"""


# Entrada
ph = float(input("Escribe el precio por cada hora trabajada\n"))
h = float(input("Escribe el numero de horas trabajadas\n"))

# Caja negra
a = ph*h
Net = a - a * 0.20

# Salida
print("El salario Neto es",Net)