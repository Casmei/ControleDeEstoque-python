from util import StaticList


class ListaProduto:
    def __init__(self, conjunto: StaticList):
        self.lista_produtos = conjunto

    def to_dict(self):
        return [
            {"produto": produto.to_dict(), "quantidade": quantidade}
            for produto, quantidade in self.lista_produtos
        ]

    def __iter__(self):
        return iter(self.lista_produtos)

    def __str__(self):
        return f'Produtos(lista={", ".join([f"{produto}, quantidade: {quantidade}" for produto, quantidade in self.lista_produtos])}'
