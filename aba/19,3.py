activo = True

while activo:
    texto = input("Escribí algo (salir para terminar): ")
    if texto == "salir":
        activo = False
    else:
        print(texto)