"""
Entradas --> un valor int que va a ser nuesta contraseña
Contraseña --> int --> A 

Salidas: 2 str dependiendo si la contraseña es correcta o no
Correcta --> str --> B 
Incorreta --> str ---> C
"""
# Entrada
A = int(input())

# Caja negra
while A !=2002:
    print("Senha Invalida") # Salida
    A = int(input())

# Salida
print("Acesso Permitido")