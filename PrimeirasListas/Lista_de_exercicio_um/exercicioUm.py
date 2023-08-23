valor_em_reais = float(input('Digite o valor em Reais:'))

taxa_conversao = 3.12

valor_em_dolares = valor_em_reais / taxa_conversao

print(f"{valor_em_reais} reais são {round(valor_em_dolares, 2)} dolares")