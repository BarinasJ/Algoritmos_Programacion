"""
Entradas --> 2 valores float, el dinero invertido en el banco ; los intereses del banco por su inversión
Dinero invertido en el banco --> float --> a
Intereses del banco --> float --> b

Salidas: El dinero total en el banco
Dinero total --> float --> c

"""

# Entradas
a = float(input("\nHola cuanto dinero tienes invertido en el banco "))
b = float(input("Cuales son los intereses (%) de tu banco por inversión "))

# Caja negra 
b = b/100
c = a * b
d = c + a 

# Salidas 
print("\nEl dinero de tu cuenta es",d,"\n")  if c > 100000 else print("\nEl dinero de tu cuenta es",a,"\n")

