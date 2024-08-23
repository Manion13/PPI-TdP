def suma_y_multiplicacion(lista):
    suma = 0
    multiplicacion = 1
    for numero in lista:
        suma += numero
        multiplicacion *= numero
    return suma, multiplicacion
