lado_um = int(input("Digite o valor do lado um: "))
lado_dois = int(input("Digite o valor do lado dois: "))
lado_tres = int(input("Digite o valor do lado três: "))

if lado_um == lado_dois and lado_um == lado_tres:
    print("Triângulo Equilátero!")
elif lado_um != lado_dois and lado_um != lado_tres and lado_dois != lado_tres:
    print("Triângulo Escaleno!")
elif lado_um == lado_dois or lado_um == lado_tres or lado_dois == lado_tres:
    print("Triângulo Isósceles!")