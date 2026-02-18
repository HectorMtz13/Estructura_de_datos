import pandas as pd
import math as math
# Leer archivos CSV delimitado por comas (por defecto)
df = pd.read_csv('./Housing.csv')

#Mostrar las primeras 5 filas
lista = df['price']

def housingStats(str):
    lista = list(df[str])
    media(lista)
    moda(lista)
    varianza(lista)
    desviacion_estandar(lista)

def media(lista):
    suma = 0
    for i  in lista:
        suma += i
    media = suma/len(lista)
    return print( "Media -> ", media)

def moda(lista):
        moda = 0
        modaf = lista[0]
        for i in lista:
            if lista.count(i) > moda:
                moda = lista.count(i)
                modaf = i
        return print("Moda -> ", modaf)

def varianza(lista):
    media = sum(lista) / len(lista)
    Varianza = sum((x - media) ** 2 for x in lista) / (len(lista))
    return print("Varianza -> ", Varianza)

def desviacion_estandar(lista):
    media = sum(lista) / len(lista)
    varianza = sum((x - media) ** 2 for x in lista) / (len(lista))
    desviacion_estandar = math.sqrt(varianza)
    return print("Desviacion estandar -> ", desviacion_estandar)

housingStats('yr_built')