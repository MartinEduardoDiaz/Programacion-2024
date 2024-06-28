print()

matematicas = (55, 17, 93, 75, 88, 55)
quimica = (10, 85, 75, 88, 91, 75)
programacion = (68, 78, 85, 68, 82, 10)

materias = ('Matematicas', 'Quimica', 'Programación')
puntuacion = (matematicas, quimica, programacion)

# A
for i in range(len(materias)):
    asignaturas = materias[i]
    puntajes = puntuacion[i]

    temp = set()
    duplicados = []

    for j in puntajes:
        if j in temp:
            duplicados.append(j)
        else:
            temp.add(j)
    if duplicados:
        print(duplicados)

print()

# B

listamatematicas = list(matematicas)
listquimica = list(quimica)
listaprogramacion = list(programacion)

listatodas = [listamatematicas, listquimica, listamatematicas].sort()


# C

lista = set([listamatematicas, listquimica, listaprogramacion])