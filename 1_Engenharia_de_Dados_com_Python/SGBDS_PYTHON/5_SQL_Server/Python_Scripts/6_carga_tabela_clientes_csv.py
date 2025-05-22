import pandas as pd # type: ignore
import pyodbc # type: ignore

server = 'DESKTOP-1Q56108' # Nome do servidor SQL Server
database = 'Python'        # Nome do banco de dados
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'f'SERVER={server};'f'DATABASE={database};''Trusted_Connection=yes;')
cursor = conexaoDB.cursor() # criando o cursor de comando para executar as consultas (queries)

dados_clientes = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_csv\Clientes.csv', delimiter=',')

dados_clientes['created_at'] = pd.to_datetime(dados_clientes['created_at'])
dados_clientes['email'] = dados_clientes['email'].fillna('Sem registro')
dados_clientes['street'] = dados_clientes['street'].fillna('Sem info')
dados_clientes['number'] = dados_clientes['number'].fillna('Sem número')
dados_clientes['additionals'] = dados_clientes['additionals'].fillna('Sem info')

cursor.execute('TRUNCATE TABLE [Clientes]')
cursor.commit()

for index, linha in dados_clientes.iterrows():
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

cursor.commit()     # Valida os dados no SQL Server
cursor.close()      # Fecha o cursor
conexaoDB.close()   # Fecha a conexão do SQL Server 
