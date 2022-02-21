"""
Entradas: 2 numeros int que se procederan a dividir utilizando restas sucesivas
Numero 1 --> int --> N1
Numero 2 --> int --> N2

Salidas --> El resto de la división 
Resto --> int --> R
"""

# Entradas 
N1 = int(input("\nDime el primer numero (Dividendo) "))
N2 = int(input("Dime el Segundo numero (Divisor) "))

# Caja negra
print()
R = int(N1/N2)
N = 0
for i in range(R):
    print(f"{N1} - {N2} = {N1-N2}")
    N1 = N1 - N2
    N += 1

# Salidas
print(f"\nEl resto de la división es {N1}")
print(f"El cociente de la dicisión es {N}\n")