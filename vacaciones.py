while True:
    print("**********************************")
    print("Sistema vacacional de una empresa.")
    print("********************************** \n")
    print("Existen 3 departamentos dentro de la empresa, con su respectiva clave.")
    print("Clave 1 - Atención al cliente.")
    print("Clave 2 - Logística.")
    print("Clave 3 - Gerencia. \n")

    nombre = input("Por favor, ingrese el nombre del Empleado: ")
    claveDep = int(input("Por favor, ingrese la clave del departamento: "))
    # antiguedad puede ser 5.7 anios
    antiguedad = float(input("Por favor, ingrese la antigüedad en años del empleado: "))

    
    if claveDep == 1:
        if antiguedad >= 1 and antiguedad < 2:
            print("El empleado ", nombre, " tiene derecho a 6 días de vacaciones.")
        elif antiguedad >=2 and antiguedad <= 6:
            print("El empleado ", nombre, " tiene derecho a 14 días de vacaciones.")
        elif antiguedad >=7:
            print("El empleado ", nombre, " tiene derecho a 20 días de vacaciones.")
        else:
            print("El empleado ", nombre, "aún no tiene derecho a vacaciones.")
    elif claveDep == 2:
        if antiguedad == 1 and antiguedad < 2:
            print("El empleado ", nombre, " tiene derecho a 7 días de vacaciones.")
        elif antiguedad >=2 and antiguedad <= 6:
            print("El empleado ", nombre, " tiene derecho a 15 días de vacaciones.")
        elif antiguedad >=7:
            print("El empleado ", nombre, " tiene derecho a 22 días de vacaciones.")
        else:
            print("El empleado ", nombre, "aún no tiene derecho a vacaciones.")
    elif claveDep == 3:
        if antiguedad == 1 and antiguedad < 2:
            print("El empleado ", nombre, " tiene derecho a 10 días de vacaciones.")
        elif antiguedad >=2 and antiguedad <= 6:
            print("El empleado ", nombre, " tiene derecho a 20 días de vacaciones.")
        elif antiguedad >=7:
            print("El empleado ", nombre, " tiene derecho a 30 días de vacaciones.")
        else:
            print("El empleado ", nombre, "aún no tiene derecho a vacaciones.")
    else:
        print("La clave no es correcta, vuelva a intentar.")

    salir= str(input("¿Desea salir? s/n: "))
    if (salir.lower() == "s"):
        break
