numero_um = int(input("Digite o número 1: "))
numero_dois = int(input("Digite o número 2: "))
numero_tres = int(input("Digite o número 3: "))

if numero_um > numero_dois and numero_um > numero_tres:
    print(f"O número {numero_um} é maior do que {numero_dois} e {numero_tres}")
elif numero_dois > numero_um and numero_dois > numero_tres:
    print(f"O número {numero_dois} é maior do que {numero_um} e {numero_tres}")
elif numero_tres > numero_um and numero_tres > numero_dois:
    print(f"O número {numero_tres} é maior do que {numero_um} e {numero_dois}")
else:
    print("Erro!")