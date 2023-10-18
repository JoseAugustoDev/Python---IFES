from procurarAluno import procurarAluno
from atualizarAluno import atualizarAluno

def ler_dados():

    nome_estudante = input("Digite o nome do estudante: ")
    idade_estudante = int(input("Digite a idade do estudante: "))
    curso_estudante = input("Digite o curso do estudante: ")

    estudante = {
        "nome": nome_estudante,
        "idade": idade_estudante,
        "curso": curso_estudante,
    }

    return estudante

def criar_arquivo(dados_aluno):

    with open('manipulaçãoDeArquivos/listaExerciciosManipulacao/dicionarioEstudantes.txt', 'w') as lista:

        lista.write(f"{dados_aluno}\n")

if __name__ == '__main__':
    dados_alunos = ler_dados()
    criar_arquivo(dados_aluno=dados_alunos)
    aluno_escolhido = procurarAluno()
    print(atualizarAluno(aluno_escolhido=aluno_escolhido))