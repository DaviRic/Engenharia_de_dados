
import sqlite3
import pandas as pd # type: ignore
import tkinter as tk
import tkinter.messagebox as messagebox
import sqlite3

# 1°: Criar banco de dados
con = sqlite3.connect("cadastro_produto.db")
cursor = con.cursor()

con.commit()
con.close()

def validar_numero(valor, modo):
    # Verifica se o valor é vazio ou se é um número válido (inteiro ou decimal)
    if modo == 1: # Se está inserindo texto
        if valor == (valor.replace('.', '', 1).isdigit() and valor.count('.') <= 1):
            return True
        else:
            messagebox.showerror('Erro', """Insira um valor valído (Essa área é apenas para números.
                                  Se for decimais separe por ponto)""")
    else: # Deletando texto
        return True

def cadastrar_produto():

    # Captura os dados
    id_produto = entry_id.get()
    nome_produtor = entry_nome.get()
    valor_produto = entry_valor.get()
    fornecedor_produto = entry_fornecedor.get()
    categoria_produto = entry_categoria.get()
    responsavel_cadastro = entry_responsavel.get()

    con = sqlite3.connect("cadastro_produto.db")
    cursor = con.cursor()

    # Insere no banco de dados os dados capturados
    cursor.execute("""INSERT INTO produto VALUES (?, ?, ?, ?, ?, ?)""",
                    (id_produto, nome_produtor, valor_produto, fornecedor_produto,
                     categoria_produto, responsavel_cadastro)
                  )

    con.commit()
    con.close()

    entry_id.delete(0, 'end')
    entry_categoria.delete(0, 'end')
    entry_fornecedor.delete(0, 'end')
    entry_responsavel.delete(0, 'end')
    entry_nome.delete(0, 'end')
    entry_valor.delete(0, 'end')

    messagebox.showinfo('Sucesso', 'Produto cadastrado')
    # janela.destroy()

def salvar_excel():
    con = sqlite3.connect('cadastro_produto.db')

    query = 'SELECT * FROM produto'

    df = pd.read_sql(query, con)
    con.close()
    df.to_excel('Produtos.xlsx', index=False)
    messagebox.showinfo('Sucesso', 'Arquivo excel criado')


janela = tk.Tk()
janela.title('Cadastro de produto')

# Id do produto
label_id = tk.Label(janela, text="ID do produto: ").grid(row=1, column=1, padx=10, pady=10)
entry_id = tk.Entry(janela, width=30)
entry_id.grid(row=1, column=2, padx=10, pady=10)

# Nome do produto
label_nome = tk.Label(janela, text="Nome do produto: ").grid(row=2, column=1, padx=10, pady=10)
entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row=2, column=2, padx=10, pady=10)

# Valor do produto
label_valor = tk.Label(janela, text="Valor do produto: ").grid(row=3, column=1, padx=10, pady=10)
entry_valor = tk.Entry(janela, width=30)
entry_valor.grid(row=3, column=2, padx=10, pady=10)

# Fornecedor do produto
label_fornecedor = tk.Label(janela, text="Fornecedor do produto: ").grid(row=4, column=1, padx=10, pady=10)
entry_fornecedor = tk.Entry(janela, width=30)
entry_fornecedor.grid(row=4, column=2, padx=10, pady=10)

# Categoria do produto
label_categoria = tk.Label(janela, text="Categoria do produto: ").grid(row=5, column=1, padx=10, pady=10)
entry_categoria = tk.Entry(janela, width=30)
entry_categoria.grid(row=5, column=2, padx=10, pady=10)

# Responsável pelo cadastro
label_responsavel = tk.Label(janela, text="Responsavel pelo cadastro: ").grid(row=6, column=1, padx=10, pady=10)
entry_responsavel = tk.Entry(janela, width=30)
entry_responsavel.grid(row=6, column=2, padx=10, pady=10)

# Botão de cadastrar produto (Botão para apertar para mandar os dados para o banco de dados)
bt_cadastrar = tk.Button(janela, text="Cadastrar produto", width=25, command=cadastrar_produto)
bt_cadastrar.grid(row=7, column=1, padx=10, pady=10)

# Botão para gerar o arquivo excel
bt_gerar_excel = tk.Button(janela, text="Gerar excel", width=25, command=salvar_excel)
bt_gerar_excel.grid(row=7, column=2, padx=10, pady=10)

janela.mainloop()
