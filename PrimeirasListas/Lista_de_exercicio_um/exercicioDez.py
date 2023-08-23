idade_usuario_em_anos = int(input("Digite sua idade em anos:"))
idade_usuario_em_meses = int(input("Agora digite os meses:"))
idade_usuario_em_dias = int(input("E também os dias:"))

dias_em_um_ano = 365
dias_em_um_mes = 30

idade_final_usuario_em_dias = (idade_usuario_em_anos * dias_em_um_ano) + (idade_usuario_em_meses * dias_em_um_mes) + idade_usuario_em_dias

print(f"A sua idade em dias é de: {idade_final_usuario_em_dias}")