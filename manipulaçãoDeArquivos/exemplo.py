# Lendo o Arquivo

with open('manipulaçãoDeArquivos/arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

# Escrevendo no arquivo

with open('manipulaçãoDeArquivos/arquivo2.txt', 'w') as arquivo:
    arquivo.write("São Paulo maior de todos! \n")
    arquivo.write("São Paulo!")

# Lendo o Arquivo

with open('manipulaçãoDeArquivos/arquivo2.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

# Anexando linha no final do arquivo

with open('manipulaçãoDeArquivos/arquivo2.txt', 'a') as arquivo:
    arquivo.write("\nFinal")