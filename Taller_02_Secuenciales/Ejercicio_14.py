"""
Entradas --> 3 entradas de valor float 2 para consumo actual y anterior y otro para el valor por kilovatio
lectura anterior --> float --> kw_1
Lectura actual --> float --> kw_2 
Valor por kw --> float --> val

Salida --> 1 salida de valor float que es el consumo total
Consumo total --> float --> tot
"""

# Entradas
kw_1 = float(input("\nDime la lectura anterior y la actual "))
kw_2 = float(input())
val = float(input("Dime el valor por kilovatio "))

# Caja negra
tot = (kw_2-kw_1)* val

# Salida
print("\nEl valor total es",tot ,"\n")