from time import sleep
from models.produto import Produto
from database.lista import Lista
lista = Lista()

def main() -> None:
  menu()

def menu() -> None:
  print('==============================')
  print('=========== Mercado ==========')
  print('==============================')

  print('Selecione uma opção abaixo: ')
  print('1 - Cadastrar produto')
  print('2 - Listar produtos')
  print('3 - Cadastrar venda')
  print('4 - Listar vendas')
  print('5 - Sair do sistema')
  
  escolha: int = int(input('Opção: '))

  if escolha == 1:
    criar_produto()
  elif escolha == 2:
    listar_produtos()
  elif escolha == 3:
    cadastrar_venda()
  elif escolha == 4:
    listar_vendas()
  elif escolha == 5:
    print('Volte sempre!')
    sleep(2)
    exit()
  else:
    print('Opção inválida')
    menu()

def criar_produto() -> None:
  movel = str(input("Digite o nome do movel: "))
  codigo = int(input(f"Digite o código do movel {movel}: "))
  cor = str(input(f"Digite a cor do movel {movel}: "))
  quantidade = int(input(f"Digite a quantidade do movel {movel}: "))
  
  produto = Produto(movel, codigo, cor, quantidade)
  cadastrar_produto_na_lista(produto)

def cadastrar_produto_na_lista(produto):
  lista.inserir_elemento_na_lista(produto)
  print("Cadastro concluído!")
  continuar_cadastro = str(input("Deseja cadastrar outro produto?(s/n) "))

  if continuar_cadastro == "s":
    criar_produto()
  elif continuar_cadastro == "n":
    print("Obrigado!")
    main()
  else:
    print("Opção invalida")
    main()

def listar_produtos() -> str:
  lista.imprimir_elementos_da_lista()

def cadastrar_venda():
  pass

def listar_vendas():
  pass


main()
# tiago otario