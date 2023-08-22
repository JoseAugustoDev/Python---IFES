nota_aluno = int(input("Digite a nota do aluno(a): "))

if nota_aluno < 0:
    print("Nota Inválida!!!")
elif nota_aluno >= 7:
    print("Aprovado!!!")
elif nota_aluno < 7:
    print("Reprovado!!!")
