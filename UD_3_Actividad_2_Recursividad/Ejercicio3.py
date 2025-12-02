# Ejercicio 3) Función que, dado un número entero, cuente su número de dígitos.

def contarDigitos(numero):
    # Caso base:
    if numero <= 9:
        return 1
    else:
        # Caso recursivo: sumamos un digito y llamos a la funcion con un dígito menos
        return 1 + contarDigitos(numero // 10)


numero = int(input("Ingresa un numero: "))
print(f"Numero de digitos de {numero} {contarDigitos(numero)}")