"""
Entradas --> tres números enteros seguidos en una sola línea
1er Numero --> Horas del lugar --> Hl
2do Numero --> Horas de viaje --> Hv
3er Numero --> Diferencia Horaria --> Dh

Salidas -->Calcular a que hora llegan al lugar de destino de James y Cuadrado
HoraLlegada
"""

Numeros=input("")
(Hl,Hv,Dh)=Numeros.split(" ")
Hl=int(Hl)
Hv=int(Hv)
Dh=int(Dh)
if((Hl+Hv+Dh)>24):
    HoraLlegada=(Hl+Hv+Dh)-24
    print(HoraLlegada)
elif((Hl+Hv+Dh)<0):
    HoraLlegada=(Hl+Hv+Dh)+24
    print(HoraLlegada)
else:
    HoraLlegada=(Hl+Hv+Dh)
    print(HoraLlegada)