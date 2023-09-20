inteiros = (11, 22, 33, 44, 55, 66, 77, 88, 99, 1)

tudo_acima_de_dez = True

for x in inteiros:
    if x < 10:
        tudo_acima_de_dez = False

if tudo_acima_de_dez == True:
    print("Todos os números são acima de dez!")
else:
    print("Nem todos os números estão acima de dez!")