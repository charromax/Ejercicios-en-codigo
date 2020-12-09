import random

# crear y rellenar un array 'arr' de 5 filas y 3 columnas

rows, cols = (5, 3) 
arr = [[random.randint(0, 10) for primerElemento in range(cols)] for j in range(rows)] 
for primerElemento in range(rows):
    print(arr[primerElemento])

# ---------------------------------------------------------------------------
# inicio algoritmo burbuja 2d
# --------------------------------------------------------------------------

for primerElemento in range(rows - 1):
    for sigElemento in range (primerElemento + 1, rows):                    #en python las filas y columnas se nombran empezando desde 0
                                                     #por eso se resta 1 mas que el ejemplo en clase
        if totalFacturado[primerElemento][2] < arr[sigElemento][2]:#<-                  cambiando este valor cambia la columna de ordenamiento
            aux = arr[primerElemento]
            arr[primerElemento] = arr[sigElemento]
            arr[sigElemento] = aux

print('--------------------------------------------------------------------')
for primerElemento in range(rows):
    print(arr[primerElemento])
