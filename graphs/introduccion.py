Nodes = ["A","B","C","D","E","F"]
Grafos = {"A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F"],
"D": ["B"], "E": ["B", "F"], "F": ["C", "E"]}

def matriz_adjacencia(grafo):
    matriz = [[0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]
    for i in range(len(Nodes)):
        for j in range(len(Nodes)):
            if Nodes[j] in grafo[Nodes[i]]:
                matriz[i][j] = 1
    return matriz

def BFS(grafo, start):
    visited = []
    queue = []
    visited.append(start)
    queue.append(start)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbor in grafo[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
            
BFS(Grafos, "C")

Nodes = ["A","B","C","D","E","F"]
Grafos = {"A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F"],
"D": ["B"], "E": ["B", "F"], "F": ["C", "E"]}

def matriz_adjacencia(grafo):
    matriz = [[0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]
    for i in range(len(Nodes)):
        for j in range(len(Nodes)):
            if Nodes[j] in grafo[Nodes[i]]:
                matriz[i][j] = 1
    return matriz

def BFS(grafo, start):
    visited = []
    queue = []
    visited.append(start)
    queue.append(start)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbor in grafo[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
            
BFS(Grafos, "C")