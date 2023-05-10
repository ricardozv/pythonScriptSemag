import pandas as pd

# ler a tabela em um DataFrame do pandas
tabela = pd.read_excel('tabela.xlsx')

# pedir ao usuário o código e o nome da subação para filtrar
codigo = input('Digite o código da subação: ')
nome = input('Digite o nome da subação: ')

# criar um filtro com base no código e nome da subação
filtro = (tabela['codSubacao'] == int(codigo)) & (tabela['nomeSubacao'] == nome)

# aplicar o filtro na tabela e imprimir o resultado
resultado = tabela.loc[filtro]
print(resultado)

