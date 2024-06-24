print()


tupla_ZC = (8848, 8611, 8586, 8200, 8460, 8200)
tupla_ZS = (8848, 5567, 8125, 4560, 8051, 4560)
tupla_ZA = (2200, 2500, 1000, 2200, 3623, 990)

print("Se imprimen los números duplicados:")
print(tupla_ZC[3]*2, tupla_ZC[5]*2)
print(tupla_ZS[3]*2, tupla_ZS[5]*2)
print(tupla_ZA[0]*2, tupla_ZA[3]*2)


print()

tuplaset_ZC = set(tupla_ZC)
tuplaset_ZS = set(tupla_ZS)
tuplaset_ZA = set(tupla_ZA)

print("Se imprime la intersección:")
print(tuplaset_ZC.intersection(tuplaset_ZS))


print()


tupla_todas = tupla_ZC + tupla_ZS + tupla_ZA

tupla_sin_duplicados = set(tupla_todas)

print("Se imprime la tupla sin numeros duplicados:")
print(tupla_sin_duplicados)


print()


tupla_final = tuple(tupla_sin_duplicados)

tupla_a_lista = [tupla_final]

print("Se imprime la tupla convertida en lista:")
print(tupla_a_lista)


print()