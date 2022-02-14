"""
Entradas --> 1 valor float que es el monto total de la compra
Costo total --> float --> a

Salidas --> 3-4 valores float según a, costo fondos de la empresa, la cantidad a pagar a crédito, 
el monto a pagar por intereses  y si es necesario, la cantidad prestada al banco.
Fondos de la empresa --> float --> b
Cantidad a pagar a credito --> float --> c 
Intereses --> float --> d
Prestamo del banco --> float --> e

"""

# Entradas 
a = float(input("\nDime el valor total de la compra "))

# Caja negra 
if a > 5000000:
    b = float(a*.55)
    c = float(a*.25)
    e = float(a*.30)
    d = float(c*.20)
else:
    b = float(a*.70)
    c = float(a*.30)
    d = float(c*.20)
    e = 0

# Salida 
print(f"\nLos fondos utilizados de la empresa son: {b} \nEl credito al fabricante es de: {c} \nPor intereses del fabricante tenemos {d}\nEl prestamo del banco es: {e}\n")
