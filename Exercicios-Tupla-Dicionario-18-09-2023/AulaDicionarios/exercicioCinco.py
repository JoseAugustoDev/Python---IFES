pessoa = {}

for x in range(1,4):
    nome = input("Digite o nome da pessoa: ")

    idade = int(input("Digite a idade: "))

    pessoa[f"{nome}"] = idade

escolha_usuario = input("Digite a pessoa que gostaria de saber a idade: ")

for x, y in pessoa.items():  
    if x == escolha_usuario:
        print(f"A idade de {x} é {y}")