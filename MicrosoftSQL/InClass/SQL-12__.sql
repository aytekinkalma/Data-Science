-- SQL-12. ders_18.06.2022(session-11)


--NUMBERING FUNCTIONS
-- Sýralama ile partition lara bölme, kümülatif oranlar oluþturma, Numaralandýrma vs

----- NUMBERING FUNCTIONS 1
-- ROW_NUMBER : HEr bir partition içerisinde 1 den baþlayýp artan bir sütun oluþuyor
-- RANK : 1 den baþlayarak Deðerler arasýnda fark var ise sýralýyor. Ayný deðerlere ayný ranký veriyor. (Örnekle daha iyi anlaþýlacak)
-- DENSE_RANK: Dense_rank e benziyor ancak --> (Örnekle daha iyi anlaþýlacak)
    -- ayný partition içinde; 
        -- row_number: 1-2-3-4-5
        -- Rank örnek: 1-2-2-2-5
       -- DEnse_rank: 1-2-2-2-3    

-- Row_Number()
--Soru: Her bir kategori içinde ürünlerin fiyat sýralamasýný yapýnýz.
select product_id, category_id, list_price
from product.product

-- Partition içinde sýralama yaptý
----------------------------------
-- Rank() -- Dense_Rank()
select product_id, category_id, list_price,
ROW_NUMBER() over(partition by category_id order by list_price) RowNum,
RANK() over(partition by category_id order by list_price) [Rank],
DENSE_RANK() over(partition by category_id order by list_price) Dense_Rank
from product.product

-- satýr 16 -- > rank:15,  dense_rank:16 çünkü list_price satýr 14 ve 15 te ayný. Eðer satýr 12,13,14,15 te 
-- list_price ayný olsaydý, satýr 12,13,14,15 de rank:12 , dense_rank:12 olup, satýr 16 da rank: 16, dense_rank : 13 olacaktý
-- NOT: RowNum : Buna "Camel type" isimlendirme deniyor
-- NOT: [Rank] : Köþeli parantez içinde yazdýðým içindeki kelimeleri SQL server string ifade gibi algýlar.
-- NOT: Dense_Rank: Pembe olarak çýkýyor. Çünkü bu SQL de bir fonksiyon ismi. Bunu deðiþtirmek önerilir
----------------------------------
-- Soru: Herbir model_yili içinde ürünlerin fiyat sýralamasýný yapýnýz (artan fiyata göre 1'den baþlayýp birer birer artacak)
-- row_number(), rank(), dense_rank()
SELECT product_id, model_year,list_price,
		ROW_NUMBER() OVER(PARTITION BY model_year ORDER BY list_price ASC) RowNum,
		RANK() OVER(PARTITION BY model_year ORDER BY list_price ASC) RankNum,
		DENSE_RANK() OVER(PARTITION BY model_year ORDER BY list_price ASC) DenseRankNum
FROM product.product;


------- NUMBERING FUNCTIONS 2
-- CUME_DIST()    : Kümülatif distribution = Row number/total rows. Kümülatif deðerler getirecek ve son satýr "1" olacak
-- PERCENT_RANK() : Percent_rank = (row number -1) /(total rows -1)
-- NTILE(N)       : Eþit sayýda kümelere bölme. Veri sýralandýktan sonra küme sayýsýný belirtip kümeleme yapýyoruz


-- Soru: Write a query that returns the cumulative distribution of the list price in product table by brand.
-- product tablosundaki list price' larýn kümülatif daðýlýmýný marka kýrýlýmýnda hesaplayýnýz
SELECT brand_id,list_price,
    ROUND(CUME_DIST() OVER(PARTITION BY brand_id ORDER BY list_price),3) as CUM_DIST
FROM product.product;

-- brand_id partition a göre ilk veri yüzde kaçlýk dilime denk geliyorsa yazdý, 
-- ..partition bittiðinde, yani son deðer 1 oldu
--  ROUND(x,3) --- virgülden sonra kaç basamak görmek istiyoruz: 3 basamak		
----------------------------------
-- Soru: Write a query that returns the relative standing of the list price in product table by brand.
SELECT brand_id,list_price,
    ROUND(CUME_DIST() OVER(PARTITION BY brand_id ORDER BY list_price),3) as CumDist,
    ROUND(PERCENT_RANK() OVER(PARTITION BY brand_id ORDER BY list_price),3) as PercentRank
FROM product.product;
----------------------------------
-- Yukarýdaki CumDist sütununu CUME_DIST fonksiyonu kullanmadan hesaplayýnýz
with tbl as (
	select	brand_id, list_price,
			count(*) over(partition by brand_id) TotalProductInBrand,
			row_number() over(partition by brand_id order by list_price) RowNum,
			rank() over(partition by brand_id order by list_price) RankNum
	from	product.product
)
select *,
	round(cast(RowNum as float) / TotalProductInBrand, 3) CumDistRowNum,
	round((1.0*RankNum / TotalProductInBrand), 3) CumDistRankNum
from tbl
-- WITH ile geçici tablo oluþturduk, sorgumuz daha sade gözüksün diye
-- Row_number la hesaplamak mý, Rank_number la hesaplamak mý daha doðru baktýk. --
-- Tam istediðimiz sonuca ulaþamadýk 2 si ile de. Hoca bakýp sonucu atacak

-------------------------- Farklý örnekler

--Write a query that returns both of the followings:
--The average product price of orders.
--Average net amount.
--Aþaðýdakilerin her ikisini de döndüren bir sorgu yazýn:
--Sipariþlerde yer alan ürünlerin liste fiyatlarýnýn ortalamasý
--Tüm sipariþlerdeki ortalama net tutarý
SELECT DISTINCT order_id, 
AVG(list_price) OVER(PARTITION BY order_id) avg_price, 
AVG(list_price * quantity* (1-discount)) OVER() avg_net_amount
FROM sale.order_item

-- OVER() : Tablonun tamamý tek bir partition olmasýný istediðimiz için partition yapmadýk burada
-----------------------------------
-- Soru: --List orders for which the average product price is higher than the average net amount.
--Ortalama ürün fiyatýnýn ortalama net tutardan yüksek olduðu sipariþleri listeleyin.
select * from (SELECT DISTINCT order_id, 
cast(AVG(list_price) OVER(PARTITION BY order_id) as numeric(6,2)) AvgPrice, 
cast(AVG(list_price*quantity*(1-discount)) OVER() as numeric(6,2)) AvgNetPrice
FROM sale.order_item) A
where A.AvgPrice > A.AvgNetPrice
-------------------------------------------
-- Cumulative sorusu
-- Soru : Calculate the stores' weekly cumulative number of orders for 2018
SELECT A.store_id, A.store_name, B.order_date,
DATEPART(ISO_WEEK, B.order_date) WeekOfYear
FROM sale.store A, sale.orders B where A.store_id = B.store_id And Year(B.order_date)= '2018'
order by 1,3
-- Þimdi partition ým burada store_id ve week of year olacak
-- Yani store id ve Select bloðunda DATEPART(ISO_WEEK, B.order_date) fonksiyonun sonucundan dönene göre partition yapacaðýz
SELECT A.store_id, A.store_name, B.order_date,
DATEPART(ISO_WEEK, B.order_date) WeekOfYear,
COUNT(*) OVER(PARTITION BY A.store_id, DATEPART(ISO_WEEK, B.order_date)) weeks_order
FROM sale.store A, sale.orders B where A.store_id = B.store_id And Year(B.order_date)= '2018'
order by 1,3
-- Bir sonraki sütuna geçelim. Maðazanýn kümülatif satýþ sayýsý(haftalýk)
select  a.store_id, a.store_name, -- b.order_date,
	datepart(ISO_WEEK, b.order_date) WeekOfYear,
	COUNT(*) OVER(PARTITION BY a.store_id, datepart(ISO_WEEK, b.order_date)) weeks_order,
	COUNT(*) OVER(PARTITION BY a.store_id ORDER BY datepart(ISO_WEEK, b.order_date)) cume_total_order
from sale.store A, sale.orders B
where a.store_id=b.store_id and year(order_date)='2018'
ORDER BY 1, 3
-- 1. haftada toplam 4 satýþ, ccum satýþ 4 , 2. hafta 6, cum satýþ 10 , 3. hafta 3, cum_satýþ 13 vs vs
-- Son olarak buna bir distinct atalým.
select distinct a.store_id, a.store_name, -- b.order_date,
	datepart(ISO_WEEK, b.order_date) WeekOfYear,
	COUNT(*) OVER(PARTITION BY a.store_id, datepart(ISO_WEEK, b.order_date)) weeks_order,
	COUNT(*) OVER(PARTITION BY a.store_id ORDER BY datepart(ISO_WEEK, b.order_date)) cume_total_order
from sale.store A, sale.orders B
where a.store_id=b.store_id and year(order_date)='2018'
ORDER BY 1, 3
-- Sonuç: Her bir satýr o haftanýn toplam satýþ sayýsýný gösteriyor
-------------------------------------------
-- Soru: Calculate 7-day moving average of the number of products sold between '2018-03-12' and '2018-04-12'
-- o günlük satýþ ve 1 önceki haftanýn ortalama satýþ sayýsý

--- Önce ihtiyacýmýz olanlara bakalým
select B.order_date, A.order_id, A.product_id, A.quantity
from sale.order_item A, sale.orders B
where A.order_id = B.order_id
-- Ayýn 1 inde toplam 11 tane ürün satýþmýþ, ayýn 2 sinde toplam 2 ürün
-- günlük bazda kaç ürün satýldýðýný bilmem lazým
-- 7 gün geri ve ileri gidebileceðim ve birbiriyle kýyaslayabileceðim bir yapý olmalý
-- Bu veri setinden tek bir gün için toplam quantity yi görmem lazým onu 1 hafta öncesiyle katþýlaþtýracaðýz
-- Bunu da sorgum karýþýk olmasýn diye WITH ile geçici tablo oluþturalým
with tbl as (
	select	B.order_date, sum(A.quantity) SumQuantity --A.order_id, A.product_id, A.quantity
	from	sale.order_item A, sale.orders B
	where	A.order_id = B.order_id
	group by B.order_date)
select	* from tbl
-- Son 7 gündeki hareketli ortalamayý hesaplayacaðýz. Bunu da o günden geriye 7 satýr git
-- .. o deðerlerin ortalamasýný getir diyeceðiz. O günün yanýna yazdýracaðýz
-----------NOT: HATA var gibi görünüyor ancak sonuç geliyor----
with tbl as (
	select	B.order_date, sum(A.quantity) SumQuantity --A.order_id, A.product_id, A.quantity
	from	sale.order_item A, sale.orders B
	where	A.order_id = B.order_id
	group by B.order_date)
select	*,
	avg(SumQuantity) over(order by order_date rows between 6 preceding and current row) sales_moving_average_7
from	tbl
where	order_date between '2018-03-12' and '2018-04-12'
order by 1

-- partition yapmama gerek yok ancak frame belirlemem lazým(7 satýrlýk ortalama için)
-- between 6 preciding and current row : 6 satýr geriye + 1 current row = 7 günlük 
-- Ortalamayý integer yerine float istersek cast(.. as float.. ) þeklinde yapabiliriz
-- Sipariþi olmayan tarihler var. O zaman gerideki günleri sayamayacaðýz.
-- Eðer bu kayýp günler önemliyse, tariht tablosu oluþturmamýz lazým
-- .. left joinle olmayan tarihleride ekleyelim sonra olmayan tarihlerin karþýsýna 0 yazýp sonra
-- .. üstteki sorgumuzla sonuca ulaþabiliriz
-- where bloðunda koþulu alýp ondan sonra filtreleme yapýyor burada
-- önce partition yapýp sonra filtrelemeyi yapacaksam . partitionlý sorguyu bir tabloya kaydedip
-- .. sonra where bloðu ekleyebilirim baþka bir sorguda
-------------------------------
-- Soru: List customers whose have at least 2 consecutive orders are not shipped
-- NOT: Hoca kendisi gerçek hayatta çözdüðü bir problemin çözümünü atacak notlarda

