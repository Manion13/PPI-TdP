n = int(input("Ingrese la cantidad de números: "))
positivos = 0
contador = 0

while contador < n:
    num = int(input("Ingrese un número: "))
    if num > 0:
        positivos += 1
    contador += 1

print("La cantidad de positivos es:" ,positivos)
