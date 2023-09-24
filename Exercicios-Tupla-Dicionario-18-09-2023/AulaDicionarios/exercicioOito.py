contatos = {}

for i in range(0,3):
    nome_contato = input("Digite o nome do contato: ")
    numero_contato = int(input("Digite o número do contato: "))

    contatos[f"{nome_contato}"] = numero_contato

escolha_usuario = input("Digite o nome do usuario no qual deseja remover o contato da lista: ")

del contatos[escolha_usuario]

print(contatos)