tupla = ('carro', 'moto', 'barco', 'navio', 'sebonoclastia')

comprimento = ()

for x in tupla:
    comprimento += (len(x),)

print(comprimento)