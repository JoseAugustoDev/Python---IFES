lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0

for x in lista_numeros:
    if x % 2 == 0:
        lista_numeros[i] = 0
    
    i += 1

print(lista_numeros)