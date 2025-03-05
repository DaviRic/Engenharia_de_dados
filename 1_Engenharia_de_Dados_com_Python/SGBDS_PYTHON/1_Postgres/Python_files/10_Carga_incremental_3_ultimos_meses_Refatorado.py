import pandas as pd # type: ignore
from sqlalchemy import create_engine, Integer, String, Date, VARCHAR, text # type: ignore
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta # type: ignore

pd.set_option('display.max_columns', None)
caminho_do_arquivo = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\Postgree\V_OCORRENCIA_AMPLA.json"
df = pd.read_json(caminho_do_arquivo, encoding='utf-8')
colunas = ["Numero_da_Ocorrencia", "Classificacao_da_Ocorrencia", "Data_da_Ocorrencia", "Municipio", "UF", "Regiao", "Nome_do_Fabricante", "Modelo"]
df = df[colunas]


# Método 1: Não leva em consideração a variação nos númerosde dias em casa mês, resultando em uma aproximação
data_atual = datetime.now()
data_ha_3_meses = data_atual - timedelta(days=90)
data_ha_3_meses_apenas_data = data_ha_3_meses.date()

print(data_ha_3_meses_apenas_data)


# Método 2: leva em consideração a variação nos números de dias em cada mês, fornecendo um resultado mais preciso
data_atual_2 = datetime.now()
d_menos_3m = data_atual_2 - relativedelta(months=3)
dt_d_menos3m = d_menos_3m.date()

print(dt_d_menos3m)

df['Data_da_Ocorrencia'] = pd.to_datetime(df['Data_da_Ocorrencia'])
data_ha_3_meses_apenas_data = pd.to_datetime(data_ha_3_meses_apenas_data)
dt_d_menos3m = pd.to_datetime(dt_d_menos3m)

df = df[df['Data_da_Ocorrencia'] >= dt_d_menos3m]

dt_d_menos3m = dt_d_menos3m.date()
print(dt_d_menos3m)


# Definições das variáveis para conectar com os bancos de dados
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
delete = text(f'''
              DELETE FROM {nome_tabela}
              WHERE "Data_da_Ocorrencia" >= '{dt_d_menos3m}'
              ''')

cursor.execute(delete)
cursor.commit()

df.to_sql(nome_tabela, engine, index=False, if_exists='append',
          dtype={'Numero_da_Ocorrencia' : Integer,
              'Classificacao_da_Ocorrencia' : VARCHAR(50),
              'Data_da_Ocorrencia' : Date
            })

engine.dispose()
cursor.close()




