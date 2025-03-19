from sqlalchemy import create_engine, INTEGER, String, DATE, VARCHAR # type: ignore
import pandas as pd # type: ignore

# Passando os dados da origem de dados para um dataframes
df_customers = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\Arquivo_meu\Origem_de_dados\Bike\customers.csv').fillna('')
df_customers.head()

# Enviar dataframe para o MySQL
# df_customers.to_sql(name='teste', con=conn, if_exists='append', index=False)

# ----- Parâmetros -----
# name -> tabelas de destino;
# con -> conexão;
# if_exists -> Se já existir a tabela no meu banco de dados o que fazer? replace: substitui toda a tabela
#              append: insere dados na última linha;
# index -> o índice do DF padrão é True (leva o índice para a tabela) false (Não leva o índice do Python)
#          para a tabela.
# conn.close() e eng.dispose() -> fecha as conexões (sempre usar)

# Adicionando ao final da tabela mesmo que os dados já existam
eng = create_engine('mysql+mysqldb://root:senha123@localhost/python')
conn = eng.connect()

tabela_destino = 'clientes_teste'

# Pegando o dataframe e enviando para o banco de dados. Enviando os dados do dataframe para o banco de dados
df_customers.to_sql(name=tabela_destino, con=conn, if_exists='append', index=False)


# Usando o replace, ele só reescreve o dado que já existe ao invés de adicionar ao final
eng = create_engine('mysql+mysqldb://root:senha123@localhost/python')
conn = eng.connect()

tabela_destino = 'clientes_teste_replace'

# Pegando o dataframe e enviando para o banco de dados. Enviando os dados do dataframe para o banco de dados
df_customers.to_sql(name=tabela_destino, con=conn, if_exists='replace', index=False)



'''
Mapeando colunas usando dicionário

Parâmetro no MySQL = dtype

Criar um dicionário com os tipos de dados e atribuir no parâmetro dtype

'''

# Usando o replace, ele só reescreve o dado que já existe ao invés de adicionar ao final
eng = create_engine('mysql+mysqldb://root:senha123@localhost/python')
conn = eng.connect()

tabela_destino = 'clientes_schema'
tipo_da_coluna = {
    'customer_id' : INTEGER,
    'first_name'  : VARCHAR(50),
    'last_name'   : String(50)
    }


# Pegando o dataframe e enviando para o banco de dados. Enviando os dados do dataframe para o banco de dados
df_customers.to_sql(name=tabela_destino, con=conn, if_exists='replace', dtype=tipo_da_coluna, index=False)


conn.close()
eng.dispose()
