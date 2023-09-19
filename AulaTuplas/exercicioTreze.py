tupla_inteiros = (2, 4, 6, 8, 10)

todos_pares = True

for x in tupla_inteiros:
    if x % 2 != 0:
        todos_pares = False

if todos_pares == True:
    print("Todos os números são pares!")
else:
    print("Nem todos os números são pares!")