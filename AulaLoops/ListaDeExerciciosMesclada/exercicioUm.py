i = 0

resp_usuario_continuar = 1

soma_nota_aluno = 0

while resp_usuario_continuar != 0:
    nota_aluno = float(input("Digite a nota do aluno(a):"))

    soma_nota_aluno = soma_nota_aluno + nota_aluno

    i += 1

    resp_usuario_continuar = int(input("Se deseja continuar digite 1: \nSe deseja parar digite 0: "))

quant_de_notas = i

media = soma_nota_aluno / quant_de_notas

print(f"A média das notas do aluno é de: {media}")