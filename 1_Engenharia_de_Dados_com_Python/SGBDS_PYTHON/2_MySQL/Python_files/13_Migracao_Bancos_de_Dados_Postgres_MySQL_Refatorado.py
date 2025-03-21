# Migrando dados do banco de dados do Postgres para o MySQL
from sqlalchemy import create_engine, INTEGER, DATE, DATETIME, VARCHAR, String
import pandas as pd

# Conexão com a origem (Postgres)
eng_postgres = create_engine('postgresql://postgres:senha123@localhost:5432/python')

# Conexão de destino (MySQL)
eng_mysql = create_engine('mysql+mysqldb://root:senha123@localhost/python')

query = "SELECT id, dt_ocorrencia, uf, regiao, classificacao_da_ocorrencia FROM anac_mapeamento"

df = pd.read_sql_query(query, eng_postgres) # Transforma a query em DataFrame


# Levando os dados para o destino
tabela_destino = 'anac_origem_postgres'

tipo_da_coluna = { # Inferindo os tipos de dados
        'id':INTEGER,
        'dt_ocorrencia':DATE,
        'uf':VARCHAR(15),
        'regiao':VARCHAR(15),
        'classificacao_da_ocorrencia':VARCHAR(15)
    }

# Carga de dados
# Pegando o dataframe e enviando para o banco de dados. Enviando os dados do dataframe para o banco de dados
df.to_sql(name=tabela_destino, con=eng_mysql, if_exists='replace', dtype=tipo_da_coluna, index=False)

eng_mysql.dispose()
eng_postgres.dispose()
