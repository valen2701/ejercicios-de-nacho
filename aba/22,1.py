def hacer_camiseta():
    print("las opciones son las siguientes\n 1.S \n 2.M \n 3.L")
    ta = int(input("elegi tu talle: "))
    if ta == 1:
        talle = "S"
    elif ta == 2:
        talle = "M"
    else:
        talle = "L"
    impresion = input("deci la impresion: ")
    print(f"el talle es {talle} y su mensaje es {impresion}")


hacer_camiseta()