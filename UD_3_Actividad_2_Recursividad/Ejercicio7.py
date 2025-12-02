# Ejercicio 7) Función que, dado una palabra o frase,
# determine si es un palíndromo (se lee igual al derecho y al revés).

def es_palindromo(palabra, posInicial, posicionFinal):
    print(posInicial, posicionFinal)
    # 1º Caso base: sólo tenemos una letra
    if  posInicial >= posicionFinal:
        return True
    else:
        # 2º Caso base: cuando las letras que comparo no son iguales
        if(palabra[posInicial]!= palabra[posicionFinal]):
            return False
        else:
            return es_palindromo(palabra, posInicial + 1, posicionFinal -1 )

palabra = input("Ingresa un texto: ")
if es_palindromo(palabra, 0, len(palabra) - 1):
    print(f"{palabra} es un palindromo")
else:
    print(f"{palabra} no es un palindromo")