tipo_consumidor = int(input("Digite (1) para tipo de consumidor Industrial \nDigite (2) para tipo de consumidor Comercial\nDigite (3) para tipo de consumidor Residencial \n=> "))
consumo_usuario = int(input("Digite o seu consumo de energia: "))

valor_final = 0

if tipo_consumidor == 1:
    valor_final = (0.68 * consumo_usuario) + 34
elif tipo_consumidor == 2:
    valor_final = (0.37 * consumo_usuario) + 45
elif tipo_consumidor == 3:
    valor_final = (0.77 * consumo_usuario) - 22
else:
    print("Erro!")

print(f"O valor final é de: {valor_final}")