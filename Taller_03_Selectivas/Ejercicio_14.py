"""
Entradas --> 2 valores float que son la lectura anterior y la actual
Anterior --> float --> ant
Actual --> float --> act

Salidas --> 1 valor int que es el total a pagar 
Total --> float --> Tot
"""

# Entrada 
ant = float(input("\nEscribe la lectura anterior "))
act = float(input("Escribe la lectura actual "))
Dif = (act-ant)

# Caja negra 
Valor = [4600, 80000, 100000, 120000]
lista = [0, 100, 300, 500, 100, 300, 500, 1000000000000000000000000000000000] # El ultimo valor para representar infinito

for i in range(4):
    if lista[i] <= Dif <= lista[4 + i]:
        Tot = Dif * Valor[i]

# Salida
print("La cantidad a pagar es de",Tot,"\n")
     