raio_esfera = int(input("Digite o valor do raio da esfera:"))

valor_pi = 3.1415

volume_esfera = (4 / 3) * valor_pi * (pow(raio_esfera, 3))

area_superficie_esfera = 4 * valor_pi * (pow(raio_esfera, 2))

print("Considerando PI = 3.1415")
print(f"O valor do volume da esfera de raio {raio_esfera} é de: {volume_esfera}, já o valor da área é de: {area_superficie_esfera}")