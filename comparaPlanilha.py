import pandas as pd

# Ler as planilhas A e B
planilha_a = pd.read_excel('certezaTerceirizados.xlsx')
planilha_b = pd.read_excel('dimTerceirizados.xlsx')

# Filtrar os valores da coluna 'nomeSub' da planilha A que não estão presentes na planilha B
valores_exclusivos = planilha_a[~planilha_a['sub'].isin(planilha_b['sub'])]

# Salvar os valores exclusivos em um arquivo CSV
valores_exclusivos.to_csv('resultado.csv', index=False)
