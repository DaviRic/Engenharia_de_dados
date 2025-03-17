
# sqlalchemy - MySQL
# https://docs.sqlalchemy.org/en/20/dialects/mysql.html#create-table-arguments-including-storage-engines
# Tipos diferentes de conectores
# mysqlconnector - pip install mysql-connector-python
# pymysql - pip install pymysql
# mysqldb - pip install MySQL-python ou pip install mysqlclient

import pandas as pd # type: ignore
from sqlalchemy import create_engine, text # type: ignore

# Conexão com o banco de dados (-----> COM ERRO <-----)

eng = create_engine('mysql+pymysql://root:senha123@localhost/python')

conn = eng.connect()

query = 'SELECT * FROM python.categories'
resultado = conn.execute(query)

# Printar linhas
for row in resultado:
    print(row)


conn.close()
eng.dispose() # Libera todos os recursos associados ao objeto eng (o mecanismo sqlAlchemy),
              # incluindo todas as conexões abertas e quaisquer outros recursos mantidos por ele

# Resolvendo erro da célula anterior. SQLAlchemy não sabe como executa a string. Resolve colocando a query entre ()
# Conexão com o banco de dados

eng = create_engine('mysql+pymysql://root:senha123@localhost/python')

conn = eng.connect()

query = text('SELECT * FROM python.customers')
resultado = conn.execute(query)

# Printar linhas
for row in resultado:
    print(row)

conn.close()
eng.dispose() # Libera todos os recursos associados ao objeto eng (o mecanismo sqlAlchemy),
              # incluindo todas as conexões abertas e quaisquer outros recursos mantidos por ele

# Conexão com o banco de dados
eng = create_engine('mysql+pymysql://root:senha123@localhost/python')

conn = eng.connect()

query = text('SELECT * FROM python.customers')
df_customers = pd.read_sql(query, conn)

conn.close()
eng.dispose()

# Tipos diferentes de conectores
# mysqlconnector - pip install mysql-connector-python
# pymysql - pip install pymysql
# mysqldb - pip install MySQL-python ou pip install mysqlclient


# Conexão com o banco de dados
eng = create_engine('mysql+mysqlconnector://root:senha123@localhost/python')
conn = eng.connect()

query = text('SELECT * FROM python.customers')
df_customers = pd.read_sql(query, conn)

conn.close()
eng.dispose()
