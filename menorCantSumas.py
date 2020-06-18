import random

randomlist = []
for i in range(0, 100):
    randomlist.append(random.randint(0, 100))  # genera una lista de 50 numeros aleatorios entre 0 y 110

# --------------------------------------------------------------------------------------

cantidadDeSumas = 0
suma = 0
sumaString = ''

for num in randomlist:
    suma += num
    sumaString += (str(randomlist[cantidadDeSumas]) + " + ")
    cantidadDeSumas = cantidadDeSumas + 1
    if suma > 55:                                  # otra forma es romper el bucle for con break
        break

print(f"la suma es {sumaString}")
print(f"la menor cantidad de sumas para llegar a 55 es: {cantidadDeSumas}")