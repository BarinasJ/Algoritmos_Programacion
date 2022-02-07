"""
Entradas:
valor float del total de la venta
Total de venta --> float --> vnt

Salidas:
La venta con el 15% de descuento
Total --> float --> Total
"""

# Entradas
vnt = float(input("Escribe el total de compra\n"))

# Caja negra
Total = vnt - vnt * 0.15

# Salidas
print("El total de la venta es", Total)