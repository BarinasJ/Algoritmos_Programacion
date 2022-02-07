"""
Entradas: Las 3 ventas de valor float, 1 sueldo base de valor float
Sueldo base --> float --> Base
Venta 1 --> float --> v1
Venta 2 --> float --> v2
Venta 3 --> float --> v3

Salidas  
Comisiones --> float --> Com
Total --> float --> Comisiones
"""
# Entradas
Base = float(input("Dime tu sueldo base\n"))
v1 = float(input("Dime el valor de la venta 1\n"))
v2 = float(input("Dime el valor de la venta 2\n"))
v3 = float(input("Dime el valor de la venta 3\n"))

# Caja negra
com = (v1+v2+v3) * 0.1
total = (com + Base)

# Salidas
print(f"Tu valor por comisines de venclstas es {com} Y el total es {total}")