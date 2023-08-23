nome_vendedor = input("Digite o nome do vendedor:")

carros_vendidos = int(input("Digite a quantidade de carros vendidos: "))
vendas_totais = int(input("Digite a quantidade de vendas totais:"))
salario_fixo = float(input("Qual seu salário fixo:"))
valor_comissao = float(input("Digite o valor da sua comissão:"))

salario_final = salario_fixo + (valor_comissao * carros_vendidos) + ((5 * vendas_totais) / 100)

print(f"Para o vendedor {nome_vendedor} o salário final é de: {salario_final}")