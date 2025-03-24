# Migrando dados do banco de dados do Postgres para o MySQL
from sqlalchemy import create_engine, INTEGER, VARCHAR # type: ignore
import pandas as pd # type: ignore

# Conexão com a origem (Postgres)
eng_postgres = create_engine('postgresql://postgres:senha123@localhost:5432/python')

# Conexão de destino (MySQL)
eng_mysql = create_engine('mysql+mysqldb://root:senha123@localhost/python')

query = "SELECT * FROM python.customers"

df = pd.read_sql_query(query, eng_mysql) # Transforma a query em DataFrame

# Levando os dados para o destino
tabela_destino = 'clientes_origem_MySQL'

tipo_da_coluna = { # Inferindo os tipos de dados
        'customer_id':INTEGER,
        'first_name':VARCHAR(50),
        'last_name':VARCHAR(50),
        'phone':VARCHAR(30),
        'email':VARCHAR(50),
        'street':VARCHAR(100),
        'city':VARCHAR(50),
        'state':VARCHAR(20),
        'zip_code':VARCHAR(20)
    }

# Carga de dados
# Pegando o dataframe e enviando para o banco de dados. Enviando os dados do dataframe para o banco de dados
df.to_sql(name=tabela_destino, con=eng_postgres, if_exists='replace', dtype=tipo_da_coluna, index=False)

eng_mysql.dispose()
eng_postgres.dispose()


