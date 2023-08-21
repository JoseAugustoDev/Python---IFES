lista_numeros = []

quant_numeros = int(input("Digite a quantidade de números desejada: "))

i = 0

while quant_numeros > i:
    numero_usuario = int(input("Digite o número: "))
    lista_numeros.append(numero_usuario)
    i += 1

maior = 0

for x in lista_numeros:
    if x > maior:
        maior = x
    
print(f"O maior numero é: {maior}")