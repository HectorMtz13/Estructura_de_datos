class nodoArbol:
    
    def __init__(self,valor):
        self.valor = valor
        self.hijos = []
        
    def agregar_hijos(self,nodo):
        self.hijos.append(nodo)

    def mostrar(self, nivel = 0):
        print(" " * nivel + f"- {self.valor}")
        for hijo in self.hijos:
            hijo.mostrar(nivel + 1)

raiz = nodoArbol("SOFTWARE")
maestro1 = nodoArbol("morgan")
maestro2 = nodoArbol("boyain")
alumno1 = nodoArbol("Hector")
alumno2 = nodoArbol("Martinez")

raiz.agregar_hijos(maestro1)
raiz.agregar_hijos(maestro2)

maestro1.agregar_hijos(alumno1)
maestro2.agregar_hijos(alumno2)

raiz.mostrar()




#___________Segundo ejercicio_______________

class nodoBinario:
    def __init__(self,valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

raiz = nodoBinario(12)
raiz.izquierdo = nodoBinario(6)
raiz.derecho = nodoBinario(17)

raiz.izquierdo.izquierdo = nodoBinario(5)
raiz.izquierdo.derecho = nodoBinario(7)

print("raiz", raiz.valor)
print("raiz izquierdo (hijo)" , raiz.izquierdo.valor)
print("raiz derecho (hijo)" , raiz.derecho.valor)



#________--Tercer ejercicio --__________

def inorden(nodo):
    if nodo:
        inorden(nodo.izquierdo)
        print(nodo.valor, end= " ")
        inorden(nodo.derecho)
print("recorrido")
inorden(raiz)



#_________--Cuarto ejercicio --_______
class Nodo:
    def __init__(self, letra):
        self.letra = letra
        self.hijos = []
        self.fin = False


raiz = Nodo("")

def insertar(palabra):
    nodo = raiz
    
    for letra in palabra:
        encontrado = None
        
        
        for hijo in nodo.hijos:
            if hijo.letra == letra:
                encontrado = hijo
                break
        
        if encontrado is None:
            nuevo = Nodo(letra)
            nodo.hijos.append(nuevo)
            nodo = nuevo
        else:
            nodo = encontrado
    
    nodo.fin = True


insertar("mar")
insertar("malo")
insertar("mas")


def sugerencias(nodo, prefijo):
    if nodo.fin:
        print(prefijo)
    
    for hijo in nodo.hijos:
        sugerencias(hijo, prefijo + hijo.letra)


def buscar(prefijo):
    nodo = raiz
    
    for letra in prefijo:
        encontrado = None
        
        for hijo in nodo.hijos:
            if hijo.letra == letra:
                encontrado = hijo
                break
        
        if encontrado is None:
            print("No hay palabras")
            return
        
        nodo = encontrado
    
    sugerencias(nodo, prefijo)

print("Sugerencias para 'ma':")
buscar("ma")

#----------- quinto ejercicio =----------
class NodoABB:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def insertar(raiz, valor):
    if raiz is None:
        return NodoABB(valor)
    
    if valor < raiz.valor:
        raiz.izq = insertar(raiz.izq, valor)
    else:
        raiz.der = insertar(raiz.der, valor)
    
    return raiz

valores = [50, 25, 75, 10, 30, 60, 90]
raiz = None

for v in valores:
    raiz = insertar(raiz, v)




