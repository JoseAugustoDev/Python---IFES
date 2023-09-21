pessoa = {}

for x in range(0,3):
    nome = input("Digite o nome da pessoa: ")

    idade = int(input("Digite a idade: "))

    pessoa[f"nome_{x}"] = nome
    pessoa[f"idade_{x}"] = idade

for x, y in pessoa.items():
    print(x)