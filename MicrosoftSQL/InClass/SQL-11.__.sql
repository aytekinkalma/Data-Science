-- SQL-11. ders_16.06.2022(session-10)

--

-- How many different product are in each brand in each category?
-- group by ile
select category_id,brand_id,COUNT(product_id)
from product.product
group by category_id,brand_id
------------------------------------------------
--WF ile
select distinct category_id,brand_id,COUNT(product_id) OVER(PARTITION BY category_id,brand_id) cnt_prod
from product.product
"""

--------------------------------
-- FIRST_VALUE FUNCTION
-- Bir sütun için en üst satýrda yer alan deðeri getiriyor(Partition, WF ve koþullara göre)
"""
-- Örnek kod
Select A.customer_id, A.first_name, B.order_date,
FIRST_VALUE(order_date) OVER (ORDER BY B.Order_date) first_date from sale.customer A, sale.orders B 
WHERE A.customer_id = B.customer_id

--------------------------

-- Soru: Write a query that returns most stocked product in each store
-- Sorunun ilk kýsmýný yapalým burada her bir store a göre en çok stoðu olan product_id ne buna bakacaðým
Select store_id, product_id,
FIRST_VALUE(product_id) OVER(PARTITION BY store_id ORDER BY quantity DESC) most_stocked_prod
FROM product.stock
-- product_id nin ilk deðerini alýp , quantity ye göre DESCENDING sýralamam gerekiyor. 
-- Çünkü azalan sýralamada en yüksekten düþüðe gidiyor. Yani first value dediðimde
-- bunun en üsttekini yani order by yaptýðýmýz için maximum deðerini aldý
-- store_id 1 karþýsýna gelen 30 numaralý ürün 30 tane varmýþ
-- store_id 2 karþýsýna gelen 64 numaralý ürün 30 tane varmýþ
-- most_stocked_prod --> first_value of product_id
-- Þimdi istediðimiz çýktýyý getirelim
Select distinct store_id, 
FIRST_VALUE(product_id) OVER(PARTITION BY store_id ORDER BY quantity DESC) most_stocked_prod
FROM product.stock
-- Elde etmek istediðimiz sonuç geldi
-------------------------
-- Üstteki sorguda En yüksek quantity ye sahip ürün ve miktarý
Select distinct store_id, 
FIRST_VALUE(product_id) OVER(PARTITION BY store_id ORDER BY quantity DESC) most_stocked_prod,
FIRST_VALUE(product_id) OVER(ORDER BY quantity DESC) MSP_W
FROM product.stock

-- Dersin 2. bölümü
-- Soru: --Write a query that returns customers and their most valuable order with total amount of it.
-- Müþterilerin en yüksek miktara sahip deðerlerini döndürün
select B.customer_id
from sale.order_item A, sale.orders B
WHERE A.order_id = B.order_id
--Þimdi.. En deðerli sipariþi nasýl bulabiliriz. müþteriler- sipariþler ve net price larýna bakacaðým ve
-- her bir müþteri için en yükseðini bulacaðým
SELECT	customer_id, B.order_id, SUM(quantity * list_price* (1-discount)) net_price
FROM	sale.order_item A, sale.orders B
WHERE	A.order_id = B.order_id
GROUP BY customer_id, B.order_id
ORDER BY 1,3 DESC;
-- net price ý her bir customer_id ve sipariþ için bulmuþ olduk
--customer_id 1 için en yüksek amoun 1038.5370, -- order_id 1555, 3 için, 6763.3454 -- order_id 1612

-- Devam edelim ve üsttekini bir alt sorguya alýp kaydedelim WITH ile
-- Sonra onu(WITH T1) i kullanarak istediðimiz sonuca ulaþalým
WITH T1 AS (
select customer_id, B.order_id, SUM(quantity*list_price*(1-discount)) net_price
from sale.order_item A, sale.orders B where A.order_id = B.order_id
Group by customer_id, B.order_id
)
Select distinct customer_id,
FIRST_VALUE(order_id) OVER(PARTITION BY customer_id ORDER BY net_price Desc) MV_order,
FIRST_VALUE(net_price) OVER(PARTITION BY customer_id ORDER BY net_price Desc) MV_order_NET_PRICE
from T1
-- En yüksek net price a sahip sipariþi getirdik ve distinct yaptýk
-- 2. partition da net price ý getireceðiz ve ilk satýrdaki deðeri alacaðýz
-- MV: most valuable

-----------------------------------------

--Soru: Write a query that returns first order date by month
Select distinct Year(order_date) Year, Month(order_date) Month,
FIRST_VALUE(order_date) 
OVER(PARTITION BY Year(order_date),Month(order_date) ORDER BY Year(order_date)) first_order_date 
from  sale.orders

-- FIRST_VALUE(order_date): Her bir ay bazýnda ilk order_date i istiyorduk

-- Dersin 3. bölümü
-- LAST_VALUE
-- Sýralanmýþ sütun deðerleri içerisinden son deðeri getiriyor
-- Örnek kod
Select A.customer_id, A.first_name, B.order_date,
last_value(order_date) OVER (ORDER BY B.Order_date desc) last_date from sale.customer A, sale.orders B 
WHERE A.customer_id = B.customer_id

-- order_date ve last_date ayný deðerler gelmiþ. Çünkü default frame koþulunu kullandý
-- Her bir satýr için bir önceki satýrý hesaba kattý
-- 1. satýr, önceki satýr yok, kendisini aldý,
-- 2. satýrda önceki satýrý 1. satýr, bunlardan last_valueyu alýyor yani 2 yi o yüzde
-- 3. ... 
--- O yüzden Rows between unboundend preciding and unbounded following demek lazým.
-- yani last_value kullanýrken Window frame i ütteki þekilde kullanmalýyýz

--------------------------------------------

-- Store tablosunda en yüksek quantity ye sahip ürünü last_value ile getirmek istiyorum
-- Önce stock tablomuza bakalým tekrar
select * from product.stock order by 1,3 asc
-- Devam edelim
SELECT	DISTINCT store_id,
		LAST_VALUE(product_id) OVER (PARTITION BY store_id ORDER BY quantity ASC, product_id DESC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) most_stocked_prod
FROM	product.stock
-------
SELECT	DISTINCT store_id,
		LAST_VALUE(product_id) OVER (PARTITION BY store_id ORDER BY quantity ASC, product_id DESC RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) most_stocked_prod
FROM	product.stock

-- order by da 2 tane sütun kullandýk
-- NOT: range ile rows hemen hemen ayný iþlemleri yapýyor
    -- rows : unbounded preciding/following gibi keyword lerle kullanýp staýr sayýsý belirtmek istiyorsanýz kullanýyoruz
    -- range: yine keyword ler kullanýlýyor ANCAK Manuel olarak satýr sayýsý belirtemiyorsunuz

---------------
-- LAG() AND LEAD()
-- LAG() : Her bir satýr için kendisinden belirttiðimiz kadar önceki satýr deðerini getiriyor
        -- Örneðin; order_date sütunundan 3 önceki deðeri o deðerin yanýna getiriyoruz
        -- default u 1 : Kendisinden 1 önceki satýr deðerini al
        -- Null deðer için bir þey yazdýrmak istiyorsak, onu null un yerine yazdýrabiliyoruz
-----------------------------------------
-- Örnek kod
SELECT order_date,
lag(order_date,2) OVER(ORDER BY order_date) previous_second_w_lag from sale.orders
-- LEAD() : lag ýn tersi olarak sonraki satýr ddeðerlerini alýyoruz

-- Örnek kod
SELECT order_date,
lead(order_date,2) OVER(ORDER BY order_date) next_second_w_lead from sale.orders

--------------------------------
-- Soru: Her bir staff için çalýþanlarýn aldýðý sipariþlerin 1 önceki sipariþ tarihlerini yazdýrýn
SELECT	A.staff_id, B.first_name, B.last_name, A.order_id, A.order_date,
		LAG(order_date) OVER(PARTITION BY A.staff_id ORDER BY A.order_id) prev_order
FROM	sale.orders A, sale.staff B
WHERE	A.staff_id = B.staff_id

--Write a query that returns the order date of the one next sale of each staff (use the LEAD function)
SELECT	DISTINCT A.order_id, B.staff_id, B.first_name, B.last_name, order_date,
		LEAD(order_date, 1) OVER(PARTITION BY B.staff_id ORDER BY order_id) next_order_date
FROM	sale.orders A, sale.staff B
WHERE	A.staff_id = B.staff_id

-- Sütunlarý çektik
-- her bir sipariþin kendisinden 1 önceki sipariþ tarihini aldýk
-- Örneðin ;3. sipariþten bir önceki sipariþ 9 , bunun tarihi 2018-01-05 sonra 3. satýrda 12, 2018-01-06 nýn yanýna 2018-01-05 geldi
-- diðer satýrlar ayný mantýk. Ýlk sütundan önce sipariþ olmadýðý için NULL geldi
-- Not: order_id 20 numaralý sipariþ için 1 önceki tarih ayný o yüzden order_by da A.order_date yerine
-- .. A.order_id ye göre yaparsak daha mantýklý olabilir. Çünkü order_date e göre sýralayýnca önce order_id 19 u mu almalý yoksa 20 yi mi
-- .. gibi bir sorun oluþuyor. O yüzden order_id ye göre sýraladýk

-- Eðer partition yapmasaydým order_id 1,2,3,4 diye gidecek ve staff ler farklý olacaktý
SELECT	A.staff_id, B.first_name, B.last_name, A.order_id, A.order_date,
		LAG(order_date) OVER(ORDER BY A.order_id) prev_order
FROM	sale.orders A, sale.staff B
WHERE	A.staff_id = B.staff_id