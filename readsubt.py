import pandas as pd

# Carregar a planilha A
planilha_a = pd.read_excel('terceirizadost.xlsx')

# Ler apenas a coluna "subt" da planilha A
coluna_subt = planilha_a['subt']

# Exibir a coluna "subt"
print("Coluna subt da planilha A:")
print(coluna_subt)
