"""
Entradas --> 2 valores float que son los bolivares prestados y los cobrados en intereses
Bolivares prestados --> float --> x 
Bolivares por intereses --> float --> i 

Salidas --> El interes anual float
Interes anual --> float --> a
"""

# Entradas
x = float(input("¿De cuantos bolivares es el prestamo?"))
i = float(input("¿Cuánto se pago en intereses?"))

# Caja negra
a = ((i*100)/x)/4

# Salida 
print(f"El interes anual es de {a}%")