"""
Entradas: 5 valores flotantes que son las notas del estudiante
Nota 1 parcial --> float --> n1
Nota 2 parcial --> float --> n2 
Nota 3 parcial --> float --> n3
Nota 4 Examen final --> float --> n4
Nota 5 trabajo final --> float --> n5 


Salida: Nota del estudiante
Notal final --> float --> suma 
"""
# Entradas
n1 = float(input("Escribe la nota del primer parcial\n"))
n2 = float(input("Escribe la nota del segundo parcial\n"))
n3 = float(input("Escribe la nota del tercer parcial\n"))
n4 = float(input("Escribe la nota del examen final\n"))
n5 = float(input("Escribe la nota del trabajo final\n"))

# Caja negra
a = float((n1+n2+n3)/3) * 0.55
b = float(n4 * 0.3)
c = float(n5 * 0.15) 
suma = a + b +c 

# Salidas
print("La nota final es",suma)