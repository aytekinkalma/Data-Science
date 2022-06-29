#%% SQL-7. ders_09.06.2022(session-6)

#%%SET OPERATIONS

# Birden fazla sorgunun tek bir sorgu sonucu olarak gözükmesi(Buna python da append diyebilirsiniz)
# 2 farklı sorgunun kesişimi, birleşimi vs gibi düşünebilirsiniz
# Satırları alt alta gelecek şekilde birleştirmek, aralarındaki farkı almak için
    # Veri tipleri aynı olmalı
    # Sütun sayıları aynı olmalı
    # Bütün işlemleri yaptıktan sonra ORDER BY ı  kullanabiliyoruz(VIEW de de izin vermiyordu mesela)

#######################################
# 1.UNION
# İki veri setini alt alta eklemeye yarar
# Karşımıza çıkan veri seti DISTINCT bir veri setidir. Aynı satırdan 1 den fazla olmaz
# ÖRNEK: SELECT emp_id, first_name, last_name, job_title from employees_A UNION SELECT emp_id, first_name, last_name, job_title from employees_B;
"""
TABLE_A      TABLE_B     TABLE_A UNION TABLE_B      
  A            C                    A
  B            D                    B
  C            E                    C
                                    D
                                    E

""" 
##################
"""
-- SORU: Charlotte şehrindeki müşterilerle aurora şehrindeki müşterilerin soyisimlerini listeleyin
-- Normalde set operater kullanmadan da yapabiliriz ama biz burada göstermek için kullanacağız

SELECT last_name FROM sale.customer WHERE city ='Charlotte'  --- 49 rows
UNION
SELECT last_name FROM sale.customer WHERE city ='Aurora'     --- 79 rows

-- SONUÇ: 105 rows geldi. UNION sorgu sonucunda DISTINCT bir küme döndürdü
-- NOT: Sorgu sonucu sıralı olarak geldi. SQL server da bir sorguda DISTINCT uygulandığında bu oluyor
"""
"""
# Sütun ismi değişirse? 
SELECT last_name FROM sale.customer WHERE city ='Charlotte'  --- 49 rows
UNION
SELECT last_name soyisim FROM sale.customer WHERE city ='Aurora'     --- 79 rows

-- Değişkenlerin sırası ve sayısı önemli, sütun ismini değiştirdiğimizde UNION ın üstündeki sütun ismini baz alır
"""
##################
"""
-- SORU:Çalışanların ve müşterilerin e-posta unique olacak şekilde listeleyiniz.
SELECT email FROM sale.staff     -- 10 rows
UNION
SELECT email FROM sale.customer  -- 2000 rows

-- 2004 rows
"""
#######################################
# 2.UNION ALL
# UNION gibi alt alta ekler ancak DISTINCT uygulamaz
# ÖRNEK: SELECT emp_id, first_name, last_name, job_title from employees_A UNION ALL SELECT emp_id, first_name, last_name, job_title from employees_B;
"""
TABLE_A      TABLE_B     TABLE_A UNION ALL TABLE_B      
  A            C                    A
  B            D                    B
  C            E                    C
                                    C
                                    D
                                    E
# UNION ALL Duplicate yaptı. UNION dan farkı bu. DISTINCT yapmadığı için performansı ve hızı daha iyi
# Ancak unique değerler istersek UNION kullanmalıyız
"""
##################
"""
-- SORU: Müşterilerin içinde Thomas isminde olanlar veya soyismi thomas olanları getirelim
SELECT first_name FROM sale.customer WHERE first_name ='Thomas'       -- 10 rows
UNION ALL
SELECT last_name soyisim FROM sale.customer WHERE last_name ='Thomas'  -- 27 rows

-- 37 rows
"""

#######################################
# 3.INSERSECT
# iki tabloyu karşılaştırıp 2 tablo sonucunda ortak(Kesişim) olanı döndürüyor

"""
TABLE_A      TABLE_B     TABLE_A UNION TABLE_B      
  A            B                    B
  B            D                    D
  D            E                    
""" 
##################
"""
-- SORU:brand ı getir, 2018 yılında herhangi bir ürünü ve 2019 yyılında herhangi bir ürünü olsn

-- Not INNER JOIN yerine altta tablo arasına virgül koyarak yazabiliyorduk
SELECT A.brand_id, B.brand_name FROM product.product A, product.brand B
WHERE a.brand_id = b.brand_id AND a.model_year = 2018   -- 177 rows
INTERSECT
SELECT A.brand_id, B.brand_name FROM product.product A, product.brand B
WHERE a.brand_id = b.brand_id AND a.model_year = 2019   -- 140 rows

--35 rows. NOT: Toplamda 40 marka vardı
"""
##################
#%% Dersin 2. bölümü
"""
-- SORU: 2018,2019 ve 2020 de sipariş veren müşterilerim?(Her 3 yılda da sipariş veren müşteriler)
SELECT A.first_name, A.last_name FROM sale.customer A, sale.orders B
WHERE A.customer_id = B.customer_id AND
		YEAR(B.order_date) = 2018   -- 635 rows
INTERSECT
SELECT A.first_name, A.last_name FROM sale.customer A, sale.orders B
WHERE A.customer_id = B.customer_id AND
		YEAR(B.order_date) = 2019   -- 688 rows
INTERSECT
SELECT A.first_name, A.last_name FROM sale.customer A, sale.orders B
WHERE A.customer_id = B.customer_id AND
		YEAR(B.order_date) = 2020   -- 292 rows
        
-- 14 rows
"""
"""
# Üstteki sorguda müşterilerin yaptıkları siparişleri görüntüleyelim
select	*
from
	(
	select	A.first_name, A.last_name, B.customer_id
	from	sale.customer A , sale.orders B
	where	A.customer_id = B.customer_id and
			YEAR(B.order_date) = 2018
	INTERSECT
	select	A.first_name, A.last_name, B.customer_id
	from	sale.customer A, sale.orders B
	where	A.customer_id = B.customer_id and
			YEAR(B.order_date) = 2019
	INTERSECT
	select	A.first_name, A.last_name, B.customer_id
	from	sale.customer A , sale.orders B
	where	A.customer_id = B.customer_id and
			YEAR(B.order_date) = 2020
	) A, sale.orders B
where	a.customer_id = b.customer_id and Year(b.order_date) in (2018, 2019, 2020)
order by a.customer_id, b.order_date
;
"""

# HOCA: Serdar ve Heagle hocanın sorularına cevap verelim EXCEPT' e geçmeden önce 
"""
-- SORU: AURORA VE CHARLOTTE  da YAŞAYAN KİŞİLERİN SOYISIMLERİ bu şehirlerde aynı soyisimli kişiler yaşıyor olabilir

SELECT last_name FROM sale.customer WHERE city ='Charlotte'
INTERSECT
SELECT last_name FROM sale.customer WHERE city ='Aurora'
---- 9 rows
-----

SELECT email FROM sale.staff
INTERSECT
SELECT email FROM sale.customer

---- Boş
"""

#######################################
# 4.EXCEPT
# A kümesinde olup B kümesinde olmamayan
"""
TABLE_A      TABLE_B     TABLE_A EXCEPT TABLE_B      
  A            B                    A
  B            C                    
  C            D                   
""" 
"""
-- SORU: 2018 de olan 2019 da olmayan brandleri getiriniz

SELECT A.brand_id, B.brand_name
FROM product.product A, product.brand B
WHERE A.brand_id = B.brand_id
    AND A.model_year = 2018
EXCEPT
SELECT A.brand_id, B.brand_name
FROM product.product A, product.brand B
WHERE A.brand_id = B.brand_id
    AND A.model_year = 2019;
    
# 2 rows. Sadece 2 marka bu şarta uyuyor.
"""
####################
"""
-- SORU: sadece 2019 da sipariş verilen diğer yıllarda sipariş verilmeyen ürünleri getiriniz

SELECT C.product_id, D.product_name FROM
(
SELECT B.product_id FROM sale.orders A, sale.order_item B
WHERE Year(A.order_date) = 2019 AND A.order_id = B.order_id
EXCEPT
SELECT B.product_id FROM sale.orders A, sale.order_item B
WHERE Year(A.order_date) <> 2019 AND A.order_id = B.order_id
) C, product.product D
WHERE C.product_id = D.product_id

-- 5 rows. Nested query ile product tablosunu birleştirip product_name i de getirdik
"""
####################
"""
-- SORU:brand ı getir, 2018 yılında herhangi bir ürünü ve 2019 yyılında herhangi bir ürünü olsn DEMİŞTİK INTERSECT te
. Şimdi  Bunların dışında kalan 5 ürünü bulmak istiyoruz

select	brand_id, brand_name
from	product.brand
except
select	*
from	(
		select	A.brand_id, B.brand_name
		from	product.product A, product.brand B
		where	a.brand_id = b.brand_id and
				a.model_year = 2018
		INTERSECT
		select	A.brand_id, B.brand_name
		from	product.product A, product.brand B
		where	a.brand_id = b.brand_id and
				a.model_year = 2019
		) A
"""
##################
"""
-- product_id ye göre 2019 yılında sipariş verilen diğer yıllarda sipariş verilmeyen ürünler
-- Bunu except ile yaptık. Bunu pivot table başka bir çıktıya bakalım. O 5 tane şart gösterdiğimiz de geldi
-- .. burada product_id ye göre bir nevi indexleme yaparak bunu da görüyoruz

SELECT *
FROM
			(
			SELECT	b.product_id, year(a.order_date) OrderYear, B.item_id
			FROM	SALE.orders A, sale.order_item B
			where	A.order_id = B.order_id
			) A
PIVOT
(
	count(item_id)
	FOR OrderYear IN
	(
	[2018], [2019], [2020], [2021]
	)
) AS PIVOT_TABLE
order by 1

"""
#######################################
# 5.CASE Expression
# Yeni bir sütun oluştururken başka bir sütunu referans gösteriyorsak kullanıyoruz
# Yeni sütunda, örneğin departmanda DS e , "Data science", diğerlerine "others" yazdırsın gibi...

###############################
# A.SIMPLE CASE
"""
CASE case_expression
     WHEN ...
     WHEN ...
     end give_table_name
from	table_1
"""
###########
"""
--- SORU: Generate a new columns containing what the mean of the values in the Order_Status column
--- 1.Pending 2.Processing 3.Rejected, 4.Completed
select	order_id, order_status,
		case order_status
			when 1 then 'Pending'
			when 2 then 'Processing'
			when 3 then 'Rejected'
			when 4 then 'Completed'
		end order_status_desc
from	sale.orders

-- order_status =1 ise bunu "Pending", 2 ise "Processing", 3 ,se 'Rejected', 4 se 'Completed' olarak yaz..
-- NOT: Bu kalıcı bir değişiklik yapmıyor tablolarda
-- DDL kodlarıyla tablomuza yeni alan ekleriz sonra bu sorguyla update ederiz bu değerler veritabanımızda kalır
"""

"""
--- SORU: Add a column to sale.staff table containing the store names of the employees
--- Bunu normalde kendimiz staff ve store kullanarak alabiliriz ama bunu CASE ile yapalım
--- 1.Davi techno Retail; 2.The BFLO Store 3.Burkes Outlet
SELECT first_name, last_name, store_id,
	CASE store_id
		WHEN 1 THEN 'Davi techno Retail'
		WHEN 2 THEN 'The BFLO Store'
		WHEN 3 THEN 'Burkes Outlet'
	END AS store_name
FROM sale.staff

-- Bu simple case di  sonra searched case e geçeceğiz
-- Burada 1 değişken var buna eşitliğine bakıyoruz 1 ise şunu yap, 2 ise şunu yap vs gibi
-- searched case de 0 ile 1000 arasındaysa şu, 1000 ile 2000 arasınysa şu ya da detaylı koşul varsa search case yapıyoruz
"""

##############################
# B.SEARCHED CASE
"""
--- SORU: Generate a new columns containing what the mean of the values in the Order_Status column
--- 1.Pending 2.Processing 3.Rejected, 4.Completed
select	order_id, order_status,
		case
			when order_status = 1 then 'Pending'
			when order_status = 2 then 'Processing'
			when order_status = 3 then 'Rejected'
			when order_status = 4 then 'Completed'
			else 'other'
		end order_status_desc
from	sale.orders
;

--- Bu "WHEN" kısımları Boolean bir değer döndürüyor gibi düşünebiliriz
--- Başka bir alternatif yok ama olsaydı else 'other' yazdırarak diğerlerine "other" yazdırabilirdik
"""
###############
"""
-- SORU:  MüşterilERİN e-mail adreslerindeki servis sağlayıcılarını yeni bir sütun oluşturarak belirtiniz.
--  gmail ise gmail, hotmail ise hotmail, yahoo ise yahoo, ... ,  diğerleri ise "other" yazdıralım

SELECT first_name, last_name,email,
	CASE
		WHEN email LIKE '%gmail%' THEN 'Gmail'
		WHEN email LIKE '%hotmail%' THEN 'Hotmail'
		WHEN email LIKE '%yahoo%' THEN 'Yahoo'
		ELSE 'Other'
	END AS email_service_provider
FROM sale.customer

-- '%gmail%'  : içinde gmail geçiyorsa
-- msn, outlook, aol gibi uzantılar 'other' a döndü

-- Not: oluşturduğumuz email_service_provider değişkeni/sutünu bir yerde oluşmadı. Kalıcı değil bu sorgu sonucu
"""
##################
"""
-- Soru: Aynı siparişte hem mp4 player, hem Computer Accessories hem de Speakers kategorilerinde ürün sipariş veren müşterileri bulunuz.
-- Önce bu kategoriler veritabanında nasıl yazılıyor bakalım
select * from product.category
---'Computer Accessories'
---'Speakers'
---'mp4 player'

Select * from product.category A, product.product B, sale.order_item C
WHERE A.category_name in ('Computer Accessories','Speakers','mp4 player') AND
A.category_id = B.category_id AND
    B.product_id = C.product_id

--- Eğer set operationları kullansaydık farklı 
--- her bir order_id için belirtilen ürünlerden en az 1 tane almış olmasına bakıyorum
--- her bir order_id ye göre gruplama yapacağız
--- Sonra herbir order_id içinden farklı category id sini saydıracağım

select	c.order_id, count(distinct a.category_id) uniqueCategory
from	product.category A, product.product B, sale.order_item C
where	A.category_name in ('Computer Accessories', 'Speakers', 'mp4 player') AND
		A.category_id = B.category_id AND
		B.product_id = C.product_id
group by C.order_id
having	count(distinct a.category_id) = 3
;

--- her bir order_id için bir sonuç geldi.
--- 1: Tek kategoryden sipariş verilmiş
--- 2: 2 farklı kategoryden sipariş verilmiş
----3: --> Bize bu 3 lazım bunu da HAVING ile belirttik
--- Bir de bu siparişi veren kişilerin isim soyisimleri alalım. Bunu nested query yapıp isimleri getirelim
--- sipariş nodan siparişi veren kişilere gideceğiz 

--- sipariş veren müşterileri bulalım
select	C.first_name, C.last_name
from	(
		select	c.order_id, count(distinct a.category_id) uniqueCategory
		from	product.category A, product.product B, sale.order_item C
		where	A.category_name in ('Computer Accessories', 'Speakers', 'mp4 player') AND
				A.category_id = B.category_id AND
				B.product_id = C.product_id
		group by C.order_id
		having	count(distinct a.category_id) = 3
		) A, sale.orders B, sale.customer C
where	A.order_id = B.order_id AND
		B.customer_id = C.customer_id
;
"""
#########################
"""
Yukardaki sonucu başka nasıl alabilirdik
--- hoca gönderecek
"""























