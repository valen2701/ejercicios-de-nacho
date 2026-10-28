# Usamos los mismos vértices y las mismas conexiones que en lista_adyacente.py.
vertices = ["A", "B", "C", "D"]

# Las filas y las columnas siguen el orden de la lista "vertices".
# Un 1 indica que hay una arista; un 0 indica que no hay conexión.
# Por ejemplo, la fila de A es [0, 1, 1, 0]:
# A no tiene conexión consigo mismo, sí con B y C, y no con D.
matriz = [
    [0, 1, 1, 0],  # Conexiones de A
    [1, 0, 0, 1],  # Conexiones de B
    [1, 0, 0, 1],  # Conexiones de C
    [0, 1, 1, 0],  # Conexiones de D
]

# Imprimimos los nombres de las columnas y cada fila con su vértice.
print("  " + " ".join(vertices))
for vertice, fila in zip(vertices, matriz):
    print(f"{vertice} " + " ".join(str(valor) for valor in fila))