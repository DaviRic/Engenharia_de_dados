import pandas as pd # type: ignore
from datetime import datetime
from sqlalchemy import create_engine, Integer, String, Date, VARCHAR, text # type: ignore

pd.set_option('display.max_columns', None)
caminho_do_arquivo = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\Postgree\V_OCORRENCIA_AMPLA.json"
df = pd.read_json(caminho_do_arquivo, encoding='utf-8')

colunas = ["Numero_da_Ocorrencia", "Classificacao_da_Ocorrencia", "Data_da_Ocorrencia", "Municipio", "UF", "Regiao", "Nome_do_Fabricante", "Modelo"]
df = df[colunas]

df["Data_da_Ocorrencia"] = pd.to_datetime(df["Data_da_Ocorrencia"])


ano_atual = datetime.now().year

df = df[df["Data_da_Ocorrencia"].dt.year == ano_atual]

dbname   = 'python'
user     = 'postgres'
password = 'senha123'
host     = 'localhost'
port     = '5432'

conexao_str = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

engine = create_engine(conexao_str)
nome_tabela = 'anac_sqlalchemy'

# Deletar registros com base no ano atual
cursor = engine.connect()
delete = text(f'DELETE FROM {nome_tabela} WHERE EXTRACT (YEAR FROM "Data_da_Ocorrencia") = {ano_atual}')
cursor.execute(delete)
cursor.commit

df.to_sql(nome_tabela, engine, index=False, if_exists='append',
          dtype={'Numero_da_Ocorrencia' : Integer,
              'Classificacao_da_Ocorrencia' : VARCHAR(50),
              'Data_da_Ocorrencia' : Date
            })
engine.dispose()
cursor.close()
