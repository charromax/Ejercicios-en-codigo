vector = [0, 1, 3, 1 ,3, 3, 1, 1, 5, 1]
contador = 0
for posicion in range(0,len(vector)):
    if vector[posicion] == 1:
        contador += 1

porcentaje = (contador * 100) / len(vector)
print(porcentaje)
