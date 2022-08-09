import pandas as pd

boletim = {'aluno': ['aluno_1', 'aluno_2', 'aluno_3', 'aluno_4' ],
      'nota_1': [10, 2, 9, 10],
      'nota_2': [6, 10, 5, 5],
      'faltas': [2, 5, 6, 3]
          }

df = pd.DataFrame(boletim)
df['média'] = (df['nota_1'] + df['nota_2']) / 2
df['situação'] = 0

df.loc[df['média'] >= 7, 'situação'] = 'Aprovado'
df.loc[df['média'] < 7, 'situalção'] = 'Reprovado'
df.loc[df['faltas'] > 5, 'situação'] = 'Reprovado'

media = df['média'].median()
faltas = df['faltas'].max()
maiorMedia = df['média'].max()

print(df)
print('A média geral dos alunos: '+str(media))
print('O maior número de faltas: '+str(faltas))
print('A maior média: '+str(maiorMedia))

df.to_csv('alunos_situação.cvs')
