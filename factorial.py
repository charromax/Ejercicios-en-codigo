while True:
    print(".....................................................")
    print("Dado un número entero positivo, mostrar su factorial.")
    print("..................................................... \n")

    numero = int(input("Ingrese un número entero: "))      #Le pedimos al usuario un numero 

    fact =1                         #esta variable "f" representa al factorial, la iniciamos en 1.

    if numero >= 0:                  #condición planteada por el ejercicio, que el numero sea mayor que 0.
        for i in range(1, numero+1):      #el bucle se va a repetir desde 1 hasta el numero que ingrese el usuario.
            fact = fact * i                      #asi se resuelve el factorial
        print("El factorial de ", numero, "es: ",fact)
    else:
        print("Por favor, ingrese un número entero positivo.")

    salir= str(input("¿Desea salir? s/n: "))     #ignorar, esto pregunta al usuario si quiere salir 
    if (salir.lower() == "s"):                   #sino sale, vuelve a ejecturar el programa  
        break
    else:
        print("Vamos de nuevo.")