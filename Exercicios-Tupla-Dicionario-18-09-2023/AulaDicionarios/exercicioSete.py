contatos = {}

for i in range(0,3):
    nome_contato = input("Digite o nome do contato: ")
    numero_contato = int(input("Digite o número do contato: "))

    contatos[f"{nome_contato}"] = numero_contato

print(contatos)