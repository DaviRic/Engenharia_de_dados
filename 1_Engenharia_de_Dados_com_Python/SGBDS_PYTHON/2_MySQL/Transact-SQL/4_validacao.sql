-- Deletando todas as tabelas
DELETE FROM python.order_items;
DELETE FROM python.orders;
DELETE FROM python.customers;
DELETE FROM python.products;
DELETE FROM python.categories;
DELETE FROM python.stores;

SELECT count(*) as ord_items FROM python.order_items;
SELECT count(*) as stores FROM python.stores;
SELECT count(*) as orders FROM python.orders;
SELECT count(*) as customers FROM python.customers;
SELECT count(*) as products FROM python.products;
SELECT count(*) as categories FROM python.categories;

SELECT * FROM python.order_items;
SELECT * FROM python.stores;
SELECT * FROM python.orders;
SELECT * FROM python.customers;
SELECT * FROM python.products;
SELECT * FROM python.categories;