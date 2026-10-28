# Grafo no dirigido: cada arista se puede recorrer en ambos sentidos.
# Por ejemplo, A está conectada con B y también B está conectada con A.
# Cada clave es un vértice y su lista contiene sus vértices vecinos.
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}

# Recorremos el diccionario para mostrar los vecinos de cada vértice.
for vertice, vecinos in grafo.items():
    print(f"{vertice} esta conectado con: {', '.join(vecinos)}")