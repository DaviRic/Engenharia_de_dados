import pandas as pd # type: ignore

def rename_reorder_data(dados):

    # Renomeando as colunas do DataFrame
    dados = dados.rename(columns={'Name':'Full_Name'})

    # Renomeando as colunas usando variável
    colunas = {'Full_Name':'Name', 'ID':'Id'}
    dados = dados.rename(columns=colunas)
    return dados

dados = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Produto.xlsx') 
dataframe = rename_reorder_data(dados)


