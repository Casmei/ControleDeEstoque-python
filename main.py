from models.Saida import Saida
from util import JSONDatabase, StaticList
from models.Produto import Produto
from models.Entrada import Entrada
from models.ListaProduto import ListaProduto


db = JSONDatabase("produtos.json")


class Estoque:
    def __init__(self):
        """
        Vai ler os dados no banco de dados,
        e armazenar nas variáveis
        """
        read = db.read()
        produtos = read.get("produtos", None)
        entradas = read.get("entradas", None)
        saidas = read.get("saidas", None)

        """
        Caso não tenha essas classes
        """
        self.produtos = StaticList(0)
        self.entradas = StaticList(0)
        self.saidas = StaticList(0)

        """
        Com os dados armazenados nas variáveis,
        vamos passar para a StaticList
        """
        # Se existir produtos no Bd
        if produtos:
            for i in produtos:
                # Transforma o produto json para a classe Produto
                self.produtos = self.produtos.add(Produto.from_dict(i["id"], i["name"]))

        # Se existir Entradas no Bd
        if entradas:
            for i in entradas:
                produtos = [
                    (
                        Produto.from_dict(i["produto"]["id"], i["produto"]["name"]),
                        i["quantidade"],
                    )
                    for i in i["produtos"]
                ]
                self.entradas = self.entradas.add(
                    Entrada.from_dict(i["nf"], ListaProduto(produtos))
                )

        if saidas:
            for i in saidas:
                produtos = [
                    (
                        Produto.from_dict(i["produto"]["id"], i["produto"]["name"]),
                        i["quantidade"],
                    )
                    for i in i["produtos"]
                ]
                self.saidas = self.saidas.add(
                    Saida.from_dict(i["nf"], ListaProduto(produtos))
                )

    def to_dict(self):
        """
        Transformar em dicionário os valores passados
        """
        return {
            "produtos": [i.to_dict() for i in self.produtos],
            "entradas": [i.to_dict() for i in self.entradas],
            "saidas": [i.to_dict() for i in self.saidas],
        }

        ...

    # * ################## LÓGICA DOS PRODUTOS ##################
    def cadastrar_produto(self, produto: Produto):
        """
        Cadastrar o produto no
        arquivo e adiciona-lo na lista simples.
        Parâmetros: Recebe o produto do tipo produto.
        """
        self.produtos = self.produtos.add(produto)
        db.write(self.to_dict())

    def retorna_produto(self, nome):
        """
        Realizar uma busca pelo nome do
        produto.
        Parâmetro: Nome do produto
        """
        if len(nome) > 30:

            def find(produto):
                return produto.id == nome

        else:

            def find(produto):
                return produto.name == nome

        return self.produtos.find(find)

    def deletar_produto(self, nome):
        produto = self.retorna_produto(nome)
        self.produtos.remove(produto)

        db.write(self.to_dict())
        return "Item removido!"

    # * ################## LÓGICA DAS ENTRADAS ##################
    def cadastrar_entrada(self, entrada: Entrada):
        """
        Vai criar uma nova entrada, e adicionar a lista
        """
        self.entradas = self.entradas.add(entrada)
        # adiciona o produto ao Json
        db.write(self.to_dict())

    def retorna_entrada(self, nf):
        return self.entradas.find(lambda entrada: entrada.nf == nf)

    # * #################### SAIDAS ####################
    def cadastrar_saida(self, saida: Saida):
        """
        Vai criar uma nova saida, e adicionar a lista
        """
        self.saida = self.saidas.add(saida)
        # adiciona o produto ao Json
        db.write(self.to_dict())
        ...

    def get_all_decrements(self):
        ...

    def get_decrement_by_id(seld, id):
        ...

    #################### FERRAMENTAS ####################
    def product_total(self, name):
        ...

    def registry():
        ...
