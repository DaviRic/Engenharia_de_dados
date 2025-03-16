import mysql.connector # type: ignore
import pandas as pd # type: ignore

def carga_categories(df_categories):

    cnx = mysql.connector.connect (
                                    user='root',          # Usuário   
                                    password='senha123',  # Senha
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

def carga_products(df_products):

    cnx = mysql.connector.connect (
                                    user='root',          # Usuário   
                                    password='senha123',  # Senha
                                    host='localhost',     # Servidor MySQL
                                    database='python'     # Banco de dados
                                )
    cursor = cnx.cursor()

    # Insere do dataframe no banco de dados
    for _, df_products_coluna in df_products.iterrows():
        
        cursor.execute('SELECT product_id FROM python.products WHERE product_id = %s', (df_products_coluna['product_id'],))
        result = cursor.fetchone()

        if not result:
            cursor.execute(
            '''
                INSERT INTO python.products (product_id, product_name, brand_id, category_id, model_year, list_price)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (
                df_products_coluna['product_id'],
                df_products_coluna['product_name'],
                df_products_coluna['brand_id'],
                df_products_coluna['category_id'],
                df_products_coluna['model_year'],
                df_products_coluna['list_price'],
                )
            )

    cnx.commit()
    cursor.close()  # Fecha o cursor
    cnx.close()     # Fecha conexão

def carga_stores(df_stores):

    cnx = mysql.connector.connect (
                                    user='root',          # Usuário   
                                    password='senha123',  # Senha
                                    host='localhost',     # Servidor MySQL
                                    database='python'     # Banco de dados
                                )
    cursor = cnx.cursor()

    # Insere do dataframe no banco de dados
    for _, df_stores_coluna in df_stores.iterrows():
        
        cursor.execute('SELECT store_id FROM python.stores WHERE store_id = %s', (df_stores_coluna['store_id'],))
        result = cursor.fetchone()

        if not result:
            cursor.execute(
            '''
                INSERT INTO python.stores (store_id, store_name, phone, email, street, city, state, zip_code)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                df_stores_coluna['store_id'],
                df_stores_coluna['store_name'],
                df_stores_coluna['phone'],
                df_stores_coluna['email'],
                df_stores_coluna['street'],
                df_stores_coluna['city'],
                df_stores_coluna['state'],
                df_stores_coluna['zip_code']
                )
            )

    cnx.commit()
    cursor.close()  # Fecha o cursor
    cnx.close()     # Fecha conexão

def carga_customer(df_customers):

    cnx = mysql.connector.connect (
                                    user='root',          # Usuário   
                                    password='senha123',  # Senha
                                    host='localhost',     # Servidor MySQL
                                    database='python'     # Banco de dados
                                )
    cursor = cnx.cursor()

    # Insere do dataframe no banco de dados
    for _, df_customers_coluna in df_customers.iterrows():
        
        cursor.execute('SELECT customer_id FROM python.customers WHERE customer_id = %s', (df_customers_coluna['customer_id'],))
        result = cursor.fetchone()

        if not result:
            cursor.execute(
            '''
                INSERT INTO python.customers (customer_id, first_name, last_name, phone, email, street, city, state, zip_code)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                df_customers_coluna['customer_id'],
                df_customers_coluna['first_name'],
                df_customers_coluna['last_name'],
                df_customers_coluna['phone'],
                df_customers_coluna['email'],
                df_customers_coluna['street'],
                df_customers_coluna['city'],
                df_customers_coluna['state'],
                df_customers_coluna['zip_code']
                )
            )

    cnx.commit()
    cursor.close()  # Fecha o cursor
    cnx.close()     # Fecha conexão

def carga_orders(df_orders):

    cnx = mysql.connector.connect (
                                    user='root',          # Usuário   
                                    password='senha123',  # Senha
                                    host='localhost',     # Servidor MySQL
                                    database='python'     # Banco de dados
                                )
    cursor = cnx.cursor()

    # Insere do dataframe no banco de dados
    for _, df_orders_coluna in df_orders.iterrows():
        
        cursor.execute('SELECT order_id FROM python.orders WHERE order_id = %s', (df_orders_coluna['order_id'],))
        result = cursor.fetchone()

        if not result:
            cursor.execute(
            '''
                INSERT INTO python.orders (order_id, customer_id, order_status, order_date, required_date, shipped_date, store_id, staff_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                df_orders_coluna['order_id'],
                df_orders_coluna['customer_id'],
                df_orders_coluna['order_status'],
                df_orders_coluna['order_date'],
                df_orders_coluna['required_date'],
                df_orders_coluna['shipped_date'],
                df_orders_coluna['store_id'],
                df_orders_coluna['staff_id']
                )
            )

    cnx.commit()
    cursor.close()  # Fecha o cursor
    cnx.close()     # Fecha conexão

def carga_order_items(df_orders_items):

    cnx = mysql.connector.connect (
                                    user='root',          # Usuário   
                                    password='senha123',  # Senha
                                    host='localhost',     # Servidor MySQL
                                    database='python'     # Banco de dados
                                )
    cursor = cnx.cursor()

    # Insere do dataframe no banco de dados
    for _, df_orders_items_coluna in df_orders_items.iterrows():
        
        cursor.execute('SELECT order_id FROM python.order_items WHERE order_id = %s', (df_orders_items_coluna['order_id'],))
        result = cursor.fetchone()

        if not result:
            cursor.execute(
            '''
                INSERT INTO python.order_items (order_id, item_id, product_id, quantity, list_price, discount)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (
                df_orders_items_coluna['order_id'],
                df_orders_items_coluna['item_id'],
                df_orders_items_coluna['product_id'],
                df_orders_items_coluna['quantity'],
                df_orders_items_coluna['list_price'],
                df_orders_items_coluna['discount']
                )
            )

    cnx.commit()
    cursor.close()  # Fecha o cursor
    cnx.close()     # Fecha conexão

df_categories = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\Arquivo_meu\Origem_de_dados\Bike\categories.csv', sep=',').fillna('')
df_stores = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\Arquivo_meu\Origem_de_dados\Bike\stores.csv', sep=',').fillna('')
df_customers = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\Arquivo_meu\Origem_de_dados\Bike\customers.csv', sep=',').fillna('')
# df_customers = df_customers.fillna('') Transformação de dados. Eliminando NaN
df_products = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\Arquivo_meu\Origem_de_dados\Bike\products.csv').fillna('')
df_orders = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\Arquivo_meu\Origem_de_dados\Bike\orders.csv').fillna('')
# Transformando dados para o tipo correto [Próximas três linhas]
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])
df_orders['required_date'] = pd.to_datetime(df_orders['required_date'])
df_orders['shipped_date'] = pd.to_datetime(df_orders['shipped_date'])
df_orders_items = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\Arquivo_meu\Origem_de_dados\Bike\order_items.csv').fillna('')


# Chamando as funções para carregar os dados no banco de dados
carga_categories(df_categories)
carga_products(df_products)
carga_stores(df_stores)
carga_customer(df_customers)
carga_orders(df_orders)
carga_order_items(df_orders_items)



