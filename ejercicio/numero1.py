print()

numero = int(input("Ingrese su número a adivinar: "))

while True:
    numero2 = int(input("Ingrese un número: "))
    if numero2 == numero:
        print("Adivinaste el número")
        break
    if numero2 > numero:
        print("El número es mayor al número a adivinar")
    if numero2 < numero:
        print("El número es menor al número a adivinar")

print()