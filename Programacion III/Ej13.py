contraseña_correcta = "AguanteProgramacionIII"
intentos = 3

while intentos > 0:
    contraseña_ingresada = input("Ingrese la contraseña: ")
    if contraseña_ingresada == contraseña_correcta:
        print("FELICITACIONES")
        break
    else:
        intentos -= 1
        print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
        if intentos == 0:
            print("CONTRASEÑA BLOQUEADA")
