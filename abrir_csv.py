# Usando pandas (a forma mais prática)

import pandas as pd

arquivo = "CEPs.csv"

df = pd.read_csv(arquivo)

# teste para ver se o arquivo foi lido corretamente
# print(df)

#informações sobre o dataframe
def info():
    """retorna informações sobre o dataframe"""
    return df.info()


#Acesso linhas específicas:
def primeiras_linhas(n):
    """retorna as n primeiras linhas da tabela"""
    return df.head(n)

def ultimas_linhas(n):
    """retorna as n últimas linhas da tabela"""
    return df.tail(n)

def distrito_por_linha(indice):
    """retorna os dados de distrito, CEP de início e CEP de fim, de uma linha específica pelo índice"""
    return df[['distritos','CEP_inicio', 'CEP_fim']].iloc[indice]


print("dados de CEP carregados com sucesso")
# # Acessar colunas:
# # quebrado
# def acessar_coluna(str(nome_da_coluna)):
#     return df[nome_da_coluna]
    

# # Iterar sobre linhas:
# def iterar_sobre_linhas(indice_da_coluna):
#     for row in df.iterrows():
#         print(row[indice_da_coluna])
        
# # for index, row in df.iterrows():
# #     print(row['indice_da_coluna'])


# ###AREA DE TESTE###
# for index, row in df.iterrows():
#     print(row['indice_da_coluna'])
# for index, row in df.iterrows():
#     print(row[2:3])

# list=["teste1","teste2","teste3"]

# df.iterrows()


# # Source - https://stackoverflow.com/a/74642175
# # Posted by Sam, modified by community. See post 'Timeline' for change history
# # Retrieved 2026-03-11, License - CC BY-SA 4.0

# for i in range(len(df)):

#     #print(df['a'][i] will produce KeyError: 0
#     #This is because, range(2) [length of df] will give
#     #0, 1
#     #But we don't have 0 as a row in df
#     print(df['CEP_inicio'].iloc[i])

# df["CEP_inicio"].iloc[14]
# df[['distritos','CEP_inicio', 'CEP_fim']].iloc[23]



# distrito_por_linha(26)