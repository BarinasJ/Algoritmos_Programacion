lista=[12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23] 
Colexn=list(set(lista))
diccionario={}
size=len(Colexn)-1
while size>=0:
    c=0
    for i in lista:
        if (Colexn[size]==i):
            c=c+1
        diccionario.update({Colexn[size]:c})
    size=size-1
print(diccionario)