# 1°: Importar json como DF
import pandas as pd # type: ignore
import psycopg2 # type: ignore

caminho_do_arquivo = r"C:\Users\Usuario\Desktop\Engenharia_de_Dados\1_Engenharia_de_Dados_com_Python\SGBDS_PYTHON\1_Postgres\V_OCORRENCIA_AMPLA.json"
df = pd.read_json(caminho_do_arquivo, encoding='utf-8')

# 2°: Tratar os dados. Levar em considaração apenas as colunas: ["Numero da ocorrencia", "Classificacao da ocorrencia", "Data da ocorrencia", "Municipio", "UF", "Regiao"]
# 3°: Tirando o acento dos nomes das colunas

colunas = ["Numero_da_Ocorrencia", "Classificacao_da_Ocorrencia", "Data_da_Ocorrencia", "Municipio", "UF", "Regiao", "Nome_do_Fabricante"]
df = df[colunas] # Aqui eu tô pegando o meu dataframe e deixando somente com as colunas da variável colunas
# df.rename(columns={'Classificacao_da_Ocorrência': 'Classificacao_da_Ocorrencia'}, inplace=True)

# 4°: Criando banco de dados e tabela "**Foi feito pela interface do postgre**"
# 5°: Configurando a conexão com o Postgre
# 6°: Enviar dados para o Postgre
# 7°: Criar um DELETE da tabela para não ver histórico, mantendo em banco sempre os dados mais recentes

dbname   = 'python'
user     = 'postgres'
password = 'senha123'
host     = 'localhost'
port     = '5432'

# 5°: Conexão com o postgre
conexao = psycopg2.connect(dbname=dbname,
                        user=user,
                        password=password,
                        host=host,
                        port=port)

cursor = conexao.cursor()

# 7°: Deletando a base de dados
cursor.execute("DELETE FROM Anc")

# 6°: Enviar dados para o Postgre
# Carga de dados
for indice, coluna_df in df.iterrows():
    cursor.execute("""
                    INSERT INTO Anc (
                    Numero_da_Ocorrencia,
                    Classificacao_da_ocorrencia,
                    Data_da_ocorrencia,
                    Municipio,
                    UF,
                    Regiao,
                    Nome_do_fabricante
                     ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                        coluna_df["Numero_da_Ocorrencia"],
                        coluna_df["Classificacao_da_Ocorrencia"],
                        coluna_df["Data_da_Ocorrencia"],
                        coluna_df["Municipio"],
                        coluna_df["UF"],
                        coluna_df["Regiao"],
                        coluna_df["Nome_do_Fabricante"]
                     )
                  )
conexao.commit()
cursor.close()
conexao.close()
