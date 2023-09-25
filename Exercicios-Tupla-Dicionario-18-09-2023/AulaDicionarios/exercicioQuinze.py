alimentos_calorias = {"Chocolate": 200, "Frango": 166, "Picanha": 288}

soma_calorias = 0

for x, y in alimentos_calorias.items():
    soma_calorias = soma_calorias + y

print(f"A soma total de calorias é de: {soma_calorias}")