from models.Saida import Saida
from util import MenuManager, StaticList

from main import Estoque, Produto
from models.ListaProduto import ListaProduto
from models.Entrada import Entrada
from models.Produto import Produto

menu = MenuManager()
estoque = Estoque()

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

# * ######### PRODUTOS #########
def criar_produtos():
    """
    Criar novos produtos, e
    chamar a função de cadastro

    """
    print("=" * 70)
    while True:
        nome = input("Nome do produto: ")
        continuar = input("Deseja adicionar outro: (s/n) ")
        produto = Produto(nome)
        estoque.cadastrar_produto(produto)
        print(f"{GREEN}Produto Cadastrado com Sucesso!{RESET}")
        print()
        if continuar.lower() == "n":
            break
    print("=" * 70)


def req_deletar_produto():
    print("=" * 70)
    # TODO FAZER A VALIDAÇÃO DO NOME DO PRODUTO
    produto = input("Digite o nome do produto que deseja deletar: ")
    confirmacao = input(f"Realmente deseja excluir o produto {produto}?: (s/n) ")
    if "s" == confirmacao.lower():
        estoque.deletar_produto(produto)
        print(f"{GREEN}Produto deletado com sucesso!{RESET}")
    else:
        print(f"{RED}Deleção cancelada!{RESET}")
    print("=" * 70)


def listar_produtos():
    """
    Pecorrer o Array de produtos no
    arquivo, e retorna-los.
    """
    print("=" * 70)
    print("Listagem de Produtos")
    if len(estoque.produtos) == 0:
        print(f"{RED}Não há produtos cadastrados!{RESET}")
    else:
        for i in estoque.produtos:
            espaço_id = gerar_espacos(i.id, 32)
            espaço_name = gerar_espacos(i.name, 12)
            print(
                f"| {BLUE}{i.name}{RESET} {espaço_name} | {YELLOW}{i.id}{RESET} {espaço_id}"
            )
    print("=" * 70)


def produto_pelo_nome():
    """
    retorna um produto pelo nome.
    """
    nome = input("Digite o nome do produto que deseja buscar: ")
    produto = estoque.retorna_produto(nome)

    print("=" * 70)
    if produto == None:
        print(f"{RED}Produto não existe{RESET}")
    else:
        print(f"ID do produto: {YELLOW}{produto.id}{RESET}")
        print(f"Nome do produto: {YELLOW}{produto.name}{RESET}")
    print("=" * 70)


def produto_pelo_id():
    """
    retorna um produto pelo ID.
    """
    print("=" * 70)
    id = input("Digite o ID do produto que deseja buscar: ")
    produto = estoque.retorna_produto(id)

    print()
    if produto == None:
        print("{RED}Produto não existe{RESET}")
    else:
        print(f"ID do produto: {YELLOW}{produto.id}{RESET}")
        print(f"Nome do produto: {YELLOW}{produto.name}{RESET}")
    print("=" * 70)


# * ####### ENTRADAS #########
def criar_entrada():
    print("=" * 70)
    nf = input("Qual a nota fiscal da entrada: ")
    produtos = StaticList(0)
    while True:
        nome = input("Nome do produto: ")

        def comparador(produto):
            return produto.name == nome

        produto = estoque.produtos.find(comparador)

        if produto == None:
            print(f"{RED}Produto não existe{RESET}")
            print("=" * 70)
            return

        quantidade = int(input(f"Quantidade de {nome}: "))
        produtos = produtos.add((produto, quantidade))

        if input("Deseja adicionar outro produto?: (s/n) ").lower() == "n":
            break

    estoque.cadastrar_entrada(Entrada(nf, ListaProduto(produtos)))
    print(f"{GREEN}Entrada cadastrada com sucesso!{RESET}")
    print("=" * 70)


def listar_entrada():
    print("=" * 70)

    if len(estoque.entradas) == 0:
        print(f"{RED}Não há entradas cadastradas!{RESET}")
        print("=" * 70)
    else:
        for i in estoque.entradas:
            print()
            print(f"Nota fiscal da entrada: {YELLOW}{i.nf}{RESET}")
            print(f"Data da entrada: {YELLOW}{i.createdAt.strftime('%d-%m-%Y')}{RESET}")
            print()
            for produto, quantidade in i.lista_produto:
                espaco_produto = gerar_espacos(produto.name, 15)
                espaco_quantidade = gerar_espacos(str(quantidade), 15)
                print(
                    f"{produto.name} {espaco_produto} | {quantidade} {espaco_quantidade}"
                )

            if len(estoque.entradas) > 1:
                print()
                print("*" * 30)
        print()
        print("=" * 70)


def gerar_espacos(item, tamanho: int):
    return ((len(item) - tamanho) * -1) * " "


def entrada_pela_nf():
    """
    retorna um entrada pela sua nota fiscal.
    """
    print("=" * 70)
    nf = input("Digite a nota fiscal da entrada que deseja buscar: ")
    entrada = estoque.retorna_entrada(nf)
    if entrada == None:
        print(f"{RED}Entrada não existe{RESET}")
        print("=" * 70)
        return
    print(f"Nota fiscal: {YELLOW}{entrada.nf}{RESET}")
    print(f"Data de criação: {YELLOW}{entrada.createdAt.strftime('%d/%m/%Y')}{RESET}")
    # TODO PRECISO FAZER ESSA LÓGICA
    print()
    if not entrada.lista_produto:
        print(f"{RED}Não há produtos cadastrados nesta entrada!{RESET}")
        print("=" * 70)
    else:
        for produto, quantidade in entrada.lista_produto:
            espaco_produto = gerar_espacos(produto.name, 15)
            espaco_quantidade = gerar_espacos(str(quantidade), 15)
            print(f"{produto.name} {espaco_produto} | {quantidade} {espaco_quantidade}")
    print("=" * 70)


# * ####### SAIDA #########
# def criar_saida():
#     nf = input("Qual a nota fiscal da saida: ")
#     produtos = StaticList(0)
#     quantidade = 0

#     while True:
#         nome = input("Nome do produto a dar baixa: ")
#         produto = estoque.produtos.find(lambda produto: produto.name == nome)

#         if produto == None:
#             print("Produto não existe")
#             return

#         quantidade = int(input(f"Quantidade de {nome} para dar baixa: "))

#         """ def comparador_de_quantidade(era):
#             ...

#         estoque.entradas.find() """

#         # # TODO Lógica de verificar a quantidade ao dar baixa
#         # produtos = produtos.add([(produto, quantidade)])

#         if input("Deseja adicionar outro produto?: (s/n) ").lower() == "n":
#             break

#     produtos = produtos.add((produto, quantidade))
#     estoque.cadastrar_saida(Saida(nf, ListaProduto(produtos)))
#     print("Saida cadastrada com sucesso!")


# def listar_saida():
#     for i in estoque.saidas:
#         table = Table(
#             title=f"Saída {i.nf}",
#             show_header=True,
#             header_style="bold red",
#         )

#         table.add_column("Produto", justify="center", style="bold green")
#         table.add_column("Quantidade", justify="center", style="bold green")

#         for produto, quantidade in i.lista_produto:
#             table.add_row(produto.name, str(quantidade))

#         print(table)


# def saida_nf():
#     """
#     retorna uma saída pela sua nota fiscal.
#     """
#     nf = input("Digite a nota fiscal da saida que deseja buscar: ")
#     saida = estoque.retorna_saida(nf)

#     print()
#     if saida == None:
#         print("saida não existe")
#     else:
#         print("=" * 70)
#         print(f"Nota fiscal: {saida.nf}")
#         print(f"Data de criação: {saida.createdAt.strftime('%d/%m/%Y')}")
#         print("=" * 70)
#         table = Table(
#             title=f"Saida {saida.nf}",
#             show_header=True,
#             header_style="bold red",
#         )

#         table.add_column("Produto", justify="center", style="bold green")
#         table.add_column("Quantidade", justify="center", style="bold green")

#         for produto, quantidade in saida.lista_produto:
#             table.add_row(produto.name, str(quantidade))

#         print(table)
#         print("=" * 70)


# * ########## FERRAMENTAS #############
def total_produto():
    ...
    # produto = input("Digite o nome do produto que deseja saber o total")


############ MENU ############
menu.format_title(lambda title: f"-<< {title} >>-")
menu.format_option(lambda index, option: f"[{index}] - {option}")
menu.format_input(lambda: "Escolha uma opção: ")
menu.format_sequence(lambda s: " -> ".join(s) + "\n")
menu.format_back(lambda index: f"[{index}] - Voltar")

menu.add(
    {
        "Estoque": {
            "Entradas": menu.to("Entradas"),
            "Produtos": menu.to("Produtos"),
            "Saidas": menu.to("Saidas"),
            "Ferramentas": menu.to("Ferramentas"),
            "Sair": menu.close,
        },
        #######################################
        "Entradas": {
            "Registrar nova Entrada": criar_entrada,
            "Listar entradas": listar_entrada,
            "Buscar entradas": entrada_pela_nf,
        },
        #######################################
        "Produtos": {
            "Adicionar Produto": criar_produtos,
            "Deletar Produto": req_deletar_produto,
            "Listar Produtos": listar_produtos,
            "Buscar Produtos": menu.to("Buscar Produtos"),
        },
        "Buscar Produtos": {
            "Buscar produto pelo nome": produto_pelo_nome,
            "Buscar produto pelo ID": produto_pelo_id,
        },
        #######################################
        "Saidas": {
            "Registrar Saída": ...,
            "Listar Saída": ...,
            "Buscar Saída": ...,
        },
        #######################################
        "Ferramentas": {
            "Total de um produto": total_produto,
            "Relatório": ...,
        },
    }
)
#############################

menu.show()


"""
Eu tenho uma loja. Essa loja recebe várias entradas de um mesmo produto

5 entradas e nas 5 veio 10 mandiocas = 50 mandiocas

saidas = valor que eu vendi - o total do produto que eu tenho no estoque

"""
