--SQL-9. ders_13.06.2022(session-8)


--1.CORRELATED SUBQUERIES
-- Çok yaygýn kullanýlýr
-- 2 fonksiyon var burada. 1.Exist 2.non-exist
-- exist : tabloya bir sorgu atýyorusunuz sonra B tablosundan ya da yine A tablosunda bu kayýtlarýn baþka bir yerde bulunup
-- .. bulunmadýðýna bakýyorsunuz. Bir alan çekmiyorsunuz oradan. Sadece var mý yok mu buna bakýyoruz. Bir check etme iþlemi yani
-- NOT exist : Tam tersi 2. tabloda olmama durumunu test ediyorsunuz


-- EXIST
SElect * from sale.customer WHERE EXISTS(SELECT 1)

SELECT * from sale.customer A WHERE EXISTS (SELECT 1 FROM sale.orders B WHERE B.order_date > '2020-01-01' AND A.customer_id=B.customer_id)
-- Bana sadece 2020 ocak 1 den sonra sipariþ vermiþ olma "durumunu" göster
-- SELECT 1: Buradaki 1 in hiç bir anlamý yok. Buna takýlmayalým

------------

-- NOT EXIST
SElect * from sale.customer WHERE NOT EXISTS(SELECT 1)

SELECT * from sale.customer A WHERE NOT EXISTS (SELECT 1 FROM sale.orders B WHERE B.order_date > '2020-01-01' AND A.customer_id=B.customer_id)
-- Bana sadece 2020 ocak 1 den sonra sipariþ yapmýþ olmama "durumunu" göster
-- Soru: Bu sorguda diyelim biri yeni kaydedilmiþ ve sipariþi olmamýþ. BU sorgu sonucunda bu müþteri gelir mi gelmez mi ?
-- ...Kriter þu burada: Customer tablosuna gidiyor her bir satýr için customer_id 1 sonra order tablosuna gidiyor orders ý varsa alýyor yoksa almýyor
-- ... inner query içinde varsa o kiþiyi alýyor yoksa eliyor. Yani gelmesi lazým

--Soru: Apple - Pre-Owned iPad 3 - 32GB - White ürünün hiç sipariþ verilmediði eyaletleri bulunuz.
--Eyalet müþterilerin ikamet adreslerinden alýnacaktýr.

Select * from product.product WHERE product_name = 'Apple - Pre-Owned iPad 3 - 32GB - White'

-- Bu ürünün hangi sipariþlerde verildiðini bir sorgulayayým sonra eyalet kýsmýna geçiþ yapalýmö

select	distinct C.state
from	product.product P,
		sale.order_item I,
		sale.orders O,
		sale.customer C
where	P.product_name = 'Apple - Pre-Owned iPad 3 - 32GB - White' and
		P.product_id = I.product_id and
		I.order_id = O.order_id and
		O.customer_id = C.customer_id
;

-- Þimdi bana öyle bir eyalet getir ki o eyalette bu ürün satýn alýnmamýþ olsun
-- UNION la birleþtirip olmayanlarý EXCEPT ile çýkartabiliriz vs ama þimdi biz NOT EXIST ile yapacaðýz burada

-- Exist içine yukarýdaki sorguyu yapýþtýrýyoruz outer query de from dan sonra sale.customer C2 dedik
-- .. Çünkü bir þart eklemeliyiz(Altta açýklanýyor)
select	distinct [state]
from	sale.customer C2
where	not exists (
			select	distinct C.state
			from	product.product P,
					sale.order_item I,
					sale.orders O,
					sale.customer C
			where	P.product_name = 'Apple - Pre-Owned iPad 3 - 32GB - White' and
					P.product_id = I.product_id and
					I.order_id = O.order_id and
					O.customer_id = C.customer_id and
					C2.state = C.state
		)
;

-- Þartýmýz: C2.state = C.state : Yani, outer query de gelen statelerin inner query de olmama þartýný inner query ye ekliyorum
-- EXIST ya da NOT EXIST i foreign keyler ya da primary keyler üzerinden yaparsak daha hýzlý çalýþýr
-- .. Diðer türlü tüm tabloyu taramasý gerekiyor


--Dersin 2. bölümü
--Soru: Burkes Outlet maðaza stoðunda bulunmayýp,
-- Davi techno maðazasýnda bulunan ürünlerin stok bilgilerini döndüren bir sorgu yazýn

SELECT PC.product_id, PC.store_id, PC.quantity
FROM product.stock PC, sale.store SS
WHERE PC.store_id = SS.store_id AND SS.store_name = 'Davi techno Retail' AND
NOT EXISTS( SELECT DISTINCT A.product_id, A.store_id, A.quantity
FROM product.stock A, sale.store B
WHERE A.store_id = B.store_id AND B.store_name = 'Burkes Outlet' AND PC.product_id = A.product_id AND A.quantity>0)

--- Davi techno Retail da stoðu bulunnanlarý alacak
--- Burkes Outlet in stocklarýnda quantity>0 olanlarý not exists yapacak
--- quantityi belirtmeseydik;
--- çýktý hiçbir þey getirmedi. Buradan þu çýkýyor olabilir. Bu ürünlerin(Çýktýdaki 5 tane) Burkes outlet maðazaýnda satýrlarý var
-- ancak bu ürünlerin stock miktarlarý 0.
-- sale.store tablosunu inner query ile kullanmadýk ama yinede outer query de SS.store_name diyebiliriz

-- Bütün ürünlerimin stock bilgisi stock tablosunda var. Burkes in stoðunda 0 olarak gözüken ürünlerden bul diye de sonuca ulaþabiliriz
-- Exists ve quantity=0 diyerek
SELECT PC.product_id, PC.store_id, PC.quantity
FROM product.stock PC, sale.store SS
WHERE PC.store_id = SS.store_id AND SS.store_name = 'Davi techno Retail' AND
EXISTS( SELECT DISTINCT A.product_id, A.store_id, A.quantity
FROM product.stock A, sale.store B
WHERE A.store_id = B.store_id AND B.store_name = 'Burkes Outlet' AND PC.product_id = A.product_id AND A.quantity=0)


-- Soru: -- Brukes Outlet storedan alýnýp The BFLO Store maðazasýndan hiç alýnmayan ürün var mý?
-- Varsa bu ürünler nelerdir?
-- Ürünlerin satýþ bilgileri istenmiyor, sadece ürün listesi isteniyor.

SELECT P.product_name
FROM product.product P   
WHERE NOT EXISTS (
SELECt I.product_id
FROM sale.order_item I, sale.orders O, sale.store S
WHERE I.order_id = O.order_id AND S.store_id = O.store_id 
AND S.store_name = 'The BFLO Store' 
and P.product_id = I.product_id)

-- sorguya devam ediyoruz
-- P.product_name: product name geliyor ancak bu aþaðýdaki kurala uymalý(subquery de)
-- NOT EXIST Dediðine göre birþeyleri eleyeceðiz. (The BFLO Store maðazasýndan hiç alýnmayan)
-- Elemek istediðimiz yer: P.product_id = I.product_id  bu kod . Bütün product listemizde "The BFLO Store" dan sipariþ edilmiþ ürünleri eliyorum
-- Bir kriter daha vardý: Brukes Outlet storedan alýnan o yüzden AND diyip EXISTS diyip devam ediyorum
-- Sonuç olarak 8 tane ürün geldi. 520 tane üründen 8 geldi
-- Tek sorguda product tablosunda istediðimiz 8 satýrý seçmiþ olduk

SELECT P.product_name, p.list_price, p.model_year
FROM product.product P
WHERE NOT EXISTS (
		SELECt	I.product_id
		FROM	sale.order_item I,
				sale.orders O,
				sale.store S
		WHERE	I.order_id = O.order_id AND S.store_id = O.store_id
				AND S.store_name = 'The BFLO Store'
				and P.product_id = I.product_id)
	AND
	EXISTS (
		SELECt	I.product_id
		FROM	sale.order_item I,
				sale.orders O,
				sale.store S
		WHERE	I.order_id = O.order_id AND S.store_id = O.store_id
				AND S.store_name = 'Burkes Outlet'
				and P.product_id = I.product_id)
;
    
--- Bunu yine except ile yapabilirdik

SELECT	distinct I.product_id
		FROM	sale.order_item I,
				sale.orders O,
				sale.store S
		WHERE	I.order_id = O.order_id AND S.store_id = O.store_id
				AND S.store_name = 'Burkes Outlet'
except
		SELECT	distinct I.product_id
		FROM	sale.order_item I,
				sale.orders O,
				sale.store S
		WHERE	I.order_id = O.order_id AND S.store_id = O.store_id
				AND S.store_name = 'The BFLO Store'
;


-------------------------------------
-- CTE(Common Table Expressions)
-- Bir VIEW gibi çalýþýrlar.
-- Sorgu sürecinde o sýrada meydana gelip daha sonra Sorgu sonunda kaybolan objelerdir.
-- Sadece sorguya özgü VIEW diyebiliriz.
-- ALL CTEs(ordinary or recursive) stat with a "WITH" clause ...
-- Bir common table içinde birden fazla WITH clause kullanýlabilir
-- 2. çeþiti var 1.Ordinary 2. Recursive

-------------------------
-- 1.Ordinary Common Table Expressions
/*
WITH query_name [(column_name1, ...)] AS
(SELECT ... ) -- CTE Definition

SQL_Statement; -- yukarda tanýmlamýþ olduðumuz tabloyu kullanýyoruz bu statementta
*/
------------
-- 2.Recursive Common Table Expressions
/*
WITH table_name (column_list) AS
..............
Hoca: devamý önemli deðil çünkü ihtiyaç olunca gerekli kaynaklardan kopyala yapýþtýr yapacaðýz çalýþýrken
*/
-- for döngüsü gibi kural tanýmlayarak bir sorgu oluþturabiliyorsunuz

---------

-----------------------------
-- 1.Ordinary Common Table Expressions
-- Soru: -- Jerald Berray isimli müþterinin son sipariþinden önce sipariþ vermiþ 
--ve Austin þehrinde ikamet eden müþterileri listeleyin.

SELECT * FROM sale.customer a, sale.orders b
WHERE a.first_name = 'Jerald' and a.last_name ='Berray'
and a.customer_id = b.customer_id 

-- her yýlda 1 er tane sipariþ var. Buradan max(order_date i seçeceðiz)

SELECT  max(b.order_date) FROM sale.customer a, sale.orders b
WHERE a.first_name = 'Jerald' and a.last_name ='Berray'
and a.customer_id = b.customer_id 

--- bu elimizde dursun. Þimdi austin þehrinde ikamet edenlere bakalým
SElect * from sale.customer a 
where a.city = 'Austin'
--42 rows

----

SElect * from sale.customer a , sale.orders b
where a.city = 'Austin' and a.customer_id = b.customer_id
--35 row.. hepsinin sipariþ bilgisi yokmuþ

--- WITH i kullanalým

with tbl AS (
	select	max(b.order_date) JeraldLastOrderDate
	from	sale.customer a, sale.orders b
	where	a.first_name = 'Jerald' and a.last_name = 'Berray'
			and a.customer_id = b.customer_id
)
select	*
from	sale.customer a,
		Sale.orders b,
		tbl c
where	a.city = 'Austin' and a.customer_id = b.customer_id and
		b.order_date < c.JeraldLastOrderDate
;


--- b.order_date < c.JeraldLastOrderDate koþulu sona eklemiþ olduk

-- Dersin 3. bölümü
-- NOT : With clause sadece tek bir sorguda çalýþýyor. 
-- Fakat with bloðunda birden fazla sorgu tanýmlayabilirsiniz
-- Bununla ilgili bir örnek yapalým


-- Herbir markanýn satýldýðý en son tarihi bir CTE sorgusunda,
-- Yine herbir markaya ait kaç farklý ürün bulunduðunu da ayrý bir CTE sorgusunda tanýmlayýnýz.
-- Bu sorgularý kullanarak  Logitech ve Sony markalarýna ait son satýþ tarihini ve toplam ürün sayýsýný (product tablosundaki) ayný sql sorgusunda döndürünüz

with tbl as(
	select	br.brand_id, br.brand_name, max(so.order_date) LastOrderDate
	from	sale.orders so, sale.order_item soi, product.product pr, product.brand br
	where	so.order_id=soi.order_id and
			soi.product_id = pr.product_id and
			pr.brand_id = br.brand_id
	group by br.brand_id, br.brand_name
) ,  ---1. tablo sonucunda her bir product ýn son sipariþ tarihi . 23 brand_id li DENAQ 2020-04-23 te en son sipariþ verilmiþ
tbl2 as(
	select	pb.brand_id, pb.brand_name, count(*) count_product
	from	product.brand pb, product.product pp
	where	pb.brand_id=pp.brand_id
	group by pb.brand_id, pb.brand_name
)  ---2. tabloda Her bir markada kaç ürünün bulunduðu. 40 satýr geldi
select	*
from	tbl a, tbl2 b
where	a.brand_id=b.brand_id and
		a.brand_name in ('Logitech', 'Sony')

--- Sony markasýna ait herhangi bir ürün en son 2020-10-21 de sipariþ verilmiþ
--- ve sony markasýna ait envanterimde 46 ürün varmýþ 
--- Logitect markasýna ait herhangi bir ürün en son 2020-08-23 de sipariþ verilmiþ
--- ve sony markasýna ait envanterimde 27 ürün varmýþ


------------------------
-- Recursive CTE Expressions
-- Ýçerisinde UNION ALL yazýp CTE içerisinde belirtmiþ olduðumuz tabloyu kullanacaðýz recursive þekilde

-- 0'dan 9'a kadar herbir rakam bir satýrda olacak þekide bir tablo oluþturun.
-- Normalde kalýbýmýz aþaðýdaki gibi
/*
WITH CTE AS ()
SELECT * from CTE;
*/

-- Bu hata veriyor.Þimdi parantez içini dolduracaðým
-- Tablo adým CTE olsun

WITH CTE AS (select 0 rakam UNION ALL select 1 rakam)  -- Bu þekilde 10 a kadar gidebiliriz
SELECT * from CTE;

--- Bunu dinamik yapalým adým adým ..DIKKAT Bu alttaki sonsuza kadar gider
---WITH CTE AS (select 0 rakam UNION ALL select rakam+1)
---SELECT * from CTE;

---WHERE bloðunda bunu sýnýrlayalým

WITH CTE AS (select 0 rakam UNION ALL select rakam+1 from cte where rakam<9)
SELECT * from CTE;

--- Raporlamada bu tip tablolar çok kullanýyorlar.
-- PowerBI da bir database oluþturarak bunu kullanacaksýnýz
-- DB ler genelde tarihler olur. Haftanýn günü, tatil mi deðil. O tarihin içinde bulunduðu ayýn ilk günü, son günü vs
-- .. gibi attribute lar olur. Bunlar çok büyük esneklik saðlar. Sizde CTE ile baþlayýp böyle bir attribute(ya da tablo) oluþturabilirsiniz


--Soru: 2020 ocak ayýnýn herbir tarihi bir satýr olacak þekilde 31 satýrlý bir tablo oluþturunuz.
--with cast('2020-01-01' as date) tarih  --- veriyi date olarak cast ettik

with ocak as (
	select	cast('2020-01-01' as date) tarih  --- veriyi date olarak cast ettik
	union all
	select	cast(DATEADD(DAY, 1, tarih) as date) tarih   -- üstteki "tarih" ile tanýmlanana 1 ekle DATEADD(DAY, 1, tarih) as date datetime olarak geldiði için bunuda cast ettik
	from ocak
	where tarih < '2020-01-31'
)
select * from ocak;
with cte AS (
	select cast('2020-01-01' as date) AS gun
	union all
	select DATEADD(DAY,1,gun)
	from cte
	where gun < EOMONTH('2020-01-01')  --EOMONTH: ayýn son gününü alýr
) --- buradan sonra biz tarih tablosu oluþturalým
select gun tarih, day(gun) gun, month(gun) ay, year(gun) yil,
	EOMONTH(gun) ayinsongunu
from cte;

-- Siz bunun yanýna tarih tablosu oluþturacaksanýz ekleme yapabilirsiniz
-- Bu þekilde bir çok attribute oluþturursanýz bu size çok büyük zenginlik kazandýracaktýr.
-- her bir tablodaki tarih ile bu tabloyu joinlersiniz. Yani bu tarihleri diðer tablolarda kullanabilirsiniz.
-- Bunun çýkýþ noktasý common table expressions

----------------------

--- Soru: Write a query that returns all staff with their manager_ids(use recursive CTE)
-- Her bir çalýþanýn patronuyla CTE sini alacaðýz burada

Select staff_id, first_name, manager_id from sale.staff where staff_id =1
 --- Þimdi de manager ý james olan kiþileri getirelim
Select * from sale.staff a where a.manager_id = 1

-- Þimdi with ekleyelim ve where a.manager_id = 1 i manuel olarak almayacaðým. Bir önce tanýmlamýþ olduðum kiþinin id sine(staff_id) sine eþitleyeceðiz

with cte as (
	select	staff_id, first_name, manager_id
	from	sale.staff
	where	staff_id = 1
	union all
	select	a.staff_id, a.first_name, a.manager_id
	from	sale.staff a, cte b
	where	a.manager_id = b.staff_id
)
select *
from	cte
;

--- a.manager_id = b.staff_id si 1 olanlarý çaðýr sonra   a.manager_id ye dönecek sonra sale.staff a tekrar gidecek tekrar
--- a.manager_id = b.staff_id  ye bakacak vs vs böyle devam edip En sonra manager_id si olmayana dönecek ve break olacak sorgumuz
--- Bu tip bir sorgu raporlama yaparken iþe yarar yoksa þu þekilde de yapabilirdik.


select staff_id, first_name, manager_id
from sale.staff
order by manager_id

--------------------
--- Soru: --2018 yýlýnda tüm maðazalarýn ortalama cirosunun altýnda ciroya sahip maðazalarý listeleyin.
--List the stores their earnings are under the average income in 2018.
--- with clause un altýnda 2 tane tablo tanýmlayacaðýz

WITH T1 AS (
SELECT	c.store_name, SUM(list_price*quantity*(1-discount)) Store_earn
FROM	sale.orders A, SALE.order_item B, sale.store C
WHERE	A.order_id = b.order_id
AND		A.store_id = C.store_id
AND		YEAR(A.order_date) = 2018
GROUP BY C.store_name
),
T2 AS (
SELECT	AVG(Store_earn) Avg_earn
FROM	T1
)
SELECT *
FROM T1, T2
WHERE T2.Avg_earn > T1.Store_earn
;

---1. tabloda Her bir store name her bir maðazanýn yapmýþ olduðu satýþ tutarý. Filtre olarak da yýla 2018 dedik
---2.tabloda T1 deki deðerlere göre ortalama aldýk
--- Tablolarý birbiri içerisinde referans gösterebiliyoruz
--- Final de T1,T2 tablosuna git T2 deki ortalama cironun T1 deki store cirolarýndan büyük olan maðazalarý getir




