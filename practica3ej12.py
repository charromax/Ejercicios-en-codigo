# 12) Hallar el máximo de una lista de N números (N>1, variable
# pero conocido de antemano).
# ------------------------------------------------------------------------

ene = int(input("Cual es el valor de N? -> "))

numMasAlto= 0              # inicio el numero mas alto como 0 al principio de la operacion
listaDeNumerosIngresados = []
for numeros in range(ene): # la variable numeros va adquiriendo valores entre 0 y N con cada iteracion
    numero = int(input("ingrese numero: "))
    if numero > numMasAlto:
        numMasAlto = numero      # si el numero ingresado es el mas alto HASTA AHORA, entonces el numero mas alto pasa a ser el numero ingresado
    listaDeNumerosIngresados.append(numero)          # lo agrego a la lista de numeros ingresados

print(f"El numero mas alto en la lista {listaDeNumerosIngresados} es: {numMasAlto}")
