salario_usuario = int(input("Digite seu salário: "))

aliquota = 0
deducao = 0
imposto_a_ser_pago = 0
salario_liquido = 0

if salario_usuario <= 1903.98:
    print("Isento")
elif salario_usuario > 1903.98 and salario_usuario <= 2826.65:

    aliquota = 0.075
    deducao = 142.80
    imposto_a_ser_pago = (salario_usuario * aliquota) - deducao
    salario_liquido = salario_usuario - imposto_a_ser_pago
    print(f"Imposto a ser pago: {round(imposto_a_ser_pago, 2)}")
    print(f"Salário líquido de: {salario_liquido}")

elif salario_usuario >= 2826.66 and salario_usuario <= 3751.05:

    aliquota = 0.15
    deducao = 354.80
    imposto_a_ser_pago = (salario_usuario * aliquota) - deducao
    salario_liquido = salario_usuario - imposto_a_ser_pago
    print(f"Imposto a ser pago: {round(imposto_a_ser_pago, 2)}")
    print(f"Salário líquido de: {salario_liquido}")

elif salario_usuario >= 3751.06 and salario_usuario <= 4664.68:

    aliquota = 0.225
    deducao = 636.13
    imposto_a_ser_pago = (salario_usuario * aliquota) - deducao
    salario_liquido = salario_usuario - imposto_a_ser_pago
    print(f"Imposto a ser pago: {round(imposto_a_ser_pago, 2)}")
    print(f"Salário líquido de: {salario_liquido}")
    
elif salario_usuario > 4664.68:
    aliquota = 0.275
    deducao = 869.36
    imposto_a_ser_pago = (salario_usuario * aliquota) - deducao
    salario_liquido = salario_usuario - imposto_a_ser_pago
    print(f"Imposto a ser pago: {round(imposto_a_ser_pago, 2)}")
    print(f"Salário líquido de: {salario_liquido}")

else:
    print("Erro!")