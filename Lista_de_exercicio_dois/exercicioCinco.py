nome_aluno = input("Digite o nome do aluno: ")

nota_um = float(input("Digite a nota Um: "))
nota_dois = float(input("Digite a nota Dois: "))

media = (nota_um + nota_dois) / 2

if media >= 7 and media <= 10:
    print(f"{nome_aluno}. Média {media}. Situação: Aprovado!")
elif media >= 5 and media < 7:
    print(f"{nome_aluno}. Média {media}. Situação: Recuperação!")
elif media >= 0 and media < 5:
    print(f"{nome_aluno}, com a média {media} está: Reprovado!")
else:
    print("Erro!")