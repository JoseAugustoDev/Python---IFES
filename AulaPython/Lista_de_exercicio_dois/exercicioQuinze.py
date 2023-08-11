hora_inicial = int(input("Digite a hora inicial: "))
minutos_iniciais = int(input("Digite os minutos dessa hora inicial: "))

hora_final = int(input("Digite a hora final: "))
minutos_finais = int(input("Digite os minutos dessa hora final: "))

horas_duracao_jogo = 0
minutos_duracao_jogo = 0

minutos = 60
horas = 24

if hora_inicial < 24 and hora_final < 24 and minutos_iniciais < 60 and minutos_finais < 60:
    if hora_inicial <= hora_final and minutos_iniciais <= minutos_finais:
        horas_duracao_jogo = hora_final - hora_inicial
        minutos_duracao_jogo = minutos_finais - minutos_iniciais

    elif hora_inicial <= hora_final and minutos_iniciais >= minutos_finais:
        horas_duracao_jogo = (hora_final - hora_inicial) - 1
        minutos_duracao_jogo = (minutos - minutos_iniciais) + minutos_finais
        
    elif hora_inicial >= hora_final and minutos_iniciais <= minutos_finais:
        horas_duracao_jogo = (horas - hora_inicial) + hora_final
        minutos_duracao_jogo = minutos_finais - minutos_iniciais

    elif hora_inicial >= hora_final and minutos_iniciais >= minutos_finais:
        horas_duracao_jogo = ((horas - hora_inicial) + hora_final) - 1
        minutos_duracao_jogo = (minutos - minutos_iniciais) + minutos_finais
        
    else:
        print("Erro!")
else:
    print("Entrada de dados não válida!")

print(f"A partida teve duração de: {horas_duracao_jogo} horas e {minutos_duracao_jogo} minutos.")