import pandas as pd # type: ignore
def cast_types():
    df = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_csv\Clientes.csv', delimiter=',')

    df['id'] = df['id'].astype(float)

    df['number'] = df['number'].astype(str)

    # Convertendo a colunas created_at para o formato data e hora
    df['created_at'] = pd.to_datetime(df['created_at'])

    # Filtrando um intervalo de tempo e passando para um novo dataframe
    df_filtrado = df[(df['created_at'].dt.year >= 2018) & (df['created_at'].dt.year <= 2020)]

    # Filtrando somente as datas de janeiro de 2018
    df_janeiro_2018 = df[(df['created_at'].dt.year == 2018) & (df['created_at'].dt.month == 1)]

    # Converter a coluna 'created_at' para o formato padrão brasileiro
    df_janeiro_2018['created_at'] = df_janeiro_2018['created_at'].dt.strftime('%d/%m/%Y')

    df_janeiro_2018['created_at'].dtype

    # Transformando a coluna created_at em formato de data
    df['created_at'] = pd.to_datetime(df['created_at'])

    # Transformando a data para o padrão brasileiro
    df['created_at'] = df['created_at'].dt.strftime('%d/%m/%Y %H:%M:%S')

cast_types()
