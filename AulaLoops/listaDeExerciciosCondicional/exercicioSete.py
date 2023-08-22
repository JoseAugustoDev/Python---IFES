ponto_x = float(input("Digite o valor da coordenada X:"))
ponto_y = float(input("Digite o valor da coordenada Y:"))

if ponto_x > 0 and ponto_y > 0:
    print("Primeiro Quadrante!")
elif ponto_x < 0 and ponto_y > 0:
    print("Segundo Quadrante!")
elif ponto_x < 0 and ponto_y < 0:
    print("Terceiro Quadrante!")
elif ponto_x > 0 and ponto_y < 0:
    print("Quarto Quadrante!")