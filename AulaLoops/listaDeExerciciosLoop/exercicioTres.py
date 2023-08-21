numero_usuario = int(input("Digite o numero que deseja descobrir a tabuada: "))

for i in range(1, 11):
    multiplicacao = numero_usuario * i
    print(f"{numero_usuario} X {i} = {multiplicacao}")