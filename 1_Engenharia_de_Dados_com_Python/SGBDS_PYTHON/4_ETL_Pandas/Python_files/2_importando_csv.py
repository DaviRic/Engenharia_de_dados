import pandas as pd # type: ignore

df = pd.read_csv(r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_csv\Clientes.csv", delimiter=',')

# Filtrar um item específico de uma coluna
df_estado = df.loc[df['state'] == 'Mato Grosso']
df_estado

# Escolher estados específicos
estados = ['Rio de Janeiro', 'Ceará', 'Rondônia', 'Bahia']
df_estados = df.loc[df['state'].isin(estados)]
df_estados.head(5)

# Substituir os valores NaN. Esse valor quebra na leitura do dataframe
df['street'] = df['street'].fillna('Não registrado')
df['number'] = df['number'].fillna('Sem número')
df['additionals'] = df['additionals'].fillna('Sem informação adicional')
df['email'] = df['email'].fillna('Email não cadastrado')
df['state'] = df['state'].fillna('Estado não informado')

df['state'] = df['state'].replace('São Paulo', 'Sao Paulo')


# Usando variáveis como parâmetro no método replace
valor_atual = 'Amazonas'
valor_substituto = 'AM'

df['state'] = df['state'].replace(valor_atual, valor_substituto)
df.head(3)

# Fazendo a substituição de vários valores ao mesmo tempo
df_lista_estados = {'Paraná': 'PR', 'Rondônia': 'RO', 'Pará': 'PA', 'Minas Gerais': 'MG'}
df['state'] = df['state'].replace(df_lista_estados)


debug_caminho = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Caquinha.xlsx"

df_debug = pd.read_excel(debug_caminho)
df_debug.head()




