asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = {}

for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    notas[asignatura] = nota

for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}.")
