from models.Saida import Saida
from util import MenuManager, StaticList

from main import Estoque, Produto
from models.ListaProduto import ListaProduto
from models.Entrada import Entrada
from models.Produto import Produto


from rich.console import Console
from rich.table import Table

menu = MenuManager()
estoque = Estoque()

print = Console().print

# * ######### PRODUTOS #########
def criar_produtos():
    """
    Criar novos produtos, e
    chamar a função de cadastro

    """
    flag = True
    while True:
        nome = input("Nome do produto: ")
        continuar = input("Deseja adicionar outro: (s/n) ")
        produto = Produto(nome)
        estoque.cadastrar_produto(produto)
        print()
        print("Produto Cadastrado com Sucesso!")
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


# * ####### ENTRADAS #########
def criar_entrada():
    """
    Cria uma entrada no JSON

    - Pega a nota fiscal da entrada
    - Cria uma lista ```produtos```
    - Loop para adicionar os produtos na lista
        -  Vai pegar o nome do produto e verificar se já existe na lista
        -  Pegar quantidade desse produto
        -  Adicionalos na lista de produtos
        -  Verifico se desejo adicionar outro
    - Cadastro minha entrada, com a nf e uma lista de produtos
    """
    nf = input("Qual a nota fiscal da entrada: ")
    produtos = StaticList(0)
    while True:
        nome = input("Nome do produto: ")

        def comparador(produto):
            return produto.name == nome

        produto = estoque.produtos.find(comparador)

        if produto == None:
            print("Produto não existe")
            break

        quantidade = int(input(f"Quantidade de {nome}: "))
        produtos = produtos.add((produto, quantidade))

        if input("Deseja adicionar outro produto?: (s/n) ").lower() == "n":
            break

    estoque.cadastrar_entrada(Entrada(nf, ListaProduto(produtos)))
    print("Entrada cadastrada com sucesso!")


def listar_entrada():
    for i in estoque.entradas:
        table = Table(
            title=f"Entrada {i.nf}",
            show_header=True,
            header_style="bold red",
        )

        table.add_column("Produto", justify="center", style="bold green")
        table.add_column("Quantidade", justify="center", style="bold green")

        for produto, quantidade in i.lista_produto:
            table.add_row(produto.name, str(quantidade))

        print(table)


def entrada_pela_nf():
    """
    retorna um entrada pela sua nota fiscal.
    """
    nf = input("Digite a nota fiscal da entrada que deseja buscar: ")
    entrada = estoque.retorna_entrada(nf)

    print()
    if entrada == None:
        print("Entrada não existe")
    else:
        print("=" * 70)
        print(f"Nota fiscal: {entrada.nf}")
        print(f"Data de criação: {entrada.createdAt.strftime('%d/%m/%Y')}")
        print("=" * 70)
        table = Table(
            title=f"Entrada {entrada.nf}",
            show_header=True,
            header_style="bold red",
        )

        table.add_column("Produto", justify="center", style="bold green")
        table.add_column("Quantidade", justify="center", style="bold green")

        for produto, quantidade in entrada.lista_produto:
            table.add_row(produto.name, str(quantidade))

        print(table)
        print("=" * 70)


# * ####### SAIDA #########
def criar_saida():
    nf = input("Qual a nota fiscal da saida: ")
    produtos = StaticList(0)
    quantidade = 0

    while True:
        nome = input("Nome do produto a dar baixa: ")
        produto = estoque.produtos.find(lambda produto: produto.name == nome)

        if produto == None:
            print("Produto não existe")
            return

        quantidade = int(input(f"Quantidade de {nome} para dar baixa: "))

        """ def comparador_de_quantidade(era):
            ...

        estoque.entradas.find() """

        # # TODO Lógica de verificar a quantidade ao dar baixa
        # produtos = produtos.add([(produto, quantidade)])

        if input("Deseja adicionar outro produto?: (s/n) ").lower() == "n":
            break

    produtos = produtos.add((produto, quantidade))
    estoque.cadastrar_saida(Saida(nf, ListaProduto(produtos)))
    print("Saida cadastrada com sucesso!")


def listar_saida():
    for i in estoque.saidas:
        table = Table(
            title=f"Saída {i.nf}",
            show_header=True,
            header_style="bold red",
        )

        table.add_column("Produto", justify="center", style="bold green")
        table.add_column("Quantidade", justify="center", style="bold green")

        for produto, quantidade in i.lista_produto:
            table.add_row(produto.name, str(quantidade))

        print(table)


def saida_nf():
    """
    retorna uma saída pela sua nota fiscal.
    """
    nf = input("Digite a nota fiscal da saida que deseja buscar: ")
    saida = estoque.retorna_saida(nf)

    print()
    if saida == None:
        print("saida não existe")
    else:
        print("=" * 70)
        print(f"Nota fiscal: {saida.nf}")
        print(f"Data de criação: {saida.createdAt.strftime('%d/%m/%Y')}")
        print("=" * 70)
        table = Table(
            title=f"Saida {saida.nf}",
            show_header=True,
            header_style="bold red",
        )

        table.add_column("Produto", justify="center", style="bold green")
        table.add_column("Quantidade", justify="center", style="bold green")

        for produto, quantidade in saida.lista_produto:
            table.add_row(produto.name, str(quantidade))

        print(table)
        print("=" * 70)


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
            "Registrar Saída": criar_saida,
            "Listar Saída": listar_saida,
            "Buscar Saída": saida_nf,
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
