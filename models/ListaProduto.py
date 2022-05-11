from typing import Tuple
from models.Produto import Produto
from util import StaticList


class ListaProduto:
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
