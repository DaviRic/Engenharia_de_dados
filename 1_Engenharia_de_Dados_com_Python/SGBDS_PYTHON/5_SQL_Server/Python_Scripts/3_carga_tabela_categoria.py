import pandas as pd # type: ignore
import pyodbc # type: ignore

server = 'DESKTOP-1Q56108' # Nome do servidor SQL Server
database = 'Python'        # Nome do banco de dados
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'f'SERVER={server};'f'DATABASE={database};''Trusted_Connection=yes;')
cursor = conexaoDB.cursor() # criando o cursor de comando para executar as consultas (queries)

dados_categoria = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Categoria.xlsx')
# dados_categoria.head()

cursor.execute('DELETE FROM [Categoria]')
cursor.commit()

dados_categoria.head(5)

for index, linha in dados_categoria.iterrows():
    # Insere os dados nas colunas
    cursor.execute("INSERT INTO [Categoria](ID, categoria) values(?, ?)", linha.id, linha.nome)

cursor.commit()     # Valida os dados no SQL Server
cursor.close()      # Fecha o cursor
conexaoDB.close()   # Fecha a conexão do SQL Server




