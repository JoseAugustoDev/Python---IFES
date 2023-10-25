from ler_dados import ler_dados

lista = ler_dados()

maior = 0
menor = lista_numeros[0]

for x in lista_numeros:
    if x > maior:
        maior = x

    if x < menor:
        menor = x 

print(f"O maior número é: {maior}")  
print(f"O menor número é: {menor}")  