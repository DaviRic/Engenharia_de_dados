import pandas as pd # type: ignore
import pyodbc # type: ignore

server = 'DESKTOP-1Q56108' # Nome do servidor SQL Server
database = 'Python'        # Nome do banco de dados
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'f'SERVER={server};'f'DATABASE={database};''Trusted_Connection=yes;')
cursor = conexaoDB.cursor() # criando o cursor de comando para executar as consultas (queries)

categoria = pd.read_sql("SELECT * FROM Categoria", conexaoDB)
categoria.head(10)

query = 'SELECT * FROM Categoria'
categoria_df = pd.read_sql(query, conexaoDB)
categoria_df.head(10)

query_clientes = """SELECT * FROM [dbo].[Clientes]
                    WHERE state_brazil in ('Acre', 'Mato Grosso', 'Goiás', 'Maranhão')
                    AND first_name in ('Stephanie', 'Laura', 'Heitor', 'Bruno')"""

clientes_especificos = pd.read_sql(query_clientes, conexaoDB)
clientes_especificos.head(10)

query_ordens = """SELECT * FROM [dbo].[Ordens]"""

ordens = pd.read_sql(query_ordens, conexaoDB)
