# _____________________________________3ra Practica___________________________________________

#Dada una cadena de caracters como dato, desea  saber el numero de veces que aparecen las letras 'a','b. . . 'z' en dicha cadena. Escriba un porgrama que resuelva el problema'
# Cuantas letras tiene la cadena, cuantas vocales hay de manera indivsual?
# a) Si uso  arreglos .Cuantos necesito?Porque?
# b) Existe otra forma de resolverlo?

import array
cadena = "Parangaricutirimicuaro"
letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for x in letras:
    cadena = cadena.lower()
    cantidad = cadena.count(x)
    if cantidad > 0:
        print(x, ":", cantidad)

# Con arreglos
cadena = "Parangaricutirimicuaro".lower()
cadena_arreglo = list(cadena)

letras = ['abcdefghijklmnopqrstuvwxyz']
letras_arreglo = list(letras[0])
for x in letras_arreglo:
    cantidad = cadena_arreglo.count(x)
    if cantidad > 0:
        print(x, ":", cantidad)