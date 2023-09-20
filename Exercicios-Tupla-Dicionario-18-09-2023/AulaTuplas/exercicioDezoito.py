notas_alunos = ()

for x in range(0, 5):
    notas = int(input("Digite a nota: "))

    notas_alunos += (notas, )

ordenado = sorted(notas_alunos)

print(ordenado)