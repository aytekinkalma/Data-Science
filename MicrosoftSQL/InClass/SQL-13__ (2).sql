--SQL-13. ders_20.06.2022(session-12)

-- DATABASE INDEX

-- Bir tabloda belli alanlara yapýlan sorgular daha fazla ise
-- .. ( Mesela: Kiþi tablosunda sürekli isim üzerinden sotgu yapýlýyor)
-- .. Bu alanlara index atýyorsunuz. Bize fayda saðlýyor
-- .. Indexler database seviyesinde oluyor. Yani DB deki bütün sütunlara index atalým diyemiyoruz
-- NOT: Primary key ler ve foreign key ler de birer indextir aslýnda
-- Management studioda bir sorgu yazdýktan sonra bu sorgu ne kadar sürüyor bunun için bir yapý sunuyor
-- .. Bu bilgiye göre tablo ya da sorgularýnýzý deðiþtirebilirsiniz

-- Burada 2 temel terim var. SCAN, SEEK
-- Scan : SQL server sorguya bakýp bu kriter hangi satýrlarda var ona bakýyor. Yani Full scan yapýyor.
-- .. Bu yavaþ metodtur ama her zaman doðru sonuç getirir
-- Seek : Indexleri koyduktan sonra dict mantýðýyla ilgili yeri bulur
-- .. Index seek : 1.Clustered 2.Non-clustered
-- a.Clustered Index: Belirli bir sütun üzerinde oluþturmuþ olduðunuz cluster indexte SQL o sorgusunda
-- .. o alana nerede ise o alana(kümeye) gidiyor hýzlýca buluyor. Her bir tabloda tek bir clustered index
-- .. olabiliyor. Çünkü sýralama belli bir sütuna göre yapýldýysa, diðer sütunlar o sýralanan sütuna göre 
-- .. sýraya gireceði için tek bir clustered index oluyor. (B-tree mantýðýyla çalýþýr)

-- Örnek kod
-- CREATE CLUSTERED INDEX index_name ON schema_name.table_name (column_list);
-- Bunu çalýþtýrýnca bir "VIEW" mantýðýyla DB de bir nesne oluþuyor

-- b.Non-Clustered Index: Bir tabloda clustered index oluþturdunuz. Sonra farklý alanlara da index oluþturmak istiyorsunuz
-- .. Bunlar non-clustered indexler olacaktýr. Birden fazla tabloda non-clustered index oluþturulabiliyor ve 2 den fazla
-- .. sütun üzerinde non-clustered index oluþturulabiliyor.(B-tree yapýsý burada da geçerli)

-- ADVANTAGES AND DISADVANTAGES
-- ADVANTAGE    : 1.Hýz, 2.sýralama 3.Unique indexes guarantee
-- DISADVANTAGES: 1.INSERT, UPDATE and DELETE becomes slower, 2.Disk alanýnda yer kaplar

--önce tablonun çatýsýný oluþturuyoruz.
create table website_visitor 
(
visitor_id int,
ad varchar(50),
soyad varchar(50),
phone_number bigint,
city varchar(50)
);

-- veri insert edelim while döngüsünde 1 den 200000 e kadar
DECLARE @i int = 1
DECLARE @RAND AS INT
WHILE @i<200000
BEGIN
	SET @RAND = RAND()*81
	INSERT website_visitor
		SELECT @i , 'visitor_name' + cast (@i as varchar(20)), 'visitor_surname' + cast (@i as varchar(20)),
		5326559632 + @i, 'city' + cast(@RAND as varchar(2))
	SET @i +=1
END;

-- Tabloyu kontrol edelim
SELECT top 10*
FROM
website_visitor

-- indexleri oluþturdunuz diyelim. Ama zaman içinde tabloda deðiþiklikler oldu diyelim.
-- SQL server sorgular arasýnda yönlendirme yapabilir. Yönlendirme yapabilmesi için bu istatistikleri kullanýr
-- Biz bu istatistikleri kapatýp açabiliyoruz. Biz bu istatistikleri açalým
--Ýstatistikleri (Process ve time) açýyoruz, bunu açmak zorunda deðilsiniz sadece yapýlan iþlemlerin detayýný görmek için açtýk.
SET STATISTICS IO on
SET STATISTICS TIME on

-- basit bir sorgu yapalým.
select * from website_visitor where visitor_id = 100 -- Burada 200000 satýrý taradý

-- MS-SQL server da sorgumuzu seçip Execute ýn saðýnda "V" iþareti var onunda saðýndakine(execution plan) týklayalým
-- Çýktýda bazý þeyler geldi onlarýn üzerine mouse la geldiðimizde bilgiler görünüyor
-- Select Coat: .. 
-- Table scan: Kullanmýþ olduðu yöntem. Bu ekranda en üstte. (Cluster yapýnca burasý "Clustered Index seek" olacak)
-- .. "Estimated number of rows to be read-->199999",
-- .. "Estimated number of execution -- 1" 
-- .. vs vs
-- 2 sorguyu karþýlaþtýrmak için bunu kullanabilirsiniz

-- Dersin 2. bölümü

-- Tabloda index oluþturalým

Create CLUSTERED INDEX CLS_INX_1 ON website_visitor (visitor_id);
-- CLS_INX_1          : Index adý. NOT: Index adý DB içinde unique olmalý
-- ON website_visitor : website_visitor tablosu üzerinde tanýmlandý
-- (visitor_id)       : Hangi alana uygulanacaðý
-- Object Explorer da -- > tables - dbo.website_visitor -- > Indexes -- > CLS_INX_1(Clustered) ... Oluþmuþ

-- Indexi attýk artýk SQL server visitor ID lerin nerede olduðunu biliyor. Artýk sorgu daha hýzlý gelecektir
select * from website_visitor where visitor_id = 100 -- Burada 200000 ýn hepsini okumadý
-- sorguyu seçip yine "execution plan" a týklayalým. Çýktýda "Clustered_Index seek" geldi
-- Not: Eðer tablolar çok büyükse mutlaka index atmamýz gerekiyor.

-- visitor_id de index var þu an tekrar bir index oluþturursak bu artýk clustered index olmayacak bu non-clustered index olacak
select ad from website_visitor where ad = 'visitor_name17'; -- 200000 satýrý okudu yine
-- "execution plan"a bakalým
-- Peki bu alana index nasýl atacaðýz(Non-cluster)
CREATE NONCLUSTERED INDEX ix_NoN_CLS_1 ON website_visitor (ad);
-- "execution plan"a bakalým. Index seek. Artýk en alttaki "leaf" leri okumak zrounda deðil(B-tree de)
-- .. index içerisindeki ismi bulmaya çalýþýyor. Sonra sonucu getiriyor.

 --------------------------------------
-- Ýsim ve soyisme beraber index atalým.(Ayný isim soyisme ait baþka bir kiþi olmadýðý için)
Create unique NONCLUSTERED INDEX ix_NoN_CLS_2 ON website_visitor (ad) include (soyad)
-- Artýk isim ve soyisme beraber gönderilen planda ne olacak bakalým 
select ad, soyad from website_visitor where ad = 'visitor_name17';
-- "execution plan" a göre indexe göre arama yaptý. Extra isim soyisim üzerinde arama yapmadý

--------------------------------------
-- clustered index (visitor_id)
-- non-clustered index (ad)
-- non-clustered index (ad) include (soyad)
-- Üsttekileri yaptýk. Peki sadece soyadý üzerinden sorgu yapsaydý
select ad, soyad from website_visitor where soyad = 'visitor_name17'; -- çýktý yok ama execution plana bakmak için böyle yazdýk
-- execution plan "Index scan" yani tablonun hepsini kontrol ediyor Yani "index seek" yapmadý


-- Dersin 3. bölümü

-- Python üzerinden SQL server a baðlanma
-- ipynb. dosyasý üzerinde notlar var
