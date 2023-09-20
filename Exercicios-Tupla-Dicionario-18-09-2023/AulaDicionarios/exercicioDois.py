pessoa = {}

for x in range(0,3):
    nome = input("Digite o nome da pessoa: ")

    idade = int(input("Digite a idade: "))

    pessoa["nome"] = nome
    pessoa["idade"] = idade

    print(pessoa)
