palavras_chave = {}

for x in range(0, 3):
    chave = input("Digite a chave: ")
    definicao = input(f"Digite a definição de {chave}: ")

    palavras_chave[chave] = definicao

escolha_usuario = input("Escolha a chave na qual deseja descobrir a definição: ")

print(palavras_chave[escolha_usuario])