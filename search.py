import pandas as pd

# Ler planilha de Excel
tabela = pd.read_excel('tabela.xlsx')

# Lista de palavras a pesquisar
palavras = ['PESSOAL CONTRATADO', 'VIGILÂNCIA', 'TECNOLOGIA DA INFORMAÇÃO', 'LIMPEZA E CONSERVACAO', 'ESTAGIÁRIOS E TRAINEES']

# Filtrar tabela pelas palavras na coluna 'nomeSubacao'
filtro = tabela['subacao'].str.contains('|'.join(palavras), case=False)

# Mostrar resultados
print(tabela.loc[filtro])
