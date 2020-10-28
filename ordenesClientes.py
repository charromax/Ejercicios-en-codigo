# Ejemplo 1: Durante un mes una imprenta recibe Órdenes de Pedido de
# sus clientes, cada orden de pedido posee los siguientes datos:

#  Código de Cliente (codificado de 1 á 100)
#  Cantidad de Formularios

# Un cliente puede realizar más de una orden de pedido en el mes, los
# datos se ingresan desordenados. Un código de Cliente igual a cero
# indica el fin de los datos.

# Se desea saber:
# a) La cantidad de órdenes de pedido mensuales que realiza cada
# Cliente.
# b) La cantidad total de formularios comprados en el mes por cada
# Cliente.

# ------------------------------------------------------------------------------
import random

rows, cols = (100, 2) 
arr = [[random.randint(0, 10) for i in range(cols)] for j in range(rows)] 
for i in range(rows):
    print(arr[i])

#-------------------------------------------------------------------------------


cantForms = [0 for i in range(101)]
cantPedidos = [0 for i in range(101)]
for i in range(rows):
    cantForms[arr[i][0]] += arr[i][1]
    cantPedidos[arr[i][0]] += 1

client_id = int(input("ingrese la id del cliente(0 - 10) para recibir informacion: "))
print('buscando info....')
print('')
print('-----------------------------------------------------------------------------')
print(f"El cliente {client_id} realizo {cantPedidos[client_id]} pedidos, por un total de {cantForms[client_id]} formularios")