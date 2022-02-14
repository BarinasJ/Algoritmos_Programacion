"""
Entradas --> 3 valores, uno float que es la edad, otro float que es nivel de hemoglobina, otro srt que 
es el sexo de la persona 
Edad --> float --> B edd
Hemoglobina --> float --> C Hem
Sexo --> float --> D Sex

Salidas --> 1 cadena de texto que le indica a la persona si esta positivo para hemoglobina
Positivo --> str --> E pos
"""

# Entrada 
edd = float(input("\nEscribe tu edad en años "))
Hem = float(input("Escribe tu nivel de hemoglobina en g% "))
if edd > 15:
    Sex = float(input("Escribe tu sexo, utiliza\n1 para masculino\n2 para femenino\n"))
else: 
    Sex = 0
# Caja negra 
lista_1 = [0,1/12,0.5,1,5,10,15,15]
lista_2 = [1/12,0.5,1,5,10,15,100,100]
lista_3 = [12,10,11,11.5,12.6,13,14,12]

J = 0
for i in range(8):
    if edd <= 15:
        if (lista_1[i] < edd <= lista_2[i]) and (Hem < lista_3[i]):
             print("Positivo para anemia\n") # Salida
        else:
            J += 1
    if J == 8:
        print("Negativo para Anemia\n") # Salida

        
    
if edd > 15:
        if Sex == float(1):
            if (lista_1[7] < edd < lista_2[7]) and (Hem < lista_3[6]):
                print("Positivo para anemia\n") # Salida
            else: 
                print("Negativo para anemia\n") # Salida
        else:
            if (lista_1[6] < edd < lista_2[6]) and (Hem < lista_3[7]):
                print("Positivo para anemia\n") # Salida
            else: 
                print("Negativo para anemia\n") # Salida
            

