print()

'''
Determinar si una palabra ingresada por teclado es un palíndromo. Eliminar espacios y
convertir el texto ingresado a minúsculas. Además, imprimir la palabra invertida.
'''

palabra = str(input("Ingrese una palabra para determinar si es un palíndromo: ")).lower()
print()

menosuno = -1


while True:
    it = 0
    print(palabra[menosuno])
    menosuno -= 1
    if it > len(palabra):
        break




print()