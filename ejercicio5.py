# A partir de los datos de pago por hora y de cantidad de
# horas trabajadas, calcular el sueldo de un operario sabiendo
# que si las horas trabajadas superan las 100, las horas
# excedentes se pagan doble.

# ---------------------------------------------------------------------

while True:

    pagoPorHora = float(input("Ingrese el sueldo por hora: "))
    cantHorasTrabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))

    if cantHorasTrabajadas > 100: #si trabajo mas de 100 horas, vale doble
        excedente = cantHorasTrabajadas - 100
        sueldo= (pagoPorHora * 100) + ((pagoPorHora * 2) * excedente) # el pago por las primeras 100h mas las horas excedentes al doble
    else:
        sueldo = pagoPorHora * cantHorasTrabajadas
    
    print(f"Le corresponde un monto de ${sueldo}p") # esto equivale a escribir print("Le corresponde un monto de $" + sueldo + "p")

    salir= str(input("salir? s/n: "))
    if salir.lower() == "s":
        break