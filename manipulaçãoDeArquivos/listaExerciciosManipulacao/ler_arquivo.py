def ler_arquivo(caminho_do_arquivo):
    lista = []
    
    with open(caminho_do_arquivo, 'r') as arquivo:
        for linha in arquivo:
            lista.append(linha)

    return lista