from Funciones import *

contador = 1

def doble(a):
    print(contador)
    a = a * 2
    print(f"Valor de a en funcion doble: {a} ")

def mostrar_mensaje(nombre, saludo="Buenos dias", edad=18):
    print(f"{saludo} {nombre} tienes {edad} anos")

print("Linea 1",end="\n")
print("Linea 2", end="#")
print("Linea 3")
print("Linea 2")

mostrar_mensaje("Ana")
mostrar_mensaje("Pepe", "Buenas tardes")
mostrar_mensaje("Juan", "Buenas noches", 23)

resultado = calculos(3,6)
print(resultado)
print(f"Media {resultado[0]} el mayor es {resultado[1]} ")

a = 4
doble(a)
print(f"Valor de a en funcion principal: {a} ")

n1 = int(input("Ingresa un numero: "))
n2 = int(input("Ingresa otro numero: "))

print(f"El mayer de {n1} y {n2} es {mayor(n1,n2)}")

def factoria():
    while True:
        try:
            n = input("Introduce un número entero positivo: ")
            if int(n) < 0:
                print("Tiene que ser positivo.")
            else:
                break
        except ValueError:
            print("Entrada no valida.")

    n_separado = list(n)

    suma = 0
    for i in n_separado:
        resultado = 1
        for x in range(2, int(i) + 1):
            resultado *= x

        suma += resultado

    if suma == int(n):
        print(f"El número {n} es una factoría.")
    else:
        print(f"El número {n} no es una factoría.")

factoria()




