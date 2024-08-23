cadena = input("Ingrese una cadena de texto: ")
vocales = "aeiouAEIOU"
cantidad_vocales=0
for char in cadena:
    if char in vocales:
        cantidad_vocales+=1
print(f"Cantidad de vocales: {cantidad_vocales}")
