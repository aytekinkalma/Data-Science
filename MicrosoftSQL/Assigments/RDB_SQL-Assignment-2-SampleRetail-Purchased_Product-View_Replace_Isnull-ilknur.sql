USE SampleRetail;
/*
DROP ViEW IF EXISTS join_view;
DROP ViEW IF EXISTS view_hdd;
DROP ViEW IF EXISTS view_Woofer;
DROP ViEW IF EXISTS view_Subwoofer;
DROP ViEW IF EXISTS view_Speakers;
*/
GO

-- RUN EVERY TIME
CREATE OR ALTER VIEW join_view AS
SELECT	sc.customer_id, 
		sc.first_name, sc.last_name,
		pp.product_name
FROM	sale.customer sc
JOIN	sale.orders so
		ON sc.customer_id=so.customer_id
JOIN	sale.order_item soi
		ON so.order_id=soi.order_id
JOIN	product.product pp
		ON	soi.product_id=pp.product_id;
GO

--#table_hdd -> '2TB Red 5400 rpm SATA III 3.5 Internal NAS HDD' --109
CREATE OR ALTER VIEW view_hdd AS
SELECT DISTINCT *
FROM	join_view
WHERE	product_name='2TB Red 5400 rpm SATA III 3.5 Internal NAS HDD'
GO

--1. 'Polk Audio - 50 W Woofer - Black' -- (first_product) --102
CREATE OR ALTER VIEW view_Woofer AS
SELECT DISTINCT *
FROM	join_view
WHERE	product_name='Polk Audio - 50 W Woofer - Black'
GO

--2. 'SB-2000 12 500W Subwoofer (Piano Gloss Black)' -- (second_product) --90
CREATE OR ALTER VIEW view_Subwoofer AS
SELECT DISTINCT *
FROM	join_view
WHERE	product_name='SB-2000 12 500W Subwoofer (Piano Gloss Black)'
GO

--3. 'Virtually Invisible 891 In-Wall Speakers (Pair)' -- (third_product) --95
CREATE OR ALTER VIEW view_Speakers AS
SELECT DISTINCT *
FROM	join_view
WHERE	product_name='Virtually Invisible 891 In-Wall Speakers (Pair)'
GO

--RESULT -> LEFT JOIN #table_hdd, #table_Woofer, #table_Subwoofer, #table_Speakers
SELECT	hdd.*, 
		REPLACE(ISNULL(woofer.product_name,'No'),'Polk Audio - 50 W Woofer - Black','Yes') as First_product,
		REPLACE(ISNULL(subwoofer.product_name,'No'),'SB-2000 12 500W Subwoofer (Piano Gloss Black)','Yes') as Second_product,
		REPLACE(ISNULL(speakers.product_name,'No'),'Virtually Invisible 891 In-Wall Speakers (Pair)','Yes') as Third_product
FROM	view_hdd as hdd
LEFT JOIN	view_Woofer as woofer ON hdd.customer_id=woofer.customer_id
LEFT JOIN	view_Subwoofer as subwoofer ON hdd.customer_id=subwoofer.customer_id
LEFT JOIN	view_Speakers as speakers ON hdd.customer_id=speakers.customer_id
GO