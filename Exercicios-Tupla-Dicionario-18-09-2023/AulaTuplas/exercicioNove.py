tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

pares = ()

for x in tupla:
    if x % 2 == 0:
        pares += (x, )


print(pares)