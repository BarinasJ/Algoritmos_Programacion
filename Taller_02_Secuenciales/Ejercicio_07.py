"""
Entradas: 2 dato float que seran los metros 
Metros --> float --> m

Salidas: 2 Datos float que serán las pulgadas y los pies
Pulgadas --> float --> p
Pies --> float --> ft
"""

# Entrada
m = float(input("Escribe los metros\n"))

# Caja negra
p = m * 39.37 
ft = p / 12

# Salida
print(f"La cantidad de pulgadas es {p} y la cantidad de pies es {ft}")