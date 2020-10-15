import random

list = []
for i in range(0, 5): # genera una lista de 5 enteros aleatorios
    list.append(random.randint(0, 10))  # entre 0 y 10

#--------------------------------------------------------------------------
# se utiliza metodo burbuja explicado en clase 
# ordenar de MENOR a MAYOR
#--------------------------------------------------------------------------

print(list)
print('------------------------------------------------------------------')

for i in range(len(list)):
    ordenado = True

    for j in range(len(list) - i - 1):              #la burbuja se achica a medida que i va recorriendo el arreglo
        if list[j] > list[j + 1]:                   #para cambiar el orden reemplazar > por <
            list[j], list[j+1] = list[j+1], list[j] #intercambio de valores
            ordenado = False                        #si tuve que cambiar valores, entonces el arreglo esta desordenado y hay que chequear 1 vez mas                    
    print(list)                                     #solo para ver como se mueven los numeros en el arreglo
    if ordenado: 
        break                                       #si no se cambio ningun valor en la pasada de j, ya esta

print(list)