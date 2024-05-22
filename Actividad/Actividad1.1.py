
NJoel1=5.64
NJoel2=3.45
NJoel3=4.56

NAlondra1=4.56
NAlondra2=5.64
NAlondra3=6.91

NPaz1=3.45
NPaz2=4.01
NPaz3=6.23

PromedioJoel=NJoel1+NJoel2+NJoel3
PromedioAlondra=NAlondra1+NAlondra2+NAlondra3
PromedioPaz=NPaz1+NPaz2+NPaz3

PromedioTodos = (PromedioJoel+PromedioAlondra+PromedioPaz)/3

print(" ")
print("Las notas de los estudiantes son:")
print(" ")

print("Joel:", "|", NJoel1, "|", NJoel2, "|", NJoel3, "|")
print("Promedio:", round((NJoel1+NJoel2+NJoel3)/3,3))
print(" ")

print("Alondra:", "|", NAlondra1, "|", NAlondra2, "|", NAlondra3, "|")
print("Promedio:", round((NAlondra1+NAlondra2+NAlondra3)/3,3))
print(" ")

print("Paz:", "|", NPaz1, "|", NPaz2, "|", NPaz3, "|")
print("Promedio:", round((NPaz1+NPaz2+NPaz3)/3,3))
print(" ")
print(" ")

print("La Nota Minima de cada Estudiante es:")
print(" ")
print("Joel:", min(NJoel1, NJoel2, NJoel3))
print(" ")
print("Alondra:", min(NAlondra1, NAlondra2, NAlondra3))
print(" ")
print("Paz:", min(NPaz1, NPaz2, NPaz3))
print(" ")
print(" ")

print("El Promedio de todos los Estudiantes es:", round(PromedioTodos,3))
print(" ")
print(" ")