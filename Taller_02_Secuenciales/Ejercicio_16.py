"""
Entrada --> 1 valor float de galones 
Galones --> float --> gal 

Salida --> 1 valor float que sería el costo 
"""

# Entrada
gal = float(input("Escribe la cantidad de galones"))

# Caja negra
gal = (gal * 3.785 * 50000)

# Salida 
print("El precio total es",gal,"COP")