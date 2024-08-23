tipo_hamburguesa = input("¿Quieres una hamburguesa vegetariana? (si/no): ")
ingredientes_comunes = ["lechuga", "queso", "tomate"]

if tipo_hamburguesa == "si":
    tipo = "vegetariana"
    ingredientes = ["calabaza", "soja"]
else:
    tipo = "no vegetariana"
    ingredientes = ["carne vacuna", "carne de pollo"]

print(f"Elige un ingrediente adicional para tu hamburguesa {tipo} (además de {', '.join(ingredientes_comunes)}):")
for i, ingrediente in enumerate(ingredientes):
    print(f"{i + 1}. {ingrediente}")

eleccion = int(input("Ingresa el número del ingrediente que deseas: "))
ingrediente_adicional = ingredientes[eleccion - 1]

print(f"Tu hamburguesa {tipo} llevará {', '.join(ingredientes_comunes)} y {ingrediente_adicional}.")
