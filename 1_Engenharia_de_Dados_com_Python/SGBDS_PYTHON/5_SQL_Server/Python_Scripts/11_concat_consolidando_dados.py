# %%
import pandas as pd
import os

vendas_2021 = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\5_SQL_Server\arquivos_excel\Vendas2021.xlsx')
vendas_2022 = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\5_SQL_Server\arquivos_excel\Vendas2022.xlsx')
vendas_2023 = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\5_SQL_Server\arquivos_excel\Vendas2023.xlsx')

# %%
# arquivos_consolidados = pd.concat([vendas_2021, vendas_2022, vendas_2023])
# arquivos_consolidados = pd.concat([vendas_2021, vendas_2022, vendas_2023], ignore_index=True) # Não cria índice ao criar o novo dataframe
arquivos_consolidados = pd.concat([vendas_2021, vendas_2022, vendas_2023], keys=["2021", "2022", "2023"]) # Cria uma nova coluna onde é identificado os dados de cada tabela

# %%
arquivos_consolidados.head(60)

# %%
# Caminho para pasta onde será salvo o arquivo Excel
pasta_destino = r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\5_SQL_Server\arquivos_excel\concat_vendas\\'

# Nome do arquivo
nome_arquivo = 'VendasConcat.xlsx'

# Lista para armazenar os dados dos arquivos
dados = []

# Caminho completo do arquivo Excel
caminho_completo = pasta_destino + nome_arquivo

if os.path.exists(caminho_completo): # Se não existir, o arquivo será criado
    # Carregar o arquivo Excel consolidade existente em um dataframe
    df_existente = pd.read_excel(caminho_completo)
    # Adiciona os dados existentes no dataframe. Se existir, ele adiciona no final dataframe
    dados.append(df_existente)


arquivos_consolidados.to_excel(caminho_completo, index=False)

# %% [markdown]
# #### Nome dos arquivos no dataframe ( Criando no dataframe uma coluna que especifica o nome do arquivo daquele dado)

# %%
vendas_2021 = r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\5_SQL_Server\arquivos_excel\Vendas2021.xlsx'
vendas_2022 = r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\5_SQL_Server\arquivos_excel\Vendas2022.xlsx'
vendas_2023 = r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\5_SQL_Server\arquivos_excel\Vendas2023.xlsx'

# %%
df_2021 = pd.read_excel(vendas_2021)
df_2022 = pd.read_excel(vendas_2022)
df_2023 = pd.read_excel(vendas_2023)

# %%
# Criando no dataframe uma coluna que especifica o caminho do arquivo daquele dado

nome_arquivo_2021 = os.path.splitext(os.path.basename(vendas_2021))[0]
nome_arquivo_2022 = os.path.splitext(os.path.basename(vendas_2022))[0]
nome_arquivo_2023 = os.path.splitext(os.path.basename(vendas_2023))[0]

df_2021['nome_do_arquivo'] = nome_arquivo_2021
df_2022['nome_do_arquivo'] = nome_arquivo_2022
df_2023['nome_do_arquivo'] = nome_arquivo_2023

# %%
arquivos_consolidados_df = pd.concat([df_2021, df_2022, df_2023])

# %%
arquivos_consolidados_df

# %%



