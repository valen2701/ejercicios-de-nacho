# Grafo no dirigido: cada vértice guarda la lista de sus vecinos.
# El orden de los vecinos determina cuál se visita primero si hay opciones.
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}


def dfs(grafo, inicio):
    """Recorre el grafo en profundidad y devuelve el orden de visita."""
    visitados = set()
    recorrido = []

    def visitar(vertice):
        # Marcamos el vértice antes de explorar vecinos para evitar repetirlo.
        visitados.add(vertice)
        recorrido.append(vertice)

        # DFS sigue por un vecino y avanza lo más lejos posible antes de volver.
        for vecino in grafo[vertice]:
            if vecino not in visitados:
                visitar(vecino)

    visitar(inicio)
    return recorrido


# Empezamos el recorrido desde A.
print("DFS (profundidad):", " -> ".join(dfs(grafo, "A")))