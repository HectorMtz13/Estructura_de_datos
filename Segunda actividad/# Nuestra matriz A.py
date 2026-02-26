# Nuestra matriz A
# Sacar la lista de coordenadas (i,j) donde A(i,j) = x (Lodas las ocurrencias)
#Mensaje "no encontreado" si no hay coincidencias

A = [
    [4,7,2,9,5,7],
    [1,3,7,6,8,0],
    [9,2,5,7,4,6],
    [8,7,1,3,7,2],
    [5,0,6,4,2,9],
    [7,8,9,2,1,7]
]
# x = int(input("Ingresa el valor que deses busccar dentro de la matriz : "))
# coordenadas = []

# for i in range(len(A[0])):
#     for j in range(len(A[0])):
#         if A[i][j] == x:
#             coordenadas.append((i+1, j+1))
# if coordenadas == []:
#     print("no encontrado")
# else:
#     print("Coordenadas encontradas: ", coordenadas)


# def coordenadas(A,x):
#     coordenadas = []

#     for i in range(len(A[0])):
#         for j in range(len(A[0])):
#             if A[i][j] == x:
#                 coordenadas.append((i+1, j+1))
#     if coordenadas == []:
#         print("no encontrado")
#     else:
#         print("Coordenadas encontradas: ", coordenadas)
# coordenadas(A,7)

x = int(input("Ingresa el valor que deseas buscar dentro de la matriz: "))
coordenadas = [(i+1, j+1) for i, fila in enumerate(A) for j, valor in enumerate(fila) if valor == x]

if coordenadas:
    print("Coordenadas encontradas:", coordenadas)
else:
    print("no encontrado")
