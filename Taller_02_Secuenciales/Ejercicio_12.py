"""
Entradas --> 11 valores float entre notas de tareas y examentes finales
Examen Matematicas --> float --> ex_m
Nota 1 matematicas --> float --> M1 
Nota 2 matematicas --> float --> M2 
Nota 3 matematicas --> float --> M3 
Examen Física --> float --> ex_f
Nota 1 física --> float --> f1
Nota 2 física --> float --> f2 
Examen Química --> float --> ex_q
Nota 1 química --> float --> q1 
Nota 2 química --> float --> q2 
Nota 3 química --> float --> q3 


Salidas --> 4 valores float correspondientes a la nota de cada asignatura, y al promedio general 
Nota en matematicas --> float --> Matematicas 
Nota en Física --> float --> Física 
Nota en Química --> float --> Química 
Promedio genetal --> float --> prom
"""


# Entradas
ex_m = float(input("\nEscribe la nota de tu examen final de Matemáticas ")) 
m1 = float(input("\nEscribe las notas de tus 3 tareas de Matemáticas\n"))
m2 = float(input()) 
m3 = float(input())
ex_f = float(input("\nEscribe la nota de tu examen final de Física ")) 
f1 = float(input("\nEscribe las notas de tus 2 tareas de Física\n"))
f2 = float(input()) 
ex_q = float(input("\nEscribe la nota de tu examen final de Química ")) 
q1 = float(input("\nEscribe las notas de tus 3 tareas de Química\n"))
q2 = float(input()) 
q3 = float(input())

# Caja negra
matematicas = (ex_m * 0.90) + ((m1+m2+m3)/3)*0.10
física = (ex_f * 0.80) + ((f1+f2)/2)*0.20
química = (ex_q * 0.85) + ((q1+q2+q3)/3)*0.15
prom = (matematicas + física + química)/3

# Salida	
print("\nEn Matematicas tu nota es de: ",matematicas,"\nen Física tu nota es de: ",física,"\n en Química tu nota es de: ",química,"\n Y tu promedio general en",prom)