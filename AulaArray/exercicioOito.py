lista_numeros = [0, 16, 6, 7, 8, 9, 10, 12, 265, 36, 44, 15]

maior = 0
menor = lista_numeros[0]

for x in lista_numeros:
    if x > maior:
        maior = x

    if x < menor:
        menor = x 

print(f"O maior número é: {maior}")  
print(f"O menor número é: {menor}")  