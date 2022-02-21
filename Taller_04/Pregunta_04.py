"""
Entradas --> una sola línea que contiene dos números enteros M y P (1 ≤ H, P ≤ 1000)
Hotdogs consumidos --> Hc
Numero participantes --> P

Salida --> una sola línea con un número racional que represente el promedio de perritos calientes consumidos por los participantes.
Perros calientes consumidos --> Sal
"""

datos=(input(""))
(Hc,P)=datos.split(" ")
Hc=int(Hc)
P =int(P)
Sal=(Hc/P)
print(round(Sal,2))
