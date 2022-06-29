-- SQL-10. ders_15.06.2022(session-9)
-- Dersin 1. bölümü
-- WINDOW FUNCTIONS
-- 3 gün sürecek
-- Daha az satýr sorgu ile hem de verideki detayý kaybetmiyoruz

-- CONTENT
-- 1.Window Functions(WF) vs GROUP BY
-- 2.Types of WF
-- 3.WF Syntax and Keywords
-- 4.Window frames      -- Çok önemli
-- 5.How to Apply WF

---------------------------------
-- 1.GROUP BY vs WF
-- GROUP BY  aggregate fonksiyon ile tek satýr sonuç döndürüyordu.
-- WF Ayný group by mantýðýnda çalýþýyor ama satýr sayýsýnda azalma olmuyor
-- Group by biraz yavaþ, WF daha hýzlýdýr(Genelde)

/*
                                   Group by       Window Functions      
 Distinct                          necessity      optional
 Aggregation                       necessity      optional
 Ordering                          invalid         valid
 Performance                       shower          faster
 Dependency on selected Field      dependent      independent

Distinct    : Group by da distinct sonuç gelir, WF de bu oladabilir olmayadabilir
Aggregation : Aggregate kullanmak gerekir group by da, WF de bu oladabilir olmayadabilir çünkü aggregare haricinde bir çok fonksiyonu vardýr 
Ordering    : Group by içinde kullanýlmýyor. Bir grup belirliyorsunuz. TAbloda birden fazla sýnýf olsun
 .. bu tabloda sýnýfa göre gruplama yaparsanýz öðrencilerin notlarý arasýnda ortalama deðiþmez group by da
 .. WF de order by gerekiyor genelde. Belirlediðiniz grubun ortalamasýna göre farklý sonuçlar döndürüyor WF

Performance : Group by biraz yavaþ, WF daha hýzlýdýr(Genelde)
Dependency on selected Field: Group by yaparken bilgilerin seçilen alana baðlýdýr. Bazý bilgiler kaybolur çýktýda  WF de bu baðýmsýzdýr
*/

-- GROUP BY: Group by yaptýktan sonra fonksiyon unique belirliyor gruplarý ve çýktý veriyor
-- WF: Gruplarý kendiniz manuel tanýmlayabiliyorsunuz. Bu her bir grup bize bir Frame(window) i gösteriyor

-- Þimdi group by ve WF kullanarak bir örnek yapalým
-- Soru: Her bir ürünün toplam stok miktarýný hesaplayýn
---------- group by ; 
select product_id, Sum(quantity) from product.stock
group by product_id
order by 1

----------- WF;
-- Önce bir stock tablomuza bakalým
select * from product.stock
order by product_id

-- Yeni bir satýr ekleyeceðiz þimdi
-- 1 numaralarý ürünün bütün satýrlardaki toplamýný yazdýrmak istiyorum
select *, sum(quantity) over(partition by product_id) sumWF
from product.stock
order by product_id

--- sum(quantity) over(partition by product_id) sumWF : her bir product_id için quantity toplamýný al ve sumWF de yazdýr

--- group by ile ayný sonuç istediði için distinct atacaðýz. distinct i product_id ye atacaðýz
select	distinct product_id, sum(quantity) over(partition by product_id) sumWF
from	product.stock
order by product_id

-- ÖNEMLÝ NOT: Where þartýna yazacaðýnýz þart WF hesaplanmadan önce uygulanýr
-- Soru: markalara göre ortalama ürün fiyatlarýný group by ve WF ile yapalým
----------- group by;
select brand_id, avg(list_price)
from product.product
group by brand_id 

------------ WF;
select brand_id, avg(list_price) over(partition by brand_id) as avg_price
from product.product
-- 520 rows
--  group by ile ayný çýktý gelmesi için distinct ekleyelim
select distinct brand_id, avg(list_price) over(partition by brand_id) as avg_price
from product.product
-- 40 rows
-----------------------------------------------

-- 2 tane WF kullanalým
-- Soru: brand_id ye göre her bir brand_id de kaç ürün var ve her bir brand id ye göre en yüksek fiyatlý ürün
select	*,
		count(*) over(partition by brand_id) CountOfProduct,
		max(list_price) over(partition by brand_id) MaxListPrice
from	product.product
order by brand_id, product_id


---- Dersin 2. bölümü


--  WF ile oluþturduðunu kolonlar birbirinden baðýmsýz hesaplanýr.
-- Dolayýsýyla ayný select bloðu içinde farklý partitionlar tanýmlayarak yeni kolonlar oluþturabiliriz
-- group by lý sorgularda tek bir partition vardýr(Select den sonra yazýlan aggregate fonksiyonlar tek bir partition dýr)
-- WF de sütunlar arasýnda partitionlar farklý olabilir

--Soru: WF ile her bir markadan kaçar tane ürün var ve her bir kategory içindeki toplam ürün sayýsýný bulalým

select	product_id, brand_id, category_id, model_year,
		count(*) over(partition by brand_id) CountOfProductinBrand,
		count(*) over(partition by category_id) CountOfProductinCategory
from	product.product
order by brand_id, product_id, model_year

-- 520 rows
-- brand_id    si 1 olandan toplam 41 ürün varmýþ, vs vs
-- category_id si 1 olandan toplam 40 ürün varmýþ, 4 numaralý kategoriden 283 tane ürün varmýþ vs vs
-- order by ile sýralamayý deðiþtirip ona göre çýktýmýzý istediðimiz sýralamada getirebiliriz
-- order by ile sonucu daha rahat gözlemliyoruz. O yüzden order by ile kullanmamýz daha iyi olacaktýr

-- NOT: Burada distinct yapabilir miyiz? Sonuç deðiþmez Çünkü product_id ler unique zaten
-- .. o yüzden product_id select bloðunda durduðu sürece distinct iþe yaramayacaktýr
-- .. product_id yi silip yaparsam distinct row sayýsý azalacaktýr. Çünkü çoklayan satýrlar varolacak.

----------------------------
-- 2.TYPES of WF
-- a.Aggregate Functions --- Avg, min, ...
-- b.Navigation Funtions --- Partition içerisinden gezinerek yaptýðýmýz 
-- c.Numbering Functions --- Partition lar içerisinde belirlediðimiz sýralama ile

----------------------------
-- 3.TYPES of WF
-- Syntax and Keywords
-- Select(columns) FUNCTION() OVER(PARTITION BY ... ORDER BY ... WINDOW FRAME) from table1;
-- Hesaplayacaðýmýz fonksiyonda sýralama önemliyse partition içinde order by yapýyoruz

-- Örnek kod(Hata verir)
-- SELECT *, avg(time) over (partition by id order by date rows between 1 preciding and current row) as avg_time from time_of_sales  --  

-- rows between 1 preciding and current row : 1 önceki satýrla içinde bulunduðu satýr ortalamasýný al

-------------------------------------------
-- 4.Window frames 
-- Verinin tamamý bir partition olsun sonra biz bunu farklý partition lara bölüyoruz sonra da
-- .. bi basamak sonra satýrlar arasýndaki iliþkiye window frame tanýmlýyoruz. Asýl konu burada dönüyor.
-- .. belirlediðimiz frame üzerinde fonksiyonumuz çalýþýyor. Bunun sýnýrlarýný deðiþtirebiliyorum
-- .. Örneklerde daha net oturacak.
-- current row: iþlem yapýlan satýr olsun mesela
-- partition baþýndan itibaren current row a kadar olan satýr bu satýr benim frame im olsun diyebilirim(current row dahil) -- unbounded(kümülatif toplam)
-- partition  current row dan itibaren sona kadar olan satýr bu satýr benim frame im olsun diyebilirim .. 
-- N Preciding, M following Current row dan baþlarsam; 3 önceki satýrdan baþlayýp 5 sonraki satýra kadar git diyebilirim. Toplam 9 satýrým olacaktýr

------------------------------------------
-- 5. How to Apply WF

/*
örnek

id      date       time
1     2019-07-05    22
1     2019-04-15    26
2     2019-02-06    28
1     2019-01-02    30
2     2019-08-30    20
2     2019-03-09    22

PARTITION BY id                ---> ORDER by             -- avg(time)(ROWS BETWEEN 1 PRECIDING AND CURRENT ROW)
id      date        time      id  date         time     id        date    time       avg_time
1     2019-07-05    22        1   2019-01-02    30       1   2019-01-02    30          30
1     2019-04-15    26        1   2019-04-15    26       1   2019-04-15    26          28
1     2019-01-02    30        1   2019-07-05    22       1   2019-07-05    22          24
                                                         2   2019-02-06    28          28
id      date        time      id  date         time      2   2019-03-09    22          25
2     2019-02-06    28         2  2019-02-06   28        2   2019-08-30    20          21
2     2019-08-30    20         2  2019-03-09   22
2     2019-03-09    22         2  2019-08-30   20

*/
--- Hoca : Çalýþacaðýnýz yerde raporlama yapýlýyorsa bu WF konusunu çok fazla kullanýyorsunuz
---------------------------------------------------------------------------------
-- Sürekli kullanýlabilecek bir sorgu göstereceðiz WF ile alakalý
-- Windows frame i anlamak için birkaç örnek:
-- Herbir satýrda iþlem yapýlacak olan frame in büyüklüðünü (satýr sayýsýný) tespit edip window frame in nasýl oluþtuðunu aþaðýdaki sorgu sonucuna göre konuþalým.

SELECT	category_id, product_id,
		COUNT(*) OVER() NOTHING,
		COUNT(*) OVER(PARTITION BY category_id) countofprod_by_cat,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id) countofprod_by_cat_2,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) prev_with_current,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) current_with_following,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) whole_rows,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) specified_columns_1,
		COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN 2 PRECEDING AND 3 FOLLOWING) specified_columns_2
FROM	product.product
ORDER BY category_id, product_id

-- Detay olarak category_id, product_id yi aldýk sadece. 8 tane de WF yazdýk
-- farklý frame yapýlarý tanýmlandý. her bir frame de kaç satýr geliyor görmek için bu örneði kullanýyoruz
-- sorgunun tümünü çalýþtýrýnca -520 rows. Herhangi bir satýrda herhangi bir filtreleme yapmadýk demek bu
-- 1 WF: OVER() NOTHING : Partition ýnýmýz tablomuzun tamamýdýr ve tek bir partition vardýr. Büyüklüðü? Tablomuzun tamamýdýr. Yani 520 rows
-- 2 WF: COUNT(*) OVER(PARTITION BY category_id) countofprod_by_cat : her bir category_id için farklý bir deðer hesaplanacak
-- 3 WF: COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id) countofprod_by_cat_2, : order by eklenmiþ. ürünlerin sýralamasý önemli deðil normalde 
-- .. ama order by tanýmladýðýmýz için Window frame imiz deðiþiyor.
-- .. yani Window frame tanýmlamazsak partition baþýndan current row a kadar olan bizim window frame imizdir. (örn: 10. satýr için ilk satýrdan 10 a kadar gidiyor hepsini count yapýyor vs vs)
-- 4 WF:COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) prev_with_current, :
-- ... ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW: Bu default deðer olduðu için bir üstteki ile ayný çýktý geldi. Açýklama için bir altýn açýklamasýna bakýnca onun tersi
-- diye mantýk kurup anlayabiliriz
-- 5 WF:COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) current_with_following, :
-- .. üsttekinin tam tersi bir window frame var (yukarda unb-current), burada (current-unb fol)
-- ..BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING: Current rowdan(parition ýmýzýn) partition ýmýn sonuna kadar(ilk satýr için partition ýn tamamýdýr yani 40)
-- .. 2. satýrdaonun 1 eksiði vs (yani birinci partition da 40 yazdýrdý, sonra 39, sonra 37 vs vs.)
-- 6 WF:COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) whole_rows, :
-- .. ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) whole_rows : partition ýn en baþý ve en sonu. Partition da hangi satýrda olursam olayým daima partition ýmýn baþý ve sonu
-- .. arasýnda iþlem yap. O yüzden hepsi 40 geldi. 1 WF ile ayný sonucu üretti.
-- 7 WF:COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) specified_columns_1, : 
-- .. ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING : partition içerisinde 1 satýr öne git ve 1 satýr sonraya git( Toplamda 1 önceki current ve 1 sonrakini alýp 3 satýr alýyor 
---.. NOT: Eðer 1 üst satýr ya da 1 alt satýr partition içerisinde deðilse onu iþleme alamýyoruz(1. satýr için count(*)=2 dir(current ve sonraki toplam 2), 2. satýr için 3, 3. satýr için 3 vs , partition sonunda
-- .. yani mesela 40. satýrda yine 2 gelmiþ(1 önceki ve 1 current toplam 2))
-- 8 WF:COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id ROWS BETWEEN 2 PRECEDING AND 3 FOLLOWING) specified_columns_2 :
-- .. Bu da üstteki ile ayný mantýk ilk frame 4(1 current ve 3 following), 2. si 5(1 üst,1 current ve 3 following), 3. sü 6(2 satýr üst,1 current ve 3 following)

-- Dersin 3. bölümü
-- WF lerde aggregate functions
-- Analytic Aggregate Functions :  min(), max(), avg(), count(), sum()

-- Soru: Her bir kategorideki en ucuz ürünün fiyatý nedir? category_id ve "cheapest_by_cat"
select *, min(list_price) over(partition by category_id) cheapest_by_cat
from product.product

-- her kategorinin yanýna o ürünün en ucuz fiyatýný getirdi
-- distinct li sonuç istediði için distinct atalým
select	distinct category_id, min(list_price) over(partition by category_id) cheapest_by_cat
from	product.product

---------------------------
-- Soru: Product tablosnda kaç farklý product var. Toplam ürün sayýsýný WF ile yapýnýz
select distinct count(*) over() as num_of_product
from product.product

-- Tek bir satýrlýk sonuç istiyor. Toplam ürün sayýsýný istiyor
-- Farklý ürünü bulurken count(*) yapmamýz yeterli çünkü product_id unique
-- her bir product için o sayý(520) tekrarlayacaðý için distinct yazmalýyým

-----------------------
-- Soru: How many differnt product in the order_item table? 520 tane ürünün kaç tanesini satmýþým?
-- Bu soru diðer soruya göre biraz farklý
-- 1 ürün bu tabloda 1 den fazla tabloda geçebilir burada. product_id unique deðil

select distinct product_id, count(*) over(partition by product_id) as num_of_order
from sale.order_item
-- 307 rows -- Bu tabloda 307 farklý ürün(product_id) varmýþ
-- Bu 307 sonucunu tek satýrda istiyoruz.

-- group by ile bunu yapsaydýk
select count(distinct product_id) UniqueProduct from sale.order_item

--- WF ile deneyelim
select count(distinct product_id) over() UniqueProduct from sale.order_item -- HATA. Bunu count içinde distinct olacaksa bunu group by ile yapabiliriz

-- ya da mesela select distinct product_id yi baþka yerde tanýmlayacaðýz
select distinct count(*) over()
from (select distinct product_id,  count(*) over(partition by product_id) as number_of_product
from sale.order_item) as a

--------------------
-- Soru: Write a query that returns how mant products are in each order?
-- Her bir sipariþte kaç farklý ürün olduðunu döndüren bir sorgu yazýn? 

-- group by ile
select	order_id, count(distinct product_id) UniqueProduct,
		sum(quantity) TotalProduct
from	sale.order_item
group by order_id
-- o sipariþte uniquer product sayýsý ve toplam kalem sayýsýný getirdi
-- sum(quantity) TotalProduct: Mesela order_id 1 de toplam 5 farklý ürün var toplam 8 ürün var

-- WF ile
select distinct order_id, 
count(product_id) over(partition by order_id) Count_of_Uniqueproduct,
SUM(quantity) over (partition by order_id) Count_of_product
from sale.order_item
---------------------------
-- How many different product are in each brand in each category?
-- Herbir kategorideki herbir markada kaç farklý ürünün bulunduðu
select distinct category_id, brand_id,
 count(*) over(partition by brand_id, category_id) count_of_Product
from product.product

-- 1 numaralarý kategoride 1 numaralý markaya ait 15 tane ürün varmýþ,
-- 4 numaralarý kategoride 8 numaralý markaya ait 15 tane ürün varmýþ vs vs ...

-- brand isimlerini getirmek istersek üstteki sorguyu bir subquery olarak kullanabiliriz
select A.*, B.brand_name from 
(select distinct category_id, brand_id,
 count(*) over(partition by brand_id, category_id) count_of_Product
from product.product
 ) A, product.brand B
where A.brand_id = B.brand_id

--- join ile WF örneði- ayný sonucu alalým
select distinct category_id, A.brand_id,
count(*) over(partition by A.brand_id, A.category_id) count_of_Product,
B.brand_name
from product.product A, product.brand B
WHERE A.brand_id = B.brand_id

