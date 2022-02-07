"""
Entradas --> 2 valores float equivalentes al precio del computar de contados o por cada cuota
Precio de contado --> float --> p 
Precio por cuota --> float --> c

Salidas --> 2 salidas que es el porcentaje de recargo y el procentaje por cuota
Porcentaje --> float --> a
Porcentaje por cuota --> float --> b
"""

# Entrada
p = float(input("\nEscribe el valor del Computador pagando de contados\n"))
c = float(input("\nEscribe el valor por cada cuota\n "))

# Caja negra
c = c*12
a = (((c*100)/p)-100)
b = (((c*100)/p)-100)/12
# Salida 
print(f"Por recargo el porcentaje es de {a}% y por cuota es de {b}%")