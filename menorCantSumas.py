import random

listaDelUnoAlCien = [*range(1, 100)]
  # genera una lista de 100 numeros ordenados entre 0 y 100

# --------------------------------------------------------------------------------------

cantidadDeSumas = 0
suma = 0
sumaString = ''

while suma < 55:
    cantidadDeSumas = cantidadDeSumas + 1
    suma += listaDelUnoAlCien[cantidadDeSumas]
    sumaString += (str(cantidadDeSumas) + " + ")

print(f"la suma es {sumaString}")
print(f"la menor cantidad de sumas para llegar a 55 es: {cantidadDeSumas}")