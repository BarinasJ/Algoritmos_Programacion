"""
Entradas ---

Salidas --> 2 valores enteros uno que el dato en la posición 12 de la sucesión, y la suma de los 
primeros 12 valores de la sucesión
Posición 12 --> int --> P
Suma --> int --> S
"""

# Caja negra
S = 0
for i in range(12):
    P = 5*i + 6
    S = S + P
    
# Salidas
print("\nEl término doceavo en la suceción es:",P) 
print("La suma de los primeros 12 numeros de la sucesión es:",S,"\n") 