import pandas as pd
import json

# lê a planilha 'Sheet2' do arquivo 'tabela.xlsx'
data = pd.read_excel('tabela.xlsx', sheet_name='Sheet2')

# termos de busca
termos = [
    'PESSOAL CONTRATADO',
    'VIGILÂNCIA',
    'TECNOLOGIA DA INFORMAÇÃO',
    'LIMPEZA E CONSERVACAO',
    'ESTAGIÁRIOS E TRAINEES',
    'SERVIÇOS DE INFORMÁTICA',
]

# aplica o filtro em todas as células do DataFrame
filtro = data.applymap(lambda x: any([t in str(x) for t in termos]))

# encontra as linhas que contêm pelo menos uma ocorrência de qualquer um dos termos
linhas = filtro.any(axis=1)

# filtra o DataFrame usando as linhas encontradas
resultado = data[linhas]

# mostra o resultado no terminal
print(resultado)

# converte o resultado para um dicionário e salva em um arquivo JSON
resultado_dict = resultado.to_dict(orient='records')
with open('resultado.json', 'w', encoding='utf-8') as f:
    json.dump(resultado_dict, f, ensure_ascii=False, indent=4)
