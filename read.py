import pandas as pd

# Carregar as planilhas
planilha_a = pd.read_excel('terceirizadosr.xlsx')
planilha_b = pd.read_excel('terceirizadost.xlsx')

# Exibir as planilhas
print("Planilha A:")
print(planilha_a)

print("\nPlanilha B:")
print(planilha_b)
