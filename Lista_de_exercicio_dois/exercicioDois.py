distancia_carro_um = int(input("Digite a distância (em KM) percorrida pelo carro um: "))
tempo_carro_um = int(input("Digite o tempo que o carro um gastou: "))

velocidade_media_carro_um = distancia_carro_um / tempo_carro_um

distancia_carro_dois = int(input("Digite a distância (em KM) percorrida pelo carro dois: "))
tempo_carro_dois = int(input("Digite o tempo que o carro dois gastou: "))

velocidade_media_carro_dois = distancia_carro_dois / tempo_carro_dois

if velocidade_media_carro_um == velocidade_media_carro_dois:
    print("As velocidades são iguais")
elif velocidade_media_carro_um > velocidade_media_carro_dois:
    quant_mais_rapido = velocidade_media_carro_um - velocidade_media_carro_dois 
    print(f"O carro um é {quant_mais_rapido} km mais rapido que o carro dois")
elif velocidade_media_carro_dois > velocidade_media_carro_um:
    quant_mais_rapido = velocidade_media_carro_dois - velocidade_media_carro_um
    print(f"O carro dois é {quant_mais_rapido} km mais rapido que o carro um")
else:
    print("Erro!")