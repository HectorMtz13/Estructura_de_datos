#Dado un arreglo unidimencional de numeros enteros, ordenados crecientemente, escruba un programa que elimine todos los elementos repetisos.considere que de haber valores repetidos
# Estos se encontraran en posiciones consecutivas del arrelgo

Numeros = [1,2,4,4,4,5,7,9,11,11,13,14,15,16,16]
#y = set(Numeros)
#print(y)
unicos = []
for x in Numeros:
    if x not in unicos:
        unicos.append(x)
print(unicos)