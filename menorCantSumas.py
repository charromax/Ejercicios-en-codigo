import random

def create_list():
    '''
    :return:

    '''
    randomlist = []
    for i in range(0, 100):
        randomlist.append(random.randint(0, 100))  
    return randomlist

# --------------------------------------------------------------------------------------

cantidadDeSumas = 0
suma = 0
sumaString = ''
list = create_list()

for num in list:
    suma += num
    sumaString += (str(list[cantidadDeSumas]) + " + ")
    cantidadDeSumas = cantidadDeSumas + 1
    if suma > 55:                                  # otra forma es romper el bucle for con break
        break


print(f"la suma es {sumaString}")
print(f"la menor cantidad de sumas para llegar a 55 es: {cantidadDeSumas}")