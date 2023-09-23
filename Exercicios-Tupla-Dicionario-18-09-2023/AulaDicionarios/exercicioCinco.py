pessoa = {}

for x in range(1,4):
    nome = input("Digite o nome da pessoa: ")

    idade = int(input("Digite a idade: "))

    pessoa[f"nome_{x}"] = nome
    pessoa[f"idade_{x}"] = idade

escolha_usuario = input("Digite a pessoa que gostaria de saber a idade: ")

for x, y in pessoa.items():  
    if y == escolha_usuario:
        idade_usuario = pessoa[f"idade_{x[5:6]}"]
        print(f"A idade de {y} é {idade_usuario}")