meu_dicionario = {}

dicionario_frutas = {'maçã': 3, 'banana': 2, 'laranja': 4}

pessoa = {"nome": "Jose", "idade": 18, "estado_civil": "solteiro"}

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["estado_civil"])

pessoa["escola"] = "IFES"

print(pessoa["escola"])

print(pessoa)

pessoa["escola"] = "ABL"

print(pessoa["escola"])

for chave in pessoa:
    print(chave)

for chave, items in pessoa.items():
    print(f"{chave} = {items}")