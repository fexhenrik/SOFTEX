class petschool:
  def __init__(self, nome, especie, raça, turno):
    self.nome = nome
    self.especie = especie
    self.raça = raça
    self.turno = turno

  def exibir1(self):
    print(self.nome, self.especie, self.raça, self.turno)
  def exibir2(self):
    print(self.nome, self.especie, self.raça, self.turno)
  def exibir3(self):
    print(self.nome, self.especie, self.raça, self.turno)


pet1 = petschool('Bellinha', '\nCão', '\nPoodie', '\nTarde')
pet2 = petschool('\nDante', '\nGato', '\nPersa', '\nTarde')
pet3 = petschool('\nBolinha', '\nCão', '\nLabrador', '\nManhã')

pet1.exibir1()
pet2.exibir2()
pet3.exibir3()
