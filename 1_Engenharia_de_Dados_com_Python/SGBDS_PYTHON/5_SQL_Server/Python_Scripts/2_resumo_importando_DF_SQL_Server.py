import pandas as pd # type: ignore
import pyodbc # type: ignore

server = 'DESKTOP-1Q56108' # Nome do servidor SQL Server
database = 'Python'        # Nome do banco de dados
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'f'SERVER={server};'f'DATABASE={database};''Trusted_Connection=yes;')
cursor = conexaoDB.cursor() # criando o cursor de comando para executar as consultas (queries)

dados = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Produto.xlsx')

cursor.execute('DELETE FROM [Produtos]')
cursor.commit()

# %%
for index, linha in dados.iterrows():
    # Insere os dados nas colunas              # Banco de dados                                    # DataFrame
    cursor.execute("INSERT INTO [Produtos](id, nome, preco, id_categoria) values(?, ?, ?, ?)",
                   linha.ID, linha.Name, linha.Price, linha.Id_Category)

cursor.commit()     # Valida os dados no SQL Server
cursor.close()      # Fecha o cursor
conexaoDB.close()   # Fecha a conexão do SQL Server


