with open('manipulaçãoDeArquivos/listaExerciciosManipulacao/dicionarioEstudantes.txt', 'r') as arquivo:
    escolha_aluno = input("Qual aluno deseja procurar: ")
    
    for linha in arquivo:

        if escolha_aluno in linha:

            print(linha)