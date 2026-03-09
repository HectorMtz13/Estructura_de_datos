from collections import deque

def enqueue(q: deque, elemento):
    q.append(elemento)

def dequeue(q: deque):
    return q.popleft()  # toma el primer elemento y lo elimina

def peek(q: deque):
    return q[0]

def is_empty(q: deque) -> bool:
    return len(q) == 0

def size(q: deque) -> int:
    return len(q)


def retirar(saldos: deque[int], monto: int, historial: deque[int] | None = None) -> None:
    saldo_original = dequeue(saldos)
    if historial is not None:
        enqueue(historial, saldo_original)
    nuevo_saldo = saldo_original - monto
    enqueue(saldos, nuevo_saldo)


def depositar(saldos: deque[int], monto: int, historial: deque[int] | None = None) -> None:
    saldo_original = dequeue(saldos)
    if historial is not None:
        enqueue(historial, saldo_original)
    nuevo_saldo = saldo_original + monto
    enqueue(saldos, nuevo_saldo)


# ___________________________________________________________________________
saldos = deque()
historial_saldos = deque()
historial_depositos = deque()

print(is_empty(saldos))

for _ in range(5):
    enqueue(saldos, 1000)

monto_retiro = 500

for _ in range(5):
    retirar(saldos, monto_retiro, historial_saldos)

print("historial (saldo antes del retiro): ", list(historial_saldos))
print("saldos finales ", list(saldos))

for _ in range(5):
    enqueue(saldos, 1000)  # aquí estaba el error

monto_deposito = 300

for _ in range(5):
    depositar(saldos, monto_deposito, historial_depositos)

print("Historial (antes de depósito):", list(historial_depositos))
print("Saldos finales:", list(saldos))