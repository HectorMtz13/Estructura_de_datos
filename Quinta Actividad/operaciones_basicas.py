class Pila:
    def __init__(self):
        self.pila = []
        self.top = -1

    def push(self, elemento):
        self.pila.append(elemento)
        self.top += 1

    def pop(self):
        if self.is_empty():
            return "La pila está vacía"
        self.top -= 1
        return self.pila.pop()

    def peek(self):
        if self.is_empty():
            return "La pila está vacía"
        return self.pila[self.top]

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1