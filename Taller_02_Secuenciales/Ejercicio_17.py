"""
Entradas --> 1 valor float corrrespondiente al presupuesto 
Presupuesto --> float --> p

Salidas --> 3 valores float para el presupuesto de cada area
Gineciología --> float --> g
Traumatología --> float --> t 
Pediatría --> float --> p
"""

# Entrada
p = float(input("\nDime le presupuesto\n")) 

# Caja negra
g = p * 0.40
t = p * 0.30
p = p * 0.30

# Salida
print("Para Ginecología el presuesto es:",g,"Para Traumatología es:",t,"Para Pediatría es:",p,"\n")