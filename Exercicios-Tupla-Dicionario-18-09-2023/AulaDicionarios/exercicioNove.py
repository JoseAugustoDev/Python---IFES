alunos = {}

resp = 1

quant_alunos = 0

while resp != 0:
    nome_aluno = input("Digite o nome do aluno: ")
    nota_aluno = int(input("Digite a nota do aluno: "))

    alunos[f"{nome_aluno}"] = nota_aluno

    quant_alunos += 1

    resp = int(input("Digite 1 para continuar: \nDigite 0 para sair: \n"))

soma = 0

for x, y in alunos.items():
    soma = soma + y

media = soma / quant_alunos

print(f"A média das notas é de: {media}")