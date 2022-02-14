"""
Entradas --> 3 valores float correspondientes a A, B y C
A --> float --> A 
B --> float --> B
C --> float --> C
Salidas --> 2 valores float correspondientes a la solución Ax2 +Bx + C que salen 2 valores x1 y x2
X1 --> float --> x_1
X2 --> float --> x_2
"""

# Entradas
A = float(input("\nDime el valor de A "))
B = float(input("Dime el valor de B "))
C = float(input("Dime el valor de C "))

# Caja negra
op = B**2 -4*A*C
if op == 0:
    x_1 = x_2 = -B/(2*A)
elif op > 0: 
    x_1 = (-B + (B**2 -4*A*C)**0.5)/(2*A)
    print(x_1)
    x_2 = (-B - (B**2 -4*A*C)**0.5)/(2*A)
else: 
    x_1 = x_2 = "No tiene solución en los reales"

# Salidas
print(f"\nEl valor de X1 es: {x_1}\nEl valor de X2 es: {x_2}\n") if op >= 0 else print(x_1,"\n") 