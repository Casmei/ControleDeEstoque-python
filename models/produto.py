class Produto:
    def __init__(self, movel: str, codigo: int, cor: str, quantidade: int):
        self.movel = movel
        self.codigo = codigo
        self.cor = cor
        self.quantidade = quantidade

    def __str__(self):
        return f'{self.codigo}\n{self.movel}\n{self.cor}\n{self.quantidade}'