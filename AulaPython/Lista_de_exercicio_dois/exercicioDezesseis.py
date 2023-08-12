numero_usuario = int(input("Digite um número com 3 dígitos: "))

primeiro_digito = numero_usuario//100
auxiliar = numero_usuario%100
segundo_digito = auxiliar//10 
terceiro_digito = auxiliar%10

soma_digitos = primeiro_digito + segundo_digito + terceiro_digito

print(f"A soma de {primeiro_digito} + {segundo_digito} + {terceiro_digito} é de: {soma_digitos}")