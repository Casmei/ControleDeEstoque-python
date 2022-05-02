from time import localtime

class Venda:
  def __init__(self, movel):
    data = localtime()
    self.ano_da_compra = data[1]
    self.mes_da_compra = data[2]
    self.dia_da_compra = data[3]
    self.hora_da_compra = data[4]
    self.minuto_da_compra = data[5]
    self.movel: str = movel

  def retornar_nome_do_movel(self):
    ...
  
  def nome_do_movel(self) -> str:
    return f"{self.movel}"

  def data_da_venda(self) -> str:
    return f"""{self.dia_da_compra}/{self.mes_da_compra}/{self.ano_da_compra}-{self.hora_da_compra}:{self.minuto_da_compra}"""