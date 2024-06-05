
'''

Guia de Estudio

Listas, Tuplas, Sets y Diccionarios


Ejercicio N°4

Implementar un algoritmo que permita ingresar el nombre y la edad de tres personas. Esta
información se debe almacenar en un diccionario. Se debe realizar las siguientes
operaciones:

a. Ingresar el nombre y la edad de tres personas por consola y almacenarlos en un
diccionario. Imprimir el nombre y la edad de cada persona.
b. Agregar una nueva persona al diccionario.
c. Eliminar una persona del diccionario.
d. Mostrar el diccionario actualizado.

'''

print()

nombre1 = input("Ingrese el nombre de la primera persona: "),
edad1 = input("Ingrese la edad de la primera persona: ")

diccionario1 = {
    "Nombre":nombre1,
    "Edad":edad1
}


print()

nombre2 = input("Ingrese el nombre de la segunda persona: "),
edad2 = input("Ingrese la edad de la segunda persona: ")

diccionario2 = {
    "Nombre":nombre2,
    "Edad":edad2
}


print()

nombre3 = input("Ingrese el nombre de la tercera persona: "),
edad3 = input("Ingrese la edad de la tercera persona: ")

diccionario3 = {
    "Nombre":nombre3,
    "Edad":edad3
}


print()

print(diccionario1)
print(diccionario2)
print(diccionario3)