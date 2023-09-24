lista_de_produtos = {}

resp = 1

while resp != 0:
    produto = input("Digite o produto a ser adicionado: ")
    preco = int(input(f"Digite o preco de {produto}: "))

    lista_de_produtos[f"{produto}"] = preco

    resp = int(input("Digite 1 para continuar: \nDigite 0 para sair:\n"))

soma = 0

for x, y in lista_de_produtos.items():
    soma = soma + y

print(f"O valor total é de: R$ {soma}")