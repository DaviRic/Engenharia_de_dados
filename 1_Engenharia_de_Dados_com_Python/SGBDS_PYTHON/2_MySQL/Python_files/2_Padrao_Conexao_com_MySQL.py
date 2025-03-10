import mysql.connector # type: ignore
cnx = mysql.connector.connect (
                                user='root',          # Usuário   
                                password='senha123',  #  Senha
                                host='localhost',     # Servidor MySQL
                                database='sakila'     # Banco de dados
                              )

cursor = cnx.cursor()   # Executa comandos de query, insert, delete, create, update, etc

cursor.close()  # Fecha o cursor
cnx.close()     # Fecha conexão
