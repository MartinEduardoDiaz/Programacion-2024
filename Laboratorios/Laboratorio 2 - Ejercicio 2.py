
print()

BreveResumen = str(input("Ingrese un breve resumen del articulo: "))
ResumenTrue = (len(BreveResumen) <= 60)



print()

print("La longitud de la variable que almacena el resumen es igual o menor a 60 caracteres: ", bool(ResumenTrue))

print()
print()

print("La Longitud de caracteres de el Resumen es: ", len(BreveResumen))

print()

print("Breve Resumen en Mayusculas: ", BreveResumen.upper())

print()

print("Los diez ultimos caracteres del Resumen: ", BreveResumen[-10], BreveResumen[-9], BreveResumen[-8], BreveResumen[-7], BreveResumen[-6], BreveResumen[-5], BreveResumen[-4], BreveResumen[-3], BreveResumen[-2], BreveResumen[-1])

print()

ResumenConGuion = '-'.join(BreveResumen.split())
print("Las palabras del resumen con un guión como separador: ", ResumenConGuion)

print()
print()