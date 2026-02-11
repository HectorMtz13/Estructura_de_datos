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


#_________________________________________2da Practica___________________________________________________

# En un arreglo unidimensional se almacena las calificaciones finales de n alumnos de un curso universitario

# a) El promedio general del curso
n = int(input("Ingrese el numero de alumnos: ")) # la lista de l=calificaciones era (alumnos = [8,8,7,5,10,9,9,5,6,10] )

calificaciones = []
for i in range(n):
    nota = float(input(f"Ingrese la calificación del alumno {i+1}: "))
    calificaciones.append(nota)
# a)
Promedio_general = sum(calificaciones) / len(calificaciones)
print(Promedio_general)

# b) Numero de alumnos que aprobaron y el numero de alumnos que reprobaron
Aprobados = [alumno for alumno in calificaciones if alumno >= 6.0]
Aprobados1 = len(Aprobados)
Reprobados = [alumno for alumno in calificaciones if alumno < 6.0]
Reprobados1 = len(Reprobados)
print(f"Numero de alumnos aprovados: {Aprobados1} ")
print(f"Numero de alumnos aprovados: {Reprobados1} ")

# c) El porcentaje de alumnos que aprobaron y reprobaron el curso
Porcentaje_Aprobados = (Aprobados1 / n) * 100
Porcentaje_Reprobados = (Reprobados1 / n ) * 100
print(f"Porcentaje de alumnos aprovados es : {Porcentaje_Aprobados}% ")
print(f"Porcentaje de alumnos Reprobados es : {Porcentaje_Reprobados}% ")

# d) Numero e alumnos cuya calificacion sea mayor o igual a 8
Alumnos_Mayor = [alumno for alumno in calificaciones if alumno >= 8.0]
Num_Alumnos_8 = len(Alumnos_Mayor)
print(f"La cantidad de alumnos con calificaicon mayor a 8.0 es : {Num_Alumnos_8}")



