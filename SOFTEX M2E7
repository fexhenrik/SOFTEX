#Programa desenvolvido em https://replit.com/
X = 0
Y = 0
Z = 0
branco = 0

while True:
    print("Digite seu voto: ")
    print("1 = Candidato_X"), print("2 = Candidato_Y"), print("3 = Candidato Z"), print("4 = Brancos e Nulos")
    try:
        voto = int(input("Digite seu voto: "))
        if voto == 1:
            X += 1
        elif voto == 2:
            Y += 1
        elif voto == 3:
            Z += 1
        elif voto == 4:
            branco += 1
        else:
            print("Opção Inválida! Digite novamente. ")
            continue 

        sair = int(input("Deseja encerrar a votação? 1) Sim, sair 2) Não, continuar"))
        if sair == 1:
              print(f'Votos computados para o Candidato_X foram: {X}')
              print(f'Votos computados para o Candidato_Y foram: {Y}')
              print(f'Votos computados para o Candidato_Z foram: {Z}')
              print(f'Votos brancos foram: {branco}')
              if X > Y and X > Z:
                print("O Candidato_X foi o vencedor das eleições.")
              elif Y > Z and Y > X:
                print("O Candidato_Y foi o vencedor das eleições.")
              elif Z > Y and Z > X:
                print("O Candidato_Z foi o vencedor das eleições.")
              elif branco > X and branco > Y and branco > Z:
                print("Houveram mais votos brancos.")
              break 

        elif sair == 2: 
              continue
              
    except Exception:
      print("ERROR")
