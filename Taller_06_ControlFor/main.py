archivo = open('paises.txt', 'r')#imprima la posicion de colombia
"""
c=0 
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
"""
#Imprimir todos los paises que inicien con la letra C
lista=[]
paises=[]
for e in archivo:
  a=e.index(":")
  for r in range(0,a):
    lista.append(e[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for e in paises:
  if(e[0]=="C"):
    print(e)
"""
#imprima todas las capitales que inicien con la leta B
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
    
"""
#Cuente e imprima cuantas ciudades inician con la letra M
m=0
lista=[]
ciudadm=[]
for i in archivo:
  a=i.index(":")
  for q in range(a+2, len(i)-1):
    lista.append(i[q])
    a="".join(lista)
  ciudadm.append(a)
  lista=[]
for i in ciudadm:
  if(i[0]=="M"):
    m=m+1
print(m)
"""
#Imprima todos los paises y capitale cuyo inicio sea con la letra U
lista=[]
lista2=[]
ciudadu=[]
paisu=[]
for i in archivo:
  e=i.index(":")
  for q in range(e+2, len(i)-1):
    lista.append(i[q])
    e="".join(lista)
  ciudadu.append(e)
  lista=[]
  n=i.index(":")
  for t in range(0, n):
    lista2.append(i[t])
    n="".join(lista2)
  paisu.append(n)
  lista2=[]
for i in paisu:
  if(i[0]=="U"):
    print(i) 
for i in ciudadu:
  if(i[0]=="U"):
    print(i)
"""

"""
#Cuente e imprima cuantos paises que hay en el archivo
lista=[]
contador=0
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  contador=contador+1
  print(contador)
  lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
""
#Busque e imprima la ciudad de Singapur
lista=[]
ciudades=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudades.append(a)
  lista=[]
for i in ciudades:
  if(i=="Singapur"):
    print(i)
""
#Busque e imprima el pais de Venezuela y su capital
lista=[]
pais=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  for r in lista:
    pais.append(r)
for i in pais:
  if i=="Venezuela: Caracas\n":
    print(i)
    break
  lista=[]   
""
#Cuente e imprima las ciudades que su pais inicie con la letra E
lista=[]
paises=[]
ciudades=[]
ciudad=[]
for i in archivo:
  lista.append(i)
for i in lista:  
  if(i[0]=="E"):
    ciudades.append(i)
  c="".join(ciudades)  
for i in ciudades:
  a=i.index(":")     
  for r in range(a+2,len(i)-1):
    ciudad.append(i[r])
  b = "".join(ciudad)  
for i in ciudad:
    print(i,end="")
  
""
#Busque e imprima la Capiltal de Colombia
lista=[]
ciudades=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudades.append(a)
  lista=[]
for i in ciudades:
  if(i=="Bogotá"):
    print(i)
""
#imprima la posicion del pais de Uganda
c=0 
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
""
#imprima la posicion del pais de Mexico
c=0 
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="México: Ciudad de México \n"):
    break
  lista=[]   
print(c)
""
#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
lista=[]
for i in archivo:
  lista.append(i)
lista.remove("Madagascar: rey julien\n")
lista.insert(109,"Madagascar: Antananarivo\n")
print(lista)
""
#Agregue un país que no esté en la lista 
lista=[]
for i in archivo:
  lista.append(i)
lista.insert(136,"Palestina: Jerusalem\n")
print(lista)
""
archivo.close()
"""