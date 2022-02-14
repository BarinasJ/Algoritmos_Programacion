"""
Entradas --> 1 valor float correspondiente a los kilometros recoridos
Kilometros --> float --> A

Salidas --> 1 valor float correspondiente al precio a pagar por el alquiler
Precio --> float --> B

"""

# Entrada 
A = float(input("\nEscribe los kilometros recoridos "))

# Caja negra 
if A <= 300: 
    B = 50000 
elif 1000 > A > 300:
    B = 70000 + 30000 * (A - 300)
else: 
    B = 150000 + 9000 * (A - 1000)
    
# Salida 
print(B)