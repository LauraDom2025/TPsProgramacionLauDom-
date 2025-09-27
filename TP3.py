#escribir un programa que solicite la edad al usuario.Si el usuario es mayor de 18 años deberá mostrar un mensaje en pantalla que diga que es mayor de edad.#
edad = int(input("ingrese su edad: "))
if edad >=18:
    print("es mayor de edad")
else:
    print("no es mayor de edad")
    
    
#escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga "aprobado"; en caso contrario deberá mostrar el mensaje "desaprobado"#
nota = int(input("Ingrese su nota: "))
    
if nota >=6:
     print("Aprobado!")
else:
     print("Desaprobado.") 
     
     
#Escribir un programa que permita solo ingresar números pares. Si el usuario ingresa un número par, imprimir por pantalla el mensaje "Ha introducido un número par"; en caso contrario imprimir "por favor ingrese un número par"#
numero = int (input("ingrese un numero: "))
     
if numero % 2 == 0:
         print ("ha ingresado un numero par")
else:
         print ("por favor ingrese un numero par")
         
#Escribir un programa que solicite la edad al usuario e imprima: niño, adolescente, adulto joven, adulto.#
edad = int (input("Ingrese su edad: "))
if edad < 12:
    print ("Segun esta edad su categoria es niño o niña")
elif edad >=12 and edad <18:
    print ("Segun esta edad su categoria es adolescente") 
elif edad >= 18 and edad <30:
    print ("Segun esta edad su categoria es: Adulto joven")
else:
    print("Segun su edad la catergoría a la que perteneces es: adulto")
    
#Escribir un programa que permita el ingreso de una contraseña según las condiciones solicitadas, sino que pida ingresar una contraseña correcta.#
contraseña = input ("Ingrese su contraseña: ")
if len(contraseña) >=8 and len(contraseña) <=14:
    print ("Ha ingresado una contraseña correcta!")
else:
    print ("Ingrese una contraseña que tenga entre 8 y 14 caracteres")
    

#Tomar una lista de numeros y calcular la moda, la mediana y la media.#
import random
from statistics import mean, median, mode
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media_valor = mean(numeros_aleatorios)
mediana_valor = median(numeros_aleatorios)

try:
    moda_valor = mode(numeros_aleatorios)
except:
    moda_valor = "No hay una moda única"
    
print("Lista de números aleatorios:", numeros_aleatorios)
print("Media:", media_valor)
print("Mediana:", mediana_valor)
print("Moda:", moda_valor)

if isinstance(moda_valor, int):  # Solo si hay una moda única
    if media_valor > mediana_valor and mediana_valor > moda_valor:
        print("La distribución tiene sesgo positivo (a la derecha).")
    elif media_valor < mediana_valor and mediana_valor < moda_valor:
        print("La distribución tiene sesgo negativo (a la izquierda).")
    elif media_valor == mediana_valor == moda_valor:
        print("La distribución no tiene sesgo (simétrica).")
    else:
        print("La distribución tiene un sesgo irregular.")
else:
    print("No se puede determinar el sesgo porque no hay una moda única.")
    
#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual.#
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
     frase += "!"
     print(frase)
     
     
#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 para la opción deseada#
nombre = input("Ingrese su nombre: ")
print("Elija una opción:")
print("1. Nombre en MAYÚSCULAS")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra en mayúscula")

opcion = input("Ingrese 1, 2 o 3 según su preferencia: ")
if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida. Por favor ingrese 1, 2 o 3.")
    

#Escribir un programa principiante en python que pida al usuario la magnitud de un terremoto y la clasifique.#
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else: 
    print("Extremo (puede causar graves daños a gran escala)")
    
    
#Ejercicio de código para las estaciones del año.#
hemisferio = input("Ingrese su hemisferio (N para Norte / S para Sur): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

estacion = "Fecha no válida"

if hemisferio == "N":  # Hemisferio Norte
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
        
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
        
else:
    estacion = "Hemisferio no válido"
    
print("La estación del año es:", estacion)