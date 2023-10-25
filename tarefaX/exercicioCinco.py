from ler_dados import ler_dados

lista = ler_dados()

lista_inteiros = []

for x in lista:
    lista_inteiros.append(int(x))

soma = 0

for x in lista_inteiros:
    soma = soma + x

print(f"A soma é: {soma}")