nome_usuario = input("Digite o seu nome: ")
sexo_usuario = int(input("Digite (1) para masculino \n Digite (2) para feminino: "))
peso_usuario = float(input("Digite seu peso: "))
altura_usuario = float(input("Digite sua altura (em cm): "))
idade_usuario = int(input("Digite sua idade: "))

quant_calorias_ideal = 0

if sexo_usuario == 1:
    quant_calorias_ideal = 66 + (13.7 * peso_usuario) + (5 * altura_usuario) - (6.8 * idade_usuario)
elif sexo_usuario == 2:
    quant_calorias_ideal = 665 + (9.6 * peso_usuario) + (1.8 * altura_usuario) - (4.7 * idade_usuario)
else:
    print("Erro!")