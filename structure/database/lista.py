class Lista:

  def __init__(self):
    self. tamanho = 10 
    self.elementos = [None] * self.tamanho
    self.quantidade = 0
  
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
