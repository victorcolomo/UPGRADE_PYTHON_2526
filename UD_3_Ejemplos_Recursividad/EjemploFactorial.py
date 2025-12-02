def factorial(n):
    # Definir el caso base
    if n == 0 or n == 1:
       return 1
    else:
        # Caso recursivo, decrementamos n para acercarnos al caso base
        return n * factorial(n - 1)

n = int(input("Ingresa un numero: "))
print(factorial(n))