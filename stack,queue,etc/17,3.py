lugares_favoritos = {
    "Juan": ["ee.uu", "estonia"],
    "manu": ["burger"],
    "azi": ["la matanza", "puerta de hierro"]
}

for nombre, lugares in lugares_favoritos.items():
    print(nombre)
    for lugar in lugares:
        print(lugar)