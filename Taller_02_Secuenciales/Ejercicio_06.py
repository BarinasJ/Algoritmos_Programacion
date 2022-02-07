"""
Entradas: 2 Valores int uno para la cantidad de hombres y otro para la cantidad de mujeres
Hombres --> int --> h
Mujeres --> int --> m

Salidas: 2 valores float para indicar el porcentajes de hombres y mujeres
Porcentaje de hombres --> float --> per_h 
Porcentaje de muheres --> float --> per_m
"""
# Entradas
h = int(input("Escribe la cantidad de hombres\n"))
m = int(input("Escribe la cantidad de mujeres\n"))

# Caja negra
per_h = (h*100)/(h+m)
per_m = (m*100)/(h+m)

# Salida
print("El porcentaje de hombres es",per_h,"%","El porcentaje de mujeres es",per_m,"%\n")