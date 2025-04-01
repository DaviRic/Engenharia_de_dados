
import pandas as pd # type: ignore
import os


vendas_2021 = pd.read_excel(r"")
vendas_2022 = pd.read_excel(r"")
vendas_2023 = pd.read_excel(r"")


diretorio = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivo_leitura_varios"

# Variável que vai armazenar os dados dos arquivos .xlsx
dados = []

# Itera sobre os arquivos .xlsx presentes no diretório
for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.xlsx'):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        df = pd.read_excel(caminho_arquivo)
        dados.append(df)

consolidado = pd.concat(dados)
# consolidado.head()



pasta_destino = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivo_consolidado\\"

nome_arquivo = "union_files_delete.xlsx"

caminho_completo = pasta_destino + nome_arquivo

if os.path.exists(caminho_completo):
    os.remove(caminho_completo)

consolidado.to_excel(caminho_completo, index=False)





