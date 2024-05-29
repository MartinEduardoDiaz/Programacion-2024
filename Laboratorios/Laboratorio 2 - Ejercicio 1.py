
PrecioManzana = int(100)
CantidadManzana = int(150)

PrecioPera = int(250)
CantidadPera = int(80)

PrecioDurazno = int(300)
CantidadDurazno = int(120)

print()

CompraManzana = int(input("Ingrese la cantidad de Manzanas que desea comprar: "))
CompraPera = int(input("Ingrese la cantidad de Peras que desee comprar: "))
CompraDurazno = int(input("Ingresar la cantidad de Duraznos que desea comprar: "))

print()

PrecioFinalManzanas = CompraManzana*CantidadManzana
PrecioFinalPeras = CompraPera*CantidadPera
PrecioFinalDuraznos = CompraDurazno*CantidadDurazno

print("El total a pagar por Manzanas es: ", PrecioFinalManzanas)
print("El total a pagar por Peras es: ", PrecioFinalPeras)
print("El total a pagar por Duraznos es: ", PrecioFinalDuraznos)

print()
print()

ManzanasYPeras = (CompraManzana*CantidadManzana) + (CompraPera*CantidadPera)
print("La suma total a pagar por la compra de Manzanas y Peras es: ", ManzanasYPeras)

print()

print("El valor máximo de los tres totales es: ", max(PrecioFinalManzanas, PrecioFinalPeras, PrecioFinalDuraznos))

print()

print("El valor minimo de los tres totales es: ", min(PrecioFinalManzanas, PrecioFinalPeras, PrecioFinalDuraznos))

print()

PromedioUnitario = (PrecioManzana + PrecioPera + PrecioDurazno)/3
print("El promedio del precio unitario de todas las frutas es: ", PromedioUnitario)

print()
print()