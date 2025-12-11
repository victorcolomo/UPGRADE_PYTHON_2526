


notas = [ [ 1 ,4 , 5] , [6, 9, 10] ]
notas.append([8,10,5])

notas[0][0] = 7
notas[0].append(8)
notas[1].pop()

for nota in notas:
    for trim in nota:
        print(trim, end=' ')
    print()