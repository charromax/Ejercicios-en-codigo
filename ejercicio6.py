# Las comisiones por ventas en una empresa se liquidan de
# acuerdo con las siguientes condiciones:

# - para importes menores que $500: el 5% del importe;
# - para importes iguales o mayores a $ 500 pero menores que $1000: el 6,5% del importe;
# - para importes iguales o mayores que $1000: el 6,5% del importe más $60.

# Dado el importe de una venta, calcular la comisión que se debe pagar al vendedor respectivo.

#-------------------------------------------------------------------------------------------------

while True:

    importeDeVenta = float(input("ingrese el importe de la venta: "))

    comision = None # equivale a valor NULL en otros lenguajes 

    if importeDeVenta > 0 and importeDeVenta < 500:
        comision = (importeDeVenta * 5) / 100 # el 5% de la venta

    elif importeDeVenta >= 500 and importeDeVenta < 1000:
        comision = (importeDeVenta * 6.5) / 100 # el 6.5% de la venta
    
    elif importeDeVenta >= 1000:
        comision = ((importeDeVenta * 6.5) / 100) + 60 # el 6.5% de la venta mas 60p

    else:
        print("Entrada Invalida, intente de nuevo") # cualquier otro valor no es considerado

    if comision: #si la variable es distinta de NULL da TRUE
        print(f"Su comision es: ${comision}")

    salir= str(input("salir? s/n: "))
    if salir.lower() == "s":
        break