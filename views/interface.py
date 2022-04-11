from time import sleep
from ..models.produto import Produto
from ..database.lista import Lista

lista = Lista()
produto = Produto()

def main() -> None:
  menu()

def menu() -> None:
  print('==============================')
  print('=========== Mercado ==========')
  print('==============================')

  print('Selecione uma opção abaixo: ')
  print('1 - Cadastrar produto')
  print('2 - Listar produtos')
  print('3 - Comprar produto')
  print('4 - Visualizar carrinho')
  print('5 - Fechar pedido')
  print('6 - Sair do sistema')

  escolha: int = int(input('Opção: '))
  return escolha

def escolhas(escolha) -> None:
  if escolha == 1:
    cadastrar_produto()
  elif escolha == 2:
    listar_produtos()
  elif escolha == 3:
    comprar_produto()
  elif escolha == 4:
    visualizar_carrinho()
  elif escolha == 5:
    fechar_pedido()
  elif escolha == 6:
    print('Volte sempre!')
    sleep(2)
    exit()
  else:
    print('Opção inválida')
    menu()


def cadastrar_produto() -> None:
  pass
def listar_produtos() -> None:
  pass
def comprar_produto() -> None:
  pass
def visualizar_carrinho() -> None:
  pass
def fechar_pedido() -> None:
  pass