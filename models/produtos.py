class Moveis:
    def __init__(self, codigo, movel, cor, quantidade):
        self.movel = str(movel)
        self.codigo = int(codigo)
        self.cor = str(cor)
        self.quantidade = int(quantidade)
        self.proximo = None

    def __str__(self):
        return f'codigo = {self.codigo}\n nome = {self.movel}\n cor = {self.cor}\n quantidade = {self.quantidade}\n'