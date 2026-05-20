#crear una clase y utilizar la misma lista, pero crear un objeto lista, que se reinicia al ser ingresara a cada metodo de ordenamiento

# lista = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]

# def bubblesort(lista):
#     n = len(lista)
    
#     for i in range(n):
#         intercambio = False
        
#         for j in range(0, n - i - 1):
#             if lista[j] > lista[j + 1]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#                 intercambio = True
#         if not intercambio:
#             break

# bubblesort(lista)
# print(lista)

#-------------------------------------------------------------------------------------------

# lista = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]
# def selectionsort(A):
#     n = len(A)
    
#     for i in range(n):
#         min_index = i
        
#         for j in range(i + 1, n):
#             if A[j] < A[min_index]:
#                 min_index = j
        
#         if min_index != i:
#             A[i], A[min_index] = A[min_index], A[i]

# selectionsort(lista)
# print(lista)



#--------------------------------------------------------------------------------------------------
# def ordnamiento_por_insercion(lista):
#     for i in range(1, len(lista)):
#         valor_actual = lista[i]
#         j = i-1


#         # desplazar elemento de la parte ordenada 
#         while j>= 0 and valor_actual < lista[j]:
#             lista[j+1] = lista[j]
#             j -=1
        
#         lista[j+1] = valor_actual

# lista = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]
# ordnamiento_por_insercion(lista)
# print("lista ordenada", lista)



#-----------------------------------------------------------------------------------------------
# def mergen_sort(lista):
#     if len(lista) > 1:
#         mid = len(lista) // 2
#         L = lista[:mid]
#         R = lista[mid:]

#         mergen_sort(L)
#         mergen_sort(R)

#         i = j = k = 0

#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 lista[k] = L[i]
#                 i += 1
#             else:
#                 lista[k] = R[j]
#                 j += 1
#             k += 1

#         while i < len(L):
#             lista[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(R):
#             lista[k] = R[j]
#             j += 1
#             k += 1

# lista = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]
# mergen_sort(lista)
# print(lista)



#-------------------------------------------------------------------------------------------------------
# def quick_sort(lista):
#     if len(lista) <= 1:
#         return lista
    
#     pivote = lista[len(lista)//2]

#     #separamos de elementos de comparacion
#     izquierda = [x for x in lista if x< pivote]
#     centro = [x for x in lista if x == pivote]
#     derecha = [x for x in lista if x > pivote]

#     return quick_sort(izquierda) + centro + quick_sort(derecha)

# lista = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]
# print(quick_sort(lista))



# import random

# def quick_sort_random(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = random.choice(arr)
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     return quick_sort_random(left) + middle + quick_sort_random(right)

# lista = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]
# print(quick_sort_random(lista))

#--------------------------------------------------------------------------------------------------------
def counting_sort(arr):
    if not arr:
        return []
    
    max_val = max(arr)

    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    # contar ocurrencias
    for num in arr:
        count[num] += 1

    # acumuladas
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # construir salida (esto va FUERA del for anterior)
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output


lista = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]
sorted_data = counting_sort(lista)
print(sorted_data)