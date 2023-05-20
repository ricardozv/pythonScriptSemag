import csv

def encontrar_valores_faltantes(file_path):
    valores_subt = set()
    valores_subv = set()

    # Lê o arquivo CSV e armazena os valores de "subt" e "subv" em conjuntos
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            valores_subt.add(row['subt'])
            valores_subv.add(row['subv'])

    print(f"Tabela verdade: {len(valores_subt)}")
    print(f"Tabela test: {len(valores_subv)}")
    # Encontra os valores presentes em "subt" e não em "subv"
    valores_faltantes = valores_subv - valores_subt

    return valores_faltantes


# Caminho do arquivo CSV
caminho_arquivo_csv = 'colun.csv'

# Chamada da função para encontrar os valores faltantes
valores_faltantes = encontrar_valores_faltantes(caminho_arquivo_csv)
print(f"Total de Subações não encontradas na tabela verdade: {len(valores_faltantes)}")

# Imprime os valores faltantes
for valor in valores_faltantes:
    print(valor)
