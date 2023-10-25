from ler_dados import ler_dados

lista_1 = ler_dados()

i = 0

for x in lista_numeros:
    if x % 2 == 0:
        lista_numeros[i] = 0
    
    i += 1

print(lista_numeros)