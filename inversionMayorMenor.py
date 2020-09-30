# Cargar un vector de 100 elementos. Encontrar el valor
# máximo y el valor mínimo e intercambiar sus posiciones.
# Imprimir el vector resultante.
# --------------------------------------------------------------------------------------
import random

vector = []
for i in range(0, 100):
    vector.append(random.randint(-100, 100))  # genera una lista de 100 numeros aleatorios entre -100 y 100

# --------------------------------------------------------------------------------------

numeroMayor = vector[0]   # inicio la variable al primer valor de la lista
numeroMenor = vector[0]   # 
posMayor = 0
posMenor = 0

#---------------------------------------------------------------------------------------

for item in vector:
    if item > numeroMayor:
        numeroMayor = item
        posMayor = vector.index(item)
    if item < numeroMenor:
        numeroMenor = item
        posMenor = vector.index(item)

print("menor = ", (numeroMenor, posMenor))
print("mayor = ", (numeroMayor, posMayor))
vector[posMenor] = numeroMayor
vector[posMayor] = numeroMenor   # invierto las posiciones del mayor y el menor


for item in vector:
    print((item, vector.index(item)))
    

    