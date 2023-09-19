tupla_inteiros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

i = 0
soma = 0

for x in tupla_inteiros:
    soma = soma + x

    i += 1

media = soma / i

print(media)