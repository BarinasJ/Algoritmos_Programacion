"""
Entradas ----

Salidas --> El numero de terminos nesesarios para que la exprexión se acerque a 1000
Terminos --> int --> E T
Sumatoria --> int --> d S
"""
# Caja negra
T = 1
while True:
    S = ((T**2)+1)/T
    if S > 1000:
        T -= 1
        S = ((T**2)+1)/T
        break
    else: 
        print(T)
        T += 1
# Salidas
print("\nEl numero de terminos necesarios es:",T)
print("El resultado de la sumatoria es:",S,"\ncuando k es:",T,"\n")