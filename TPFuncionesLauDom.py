#TP Funciones Lau Dom#

# 1. F que imprime "Hola Mundo!!!#
def imprimir_hola_mundo():
    print("Hola Mundo!!!")

# 2. F que saluda al usuario por nombre#
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. F inf.personal#
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4. F para cálculos de círculo#
def calcular_area_circulo(radio):
    return 3.1416 * radio * radio

def calcular_perimetro_circulo(radio):
    return 2 * 3.1416 * radio

# 5. F para convertir segundos a horas#
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. F para mostrar tabla de multiplicar#
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# 7. F para operaciones básicas#
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return suma, resta, multiplicacion, division

# 8. F para calcular IMC#
def calcular_imc(peso, altura):
    return peso / (altura * altura)

# 9. F para convertir Celsius a Fahrenheit#
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. F para calcular promedio#
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# PROGRAMA PRINCIPAL
def main():
    print("=== PRÁCTICO 2: FUNCIONES EN PYTHON ===")
    
    # Ejercicio 1
    print("\n1. Ejercicio 1 - Hola Mundo:")
    imprimir_hola_mundo()
    
    # Ejercicio 2
    print("\n2. Ejercicio 2 - Saludo personalizado:")
    nombre = input("Ingrese su nombre: ")
    saludo = saludar_usuario(nombre)
    print(saludo)
    
    # Ejercicio 3
    print("\n3. Ejercicio 3 - Información personal:")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su ciudad de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    
    # Ejercicio 4
    print("\n4. Ejercicio 4 - Cálculos de círculo:")
    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")
    
    # Ejercicio 5
    print("\n5. Ejercicio 5 - Conversión de segundos a horas:")
    segundos = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")
    
    # Ejercicio 6
    print("\n6. Ejercicio 6 - Tabla de multiplicar:")
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)
    
    # Ejercicio 7
    print("\n7. Ejercicio 7 - Operaciones básicas:")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)
    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Multiplicación: {num1} × {num2} = {multiplicacion}")
    print(f"División: {num1} ÷ {num2} = {division}")
    
    # Ejercicio 8
    print("\n8. Ejercicio 8 - Cálculo de IMC:")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}")
    
    # Ejercicio 9
    print("\n9. Ejercicio 9 - Conversión de temperatura:")
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
    
    # Ejercicio 10
    print("\n10. Ejercicio 10 - Cálculo de promedio:")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    promedio = calcular_promedio(num1, num2, num3)
    print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")
    
    print("\n Fin")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()