print()

# Ejemplo

edad = int(input("Ingrese su edad: "))
print()
if edad >= 0 and edad < 12:
    print("Eres un Niño")
elif edad >= 12 and edad < 18:
    print("Eres un Adolescente")
elif edad >= 18 and edad < 65:
    print("Eres Mayor de edad")
elif edad >= 65 and edad <= 120:
    print("Eres un Adulto Mayor")
else:
    print("Edad Invalida")

print()