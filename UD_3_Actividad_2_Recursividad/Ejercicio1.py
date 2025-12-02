# Ejercicio 1) Función que nos devuelva la suma de los números naturales hasta N.
# N se pide por teclado

# 5 = 5+ 4 ....

def sumaN(n):
    # Caso base
    if n == 0:
        return 0
    else:
        return n + sumaN(n - 1)

n = int(input("Ingresa un numero: "))
print(f"La suma de los {n} naturales es {sumaN(n)}")

