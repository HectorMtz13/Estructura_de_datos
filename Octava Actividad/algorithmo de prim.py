import heapq

def prim(grafo, inicio):
    visitados = set()
    heap = []
    orden = []

    heapq.heappush(heap, (0, inicio))

    while heap:
        peso, nodo = heapq.heappop(heap)
        if nodo in visitados:
            continue
        visitados.add(nodo)
        orden.append(nodo)

        for vecino, peso_arista in grafo[nodo]:
            if vecino not in visitados:
                heapq.heappush(heap, (peso_arista, vecino))
    return orden



grafo = {
    0: [(2, 20), (1, 10)],
    1: [(0, 10), (4, 10), (3, 50)],
    2: [(0, 20), (3, 20), (4, 33)],
    3: [(2, 20), (4, 20), (5, 2), (1, 50)],
    4: [(2, 33), (1, 10), (3, 20), (5, 1)],
    5: [(4, 1), (3, 2)]
}

resultado = prim(grafo,2)
print(resultado)