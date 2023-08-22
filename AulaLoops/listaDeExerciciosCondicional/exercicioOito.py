numero_um = int(input("Digite um número: "))
numero_dois = int(input("Digite outro número: "))
numero_tres = int(input("Digite outro número: "))

if numero_um > numero_dois and numero_um > numero_tres:
    print(f"{numero_um} é maior do que {numero_dois} e {numero_tres}!")
elif numero_dois > numero_um and numero_dois > numero_tres:
    print(f"{numero_dois} é maior do que {numero_um} e {numero_tres}!")
elif numero_tres > numero_um and numero_tres > numero_dois:
    print(f"{numero_tres} é maior do que {numero_dois} e {numero_um}!")