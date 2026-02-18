#__________________Ejercicio 5 ____________________
#Se realizara una mutilicacion de matricez en base a un listado
# Generar una multiplicacion entre una muliplicacion de la matriz a con la matriz b, y el sresultado se guardara en un anueva matriz c

A = [[5,6,13],
    [3,10,1],
    [2,11,3]]

B = [[1,2,1],
    [6,5,15],
    [3,11,12]]

resul = []
for i in range(len(A)):
    fil = []
    for j in range(len(A[0])):
        C = 0
        for x in range(len(B)):
            C+= A[i][x] * B[x][j]
            fil.append(C)
        resul.append(C)
print(resul)

#forma mas optima

