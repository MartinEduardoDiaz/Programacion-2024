
print("")
print("Ingrese el precio del Primer Producto")
Producto1precio=input()
print("Ingrese la cantidad del Primer Producto")
Producto1cantidad=input()
print("")
print("Ingrese la descripción del Primer Producto")
Producto1=input()

print("")
print("Ingrese el precio del Segundo Producto")
Producto2precio=input()
print("Ingrese la cantidad del Segundo Producto")
Producto2cantidad=input()
print("")
print("Ingrese la descripción del Segundo Producto")
Producto2=input()
print("")

intP1P=int(Producto1precio)
intP1C=int(Producto1cantidad)
intP2P=int(Producto2precio)
intP2C=int(Producto2cantidad)

TotalProducto1=intP1P*intP1C
TotalProducto2=intP2P*intP2C

print("")
print("Descripción del Primer Producto:")
print(Producto1)
print("")
print("Descripción del Segundo Producto:")
print(Producto2)
print("")


print("")
print("Valor Total del Inventario de los Productos:", TotalProducto1+TotalProducto2)
print("")
print("Precio Promedio de los Productos:", (TotalProducto1+TotalProducto2)/2)
print("")