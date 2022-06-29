#%% SQL-3. ders_03.01.2022_ LAB DERSI

# Bugün ders planımız:
# 1.Built-in functions (kalınan yerden devam)
# 2.Joins & Views
# Sample Retail üzerinde çalışacağız

#%%  # DERSIN 1. BÖLÜMÜ
##############################################################
# TRIM(), LTRIM(), RTRIM()
# TRIM fonksiyonu: Özellikle text datalarda bir hücredeki girdinin bazen başında ya da sonunda boşluklar olabiliyor
# .. Bunlar bazen eşitlemede, sorguda ya da join vs yaparken sorun çıkartabiliyor.
# O yüzden verideki başında ve sonundaki boşlukları temizleyen fonksiyondur bu
# LTRIM(): Sadece solundaki boşlukları siler
# RTRIM(): Sadece sağdaki boşlukları siler
"""
     Function Syntax                                                Description
TRIM([removed_characters, from] input_string)   ---->   Return a new string from a specified string after removing all leading and trailing blanks or characyers
LTRIM(input_string)                             ---->   Return a new string from a specified string after removeing all leading blanks
RTRIM(input_string)                             ---->   Return a new string from a specified string after removeing all trailing blanks
"""

"""
SELECT ' CHARACTER';
# CHARACTER yazısının başında boşluk var, çıktıda hala görünüyor
"""
######################
"""
SELECT TRIM(' CHARACTER');
# CHARACTER yazısının başında boşluk var, çıktıda gitti
# Bu sorgu Tablolarda kalıcı değişiklik yapmaz(Select ile kullandığım için. Update, Delete vs de kalıcı değişiklik oluyordu)
"""
######################
"""
SELECT GETDATE();
# Sistem tarihi ve zamanını getiriyor
"""
######################
# sampleretail -- Programmability--functions-system functions -- string functions
# Burada çıkanlar tanımlanmış fonksiyonlardır, en alt satırlarda TRIM fonksiyonunu görüyoruz
# .. SQL server içerisinde bu TRIM tanımlanmış
# Parameters : Varchar bir değer döndürür

"""
# Başka örnekler
SELECT TRIM(' CHARACTER ')
SELECT TRIM(        '       CHAR ACTER ')  # Tek tırnaktan önce yazılan boşlukların anlamı yok, tırmaktan sonra text ifadenin başladığını biliyor fonksiyon

"""
# TRIM in başka bir kullanımına bakacağız;
"""
SELECT TRIM('X' FROM 'ABCXXDE')             #  Output  : ABCXXDE
SELECT TRIM('X' FROM 'XXXXXXXABCXXDEXXXXX') #  Output  : ABCXXDE
# Yani baş ve sona bakıyor sadece
"""

"""
SELECT TRIM('ABC' FROM 'CCCCBBBAAAFRHGKDFKSLDFJKSDFACBBCACABACABCA') # Output : FRHGKDFKSLDFJKSDF
# 'ABC' : Hem A yı Hem B yi Hem C yi kes diyoruz burada
"""
# ARA NOT: Db oluştururken database in case sensitive olup olmadığını ayarlayabiliyoruz

# LTRIM(), RTRIM()
"""
SELECT LTRIM ('     CHARACTER ')   # Sadece soldaki boşluklar gitti çıktıda
SELECT RTRIM ('     CHARACTER ')   # Sadece sağdaki boşluklar gitti çıktıda
"""
##############################################################
# REPLACE(), STR()
# Replace: Bir textin içerisindeki ifade yerine başka bir ifade yazmamızı sağlar
# Str: Nümerik sayının string e çevrilmesini istersek kullanıyoruz

# REPLACE
"""
SELECT REPLACE('CHARACTER STRING', ' ', '/')  # 'CHARACTER STRING' içinde Boşluk varsa, bunu slash(/) ile değiştir # output: CHARACTER/STRING
SELECT REPLACE('CHARACTER STRING', 'CHARACTER STRING', 'CHARACTER')     # Output: CHARACTER
# 'CHARACTER STRING' içinde 'CHARACTER STRING' varsa, bunun 'CHARACTER' ile değiştir dedik
"""
# STR
"""
SELECT STR (5454)                   # Output:       5454  # Output da dtype: Text # NOT: başına 6 boşluk ekleyip sonra texte çevirdi
# NOT: String fonksiyonu bize 10 karakterlik text döndürüyor. Mesela 10 dan fazla yazarsak
SELECT STR(1234567890123456)        # Output: **********  # 10 karakter döndürmek yerine SQL çıktı vermenin mantıksız olacağını düşünüp 10 tane * veriyor
SELECT STR (2135454654)             # Output: 2135454654  # Output da dtype: Text           
SELECT STR (133215.654645, 11, 3)   # Output: 133215.655  # Toplam 11 karakter olsun(boşluklarla vs), 3 karakterde virgülden sonra olacak
# NOT: Sonu 655 geldi çünkü sondaki 4 ü 5 e yuvarladı
"""
################################################################
# CAST()    : Bir ifadenin başka bir veritipine dönüştürülmesini sağlıyor. Mesela text ile numeric i concat ederken işe yarıyor
            ###### Örnek: SELECT 'customer' + '_' + CAST(1 AS VARCHAR(1)) AS col;
# CONVERT() : Tanımlanmış cast işlemleri. Tarih veriyorum. Bunların içinden  belii parçasını getir. Veri tipini döndürmeyede yarar. Örneklerde göreceğiz

"""
SELECT CAST (12345 AS CHAR)  # Gördüğü şeyi(12345) string e çevirdik   # Output: 12345
SELECT CAST (123.65 AS INT)  # float ı integer a çevirdi               # Output: 123

SELECT CONVERT(int, 30.60)                 # integer veritipinde bir sonuç istiyoruz       # output: 30
SELECT CONVERT (VARCHAR(10), '2020-10-10') # VARCHAR(10) veritipinde bir sonuç istiyoruz   # output:2020-10-10 : dtype:text
# CONVERT özellikle tarih veritiplerinde kullanırız, 
SELECT CONVERT (DATETIME, '2020-10-10')   # DATETIME veritipinde bir sonuç istiyoruz      # output: 2020-10-10 00:00:00:000
SELECT CONVERT (NVARCHAR, GETDATE(),112)  # NVARCHAR veritipinde bir sonuç istiyoruz      # output: 20220606
# Convertte, Cast ten farklı olarak önceden tanımlanmış fonksiyonlar var
# GETDATE() sonucunu al NVARCHAR a çevir, 112 formatında(YYYYMMDD) texte çevir   
SELECT CAST ('20201010' AS DATE)              # output:
SELECT CONVERT (NVARCHAR, CAST ('20201010' AS DATE),103 ) # integer veritipinde bir sonuç istiyoruz  # output:

# NOT: Yazdığımız sorgunun veritipini görme ;
# .. Sorgunuzu tablo olarak create edip sonrasında sp_help 'dbo.table_name' yazdığınız zaman görürüz
"""
# DERSIN 2. BÖLÜMÜ
################################################################
# COALESCE
# Bir takım girdileriniz var bazılarını boş olabilir. Siz ilk dolu olanı almak istediğinizde kullanıyorsunuz
"""
SELECT COALESCE(NULL,'Hi','Hello',NULL)  # En az 2 parametre atamalıyız parantez içine,  # Output: Hi
"""

################################################################
# NULLIF
# 2 değer var bu değerlerin birbirine eşit olup olmaması. Eşitse boş değer döbdürmesini, eşit değilse ilk
# .. dolu olanı getirmesini istersek bu fonksiyonu kullanıyoruz
"""
SELECT NULLIF (10,10)    # Output: NULL
SELECT NULLIF (10,11)    # Output: 10
"""

################################################################
# ROUND()     : Float veritipinde virgülden sonra Round diyerek yuvarlayabilmemizi sağlar
# ISNULL()    : 2 parametre yazacağız mesela birinci parametre boşsa ikinci parametreyi getirecek
        ####### ÖRN: Öğrenci yaş ortalamasını al diyeceğiz mesela. NULL olmayan değerlerin ortalamasını al derken bunu kullanacağız.
# ISNUMERIC() : Tablo içerisinde değerleri ortalama işlemine dahil etmek istiyorsunuz ama içerde karakterler içerde karışmış olabilir
# .. bundan önce bu veri nümeric mi değil mi derken bu fonk. kullanıyoruz
"""
SELECT ROUND (432.368, 2,0)  # output: 432.370 # Virgülden sonraki 2 karaktere göre yuvarla
# Buradaki 0 : 0 ya da 1 değer alıyor
# default olarak 0 alıyor yukarı yuvarlar. 0 ı yazmasakta olur
# 1 yazarask aşağı yuvarlar
"""
######################
"""
SELECT ISNULL(NULL, 'ABC')   # output: ABC
SELECT ISNULL('', 'ABC')     # output: (Boş geldi)  # Dikkat: burada ilk parametre NULL DEĞİL
"""
######################
"""
SELECT ISNUMERIC(123)      # output: 1  # 1:True
SELECT ISNUMERIC('ABC')    # output: 0  # 0:False
"""

#%% ################################################################################################################################
# JOINS
# TABLE OF CONTENTS
# Introduction to Joins
    # JOIN: Birden fazla tablonun birleştirilmesi. Ona göre sorgu yazacağız
# INNER JOIN  : 2 tane tabloda ortak olan satırları döndürür
    # 2 tabloyu bir condition ile;    
        # SELECT COLUMNS FROM table_A INNER JOIN table_B ON join_conditions
        # join_conditions: Mesela 1. tablodan gelen TC ile 2. tablodan gelen TC lerinin eşit olanları getir
    # Birden fazla tabloyu conditionlar ile join etmek istersek;
        # SELECT COLUMNS FROM table_A INNER JOIN table_B ON join_conditions1 AND join_conditions2 INNER JOIN table_C ON join_conditions3 OR join_conditions4 ...
"""
# Soru: Select product ID, product name, category ID and category name and make join example 
SELECT	A.product_id, A.product_name,
		B.category_id, B.category_name
FROM	product.product AS A
INNER JOIN product.category AS B
on A.category_id = B.category_id
"""

# DERSIN 3. BÖLÜMÜ
"""
# Soru: List employees of stores with their store information. select employee name, surname, store names
SELECT	A.first_name, A.last_name,
		B.store_name
FROM	sale.staff AS A
INNER JOIN sale.store AS B
on A.store_id = B.store_id

# NOT:Bu 2 tablo arasında ilişki olmak zorunda değil ,örneğin staff ile customer tablosunda last_name e göre join yapabiliriz
# .. ve bunlar arasında direk ilişki yok diagrama bakarsak. Sadece önemli olan veri tiplerinin eşit olması
"""
###################################
# LEFT JOIN  : 2 tane tabloda soldaki tabloyu baz alarak değerleri getiriyor. 2. tablodaki değerler 1. tablodada varsa getirir yoksa NULL getirir
    # SELECT columns FROM table_A LEFT JOIN table_B ON join conditions
"""
# SORU: Write a query that returns products that have never been ordered. Select product ID, product name, orderID
SELECT A.product_id, A.product_name, B.order_id 
FROM product.product A
LEFT JOIN sale.order_item B 
on A.product_id = B.product_id
WHERE B.order_id is null    

# WHERE B.order_id is null: B de order_id sinde veri olmayan satırlar # 213 rows
"""
################
"""
# Soru: Report the stock status of the products that product id greater than 310 in the stores
# .. Expected columns: product_id, product_name, store_id, product_id,
SELECT A.product_id, A.product_name, B.*
FROM product.product A
LEFT JOIN product.stock B 
on A.product_id = B.product_id
WHERE A.product_id >310 

# 237 rows
# NOT: EĞER ; WHERE B.product_id >310 yazsaydık  # 159 rows gelecekti
# Çünkü asıl sorgumuzda B den null lar geldi(B deki product_id den-4.sütun), B.product_id >310 yazınca null lar gelmedi
"""
###################################
# RIGHT JOIN   : 2 tane tabloda sağdaki tabloyu baz alarak değerleri getiriyor. 1. tablodaki değerler 2. tablodada varsa getirir yoksa NULL getirir
    # SELECT columns FROM table_A RIGHT JOIN table_B ON join conditions
"""
# Önceki sorguyu right joinle yazın
SELECT B.product_id, B.product_name, A.*
FROM product.stock A
RIGHT JOIN product.product B 
on A.product_id = B.product_id
WHERE B.product_id >310 

# Yine 237 row geldi gördüğümüz gibi
"""    
###################################
# FULL OUTER JOIN: 2 tabloyu join edeceğiz. Ama 1. tabloda olup 2. tabloda olmayan, 2.tabloda olup 
# .. 1. tabloda olmayan ve 2 tabloda da olanlar var.Bu 3 durum birleşip olarak hepsini getir
# Self Join

"""
Soru: Write a query that returns stock and order information together for all products(top100)
expected columns product_id, store_id, quantity, order_id, list_price

SELECT TOP 100 A.product_id, B.store_id, B.quantity, C.order_id, C.list_price
FROM product.product A
FULL OUTER JOIN product.stock B
ON A.product_id = B.product_id
FULL OUTER JOIN sale.order_item C
ON A.product_id = C.product_id
ORDER BY B.store_id               

# ORDER BY B.store_id:  Bunu yazarsak NULL ları net görebiliriz(Top 100 yazmasakta görebiliriz)
# 501 numaralı product_id(product tablosunda) -- Bu ürün stocklarda bulunmuyor, bu ürünün siparişide söz konusu olmamış vs
"""
###################################
# CROSS JOIN
# İki tablonun birbirleriyle kartezyen olarak çarpılması. Bütün varyasyonları görmek istiyorsak bunu kullanıyoruz
"""
# Soru: In the stocks table, there are not all products held on the product table and 
# .. you want to insert these products into the stock table.
#.. You have to insert all these products for every three stores with '0(zero)' quantity

SELECT	B.store_id, A.product_id, 0 quantity
FROM	product.product A
CROSS JOIN sale.store B
WHERE	A.product_id NOT IN (SELECT product_id FROM product.stock)  
ORDER BY A.product_id, B.store_id

WHERE	A.product_id NOT IN (SELECT product_id FROM product.stock) :  # product_id stock tablosunda olmayan ürünleri listele.Yani mesela 443 product_id nin quantity si 0
"""


###################################
# Hoca: Alttakileri size göndereceğim
# SELF JOIN
# VIEW

################################################# END ###########################################

