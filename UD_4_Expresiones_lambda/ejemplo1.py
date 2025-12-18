

# Expresiones lambda
suma = lambda a,b : a + b

print(suma(1,2))

print( (lambda a,b : a + b)(1,2)  )

es_par = lambda a : a % 2 == 0
print(es_par(3))
print(es_par(4))

mayor = lambda a,b : a if a > b else b
print(mayor(1,2))
print(mayor(4,2))

