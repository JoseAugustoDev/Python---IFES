animais = ('leão', 'macaco', 'cachorro', 'gato', 'pato', 'avestruz')

print("Lista sem ordem:")
for i in animais:
    print(i)

print("---------")

animais_em_ordem = sorted(animais)

print("Lista em ordem (3 primeiros):")

for x in range(0,3):
    print(f"{x + 1} - {animais_em_ordem[x]}")