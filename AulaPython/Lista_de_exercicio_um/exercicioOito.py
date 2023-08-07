tempo = int(input("Digite o valor do tempo:"))

posicao_inicial = 2
velocidade_inicial = 3
aceleracao = 10

calculo_espaco_percorrido = posicao_inicial + (velocidade_inicial * tempo) + (1/2 * (aceleracao * (tempo ** 2)))

print(f"O valor do espaço percorrido é de: {calculo_espaco_percorrido}")