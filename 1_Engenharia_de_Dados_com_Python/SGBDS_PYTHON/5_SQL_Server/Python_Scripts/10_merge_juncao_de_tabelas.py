import pandas as pd # type: ignore
import pyodbc # type: ignore

server = 'DESKTOP-1Q56108' # Nome do servidor SQL Server
database = 'Python'        # Nome do banco de dados
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};'f'SERVER={server};'f'DATABASE={database};''Trusted_Connection=yes;')
cursor = conexaoDB.cursor() # criando o cursor de comando para executar as consultas (queries)

Produtos = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Produto.xlsx')
Categoria = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Categoria.xlsx')
Itens = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\items.xlsx')
Ordens = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Ordens.xlsx')
Clientes = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_csv\Clientes.csv', delimiter=',')

T1 = pd.merge(Ordens, Clientes, left_on="customer_id", right_on="id", how="left")

# Left join -> faz um join entre a tabela da esquerda e a tabela da direita conservando todos os dados da tabela da esquerda
# Right join -> faz um join entre a tabela da esquerda e a tabela da direita conservando todos os dados da tabela da direita
# Inner -> retorna os dados apenas quando as duas tabelas tem chaves correspondentes
# Outer -> retorna todos os registros das duas tabelas

T1 = T1[["id_x", "created_at_x", "first_name", "cell_phone", "state"]]

T2 = pd.merge(Itens, Produtos, left_on="product_id", right_on="ID", how="left")

# Escolhi só as colunas que me importam
T2 = T2[["id", "Name", "Id_Category"]]

categoria_prod = pd.merge(T2, Categoria, left_on="Id_Category", right_on="id", how="left")

categoria_prod = categoria_prod[["id_x", "Name", "Id_Category", "nome"]]
