"""
Entradas
consumo licor --> l -->int
licor preferido --> lp --> int
edad --> e --> int
sexo --> se --> int
seguir --> seg --> int

Salidas
personas que consumen licor --> s--> int
mujeres menores de edad--> Muj_me-->int
hombres que no consumen aguardiente entre 20 y 25 años-->Hom_no_a-->int
promedio edad de quienes consumen cerveza-->cerv-->int
porcentaje de quienes consumen whisky-->por_w-->int
"""
s=0
Muj_me=0
Hom_no_a=0
Cerv=[]
Wsky=[]
p_Wsky=0
tot=[]

while True:
    l=int(input("Consume licor?\nDigite 0 para SI y 1 para NO "))  #entrada
    if l==0:
        s=s+1
        lp=int(input("Licor preferido: "))  #entrada
        e=int(input("Edad: "))  #entrada

        if lp==3:
            Cerv.append(e)
        elif lp==5:
            Wsky.append(lp)

        genero=int(input("Sexo:\nDigite 0 si es MUJER y 1 si es HOMBRE "))  #entrada

        if genero==1 and lp!=1 and e>=20 and e<=25:
            Hom_no_a+=1

                          
    elif l==1: 
        lp=0
        e=int(input("Edad: "))  #entrada
        genero=int(input("Sexo:\nDigite 0 si es MUJER y 1 si es HOMBRE "))   #entrada
        if genero==1 and e>=20 and e<=25:
            Hom_no_a+=1  

    tot.append(l)

    if e<18 and genero==0:
        Muj_me=Muj_me+1 

    seg=int(input("Desea seguir con la investigacion?\nDigite 0 para SI y 1 para NO "))   #entrada
    if seg==1:
        break

for x in range(len(Wsky)):
    if Wsky[x]==5: 
            p_Wsky+=1
    
por_w=(p_Wsky*100)/len(tot)

#salidas
print(s," son las personas que consumen licor")
print(Muj_me," son las mujeres menores de edad")  
print(Hom_no_a," son los hombres que no consumen aguardiente y tienen entre 20 y 25 años")

if Cerv:
    print(sum(Cerv)/len(Cerv)," es el promedio de edad de quienes consumen cerveza")
else:
    print("0 es el promedio de edad de quienes consumen cerveza")

print(por_w,"% consumen whisky en relación con el total encuestado")  