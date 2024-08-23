cuota_enero = 1000
incremento = 0.02

cuota_febrero = cuota_enero * (1 + incremento)
cuota_marzo = cuota_febrero * (1 + incremento)
cuota_abril = cuota_marzo * (1 + incremento)

print("El valor de la cuota en abril es: $" + str(cuota_abril))
