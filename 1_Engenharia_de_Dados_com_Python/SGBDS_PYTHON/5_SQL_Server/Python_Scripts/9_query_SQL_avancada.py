import pandas as pd # type: ignore
import pyodbc # type: ignore

server = 'DESKTOP-1Q56108' # Nome do servidor SQL Server
database = 'Python'        # Nome do banco de dados
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};'f'SERVER={server};'f'DATABASE={database};''Trusted_Connection=yes;')
cursor = conexaoDB.cursor() # criando o cursor de comando para executar as consultas (queries)

query = """
SELECT T1.id as id_vendas,
T1.product_id, T1.total_price,
T2.created_at, T2.situacao,
T3.nome as nome_produto, T4.categoria, T5.first_name as nome_cliente,
T5.email, T5.cell_phone as telefone_cliente, T5.state_brazil
FROM [dbo].[Itens] as T1
LEFT JOIN [dbo].[Ordens] as T2 ON T1.order_id = T2.id
LEFT JOIN [dbo].[Produtos] as T3 ON T3.id = T3.id
LEFT JOIN [dbo].[Categoria] as T4 on T3.id_categoria = T4.ID
LEFT JOIN [dbo].[Clientes] as T5 on T2.customer_id = T5.id
"""

df_query = pd.read_sql(query, conexaoDB)
