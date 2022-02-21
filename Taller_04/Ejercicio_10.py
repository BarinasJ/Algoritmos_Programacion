"""
Entradas
altura --> alt --> float
continuar--> cont --> int

Salidas
alturamayor-->a-->float
"""
altura=[]
while True:
    alt=float(input("Digite la altura ")) #entradas
    altura.append(alt)
    cont=int(input("Desea continuar?\nDigite 0 para SI o 1 para NO "))  #entradas
    if(cont==1):
        print("La altura mayor es: ",max(altura)) #salidas
        break