# debe tener este formato para correrlo, debe de estar dentro de cd Estructura_de_datos
# para correr el poryecto solo escribe : python server.py
# luego abre: http://localhost:5000

from flask import Flask, render_template, request, jsonify
import subprocess, sys, os

# crea la aplicacion web
app = Flask(__name__)

# lista de todos mis programas
# id       -> nombre unico para identificarlo
# carpeta  -> carpeta donde esta el archivo
# archivo  -> nombre exacto del archivo .py
# tipo     -> auto (no pide nada), input (pide datos)
# hint     -> instrucciones para el usuario
# ejemplo  -> valores de prueba para el input
PROGRAMAS = [
    # ---- Primera actividad ----
    {
        "id": "toneladas",
        "nombre": "Promedio de toneladas",
        "carpeta": "Primera actividad",
        "archivo": "Primer_Actividad.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },
    {
        "id": "calificaciones",
        "nombre": "Calificaciones de alumnos",
        "carpeta": "Primera actividad",
        "archivo": "Segundo_ejercicio.py",
        "tipo": "input",
        "hint": "primero escribe cuantos alumnos hay, luego una calificacion por linea",
        "ejemplo": "3\n8\n5\n9"
    },
    {
        "id": "letras",
        "nombre": "Frecuencia de letras",
        "carpeta": "Primera actividad",
        "archivo": "3ra actividad.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },
    {
        "id": "sin_rep",
        "nombre": "Eliminar repetidos",
        "carpeta": "Primera actividad",
        "archivo": "4ta_ejercicio.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },
    {
        "id": "matrices",
        "nombre": "Multiplicacion de matrices",
        "carpeta": "Primera actividad",
        "archivo": "Costo_mensual.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },

    # ---- Segunda actividad ----
    {
        "id": "busq_matriz",
        "nombre": "Busqueda en matriz",
        "carpeta": "Segunda actividad",
        "archivo": "# Nuestra matriz A.py",
        "tipo": "input",
        "hint": "escribe el numero que quieres buscar en la matriz, ejemplo: 7",
        "ejemplo": "7"
    },
    {
        "id": "asientos",
        "nombre": "Sistema de asientos",
        "carpeta": "Segunda actividad",
        "archivo": "Asientos.py",
        "tipo": "input",
        "hint": "escribe cuantas operaciones quieres hacer, luego por cada una: RESERVAR/LIBERAR/CONSULTAR, fila (1-6), columna (1-6)",
        "ejemplo": "2\nRESERVAR\n1\n1\nCONSULTAR\n1\n1"
    },
    {
        "id": "dataframe",
        "nombre": "Estadisticas Housing",
        "carpeta": "Segunda actividad",
        "archivo": "dataframe.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },

    # ---- Tercer Actividad ----
    {
        "id": "colas",
        "nombre": "Colas banco",
        "carpeta": "Tercer Actividad",
        "archivo": "colas.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },
    {
        "id": "bicola",
        "nombre": "Bicola (Deque)",
        "carpeta": "Tercer Actividad",
        "archivo": "bicola.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },
    {
        "id": "colas_mod",
        "nombre": "Colas modificadas",
        "carpeta": "Tercer Actividad",
        "archivo": "Colas_modificado.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },

    # ---- Cuarta Actividad ----
    {
        "id": "api_bicolas",
        "nombre": "API Bicolas",
        "carpeta": "Cuarta Actividad",
        "archivo": "Api(Bicolas).py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },
    {
        "id": "cola_circ",
        "nombre": "Cola Circular",
        "carpeta": "Cuarta Actividad",
        "archivo": "colas_circulares.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },
    {
        "id": "reintento",
        "nombre": "Reintento de tareas",
        "carpeta": "Cuarta Actividad",
        "archivo": "reintento_tareas.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },

    # ---- Quinta Actividad ----
    {
        "id": "dulces",
        "nombre": "Pila de dulces",
        "carpeta": "Quinta Actividad",
        "archivo": "dulces.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },
    {
        "id": "pila_ops",
        "nombre": "Operaciones de pila",
        "carpeta": "Quinta Actividad",
        "archivo": "operaciones_basicas.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },

    # ---- Sexta Actividad ----
    {
        "id": "cinco_ej",
        "nombre": "5 ejercicios de arboles",
        "carpeta": "Sexta Actividad",
        "archivo": "5_ejercicios.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },
    {
        "id": "arbolitos",
        "nombre": "Arbol BST clase",
        "carpeta": "Sexta Actividad",
        "archivo": "arbolitos_clase.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },
    {
        "id": "recorridos",
        "nombre": "Pre / In / Posorden",
        "carpeta": "Sexta Actividad",
        "archivo": "preorden,inorden,posorden.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },

    # ---- Septima Actividad ----
    {
        "id": "bfs",
        "nombre": "Busqueda en anchura BFS",
        "carpeta": "Septima Actividad",
        "archivo": "busqueda_anchura.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },
    {
        "id": "hanoi",
        "nombre": "Torre de Hanoi / Dijkstra",
        "carpeta": "Septima Actividad",
        "archivo": "torre_de_hanoi.py",
        "tipo": "input",
        "hint": "escribe el nodo inicial del 0 al 7, ejemplo: 0",
        "ejemplo": "0"
    },

    # ---- Octava Actividad ----
    {
        "id": "prim",
        "nombre": "Algoritmo de Prim",
        "carpeta": "Octava Actividad",
        "archivo": "algorithmo de prim.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },
    {
        "id": "ordenamiento",
        "nombre": "Metodos de ordenamiento",
        "carpeta": "Octava Actividad",
        "archivo": "metodo_ordenamiento.py",
        "tipo": "auto",
        "hint": "",
        "ejemplo": ""
    },
]


# carga la pagina principal
@app.route("/")
def index():
    return render_template("index.html", programas=PROGRAMAS)


# lee y devuelve el codigo fuente
@app.route("/codigo/<pid>")
def codigo(pid):
    # busca el programa por su id
    p = next((x for x in PROGRAMAS if x["id"] == pid), None)
    if not p:
        return jsonify({"error": "programa no encontrado"}), 404

    # arma la ruta completa al archivo
    ruta = os.path.join(os.path.dirname(__file__), p["carpeta"], p["archivo"])

    try:
        # abre el archivo y lo manda al navegador
        with open(ruta, encoding="utf-8") as f:
            return jsonify({"codigo": f.read(), "programa": p})
    except FileNotFoundError:
        return jsonify({"error": "no se encontro: " + ruta}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ejecuta el programa y devuelve el output
@app.route("/correr", methods=["POST"])
def correr():
    d = request.json

    # busca el programa en la lista
    p = next((x for x in PROGRAMAS if x["id"] == d.get("id")), None)
    if not p:
        return jsonify({"error": "programa no encontrado"}), 404

    ruta = os.path.join(os.path.dirname(__file__), p["carpeta"], p["archivo"])

    if not os.path.exists(ruta):
        return jsonify({"error": "archivo no existe: " + ruta}), 404

    try:
        # corre el archivo como subproceso
        r = subprocess.run(
            [sys.executable, ruta],
            input=d.get("inputs", ""),   # manda los inputs como si los escribiera el usuario
            capture_output=True,          # captura el print() del programa
            text=True,
            timeout=15,                   # maximo 15 segundos
            cwd=os.path.dirname(ruta)     # corre desde su propia carpeta (necesario para dataframe.py)
        )
        # regresa lo que imprimio el programa
        return jsonify({"stdout": r.stdout, "stderr": r.stderr, "code": r.returncode})

    except subprocess.TimeoutExpired:
        return jsonify({"error": "el programa tardo mas de 15 segundos"}), 408
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("\n  corriendo en: http://localhost:5000\n")
    # debug=True reinicia el servidor solo cuando cambias el codigo
    app.run(debug=True, port=5000)