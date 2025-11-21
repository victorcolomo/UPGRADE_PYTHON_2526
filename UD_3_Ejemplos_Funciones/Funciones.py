def mayor(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "Son iguales"

def calculos(a,b):
    media = (a + b) / 2
    if a > b:
        return media, a
    else:
        return media, b