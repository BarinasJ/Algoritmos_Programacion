""" 
Entradas --> 1 valor str ; nombre de la persona ; un valor float que es el monto de la compra
Nombre --> str --> A
Compra --> float --> B

Salidas --> 1 valor float correspondiente al total a pagar aplicado el descuento, 1 str que es el nombre de 
la persona, 1 valor float que es B y un valor flotante correspondiente al descuento aplicado
Total --> float --> C 
Nombre --> str --> A 
Compra --> float --> B 
Descuento --> float --> D

"""

# Entrada 
A = str(input("\nEscribe tu nombre "))
B = float(input("Escribe el valor de tu compra "))

# Caja negra 
if B < 50000:
    D = 0
elif 50000 <= B < 100000:
    D = .05 
elif 100000 <= B < 700000:
    D = .11 
elif 700000 <= B < 1500000:
    D = .18
else: 
    D = .25

C = B - B * D 

# Salida 
print(f"\nQué tal {A}?\nPara la compra: {B}\nEl valor a pagar es: {C}\nCon un descuento de: {B*D}\n")
