distancia_em_km = int(input("Digite a distância em Km: "))
quant_litros_gasolina_consumidos = int(input("Digite a quantidade de litros de gasolina que foram consumidos: "))

consumo_km_por_litro = distancia_em_km / quant_litros_gasolina_consumidos

if consumo_km_por_litro < 8:
    print("Venda o carro!")
elif consumo_km_por_litro >= 8 and consumo_km_por_litro <= 14:
    print("Econômico!")
elif consumo_km_por_litro > 12:
    print("Super Econômico.")
else:
    print("Erro!")

