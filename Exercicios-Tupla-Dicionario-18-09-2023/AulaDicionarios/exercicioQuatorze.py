frutas = {"Maçã": 100, "Açaí": 50, "Banana": 70, "Abacaxi": 999}

maior = 0
fruta_maior = " "

for x, y in frutas.items():
    print(x)
    if y > maior:
        maior = y
        fruta_maior = x
    
print(f"{fruta_maior} tem a maior quantidade: {maior}")