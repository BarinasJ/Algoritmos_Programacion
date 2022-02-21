"""
Entradas --> 2 valores int que indican el multiplicador de xp y el xp que dan los mounstruos
Multiplicador --> int --> Mult
XP --> int --> Xp

Salidas --> El xp que dará el mounstruo actualmente
XP_actual --> int --> C XpAct
"""

# Caja negra
while True:
    Mult = input().split() # Entradas
    Xp = int(Mult[0]) 
    M = int(Mult[1]) 
    if Xp == 0 and M == 0:
        break
    else: 
        C = M * Xp
    print(C) # Salidas