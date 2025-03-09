CREATE TABLE IF NOT EXISTS anac_mapeamento(
    ID INT,
    Classificacao_da_Ocorrencia VARCHAR(50),
    Dt_Ocorrencia DATE,
    Municipio VARCHAR(50),
    Regiao VARCHAR(30),
    Fabricante VARCHAR(100)
)

SELECT column_name FROM information_schema.columns
WHERE table_name = 'anac_mapeamento';

ALTER TABLE anac_mapeamento
ADD COLUMN nome_da_nova_coluna tipo_de_dados;