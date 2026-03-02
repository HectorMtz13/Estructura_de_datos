def enque(lista, elemento):
    lista.append(elemento)

def deque(lista, lista2):
    enque(lista2, lista[0])
    lista.pop(0)

def peek(lista):
    return lista[0]

def is_empty(lista):
    return lista == []

def size(lista):
    return len(lista)

def retirar(lista, lista2):
    r = lista[0] - lista2[0]
    deque(lista, lista2)
    enque(lista, r)

def depositar(lista, lista2):
    r = lista[0] + lista2[0]
    deque(lista, lista2)
    enque(lista, r)


saldo = []
retiro = []
deposito = []
print(is_empty(saldo))
enque(saldo, 1000)
enque(saldo, 1000)
enque(saldo, 1000)
enque(saldo, 1000)
enque(saldo, 1000)

print(saldo)
retiro = [500]
print(saldo, retiro)
retirar(saldo, retiro)
retirar(saldo, retiro)
retirar(saldo, retiro)
retirar(saldo, retiro)
retirar(saldo, retiro)

print(saldo)
deposito = [300]
print(saldo, deposito)
depositar(saldo, deposito)
depositar(saldo, deposito)
depositar(saldo, deposito)
depositar(saldo, deposito)
depositar(saldo, deposito)
print(saldo)

# print(is_empty(lista))
# enque(lista,1)
# print(lista)
# print(is_empty(lista))
# enque(lista,3)
# enque(lista,2)
# print(peek(lista))
# print(size(lista))
# print(lista)


#Crear una pequena terminar de banco, en la cual vamos a trabajar con el enque,peek,size,deque y is_empty
#enque -> presentar el saldo a la persona, actualizar el saldo,retiro y agrego de deposito


# lista_clientes = [1000,1000,1000,1000,1000]
