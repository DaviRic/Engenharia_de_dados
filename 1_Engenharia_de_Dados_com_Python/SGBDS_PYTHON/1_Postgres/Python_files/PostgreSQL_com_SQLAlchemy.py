import pandas as pd # type: ignore
from sqlalchemy import create_engine, Integer, String, Date, VARCHAR # type: ignore

pd.set_option('display.max_columns', None)
caminho_do_arquivo = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\Postgree\V_OCORRENCIA_AMPLA.json"
df = pd.read_json(caminho_do_arquivo, encoding='utf-8')
df.head(3)

colunas = ["Numero_da_Ocorrencia", "Classificacao_da_Ocorrencia", "Data_da_Ocorrencia", "Municipio", "UF", "Regiao", "Nome_do_Fabricante", "Modelo"]
df = df[colunas]

dbname   = 'python'
user     = 'postgres'
password = 'senha123'
host     = 'localhost'
port     = '5432'

# String de conexão
conexao_str = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

# Cria uma conexão usando o sqlalchemy
engine = create_engine(conexao_str)

nome_tabela = 'anac_sqlalchemy' # Nome da tabela no banco de dados PostgreSQL

# Envia o dataframe para o banco de dados
df.to_sql(nome_tabela, engine, index=False, if_exists='replace', dtype={
                                                                        'Numero_da_Ocorrencia': Integer,
                                                                        'Classificacao_da_Ocorrencia': VARCHAR(50),
                                                                        'Data_da_Ocorrencia': Date
                                                                       })
# replace => sobrescreve toda a tabela
# append => adiciona dados ao fim da tabela

# Fecha a conexão
engine.dispose()


