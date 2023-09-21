pessoa = {}

for x in range(0,3):
    nome = input("Digite o nome da pessoa: ")

    idade = int(input("Digite a idade: "))

    pessoa[f"nome_{x}"] = nome
    pessoa[f"idade_{x}"] = idade

escolha_usuario = input("Digite a pessoa que gostaria de saber a idade: ")

for x, y in pessoa.items():
    if y == escolha_usuario:
        print(pessoa[f'{x}'])