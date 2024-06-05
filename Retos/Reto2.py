
print()

nombre_estudiante = input("Ingrese el nombre del Estudiante: ")

print()

nombre_asignatura_1 = input("Ingrese el nombre de la Primera Asignatura: ")
nota1_a1 = int(input("Ingrese la Nota del Laboratorio 1: "))
nota2_a1 = int(input("Ingrese la Nota del Laboratorio 2: "))
nota3_a1 = int(input("Ingrese la Nota del Laboratorio 3: "))

print()

nombre_asignatura_2 = input("Ingrese el nombre de la Segunda Asignatura: ")
nota1_a2 = int(input("Ingrese la Nota del Laboratorio 1: "))
nota2_a2 = int(input("Ingrese la Nota del Laboratorio 2: "))
nota3_a2 = int(input("Ingrese la Nota del Laboratorio 3: "))

print()

nombre_asignatura_3 = input("Ingrese el nombre de la Tercera Asignatura: ")
nota1_a3 = int(input("Ingrese la Nota del Laboratorio 1: "))
nota2_a3 = int(input("Ingrese la Nota del Laboratorio 2: "))
nota3_a3 = int(input("Ingrese la Nota del Laboratorio 3: "))



# Ponderación

NotaFinalA1 = (nota1_a1*0.3) + (nota2_a1*0.5) + (nota3_a1*0.2)
NotaFinalA2 = (nota1_a2*0.3) + (nota1_a2*0.5) + (nota3_a2*0.2)
NotaFinalA3 = (nota1_a3*0.3) + (nota2_a3*0.5) + (nota3_a3*0.2)

NotaFinalPonderada = (NotaFinalA1 + NotaFinalA2 + NotaFinalA3)/3


# Tuplas

TuplaAsignatura1 = tuple(nombre_asignatura_1, set(nota1_a1, nota2_a1, nota3_a1), NotaFinalA1)
TuplaAsignatura2 = tuple(nombre_asignatura_2, set(nota1_a2, nota2_a2, nota3_a2), NotaFinalA2)
TuplaAsignatura3 = tuple(nombre_asignatura_3, set(nota1_a3, nota2_a3, nota3_a3), NotaFinalA3)




print()

nombre_estudiante = {
    "Nombre de la Primera Asignatura": nombre_asignatura_1,
    "Nota 1 Asignatura 1": nota1_a1,
    "Nota 2 Asignatura 1": nota2_a1,
    "Nota 3 Asignatura 1": nota3_a3,

    "Nombre de la Segunda Asignatura": nombre_asignatura_2,
    "Nota 1 Asignatura 2": nota1_a2,
    "Nota 2 Asignatura 2": nota2_a2,
    "Nota 3 Asignatura 2": nota3_a2,

    "Nombre de la Tercera Asignatura": nombre_asignatura_3,
    "Nota 1 Asignatura 3": nota1_a3,
    "Nota 2 Asignatura 3": nota2_a3,
    "Nota 3 Asignatura 3": nota3_a3,

    "Nota Final Ponderada": round(NotaFinalPonderada, 1)
}

print(nombre_estudiante)