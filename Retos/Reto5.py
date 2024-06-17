print()

n = int(input("Ingrese un Valor: "))
print()



# F(x) = F(x-1) + F(x-2)

numero = 1

while numero <= n:
    print(numero)
    numero+=(numero-1) + (numero-2)

print()