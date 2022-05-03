from uuid import uuid4
from datetime import datetime

class Product:
    def __init__(self, name: str):
        self.name = name

    def to_dict(self):
        return { 'name': self.name }

class Entrada:
    def __init__(self, nf: str, quantity: int, products_list: list[Product]):
        self.id = uuid4()
        self.createdAt = datetime()
        self.nf = nf
        self.quantity = quantity
        self.products_list = products_list

        self.products_as_dict = []
        for i in products_list:
            self.products_as_dict.append(i.to_dict())

    def to_dict(self):
        return {
            'id': self.id,
            'createdAt': self.createdAt,
            'nf': self.nf,
            'products': self.products_as_dict,
            'quantity': self.quantity
        }

class Saida:
    def __init__(self):
        pass

class Lista:
    def __init__(self, size: int):
        self.size = size

    # TODO TRANSFORMAR EM UMA LISTA DINÂMICA
    def inserir_elemento_na_lista(self, elemento):
      if self.quantidade == 10:
        return "Tamanho da lista insuficiente"
      else:
        self.elementos[self.quantidade] = elemento
        self.quantidade += 1

    def remover_elemento_da_lista(self, posicao):
      if posicao == len(self.elementos) - 1:
        self.quantidade -= 1
      else:
        for i in range(posicao, self.quantidade):
          self.elementos[i] = self.elementos[i + 1]
        self.quantidade -= 1

    def substituir_elemento_da_lista(self, posicao, elemento):
      if posicao >= self.quantidade:
        return "Posição fora da lista"
      else:
        self.elementos[posicao] = elemento
    
    def pesquisar_elemento_da_lista(self, posicao):
      if posicao >= 10 or posicao < 0:
        return "Posição fora da lista"
      else:
        return self.elementos[posicao]

    def imprimir_elementos_da_lista(self):
      for i in range(self.quantidade):
        print(self.elementos[i])

# TODO RETORNAR O TOTAL DE DETERMINADO PRODUTO
def total(self):
  ...