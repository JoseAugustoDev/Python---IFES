nome_aluno = input("Digite o nome do aluno:")

nota_prova_um = float(input("Digite o valor da nota da prova 1:"))
nota_prova_dois = float(input("Digite o valor da nota da prova 2:"))
nota_atividade = float(input("Digite o valor da nota da atividade:"))

calculo_media = ((4 * nota_prova_um) + (3 * nota_prova_dois) + (2 * nota_atividade)) / 9

print(f"A média das notas do aluno {nome_aluno} é de: {round(calculo_media)}")