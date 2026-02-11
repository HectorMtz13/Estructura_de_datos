#Actividad de python
Toneladas = [12, 24,16,15,20,18,6,10,12,11,15,12]

#   Promedio anual a)
#Sumas todos los datos del arreglo y dividirlos entre el total de los elementos 
Promedio_anual = sum(Toneladas) / len(Toneladas)
print(Promedio_anual)

# B)
#Realizar una comparacion de todos los valores vs promedio integrar un arreglo con todos los valores superiores al promedio 
Superior = [tonelada for tonelada in Toneladas if tonelada > Promedio_anual]
superior1 = (len(Superior))
print(superior1)
# c)
Inferior = [tonelada for tonelada in Toneladas if tonelada <  Promedio_anual]
inferior1 = len(Inferior)
print(Inferior)