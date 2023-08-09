angulo_um = int(input("Digite o ângulo Um: "))
angulo_dois = int(input("Digite o ângulo Dois: "))
angulo_tres = int(input("Digite o ângulo Três: "))

soma_angulos = angulo_um + angulo_dois + angulo_tres

soma_angulos_internos_triangulo = 180

if soma_angulos == soma_angulos_internos_triangulo:
    if angulo_um < 90 and angulo_dois < 90 and angulo_tres < 90:
        print("Triângulo Acutâneo.")
    elif angulo_um == 90 or angulo_dois == 90 or angulo_tres == 90:
        print("Triângulo retângulo")
    elif angulo_um > 90 or angulo_dois > 90 or angulo_tres > 90:
        print("Triângulo Obtusângulo.")
else:
    print("Não é um triângulo.")
