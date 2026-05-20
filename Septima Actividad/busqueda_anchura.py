#Busqueda de anchura

    #       A
    #     /   \
    #    B     C
    #   / \   /  \
    #  D   E F    G
#Busqueda de anchura maneja una cola
#debe imprimir una listaA[B,C], B[D,E], C[F,G], D[], E[], F[], G[]
# que tome el grafo, lo reciba y lo haga una lista
# y vamos a ir agregandolos a una lista cada ve que se hayan atendido cada proceso

from collections import deque

def Busqueda_Anchura(graph, start):
    visited = set()
    queue = deque([start])
    recorrido = []

    while queue:
        node = queue.popleft()
        print(f"Sale: {node} -> Cola: {list(queue)}")
        if node not in visited:
            visited.add(node)
            recorrido.append(node)
            print(f"{node}[{','.join(graph[node])}]")
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    print(f" Entra: {neighbor} -> Cola: {list(queue)}")

    print("Recorrido final:")
    print(" ".join(recorrido))

graph = {'A': ['B', 'C'],'B': ['D', 'E'],'C': ['F', 'G'],'D': [],'E': [],'F': [],'G': []}
Busqueda_Anchura(graph, 'A')
