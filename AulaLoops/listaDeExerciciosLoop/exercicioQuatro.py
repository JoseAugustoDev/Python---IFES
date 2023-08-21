lista_numeros = []

quant_numeros = int(input("Digite a quantidade de números: "))

soma_pares = 0
soma_impares = 0

i = 0

while quant_numeros > i:
    numero_usuario = int(input("Digite o número: "))
    lista_numeros.append(numero_usuario)

    i += 1

for x in lista_numeros:
    if x % 2 == 0:
        soma_pares += 1
    elif x % 2 != 0:
        soma_impares += 1
    
print(f"O total de números ímpares é de: {soma_impares}")
print(f"O total de números pares é de: {soma_pares}")