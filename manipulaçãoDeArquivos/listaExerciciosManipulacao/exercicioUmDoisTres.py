import json

with open('manipulaçãoDeArquivos/listaExerciciosManipulacao/dicionarioEstudantes.txt', 'w') as lista:
    resp = 1

    estudante = {}
    
    while resp != 0:
        nome_estudante = input("Digite o nome do estudante: ")
        idade_estudante = input("Digite a idade do estudante: ")
        curso_estudante = input("Digite o curso do estudante: ")

        estudante['nome'] = nome_estudante
        estudante['idade'] = idade_estudante
        estudante['curso'] = curso_estudante

        lista.write(f"{estudante}\n")

        resp = int(input("Digite 1 se deseja continuar: \nDigite 0 se deseja parar: \n"))

with open('manipulaçãoDeArquivos/listaExerciciosManipulacao/dicionarioEstudantes.txt', 'r') as arquivo:
    escolha_aluno = input("Qual aluno deseja procurar: ")
    
    for linha in arquivo:

        if escolha_aluno in linha:

            print(linha)

