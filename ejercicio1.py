
'''
Se cuenta con tres tuplas: la primera contiene los puntajes más altos obtenidos por
estudiantes en Matemáticas. La segunda tupla contiene los puntajes más altos en Química.
Por último, la tercera tupla contiene los puntajes más altos en Programación.
'''

Puntajes_M = (55, 17, 93, 75, 88, 55)
Puntajes_Q = (10, 85, 75, 88, 91, 75)
Puntajes_P = (68, 78, 85, 68, 82, 10)


duplicados_matematicas = set([x for x in Puntajes_M if Puntajes_M.count(x) > 1])

print(duplicados_matematicas)