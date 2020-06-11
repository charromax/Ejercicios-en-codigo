
# Dados dos números A y B: si los dos son positivos,
# sumarlos, en caso contrario multiplicarlos.

# ---------------------------------------------------------------------------------
while True:    
    numA= int(input("inserte un numero: "))

    numB= int(input("inserte otro numero: "))

    if (numA >= 0) and (numB >= 0):
        suma = numA + numB
        print("La suma es: " + str(suma))

    else:
        mult = numA * numB
        print("La multiplicacion es: " + str(mult))
    
    salir= str(input("desea salir? s/n: "))
    if (salir.lower() == "s"):
        break
    else:
        print("vamos de nuevo")
