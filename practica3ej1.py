# 1) Calcular el promedio de N números dados, siendo el valor de
# N variable, pero conocido de antemano.

# ---------------------------------------------------------------------------------

ene = int(input("Cual es el valor de N? -> "))
suma= 0

for numeros in range(ene): # la variable numeros va adquiriendo valores entre 0 y N con cada iteracion
    # numeros = int(input("ingrese numero: ")) <- tambien podria pedir al usuario cada numero pero directamente voy a tomar el indice como input
    suma += numeros        # esto equivale a decir suma = suma + numeros - con cada vuelta va agregando el valor de cada numero

promedio = suma / ene

print("El promedio de los %s numeros es %s" % (ene, promedio)) # otra forma de construir una string con variables