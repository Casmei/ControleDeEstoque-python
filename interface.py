from util import MenuManager, StaticList
from main import Estoque, Produto
from models import ProductList, Entrada
from InquirerPy import inquirer
from InquirerPy.validator import NumberValidator


from rich.console import Console
from rich.table import Table

menu = MenuManager()
estoque = Estoque()

print = Console().print

######### PRODUTOS #########
def criar_produtos():
    """
    Criar novos produtos, e
    chamar a função de cadastro

    """
    flag = True
    while flag:
        nome = input("Nome do produto: ")
        continuar = input("Deseja adicionar outro: (s/n) ")
        produto = Produto(nome)
        estoque.cadastrar_produto(produto)
        flag = continuar == "s"


def req_deletar_produto():
    produto = input("Digite o nome do produto que deseja deletar: ")
    confirmacao = input(f"Realmente deseja excluir o produto {produto}?: (s/n) ")
    if "s" == confirmacao.lower():
        estoque.deletar_produto(produto)
        print("Produto deletado com sucesso!")
    else:
        return "Deleção cancelada!"


def listar_produtos():
    """
    Pecorrer o Array de produtos no
    arquivo, e retorna-los.
    """
    table = Table(show_header=True, show_lines=False, header_style="bold red")

    table.add_column("ID", justify="center", style="bold green")
    table.add_column("Nome", justify="center", style="bold green")

    for i in estoque.produtos:
        table.add_row(i.id, i.name)

    print(table)


def produto_pelo_nome():
    """
    retorna um produto pelo nome.
    """
    nome = input("Digite o nome do produto que deseja buscar: ")
    produto = estoque.retorna_produto(nome)

    print()
    if produto == None:
        print("Produto não existe")
    else:
        print(f"ID do produto: {produto.id}")
        print(f"Nome do produto: {produto.name}")


def produto_pelo_id():
    """
    retorna um produto pelo ID.
    """
    id = input("Digite o ID do produto que deseja buscar: ")
    produto = estoque.retorna_produto(id)

    print()
    if produto == None:
        print("Produto não existe")
    else:
        print(f"ID do produto: {produto.id}")
        print(f"Nome do produto: {produto.name}")


###########################

######## ENTRADAS #########
def criar_entrada():
    nf = input("Qual a nota fiscal da entrada: ")
    produtos = StaticList(0)

    while True:
        nome = input("Nome do produto: ")
        produto = estoque.produtos.find(lambda produto: produto.name == nome)

        if produto == None:
            print("Produto não existe")
            break

        quantidade = int(input(f"Quantidade de {nome}: "))
        produtos = produtos.add([(produto, quantidade)])

        if input("Deseja adicionar outro produto?: (s/n) ").lower() == "n":
            break

    product_list = ProductList(
        [(produto, quantidade) for produto, quantidade in produtos]
    )
    estoque.cadastrar_entrada(Entrada(nf, product_list))
    print("Entrada cadastrada com sucesso!")


def listar_entrada():
    for i in estoque.entradas:
        table = Table(
            title=f"Entrada {i.nf}", show_header=True, header_style="bold red"
        )

        table.add_column("Produto", justify="center", style="bold green")
        table.add_column("Quantidade", justify="center", style="bold green")

        for produto, quantidade in i.product_list:
            table.add_row(produto.name, str(quantidade))

        print(table)


# # Precisar pegar minha lista de produtos


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
            "Buscar entradas": ...,
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
        "Saída": {
            "Registrar Saída": ...,
            "Listar Saída": ...,
            "Buscar Saída": ...,
        },
        #######################################
        "Ferramentas": {
            "Total de um produto": ...,
            "Relatorio": ...,
        },
    }
)
#############################

menu.show()
