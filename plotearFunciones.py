import matplotlib.pyplot as plt


# Get a

def get_a(pedacito):
    if pedacito == '': 
        a = 1
    elif pedacito == '-':
        a = -1
    else:
        a = float(pedacito)
    return a

# Get b

def get_b(pedacito):
    if pedacito == '': 
        b = 0
    else:
        b = float(pedacito)
    return b

# Draw multiple points.
def draw_multiple_points(a, b, maxValue, minValue, step, funcion):

    # x axis value list.
    x_number_list = list(range(minValue, maxValue, step))
    

    # y axis value list.
    y_number_list = list((a*x + b) for x in x_number_list)

    # Draw point based on above x, y axis values.
    plt.plot(x_number_list, y_number_list, linewidth = 1)

    # Set chart title.
    plt.title("Grafico para f(x) = " + funcion)

    # Set x, y label text.-10
    plt.xlabel("independiente")
    plt.ylabel("ordenada al origen")
    plt.show()

if __name__ == '__main__':

    funcion = (input("Ingrese la funcion que desea graficar: "))  # en formato ax + b  funcion lineal


    minVal = int(input("Ingrese valor minimo: "))
    maxVal = int(input("Ingrese valor maximo: "))
    step = int(input("Ingrese el paso: "))

    fun_cortada = funcion.split('x') # dividir la cadena a partir del caracter x, obteniendo a y b

    a_factor = get_a(fun_cortada[0])
    b_factor = get_b(fun_cortada[1].replace(' ', ''))

    draw_multiple_points(a_factor, b_factor, maxVal, minVal, step, funcion)