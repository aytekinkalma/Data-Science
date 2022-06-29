SELECT #table_main.customer_id , #table_main.first_name, #table_main.last_name, CASE WHEN #table_1.first_product = 'Polk Audio - 50 W Woofer - Black' THEN 'Yes' ELSE 'No' end as First_product ,
											CASE WHEN #table_2.second_product = 'SB-2000 12 500W Subwoofer (Piano Gloss Black)' THEN 'Yes' ELSE 'No' end as Second_product,
											CASE WHEN #table_3.third_product = 'Virtually Invisible 891 In-Wall Speakers (Pair)' THEN 'Yes' ELSE 'No' end as Third_product
FROM #table_main
LEFT JOIN #table_1 ON #table_main.customer_id=#table_1.customer_id
LEFT JOIN #table_2 ON #table_main.customer_id=#table_2.customer_id
LEFT JOIN #table_3 ON #table_main.customer_id=#table_3.customer_id

SELECT DISTINCT SC.customer_id , SC.first_name, SC.last_name, PP.product_name
INTO #table_main
FROM sale.customer SC
INNER JOIN sale.orders SO
ON SC.customer_id = SO.customer_id
INNER JOIN sale.order_item SOI
ON SO.order_id = SOI.order_id
INNER JOIN product.product PP
ON SOI.product_id = PP.product_id
WHERE PP.product_name = '2TB Red 5400 rpm SATA III 3.5 Internal NAS HDD'

SELECT DISTINCT SC.customer_id , SC.first_name, SC.last_name, PP.product_name first_product
INTO #table_1
FROM sale.customer SC
INNER JOIN sale.orders SO
ON SC.customer_id = SO.customer_id
INNER JOIN sale.order_item SOI
ON SO.order_id = SOI.order_id
INNER JOIN product.product PP
ON SOI.product_id = PP.product_id
WHERE PP.product_name = 'Polk Audio - 50 W Woofer - Black'

SELECT DISTINCT SC.customer_id , SC.first_name, SC.last_name, PP.product_name second_product
INTO #table_2
FROM sale.customer SC
INNER JOIN sale.orders SO
ON SC.customer_id = SO.customer_id
INNER JOIN sale.order_item SOI
ON SO.order_id = SOI.order_id
INNER JOIN product.product PP
ON SOI.product_id = PP.product_id
WHERE PP.product_name = 'SB-2000 12 500W Subwoofer (Piano Gloss Black)'

SELECT DISTINCT SC.customer_id , SC.first_name, SC.last_name, PP.product_name third_product
INTO #table_3
FROM sale.customer SC
INNER JOIN sale.orders SO
ON SC.customer_id = SO.customer_id
INNER JOIN sale.order_item SOI
ON SO.order_id = SOI.order_id
INNER JOIN product.product PP
ON SOI.product_id = PP.product_id
WHERE PP.product_name = 'Virtually Invisible 891 In-Wall Speakers (Pair)'



