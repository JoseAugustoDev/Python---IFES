def dividir():
    num = int(input("Digite o número: "))

    if num != 0:
        return num
    else:
        num = int(input("Digite o número novamente: "))
        return num

valor_a = dividir()
valor_b = dividir()

divisao = valor_a / valor_b

print(f"A divisão de {valor_a} / {valor_b} é = {divisao}")