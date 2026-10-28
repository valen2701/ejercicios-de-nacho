while True:
    edad = input("Edad (o salir): ")
    if edad == "salir":
        break
    edad = int(edad)

    if edad < 3:
        print("Gratis")
    elif edad <= 12:
        print("$10")
    else:
        print("$15")