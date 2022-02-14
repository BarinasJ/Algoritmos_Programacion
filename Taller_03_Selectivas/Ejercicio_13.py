"""
Entrada --> 2 valores enteros correspondiente a una fecha de nacimientos
Días --> int --> d
Meses --> int --> m
Años --> int --> a

Salidas --> 1 valor str con el signo del zodiaco 
Zodiaco --> str --> z
"""
# Entrada 
d = int(input("\nDime el día de tu nacimiento "))
m = int(input("Dime el mes de tu nacimiento "))
a = int(input("Dime el Año de tu nacimiento "))

# Caja negra 
Signo = ["Sagitario", "Capricornio", "Acuario","Picis","Aries","Tauro","Géminis","Cáncer","Leo","Virgo","Libra","Escorpión"]
lista = [22,22,21,20,21,21,22,22,23,24,23,23]
lista_1 = [11,12,1,2,3,4,5,6,7,8,9,10]
lista_2 = [21,20,19,19,20,21,21,22,23,22,22,21]
lista_3 = [12,1,2,3,4,5,6,7,8,9,10,11]
for i in range(12):
    if ((m == lista_1[i]) and (d >= lista[i])) or ((m == lista_3[i]) and (d <= lista_2[i])):
        # Salida
        print("Tu signo es",Signo[i])

# Salida 
print("Tu edad es",2021-a) if m < 10 else print("Tu edad es",2020-a) 
        