import pandas as pd # type: ignore

df = pd.read_excel(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Produto_dup.xlsx')

# Armazena as linhas duplicadas em um dataframe o que melhora significativamente a vizualização dos dados
duplicados = df[df.duplicated()]

# Removendo as duplicatas e armazenando em uma variável o DF sem nenhuma duplicata
df_sem_duplicatas = df.drop_duplicates()

''' Nesse ponto o dataframe está tratado e eu posso
levar o documento para o destino que eu queira (Banco de dados
                                                arquivos excel,
                                                txt, etc)'''

df_sem_dup_parametro = df.drop_duplicates(subset=['ID'])
df_sem_dup_parametro

# Removendo diretamente as duplicatas do DF (inplace). Com esse método não é necessário criar um outro DataFrame
# Ele remove as duplicatas diretamente no dataframe
df.drop_duplicates(inplace=True)




