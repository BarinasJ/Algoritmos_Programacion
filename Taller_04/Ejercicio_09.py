"""
Entradas --> Valores int correspondientes al tipo de gas
Tipo de gas --> int --> Type

Salida --> 4 valores str con las respectiva cantidades de cada gas
MUITO OBRIGADO --> str --> B
Alcool --> str --> Alcool
Gasolina --> str --> Gasolina
Diesel --> str --> Diesel
"""
# Caja negra
Alcohol = 0 
Gasolina = 0 
Diesel = 0
while True:
    Type = int(input()) # Entradas
    if Type == 1: 
        Alcohol += 1
    elif Type == 2: 
        Gasolina += 1
    elif Type == 3:
        Diesel += 1
    elif Type == 4:
        break
    else: 
        Type = Type

# Salidas
print("MUITO OBRIGADO")
print("Alcool:",Alcohol)
print("Gasolina:",Gasolina)
print("Diesel:",Diesel)