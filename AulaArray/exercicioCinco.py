lista_numeros = []

resp = 1

while resp == 1:
    escolha_usuario = int(input("Digite o número que deseja incluir na lista: "))

    lista_numeros.append(escolha_usuario)

    resp = int(input("Digite (1) para continuar \nDigite (0) para sair \n"))

soma = 0

for x in lista_numeros:
    soma = soma + x

print(f"A soma final dos números é de: {soma}")