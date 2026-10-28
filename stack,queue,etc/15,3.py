glosario = {
    "variable": "Es un espacio en memoria donde se guarda un dato.",
    "lista": "Es una colección de elementos ordenados que se pueden modificar.",
    "diccionario": "Es una colección de pares clave-valor.",
    "bucle": "Es una estructura que permite repetir un bloque de código.",
    "condicional": "Es una estructura que permite tomar decisiones en el programa."
}

for palabra, significado in glosario.items():
    print(f"{palabra}:\n  {significado}\n")