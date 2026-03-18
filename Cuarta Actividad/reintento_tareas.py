#Actividad de reintentos de tareas
#Documentcion de mi tarea
from collections import deque


tareas_iniciales = [
    ("T1", 1, 0),
    ("T2", 0, 0),
    ("T3", 2, 0),
    ("T4", 1, 0),
    ("T5", 2, 2),
    ("T6", 2, 1),
]
bicola = deque(tareas_iniciales)

def formato_bicola(b):
    return " -> ".join([f"{t[0]}(f={t[1]},i={t[2]})" for t in b])

print("Simulación de datos para reintento de tareas fallidas (Bicola)\n")
print(f"{'Turno'} {'Tarea':<6} {'Operación':<24} {'Resultado':<14} Bicola resultante")
print("-------------------------------------------------------------------------------------")

turno = 1

while bicola:
    nombre, fallos, intentos = bicola.popleft()
    intentos += 1

    if fallos == 0:

        bicola.append((nombre, fallos, intentos))
        bicola.pop()
        resultado = "Completada"
    else:
        fallos -= 1
        bicola.append((nombre, fallos, intentos))
        resultado = "Falla"

    estado = formato_bicola(bicola)
    print(f"{turno:<7} {nombre:<6} {resultado:<14} {estado if estado else '(vacía)'}")
    turno += 1
