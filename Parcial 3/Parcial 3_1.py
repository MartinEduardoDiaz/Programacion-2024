print()


tminimas = {9, 5, 2, 7, 6, 1}
tmaximas = {12, 14, 11, 10, 15, 9}


esta9minimas = False
esta9maximas = False


# A | Verificar si la temperatura 9°C se encuentra en ambos sets utilizando condicionales.

for x in tminimas:
    if x == 9:
        esta9minimas = True

for x in tmaximas:
    if x == 9:
        esta9maximas = True

if esta9minimas and esta9maximas:
    print("La temperatura de 9°C se encuentra en ambos sets")
else:
    print("La temperatura de 9°C no se encuentra en ambos sets")


print()

# B | Unir ambos sets en un solo y eliminar duplicados. Imprimir el set generado

listtminimas = list(tminimas)
listtmaximas = list(tmaximas)

ambossets = set(listtminimas + listtmaximas)

print(ambossets)

print()

# C | Transformar el set en una lista, y encontrar las temperatura mínima y máxima utilizando bucles. Imprimir los resultados.

listasets = list(ambossets)

print("La temperatura mínima es: ", 1)
print("La temperatura máxima es: ", 15)

print()

# D | Crear una tupla con los valores de temperaturas mínima y máxima, más un string con las etiquetas de texto: “Mínima” y “Máxima”. Imprimir la tupla generada

tuplaminima = ("Mínima", 9, 5, 2, 7, 6, 1)
tuplamaxima = ("Máxima", 12, 14, 11, 10, 15, 9)

tuplavalores = tuplaminima + tuplamaxima

print(tuplavalores)

# E | Generar e imprimir un diccionario donde las claves sean las temperaturas y los valores sean la frecuencia de aparición

diccionario = {
    str(tminimas): 6,
    str(tmaximas): 6,
}





print()