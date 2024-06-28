print()

texto = input("Ingrese una cadena de texto: ").lower()

# contadores para cada vocal

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

# iterar sobre caracter cadena de texto

for letra in texto:
    if letra == 'a':
        contador_a += 1
    if letra == 'e':
        contador_e += 1
    if letra == 'i':
        contador_i += 1
    if letra == 'o':
        contador_o += 1
    if letra == 'u':
        contador_u += 1

print("La letra 'a' aparece", contador_a, "veces")
print("La letra 'e' aparece", contador_e, "veces")
print("La letra 'i' aparece", contador_i, "veces")
print("La letra 'o' aparece", contador_o, "veces")
print("La letra 'u' aparece", contador_u, "veces")


print()