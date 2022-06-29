#%% SQL-8. ders_11.06.2022(session-7)

#%% Subqueries & Common Table Expressions
# SUBQUERIES/INNER QUERY/NESTED QUERY

# Subquery, başka bir query içerisinde bir parantez içinde tanımlanmış alt query dir
# Select bloğunda, where bloğunda ve from bloğunda kullanabiliyoruz. Sonuç tablo mu, değer mi olduğuna göre kullanım yeri değişmektedir
# FROM da olursa--> tablo döndürür
# SELECT, WHERE --> tablo veya value dönebilir

"""
-- SELECT

select order_id, list_price,
(select avg(list_price) from product.product) AS avg_price
from sale.order_item

-- Tek bir değer kullandığım için select bloğunda kullandım
-- Sonuçta bütün satırlarda aynı değerin dönmesini istiyorsak select bloğu içerisinde kullanabiliriz subquery yi
"""
###############
"""
-- WHERE 

Select order_id, order_date from sale.orders
where order_date IN (select TOP 5 order_date from sale.orders ORDER BY order_date DESC) 

-- Siparişin verildiği son 5 gün

-- Eğer aynı tarihler gelmiş olsaydı, tekilleştirmek isteseydik;
select Top 5 order_date from 
(Select distinct order_date from sale.orders) A
where order_date IN (select TOP 5 order_date from sale.orders ORDER BY order_date DESC) 
"""
###############
"""
-- FROM 

SELECT order_id, order_date from
(select top 5 * from sale.orders order by order_date desc) A

-- FROM bloğunda tanımlanan subqueries lerde "Alias" olmalı
-- Alias istedi ancak kullanmamıza gerek kalmadı, Çünkü from bloğundan sadece 1 adet order_id sütunu dönüyor 
-- Eğer from bloğundan ikinci bir order_id sütunu dönseydi hangi tabloyu kastettiğimizi belirtmek için kullanmamız gerekirdi
"""

# Types of subqueries
# 1.Single-row Subqueries(Yukarda yaptığımız gibi, liste fiyat ortalamasını döndüren)
# 2.Multiple- row subqueries
# 3.Correlated subqueries(inner query ile outer query arasında ilişki kuruyorsak)
    # Correlated subquery çok performanslı değil, çok kullanılmıyor, djoinlerle daha iyi sonuçlar geliyor

# Single-row Subqueries : Bir sütun bir hücre döndürüyor
    # Karşılaştırma yapacağımız değerler arasında =,>,>=,<= gibi karşılaştırma araçları kullanıyoruz
    # where ve select ile kullanılabiliyor
    # Bir çok query joinle kullanılabiliyor. Hangi durumda daha anlamlı bir query yazacaksa ihtiyaca göre


#%% Dersin 2. bölümü
"""
-- Soru: Her bir order_id ye göre toplam fiyat
select	so.order_id,
		(select	sum(list_price) sum_list_price from sale.order_item
		where order_id=so.order_id
		) AS sum_price
from	sale.order_item so
group by so.order_id

--- select so.order_id  ... from sale.order_item so  order_id  : order id leri seç
--- select	sum(list_price) sum_list_price from sale.order_item: her bir satırda subquerydeki list_price ın toplamını getir
--- ancak where order_id=so.order_id olduğu durumda bunu yap
--- group by so.order_id : order id ye göre grupla

-- list_price neden hem product tablosunda hem de order_item da var?
-- product tablosunda her bir ürüne ait fiyat var. Fiyat değişirse eski fiyat gidip yenisi gelecek ve bilgi kaybı olacak
-- Her bir ürünün sipariş verildiği gündeki fiyatını bilmemiz gerekiyorsa o order_item tablosunda tutuluyor. Yani bilgi
-- .. kaybedilmemiş oluyor(Yani eski fiyatı order_item tablosundan istediğimde görebilirim)

---- NOT: Sub query olmadan aşağıdaki gibi de yapılabilirdi
select	order_id, sum(list_price) avg_list_price
from	sale.order_item
group by order_id
"""
##########################
"""
NOT
--iKİSİ ARASINDAKİ FARKIN NEDENLERİNIN MANTIKSAL AÇIKLAMASI ???
--1. KOD
SELECT  B.order_id, (SELECT SUM(list_price*quantity*(1-discount)) FROM sale.order_item WHERE order_id = B.order_id ) AS TOTAL
FROM sale.order_item B
GROUP BY B.order_id
--2. KOD
SELECT  order_id, (SELECT SUM(B.list_price*B.quantity*(1-B.discount)) FROM sale.order_item B WHERE B.order_id = order_id ) AS TOTAL
FROM sale.order_item
GROUP BY order_id

# 2 kod arasındaki tek fark alias kullanılması 2. tabloda alias kullanılmamış
# 1. sorguda subqueries de order_item dan sum(list_pirce* quantity*(1-discount)) hesaplanmış
# .. where order_id = B.order_id : Buradaki order_id tek değer o yüzden alias kullanmama gerek yok, Burdaki B.order_id yi
# .. diğer tablodan çekiyor
# 2. tabloda sbuquery deki tabloya alias verilmiş
# Where B.order_id = order_id : Buradaki B.order_id , from sale.order_item B den gelen , bu subquery içerisinde olduğu için
# .. 2. tabloda subquery hata vermez ama 1. tabloda B tablosu olmadığı için hata veriyor
# 1. subqueries, 2. subquery gibi tek bir değer döndürüyor ama 1. subquery 2. subquery ye bağlı

"""
#######################
"""
-- soru :Davis Thomas'nın çalıştığı mağazadaki tüm personelleri listeleyin

select	*
from	sale.staff
where	store_id = (
					select	store_id
					from	sale.staff
					where	first_name = 'Davis' and last_name = 'Thomas'
					)

# subquery -- davis thomas ın çalıştığı store_id

--- alternatif çözüm
select *
from (
    select store_id
    from sale.staff
    where first_name = 'Davis' and last_name= 'Thomas'
) as a, sale.staff b
where a.store_id = b.store_id

"""
############################
"""
--- Soru: Charles Cussona nın manager ı olduğu kişileri listeleyin
select	*
from	sale.staff
where	manager_id = (
					select	staff_id
					from	sale.staff
					where	first_name = 'Charles' and last_name = 'Cussona'
					)

-- Staff_id ye karşılık gelen başka bir id var. Bu sütun manager_id
-- charles ın manager ı olduğu kişileri bulmam için charles ın id sini buldum. 2 imiş
--- sonra manager_id si 2 olanlara bakacağız
-- manager_id  = :  manager_id si sale.staff dan  where first_name = 'Charles' and last_name = 'Cussona' şartını
-- sağlayan ı getirdik
"""
#############################
"""
-- Soru: -- 'Pro-Series 49-Class Full HD Outdoor LED TV (Silver)' isimli üründen pahalı olan ürünleri listeleyin.
-- Product id, product name, model_year, fiyat, marka adı ve kategori adı alanlarına ihtiyaç duyulmaktadır
select A.product_id, a.product_name, a.model_year, a.list_price, b.brand_name, c.category_name
from product.product A, product.brand B, product.category C
where list_price >
	(select list_price
	from product.product
	where product_name='Pro-Series 49-Class Full HD Outdoor LED TV (Silver)')
	and A.brand_id = B.brand_id
	and A.category_id = C.category_id

-- Önce ürünümüzü product tablosundan bulmamız lazım. Bunu subquery de buldum, list_price ını seçtim
-- subquery outer query den bağımsız.
-- Bizden istenen sütunları da select ten sonra yazalım
-- En son o tabloları hangi tablodan aldıysam
-- NOT: where list_price : liste fiyatı sadece A tablosundan döneceği için A.list_price yazmadık

--- Alternatif çözüm
SELECT * 
from product.product
where list_price > (
    select list_price
    from product.product
    where product_name = 'Pro-Series 49-Class Full HD Outdoor LED TV (Silver)'
)
"""

#%% Dersin 3. bölümü
# Multiple-row Subqueries
# Tek fark; Sonuç olarak birden fazla satır dönmesi. O yüzden direk büyüktür, küçüktür gibi
# .. operatörler kullanamayız direkt olarak
# Içindedir, içinde değildir, herhangi birinden büyüktür/küçüktür gibi şeyler yapacağız

"""
-- Soru: List all customers who orders on the same dates as Laurel Goldammer
SELECT *
FROM sale.customer AS SC, sale.orders AS SO
WHERE order_date IN (
				SELECT SO.order_date
				FROM sale.customer AS SC, sale.orders AS SO
				WHERE first_name = 'Laurel' AND last_name='Goldammer'
				AND SC.customer_id=SO.customer_id
                )
				AND SC.customer_id=SO.customer_id
                AND SO.order_status = 4

--- Subquery ile outer query arasında bir ilişki tanımlamadık
-- Burada subquey tek başına çalışıyor çünkü subquey içinden SO.order_date veya SC.customer_id yazarken
--- SO ve SC ile tabloları subquery içinde tanımlandığı için hata veremiyoruz
--- Önce Laurel Goldammer alışveriş yaptığı tarihleri istiyorum.
-- Önce customer tablosundan isim buluyorum, sipariş bilgileri orders tablosunda
-- hangi müşterinin hangi tarihlerde alışveriş yaptığını alttaki sorgu sonucunda elde ettim
--- select * from sale.customer A, sale.orders B where A.customer_id = B.customer_id
-- Bütün müşterilerden Laurel goldammer ı seçiyoruz  WHERE first_name = 'Laurel' AND last_name='Goldammer'
-- Bu subqueyden bir satır dönseydi eşittir operatörü kullanacaktık ama burada eşittir kullanamayacağım
-- O yüzden burada "IN" operatörünü kullandık.
--- WHERE order_date IN: outer query de bu tarihlerden(subquery sonuçlarından) herhangi birisi olmalı
--- AND SO.order_status = 4 : Alışverişi tamamlayanlar
"""

####################################
"""
-- Soru: List products made in 2021 and their categories other than Game, gps or Home Theater
-- 2021 yılında yapılmış olan kategorileri  Game, gps or Home Theater dışında olanlar   
--- 2 küme olacak 1.2021 yılında üretilen ürünler 2.kategori tablomuz

select	*
from	product.product
where	model_year = 2021 and
		category_id NOT IN (
						select	category_id
						from	product.category
						where	category_name in ('Game', 'GPS', 'Home Theater')
						)

------ Alternatif yol : NOT IN yerin IN ,  IN yerinde NOT IN getirerek yapabiliriz

select	*
from	product.product
where	model_year = 2021 and
		category_id IN (
						select	category_id
						from	product.category
						where	category_name NOT in ('Game', 'GPS', 'Home Theater')
						)

"""
#####################################
"""
--- Soru: List products made in 2020 and its prices more than "all" products in the Receivers Amplifiers category
-- Ürün adı, model_yılı ve fiyat bilgilerini yüksek fiyattan düşük fiyata doğru sıralayınız.

--- 1. yol -- maximum liste fiyatını çekip 
select	*
from	product.product
where	model_year = 2020 and list_price >
(select	max(B.list_price)
 from	product.category A, product.product B
				where	A.category_name = 'Receivers Amplifiers' And
                        A.category_id = B.category_id
						)   ---  A.category_name = 'Receivers Amplifiers' deki en pahalı fiyat

---- 2. yol -- Eğer subquery tek değer döndürmüyorsa , IN, NOT IN , > ALL vs gibi şeyler kullanıyoruz

select * from	product.product
where	model_year = 2020 and
		list_price > ALL (
			select	B.list_price
			from	product.category A, product.product B
			where	A.category_name = 'Receivers Amplifiers' and
					A.category_id = B.category_id
			)

--- Burada çoklu satır döndürür subquery o yüzden ">" operatörünü kullanamayız. "> ALL" kullanmalıyız
--- Subquery den dönen bütün hepsinden büyük mü diye bakıyor.(97.13 den , 105 den büyük mü vs mi diye bakıyor)
-- 6 ürünümüz , bizim ürünümüzün bulunduğu kategorideki bütün ürünlerin fiyatlarından büyük
--- ALL () : Subquery içinden dönen tüm değerlerden büyük olan
"""
##############
"""
--- Soru: List products made in 2020 and its prices more than "any" products in the Receivers Amplifiers category
--- 1. yol -- minimum liste fiyatını çekip 
select	*
from	product.product
where	model_year = 2020 and list_price >
(select	min(B.list_price)
 from	product.category A, product.product B
				where	A.category_name = 'Receivers Amplifiers' And
                        A.category_id = B.category_id
						)   ---  A.category_name = 'Receivers Amplifiers' deki en pahalı fiyat

--- 2. yol
select * from	product.product
where	model_year = 2020 and
		list_price > ANY (
			select	B.list_price
			from	product.category A, product.product B
			where	A.category_name = 'Receivers Amplifiers' and
					A.category_id = B.category_id
			)

--- bizim ürünümüzün categorysindeki minimum fiyatı baz almamız lazım bunu "> ALL" yerine "> ANY" yazarak sağlayabiliriz
--- ANY () : Subquery içinden dönen herhangi bir değerlerden büyük olan


--- Burada SON 2 örnekte yukarda ki çözümlerden 1. yolu kullanmamız performans açısından daha iyi olacaktır
--- Bu bir text verisi ise ya da farklı tablolardan gelen UNION lardan oluşan bir veri setiyse
--- Yani group by la bir değer çıkartmanın mümkün olmadığı durumlarda 2. yolu kullanmalıydık
"""
# Common Table Expressions -- BIR SONRAKI DERS






