from util import JSONDatabase, StaticList
from models import Produto, Entrada, ProductList


db = JSONDatabase("produtos.json")


class Estoque:
    def __init__(self):
        read = db.read()

        produtos = read.get("produtos", None)
        entradas = read.get("entradas", None)

        self.produtos = StaticList(0)
        self.entradas = StaticList(0)
        self.saidas = StaticList(0)

        if produtos:
            self.produtos = StaticList(len(produtos))
            for i in produtos:
                self.produtos = self.produtos.add(Produto.from_dict(i["id"], i["name"]))

        if entradas:
            self.entradas = StaticList(len(entradas))
            for i in entradas:
                produtos = [
                    (
                        Produto.from_dict(i["produto"]["id"], i["produto"]["name"]),
                        i["quantidade"],
                    )
                    for i in i["produtos"]
                ]
                self.entradas = self.entradas.add(
                    Entrada.from_dict(i["nf"], ProductList(produtos))
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

    # TODO ADICIONAR ENTRADA
    def cadastrar_entrada(self, entrada: Entrada):
        """
        Vai criar uma nova entrada, e adicionar a lista
        """
        self.entradas = self.entradas.add(entrada)
        # adiciona o produto ao Json
        db.write(self.to_dict())

    # TODO RETORNAR TODAS AS ENTRADAS
    def get_all(self):
        ...

    # TODO RETORNAR ENTRADA PELO ID
    def get_by_id(self, id):
        ...

    #################### SAIDAS ####################
    # TODO DECREMENTAR QUANTIDADE DO ITEM
    def decrement(self, id):
        ...

    # TODO RETORNAR VENDAS
    def get_all_decrements(self):
        ...

    # TODO RETORNAR VENDAS PELO ID
    def get_decrement_by_id(seld, id):
        ...

    #################### FERRAMENTAS ####################
    # TODO RETORNAR QUANTIDADE DE UM PRODUTO
    def product_total(self, name):
        ...

    # TODO RETORNAR REGISTRO DE VENDAS COM TOTAL DE SAIDAS E ENTRADAS
    def registry():
        ...
