lista_numeros = [0, 1, 2, 1, 2, 4, 5, 7, 9, 5]
lista_sem_duplicados = []

for i in lista_numeros:
    if i not in lista_sem_duplicados:
        lista_sem_duplicados.append(i)

print(lista_sem_duplicados)