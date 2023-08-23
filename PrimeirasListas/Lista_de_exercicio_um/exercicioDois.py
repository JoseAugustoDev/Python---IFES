valor_em_dolares = float(input('Digite o valor em Dolares:'))

taxa_conversao = 3.12

valor_em_reais = valor_em_dolares * taxa_conversao

print(f"{valor_em_dolares} dolares são {round(valor_em_reais, 2)} reais")