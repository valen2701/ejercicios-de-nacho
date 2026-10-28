def hacer_sandwich(*ingredientes):
    print("Preparando un sándwich con:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")
    print("¡Listo!\n")

hacer_sandwich("jamón", "queso")
hacer_sandwich("lechuga", "tomate", "pollo", "mayonesa")
hacer_sandwich("palta")
