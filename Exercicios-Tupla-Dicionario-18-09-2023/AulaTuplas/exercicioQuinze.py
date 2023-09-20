frutas = ('maçã', 'banana', 'goiaba', 'abacaxi', 'melão')

escolha_usuario = input("Digite uma fruta a encontrar: ")

i = 0

for x in frutas:
    if x == escolha_usuario:
        print(f"{x} foi encontrada")
        break
    i += 1

print(f"A fruta {escolha_usuario} foi encontrada na posição {i}")