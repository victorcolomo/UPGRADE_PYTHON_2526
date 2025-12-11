notas = {"Juan" : [3,6,7], "Ana" : [7,8,9], "Pepe" : [10,9,8]}

for clave, valor in notas.items():
    print(clave)
    for nota in valor:
        print(nota)

print(notas["Juan"][2])

notas = {"Juan" : { "T1" : 3, "T2" : 6 , "T3": 7},
         "Ana" : { "T1" : 7, "T2" : 8 , "T3": 9},
         "Pepe" : { "T1" : 10, "T2" : 9 , "T3": 9}}

print(notas["Juan"]["T3"])

for clave, valor in notas.items():
    print(clave,valor["T1"],valor["T2"],valor["T3"])