paises = {"Irlanda": "Dublin", "Japão": "Tóquio", "Coréia do Sul": "Seul", "Brasil": "Brasília"}

for x, y in paises.items():
    print(f"{x}\n")

escolha_usuario = input("Digite o País no qual deseja descobrir a capital: ")

print(paises[escolha_usuario])