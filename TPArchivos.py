import os

# Verificar si el archivo existe, si no, crearlo#
if not os.path.exists("productos.txt"):
    print("Creando archivo productos.txt...")
    with open("productos.txt", "w") as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno,450,15\n")
        archivo.write("Regla,85.75,20\n")

#2: Leer y mostrar productos#
print("\n--- PRODUCTOS EN EL ARCHIVO ---")
productos = []  

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        if len(datos) == 3:
            nombre = datos[0]
            precio = float(datos[1])
            cantidad = int(datos[2])
            
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
            
            #4: Cargar en lista de diccionarios#
            producto_dict = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            productos.append(producto_dict)  # Ahora productos está definida

#3: Agregar nuevo producto#
print("\n--- AGREGAR NUEVO PRODUCTO ---")
nuevo_nombre = input("Ingrese el nombre del producto: ")
nuevo_precio = float(input("Ingrese el precio del producto: "))
nueva_cantidad = int(input("Ingrese la cantidad del producto: "))

#Agregar solo a la lista#
productos.append({
    "nombre": nuevo_nombre,
    "precio": nuevo_precio,
    "cantidad": nueva_cantidad
})

print("Producto agregado a la lista!")

# 5: Buscar producto por nombre#
print("\n--- BUSCAR PRODUCTO ---")
nombre_buscar = input("Ingrese el nombre del producto a buscar: ")

encontrado = False
for producto in productos:
    if producto["nombre"].lower() == nombre_buscar.lower():
        print(f"Producto encontrado: {producto['nombre']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        encontrado = True

if not encontrado:
    print("Producto no encontrado.")

#6: Guardar TODOS los productos#
print("\n--- GUARDANDO TODOS LOS PRODUCTOS ---")
with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

print("¡Todos los productos guardados!")
print("Programa terminado!")