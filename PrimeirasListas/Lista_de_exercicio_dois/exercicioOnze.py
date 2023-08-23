mes_do_ano = int(input("Digite o número correspondente ao mes do ano: "))
ano = int(input("Digite o ano:"))

quant_dias_mes = 0

ano_bissexto = False

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    ano_bissexto = True
else:
    ano_bissexto = False

if mes_do_ano == 2 and ano_bissexto == False:
    quant_dias_mes = 28
    print(f"A quantidade de dias do mês {mes_do_ano} é de: {quant_dias_mes}")
elif mes_do_ano == 2 and ano_bissexto == True:
    quant_dias_mes = 29
    print(f"A quantidade de dias do mês {mes_do_ano} é de: {quant_dias_mes}")
elif mes_do_ano == 1 or mes_do_ano == 3 or mes_do_ano == 5 or mes_do_ano == 7 or mes_do_ano == 8 or mes_do_ano == 10 or mes_do_ano == 12:
    quant_dias_mes = 31
    print(f"A quantidade de dias do mês {mes_do_ano} é de: {quant_dias_mes}")
elif mes_do_ano == 4 or mes_do_ano == 6 or mes_do_ano == 9 or mes_do_ano == 11:
    quant_dias_mes = 30
    print(f"A quantidade de dias do mês {mes_do_ano} é de: {quant_dias_mes}")
else:
    print("Erro!")