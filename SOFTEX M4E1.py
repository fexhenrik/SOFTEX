#objetos materiais

class alimento:
  def __init__(self, nome, tipo, validade):
    self.nome = nome
    self.tipo = tipo
    self.validade = validade

  def exibir(self):
    print(self.nome, self.tipo, self.validade)

alimento = alimento('Nome: feijão', '\nTipo: perecível', '\nValidade: 2023')
alimento.exibir()

class roupa:
  def __init__(self, marca, tecido, preço):
    self.marca = marca
    self.tecido = tecido
    self.preço = preço

  def exibir0(self):
    print(self.marca, self.tecido, self.preço)

roupa = roupa('\nMarca = Gucci', '\nTecido: Couro Animal', '\nValor: U$7,500')
roupa.exibir0()

#objetos abstratos

class reserva_rest:
  def __init__(self, nome_res, nome_rest, horario, mesa):
      self.nome_res = nome_res
      self.nome_rest = nome_rest
      self.horario = horario
      self.mesa = mesa

  def exibir1(self):
    print(self.nome_rest, self.horario, self.mesa)

reserva_rest = reserva_rest('\nReservista: João Miguel Campos', '\nRestaurante: Oliver Garden', '\nHorário: 20:30', '\nMesa Escolhida: 13')
reserva_rest.exibir1()

class matricula:
  def __init__(self, nome, escola, turma, turno):
      self.nome = nome
      self.escola = escola
      self.turma = turma
      self.turno = turno

  def exibir2(self):
    print(self.nome, self.escola, self.turma, self.turno)

matricula = matricula('\nNome do Aluno: Pedro Vincente Camargo', '\nEscola: Escola Nossa Senhora do Carmo', '\nTurma: 3º ano médio', '\nTurno: Noite')
matricula.exibir2()
