import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

#Primeira Questao
n_40 = len(df.loc[df['age'] > 40].index)
n_col_alto = len(df.loc[(df['chol'] > 240) & (df['age'] > 40)].index)
Porc1 = 100*n_col_alto/n_40
print('Porcentagem de pessoas com mais de 40 anos que tem colesterol alto: ', Porc1, '\n')

#Segunda Questao
n_col_alto = len(df.loc[(df['chol'] > 240) & (df['age'] > 40)].index)
n_col_fbs_alto = len(df.loc[(df['chol'] > 240) & (df['age'] > 40) & (df['fbs'] == 1)].index)
Porc2 = 100*n_col_fbs_alto/n_col_alto
print('Porcentagem de pessoas com mais de 40 anos e com colesterol alto que tem alto teor de açúcar: ', Porc2, "\n")


#Terceira Questão
n_hipertrofia_col_fbs_alto = len(df.loc[(df['chol'] > 240) & (df['age'] > 40) & (df['fbs'] == 1) & (df['restecg'] == 2)].index)
n_hipertrofia_total = len(df.loc[(df['restecg'] == 2)].index)

print(n_col_fbs_alto, "\n")
print(n_hipertrofia_col_fbs_alto, "\n")
print(n_hipertrofia_total, "\n")

# Das 24 pessoas que possuem colesterol alto e alto teor de açúcar no sangue e tem mais de 40 anos,
# 18 possuem hipertrofia ventricular esquerda. Ou seja, 75% das pessoas deste grupo possuem a doença.

# Contudo, é provável que existam outras causas para esta doença, uma vez que ao analisar todo
# o conteúdo amostral, 148 pessoas a possuem. Ou seja, do total, apenas 12% dos que tem a doença
# também possuem colestero alto, alto teor de açúcar no sangue e mais de 40 anos.