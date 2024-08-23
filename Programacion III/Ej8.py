n = int(input("Ingrese la cantidad de números: "))
suma = 0
contador = 0

while contador < n:
    num = int(input("Ingrese un número: "))
    suma += num
    contador += 1

print("La suma de los números es:" ,suma)
