import random

# crear y rellenar un array 'arr' de 5 filas y 3 columnas

rows, cols = (5, 3) 
arr = [[random.randint(0, 10) for i in range(cols)] for j in range(rows)] 
for i in range(rows):
    print(arr[i])

# ---------------------------------------------------------------------------
# inicio algoritmo burbuja 2d
# --------------------------------------------------------------------------

for i in range(rows - 1):
    for z in range (i + 1, rows):                    #en python las filas y columnas se nombran empezando desde 0
                                                     #por eso se resta 1 mas que el ejemplo en clase
        if arr[z][2] < arr[i][2]:#<-                  cambiando este valor cambia la columna de ordenamiento
            aux = arr[i]
            arr[i] = arr[z]
            arr[z] = aux

print('--------------------------------------------------------------------')
for i in range(rows):
    print(arr[i])