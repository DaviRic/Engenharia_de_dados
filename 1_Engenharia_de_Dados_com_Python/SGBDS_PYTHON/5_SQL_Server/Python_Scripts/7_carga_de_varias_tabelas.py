import pandas as pd # type: ignore
import pyodbc # type: ignore

server = 'DESKTOP-1Q56108' # Nome do servidor SQL Server
database = 'Python'        # Nome do banco de dados
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'f'SERVER={server};'f'DATABASE={database};''Trusted_Connection=yes;')
cursor = conexaoDB.cursor() # criando o cursor de comando para executar as consultas (queries)

Produtos = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Produto.xlsx')
Categoria = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Categoria.xlsx')
Itens = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\items.xlsx')
Ordens = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Ordens.xlsx')
Clientes = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_csv\Clientes.csv')

cursor.execute("""
TRUNCATE TABLE [dbo].[Categoria];
TRUNCATE TABLE [dbo].[Ordens];
TRUNCATE TABLE [dbo].[Itens];
TRUNCATE TABLE [dbo].[Produtos];
TRUNCATE TABLE [dbo].[Clientes];
""")
cursor.commit() # Validar os dados do SQL Server para não bloquear o usuário

for index, linha in Produtos.iterrows():
    cursor.execute("INSERT INTO [Produtos](id, nome, preco, id_categoria) values (?, ?, ?, ?)",
                    linha.ID, linha.Name, linha.Price, linha.Id_Category)

cursor.commit()

for index, linha in Categoria.iterrows():
    # Insere os dados nas colunas
    cursor.execute("INSERT INTO [Categoria](ID, categoria) values(?, ?)", linha.id, linha.nome)

cursor.commit()   

Itens['total_price'] = Itens['total_price'].astype(float)

for index, linha in Itens.iterrows():
    # Insere os dados nas colunas
    cursor.execute("INSERT INTO [Itens](id, order_id, product_id, quantity, total_price) values(?, ?, ?, ?, ?)",
                   linha.id, linha.order_id, linha.product_id, linha.quantity, linha.total_price)

cursor.commit()  

Ordens['created_at'] = pd.to_datetime(Ordens['created_at'])

for index, linha in Ordens.iterrows():
    # Insere os dados nas colunas
    cursor.execute("INSERT INTO [Ordens](id, created_at, customer_id, situacao) values(?, ?, ?, ?)",
                   linha.id, linha.created_at, linha.customer_id, linha.status)
cursor.commit()


Clientes['created_at'] = pd.to_datetime(Clientes['created_at'])
Clientes['email'] = Clientes['email'].fillna('Sem registro')
Clientes['street'] = Clientes['street'].fillna('Sem info')
Clientes['number'] = Clientes['number'].fillna('Sem número')
Clientes['additionals'] = Clientes['additionals'].fillna('Sem info')

for index, linha in Clientes.iterrows():
    # Converter para o tipo str antes da inserção. É necessário fazer isso por conta dos caracteres especiais, 
    # No SQL Server é um pouco mais chato quando há caracteres especiais
    linha.email = str(linha.email)
    linha.state = str(linha.state)
    linha.street = str(linha.street)
    linha.number = str(linha.number)
    linha.additionals = str(linha.additionals)

    # Insere os dados nas colunas
    cursor.execute("INSERT INTO [Clientes](id, created_at, first_name, last_name, email, cell_phone, country, state_brazil,"
                   "street, number, additionals)values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   linha.id, linha.created_at, linha.first_name, linha.last_name, linha.email, linha.cell_phone,
                   linha.country, linha.state, linha.street, linha.number, linha.additionals)

cursor.commit()

# Fecha o cursor e a minha conexão com o banco de dados
cursor.close()
conexaoDB.close()
