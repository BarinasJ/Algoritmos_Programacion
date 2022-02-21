"""
Entradas ---

Salidas --> todos los numeros enteros impares menores que 100, sin contar multiplos de 7 
Numeros --> int --> N
"""

# Caja negra 
N = 1
for i in range(50):
    if (N%7) != 0:
        print(N) # Salida
        N += 2
    else: 
        N += 2
