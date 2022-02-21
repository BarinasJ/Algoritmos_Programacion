"""
Entradas
nombre --> nom --> str
puntajefinal --> pfn --> float
seguir --> cont --> int

Salidas
estudiante mayor puntaje --> str
estudiante menor puntaje --> str
mayorpuntaje --> float
menorpuntaje --> float
porcentaje inferior al promedio --> por_inf --> float
porcentaje superior al promedio --> por_sup --> float
"""
nombre=[]
puntaje=[]
pun_inf = pun_sup = 0

while True:
    nom=input("Ingrese su nombre ")  #entrada
    pfn=float(input("Ingrese su puntaje final "))  #entrada
    nombre.append(nom)  
    puntaje.append(pfn)

    cont=int(input("Desea ingresar mas datos?\nDigite 0 para SI y 1 para NO ")) #entrada
    if cont==1:
        break

for x in range(len(puntaje)):
    if puntaje[x]<(sum(puntaje)/len(puntaje)): 
            pun_inf+=1
        
    elif puntaje[x]>(sum(puntaje)/len(puntaje)):
            pun_sup+=1

por_in=round((pun_inf*100)/len(puntaje),2)
por_su=round((pun_sup*100)/len(puntaje),2)


p_m=0
pun_m=puntaje[0]

for x in range(len(puntaje)):
    if puntaje[x]>pun_m:
        pun_m=puntaje[x]
        p_m=x
print("El estudiante con mayor puntaje es: ",nombre[p_m])  #salidas
    
for x in range(len(puntaje)):    
    if puntaje[x]<pun_m:
        pun_m=puntaje[x]
        p_m=x
print("El estudiante con menor puntaje es: ",nombre[p_m])  #salidas

#salidas
print("El puntaje maximo obtenido es: ",max(puntaje))
print("El puntaje minimo obtenido es: ",min(puntaje))
print("El promedio de todos los puntajes es: ",round(sum(puntaje)/len(puntaje),2))
print(por_in,'% fue inferior al promedio')
print(por_su,'% fue superior al promedio')