-- Rodar o notebook. Enviando dados para o Postegres com sqlalchemy para ter os dados completos

-- Filtro de data manual
SELECT * FROM anac_sqlalchemy
WHERE "Data_da_Ocorrencia" >= '2024-05-29'


-- Filtrando últimos 3 meses
SELECT * FROM anac_sqlalchemy
WHERE "Data_da_Ocorrencia" >= CURRENT_DATE - INTERVAL '3 months'


-- Validando últimos 3 meses
SELECT CURRENT_DATE - INTERVAL '3 months'


-- Delete da base
DELETE FROM anac_sqlalchemy
WHERE "Data_da_Ocorrencia" >= CURRENT_DATE - INTERVAL '3 months'