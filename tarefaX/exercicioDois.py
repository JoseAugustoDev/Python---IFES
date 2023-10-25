from ler_dados import ler_dados

lista_de_itens = ler_dados()
nova_lista = []

for x in lista_de_itens:
    if len(x) > 5:
        nova_lista.append(x)

print(nova_lista)