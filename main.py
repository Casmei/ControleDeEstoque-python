from util import JSONDatabase
from models import Product, Entrada, Saida, Lista

db = JSONDatabase()

class Estoque:
    def __init__(self):
        self.lista = Lista()

    # TODO ADICIONAR ENTRADA
    def add(self, entrada: Entrada):
        """
        Vai criar uma nova entrada,
        e adicionar a lista
        """
        return self.lista.inserir_elemento_na_lista(entrada)
        
    # TODO RETORNAR TODAS AS ENTRADAS
    def get_all(self):
        ...

    # TODO RETORNAR ENTRADA PELO ID
    def get_by_id(self, id):
        ...
    
    # TODO DECREMENTAR QUANTIDADE DO ITEM
    def decrement(self, id):
        ...

    # TODO RETORNAR VENDAS
    def get_all_decrements(self):
        ...

    # TODO RETORNAR VENDAS PELO ID
    def get_decrement_by_id(seld, id):
        ...

    # TODO RETORNAR QUANTIDADE DE UM PRODUTO
    def product_total(self, name):
        ...

    # TODO RETORNAR REGISTRO DE VENDAS COM TOTAL DE SAIDAS E ENTRADAS
    def registry():
        ...