from uuid import uuid4
from datetime import datetime
from util import StaticList
from typing import Tuple

# * ################## PRODUTO ##################


class Produto:
    def __init__(self, name: str, id=None):
        self.id = id or str(uuid4())
        self.name = name

    def to_dict(self):
        """
        Transformar em dicionário meu objeto produto
        """
        return {"id": self.id, "name": self.name}

    @classmethod
    def from_dict(cls, id, name):
        return cls(name, id)

    def __str__(self):
        return f"Produtos(id={self.id}, nome={self.name})"

    def __eq__(self, i):
        return i and self.id == i.id


# * ################## LISTA DE PRODUTOS ##################
class ProductList:
    def __init__(self, a: list[Tuple[Produto, int]]):
        self.produtos_list = StaticList(len(a), a)

    def to_dict(self):
        return [
            {"produto": produto.to_dict(), "quantidade": amount}
            for produto, amount in self.produtos_list
        ]

    def __iter__(self):
        return iter(self.produtos_list)

    def __str__(self):
        return f'Produtos(lista={", ".join([f"{produto}, quantidade: {amount}" for produto, amount in self.produtos_list])}'


# * ################## ENTRADAS ##################
class Entrada:
    """
    Recebo uma lista de produtos, todos
    os outros dados são criados automaticamente
    """

    def __init__(self, nf: str, product_list: ProductList):
        self.nf = nf
        self.id = str(uuid4())
        self.createdAt = datetime.now()
        self.product_list = product_list

    @classmethod
    def from_dict(cls, nf, product_list: list[ProductList]):
        return cls(nf, product_list)

    def to_dict(self):
        return {
            "id": self.id,
            "nf": self.nf,
            "createdAt": self.createdAt.isoformat(),
            "produtos": self.product_list.to_dict(),
        }

    def __str__(self):
        return f"Entrada(id={self.id}, nf={self.nf}, createdAt={self.createdAt.strftime('%d-%m-%Y')}, produtos={str(self.product_list)})"


# * ################## SAIDA ##################
class Saida:
    def __init__(self):
        pass


# * ################## TOTAL ##################
def total(self):
    ...
