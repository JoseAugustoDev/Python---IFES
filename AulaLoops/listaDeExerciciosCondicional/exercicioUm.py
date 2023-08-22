numero_usuario = int(input("Digite um número: "))

if numero_usuario > 0:
    print(f"{numero_usuario} é positivo!")
elif numero_usuario == 0:
    print(f"{numero_usuario} é 0!")
elif numero_usuario < 0:
    print(f"{numero_usuario} é negativo!")