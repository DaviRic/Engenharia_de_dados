import pandas as pd # type: ignore
import os

diretorio = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel"

# Variável que vai armazenar os dados dos arquivos .xlsx
dados = []

# Itera sobre os arquivos .xlsx presentes no diretório
for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.xlsx'):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        df = pd.read_excel(caminho_arquivo)
        dados.append(df)

consolidado = pd.concat(dados)
consolidado
