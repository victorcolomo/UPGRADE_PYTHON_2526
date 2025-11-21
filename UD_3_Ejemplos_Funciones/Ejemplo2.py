def pares(maximo):
    for i in range(0, maximo + 1, 2):
        yield i

gen = pares(20) # devuelve el generador
print(gen) # <generator object pares at 0x0000028FBA0A1E00>
for numero in gen:
    print(numero)