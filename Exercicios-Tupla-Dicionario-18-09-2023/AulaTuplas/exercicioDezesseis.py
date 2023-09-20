tupla_1 = (1, 2, 3, 4, 5)
tupla_2 = (6, 7, 8, 9, 10)

soma = ()

for x in range(0, 5):
    soma_unidade = tupla_2[x] + tupla_1[x]

    soma += (tupla_2[x] + tupla_1[x], )
    print(f"A soma de {tupla_1[x]} + {tupla_2[x]} é de: {soma_unidade}")

print(f"Os resultados são {soma}")
