"""
Entradas --> 8 valores int para cada billete 
N1 --> int --> n_1
N2 --> int --> n_2
N3 --> int --> n_3
N4 --> int --> n_4
N5 --> int --> n_5
N6 --> int --> n_6
N7 --> int --> n_7
N8 --> int --> n_8

Salida: el valor total en el banco 
Valor total --> float --> Dinerof 
"""

# Entradas
n_1=int(input("\nEscriba el numero de billetes que tenga de 50000 "))
n_2=int(input("Escriba el numero de billetes que tenga de 20000 "))
n_3=int(input("Escriba el numero de billetes que tenga de 10000 "))
n_4=int(input("Escriba el numero de billetes que tenga de 5000 "))
n_5=int(input("Escriba el numero de billetes que tenga de 2000 "))
n_6=int(input("Escriba el numero de billetes que tenga de 1000 "))
n_7=int(input("Escriba el numero de billetes que tenga de 500 "))
n_8=int(input("Escriba el numero de billetes que tenga de 100 "))
 
# Caja negra
dinero_f = (n_1*50000)+(n_2*20000)+(n_3*10000)+(n_4*5000)+(n_5*2000)+(n_6*1000)+(n_7*500)+(n_8*100)

# Salida
print("SU dinero total del banco es",dinero_f)