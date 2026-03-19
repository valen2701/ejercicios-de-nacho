ciudades = {
    "Buenos Aires": {"pais": "Argentina", "poblacion": 3000000, "dato": "Buena comida"},
    "Madrid": {"pais": "España", "poblacion": 3200000, "dato": "lindas calles"},
    "Tokio": {"pais": "Japón", "poblacion": 14000000, "dato": "Muy poblada"}
}

for ciudad, info in ciudades.items():
    print(ciudad)
    for clave, valor in info.items():
        print(clave, valor)