with open('manipulaçãoDeArquivos/listaNumerosUsuario.txt', 'w') as lista:
    resp = 1
    
    while resp != 0:
        escolha_usuario = int(input("Digite um número: "))

        lista.write(f"{escolha_usuario}\n")

        resp = int(input("Digite 1 se deseja continuar: \nDigite 0 se deseja parar: \n"))

with open('manipulaçãoDeArquivos/listaNumerosUsuario.txt', 'r') as lerNumeros:
    soma = 0
    quant = 0
    for linha in lerNumeros:
        num = int(linha)

        soma = soma + num
        quant += 1

    media = soma / quant

    print(f"A média da soma dos números é de: {media}")