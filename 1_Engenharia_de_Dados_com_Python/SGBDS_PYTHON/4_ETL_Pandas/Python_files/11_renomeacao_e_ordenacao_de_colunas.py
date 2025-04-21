import pandas as pd

dados = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Produto.xlsx')
dados.head(3)

# Ordenar em ordem crescente linhas a partir de uma coluna
dados = dados.sort_values(by=['Name'])
dados.head(10)

# O parâmetro ascending serve para indicar se é para ordenar de forma crescente ou decrescente
dados_decrescente = dados.sort_values(by=['ID'], ascending=False)
dados_decrescente.head()
