import pandas as pd # type: ignore
import codecs
from chardet.universaldetector import UniversalDetector # type: ignore
import json

pd.set_option('display.max_columns', None)  # Ver todas as colunas

# Definir caminho do arquivo
caminho_do_arquivo = r"C:\Users\Cliente\Desktop\Engenharia_de_dados_com_Python\SGBDS_PYTHON\Postgree\V_OCORRENCIA_AMPLA.json"

# Detectar encoding do arquivo
detector = UniversalDetector()

with codecs.open(caminho_do_arquivo, 'rb') as arquivo:
    for linha in arquivo:
        detector.feed(linha)
        if detector.done:
            break  # Para a detecção se já foi suficiente

detector.close()
encoding_detectado = detector.result['encoding'] or 'utf-8'  # Fallback para 'utf-8'
print(f"Encoding detectado: {encoding_detectado}")

# Carregar JSON usando o encoding detectado
df_json_automatico = pd.read_json(caminho_do_arquivo, encoding=encoding_detectado)
print(df_json_automatico.head())

# Outra abordagem: Ler JSON diretamente e normalizar
with codecs.open(caminho_do_arquivo, 'r', encoding=encoding_detectado) as arquivo:
    data = json.load(arquivo)

df_json = pd.json_normalize(data, max_level=1)  # Ajuste de normalização
print(df_json.head())
