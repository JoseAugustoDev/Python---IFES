lista_usuario = []

resp_usuario_continuar = 1

while resp_usuario_continuar != 0:
    numero_usuario = int(input("Digite o número: "))

    lista_usuario.append(numero_usuario)

    resp_usuario_continuar = int(input("Digite 1 se deseja continuar: \nDigite 0 se deseja parar: "))

menor = lista_usuario[0]

for x in lista_usuario:
    if x < menor:
        menor = x

print(f"O menor número dessa lista é: {menor}")