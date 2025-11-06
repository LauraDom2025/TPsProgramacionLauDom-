#1- # Añadir nuevas frutas con sus respectivos precios#

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario actualizado:", precios_frutas)

#2- Actualizar los precios de las frutas#

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario con precios actualizados:", precios_frutas)

#3- crea una lista que contenga las frutas SIN los precios#

lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

#4-programa que permita almacenar y consultar números telefónicos#
contactos = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número telefónico: ")
    contactos[nombre] = telefono

nombre_consulta = input("Ingrese el nombre a consultar: ")
if nombre_consulta in contactos:
    print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print("El contacto no existe.")
    
#5-Solicita al usuario una frase e imprime...#
frase = input("Ingrese una frase: ")
palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print("Recuento:", recuento)

#6-nombres de 3 alumnos, y para cada uno una tupla de 3 notas,mosrar promedio#
alumnos = {}

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")
    
#7-Dos listas de estudiantes que aprobaron parcial1 y parcial2...#
parcial1 = {"Ana", "Luis", "Carlos", "María"}
parcial2 = {"Juan", "Luis", "Sofía", "Ana"}

ambos = parcial1 & parcial2
print("Aprobaron ambos:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno:", solo_uno)

total_aprobados = parcial1 | parcial2
print("Total de aprobados:", total_aprobados)

#8-Armá un diccionario donde las claves sean nombres de productos y los valores su stock.#
stock = {"Manzanas": 50, "Peras": 30, "Naranjas": 40}

while True:
    producto = input("Ingrese el producto a consultar (o 'salir' para terminar): ")
    if producto.lower() == "salir":
        break
    
    if producto in stock:
        print(f"Stock de {producto}: {stock[producto]}")
        agregar = input("¿Desea agregar unidades? (si/no): ")
        if agregar.lower() == "si":
            unidades = int(input("Ingrese la cantidad a agregar: "))
            stock[producto] += unidades
    else:
        print("Producto no encontrado.")
        agregar_nuevo = input("¿Desea agregarlo? (si/no): ")
        if agregar_nuevo.lower() == "si":
            unidades = int(input("Ingrese el stock inicial: "))
            stock[producto] = unidades

print("Stock final:", stock)

#9-Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.#
agenda = {
    ("lunes", "10:00"): "Reunión de trabajo",
    ("martes", "15:00"): "Clase de inglés"
}

dia = input("Ingrese el día: ")
hora = input("Ingrese la hora (HH:MM): ")

clave = (dia, hora)
if clave in agenda:
    print(f"Evento: {agenda[clave]}")
else:
    print("No hay eventos programados para esa fecha y hora.")
    
#10-Dado un diccionario que mapea nombres de países con sus capitales...#
paises = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia"}

capitales_paises = {}
for pais, capital in paises.items():
    capitales_paises[capital] = pais

print("Diccionario invertido:", capitales_paises)