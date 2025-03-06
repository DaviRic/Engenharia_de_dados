import psycopg2 # type: ignore
import pandas as pd # type: ignore
from sqlalchemy import create_engine # type: ignore

# Definições das variáveis para conectar com os bancos de dados
dbname   = 'python'
user     = 'postgres'
password = 'senha123'
host     = 'localhost'
port     = '5432'

# 5°: Conexão com o postgre
conexao = psycopg2.connect(dbname=dbname,
                        user=user,
                        password=password,
                        host=host,
                        port=port)

query = "SELECT id, dt_ocorrencia, uf, regiao, classificacao_da_ocorrencia FROM anac_mapeamento"

df = pd.read_sql_query(query, conexao)

conexao_str = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
query_2 = "SELECT id, dt_ocorrencia, uf FROM anac_mapeamento"

df_2 = pd.read_sql_query(query_2, conexao_str)
