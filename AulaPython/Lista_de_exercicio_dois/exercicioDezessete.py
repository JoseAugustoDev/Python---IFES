valor_w = int(input("Digite o valor de W: "))
valor_z = int(input("Digite o valor de Z: "))

x = 0
t = 0

if valor_w > 0 or valor_z < 7:
    x = ((5 * valor_w) + 1) / 3
    t = (5 * valor_z) + 2
else:
    x = (5 * valor_z) + 2
    t = ((5 * valor_w) + 1) / 3

print(f"x = {x}; t = {t}")

print(pow(x, 0.5))

resultado_calculo = (7 * (pow(x, 3)) - (3 * (pow(x, 0.5))) - (8 * t))/(5 * (x + 1))

print(f"O resultado do cálculo é de: {resultado_calculo}")