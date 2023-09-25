produtos_estoque = {"Coca-Cola": 1250, "Arroz": 2500, "Biscoito": 1500, "Chocolate": 2500}

nivel_estoque = int(input("Digite o nível do estoque: "))

for x, y in produtos_estoque.items():
    if y < nivel_estoque:
        print(f"{x} está abaixo do nível desejado! ")