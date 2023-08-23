nome_aluno = input("Digite seu nome: ")

media_aluno = float(input(f"Digite a média do aluno(a): {nome_aluno}"))
quant_faltas = int(input(f"Digite a quantidades de faltas do aluno(a): {nome_aluno}"))

if media_aluno >= 7 and quant_faltas < 32:
    print(f"Aluno(a): Aprovado.")
elif media_aluno < 7 and quant_faltas < 32:
    print(f"Aluno(a): Reprovado por média.")
elif media_aluno >= 7 and quant_faltas >= 32:
    print(f"Aluno(a): Reprovado por faltas.")
elif media_aluno < 7 and quant_faltas >= 32:
    print(f"Aluno(a): Reprovado por média e falta.")
else:
    print("Erro!")