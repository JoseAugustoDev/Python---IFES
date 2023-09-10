lista_usuario = []

resp = 1

while resp == 1:
    escolha_usuario = input("Digite o que deseja incluir na lista: ")

    lista_usuario.append(escolha_usuario)

    resp = int(input("Digite (1) para continuar \nDigite (0) para sair \n"))

print("\nLista Final: \n-----------")

i = 1

for x in lista_usuario:
    print(f"{i}. {x}")

    i += 1
