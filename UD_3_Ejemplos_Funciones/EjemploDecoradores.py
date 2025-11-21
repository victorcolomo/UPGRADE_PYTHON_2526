import time

def validar_enteros(funcion):
    def validar(a, b):
        # Validamos datos
        if not isinstance(a, int) or not isinstance(b, int):
            print("El valor debe ser un entero.")
            # Si los datos no son enteros, no ejecutamos la funcion oringal
            return
        #si lo datos son correctos, ejecutamos la funcion original
        return funcion(a, b)
    return validar


@validar_enteros
def suma3(a, b, c):
    return a + b + c

@validar_enteros
def suma(a, b):
    return a + b

#print(resta(1,"hola"))
#print(resta(5,7))

def mi_decorador(funcion):
    def nueva(*args):
        tiempo_inicio = time.time()
        # Ejecutar la funcion original
        retorno = funcion(*args)
        tiempo_fin = time.time()
        print(f"Tiempo de ejecucion {tiempo_fin-tiempo_inicio}")
        return retorno
    return nueva

@mi_decorador
def mostrar(mensaje):
    print(mensaje)

@mi_decorador
def resta(a, b):
    return a - b

mostrar("Hola mundo!!")

resta(1, 2)

