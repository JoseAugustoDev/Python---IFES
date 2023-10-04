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
    escolha_usuario = input("Digite 'nome' para mudar o nome: \nDigite 'idade' para mudar a idade: \nDigite 'curso' para mudar o curso: \n")

    escolha_aluno = input("Qual aluno será feita a atualização: ")

    mudanca = input("Insira o novo valor: ")    
    
    for linha in arquivo:
        print(linha)
