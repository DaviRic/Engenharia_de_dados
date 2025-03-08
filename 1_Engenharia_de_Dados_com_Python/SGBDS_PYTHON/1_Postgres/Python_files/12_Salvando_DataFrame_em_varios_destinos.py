from sqlalchemy import create_engine # type: ignore
import pandas as pd # type: ignore

dbname   = 'python'
user     = 'postgres'
password = 'senha123'
host     = 'localhost'
port     = '5432'

# 5°: Conexão com o postgre
conexao = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
engine = create_engine(conexao)
query = "SELECT id, dt_ocorrencia, uf, regiao, classificacao_da_ocorrencia FROM anac_mapeamento"

df = pd.read_sql_query(query, conexao)

# Formato json
pasta_destino_json = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\Destino\Anac_json.json"
df.to_json(pasta_destino_json, orient="index")
# orient -> orientação do formato
# O parâmetro orient="records" aceita que coloque mais um parâmetro, o lines que pode ser True ou False
# lines=True -> É separado por quebra de linhas
# Obs.: Tipos de orientação: records, index, columns, values, table

# Formato excel
pasta_destino_excel = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\Destino\Anac_excel.xlsx"
df.to_excel(pasta_destino_excel, index=False, sheet_name="Base")
# sheet_name -> guia da planilha
# index -> índice do python

# Formato CSV
pasta_destino_csv = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\Destino\Anac_csv.csv"
df.to_csv(pasta_destino_csv, sep=',')

# Formato parquet
pasta_destino_parquet = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\Destino\Anac_paquet.parquet"
df.to_parquet(pasta_destino_parquet, index=False, engine='pyarrow')

pasta_destino_particionado = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\Destino\Anac_particionado.parquet"
colunas_particionamento = ['regiao']
df.to_parquet(pasta_destino_particionado, index=False,
              partition_cols=colunas_particionamento,
              engine='pyarrow')


