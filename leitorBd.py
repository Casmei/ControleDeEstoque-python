class LeitorArquivoProduto:
  def __init__(self, nome_arquivo):
    self.nome_arquivo: nome_arquivo
    self.arquivo = open(self.nome_arquivo, 'r+', encoding='UTF-8')

  def fechar(self):
    self.arquivo.close()
    self.nome_arquivo = None
  
  def proximo_produto(self):
    self.arquivo
    nome = self.arquivo.readline().rstrip()

    if nome == "":
      return None

    cpf = self.arquivo.readline().rstrip()
    salario = self.arquivo.readline().rstrip()
    cargo = self.arquivo.readline().rstrip()

    return Funcionario(nome, cpf, salario, cargo)
