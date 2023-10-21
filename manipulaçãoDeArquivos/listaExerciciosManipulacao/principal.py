def ler_dados():

    nome_estudante = input("Digite o nome do estudante: ")
    idade_estudante = int(input("Digite a idade do estudante: "))
    curso_estudante = input("Digite o curso do estudante: ")

    estudante = {
        "nome": nome_estudante,
        "idade": idade_estudante,
        "curso": curso_estudante,
    }

    return estudante

def ler_varios_alunos():
    quantidade = int (input("Digite a Quantidade: "))
    alunos = []
    for x in range (0,quantidade):
        aluno = ler_dados()
        alunos.append (aluno)
    
    return alunos

def criar_arquivo_lista(lista, nome_arquivo):
    with open (nome_arquivo,"w") as arquivo:
        for item_lista in lista:
            item_lista = str(item_lista)
            arquivo.write(f"{item_lista}\n") 

