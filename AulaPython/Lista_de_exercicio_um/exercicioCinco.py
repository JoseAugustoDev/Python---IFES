altura_pessoa = float(input("Digite sua altura:"))
peso_pessoa = float(input("Digite seu peso:"))

calculo_IMC = peso_pessoa / (altura_pessoa * altura_pessoa)

print(f"O seu IMC é de: {round(calculo_IMC,2)}")