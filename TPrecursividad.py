# Ejercicio 1: Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejercicio 2: Fibonacci
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

# Ejercicio 3: Potencia
def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp - 1)

# Ejercicio 4: Decimal a binario
def a_binario(n):
    if n == 0:
        return ""
    else:
        return a_binario(n // 2) + str(n % 2)

# Ejercicio 5: Palindrome
def es_palindrome(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindrome(palabra[1:-1])

# Ejercicio 6: Suma de dígitos
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

# Ejercicio 7: Contar bloques
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Ejercicio 8: Contar dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

# --- Pruebas ---
if __name__ == "__main__":
    # Ej 1
    num = int(input("Ingrese un número para factorial: "))
    for i in range(1, num + 1):
        print(f"Factorial de {i}: {factorial(i)}")

    # Ej 2
    pos = int(input("Ingrese posición para Fibonacci: "))
    print("Serie completa:", [fibonacci(i) for i in range(pos + 1)])

    # Ej 3
    base = 2
    exp = 3
    print(f"{base}^{exp} = {potencia(base, exp)}")

    # Ej 4
    decimal = 10
    binario = a_binario(decimal) or "0"
    print(f"Decimal {decimal} -> Binario: {binario}")

    # Ej 5
    palabra = "reconocer"
    print(f"¿'{palabra}' es palindrome? {es_palindrome(palabra)}")

    # Ej 6
    print(f"Suma dígitos 1234: {suma_digitos(1234)}")

    # Ej 7
    print(f"Bloques para pirámide de 4: {contar_bloques(4)}")

    # Ej 8
    print(f"Veces que aparece 2 en 12233421: {contar_digito(12233421, 2)}")