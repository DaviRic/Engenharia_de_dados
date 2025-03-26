
import sqlite3
import pandas as pd # type: ignore

con = sqlite3.connect('tutorial.db')
cursor = con.cursor()

cursor.execute("INSERT INTO produto (id, nome, valor) VALUES (1, 'Tenis', 200.0)")

con = sqlite3.connect('tutorial.db')

query = 'SELECT * FROM produto'
df = pd.read_sql(query, con)

con = sqlite3.connect(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\SQLite\Scripts\Teste.db')

con.commit()
con.close()
