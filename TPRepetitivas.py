#1) crea un cod que vaya de 1 a 100
numero = 0
while numero <100:
    print(numero)
    numero+=1
    
#2) cod. cantidad de dígitos de un número
numero = input("Ingrese un número entero ")
numero_entero = int(numero)
numero_sin_signo = str(abs(numero_entero))

cantidad_dig = len(numero_sin_signo)
print("El numero ", numero, "tiene", cantidad_dig, "dígitos")

#3) suma de los números entre dos extremos
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1>num2:
    num1, num2 = num2, num1
    
suma = 0
for i in range(num1 + 1, num2):
    suma += i
print(f"La suma de los números entre {num1} y {num2} es: {suma}")

#4) Sumar números hasta que ingrese 0
print ("Ingrese números enteros para sumar ")
print ("Ingrese 0 para terminar y ver el resultado ")

suma_total = 0
numero = 1

while numero != 0:
    numero = int(input ("Ingrese un número: "))
    suma_total += numero
print ("la suma total es ", suma_total)

#5) Adivinanza
print("Adivina un número entre 0 y 9")

import random
numero_secreto = random.randint(0, 9)
intentos = 0
adivinanza = -1

while adivinanza != numero_secreto:
    adivinanza = int(input("¿Qué número crees que es? "))
    intentos += 1
    
    if adivinanza == numero_secreto:
        print(f"¡Correcto!El número era {numero_secreto}")
    else:
        print("Incorrecto. ¡Sigue intentando!")
print(f"Necesitaste {intentos} intentos.")

#6)  todos los números pares comprendidos entre 0 y 100, en orden decreciente. 
print("Números pares entre 0 y 100 (orden decreciente):")
print("-----------------------------------------------")

for numero in range(100, -1, -2):
    print(numero)
    
#7) suma de números
numero = int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(numero + 1):
    suma += i

print(f"La suma de todos los números desde 0 hasta {numero} es: {suma}")

#8) Imprimir 100 números (especifie pares, impares, posit., neg.)

CANTIDAD_NUMEROS = 5 #no usé el número 100, se puede cambiar pero para probar es más simple poner un número chico
pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0

print(f"Ingrese {CANTIDAD_NUMEROS} números enteros:")

for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Número {i + 1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print("\n--- RESULTADOS ---")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros: {ceros}")

#9) Programa que mide la media de los números
suma_total = 0
cantidad_numeros = 5 #se pone para el ejercicio, se puede cambiar por 100

for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el número {i+1}: "))
    suma_total = suma_total + numero
media = suma_total / cantidad_numeros

print(f"La media de los {cantidad_numeros} números es: {media}")