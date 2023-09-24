pessoa = {}

for x in range(0,3):
    nome = input("Digite o nome da pessoa: ")

    idade = int(input("Digite a idade: "))

    pessoa[f"{nome}"] = idade

for x, y in pessoa.items():
    print(y)