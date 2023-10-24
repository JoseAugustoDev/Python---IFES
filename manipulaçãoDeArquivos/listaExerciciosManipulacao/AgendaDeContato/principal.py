from excluir import excluirUsuario
from atualizar import atualizarLista
from adicionar import adicionarUsuario, adicionarVarios
from visualizar import visualizarLista

print("----Sistema de Agenda----")
print("---O que deseja fazer:---")

escolha_usuario = input("Digite 1 para Adicionar \nDigite 2 para Visualizar \nDigite 3 para Atualizar \nDigite 4 para Excluir \nDigite 0 para encerrar")
while True:
    if escolha_usuario == 1:
        quant_usuarios = int(input("Digite 1 para adicionar apenas 1 contatos \nDigite 2 para adicionar 2 ou mais usuarios: "))

        if quant_usuarios == 1:
            adicionarUsuario()
        elif quant_usuarios == 2:
            adicionarVarios()

    elif escolha_usuario == 2:
        visualizarLista()

    elif escolha_usuario == 3:
        visualizarLista()
        escolher_contato = input("Qual usuario deseja escolher: ")
        atualizarLista(contato_escolhido=escolher_contato)

    elif escolha_usuario == 4:
        excluirUsuario()

    elif escolha_usuario == 0:
        break
    else:
        print("Escolha Inválida!")