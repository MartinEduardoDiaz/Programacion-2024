# Definición de Variable

saludo = "Hola Mundo!"

print(saludo[0])


# Concatenación

print(saludo+" "+"Hola hola")





# Números

estatura = 1.70
peso = 70

# Potencia

imc = peso/(estatura**2)



# Bibliotecas

import math
print(math.trunc(imc))





# BOOLEANOS

print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
ampolleta = False
interruptor = True


# Función Type

print(type(ampolleta),type(interruptor))
print(type(imc))
print(type(peso))

# Salidas Booleanas
print(1 <= 0)
print(100 >= 10)
print(19 == 19)



print("\n")


# Declaración de Booleanos
print(bool(" "))
print(bool("False"))
print(bool([]))
print(bool(0))
print(bool(1))



print("\n")



# Utilizando la Función Bool
print(bool(0))
print(bool(1))



# Listas
print("Listas\n")

ciudades = ["Castro", "Queilen", "Ancud", "Quellón", "Chonchi", "Castro"]
varios = ["Nicolas", 20, True]
lista2 = list(["Python", "Ruby"])


print(type(ciudades))

print(ciudades)
print(varios)


# len cuenta la cantidad de elementos de una lista
print(len(ciudades))

# .count cuenta la cantidad de ocurrencias de un elemento en una variable (cuantas veces se repite una cosa)
print(ciudades.count("Castro"))

# Impresion de un elemento en especifico de una lista
print(ciudades[3])

listanumeros=[1,2,3,4,5,6,7,8,9,10]
numeros=listanumeros
print(numeros)



# Lista

list = [1,2,3,4,5,6,7,8,9,10]
listnum = list(range(1,3)) # funcion de rango


ciudades[0] = "Quemchi"
print(ciudades)





# Tuplas

musica = tuple()
generos = ("Rock", "Pop", "Swing", "HipHop")

print(generos)
print(type(generos))

print(generos[2])  # Imprime el elemento en esa posición
print(generos.index["Rock"])  # imprime la posicisión de ese elemento


# Las tuplas no se pueden cambiar, son inmutables


