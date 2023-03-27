import pandas as pd

def ordena(df, Coluna):
    return df.sort_values(by=[str(Coluna)])

def busca_nome(df, Nome):
    return df.loc[df['Nome'] == Nome]

def busca_versao(df, Versao):
    return df.loc[df['Versao'] == Versao]

df = pd.read_csv('Dados_Pacotes.csv')

#print(ordena(df, 'Nome'))
#print(busca_nome(df, 'pytz'))
#print(busca_versao(df, '4.4.0'))