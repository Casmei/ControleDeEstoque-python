op = 0
while op != 5:
    op = int(input('Bem Vindo a Elô Eletro! \n Escolha qual opção você deseja :\n [1] Inserir Moveis \n [2] Listar Moveis\n [3] Pesquisar Moveis\n [4] Pesquisar Vendas\n [5] Sair'))
    if op == 1:
        li.inserir()
    elif op == 2:
        li.imprimir()
    elif op == 3:
        li.pesquisar()
    elif op == 4:
        li.inserir()
    elif op == 5:
        li.sair()
    else:
        print('digite uma opcao valida !')