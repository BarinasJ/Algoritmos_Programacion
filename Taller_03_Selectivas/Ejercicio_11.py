"""
Entradas --> 1 valor float que es la temperatura en farenheit
Temperatura --> float --> T

Salida --> 1 valor str que es el deporte mas apto a practicar
Deporte --> str --> Dep
"""

# Entrada 
Temp = float(input("\nEscribe tu temperatura en Farenheit "))

# Caja negra 
if Temp > 85:
    Dep = "Natación"
elif 70 < Temp <= 85:
    Dep = "Tenis"
elif 32 < Temp <= 70:
    Dep = "Golf"
elif 10 < Temp <= 32:
    Dep = "Esquí"
else: 
    Dep = "Marcha"

# Salida 
print("\n" + Dep + "\n")