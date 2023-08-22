nome_usuario = int(input("Digite seu nome:"))
idade_usuario = int(input("Digite sua idade:"))

if idade_usuario > 16 and idade_usuario < 18:
    print(f"{nome_usuario}, você pode votar, mas não é obrigado!")
elif idade_usuario >= 18:
    print(f"{nome_usuario}, você deve votar!")