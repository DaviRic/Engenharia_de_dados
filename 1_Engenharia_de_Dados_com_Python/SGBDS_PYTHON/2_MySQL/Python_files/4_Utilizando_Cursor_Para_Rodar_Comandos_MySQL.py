# pip install pandas mysql-connector-python
import mysql.connector # type: ignore
import pandas as pd # type: ignore
cnx = mysql.connector.connect (
                                user='root',          # Usuário   
                                password='senha123',  #  Senha
                                host='localhost',     # Servidor MySQL
                                database='sakila'     # Banco de dados
                              )
cursor = cnx.cursor()


comando = '''
DELETE FROM python.testepython;
'''

cursor.execute(comando)
cnx.commit()

cursor.close()  # Fecha o cursor
cnx.close()     # Fecha conexão


# %%



