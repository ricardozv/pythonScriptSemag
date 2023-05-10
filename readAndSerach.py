import pandas as pd

# carrega o arquivo Excel
df = pd.read_excel('seuarquivo.xlsx')

# define os termos de busca
termos = [
    'PESSOAL CONTRATADO',
    'VIGILÂNCIA',
    'TECNOLOGIA DA INFORMAÇÃO',
    'LIMPEZA E CONSERVACAO',
    'PESSOAL CONTRATADO - SERVIÇOS DE INFORMÁTICA',
    'ESTAGIÁRIOS E TRAINEES'
]

# cria uma lista vazia para armazenar os resultados da busca
resultados = []

# itera sobre todas as colunas do DataFrame
for coluna in df.columns:
    # verifica se a coluna é do tipo object (string)
    if df[coluna].dtype == 'object':
        # filtra as linhas que contêm os termos de busca na coluna atual
        filtro = df[coluna].str.contains('|'.join(termos))
        # se o filtro encontrar algum resultado, adiciona o nome da coluna na lista de resultados
        if filtro.any():
            resultados.append(coluna)

# exibe os resultados
print('Os termos de busca foram encontrados nas seguintes colunas:')
for coluna in resultados:
    print(coluna)
