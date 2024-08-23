horas_trabajadas = float(input("Ingrese el número de horas trabajadas en la semana: "))
precio_por_hora = float(input("Ingrese el precio por hora: "))

if horas_trabajadas <= 35:
    salario = horas_trabajadas * precio_por_hora
else:
    salario = (35 * precio_por_hora) + ((horas_trabajadas - 35) * (precio_por_hora * 1.5))

print("El salario neto semanal es: $" + str(salario))
