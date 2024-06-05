
'''

Guia de Estudio

Listas, Tuplas, Sets y Diccionarios


Ejercicio N°3

Un zoológico quiere organizar a sus animales en diferentes categorías. Crear un algoritmo
que pueda gestionar los animales en tres categorías: aves, animales terrestres y animales
acuáticos. Luego, mostrar los sets y utilizar las funciones correspondientes de Python para
manipular los sets.

a. Crear tres sets diferentes con los nombres de tres animales en cada uno: aves,
animales terrestres y animales acuáticos.
______________________________________________________
| Aves    | Animales Terrestres | Animales Acuáticos |
|_________|_____________________|____________________|
| Aguila  | León                | Pato               |
|_________|_____________________|____________________|
| Pato    | Elefante            | Delfín             |
|_________|_____________________|____________________|
| Canario | Nutria              | Nutria             |
|_________|_____________________|____________________|

b. Agregar un nuevo animal a cada set utilizando la función correspondiente en Python,
y mostrar los sets actualizados.
c. Encontrar y mostrar los animales que pueden pertenecer a más de una categoría
utilizando la función correspondiente.

'''

aves = set(["Aguila", "Pato", "Canario"])
animalesterrestres = set(["León", "Elefante", "Nutria"])
animalesacuaticos = set(["Pato", "Delfín", "Nutria"])

print(aves)