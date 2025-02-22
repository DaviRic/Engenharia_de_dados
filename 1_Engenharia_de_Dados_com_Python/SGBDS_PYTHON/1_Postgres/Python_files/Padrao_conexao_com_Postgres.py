import psycopg2
dbname   = 'postgres'
user     = 'postgres'
password = 'senha123'
host     = 'localhost'
port     = '5432'


conn = psycopg2.connect(dbname=dbname,
                        user=user,
                        password=password,
                        host=host,
                        port=port)

cur = conn.cursor() # Cria um cursor para ser possível de manipular os dados

# Comandos SQL Transact-sql

conn.commit() # Validar as alterações que foram feitas e subir para o banco de dados

# Fehca o cursor e a conexão
cur.close()
conn.close()



