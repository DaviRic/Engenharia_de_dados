import pandas as pd # type: ignore

dados = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Produto.xlsx')

# Renomeando as colunas do DataFrame
dados = dados.rename(columns={'Name':'Full_Name'})
dados.head(1)

# Renomeando as colunas usando variável
colunas = {'Full_Name':'Name', 'ID':'Id'}
dados = dados.rename(columns=colunas)
dados.head(1)




