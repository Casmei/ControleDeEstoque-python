from uuid import uuid4


class Produto:
    def __init__(self, name: str, id=None):
        self.id = id or str(uuid4())
        self.name = name

    def to_dict(self):
        """
        Transformar em dicionário meu objeto produto
        """
        return {"id": self.id, "name": self.name}

    def __str__(self):
        return f"Produtos(id={self.id}, nome={self.name})"

    def __eq__(self, i):
        return i and self.id == i.id
