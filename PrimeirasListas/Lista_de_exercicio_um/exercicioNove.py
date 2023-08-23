quantidades_maca = int(input("Digite a quantidade de maçãs:"))
quilos_bananas = int(input("Digite a quantidade (em KG) de bananas:"))

preco_unidade_maca = 1.30
preco_quilo_banana = 5.00

valor_final_macas = quantidades_maca * preco_unidade_maca
valor_final_bananas = quilos_bananas * preco_quilo_banana

print(f"O valor de {quantidades_maca} é de: {valor_final_macas}, já para {quilos_bananas} kg de banana o valor é de: {valor_final_bananas}")