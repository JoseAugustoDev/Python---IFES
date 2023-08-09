ano_atual = int(input("Digite o ano atual: "))

pessoa_um = input("Digite o nome: ")
idade_pessoa_um = int(input("Digite a idade: "))

pessoa_dois = input("Digite outro nome: ")
idade_pessoa_dois = int(input("Digite outra idade: "))

ano_nascimento_pessoa_um = ano_atual - idade_pessoa_um
ano_nascimento_pessoa_dois = ano_atual - idade_pessoa_dois

if idade_pessoa_dois > idade_pessoa_um:
    print(f"Nome: {pessoa_um}, Idade: {idade_pessoa_um}, Ano de Nascimento: {ano_nascimento_pessoa_um}")
elif idade_pessoa_um > idade_pessoa_dois:
    print(f"Nome: {pessoa_dois}, Idade: {idade_pessoa_dois}, Ano de Nascimento: {ano_nascimento_pessoa_dois}")
elif idade_pessoa_um == idade_pessoa_dois:
    print(f"As idades são iguais. {pessoa_um} e {pessoa_dois} ambos nasceram no ano {ano_nascimento_pessoa_um}")
else:
    print("Erro!")

