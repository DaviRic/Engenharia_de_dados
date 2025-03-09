import pandas as pd # type: ignore

# Leitura de arquivo json
pasta_origem_json = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\Destino\Anac_json.json"
df_json = pd.read_json(pasta_origem_json, orient='index')

# Leitura de arquivo excel
pasta_origem_excel = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\Destino\Anac_excel.xlsx"
df_excel = pd.read_excel(pasta_origem_excel)

# sheet_name => carrega uma guia específica do arquivo csv. É só passar o nome da guia entre áspas

# Leitura de arquivo csv
pasta_origem_csv = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\Destino\Anac_csv.csv"
df_csv = pd.read_csv(pasta_origem_csv, sep=',')
df_csv.head()

# Leitura de arquivo parquet
pasta_origem_parquet = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\Destino\Anac_parquet.parquet"
df_parquet = pd.read_parquet(pasta_origem_parquet)
pasta_origem_parquet_particionado = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\Destino\Anac_particionado.parquet"
df_particionado = pd.read_parquet(pasta_origem_parquet_particionado, engine='fastparquet')
