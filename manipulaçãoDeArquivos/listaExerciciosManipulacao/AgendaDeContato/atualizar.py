import ast

def atualizarLista(contato_escolhido):
    escolha_atualizar = int(input("Digite 1 para atualizar o nome \nDigite 2 para atualizar a ddd \nDigite 3 para atualizar o numero\n"))

    with open('manipulaçãoDeArquivos/listaExerciciosManipulacao/AgendaDeContato/contatos.txt', 'r') as lista_alunos:
        for linha in lista_alunos:
            if contato_escolhido in linha:

                contato = ast.literal_eval(linha)

                if (escolha_atualizar == 1):
                    contato["nome"] = input("Digite o novo nome: ")
                elif (escolha_atualizar == 2):
                    contato["ddd"] = input("Digite a nova ddd: ")
                elif (escolha_atualizar == 3):
                    contato["numero"] = input("Digite o novo numero: ")

                return contato
            