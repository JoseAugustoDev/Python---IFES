ano = int(input("Digite o ano:"))

ano_bissexto = False

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    ano_bissexto = True
else:
    ano_bissexto = False

if ano_bissexto == True:
    print("Ano bissexto!!!")
else:
    print("Ano comum!!!")