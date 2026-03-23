from collections import deque

class Pila:
    def __init__(self):
        self.pila = []
        self.top = -1

    def push(self, elemento):
        self.pila.append(elemento)
        self.top += 1

    def __str__(self):
        return str(self.pila)


dulces = [
    12500.5, 11890.0, 13010.35, 14100.0, 13650.8, 14999.99, 15800.0, 16250.25, 15120.0, 14780.4, 13999.0, 15550.75
]

cola = deque(dulces)
pila = Pila()

while cola:
    n = len(cola)
    numero = cola.popleft()  # sacamos uno
    es_menor = True

    for x in range(n):
        actual = cola.popleft()

        if actual < numero:
            es_menor = False

        cola.append(actual)

    if es_menor:
        pila.push(numero)
    else:
        cola.append(numero)


print(pila)