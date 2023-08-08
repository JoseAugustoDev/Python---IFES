salario_usuario = float(input("Digite o valor do seu salário: "))
financiamento_desejado = float(input("Qual o valor do financiamento desejado: "))

limite_financiamento = salario_usuario * 5

if financiamento_desejado <= limite_financiamento:
    print("Financiamento Concedido!")
else:
    print("Financiamento Negado!")

