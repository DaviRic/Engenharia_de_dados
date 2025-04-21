import pandas as pd # type: ignore

dados = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Produto.xlsx')

# Ordenar em ordem crescente linhas a partir de uma coluna
dados = dados.sort_values(by=['Name'])

# O parâmetro ascending serve para indicar se é para ordenar de forma crescente ou decrescente
dados_decrescente = dados.sort_values(by=['ID'], ascending=False)
