cadena = input("Ingrese una cadena de texto: ")
es_palindromo = cadena == cadena[::-1]

if es_palindromo:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
