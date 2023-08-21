numero_usuario = int(input("Digite o número que deseja descobrir o fatorial: "))
aux = numero_usuario

i = numero_usuario

while i > 1:
    i -= 1
    
    numero_usuario = numero_usuario * i


print(f"O fatorial de {aux} é {numero_usuario}")