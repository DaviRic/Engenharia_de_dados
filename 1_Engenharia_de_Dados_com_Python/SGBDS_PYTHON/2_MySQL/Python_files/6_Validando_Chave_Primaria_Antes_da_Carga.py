import pandas as pd # type: ignore
import mysql.connector # type: ignore
caminho_categories = r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\Arquivo_meu\Origem_de_dados\Bike\categories.csv'

df_categories = pd.read_csv(caminho_categories, sep=',')

cnx = mysql.connector.connect (
                                user='root',          # Usuário   
                                password='senha123',  #  Senha
                                host='localhost',     # Servidor MySQL
                                database='python'     # Banco de dados
                              )
cursor = cnx.cursor()

# Insere do dataframe no banco de dados
for _, df_categories_coluna in df_categories.iterrows():
    
    cursor.execute('SELECT category_id FROM python.categories WHERE category_id = %s', (df_categories_coluna['category_id'],))
    result = cursor.fetchone()

    if not result:
        cursor.execute(
        '''
            INSERT INTO python.categories (category_id, category_name)
            VALUES (%s, %s)
        ''', (
            df_categories_coluna['category_id'],
            df_categories_coluna['category_name']
            )
        )

cnx.commit()

cursor.close()  # Fecha o cursor
cnx.close()     # Fecha conexão
