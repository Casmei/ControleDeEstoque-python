class Lista:

    def __init__(self):
        self.inicio = None

    def inserir(self, codigo, movel, cor, quantidade):
        novo_movel = Moveis(codigo, movel, cor, quantidade)
        novo_movel.proximo = self.inicio
        self.inicio = novo_movel

    def imprimir(self):
        atual = self.inicio
        while atual != None:
            print(atual)
            atual = atual.proximo
        print()

    def pesquisar(self, codigo):
        if self.inicio == None:
            print("lista vazia !")
            return None
        else:
            atual = self.inicio
            while atual.codigo != codigo:
                if atual.proximo == None:
                    return None
                else:
                  atual = atual.proximo
                return atual
