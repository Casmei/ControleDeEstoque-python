from main import Estoque as estoque

def mostrar_menu():
    print(" --------------- MENU --------------- ")
    print(" [1] - Cadastrar novo usuário ")
    print(" [2] - Listar funcionários ")
    print(" [3] - Buscar funcionário pelo CPF ")
    print(" [4] - Fechar programa ")
    
    return int(input(" Digite o número da operação: "))

def executa_opcao_do_menu(res, sacola_funcionarios):
  match res:
        case 1:
          cadastrar_produto()
          return True
          
        case 2:
          listar_todos_funcionarios(sacola_funcionarios)
          return True
          
        case 3:
          buscar_funcionario_por_cpf(sacola_funcionarios)
          return True
          
        case 4:
          exibir_mensagem_de_encerramento()
          return False
        
        case _:
          caso_opcao_inválida()
          return True

def cadastrar_produto():
    

def caso_opcao_inválida():
    print('\nOpção inválida!')
    input("Digite qualquer tecla para tentar novamente...")

def exibir_mensagem_de_encerramento():
    print('\nPrograma Fechado!')

def comeca_interface():
  
  flag = True
  while flag:
      res = mostrar_menu()
      flag = executa_opcao_do_menu(res, sacola_funcionarios)
      print('\n')
      
comeca_interface()