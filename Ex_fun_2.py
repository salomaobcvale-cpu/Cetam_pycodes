biblioteca = []
def cadastrar_livro():
    titulo = input("Informe o título do livro: ")
    autor = input("Informe o autor do livro: ")
    biblioteca.append([titulo, autor])
cadastrar_livro()
print("Livro cadastrado")
def listar_livros():
    for contador in biblioteca:
        print(contador[0], "-", contador[1])
listar_livros()