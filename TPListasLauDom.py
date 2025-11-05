print("=== TP 5 - LISTAS EN PYTHON ===")
print()

# Actividad 1: Notas de estudiantes
print("1) NOTAS DE ESTUDIANTES")
notas = [8, 7, 9, 6, 8, 5, 7, 9, 8, 6]
print("Lista completa de notas:")

contador = 1
for nota in notas:
    print("Estudiante", contador, ":", nota)
    contador = contador + 1

suma_notas = 0
for nota in notas:
    suma_notas = suma_notas + nota

promedio = suma_notas / len(notas)
print("Promedio:", round(promedio, 2))

nota_mas_alta = notas[0]
for nota in notas:
    if nota > nota_mas_alta:
        nota_mas_alta = nota

nota_mas_baja = notas[0]
for nota in notas:
    if nota < nota_mas_baja:
        nota_mas_baja = nota

print("Nota más alta:", nota_mas_alta)
print("Nota más baja:", nota_mas_baja)

print()
print("=" * 50)

# Actividad 2: Productos
print("2) GESTIÓN DE PRODUCTOS")
productos = []

i = 0
while i < 5:
    producto = input("Ingrese el producto " + str(i+1) + ": ")
    productos.append(producto)
    i = i + 1

print("Lista ordenada alfabéticamente:")
productos_ordenados = sorted(productos)
for producto in productos_ordenados:
    print("- " + producto)

eliminar = input("Qué producto desea eliminar? ")
if eliminar in productos:
    productos.remove(eliminar)
    print("Producto eliminado correctamente")
else:
    print("Producto no encontrado")

print("Lista actualizada:")
for producto in productos:
    print("- " + producto)

print()
print("=" * 50)

# Actividad 3: Números pares e impares (sin random)
print("3) NÚMEROS PARES E IMPARES")
# Usamos números fijos en lugar de aleatorios
numeros = [45, 12, 78, 33, 90, 15, 67, 22, 89, 34, 56, 71, 28, 19, 60]
print("Lista original:", numeros)

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números pares (" + str(len(pares)) + "):", pares)
print("Números impares (" + str(len(impares)) + "):", impares)

print()
print("=" * 50)

# Actividad 4: Eliminar repetidos
print("4) ELIMINAR ELEMENTOS REPETIDOS")
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
print("Lista original:", datos)

sin_repetidos = []
for numero in datos:
    if numero not in sin_repetidos:
        sin_repetidos.append(numero)

print("Lista sin repetidos:", sin_repetidos)

print()
print("=" * 50)

# Actividad 5: Gestión de estudiantes
print("5) GESTIÓN DE ESTUDIANTES")
estudiantes = ["Ana", "Luis", "Maria", "Carlos", "Sofia", "Pedro", "Laura", "Diego"]
print("Lista inicial de estudiantes:")
for estudiante in estudiantes:
    print("- " + estudiante)

seguir = True
while seguir:
    print()
    print("Opciones:")
    print("1. Agregar estudiante")
    print("2. Eliminar estudiante")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == "1":
        nuevo = input("Ingrese el nombre del nuevo estudiante: ")
        estudiantes.append(nuevo)
        print("Estudiante", nuevo, "agregado")
    
    elif opcion == "2":
        eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
        encontrado = False
        for estudiante in estudiantes:
            if estudiante == eliminar:
                encontrado = True
                break
        
        if encontrado:
            estudiantes.remove(eliminar)
            print("Estudiante", eliminar, "eliminado")
        else:
            print("Estudiante no encontrado")
    
    elif opcion == "3":
        seguir = False
        print("Saliendo del gestor de estudiantes...")
    
    else:
        print("Opción inválida")
    
    if seguir:
        print("Lista actualizada:")
        for estudiante in estudiantes:
            print("- " + estudiante)

print()
print("=" * 50)

# Actividad 6: Rotar lista
print("6) ROTAR LISTA")
lista_numeros = [10, 20, 30, 40, 50, 60, 70]
print("Lista original:", lista_numeros)

# Rotar a la derecha
ultimo = lista_numeros[6]  # último elemento
temp = lista_numeros[0]    # guardamos el primero

# Movemos todos los elementos una posición
lista_numeros[0] = ultimo
lista_numeros[6] = lista_numeros[5]
lista_numeros[5] = lista_numeros[4]
lista_numeros[4] = lista_numeros[3]
lista_numeros[3] = lista_numeros[2]
lista_numeros[2] = lista_numeros[1]
lista_numeros[1] = temp

print("Lista rotada:", lista_numeros)

print()
print("=" * 50)

# Actividad 7: Temperaturas
print("7) TEMPERATURAS SEMANALES")
temperaturas = [
    [15, 25],
    [16, 27], 
    [14, 26],
    [17, 28],
    [16, 29],
    [15, 30],
    [18, 31]
]

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("Temperaturas de la semana:")
i = 0
while i < 7:
    print(dias[i] + ": Mínima", temperaturas[i][0], "°C, Máxima", temperaturas[i][1], "°C")
    i = i + 1

# Promedio de mínimas
suma_minimas = 0
for dia in temperaturas:
    suma_minimas = suma_minimas + dia[0]
prom_min = suma_minimas / 7

# Promedio de máximas
suma_maximas = 0
for dia in temperaturas:
    suma_maximas = suma_maximas + dia[1]
prom_max = suma_maximas / 7

print("Promedio de mínimas:", round(prom_min, 2), "°C")
print("Promedio de máximas:", round(prom_max, 2), "°C")

# Mayor amplitud térmica
amplitudes = []
for dia in temperaturas:
    amplitud = dia[1] - dia[0]
    amplitudes.append(amplitud)

mayor_amplitud = amplitudes[0]
dia_mayor = 0
for i in range(7):
    if amplitudes[i] > mayor_amplitud:
        mayor_amplitud = amplitudes[i]
        dia_mayor = i

print("Día con mayor amplitud térmica:", dias[dia_mayor], "(", mayor_amplitud, "°C)")

print()
print("=" * 50)

# Actividad 8: Notas de estudiantes por materia
print("8) NOTAS POR MATERIA")
notas_estudiantes = [
    [8, 7, 9],
    [6, 8, 7],
    [9, 9, 8],
    [7, 6, 8],
    [8, 7, 6]
]

materias = ["Matemática", "Programación", "Base de Datos"]

print("Promedio de cada estudiante:")
estudiante_num = 1
for estudiante in notas_estudiantes:
    suma = 0
    for nota in estudiante:
        suma = suma + nota
    promedio_est = suma / 3
    print("Estudiante", estudiante_num, ":", round(promedio_est, 2))
    estudiante_num = estudiante_num + 1

print()
print("Promedio de cada materia:")
for j in range(3):
    suma_materia = 0
    for estudiante in notas_estudiantes:
        suma_materia = suma_materia + estudiante[j]
    promedio_mat = suma_materia / 5
    print(materias[j] + ":", round(promedio_mat, 2))

print()
print("=" * 50)

# Actividad 9: Ta-Te-Ti
print("9) TA-TE-TI!!!")

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"], 
    ["-", "-", "-"]
]

print("  0 1 2")
fila_num = 0
for fila in tablero:
    print(fila_num, fila[0], fila[1], fila[2])
    fila_num = fila_num + 1

jugadores = ["X", "O"]
turno = 0
juego_terminado = False

while not juego_terminado and turno < 9:
    jugador_actual = jugadores[turno % 2]
    print("Turno de jugador", jugador_actual)
    
    movimiento_valido = False
    while not movimiento_valido:
        try:
            fila = int(input("Fila (0-2): "))
            columna = int(input("Columna (0-2): "))
            
            if fila >= 0 and fila <= 2 and columna >= 0 and columna <= 2:
                if tablero[fila][columna] == "-":
                    tablero[fila][columna] = jugador_actual
                    movimiento_valido = True
                else:
                    print("Casilla ocupada. Intente otra.")
            else:
                print("Posición inválida. Usar números entre 0 y 2.")
        except:
            print("Por favor, ingrese números válidos.")
    
    # Mostrar tablero actualizado
    print("  0 1 2")
    fila_num = 0
    for fila in tablero:
        print(fila_num, fila[0], fila[1], fila[2])
        fila_num = fila_num + 1
    
    # Verificar si hay ganador
    ganador = None
    
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != "-":
            ganador = fila[0]
    
    # Verificar columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != "-":
            ganador = tablero[0][col]
    
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != "-":
        ganador = tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != "-":
        ganador = tablero[0][2]
    
    if ganador is not None:
        print("¡El jugador", ganador, "gano!")
        juego_terminado = True
    
    # Verificar empate
    tablero_lleno = True
    for fila in tablero:
        for casilla in fila:
            if casilla == "-":
                tablero_lleno = False
    
    if tablero_lleno and ganador is None:
        print("¡Empate!")
        juego_terminado = True
    
    turno = turno + 1

print()
print("=" * 50)

# Actividad 10: Ventas de productos
print("10) VENTAS DE PRODUCTOS")
ventas = [
    [10, 15, 12, 8, 20, 18, 14],
    [5, 8, 6, 10, 7, 9, 12],
    [20, 25, 18, 22, 30, 28, 24],
    [3, 5, 4, 6, 7, 8, 10]
]

productos_nombres = ["Laptop", "Mouse", "Teclado", "Monitor"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("Total vendido por cada producto:")
for i in range(4):
    total = 0
    for venta in ventas[i]:
        total = total + venta
    print(productos_nombres[i] + ":", total, "unidades")

print()
print("Ventas por día:")
ventas_por_dia = [0, 0, 0, 0, 0, 0, 0]  # 7 días

for dia in range(7):
    total_dia = 0
    for producto in range(4):
        total_dia = total_dia + ventas[producto][dia]
    ventas_por_dia[dia] = total_dia
    print(dias_semana[dia] + ":", total_dia, "unidades")

# Día con mayores ventas
mayor_venta = ventas_por_dia[0]
dia_mayor = 0
for i in range(7):
    if ventas_por_dia[i] > mayor_venta:
        mayor_venta = ventas_por_dia[i]
        dia_mayor = i

print("Día con mayores ventas totales:", dias_semana[dia_mayor], "(", mayor_venta, "unidades)")

# Producto más vendido
totales_productos = []
for i in range(4):
    total = 0
    for venta in ventas[i]:
        total = total + venta
    totales_productos.append(total)

mayor_venta_producto = totales_productos[0]
producto_mayor = 0
for i in range(4):
    if totales_productos[i] > mayor_venta_producto:
        mayor_venta_producto = totales_productos[i]
        producto_mayor = i

print("Producto más vendido:", productos_nombres[producto_mayor], "(", mayor_venta_producto, "unidades)")

print()
print("TRabajo terminado!")