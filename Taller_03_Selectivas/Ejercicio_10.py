"""
Entradas --> 1 valor float que es el sueldo bruto del trabajador
Sueldo --> float --> S

Salidas: 1 valor entero que es la categoría, y uno flotante que es su nuevo sueldo
Nuevo sueldo --> float --> N
Categoría --> int --> C

"""
# Entrada 
S = float(input("\nDime tu sueldo bruto "))

# Caja negra
if S <= 900000:
    N = S + S*.60
    C = 5
elif 2000000 >= S > 900000:
    N = S + S*.40
    C = 4
elif 3600000 >= S > 2000000:
    N = S + S*.20
    C = 3
elif 4300000  >= S > 3600000:
    N = S + S*.15
    C = 2
else:
    N = S + S*.10
    C = 1
    
# Salida 
print(f"\nTu sueldo es categoría {C}\nTu nuevo sueldo es de {N}\n")