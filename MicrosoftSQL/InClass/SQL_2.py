#%% SQL-2. ders_02.01.2022

# Databases -- SampleRetail -- (mouse sağ tık) -- new query
# Sol üstteki(Execute butonunun solundaki) boşlukta çalışacağımız database yazmalı(SampleRetail)

# %%

# tables -- product.product sağ tık -- Select Top 1000 Rows
# Sağ alt köşede sayısı(520 satır), serverı, location ve zamanı gösteriyor

# ÖDEV
# tables -- (farklı farklı tablolara)sağ tık -- select top 1000 rows diyerek bir sonraki derse kadar verileri inceleyelim
# .. bu veritabanını anlamaya çalışalım

#%% 1.Ders -- Önceki Dersin Tekrarı
# Excel dosyası hakkında neler yaptık bakalım

# Bir kütüphanenin db sini oluşturma görevi verildi ve önünüze exceldeki gibi bir veri koydular ve
# .. bunu modellememizi istediler diyelim(Relational datase modeli)
# Nasıl başlayacağız?
# Relational database oluştururken bazı aşamalardan geçmemiz gerekiyor
# Normalize bir db oluşturmalıyız
# Bunun için en 3 faz gerekiyor. Bu fazları uygulayıp veriyi bölmemiz gerekiyor

# 1.NF
# 1.Sütunların satırlarla kesişen alanda tek hücrenin tek bir bilgi içermesini sağlamak
# 2.Sadece 1 primary key i olmalı
# Burada TELNO da 2 numara yazdığı yer var excel E sütununda, bu 2 telnoları farklı farklı sütunlarda
# .. telno1, telno2 sütunlarında tutabilirim. Eğer bir kişi 10 tane telefonu varsa ne olacak?
# .. Kişinin kaç tel nosu olduğunu bilemem. O yüzden bunu farklı sütunlarda oluşturmak yerine bu
# .. başka bir "entity" olsun diyorum ve TELNO tablosu oluşturuyorum.(Excelde 12-19. satırda olan yer)
# Bu telefon numaraları tek başına anlam ifade etmiyor. Bu kullanıcıları ben yanına yazdırayım diyorum
# Bu tel noyu diğer "entity" ler ile ilişkilendirebilirim.(excel satır 12-19 arası)
# Bu 1. norm kurallarını tamamladı mı ? 
# 1.Tekrarlayan sütun içermemesi  .. YOK
# 2.Sadece 1 primary key i olmalı .. Primary key - unique olarak ne seçebilirim burada? TELNO seçebilirim
# .. NOT: Normalde "ID" primary key olur.
# .. NOT: Primary key olması için: 1.Tekrarlayan değer olmaması gerekli, 2.Null değer olmaması gerekli

# 2NF aşamasına geçtik
# Bu aşama composite PK ile alakalı
# Composite PK: 2 sütunun bir araya gelerek primary key oluşturması demek
# Bir sütun tekrarlayan değerler içeriyor ve tam olarak identify edemiyorsa örn:
"""
1         3            a              a
1         7            a              1
2         5            a              1
3         5            a              1
4         6            a              1
4         7            a              1

Burada primary key hangi sütun olmalı?
Burada hiç bir sütun unique değerler içermediği için hiç birisi tek başına primary key olamaz
1. ve 2. sütunu birlikte alırsa onlar primary key olabilir çünkü ikililere baktığımızda hepsi 1'er adet
1-3
1-7
2-5
3-5
4-6
4-7
Diğer şart null değer içermemesiydi.İçermiyor
Bunları birleştirdik ve buna COMPOSITE primary key dedik
"""
# Şimdi örneğimize dönersek TELNO tek başına TELNO primary key di. Yani composite gerek yok burada
# O zaman ikinci fazıda tamamladık

# 3NF aşamasına geçtik
# Transitive Dependency: Bİr non-key attribute unun başka bir non-key attribute unu bağlılığı olmaması
# Bağımlılık ne demek?
"""
1       a
1       a
2       e
2       e
4       c
5       c

ilk satırda 1 , a ile eşleşmiş, ikinci satırda 1, a ile eşleşmiş. Şimdi düşünüyoruz;
"2. sütun, 1. sütuna bağımlı olabilir"
üçüncü ve dördüncü satırlar için aynı şeyi söyleyebiliriz
ama dördüncü ve beşinci satıra baktık 4-c, 5-c,
Burada 4, c ile eşleşmiş, 5 te c ile eşleşmiş
"O zaman 2. sütun,  1. sütuna BAĞIMLI ama  1. sütun 2. sütuna BAĞIMLI DEĞİL"
"Yani 1. sütun 2. sütunu "identify" etmiş oluyor
"""

#%% Dersin 2. bölümü
# Bir tablodaki tüm sütunlar sadece ve sadece primary key sütununa "fully dependent" bağımlı olması gerekiyor

# 3NF aşamasına devam
# Bir non-key attribute, diğer non-key attribute a bağımlı olmayacak
"""
TCKNO   KITAP_ID  KİTAP ADI  YAZAR

Burada primary key e bakınca excelde tek sütun yine primary key olamıyor.
Burada TCKNO ve KITAP_ID birlikte primary key oldu
2 foreign key bir araya gelerek bir primary key oluşturdu
"""
# Şimdi burada composite PK oluştu o zaman neye bakmalıyız?
# Burada KITAP_ID "composite PK" nın bir alt kümesi. Bu NON-KEY olan "kitap adını" identify ediyor mu.Ediyor
# HER BIR "KITAP_ADI" için FARKLI bir "KITAP_ID" var, yani "KITAP_ADI" composite PK nın bir parçasına(partial) bağımlı(KITAP_ID ye)
# Burada "KITAP_ADI" ve "YAZAR" ı farklı tablolarda tutabilirim.

# Diagrama bakalım şimdi. Departmanlarla vs konuştuk ettik ve harita oluşturduk buna göre database i oluşturacağız
# Tablolar: Mail, Person, Phone , Loan, Book, Author, Publisher
# Phone içine niye maili koymadık, publisher ın içine neden book u koymadık vs? Bunları bir düşünemk lazım
# Yani üstte yaptıklarımızı tekrar düşünmemiz lazım bu soruları
# Burada 2 şema/domain var LOAN ve BOOK
# "LOAN" a mail, person, phone bağlı, "BOOK" a author ve publisher bağlı
# "LOAN" ve "BOOK" arasında da bir köprü var.

#%% Dersin 2. bölümü devam
# Her bir sütun tek bir veri tipi olmalı
# Temelde 3 tip veri tipi var
# Datatype: String, Date and Time , Numeric
# Bunların alt değerleri var

"""
DATA TYPE      LOWER LIMIT   UPPER LIMIT            MEMORY
char              0 chars    8000 chars            n bytes                   
varchar           0 chars    8000 chars            n bytes + 2 bytes
text              0 chars    2.147.483.647 chars   n bytes + 4 bytes  
nchar             0 chars    4000 chars            2 times n bytes
nvarchar          0 chars    4000 chars            2 times n bytes + 2bytes
ntext             0 chars    1.073.741             2 times the string length

char(10)   : 10 karakterlik yer ayırır  karakter verilerini tutuyor .. char(10) "ali" yi 3 karakteri alır ve 7 karakteride boş olarak tutar
varchar(10): En fazla 10 karakterlik yer ayırır ama az karakter yazsakta olur  karakter verilerini tutuyor .. char(10) "ali" yi 3 karakteri alır ve 7 karakteri tutmaz
nvarchar  : ülkelere göre karakterler kullanmak istiyorsak
"""

"""
FORMATLAR
DATA TYPE          format
time
date
smalldatetime
datetime
datetime2
datetimeoffset
"""

"""
NUMERIC VERI TIPLERI
DATA TYPE           LOWER LIMIT       UPPER LIMIT           MEMORY
tinyint
smallint
int
bigint
decimal(precision, scale)
numeric(precision, scale)
money
smallmoney
float

Tel noyu int ile tutabilir miyiz? (+90 da mesela + var)
TC yi int ile 
big int : 9.9999999  precision toplam rakam, scale: virgül sonrası rakam
...
"""

# Constraints
# Toplamda 8 tür constraint var
# 1.null
# 2.not null
# 3.unique      : O tablodaki değerlerin tamamı 1 kere olabilir(eşsiz olmalı. Örneğin primary key, Primary key aynı zamanda notnull du)
              # unique sütunda null değer olabilir FAKAT 1 tane olabilir(Yani NULL da unique olmalı) başka NULL olamaz
# 4.default     : Değer girilmezse , default değer girilsin
# 5.identity    : Primary key olmasını istediğiniz sütunda veri eklendikçe otomatik hücreyi dolduran bir sütun olsun dersek oraya identity constraint i ekliyoruz
        # identity(seed,increment) : seed: kaçtan başlasın, increment: kaçar kaçar artsın.Genelde identity(1,1)
        # Null değer içermiyor identity
# 6.primary key : Unique ve notnull değerli sütun. Tek primary key olabilir. 2 sütun birleşerek 1 primary key olabilir
# 7.foreign key : Çok önemli. İlişkiyi sağlayan sütundur
        # Örneğin; öğrenci tablosu olsun, sınıf tablosu olsun ve hangi öğrencinin hangi sınıfta olduğunu birlikte tutan tablo var(3. tablo)
        # .. 3. tabloda sınıf_id ve öğrenci_id foreign key dir
        # Diğer özelliği, verinin tutarlı olmasını sağlar. 
        # .. Yani, Öğrenci tablosunda ID değiştirdiğinizde 3. tabloya da yansımış olacak
        # 3. özellik: Primary key özelliklerini taşır
        # Foreign key kuralları: No action , cascade , set null(değiştirdiğiniz değer null a dönüşür) , set default(sildiğiniz değere default değer gelir)
        # Örnek: ON UPDATE CASCADE : Ana tabloda yapılan update işlemlerini alt tabloya uygula
        # Örnek: ON DELETE CASCADE : Ana tabloda yapılan delete işlemlerini alt tabloya uygula
        
# 8.check       : Bir sütunun değerleri için bir kural belirtmek istiyorsanız. Örn: yaş sütununda değerler 140 dan büyük olamaz gibi..
        # örn: Age Int CHECK (Age>= 21)
        # örn: CONSTRAINT QuotaCap CHECK((HireDate < "01-01-2004") OR (Quota <=30000))
# Bunlar haritayı database e çevirmenin anahtarları
"""
USE SW:
CREATE TABLE EMPLOYEES
DepartmentName  CHAR(30) NOT NULL DEFAULT "Human Resources"
...
CONSTRAINT Employee_PK PRIMARY EmployeeNo)  # Employeeno yu primary key yaptı
"""

#%% 3. Ders
# Constraints lerden devam ettik biraz üste yazıldı

################################
# DDL - Data Definition Language
################################
# CREATE
    # Örn: CREATE DATABASE db_name
# ALTER       : Sütunların yapısında değişiklik yapar(Değerlerini değiştirmiyoruz. Onu UPDATE ile yapıyoruz)
    # ADD          : ALTER TABLE table_name ADD column_name data_type column
    # ALTER COLUMN : ALTER TABLE table_name ALTER COLUMN column_name
    # DROP COLUMNS : ALTER TABLE table_name DROP COLUMN column_name
# DROP        : Tabloyu drop ediyor
    # DROP TABLE table_name
# TRUNCATE    : Tablo içerisini boşaltıyor. Format atıyor
    # TRUNCATE TABLE table_name
# SELECT INTO : Bir query nin döndürdüğü sonuçları başka tabloya koyalar
    # SELECT [columns] INTO new_table_name FROM source_table [WHERE condition]

################################
# DML (Data Manipulation Language)
################################
# SELECT
# INSERT : Tabloya veri yüklemek için kullanılır
    # INSERT ONLY ONE ROW  : INSERT INTO table_name(columns list) VALUES (column_1_value, column_2,value...)
    # INSERT MULTIPLE ROWS : INSERT INTO table_name(columns list) VALUES (column_1_value, column_2,value...), (column_1_value, column_2,value...)
    # INSERT INTO SELECT   : INSERT INTO target_table__name(columns list) SELECT (column_list) FROM source_table    # source table daki değerleri target_table a yazıyor
    # NOT: Excel kodu:  ="insert into  product (product_id,name,date,price) values("&A1&",'" &B1& "','" &C1& "'," &D1& ");
# UPDATE : Bir tablodaki değerleri güncellememizi sağlar
    # UPDATE table_name SET old_version = new_version [WHERE condition]
    # Örn: UPDATE table_name SET Name = "Ali" WHERE ID=1]
# DELETE
    # DELETE ALL ROWS       : DELETE FROM table_name:
    # DELETE WITH CONDITION : DELETE FROM table_name WHERE conditions
    # DELETE TOP ... FROM   : DELETE TOP 20 FROM table_name WHERE conditions

#%%  3. Ders devam.
# Tabloları CREATE edeceğiz hocanın gönderdiği dosya ile("RDB&SQL Session 2..." dosyası)
# Kodları yavaş yavaş çalıştırıp ilerleyeceğiz
"""
CREATE DATABASE LibDatabase;
"""
# Sol üstten LibDatabase i seçiyorum. Sonra şemalarımı oluşturacağım
###########
"""
CREATE SCHEMA Book;
""" 
###########
"""
CREATE SCHEMA Person;
""" 
# Şimdi tabloları oluşturabilirim
###########
"""
CREATE TABLE [Book].[Book](
	[Book_ID] [int] PRIMARY KEY NOT NULL,
	[Book_Name] [nvarchar](50) NOT NULL,
	Author_ID INT NOT NULL,
	Publisher_ID INT NOT NULL

	);
""" 
###########
"""
CREATE TABLE [Book].[Author](
	[Author_ID] [int],
	[Author_FirstName] [nvarchar](50) Not NULL,
	[Author_LastName] [nvarchar](50) Not NULL
	);

""" 
###########
"""
CREATE TABLE [Book].[Publisher](
	[Publisher_ID] [int] PRIMARY KEY IDENTITY(1,1) NOT NULL,
	[Publisher_Name] [nvarchar](100) NULL
	);
""" 
###########
"""
CREATE TABLE [Person].[Person](
	[SSN] [bigint] PRIMARY KEY NOT NULL,
	[Person_FirstName] [nvarchar](50) NULL,
	[Person_LastName] [nvarchar](50) NULL
	);
""" 
###########
"""
CREATE TABLE [Person].[Loan](
	[SSN] BIGINT NOT NULL,
	[Book_ID] INT NOT NULL,
	PRIMARY KEY ([SSN], [Book_ID])
	);
""" 
###########
"""
CREATE TABLE [Person].[Person_Phone](
	[Phone_Number] [bigint] PRIMARY KEY NOT NULL,
	[SSN] [bigint] NOT NULL	
	);
""" 
###########
"""
CREATE TABLE [Person].[Person_Mail](
	[Mail_ID] INT PRIMARY KEY IDENTITY (1,1),
	[Mail] NVARCHAR(MAX) NOT NULL,
	[SSN] BIGINT UNIQUE NOT NULL	
	);
""" 
##################################################################
"""
--Tabloları yukarıdaki şekilde öncelikle create edip devam ediniz.
--Aşağıda DML komutlarını örneklendirip tablo constraintlerini sonradan tanımlayacağız. 
--Örnek olarak insert ettiğimiz verileri sonradan sileceğiz. 
--Gerçek değerlerin insert edilmesi işlemini sizlere bıkarıyor olacağım.

----------INSERT

----!!! ilgili kolonun özelliklerine ve kısıtlarına uygun veri girilmeli !!!

-- Insert işlemi yapacağınız tablo sütunlarını aşağıdaki gibi parantez içinde belirtebilirsiniz.
-- Bu kullanımda sadece belirttiğiniz sütunlara değer girmek zorundasınız. Sütun sırası önem arz etmektedir.
"""

######################################################################################################

# Tablolarımız bu kadar, Açıklamaları okuyup yarın akşam alt taraftan devam edip bu dersi bitireceğiz

# DIAGRAM AÇIKLAMASI
# IE(Karga Ayağı) : Bir kez veya daha fazla bulunabilir
# 0I              : Hiç bulunmayabilir ya da en fazla 1 tane bulunabilir
# II              : Bir kez veya en fazla 1 tane bulunabilir

#############################################  DERS SONU  ##################################################

######################################################################################################
"""
INSERT INTO Person.Person (SSN, Person_FirstName, Person_LastName) VALUES (75056659595,'Zehra', 'Tekin')

INSERT INTO Person.Person (SSN, Person_FirstName) VALUES (889623212466,'Kerem')


--Eğer bir tablodaki tüm sütunlara insert etmeyecekseniz, seçtiğiniz sütunların haricindeki sütunlar Nullable olmalı.
--Eğer Not Null constrainti uygulanmış sütun varsa hata verecektir.

--Aşağıda Person_LastName sütununa değer girilmemiştir. 
--Person_LastName sütunu Nullable olduğu için Person_LastName yerine Null değer atayarak işlemi tamamlar.

INSERT INTO Person.Person (SSN, Person_FirstName) VALUES (78962212466,'Kerem')

--Insert edeceğim değerler tablo kısıtlarına ve sütun veri tiplerine uygun olmazsa aşağıdaki gibi işlemi gerçekleştirmez.


--Insert keywordunden sonra Into kullanmanıza gerek yoktur.
--Ayrıca Aşağıda olduğu gibi insert etmek istediğiniz sütunları belirtmeyebilirsiniz. 
--Buna rağmen sütun sırasına ve yukarıdaki kurallara dikkat etmelisiniz.
--Bu kullanımda tablonun tüm sütunlarına insert edileceği farz edilir ve sizden tüm sütunlar için değer ister.

INSERT Person.Person VALUES (15078893526,'Mert','Yetiş')

--Eğer değeri bilinmeyen sütunlar varsa bunlar yerine Null yazabilirsiniz. 
--Tabiki Null yazmak istediğiniz bu sütunlar Nullable olmalıdır.

INSERT Person.Person VALUES (55556698752, 'Esra', Null)



--Aynı anda birden fazla kayıt insert etmek isterseniz;

INSERT Person.Person VALUES (35532888963,'Ali','Tekin');-- Tüm tablolara değer atanacağı varsayılmıştır.
INSERT Person.Person VALUES (88232556264,'Metin','Sakin')


--Aynı tablonun aynı sütunlarına birçok kayıt insert etmek isterseniz aşağıdaki syntaxı kullanabilirsiniz.
--Burada dikkat edeceğiniz diğer bir konu Mail_ID sütununa değer atanmadığıdır.
--Mail_ID sütunu tablo oluşturulurken identity olarak tanımlandığı için otomatik artan değerler içerir.
--Otomatik artan bir sütuna değer insert edilmesine izin verilmez.

INSERT INTO Person.Person_Mail (Mail, SSN) 
VALUES ('zehtek@gmail.com', 75056659595),
	   ('meyet@gmail.com', 15078893526),
	   ('metsak@gmail.com', 35532558963)

--Yukarıdaki syntax ile aşağıdaki fonksiyonları çalıştırdığınızda,
--Yaptığınız son insert işleminde tabloya eklenen son kaydın identity' sini ve tabloda etkilenen kayıt sayısını getirirler.
--Not: fonksiyonları teker teker çalıştırın.

SELECT @@IDENTITY--last process last identity number
SELECT @@ROWCOUNT--last process row count



--Aşağıdaki syntax ile farklı bir tablodaki değerleri daha önceden oluşturmuş olduğunuz farklı bir tabloya insert edebilirsiniz.
--Sütun sırası, tipi, constraintler ve diğer kurallar yine önemli.

select * into Person.Person_2 from Person.Person-- Person_2 şeklinde yedek bir tablo oluşturun


INSERT Person.Person_2 (SSN, Person_FirstName, Person_LastName)
SELECT * FROM Person.Person where Person_FirstName like 'M%'


--Aşağıdaki syntaxda göreceğiniz üzere hiçbir değer belirtilmemiş. 
--Bu şekilde tabloya tablonun default değerleriyle insert işlemi yapılacaktır.
--Tabiki sütun constraintleri buna elverişli olmalı. 

INSERT Book.Publisher
DEFAULT VALUES


--Update


--Update işleminde koşul tanımlamaya dikkat ediniz. Eğer herhangi bir koşul tanımlamazsanız 
--Sütundaki tüm değerlere değişiklik uygulanacaktır.



UPDATE Person.Person_2 SET Person_FirstName = 'Default_Name'--burayı çalıştırmadan önce yukarıdaki scripti çalıştırın

--Where ile koşul vererek 88963212466 SSN ' ye sahip kişinin adını Can şeklinde güncelliyoruz.
--Kişinin önceki Adı Kerem' di.

UPDATE Person.Person_2 SET Person_FirstName = 'Can' WHERE SSN = 78962212466


select * from Person.Person_2




--Join ile update

----Aşağıda Person_2 tablosunda person id' si 78962212466 olan şahsın (yukarıdaki şahıs) adını,
----Asıl tablomuz olan Person tablosundaki haliyle değiştiriyoruz.
----Bu işlemi yaparken iki tabloyu SSN üzerinden Join ile birleştiriyoruz
----Ve kaynak tablodaki SSN' ye istediğimiz şartı veriyoruz.

UPDATE Person.Person_2 SET Person_FirstName = B.Person_FirstName 
FROM Person.Person_2 A Inner Join Person.Person B ON A.SSN=B.SSN
WHERE B.SSN = 78962212466


--Subquery ile Update

--Aşağıda Person_2 tablosundaki bir ismin değerini bir sorgu neticesinde gelen bir değere eşitleme işlemi yapılmaktadır.

UPDATE Person.Person_2 SET Person_FirstName = (SELECT Person_FirstName FROM Person.Person where SSN = 78962212466) 
WHERE SSN = 78962212466



---
----delete
--Delete' nin ne anlama geldiğini artık biliyor olmalısınız.
--Delete kullanımında, Delete ile tüm verilerini sildiğiniz bir tabloya yeni bir kayıt eklediğinizde,
--Eğer tablonuzda otomatik artan bir identity sütunu var ise eklenen yeni kaydın identity'si, 
--silinen son kaydın identity'sinden sonra devam edecektir.


--örneğin aşağıda otomatik artan bir identity primary keye sahip Book.Publisher tablosuna örnek olarak veri ekleniyor.

insert Book.Publisher values ('İş Bankası Kültür Yayıncılık'), ('Can Yayıncılık'), ('İletişim Yayıncılık')


--Delete ile Book.Publisher tablosunun içi tekrar boşaltılıyor.

Delete from Book.Publisher 

--kontrol
select * from Book.Publisher 

--Book.Publisher tablosuna yeni bir veri insert ediliyor
insert Book.Publisher values ('İLETİŞİM')

--Tekrar kontrol ettiğimizde yeni insert edilen kaydın identity'sinin eski tablodaki sıradan devam ettiği görülecektir.
select * from Book.Publisher



---/////////////////////////////

--//////////////////////////////


--Buradan sonraki kısımda Constraint ve Alter Table örnekleri yapılacaktır.
--Yapacağımız işlemlerin tutarlı olması için öncelikle yukarıda örnek olarak veri insert ettiğimiz tablolarımızı boşaltalım.


DROP TABLE Person.Person_2;--Artık ihtiyacımız yok.

TRUNCATE TABLE Person.Person_Mail;
TRUNCATE TABLE Person.Person;
TRUNCATE TABLE Book.Publisher;





---------Book tablomuz bir primary key' e sahip

-- Foreign key konstraint' leri belirlememiz gerekiyor

ALTER TABLE Book.Book ADD CONSTRAINT FK_Author FOREIGN KEY (Author_ID) REFERENCES Book.Author (Author_ID)

ALTER TABLE Person.Book ADD CONSTRAINT FK_Publisher FOREIGN KEY (Publisher_ID) REFERENCES Book.Publisher (Publisher_ID)

---------Author

--Author tablomuza primary key atamamız gerekli, çünkü oluştururken atanmamış
--Burada bir hata alacaksınız ve tabloda bir düzenleme yapmanız gerekecek, 
--Bu tecrübeyi yaşamanızı ve sorunu çözmenizi bekliyorum. Aksi taktirde bir sonraki tabloda da hata alırsınız. :)



ALTER TABLE Book.Author ADD CONSTRAINT pk_author PRIMARY KEY (Author_ID)


ALTER TABLE Book.Author ALTER COLUMN Author_ID INT NOT NULL


--publisher ve person tabloları da primary key' e sahip.



--Person.Loan tablosuna Constraint eklemeliyiz.

---------Person.Loan tablosuna foreign key constraint eklemeliyiz


ALTER TABLE Person.Loan ADD CONSTRAINT FK_PERSON FOREIGN KEY (SSN) REFERENCES Person.Person (SSN)
ON UPDATE NO ACTION
ON DELETE NO ACTION


ALTER TABLE Person.Loan ADD CONSTRAINT FK_book FOREIGN KEY (Book_ID) REFERENCES Book.Book (Book_ID)
ON UPDATE NO ACTION
ON DELETE CASCADE


--Publisher tablosu normal.


---------Person.Person tablosundaki SSN sütununa 11 haneli olması gerektiği için check constraint ekleyelim.


Alter table Person.Person add constraint FK_PersonID_check Check (SSN between 9999999999 and 99999999999)

--Alttaki constraint' te check ile bir fonksiyonun doğrulanma durumunu sorguluyoruz.
--Fonksiyon gerçek hayatta kullanılan TC kimlik no algoritmasını çalıştırıyor.
--Yapılan check kontrolu bu fonksiyonun süzgecinden geçiyor, eğer ID numarası fonksiyona uyuyorsa fonksiyon 1 değeri üretiyor ve
--işlem gerçekleştiriliyor. Fonksiyon 0 değerini üretirse bu ID numarasının istenen koşulları sağlamadığı anlamına geliyor ve 
--İşlam yapılmıyor.
--Fonksiyonu çalıştırabilmeniz için fonksiyonu bu database altında create etmeniz gerekmektedir.
--Fonksiyonun scriptini ayrıca göndereceğim.

Alter table Person.Person add constraint FK_PersonID_check2 Check (dbo.KIMLIKNO_KONTROL(SSN) = 1)



---------Person.Person_Phone

--Person_Phone tablosuna SSN için foreign key constraint oluşturmamız gerekli.

Alter table Person.Person_Phone add constraint FK_Person2 Foreign key (SSN) References Person.Person(SSN)

--Phone_Number için check...

Alter table Person.Person_Phone add constraint FK_Phone_check Check (Phone_Number between 999999999 and 9999999999)

--

-------------Person.Person_Mail için Foreign key tanımlamamız gerekli

Alter table Person.Person_Mail add constraint FK_Person4 Foreign key (SSN) References Person.Person(SSN)


---Bu aşamada Database diagramınızı çizip tüm tablolar arasındaki bağlantıların oluştuğundan emin olmanızı bekliyorum.


--Insert işlemlerini size bırakıyorum, hata alarak, constraintlerin ne anlama geldiğini kendiniz tecrübe ederek yapmanız daha değerli.
--Index konusuyla ilgili derste işlediğimiz scripti ayrıca göndereceğim.
--Buradaki Tabloların indexlerini oluşturmanız için Mentoring weekly agendaya not bırakıyorum. Birlikte veya bireysel olarak çalışabilirsiniz.


--Herhangi bir probleminizde daima slackten ulaşabilirsiniz. 
--Sağlıcakla, iyi çalışmalar.
""" 
###########
"""

""" 
###########
"""

""" 
###########
"""

""" 
###########
"""

""" 
###########
"""

""" 

###########
"""

""" 










































