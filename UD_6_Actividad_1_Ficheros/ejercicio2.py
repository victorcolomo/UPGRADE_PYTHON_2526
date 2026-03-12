'''
▪ Desarrolla un programa que cumpla los siguientes pasos:
□ El programa debe pedir al usuario que introduzca la temperatura media de cada día de la semana (lunes a domingo).
□ Cada temperatura debe ser un número decimal.
□ El programa debe guardar todas las temperaturas en un archivo llamado temperaturas.txt.
▪ El archivo debe tener este formato exacto:
Lunes: X
Martes: X
Miércoles: X
...
▪ Cuando acabe de guardar los datos, el programa debe mostrar un mensaje indicando que el archivo se ha generado correctamente.
▪ Si se ha generado correctamente, el programa debe abrir el archivo temperaturas.txt, leer las temperaturas, calcular y mostrar por pantalla::
□ Temperatura media de la semana
□ Temperatura máxima
□ Temperatura mínima
'''
from pathlib import Path

'''
dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
temperaturas=[]
# Recorremos la lista de los dias de la semana
for dia in dias:
    temp = float(input(f"Temperatura de {dia}: "))
    temperaturas.append(temp)

with open("temperaturas.txt", "w", encoding="utf-8") as archivo:
    for dia,temp in zip(dias,temperaturas):
        archivo.write(f"{dia}: {temp}\n")
'''

archivo = Path("temperaturas.txt")
contador = 0
totalTemperaturas = 0
maxima = None
if archivo.exists():
    with open("temperaturas.txt", "r", encoding="utf-8") as archivo:
        for line in archivo:
            print(line,end='')
            # Separa cada linea por :
            partes = line.strip().split(":")
            temp = float(partes[1])
            totalTemperaturas += temp
            contador += 1
            if maxima is None or temp > maxima:
                maxima = temp

print(f"Total de temperaturas {contador}")
print(f"Media {totalTemperaturas/contador}")
print(f"Maxima {maxima}")