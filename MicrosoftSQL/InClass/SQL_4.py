#%% 4.Ders
# Dersin 1. bölümü
# Bugün konumuz fonksiyonlar

# Table of Contents
# 1. Date functions
# 2. String functions
# 3. Other functions 

#%%
# Temel kavramları bize hatırlayalım
"""
# /*     */  : Yorum açmak için kullanılır .
# iki tire ard arda(--) : Bu da yorum açmak için kullanılır

/* SELECT
FROM
WHERE 
ORDER BY
TOP
    */ 
"""
# Yukarıdaki komutları yavaş yavaş kullanacağız
# Sample Retail database in de çalışacağız

"""
# Brand tablomuza bakalım

SELECT * FROM product.brand
ORDER BY brand_name

# 2 sütun , 40 satırlık veri var. Bunu istediğimiz sıraya koyduk ORDER BY ile (Ascending)
"""
######################
"""
SELECT * FROM product.brand
ORDER BY brand_name DESC

# Bu da azalan şekilde
"""
######################
# TOP
"""
SELECT TOP 10 * FROM product.brand
ORDER by brand_id DESC

# Büyük tablolarda TOP 10 kullanırız, pandastaki head() gibi düşünebiliriz
"""
######################
# WHERE : Istediğim kriterler için koşul gireceğim
"""
SELECT * FROM product.brand
WHERE brand_name LIKE 'S%'

# S%: brand_name i S ile başlayan satırları getir
"""
######################
"""
# product tablosuna bakalım

# product_id --> primary key -> 1.Unique 2.Non-Null
# product_name --> aynı isme sahip productlar var -- ÖRN: satır 409-410-411
# Ama bunlar farklı ID ile ifade edilmiş
# List price ları farklı olduğu için farklı ID ile ifade edilmiş
# Farklı nedenlerden dolayı da olabilir

# Brand_id ve category_id var yine tables- columns- altında
# Bunlarında foreign key olduğunu biliyoruz
"""
######################
"""
SELECT * FROM product.product
WHERE model_year BETWEEN 2019 AND 2021

"""
######################
"""
# Çok büyük tablolarda min ya da max değeri görmez için ORDER BY ASC/DESC kullanabiliriz

SELECT TOP 1 * FROM product.product
WHERE model_year BETWEEN 2019 AND 2021
ORDER BY model_year DESC

"""
######################
"""
SELECT * FROM product.product
WHERE category_id IN (3,4,5)

# 3 numaralı ya da 4 numaraları ya da 5 numaralarınu alan category_id yi getirdik
"""
######################
"""
# 2. yol . Üstteki ile aynı çıktı gelecek

SELECT * FROM product.product
WHERE category_id=3 OR ategory_id=4 OR ategory_id=5

"""
######################
"""
# Yukardakiler için 3,4,5 in haricindekiler

SELECT * FROM product.product
WHERE category_id NOT IN (3,4,5)
"""
######################
"""SELECT * FROM product.product
WHERE category_id NOT IN (3,4,5)
"""
######################
"""
# 2. yol . Üstteki ile aynı çıktı gelecek

SELECT * FROM product.product
WHERE category_id <> 3 AND ategory_id <> 4 AND ategory_id <> 5

<> : "Eşit değildir" anlamında , Ayrıca
!= : "Eşit değildir" anlamında bu da
"""
######################
"""

SELECT * FROM product.stock

# Bu tablo neyi anlatıyor bana? Store ile product ın ilişkisi
# Hangi mağaza hangi ürünün stock u var
# Primary key hangi sütun olmalı ? 
# store_id ve product_id birlikte primary key olmalı
# Çünkü store_id ve quantity yi yanyana koysam bu iki sütun net bir bilgi veremiyor
# product_id ile quantity yi yanyana koysam 1. numaraları product ın quantitileri farklı ama net bir bilgi
# .. alamıyorum yine. product_id neden çoklamış, quantity neyin miktarı vs? Bu tabloyu okuyamıyoruz böyle
# .. O yüzden 2 sütun(product_id, store_id) bir olup composite primary key oldu
"""

#%% # Dersin 2. bölümü
##################################################################
# Date Functions
"""
Data types
time              : saat verisi varsa
date              : tarih verisi varsa
smalldatetime     : tarih ve saat verisi birlikte
datetime          : tarih ve saat verisi birlikte
datetime2         : tarih ve saat verisi birlikte
datetimeoffset

"""
######################
# GETDATE() : Sisteminizin o anlık saatini datetime data tipinde getirir
"""
CREATE TABLE t_date_time (
	A_time time,
	A_date date,
	A_smalldatetime smalldatetime,
	A_datetime datetime,
	A_datetime2 datetime2,
	A_datetimeoffset datetimeoffset
	)

# "t_date_time isminde" bir tablo oluşturduk
# 6 tane sütunu var. Her sütunun veritipi fatklı
# Şimdi inceleyelim
"""
######################
"""
SELECT * from t_date_time

# Şu an boş. 

SELECT GETDATE() as get_date
# Tarih saat ve nanosecond sonuç döndürdü

# Insert yapalım yukarda oluşturduğumuz tabloya

INSERT t_date_time
VALUES (GETDATE(),GETDATE(),GETDATE(),GETDATE(),GETDATE(),GETDATE())

# Her bir sütun için GETDATE() insert ettik
# Her sütun kendi veritipine uygun şekilde yazdırdı
"""
######################
"""
INSERT t_date_time (A_time, A_date, A_smalldatetime, A_datetime, A_datetime2, A_datetimeoffset)
VALUES
('12:00:00', '2021-07-17', '2021-07-17','2021-07-17', '2021-07-17', '2021-07-17' )

# "time" formatına uygun şekilde values un ilk değerini saat şeklinde yazdık, diğerlerine sadece tarih girelim
# Kendi formatlarına uygun çıktı getirdiler yine
"""
#######################
# Farklı ülkelerin veya farklı kullanım amaçlarına göre tarih stillleri var
# Her bir stilin kodu var (1,2,3,4,5,6,7,(8 veya 108))
# Verinizdeki tarih formatı bize uygun değilse bu still ile değiştirebiliriz.
# Örnek yapalım
"""
SELECT CONVERT(VARCHAR, GETDATE(), 6)   # GETDATE() i varchar a dönüştürdük. Still kodu 6 yani burada 6 görmek istediğimiz format

SELECT CONVERT(DATE, '25 Oct 21', 6)    # Varchar ı date e dönüştürdük
"""
#######################
"""
# Farka bakalım dönüştürmeden önce ve sonra

SELECT GETDATE()
SELECT CONVERT (VARCHAR(10), GETDATE(), 6)

# target_dtype : (VARCHAR(10) : Veri tipi
# GETDATE()    : Dönüştürmek istediğim değer
# 6            : "Date only format tablosundaki" Dönüştürmek istediğim stil no 
"""
#######################
"""
SELECT CONVERT(DATE, '25 Oct 21', 6) 

# target_dtype : DATE : Veri tipi
# '25 Oct 21'  : Dönüştürmek istediğim değer
# 6            : "Date only format tablosundaki" Dönüştürmek istediğim stil no 
"""
# NOT: convert ü varchar ı integer a ya da integer ı varchar a convert etmek için kullanıyoruz

############################################
# Return Date or Time Parts
# Date ten istediğimiz parçaları alacağız
"""
FUNCTION         SYNTAX                         RETURN DATA TYPE
------------------------------------------------------------------
DATENAME        DATENAME(datepart, date)           nvarchar
DATEPART        DATEPART(datepart, date)            int
DAY             DAY(date)                           ...
MONTH           MONTH(date)                         ...
YEAR            YEAR (date)                         ...
"""
########################
"""
SELECT A_DATE
		, DAY(A_DATE) DAY_
		, MONTH(A_DATE) [MONTH]
		, DATENAME(DAYOFYEAR, A_DATE) DOY
		, DATEPART(WEEKDAY, A_date) WKD
		, DATENAME(MONTH, A_DATE) MON
FROM t_date_time

# Burada fonksiyonlar (Python daki built-in gibi olduğu için) isim verirken DAY sonuna alt tire
# .. ya da MONTH u köşeli parantez içine alarak fonksiyon rengi pembeye dönmeden sütuna bu şekilde
# .. isim atayabiliriz)
"""
################################################
# Return Date and Time Difference Values
# DATEDIFF: 2 zaman arasındaki farkı alacağız(gün farkı, dakika farkı, saat farklı vs)
"""
FUNCTION         SYNTAX                                      RETURN DATA TYPE
------------------------------------------------------------------
DATEDIFF        DATEDIFF(datepart, startdate, enddate)            int
"""
########################
"""
SELECT DATEDIFF(DAY,'2022-05-10',GETDATE())

# şu anki zaman ile 2022-05-10 arasındaki güm farklı nı
"""
########################
"""
SELECT DATEDIFF(SECOND,'2022-05-10',GETDATE())
"""
################################################
# Modify Date And time values

"""
FUNCTION         SYNTAX                                      RETURN DATA TYPE
------------------------------------------------------------------
DATEADD    DATEADD(datepart, number, date)     the date type of the date argument 
EOMONTH    EOMONTH(start_date [,month_to_add]) return type is the type of the start_date argument, or alternately, the date data type

# DATEADD : belirtiğimiz zamana eklemek istediğimiz değer
# EOMONTH : ayın son gününü verir
# Örnek yapalım
"""
########################
"""
SELECT DATE(DAY,5,GETDATE())     # Bu günden itibaren 5 gün ekledi
SELECT DATE(MINUTE,5,GETDATE())
"""
########################
"""
SELECT EOMONTH(GETDATE())
SELECT EOMONTH(GETDATE(),2)

# Bulunduğumuz aydan, 2 ay sonrasının, son günü
"""
########################
"""
# Veritabanımızdan örnek yapalım

SELECT * FROM sale.orders

# Burada bazı tarihler var burada
"""

#%% Dersin 3. bölümü
########################
"""
# Her bir sipariş için sipariş tarihi ve kargolama tarihi arasındaki farkı GÜN cinsinden bulalım

SELECT *, DATEDIFF(DAY, order_date, shipped_date) Diff_of_day
FROM sale.orders
"""
########################
"""
# Her bir sipariş için sipariş tarihi ve kargolama tarihi arasında 2 günden fazla geçenler

SELECT *, DATEDIFF(DAY, order_date, shipped_date) Diff_of_day
FROM sale.orders
WHERE DATEDIFF(DAY, order_date, shipped_date) > 2

# 463 rows geldi
"""
########################
"""
SELECT *
FROM sale.orders
WHERE DATEDIFF(DAY, order_date, shipped_date) > 2

# Böyle yapsaydık Diff_of_day sütunu gözükmezdi ama kod çalışırdı
# Tekrardan 463 rows
"""

#########################################################
# Bir ifadenin gün formatına uygun olup olmadığına bakar
"""
FUNCTION         SYNTAX    
ISDATE           ISDATE(EXPRESSION)
"""

#########################################################
# STRING FUNCTIONS
# 1.Character strings Data types
# 2.String functions
# 3.Related Topics

# String functions
# LEN(input_string)                          : karakter  uzunluğu
# CHARINDEX(substring, string[,start_location])   : Karakterin indexi, örn: ahmet te "H" harfi kaçıncı karakter
# PATINDEX('%pattern%', input_string)        : Bir patern aradığımız zaman örn: Bir sütunda "h" ve "m" harflerinin yan yana olduğu pattern i aramak istersek

"""
SELECT LEN ('CHARACTER ')                # Output : 10  # çünkü boşluk var burada onu da karakter olarak sayıyor
SELECT CHARINDEX('R','CHARACTER')        # Output : 4   # Kelime içerisinde "r" nin indexini bulalım 
SELECT CHARINDEX('R','CHARACTER',5)      # Output : 9   # Saymaya 5 ten başla. 5 ten başladığı için ilk "R" yi atladı ve ikinci "R" nin indexini yazdı
SELECT CHARINDEX('RA','CHARACTER',5)
SELECT CHARINDEX('RA','CHARACTER',5) -1  # Output : 9: # Saymaya 5 ten başla. (Aslında) burada 2. "R" den bir önceki karakterin index numarasını getirdi
SELECT PATINDEX('%R', 'CHARACTER')       # Output : 9 # R ile biterse "R" nin indexi
SELECT PATINDEX('%H%', 'CHARACTER')      # Output : 2
SELECT PATINDEX('%A%', 'CHARACTER')      # İlk A yı aldık(2 tane A var)
SELECT PATINDEX('__A______', 'CHARACTER') # A dan önce 2, A dan sonra 6 karakter olan bir pattern var mı?
SELECT PATINDEX('__A%', 'CHARACTER')      # Output : 1
SELECT PATINDEX('____A%', 'CHARACTER')    # Output : 1  
SELECT PATINDEX('%A____', 'CHARACTER')    # Output : 5   # 2. A nın indexini getirdi
# %R  : Burada yüzde; sayısını bilmediğim kadar karakter
# NOT: charindex fonksiyonunda indexlemeye 1 den başlıyor
"""

######################################
# LEFT()      : Soldan istediğimiz kadar karakter almamıza yarar
# RIGHT()     : Sağdam istediğimiz kadar karakter almamıza yarar
# SUBSTRING() : BAşlangıç ve bitiş karakterini vererek  sağdan,soldan veya ortadan istediğimiz kadar karakter almamıza yarar

"""
SELECT LEFT('CHARACTER',3)
SELECT RIGHT('CHARACTER',3)
SELECT SUBSTRING('CHARACTER',3,5)  # Output: ARACT  # 3 ten başla , 5 karakter al
SELECT SUBSTRING('CHARACTER',4,9)  # Output: RACTER # 4 ten başla, 9 karakter al(ama 4 ten sonra 9 karakter alamadığı için sonuna kadar aldı)

"""

######################################
# LOWER()      : Küçük harfe döndürür
# UPPER()      : Büyük harfe döndürür
# STRING_SPLIT : A table-value function: Öncekiler(Yukarıdakiler) tek bir değer döndürüyordu, A table-value function bir tablo döndürecek

"""
SELECT LOWER('CHARACTER')   # output : character
SELECT UPPER('character')   # output : CHARACTER
SELECT * FROM STRING_SPLIT('jack,martin,alain,owen', ',')              # Buradaki her bir ismi tek bir sütunda tablo kaydı olarak döndürdük
SELECT value FROM STRING_SPLIT('jack,martin,alain,owen', ',')          # value ile de tablonun değerlerini yakalayabiliriz
SELECT value as name FROM STRING_SPLIT('jack,martin,alain,owen', ',')  # sütun ismi "name" oldu

# NOT: Burada virgül: "ayırt edici değer"
"""

"""
# ÖRNEK : 'character' kelimesinin ilk harfini büyüten bir script yazınız

SELECT UPPER(LEFT('character',1))+(RIGHT('character',8))
SELECT UPPER(LEFT('character',1)) + LOWER(SUBSTRING('character',2,9))  # Eğer burda tek string yerine bir sütun olsaydı,
# ..  9 yerine her bir string için farklı değer girmem gerekirdi. Çözüm;
SELECT UPPER(LEFT('character',1)) + LOWER(SUBSTRING('character',2,LEN('character')))
# Concat ile bakalım
SELECT CONCAT UPPER(LEFT('character',1)) , LOWER(SUBSTRING('character',2,LEN('character')))
# DIKKAT: Arada artı yerine virgül var burada
"""

################################################ END ########################################################




