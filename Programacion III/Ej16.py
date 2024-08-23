nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M/F): ")

if (sexo == "F" and nombre < "M") or (sexo == "M" and nombre > "N"):
    grupo = "A"
else:
    grupo = "B"

print(f"Perteneces al grupo {grupo}.")
