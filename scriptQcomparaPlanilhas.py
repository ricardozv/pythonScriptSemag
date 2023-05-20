import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('caminho/do/arquivo.xlsx')

economias_anuais = df.groupby('Órgão')['Valor anual da Economia'].sum()

economias_anuais.plot(kind='bar')
plt.ylabel('Valor da economia anual (R$)')
plt.show()
