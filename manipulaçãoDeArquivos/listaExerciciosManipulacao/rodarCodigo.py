from principal import ler_varios_alunos, criar_arquivo_lista
from procurarAluno import procurarAluno
from atualizarAluno import atualizarAluno
from removerEstudante import removerEstudante
from ler_arquivo import ler_arquivo

if __name__ == '__main__':
    dados_alunos = ler_varios_alunos()

    criar_arquivo_lista(lista=dados_alunos, nome_arquivo="manipulaçãoDeArquivos/listaExerciciosManipulacao/alunos.txt")

    aluno_escolhido = procurarAluno()

    print(atualizarAluno(aluno_escolhido=aluno_escolhido))

    removerEstudante()

    print(ler_arquivo("manipulaçãoDeArquivos/listaExerciciosManipulacao/alunos.txt"))