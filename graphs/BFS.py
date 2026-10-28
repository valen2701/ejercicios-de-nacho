from collections import deque


# Grafo no dirigido: cada vértice guarda la lista de sus vecinos.
# El orden de los vecinos determina cuál se visita primero si hay opciones.
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}


def bfs(grafo, inicio):
    """Recorre el grafo por niveles y devuelve el orden de visita."""
    # La cola permite visitar primero los vértices descubiertos antes.
    visitados = {inicio}
    cola = deque([inicio])
    recorrido = []

    while cola:
        vertice = cola.popleft()
        recorrido.append(vertice)

        # Agregamos cada vecino no visitado para procesarlo después.
        for vecino in grafo[vertice]:
            if vecino not in visitados:
                # Se marca al agregarlo para no ponerlo dos veces en la cola.
                visitados.add(vecino)
                cola.append(vecino)

    return recorrido


# Empezamos el recorrido desde A.
print("BFS (anchura):", " -> ".join(bfs(grafo, "A")))