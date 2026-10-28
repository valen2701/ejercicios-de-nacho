respuestas = {}

while True:
    nombre = input("Nombre: ")
    lugar = input("¿A dónde irías? ")
    respuestas[nombre] = lugar

    seguir = input("¿Continuar? (si/no): ")
    if seguir == "no":
        break

for nombre, lugar in respuestas.items():
    print(nombre, "->", lugar)