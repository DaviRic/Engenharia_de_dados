
import pandas as pd # type: ignore
import pyodbc # type: ignore

server = 'DESKTOP-1Q56108' # Nome do servidor SQL Server
database = 'Python'        # Nome do banco de dados
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'f'SERVER={server};'f'DATABASE={database};''Trusted_Connection=yes;')
cursor = conexaoDB.cursor() # criando o cursor de comando para executar as consultas (queries)


dados_itens = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\items.xlsx')
# dados_itens.head()

cursor.execute('DELETE FROM [Itens]')
cursor.commit()

dados_itens['total_price'] = dados_itens['total_price'].astype(float)
# dados_itens.head(5)

for index, linha in dados_itens.iterrows():
    # Insere os dados nas colunas
    cursor.execute("INSERT INTO [Itens](id, order_id, product_id, quantity, total_price) values(?, ?, ?, ?, ?)", linha.id, linha.order_id, linha.product_id, linha.quantity, linha.total_price)

cursor.commit()     # Valida os dados no SQL Server
cursor.close()      # Fecha o cursor
conexaoDB.close()   # Fecha a conexão do SQL Server


