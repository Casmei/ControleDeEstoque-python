from datetime import datetime
from uuid import uuid4
from models.ListaProduto import ListaProduto


class Saida:
    """
    Recebo uma lista de produtos vendidos, todos
    os outros dados são criados automaticamente
    """

    def __init__(self, nf: str, lista_produto: ListaProduto):
        self.nf = nf
        self.id = str(uuid4())
        self.createdAt = datetime.now()
        self.lista_produto = lista_produto

    @classmethod
    def from_dict(cls, nf, lista_produto):
        return cls(nf, lista_produto)

    def to_dict(self):
        return {
            "id": self.id,
            "nf": self.nf,
            "createdAt": self.createdAt.isoformat(),
            "produtos": self.lista_produto.to_dict(),
        }

    def __str__(self):
        return f"Saida(id={self.id}, nf={self.nf}, createdAt={self.createdAt.strftime('%d-%m-%Y')}, produtos={str(self.product_list)})"
