import pandas as pd

# Carregar as planilhas
planilha_a = pd.read_excel('certezaTerceirizados.xlsx')
planilha_b = pd.read_excel('dimTerceirizados.xlsx')

# Comparar as colunas 'sub' das duas planilhas
valores_a_nao_em_b = planilha_a.loc[~planilha_a['subt'].isin(planilha_b['subv'])]

# Salvar os resultados em um arquivo CSV
valores_a_nao_em_b.to_csv('arquivo.csv', index=False)
