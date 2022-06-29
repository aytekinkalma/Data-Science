USE SampleRetail;
/*
DROP TABLE IF EXISTS #join_table;
DROP TABLE IF EXISTS #table_hdd;
DROP TABLE IF EXISTS #table_Woofer;
DROP TABLE IF EXISTS #table_Subwoofer;
DROP TABLE IF EXISTS #table_Speakers;
*/
GO

SELECT	sc.customer_id, 
		sc.first_name, sc.last_name,
		pp.product_name
INTO	#join_table
FROM	sale.customer sc
JOIN	sale.orders so
		ON sc.customer_id=so.customer_id
JOIN	sale.order_item soi
		ON so.order_id=soi.order_id
JOIN	product.product pp
		ON	soi.product_id=pp.product_id;
GO

--#table_hdd -> '2TB Red 5400 rpm SATA III 3.5 Internal NAS HDD' --109
SELECT DISTINCT *
INTO	#table_hdd
FROM	#join_table
WHERE	product_name='2TB Red 5400 rpm SATA III 3.5 Internal NAS HDD';
GO

--1. 'Polk Audio - 50 W Woofer - Black' -- (first_product)
SELECT DISTINCT *
INTO	#table_Woofer
FROM	#join_table
WHERE	product_name='Polk Audio - 50 W Woofer - Black'; --102
GO

--2. 'SB-2000 12 500W Subwoofer (Piano Gloss Black)' -- (second_product) --90
SELECT DISTINCT *
INTO	#table_Subwoofer
FROM	#join_table
WHERE	product_name='SB-2000 12 500W Subwoofer (Piano Gloss Black)';
GO

--3. 'Virtually Invisible 891 In-Wall Speakers (Pair)' -- (third_product) --95
SELECT DISTINCT *
INTO	#table_Speakers
FROM	#join_table
WHERE	product_name='Virtually Invisible 891 In-Wall Speakers (Pair)';
GO

--RESULT -> LEFT JOIN #table_hdd, #table_Woofer, #table_Subwoofer, #table_Speakers
SELECT	hdd.*, 
		IIF(woofer.product_name = 'Polk Audio - 50 W Woofer - Black','Yes','No') as First_product,
		IIF(subwoofer.product_name = 'SB-2000 12 500W Subwoofer (Piano Gloss Black)','Yes','No') as Second_product,
		IIF(speakers.product_name = 'Virtually Invisible 891 In-Wall Speakers (Pair)','Yes','No') as Third_product
FROM	#table_hdd as hdd
LEFT JOIN	#table_Woofer as woofer ON hdd.customer_id=woofer.customer_id
LEFT JOIN	#table_Subwoofer as subwoofer ON hdd.customer_id=subwoofer.customer_id
LEFT JOIN	#table_Speakers as speakers ON hdd.customer_id=speakers.customer_id;
GO