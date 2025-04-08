import pandas as pd # type: ignore

def read_multiple_tabas_excel():
    # Extração padrão
    df = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Caquinha.xlsx')

    # Extração selecionando no excel a guia desejada (sheet_name = nome_da_guia)
    df_produtos = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Caquinha.xlsx', sheet_name='Planilha2')

    # Extração de dados selecionando uma guia específica e pulando uma quantidade específica de linhas
    # sheet_name = nome_da_guia; skiprows = quantidade_de_linhas_para_pular
    tabela_produtos = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Caquinha.xlsx', sheet_name='Planilha2', skiprows=3)

    # Escolhendo colunas específicas (usecols)
    tabela_vendas_pessoas = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Caquinha.xlsx', sheet_name='Planilha3', usecols='A:B')

    tabela_locais_vendas = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Caquinha.xlsx', sheet_name='Planilha3', usecols='F:G')

    # Escolhendo colunas específicas usando listas (usecols = [0,3])
    tabela_pessoas_lista = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Caquinha.xlsx', sheet_name='Planilha3', usecols=[0,1])

    tabela_locais_lista = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Caquinha.xlsx', sheet_name='Planilha3', usecols=[5,6])

    # Tabela no meio da planilha
    planilha_4 = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Caquinha.xlsx', sheet_name='Planilha4', usecols='G:H', skiprows=7)

    # Uma tabela embaixo da outra
    # skiprows -> pula uma quantidade de linhas indicada
    # nows -> usa a quantidade de linhas indicadas
    vendedor_vendas = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Caquinha.xlsx', sheet_name='Planilha5', nrows=12)

    loja_vendas = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Caquinha.xlsx', sheet_name='Planilha5', skiprows=13)

read_multiple_tabas_excel()