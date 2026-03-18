class ColaCircular:
    def __init__(self,capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = -1
        self.final = -1
    
    def esta_vacia(self):
        return self.frente == -1
    
    def esta_llena(self):
        return(self.final + 1) % self.capacidad == self.frente
    
    def escolar(self,dato):
        if self.esta_llena():
            print("la cola esta llena")
            return
        if self.esta_vacia():
            self.frente = 0
            self.final = 0
        else:
            self.final = (self.final + 1) % self.capacidad

        self.cola[self.final] = dato
    
    def desencolar(self):
        if self.esta_vacia():
            print("la cola esta vacia")
            return None
        
        dato = self.cola[self.frente]

        if self.frente == self.final:
            self.frente = -1
            self.final = -1
        
        else:
            self.frente = (self.frente + 1) % self.capacidad
        
        return dato
    
    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.cola[self.frente]
        
        
    def mostrar(self):
        if self.esta_vacia():
            print("cola vacia")
            return
        
        elementos = []
        i = self.frente

        while True:
            elementos.append(self.cola[i])
            if i == self.final:
                break
            i = (i + 1) % self.capacidad
        
        print("Cola : ", elementos)

#-------------------------------------------
cola = ColaCircular(5)

while True:
    print("\n1. insertar un turno en la cola")
    print("2. Atender turno eliminandolo de la cola")
    print("3. Mostrar e turno que eta al frente")
    print("4. mostrar todos los turnos actuales en orden")
    print("5. verificar si la cola esta llena o vacia ")
    print("6. Salir")

    op = input("Opcion: ")
    if op == "1":
        turno = input("Turno: ")
        cola.escolar(turno)
    elif op == "2":
        print("Atendiendo:", cola.desencolar())
    elif op == "3":
        print("Frente:", cola.ver_frente())
    elif op == "4":
        cola.mostrar()
    elif op == "5":
        print("Vacia:", cola.esta_vacia(), "| Llena:", cola.esta_llena())
    elif op == "6":
        break
    else:
        print("Opcion invalida")