
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
print()
nombre2 = input("Ingrese el nombre de la segunda persona: "),
edad2 = input("Ingrese la edad de la segunda persona: ")
print()
nombre3 = input("Ingrese el nombre de la tercera persona: "),
edad3 = input("Ingrese la edad de la tercera persona: ")
print()

DiccionarioP = {
    "Nombre Persona 1":nombre1,
    "Edad Persona 1":edad1,
    "Nombre Persona 2":nombre2,
    "Edad Persona 2":edad2,
    "Nombre Persona 3":nombre3,
    "Edad Persona 3":edad3
}

print(f"Personas: ", DiccionarioP)

print()

print("Agrege los datos de la cuarta persona para que sea agregada al set")
print()
nombre4 = input("Ingrese el nombre de la cuarta persona: ")
edad4 = input("Ingrese la edad de la cuarta persona: ")

DiccionarioP.update({"Nombre Persona 4": nombre4})
DiccionarioP.update({"Edad Persona 4": edad4})

print()

print("Cuarta Persona Agregada:")
print(DiccionarioP)

print()

print("Una Persona Eliminada:")

