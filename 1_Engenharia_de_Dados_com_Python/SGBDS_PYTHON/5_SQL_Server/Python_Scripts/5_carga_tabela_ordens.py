
import pandas as pd # type: ignore
import pyodbc # type: ignore

server = 'DESKTOP-1Q56108' # Nome do servidor SQL Server
database = 'Python'        # Nome do banco de dados
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'f'SERVER={server};'f'DATABASE={database};''Trusted_Connection=yes;')
cursor = conexaoDB.cursor() # criando o cursor de comando para executar as consultas (queries)

dados_ordens = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Ordens.xlsx')
# dados_itens.head()

cursor.execute('DELETE FROM [Itens]')
cursor.commit()

dados_ordens['created_at'] = pd.to_datetime(dados_ordens['created_at'])
dados_ordens.head(5)

for index, linha in dados_ordens.iterrows():
    # Insere os dados nas colunas
    cursor.execute("INSERT INTO [Ordens](id, created_at, customer_id, situacao) values(?, ?, ?, ?)", linha.id, linha.created_at, linha.customer_id, linha.status)

cursor.commit()     # Valida os dados no SQL Server
cursor.close()      # Fecha o cursor
conexaoDB.close()   # Fecha a conexão do SQL Server






