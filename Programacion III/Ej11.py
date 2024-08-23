positivos = 0
total = 0

while True:
    num = float(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    if num > 0:
        positivos += 1
    total += 1

print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad total de números ingresados: {total}")
