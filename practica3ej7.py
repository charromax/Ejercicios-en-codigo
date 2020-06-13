# Dados dos números A y B construir un algoritmo que permita
# obtener A^B sin utilizar la operación de potencia.

#-------------------------------------------------------------------

base = int(input("ingrese la base: "))
potencia = int(input("ingrese la potencia: "))

resultado = 1
for indice in range(0, potencia):
    resultado *= base             # multiplica y adiciona resultado * base  
                                  # También existen las abreviaciones +=, -=, /=, y %=
print(resultado)