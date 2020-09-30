# En un proceso anterior se cargó en memoria un arreglo
# unidimensional de 80 elementos reales. Se pide exhibirlo por
# pantalla ordenado de menor a mayor.

#---------------------------------------------------------------------------

import random

list = []
for i in range(0, 5): # genera una lista de 80 reales aleatorios
    list.append(round(random.uniform(0.0, 5.0), 2))  

#--------------------------------------------------------------------------
# se utiliza metodo burbuja
#--------------------------------------------------------------------------

print(list)
print('------------------------------------------------------------------')
ordenado = False
while ordenado == False:
    ordenado = True
    for i in range(len(list) - 1):
        if list[i] < list[i+1]: 
            mayor = list[i]
            list[i] = list[i+1]  #se intercambian los valores
            list[i+1] = mayor
            ordenado = False     #cuando llegue al penultimo elemento
                                 #si ya no se cumple la condicion se asume ordenado el array

print(list)