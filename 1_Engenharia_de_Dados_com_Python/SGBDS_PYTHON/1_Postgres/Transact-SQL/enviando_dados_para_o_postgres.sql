CREATE TABLE IF NOT EXISTS Anc (
    Numero_da_Ocorrencia int,
    Classificacao_da_ocorrencia VARCHAR(50),
    Data_da_ocorrencia DATE,
    Municipio VARCHAR(50),
    UF VARCHAR(30),
    Regiao VARCHAR(30),
    Nome_do_fabricante VARCHAR(100)
)

INSERT INTO Anac (
        Numero_da_Ocorrencia,
        Classificacao_da_ocorrencia,
        Data_da_ocorrencia,
        Municipio,
        UF,
        Regiao,
        Nome_do_fabricante
    ) VALUES (
        1,
        'Acidente',
        '2022-01-01',
        'Sao Paulo',
        'SP',
        'Sudeste',
        'Jatinho 333'
    )