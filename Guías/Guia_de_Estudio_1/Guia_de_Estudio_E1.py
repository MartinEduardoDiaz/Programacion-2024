
'''

Guia de Estudio

Listas, Tuplas, Sets y Diccionarios


Ejercicio N°1

Crear un programa que permita ingresar 4 marcas de bebidas gaseosas y almacenarlas en
una lista. Luego, mostrar la lista completa y el nombre de la primera y última bebida.

a. Ingresar 4 nombres de marcas de bebida por consola y almacenarlos en una lista.
b. Imprimir la lista completa.
c. Mostrar el primer y último nombre de las bebidas de la lista.

'''

print()
bebida1 = input("Ingrese el nombre de la Primera Bebida: ")
bebida2 = input("Ingrese el nombre de la Segunda Bebida: ")
bebida3 = input("Ingrese el nombre de la Tercera Bebida: ")
bebida4 = input("Ingrese el nombre de la Cuarta Bebida: ")

list = [bebida1, bebida2, bebida3, bebida4]

print()
print("Lista: ")
print(list)

print()
print("Primero y Ultimo de la Lista")
print(list[0], list[3])

print()