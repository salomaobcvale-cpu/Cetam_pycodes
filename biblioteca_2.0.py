while True:
 print("======= SISTEMA BIBLIOTECÁRIO =======")  
 print("1 - Cadastrar livros")   
 print("2 - Cadastrar alunos")   
 print("3 - Realizar empréstimo")   
 print("4 - Sair")   

opcao = int(input("O que deseja fazer? "))   

if opcao == 1:   

    print("\n======= CADASTRO DE LIVROS =======")   

    quantidade_de_livros = int(input("Quantos livros serão cadastrados? "))   

    for i in range(quantidade_de_livros):   

        print(f"\n----- LIVRO {i + 1} -----")   

        codigo = input("Código do livro: ")   

        if codigo == "":   
            print("O código não pode ficar vazio.")   

        titulo = input("Título: ")   

        if titulo == "":   
            print("O título não pode ficar vazio.")   

        autor = input("Autor: ")   

        if autor == "":   
            print("O autor não pode ficar vazio.")   

        ano = int(input("Ano de publicação: "))   

        if ano <= 0:   
            print("O ano de publicação deve ser válido.")   

        quantidade = int(input("Quantidade disponível: "))   

        if quantidade <= 0:   
            print("A quantidade disponível deve ser maior que zero.")   

        print("Cadastro do livro concluído.")   

elif opcao == 2:   

    print("\n======= CADASTRO DE ALUNOS =======")   

    quantidade_de_alunos = int(input("Quantos alunos serão cadastrados? "))   

    for i in range(quantidade_de_alunos):   

        print(f"\n----- ALUNO {i + 1} -----")   

        matricula = input("Matrícula: ")   

        if matricula == "":   
            print("A matrícula não pode ficar vazia.")   

        nome = input("Nome do aluno: ")   

        if nome == "":   
            print("O nome não pode ficar vazio.")   

        turma = input("Turma: ")   

        if turma == "":   
            print("A turma não pode ficar vazia.")   

        print("Cadastro do aluno concluído.")   

elif opcao == 3:   

    print("\n======= REALIZAR EMPRÉSTIMO =======")   

    codigo = input("Código do livro: ")   

    if codigo == "":   
        print("O código do livro não pode ficar vazio.")   

    matricula = input("Matrícula do aluno: ")   

    if matricula == "":   
        print("A matrícula não pode ficar vazia.")   

    quantidade = int(input("Quantidade disponível do livro: "))   

    if quantidade > 0:   
        print("Empréstimo realizado com sucesso.")   
    else:   
        print("Não é possível realizar o empréstimo. Não há exemplares disponíveis.")   

elif opcao == 4:   
    print("Saindo do sistema...")   
 break  

else:   

    print("Opção inválida. Escolha uma opção de 1 a 4.")
    print("Programa encerrado.")  
        break