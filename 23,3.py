while True:
    artista = input("Artista (salir): ")
    if artista == "salir":
        print("nos vimos en disney")
        break
    titulo = input("Álbum: ")
    print({"artista": artista, "titulo": titulo})