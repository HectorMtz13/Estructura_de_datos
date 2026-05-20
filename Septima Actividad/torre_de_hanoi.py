# def hanoi(n, origen, auxiliar, destino):
#     if n == 1:
#         print(f"Disco 1: {origen} → {destino}")
#     else:
#         hanoi(n-1, origen, destino, auxiliar)
#         print(f"Disco {n}: {origen} → {destino}")
#         hanoi(n-1, auxiliar, origen, destino)

# # Ejecutar con 5 discos
# hanoi(5, 'A', 'B', 'C')


INF = float('inf')

grafo = {
    0: [(1, 9), (4, 6)],
    1: [(0, 9), (3, 8)],
    2: [(5, 6), (4, 5)],
    3: [(1, 8), (5, 1), (7, 7)],
    4: [(0, 6), (2, 5), (6, 3)],
    5: [(3, 1), (2, 6)],
    6: [(4, 3), (7, 2)],
    7: [(3, 7), (6, 2)]
}
def imprimir_matriz(grafo):
    n = len(grafo)
    matriz = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        matriz[i][i] = 0
        for vecino, peso in grafo[i]:
            matriz[i][vecino] = peso

    print("\nMatriz de adyacencia:")
    for fila in matriz:
        print(["∞" if x == float('inf') else x for x in fila])


def dijkstra(grafo, inicio):
    n = len(grafo)
    visitado = [False] * n
    dist = [float('inf')] * n
    dist[inicio] = 0

    print(f"\nNodo inicial: {inicio}")
    print("Distancias iniciales:", dist)

    for paso in range(n):
        min_dist = float('inf')
        u = -1

        for i in range(n):
            if not visitado[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:
            break

        visitado[u] = True
        print(f"\nPaso {paso+1}: Nodo {u} con distancia {dist[u]}")

        for vecino, peso in grafo[u]:
            if not visitado[vecino]:
                nueva_dist = dist[u] + peso
                if nueva_dist < dist[vecino]:
                    print(f"  → {vecino}: {dist[vecino]} → {nueva_dist}")
                    dist[vecino] = nueva_dist

        print("Distancias actuales:", dist)

    print("\nDistancias finales:")
    for i in range(n):
        print(f"Nodo {i}: {dist[i]}")

# ---- EJECUCIÓN ----
inicio = int(input("Ingresa el nodo inicial (0-7): "))

imprimir_matriz(grafo)
dijkstra(grafo, inicio)