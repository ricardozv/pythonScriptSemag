import pandas as pd

# lê a planilha 'Sheet2' do arquivo 'tabela.xlsx'
data = pd.read_excel('tabela.xlsx', sheet_name='Sheet2')

# mostra as primeiras 5 linhas
print(data.head())

