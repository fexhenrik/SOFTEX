class Identidade:
  def __init__(self, nome, datanasc):
    self.nome = nome
    self.datanasc = datanasc

  def get_nome(self):
    return self.nome

  def set_nome(self, nome):
    self.nome = nome

  def get_datanasc(self):
    return self.datanasc

  def set_datanasc(self, datanasc):
    self.datanasc = datanasc

identidade = Identidade('William', '21/12/1990')
print('Nome: ', identidade.get_nome(), '\nData de Nascimento: ', identidade.get_datanasc())
