import pandas as pd # type: ignore


df = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_csv\Clientes.csv', delimiter=',')


for coluna in df.columns:
    print(f'Coluna {coluna} é do tipo: {df[coluna].dtype}')


for coluna in df.columns:
    print(f'Colunha {coluna} tem é do tipo {df[coluna].dtypes}')


df['id'] = df['id'].astype(float)


print(df['id'].dtype)


df['number'] = df['number'].astype(str)


print(df['number'].dtype)


# #### Conversão de Datas


df = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_csv\Clientes.csv', delimiter=',')
df


print(df['created_at'].dtypes)


# Convertendo a colunas created_at para o formato data e hora
df['created_at'] = pd.to_datetime(df['created_at'])


# Filtrando um intervalo de tempo e passando para um novo dataframe
df_filtrado = df[(df['created_at'].dt.year >= 2018) & (df['created_at'].dt.year <= 2020)]



# Filtrando somente as datas de janeiro de 2018
df_janeiro_2018 = df[(df['created_at'].dt.year == 2018) & (df['created_at'].dt.month == 1)]
df_janeiro_2018.head(3)


# Converter a coluna 'created_at' para o formato padrão brasileiro
df_janeiro_2018['created_at'] = df_janeiro_2018['created_at'].dt.strftime('%d/%m/%Y')


df_janeiro_2018['created_at'].dtype


# #### Converter para o padrão BR no primeiro comando


df = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_csv\Clientes.csv', delimiter=',')

# Transformando a coluna created_at em formato de data
df['created_at'] = pd.to_datetime(df['created_at'])

# Transformando a data para o padrão brasileiro
df['created_at'] = df['created_at'].dt.strftime('%d/%m/%Y %H:%M:%S')
df





