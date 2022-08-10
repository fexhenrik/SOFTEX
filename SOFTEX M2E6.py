from datetime import date
data_atual = date.today()
ano_atual = data_atual.year

nome = str(input("Insira seu nome completo. "))
anoatual = True

while anoatual == True:
    anonasc = int(input("Insira sua data de nascimento entre 1992 e 2021. "))
    try:
        if anonasc >= 1992 and anonasc <= 2021:
          print(nome)
          print(2022 - anonasc)
          anoatual == False
          break
          
        elif anonasc < 1990 or anonasc > 2021:
          print("Erro! Digite um valor válid. ")
        elif anonasc == ' ':
          raise Exception
        else:
          raise Exception

    except:
      print("Erro. Digite um valor válido. ")
