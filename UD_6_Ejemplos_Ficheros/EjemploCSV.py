# Importamos la libreria
import csv

# Escribimos
with open("datos.csv","w",newline="",encoding="utf-8") as csvfile:
    #Creamos un objeto "escritor", indicamos el delimitador
    escritor = csv.writer(csvfile, delimiter=',')
    # Primera fila: cabecera
    escritor.writerow(["nombre","apellido","edad"])
    # Siguientes filas datos del fichero
    escritor.writerow(["Ana","Perez",20])
    escritor.writerow(["Pepe", "Gomez", 22])

# Leemos el fichero CSC
with open("datos.csv","r",encoding="utf-8") as csvfile:
    # Creamos un objeto "lector", indicamos el delimitador
    lector = csv.reader(csvfile, delimiter=',')
    cabecera = next(lector)
    for row in lector:
        print(row[0],row[1],row[2])