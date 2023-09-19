tupla_inteiros = (2, 5, 7, 1, 0, 6, 9, 55, -1)

maior = 0
menor = tupla_inteiros[0]

for x in tupla_inteiros:
    if x > maior:
        maior = x

    if x < menor:
        menor = x

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")