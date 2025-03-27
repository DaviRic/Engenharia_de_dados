import pandas as pd # type: ignore

df = pd.read_excel(r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_excel\Produto.xlsx")

df_calca = df.loc[df['Name'] == 'Calça']


itens = ['Calça', 'TV','Perfume', 'Fogão']
df_itens = df.loc[df['Name'].isin(itens)]
df_itens


# Localizar um valor mais que o um número
df_maior_1000 = df.loc[df['Price'] > 1000]
df_maior_1000.head()


df_200_a_1000 = df.loc[(df['Price'] > 200) & (df['Price'] <= 1000)]
df_200_a_1000





