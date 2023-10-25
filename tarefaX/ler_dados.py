def ler_dados():
    quantidade_de_itens = int(input("Digite a quantidade de itens: "))
    
    lista = []

    for x in range (0, quantidade_de_itens):
        escolha_usuario = input("Qual o nome do item: ")
        lista.append(escolha_usuario)

    return lista