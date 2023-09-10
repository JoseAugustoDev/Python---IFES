palavras = ['arroz', 'feijao', 'carne', 'ovo', 'roma', 'abacaxi']
palavras_grandes = []

for x in palavras:
    if len(x) > 5:
        palavras_grandes.append(x)

for i in palavras_grandes:
    print(i)
