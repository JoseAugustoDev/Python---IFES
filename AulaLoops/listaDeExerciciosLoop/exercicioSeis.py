num_inicial = 1
prox_num = 1

quant_numeros_seq_fibo = int(input("Digite a quantidade de números que deseja ver da sequência de fibonacci: "))

i = 0

while quant_numeros_seq_fibo > i:
    num_sequencia = num_inicial + prox_num
    num_inicial = prox_num
    prox_num = num_sequencia

    print(num_sequencia)

    i += 1