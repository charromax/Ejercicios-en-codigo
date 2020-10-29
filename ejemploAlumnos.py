# Se posee un listado de los alumnos, de 1º a 7º grado de una
# escuela primaria. Para cada uno de los alumnos se poseen los
# siguientes datos:
#  Nro. de Legajo
#  Grado que cursa (codificado de 1 á 7)
#  Edad
# Los datos no poseen ningún orden. No se conoce la cantidad de
# alumnos de la escuela, pero un Nro. de Legajo igual a cero indica el fin
# de los datos.
# Se desea saber:
# c) La cantidad de alumnos de cada grado.
# d) El promedio de edad de cada grado

# -----------------------------------------------------------------------------
import random

rows, cols = (20, 3)
arr = [[random.randint(0, 100),random.randint(1, 7),random.randint(6, 12) ] for j in range(rows)]
for i in range(rows):
    print(arr[i])

#     genero una matriz con 3 columnas: legajo(0-100), curso(1-7), edad(6-12)
#-------------------------------------------------------------------------------

r, c = (2, 8)
resultados = [[0,0,0,0,0,0,0,0]for j in range(r)] #arreglo holder para los contadores y sumadores

#-----------------------------------------------------------------------------------

for i in range (0, rows):
    grado = arr[i][1]
    resultados[0][grado] += 1
    resultados[1][grado] += arr[i][2]
for i in range (1, c):
    suma = resultados[1][i]
    resultados[1][i] = suma / resultados[0][i]

print(resultados[0])
print(resultados[1])