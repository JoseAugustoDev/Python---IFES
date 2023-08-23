nome_usuario = input("Digite seu nome: ")
sexo_usuario = int(input("Digite (1) para masculino \nDigite (2) para feminino: "))
idade_usuario = int(input("Digite sua idade: "))

if sexo_usuario == 1 and idade_usuario > 21:
    print(f"{nome_usuario}, é maior de idade!")
elif sexo_usuario == 2 and idade_usuario > 18:
    print(f"{nome_usuario}, é maior de idade!")
else:
    print(f"{nome_usuario}, não é maior de idade!")