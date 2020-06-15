# dada una lista de 50 numeros se desea obtener el mayor de la lista, su posicion,
# el menor de la lista y su posicion
# --------------------------------------------------------------------------------------
import random

randomlist = []
for i in range(0, 49):
    randomlist.append(random.randint(0, 110))  # genera una lista de 50 numeros aleatorios entre 0 y 110

# --------------------------------------------------------------------------------------

numeroMayor = 0   # inicio la variable a 0 para que si o si haya un valor mas grande para contabilizar
numeroMenor = 110 # inicio la variable al valor max, para asegurarme que si o si haya un valor mas chico para contabilizar
posMayor = 0
posMenor = 0

for index in range(0, len(randomlist)):

    if randomlist[index] > numeroMayor:
        numeroMayor = randomlist[index]
        posMayor = index
    elif randomlist[index] < numeroMenor:
        numeroMenor = randomlist[index]
        posMenor = index


print(randomlist)

print(f"El mayor numero de la lista es {numeroMayor}, su posicion es: {posMayor}")
print(f"El menor numero de la lista es {numeroMenor}, su posicion es: {posMenor}")