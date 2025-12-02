def fibonacci(n):
    if n == 0 or n == 1:
    # Casos base
        return n
    else:
        # Caso recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Ingresa un numero: "))
print(fibonacci(n))