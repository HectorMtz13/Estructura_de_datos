# Rpresentar una sala con una matriz Asientos[F,C] booleana, donde FALSO = libre y verdadero = reservar

# Entradas
#  Dimenciones F y C
# k operando en formato , RESERVAR(I,J), LIBERAR(I,J), O CONSULTAR

A = [
    [0, 0, 0, 0, 0 , 0],
    [0, 0, 0, 0, 0 , 0],
    [0, 0, 0, 0, 0 , 0],
    [0, 0, 0, 0, 0 , 0],
    [0, 0, 0, 0, 0 , 0],
    [0, 0, 0, 0, 0 , 0]
]
#Los 0 son espacion libres
# F = filas
# C = columnas
# (Reservar, Liberar, Consultar)


def reservar(i, j):
    if A[i-1][j-1] == 0:
        A[i-1][j-1] = 1
        return (f"Ok : ({i},{j}) lo reservaste.")
    else:
        return (f"Rechazo ({i},{j}) esta ocupado.")

def liberar(i, j):
    if A[i-1][j-1] == 1:
        A[i-1][j-1] = 0
        return (f"vale ({i},{j}) ahora esta liberado.")
    else:
        return (f"RECHAZO({i},{j}) ya libre .")

def consultar(i, j):
    if A[i-1][j-1] == 0:
        return (f"({i},{j}) esta libre.")
    else:
        return (f"({i},{j}) esta reservado.")

n = int(input("Cuantas veces deseasrepetir esta accion : "))
for q in range(n):
    x = input("escribe lo que desees realizar (RESERVAR, LIBERAR, CONSULTAR): ")
    x = x.upper()

    i = int(input("Fila (1-6): "))
    j = int(input("Columna (1-6): "))

    if x == "RESERVAR":
        print(reservar(i, j))
    elif x == "LIBERAR":
        print(liberar(i, j))
    elif x == "CONSULTAR":
        print(consultar(i, j))
    else:
        print("Acción no válida.")

reservados = []
fila = []
for fila in A:
    total = sum(fila)
    reservados.append(total)
total_reservados = sum(reservados)

fila_mayor = reservados.index(max(reservados)) + 1


print (f"despues de las {n} operaciones")
print (f"total reservados = {total_reservados}")
print(f"fila con mas reservaciones {fila_mayor}")