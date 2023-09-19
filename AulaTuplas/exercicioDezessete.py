import operator

paises = (("Brasil", 210000000), ("Argentina", 45000000), ("Nigeria", 213000000), ("Dinamarca", 5870000))

ordenado = sorted(paises, key = operator.itemgetter(1, 0))

print(ordenado)