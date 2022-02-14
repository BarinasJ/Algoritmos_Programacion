"""
Entradas --> 4 valores int a, b, c y d que vamos a convertir en str
a --> str --> a
b --> str --> b
c --> str --> c
d --> str --> d

Salidas --> 1 valores int redondeado a su centena mas cercana 
e --> int --> e
"""

# Entradas
a = str(input("\nEscribe el valor de a "))
b = str(input("Escribe el valor de b "))
c = str(input("Escribe el valor de c "))
d = str(input("Escribe el valor de d "))

# Caja negra
e = a + b + c + d
e = int(e)

if e <= (int(a) * 1000 + int(b)*100 + 50):
    e = e - int(c + d) 
else:
    De = e - ((int(a)*1000)+ (int(b)*100))
    e = e + 100 - De


# Salida 
print(f"\nEl resultado redondeado es {e}\n")