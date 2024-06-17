print()

ciudades = ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
indice_calidad_del_aire = [134, 99, 245, 50]


print("La ciudad con el índice de calidad del aire más bajo es: ", ciudades[3], "con un índice de: ", indice_calidad_del_aire[3])


if indice_calidad_del_aire[3] <= 50 and indice_calidad_del_aire[3] >= 0:
    print("Está en la categoría 'Buena'")
elif indice_calidad_del_aire[3] >= 51 and indice_calidad_del_aire[3] <= 100:
    print("Está en la categoría 'Moderada'")
elif indice_calidad_del_aire[3] >= 101 and indice_calidad_del_aire[3] <= 150:
    print("Está en la categoría 'Dañina a la salud de grupos sensibles'")
elif indice_calidad_del_aire[3] >= 151 and indice_calidad_del_aire[3] <= 200:
    print("Está en la categoría 'Dañina a la salud'")
elif indice_calidad_del_aire[3] >= 201 and indice_calidad_del_aire[3] <= 300:
    print("Está en la categoría 'Muy dañina a la salud'")
elif indice_calidad_del_aire[3] > 300:
    print("Está en la categoría 'Peligrosa'")
else: print("Numero no valido")


print()


print("La ciudad con el índice de calidad del aire más alto es: ", ciudades[2], "con un índice de: ", indice_calidad_del_aire[2])

if indice_calidad_del_aire[2] <= 50 and indice_calidad_del_aire[2] >= 0:
    print("Está en la categoría 'Buena'")
elif indice_calidad_del_aire[2] >= 51 and indice_calidad_del_aire[2] <= 100:
    print("Está en la categoría 'Moderada'")
elif indice_calidad_del_aire[2] >= 101 and indice_calidad_del_aire[2] <= 150:
    print("Está en la categoría 'Dañina a la salud de grupos sensibles'")
elif indice_calidad_del_aire[2] >= 151 and indice_calidad_del_aire[2] <= 200:
    print("Está en la categoría 'Dañina a la salud'")
elif indice_calidad_del_aire[2] >= 201 and indice_calidad_del_aire[2] <= 300:
    print("Está en la categoría 'Muy dañina a la salud'")
elif indice_calidad_del_aire[2] > 300:
    print("Está en la categoría 'Peligrosa'")
else: print("Numero no valido")

print()


# Corregir.