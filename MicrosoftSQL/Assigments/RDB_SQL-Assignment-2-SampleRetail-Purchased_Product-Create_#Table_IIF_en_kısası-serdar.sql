USE SampleRetail;
/*
DROP TABLE IF EXISTS #main_table;
*/
GO

CREATE TABLE #main_table (
	customer_id VARCHAR(255),
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	product_name VARCHAR(255)
);
GO

INSERT INTO #main_table
SELECT	sc.customer_id, 
		sc.first_name, sc.last_name,
		pp.product_name
FROM	sale.customer sc
JOIN	sale.orders so
		ON sc.customer_id=so.customer_id
JOIN	sale.order_item soi
		ON so.order_id=soi.order_id
JOIN	product.product pp
		ON soi.product_id=pp.product_id
GO

select  customer_id,first_name,last_name 
		,IIF(sum(IIF(product_name = 'Polk Audio - 50 W Woofer - Black',1,0))=1,'Yes','No') as First_
		,IIF(sum(IIF(product_name = 'SB-2000 12 500W Subwoofer (Piano Gloss Black)',1,0))=1,'Yes','No') as Second_
		,IIF(sum(IIF(product_name = 'Virtually Invisible 891 In-Wall Speakers (Pair)',1,0))=1,'Yes','No') as Third_
from #main_table
where customer_id in (select customer_id from #main_table 
						where product_name like '2TB Red 5400 rpm SATA III 3.5 Internal NAS HDD' )
group by customer_id,first_name,last_name 
order by customer_id