class Node: 
  def __init__ (self, dados):
    self.dados = dados
    self.esquerda = None
    self.direita = None


  def ordem(temp):
    if (not temp):
      return
    ordem(temp.esquerda)
    print(temp.dados, end = " ")
    ordem(temp.direita)

def removerR(raiz, no):
  i = []
  i.append(raiz)
  while (len(i)):
    temp = i.pop(0)
    if temp is no:
      temp = None
      return
    if temp.direita:
      if temp.direita is no:
        temp.direita = None
        return
      else:
        i.append(temp.direita)
    if temp.esquerda:
      if temp.esquerd is no:
        temp.esquerda = None
      else:
        i.append(temp.esquerda)


def remover (raiz, chave):
    if raiz == None:
      return None
    if raiz.esquerda == None and raiz.direita == None:
      if raiz.chave == chave:
        return None
      else: 
        return raiz
    chave_no = None
    i = []
    i.append(raiz)
    temp = None
    while (len(i)):
      temp = i.pop(0)
      if temp.dados == chave:
        chave_no = temp
      if temp.esquerda:
        i.append(temp.esquerda)
      if temp.direita:
        i.append(temp.direita)
    if chave_no:
        x = temp.dados
        removerR(raiz, temp)
        chave_no.dados = x
    return raiz

if __name__ == '__main__':
    raiz = Node(20)
    raiz.esquerda = Node(18)
    raiz.esquerda.esquerda = Node(16)
    raiz.direita = Node(15)
    raiz.direita.esquerda = Node(6)
    raiz.direita.direita = Node(4)
    raiz.direita.direita.direita = Node(3)
    print("Antes: ")
    ordem(raiz)
    chave = 20
    chave = remover(raiz, chave)
    print()
    print("Depois: ")
    ordem(raiz)
