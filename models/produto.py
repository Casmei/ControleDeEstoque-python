class Produto:
    def __init__(self, codigo: int, nome: str, quantidade: int):
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade

    def __str__(self):
        return f'{self.codigo}\n{self.movel}\n{self.quantidade}'