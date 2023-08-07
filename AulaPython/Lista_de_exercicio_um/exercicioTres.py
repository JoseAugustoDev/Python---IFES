altura_parede = float(input('Digite a altura da parede:'))
base_parede = float(input('Digite a base da parede:'))

altura_azuleijo = float(input('Digite a altura do azuleijo:'))
base_azuleijo = float(input('Digite a base do azuleijo:'))

area_parede = altura_parede * base_parede
area_azuleijo = altura_azuleijo * base_azuleijo

quant_azuleijos_na_parede = area_parede / area_azuleijo

print(f"A quantidade de azuleijos que cabem na parede é de: {quant_azuleijos_na_parede}")