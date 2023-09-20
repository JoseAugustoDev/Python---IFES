tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

numero_desejado = int(input("Digite o número que deseja encontrar: "))

for x in tupla: 
    if x == numero_desejado:
        print(f"O número {numero_desejado} foi encontrado!")