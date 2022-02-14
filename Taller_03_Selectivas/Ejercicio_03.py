"""
Entradas --> 4 valores int correspondientes a: A, B, C y D
a --> int --> a 
b --> int --> b 
c --> int --> c 
d --> int --> d 

Salidas --> un valor float con el resultado de la operación 
Resultado de la operación --> float --> e
"""

# Entradas 
a = int(input("\nDime el valor de A "))
b = int(input("Dime el valor de B "))
c = int(input("Dime el valor de C "))
d = int(input("Dime el valor de D "))

# Caja negra 
if d == 0:
    e = (a-c)**2
else: 
    e = ((a-b)**3)/d
    
# Salidas 
print(f"El resultado es {e} cuando D es igual a {d} \n")   
