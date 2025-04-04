import pandas as pd # type: ignore

df = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_csv\Clientes.csv', delimiter=',')

df['nome_completo'] = df['first_name'] + ' ' + df['last_name']

df['created_at'] = pd.to_datetime(df['created_at'])

# Adicionar coluna somente com ano
df['year'] = df['created_at'].dt.year

# Adicionar coluna somente com o mês
df['month'] = df['created_at'].dt.month

# Adicionar coluna com o nome do mês respectivo ao número
df['month'] = df['month'].astype(str)
cont = 0
for coluna in df['month']:
    match int(coluna):
        case 1:
            df.loc[cont, 'month'] = 'janeiro'
            cont+=1
        case 2:
            df.loc[cont, 'month'] = 'fevereiro'
            cont+=1
        case 3:
            df.loc[cont, 'month'] = 'março'
            cont+=1
        case 4:
            df.loc[cont, 'month'] = 'abril'
            cont+=1
        case 5:
            df.loc[cont, 'month'] = 'maio'
            cont+=1
        case 6:
            df.loc[cont, 'month'] = 'junho'
            cont+=1
        case 7:
            df.loc[cont, 'month'] = 'julho'
            cont+=1
        case 8:
            df.loc[cont, 'month'] = 'agosto'
            cont+=1
        case 9:
            df.loc[cont, 'month'] = 'setembro'
            cont+=1
        case 10:
            df.loc[cont, 'month'] = 'outubro'
            cont+=1
        case 11:
            df.loc[cont, 'month'] = 'novembro'
            cont+=1
        case 12:
            df.loc[cont, 'month'] = 'dezembro'
            cont+=1

# Adicionar coluna com o nome do mês respectivo ao número de forma mais avançada e sem gambiarra
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio',  'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

df['month_name'] = df['created_at'].dt.month.map(lambda x: meses[x-1])

# Adicionar coluna de dia
df['day'] = df['created_at'].dt.day

df = pd.read_csv(r'C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\4_ETL Pandas\arquivos_csv\Clientes.csv', delimiter=',')

# Juntando nome e sobrenome em uma coluna separada
df['nome_completo'] = df['first_name'] + ' ' + df['last_name']

# Convertendo a data para o formato de dados 'Date'
df['created_at'] = pd.to_datetime(df['created_at'])

# Adicionando a coluna ano
df['year'] = df['created_at'].dt.year

# Adicionando a coluna mês
df['month'] = df['created_at'].dt.month

# Adicionando a coluna dia
df['day'] = df['created_at'].dt.day

# Adicionando uma coluna com os nomes dos meses de acordo com o número presente na data
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio',  'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

df['month_name'] = df['created_at'].dt.month.map(lambda x: meses[x-1])
