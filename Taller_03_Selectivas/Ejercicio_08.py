"""
Entradas --> 2 valores int a y b
P --> int --> a 
Q --> int --> b

Salidas --> los 2 valores P y Q con un mensaje
P --> str --> a 
Q --> str --> b 

"""

# Entrada 
a = int(input("\nEscribe el valor de P "))
b = int(input("\nEscribe el valor de Q "))
pnt=""

# Caja negra
if a**3 + b**4 - (2*(a**2)) > 680:
    # Salida
    pnt=(str(a) + " y " + str(b) + " satisfacen la expresión\n")
else: 
    # Salida
    pnt=(str(a) + " y " + str(b) + " no Satisfacen la expresión\n")
    
#Salida
print(pnt)