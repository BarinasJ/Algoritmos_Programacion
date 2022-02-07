"""
Entradas --> 3 valores float 
Lote naranjas --> float --> x
Decena de naranajas --> float --> y 
Obtenido --> float --> k 

Salidas --> 1 valor float
pocentaje --> float --> P
"""

# Entradas 
x=int(input("Escribe el precio del lote de naranjas "))
y=float(input("Escribe el precio por decena de las naranjas "))
k=float(input("Escribe el dinero de la venta de naranjas "))

# Caja negra
dec = (x/12)
g = y * dec
ganancia = k - g
p = (ganancia / g)*100

# Salida
print(f"El porcentaje es de {p}%")