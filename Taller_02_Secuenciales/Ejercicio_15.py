"""
Entradas --> 2 valores float que son el valor de venta al público y el precio por el cual lo obtuviste
Venta al público --> float --> pvp
Precio final --> float --> pf

Salidas --> 1 valor float que es el descuento aplicado 
Descuento --> float --> d
"""


# Entradas
pvp = float(input("\nEscribe cual es el precio de venta al público "))
pf = float(input("Escribe cual es el precio final "))        

# Caja negra 
d = 100 -((pf*100)/pvp)

# Salida
print(f"\nTu descuento es del {d}%\n")