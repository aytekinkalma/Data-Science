#%% SQL-RECAP

#%% SQL-1
# Database Engine consists of two components: 1.Relational Engine (Query Processor), 2.Storage Engine
    # 1. Relational Engine is responsible for executing queries.
    # 2. Storage Engine manages database objects such as view, trigger, stored procedure
    
# SQL de verinin temin edilmesi, verinin planlanmış ortamda tutulması verinin modellenmesi, veritabanının modellenmesi önem arz ediyor.
# Hoca: Bunlarla uğraşmayacağız ama bilmekte çok fayda var.Veriyi çekerken kısa sürede bunları yapmak için veritabanı çalışma
# .. mantığını iyi bilmemiz gerekiyor.
    
# Table of Contents : A.Relational Database Concepts, B.Integrity Rules, C.Normalization

###################################################A.Relational Database Concepts ###################################################
# RDBM              : Bir takım nesnelerin birbirleri ile olan ilişkileri
    # Veri structured, text, video vs. olabilir  ama biz structured veri üzerinde SQL programlama dilini çalıştıracağız
# Database          : Veri tablolarının bulunduğu mantıki bir küme. Müşteriye hizmete yönelik ilgili tabloların varolduğu yapıdır
# Metadata          : Verinin hakkındaki veri    
    # Bu tabloda kaç satır/sütun var, kim düzenlemiş, doğum tarihleri aralığı, bu data ne zaman oluşturulmuş vs gibi bilgiler metadatadır
# Table:Veriyi bir arada içeren sütun ve satırlarda oluşan yapı
    # Table Properties - 1
        # 1.Tablo ismi eşsiz(unique) olmalı. Aynı isme ait ikinci bir tablo tanımlayamayız
        # 2.Duplicate satır olmamalı
        # 3.Columns are atomic.Yani birinin birden fazla telnosu varsa hücre içine tek bir telno yazmalıyım.
        # 4.Veri tipleri aynı olmalı.Veri tipi nümerik ise oraya "+90" ile başlayan bir şey yazamayız mesela
# Columns           : Sütunlar/Kolonlar. Her bir kolon bir özelliği ifade ediyor
# Row/Record/Tuple  : Satırlar
# Relation          : Bir kişiyi/şeyi ifade eden değer bulmaya çalışıyoruz.Örneğin;country tablosunda, countrynin temsili country_id dir 

################################################### B.Integrity Rules ###################################################
##############################
# B.1 Database Rules
# Database tarafından tanımlanmış olan bütünlüğü sağlamak için kurallarla ilgili varsayımlar


# 1.Domain integrity: Domain olarak sütunu düşünebiliriz burada
    # ..  Örneğin bir sütun düşünelim std_ID , integer olarak tanımlanmış ama altta
    # .. integer olmayan değerler varsa burada domain integrity yi korumak için bunların hepsi integer olmalı
    # .. zaten integer olarak belirlenseydi buraya string ifade giremezdik
# 2.Entity integrity: Aynı sütunu düşünelim. std_ID de bir kayıt var ama boş olamaz. Her satırda farklı bir Id bulunmalı
# 3.Referential integrity: Sipariş tablomuzda. Kendinizde olmayan bir ürünü bir müşteriye satamayız
    # .. Bir ürünüm varsa bunun kesinlikle ürün tablomda olması gerekiyor. Eğer ürün tablosunda
    # .. olmayan id yi girersem o bütünlüğü sağlayamam. Buna da Referential integrity deniyor
# 4.Exterprise Constraints:Database administratorların kullandığı bir alan Bunu çok bilmemize gerek yok.
# NOT: Bunları çok kullanmayacağız ama bunları bilmemiz bize SQL de çalışırken bir çok şey rahat anlamamızı sağlayacak 

############################# 
# B.2 Businesss Rules
# Business tarafından tanımlanmış olan bütünlüğü sağlamak için kurallarla ilgili varsayımlar

# Örneğin bir firma Her bir siparişte sadece 1 ürün satabilirim
# Örneğin başka bir firma her bir siparişte sadece 5 ürün satabilirim
# Örneğin başka bir firma her bir siparişte sadece 1 kalem satabilirim. Yeni kalem için yeni sipariş oluşturmalı
# Bu tarz kurallar İşletmenin işleyişini gösteren mantık sürecini ifade eder.

#############################
# Entity - Relationship Diagram(ER diagram)
# Entity: Nesnelerdir. Sürekli değişmeyen ve varlık olarak ifade edebileceğimiz şeylerdir. Örneğin; İnsan, Araba, Öğretmen, Sınıf vs
# Relation: Nesneler arasındaki ilişki.Örneğin; Bir öğretmen hangi sınıflara derse giriyor, öğretmen için entity, sınıf için entity
    # .. dersek, bunlar arasındaki ilişkiye de relationship diyoruz

# Attribute: Entity ye ait özellikler. Dept için dept_id, dept_name vs gibi.(entity attribute) 
# NOT:Relationshiplerin de attributeları olabilir. Örneğin: ilişkinin başladığı tarih öğretmen bu departmanda çalışıyor mu 
    # .. çalışmıyor mu, sadece ilişkiye özgü bilgileride relationshipslere tanımlayabiliriz

# ÖRNEĞİN : writer, novel, consumer : entitiler,  creates ve buys: relationship
    # Bunlar 5 adet tablo. Bunlar arasındaki ilişkiyi sağlayan primary key ve foreign keylerdir
    # Relationship: Weak ve Strong olabilir. 

######
# ERD Notations
# 2 çeşit notation kullanılıyor
# 1.Chen's notation 2.Crow's foot notation(Biz ikinciyi(Crow's foot notation) kullanacağız)
######
# Relationship türleri; Burası önemli
# a) 1:1     # 1 öğretmen sadece 1 departmanda çalışabilir. 
# b) 1:M     # 1 departmanda birden fazla öğretmen olabilir
# c) M:N      
# d) Unary   # Şemada aradaki bağlantı dolanıp(bir dikdörtgen oluşturuyordu) aynı tabloya dönüyordu. Bu o. ÖRNEK: staff_id, staff name,
# .. manager_id .. Hangi staff name in manager ı kim mesela 3(manager_id deki), son bu 3 e bakıyorum tekrar staff_id den bulup sonra 
# .. onun staff name ine bakıyorum ve manager ın ismini görmüş oluyorum. Yani hangi staff ın manager ı kim böyle dönüşlü yapılar unary.
# e) Ternary
# NOT:Bağlantılarda şekil olarak; karga ayağı, hiç olamaz ya da en fazla 1 tane olabilir vs şeklindeydi hatırlayacağımız gibi
# Bunların ne olduğunu anlamak istiyorsak SQL-1 dosyası satır 200-245 arasına bakılabilir

######
# How to Draw ER diagrams
# a.identify all entities
    # İlk olarak hangi entity lerin olacağını belirlemeliyiz(Öğrenci, Sınıf vs)
        # Öğrenci numarası entity mi olacak, attribute mu olacak vs
# b.identify relationshios
    # Hangi entitiler arasında ilişki olacak. Bu ilişkileri belirledikten sonra bu ilişkilerin türlerini belirlemek gerekecek
# c.add attributes
    # Entity mi ifade eden hangi attributelar olabilir. Bu attributelar sizin sorgulama yapmanızı veya tablodaki raporların zengin olmasını sağlar

#############################
# Constraints
# Not: Bu konunun detayı SQL-2 nin başında(ALTTA)
# İki tablo arasındaki ilişkileri sağlayan yapılardır
# sale.orders tablosuna baktığımızda 1 primary key(order_id)  var, 3 foreign key(customer_id, store_id, staff_id)
# sale.orders(order tablom ile) customer_id(customer tablom) arasında bir relation var burada değil mi
# .. buradaki orders(sale) bir relationshiptir, bir entity değildir ama customer(sale) bir entitidir
# .. ya da customer(sale) ile product(product) arasındaki ilişkiyi order(sale) ve order_item(sale) tablosu
# .. ile sağlıyoruz diagrama bakarsak. Bu yapıyı sağlamaya çalıştığımız contraintleri foreign key lerle tanımlıyoruz

################################################### C.Normalization ###################################################
# Normalization fazları var.Biz 1. , 2. ve 3. fazları göstereceğiz bu derste. Bazı kriterleri izleyerek normalizasyon yapacağız.
# SampleRetail da bir çok tablo vardı. Bunların hepsinin tek bir excel de tutulduğunu düşünelim. Bu kullanışsız ve analizini yapamayız
# Normalization hali ile tabloları oluşturmamız lazım

# Anomally(Kuraldışılık/Aykırılık): Kuraldışı şeylerin önüne geçmeye çalışıyoruz biz normalleştirirken
    # 1.Insertion Anomally   : Veri girerken olan anomallyler
    # 2.Update Anomally      : Farklı satırlarda bir ülke için farklı yüzölçümü görülmesi gibi.Ülke ismini tek satırda ifade etmeliyim
    # 3.Deletion Anomally    : Örneğin üstteki ülke için 2 satırdan birini sildik diyelim. Ama doğru olanı mı sildik?

# How to Avoid Anomalies
    # 1.Bir takım normalize olan tablolar create edeceğiz
    # 2.Bazı functional dependency ler tanımlayacağız

# Normal Forms
    # First normal form
        # 1.En az 1 tane primary key olmalı
            # PRIMARY KEY(Ya da COMPOSITE PK) KURALLARI: 1.Tekrarlayan değer olmaması gerekli, 2.Null değer olmaması gerekli
        # 2.Sütunların satırlarla kesişen alanda tek hücrenin tek bir bilgi içermesini sağlamak(Yani hücrede sadece tek bir tel no olmalı)
        # 3.Tekrarlayan satır olmamalı.
        ##### Bunları sağladıysak 1. faz normalleştirmeyi yapmış oluyoruz.
    # Second normal form
        # 1.Sağlamamız gereken 2.fazda şey non-key bir sütunun ancak 2 PK bir araya gelerek o non-key i identify etmesi gerekiyor
        # .. Yani "Partial dependency" OLMAMASI gerekiyor. Eğer bu olmazsa, "partial" bağımlı olan non-key i ve bağlı olduğu primary 
        # .. keylerden birini(bu aldığımız PK alındığı tabloda da olacak ilk tabloda da kalacak) başka bir tabloya almamız gerekiyor.
        # .. Eğer partial dependency yoksa sorun yok. 2 primary key mi olmalı ve 1 primary key mi olmalı diye bakıyorum(Notlar bkz.)
            # NOT: Primary key 1 tane ise otomatik 2. faz sağlanmış oluyor    
            # NOT:PARTAL DEP: non-key olan bir sütun primary keylerden herhangi biri ile ifade ediliyorsa bu "partial" dependency denir
            # NOT: Composite PK: 2 sütunun bir araya gelerek primary key oluşturması demek
                # Yani, bir sütun tekrarlayan değerler içeriyor ve non-key attributeları tam olarak identify edemiyorsa
        ##### 
        ##### Bunu sağladıysak 2. faz normalleştirmeyi yapmış oluyoruz 
    # Third normal form
        # 1.Primary key olmayan bütün değerlerin tamamen bağımsız olması yani;(Transitivity Dependency)
        # .. Bir müşteri tablosunda, primary key(ler) var, bir de diğer alanlar. Bu diğer alanlar tamamen o müşteri ile alakalı olacak
        # .. ve Transitivity Dependency olacak
            # NOT: Transitivity Dependency: bir non key attribute' un başka bir non key attribute' a bağımlı olmaması
"""
    Book → Author: Here, the Book attribute determines the Author attribute. If you know the book name, you can learn the author's name.
    ..However, Author doesn't determine Book, because an author can write multiple books. For example, just because we know the author's
    ..name is Orson Scott Card, we still don't know the book name.
    Author → Author_Nationality: Likewise, the Author attribute determines the Author_Nationality, but not the other way around—just 
    ..because we know the author's nationality doesn't mean we can determine the author.
        But this table introduces a transitive dependency:
    Book →Author_Nationality: If we know the book name, we can determine the author's nationality via the Author column.
        """
        ##### Bunu sağladıysak 3. faz normalleştirmeyi yapmış oluyoruz
        
############################################################################################################################
#%% SQL-2
# Temelde 3 tip veri tipi var
# Datatype: String, Date and Time , Numeric
    # String : char, varchar, text, nchar, nvarchar, ntext 
    # Date   : time, date, smalldatetime ,datetime, datetime2, datetimeoffset
    # Nümerik: tinyint, smallint, int, bigint, decimal(precision, scale), numeric(precision, scale), money, smallmoney, float

################
# Toplamda 8 tür constraint var
# 1.null
# 2.not null
# 3.unique      : O tablodaki değerlerin tamamı 1 kere olabilir(eşsiz olmalı. Örneğin primary key, Primary key aynı zamanda notnull du)
        # unique sütunda null değer olabilir FAKAT 1 tane olabilir(Yani NULL da unique olmalı). Başka NULL olamaz
# 4.default     : Değer girilmezse , default değer girilsin
        # DepartmentName  CHAR(30) NOT NULL DEFAULT "Human Resources"
# 5.identity    : Primary key olmasını istediğiniz sütunda veri eklendikçe otomatik hücreyi dolduran bir sütun olsun 
        # ...dersek oraya identity constraint i ekliyoruz
        # identity(seed, increment) : seed: kaçtan başlasın, increment: kaçar kaçar artsın.Genelde identity(1,1)
        # NOT: Identity Null değer içermiyor 
# 6.primary key : Unique ve notnull değerli sütun. Tek primary key olabilir. 2 sütun birleşerek 1 primary key de olabilir
# 7.foreign key : (Çok önemli) 
        # 1.İlişkiyi sağlayan sütundur.
        # Örneğin; öğrenci tablosu olsun, sınıf tablosu olsun ve hangi öğrencinin hangi sınıfta olduğunu birlikte tutan
        # .. tablo var(3. tablo). 3. tabloda sınıf_id ve öğrenci_id foreign key dir
        # 2. özelliği, verinin tutarlı olmasını sağlar. 
        # .. Yani, Öğrenci tablosunda ID değiştirdiğinizde 3. tabloya da yansımış olacak
        # 3. özellik: Primary key özelliklerini taşır
    # Foreign key kuralları: No action , cascade , set null(değiştirdiğiniz değer null a dönüşür) , 
    # .. set default(sildiğiniz değere default değer gelir)
        # Örnek: ON UPDATE CASCADE : Ana tabloda yapılan update işlemlerini alt tabloya uygula
        # Örnek: ON DELETE CASCADE : Ana tabloda yapılan delete işlemlerini alt tabloya uygula
# 8.check       : Bir sütunun değerleri için bir kural belirtmek istiyorsanız. Örn: yaş sütununda değerler 140 dan büyük olamaz gibi..
        # örn: Age Int CHECK (Age>= 21)
        # örn: CONSTRAINT QuotaCap CHECK((HireDate < "01-01-2004") OR (Quota <=30000))
# Bunlar(Constraintler) haritayı database e çevirmenin anahtarları

################################
# DDL - Data Definition Language
################################
# CREATE
    # Örn: CREATE DATABASE db_name
# ALTER       : Sütunların yapısında değişiklik yapar(Değerlerini değiştirmiyoruz. Onu UPDATE ile yapıyoruz)
    # ADD          : ALTER TABLE table_name ADD column_name datatype
    # ALTER COLUMN : ALTER TABLE table_name ALTER COLUMN column_name
    # DROP COLUMNS : ALTER TABLE table_name DROP COLUMN column_name
# DROP        : Tabloyu drop ediyor
    # DROP TABLE table_name
# TRUNCATE    : Tablo içerisini boşaltıyor. Format atıyor
    # TRUNCATE TABLE table_name
    # NOT: DROP vs TRUNCATE: Drop aynı pandas mantığıyla veriyi atar kalıcı olarak, truncate de tablo durur db de, sadece içindeki değerler silinir
# SELECT INTO : Bir query nin döndürdüğü sonuçları başka tabloya koyar
    # SELECT [columns] INTO new_table_name FROM source_table [WHERE condition]

################################
# DML - Data Manipulation Language
################################
# SELECT
# INSERT : Tabloya veri yüklemek için kullanılır
    # INSERT ONLY ONE ROW  : INSERT INTO table_name(columns list) VALUES (column_1_value, column_2,value...)
    # INSERT MULTIPLE ROWS : INSERT INTO table_name(columns list) VALUES (column_1_value, column_2,value...), (column_1_value, column_2,value...)
    # INSERT INTO SELECT   : INSERT INTO target_table_name(columns list) SELECT (column_list) FROM source_table    
        # source_table daki değerleri target_table a yazıyor
    # Excelden verileri çekmek istediğimizde;
        # Excel kodu örnek: : ="insert into  product (product_id,name,date,price) values('"&A1&"','" &B1& "','" &C1& "','" &D1& "');
        # Excel kodu örnek2 : ="INSERT INTO CUSTOMER ([CUSTOMERNAME],[CITY],[DISTRICT], [BIRTHDATE],[GENDER]) VALUES ('"&A2&"','"&B2&"','"&C2&"','"&D2&"','"&E2&"')"
# UPDATE : Bir tablodaki değerleri güncellememizi sağlar
    # UPDATE table_name SET old_version = new_version [WHERE condition]
    # Örn: UPDATE table_name SET Name = "Ali" WHERE ID=1]
# DELETE
    # DELETE ALL ROWS       : DELETE FROM table_name:   # Bunu pek kullanmamalıyız
    # DELETE WITH CONDITION : DELETE FROM table_name WHERE conditions
    # DELETE TOP ... FROM   : DELETE TOP 20 FROM table_name WHERE conditions

#########################################
########## DATABASE OLUŞTURMA
# CREATE DATABASE db_name
# NOT: Noktalı virgül konulmasa da komutlar çalışır
"""
CREATE DATABASE LibDatabase;
"""
# Sol üstten LibDatabase i seçiyorum. Sonra şemalarımı oluşturacağım. 
    # ÖNEMLİ NOT: Eğer bunu yapmazsam oluşturacağım tablolar hangi DB seçili ise orada oluşur

########## ŞEMA OLUŞTURMA
# CREATE SCHEMA schema_name
"""
CREATE SCHEMA Book;
-----------------------------------------
CREATE SCHEMA Person;
""" 

########## TABLO OLUŞTURMA
# CREATE TABLE table_name(column1 dtype constraints) 
# NOT: 2. örnekte PRIMARY KEY altta tanımlanmış(Composite key oluşturulmuş)

"""
CREATE TABLE [Book].[Book3](
	[Book_ID] [int] PRIMARY KEY NOT NULL,
	[Book_Name] [nvarchar](50) NOT NULL,
	Author_ID INT NOT NULL,
	Publisher_ID INT NOT NULL);
-----------------------------------------
CREATE TABLE [Person].[Loan3](
	[SSN] BIGINT NOT NULL,
	[Book_ID] INT NOT NULL,
	PRIMARY KEY ([SSN], [Book_ID]));
"""

######### CONSTRAINT EKLEME
# Constraintler 8 adetti(Str 162 bkz). Hepsi eklenmedi(SQL-2 den hepsi alınmadı) Farklı constraint örnekleri alındı.
# NOT: Karışık yazıldığı için hata verenler olabilir. Detaylı inceleme için SQL-2 dosyasına bakılabilir
"""
-----------------------------------------
ALTER TABLE Person.Loan3 ADD CONSTRAINT FK_book FOREIGN KEY (Book_ID) REFERENCES Book.Book3 (Book_ID)
-----------------------------------------
ALTER TABLE Book.Author ADD CONSTRAINT pk_author PRIMARY KEY (Author_ID)
-----------------------------------------
ALTER TABLE Book.Author ALTER COLUMN Author_ID INT NOT NULL
-----------------------------------------
ALTER TABLE Person.Loan ADD CONSTRAINT FK_PERSON FOREIGN KEY (SSN) REFERENCES Person.Person (SSN)
ON UPDATE NO ACTION
ON DELETE NO ACTION
-----------------------------------------
ALTER TABLE Person.Loan ADD CONSTRAINT FK_book FOREIGN KEY (Book_ID) REFERENCES Book.Book (Book_ID)
ON UPDATE NO ACTION
ON DELETE CASCADE
-----------------------------------------
-- Person.Person tablosundaki SSN sütununa 11 haneli olması gerektiği için check constraint ekleyelim.
Alter table Person.Person add constraint FK_PersonID_check Check (SSN between 9999999999 and 99999999999)
-----------------------------------------
Alter table Person.Person_Phone add constraint FK_Phone_check Check (Phone_Number between 999999999 and 9999999999)
-----------------------------------------
--Alttaki constraint' te check ile bir fonksiyonun doğrulanma durumunu sorguluyoruz.
--Fonksiyon gerçek hayatta kullanılan TC kimlik no algoritmasını çalıştırıyor.
--Yapılan check kontrolu bu fonksiyonun süzgecinden geçiyor, eğer ID numarası fonksiyona uyuyorsa fonksiyon 1 değeri üretiyor ve
--işlem gerçekleştiriliyor. Fonksiyon 0 değerini üretirse bu ID numarasının istenen koşulları sağlamadığı anlamına geliyor ve 
--İşlam yapılmıyor.
--Fonksiyonu çalıştırabilmeniz için fonksiyonu bu database altında create etmeniz gerekmektedir.
--Fonksiyonun scriptini ayrıca göndereceğim.

Alter table Person.Person add constraint FK_PersonID_check2 Check (dbo.KIMLIKNO_KONTROL(SSN) = 1)
"""

############################################################################################################################
#%% SQL-3
########## INSERT / INSERT INTO
# INSERT INTO table_name (columns) VALUES (value11, value12,...), (value21, value22, ...), ...
# INSERT INTO yerine INSERT yazabiliriz
# NOT: Integer a nümerik, varchar sütuna string değer girmeliyiz
"""
INSERT INTO Person.Person (SSN, Person_FirstName, Person_LastName) VALUES (75056659595,'Zehra', 'Tekin')
-----------------------------------------
INSERT INTO Person.Person  VALUES (889623212466,'Kerem',"Yılmaz")  -- Sütun ismi yazmazsam tüm sütunlara insert edecek
INSERT INTO Person.Person  VALUES (889623212466,'Kerem')           -- HATA, 3 sütun, 2 değer var
INSERT INTO Person.Person (SSN, Person_FirstName) VALUES (889623212466,'Kerem') -- Kabul etti çünkü  Person_LastName sütunu "NULL" olabiliyor
----------------------------------------
-- Sütun sırasını değiştirebilirim ama values sırasını da değiştirmeliyim
INSERT INTO Person.Person (Person_LastName,SSN, Person_FirstName) VALUES ("Yalnız",689623512466,'Ahmet') 
----------------------------------------
-- Birden fazla değer ekleme
-- NOT: Mail_ID identity(1,1) constraint ine sahip olduğu için buna değer girmeye çalışırsak hata alırız
-- Sütun isimlerini yazmazsak da kabul ederdi.
INSERT INTO Person.Person_Mail (Mail, SSN) VALUES ('zehtek@gmail.com',75056659595),
                                  ('meyet@gmail.com',13056659595),
                                  'metsak@gmail.com',24056659595)


INSERT Book.Publisher
DEFAULT VALUES
"""

########## SELECT ... INTO
# SELECT columns INTO new_table FROM old_table
# Yeni tablo oluşturma ve eski tablodaki bilgileri yeni tabloya aktarma
"""
SELECT * INTO person.person_2 from Person.Person  -- Person tablosunun tamamını person_2 tablosuna kopyala
"""

########## INSERT INTO/INSERT SELECT
# Bir tabloya farklı bir query nin sonucunda gelen değerleri insert etmemize yarıyor
# INSERT INTO new_table SELECT old_columns FROM old_table (WHERE CLAUSE)
"""
INSERT person.person_2 SELECT * FROM person.person WHERE Person_FirstName = 'Zeki' -- Primary key olmadığı için 2 tane kayıt geldi person_2 ye
"""

########## DEFAULT VALUES
# Null olabilen sütun için NULL, otomatik artan için sıradaki değeri ata
"""
INSERT Book.Publisher DEFAULT VALUES -- Publisher_ID otomatik artan, Publisher_Name Null değer alabiliyor
"""

########## UPDATE
# Değerleri güncellemek için kullanılır
"""
UPDATE person.person_2 SET Person_FirstName = 'Ahmet'
WHERE Person_lastName = 'Yalnız'
"""

########## DELETE
# Tabloyu ya da verilen koşula göre silme
"""
SELECT * FROM Book.Publisher
DELETE FROM Book.Publisher
----------------------------------------
Insert Book.Publisher values ('İLETİŞİM')
SELECT * FROM Book.Publisher
DELETE FROM Book.Publisher WHERE Publisher_Name = 'İLETİŞİM'
"""

##########  DROP TABLE
#  Verileri ile birlikte tablo gider. Tabloyu DROP etme
"""
DROP TABLE Person.person_2
"""

########## TRUNCATE 
# Tabloya format atar. Tablonun içini boşaltma(Tabloyu silmez)
"""
TRUNCATE TABLE Person.Person_Mail;
----------------------------------------
TRUNCATE TABLE Person.Person;
----------------------------------------
TRUNCATE TABLE Book.Publisher;
"""
########## ALTER
# Veritabanındaki verilerin yapısını değiştirir. CONSTRAINT lerde bunu bir çok kere yazmıştık
"""
ALTER TABLE Book.Author ALTER COLUMN Author_ID INT NOT NULL
ALTER TABLE book.book ADD CONSTRAINT FK_Author FOREIGN KEY (Author_ID)
REFERENCES book.author (Author_ID)
----------------------------------------
ALTER TABLE Person.Loan ADD CONSTRAINT FK_PERSON FOREIGN KEY (SSN)
REFERENCES Person.Person (SSN) 
ON UPDATE NO ACTION
ON DELETE NO ACTION
# ON UPDATE  : ana tabloda update yaptığımda NO ACTION yapsın
# ON DELETE  : ana tabloda delete yaptığımda NO ACTION yapsın
"""

#####################
# UFAK NOTLAR:
# Diagrama bakalım. Database diagrams -- (sağ tık) -- new database diagram -- (Tüm sütunları seçelim) -- add -- close
# Diagramda bir tabloya sağ tık -- > properties -- dediğimde o tablo ile ilgili bilgiler geliyor
# Diagramda bir tabloya sağ tık -- > table view -- modify custom --> 
    # .. --> (sol taraftaki "Data Type" ı sağ tarafa alıp tabloyu diagramda dtype ları ile birlikte görürüz) 
# relationships e tıklayıp bağlantıları da görebiliriz

# MSSQL Türkçe karakterlerde hata veriyorsa
# Tools--> Options --> (açılan yerde sol üst arama yerine language yazıyoruz), --> language --> same as windows

# Şemalar: Hoca: Şemalar tabloları birbirinden ayırmak, onları ayrı yetkilendirme yapabilmek için Şema yapıyorsunuz
# .. Bazı şemalara yetki verip bazılarına yetki vermiyoruz vs

# NOT: Db oluştururken database in case sensitive olup olmadığını ayarlayabiliyoruz

############################################################################################################################
#%% SQL-4
# NOT:  /*     */  : Yorum açmak için kullanılır .
# NOT:  iki tire ard arda(--) : Bu da yorum açmak için kullanılır

# Bazı temel SQL komutları ve örnekleri var burada bunları almadık RECAP dosyasına(SQL-4 incelenebilir)
# SELECT , FROM , WHERE , ORDER BY ,TOP, IN, NOT IN, LIKE, BETWEEN ...
# NOT: <> : "Eşit değildir"  ya da   != : "Eşit değildir" anlamında bu da

# Table of Contents
# 1. Date functions
# 2. String functions
# 3. Other functions 

#############################
# 1.DATE FUNCTIONS
# ÖNEMLİ NOT:sampleretail --Programmability-functions--system functions -- Date and Time functions. Burada çıkanlar tanımlanmış fonksiyonlardır
# Date Fonksiyonları: time ,date, smalldatetime, datetime, datetime2, datetimeoffset,

##########  GETDATE() : Sistemimizin/Bilgisayarın tarihi ve zamanını datetime data tipinde getirir.
# Date fonksiyonları ve GETDATE() iç içe bakacağız burada
"""
CREATE TABLE t_date_time (
	A_time time,
	A_date date,
	A_smalldatetime smalldatetime,
	A_datetime datetime,
	A_datetime2 datetime2,
	A_datetimeoffset datetimeoffset
	)

-- "t_date_time isminde" bir tablo oluşturduk
-- 6 tane sütunu var. Her sütunun veritipi fatklı
-- Şimdi inceleyelim
SELECT * from t_date_time     --  Şu an boş.

SELECT GETDATE() as get_date  -- Tarih saat ve nanosecond sonuç döndürdü

-- Insert yapalım yukarda oluşturduğumuz tabloya
INSERT t_date_time
VALUES (GETDATE(),GETDATE(),GETDATE(),GETDATE(),GETDATE(),GETDATE())

-- Her sütun kendi veritipine uygun şekilde yazdırdı
----------------------------------------
INSERT t_date_time (A_time, A_date, A_smalldatetime, A_datetime, A_datetime2, A_datetimeoffset)
VALUES
('12:00:00', '2021-07-17', '2021-07-17','2021-07-17', '2021-07-17', '2021-07-17' )

-- "time" formatına uygun şekilde values un ilk değerini saat şeklinde yazdık, diğerlerine sadece tarih girelim
-- Kendi formatlarına uygun çıktı getirdiler yine
"""

########## DATE FORMATLARI
# Farklı ülkelerin veya farklı kullanım amaçlarına göre tarih stilleri var(https://www.sqlshack.com/sql-convert-date-functions-and-formats/)
# Her bir stilin kodu var (1,2,3,4,5,6,7,8..., 131)). Verimizdeki tarih formatı bize uygun değilse bu still ile değiştirebiliriz.
"""
SELECT CONVERT(VARCHAR, GETDATE(), 6)   # GETDATE() i varchar a dönüştürdük. Still kodu 6 yani burada 6 görmek istediğimiz format(10 Jun 22)
----------------------------------------
SELECT CONVERT(DATE,'25 Oct 21' , 6)    # Varchar ı date e dönüştürdük(2021-10-25)
-- '25 Oct 21'  : Dönüştürülmesini istediğim veri tipi -- > VARCHAR 
-- DATE         : Dönüştürmek istediğim veri tipi -- > DATE
-- 6            : "Date only format tablosundaki" Dönüştürmek istediğim stil no(str 460 daki linke bkz) 
"""

########## DATE IÇINDEN GÜN, AY VS ALMAK/ÇEKMEK
# Date ten istediğimiz parçaları alacağız
"""
SELECT A_DATE, DAY(A_DATE) DAY_, MONTH(A_DATE) [MONTH], DATENAME(DAYOFYEAR, A_DATE) DOY, DATEPART(WEEKDAY, A_date) WKD, DATENAME(MONTH, A_DATE) MON
FROM t_date_time --- (str 428 bkz. Bu tabloyu oluşturduk ve str 445-450 insert yapıldı)

-- NOT: Burada fonksiyonlar (Python daki built-in gibi olduğu için) isim verirken DAY sonuna alt tire ya da MONTH u köşeli parantez
-- .. içine alarak fonksiyon rengi pembeye dönmeden sütuna bu şekilde isim atayabiliriz
"""
########## DATEDIFF: IKI TARIH/ZAMAN ARASINDAKI FARKI ALMAK(gün farkı, dakika farkı, saat farklı vs)
"""
SELECT DATEDIFF(DAY,'2022-05-10',GETDATE())    -- şu anki zaman ile 2022-05-10 arasındaki gün farklı
----------------------------------------
SELECT DATEDIFF(SECOND,'2022-05-10',GETDATE()) -- şu anki zaman ile 2022-05-10 arasındaki saniye farklı
----------------------------------------
--Her bir sipariş için sipariş tarihi ve kargolama tarihi arasındaki farkı GÜN cinsinden bulalım
SELECT *, DATEDIFF(DAY, order_date, shipped_date) Diff_of_day FROM sale.orders
----------------------------------------
-- Her bir sipariş için sipariş tarihi ve kargolama tarihi arasında 2 günden fazla geçenler
SELECT *, DATEDIFF(DAY, order_date, shipped_date) Diff_of_day FROM sale.orders
WHERE DATEDIFF(DAY, order_date, shipped_date) > 2  -- 463 rows
-- 2. yol -- Böyle yapsaydık Diff_of_day sütunu gözükmezdi ama kod çalışırdı
SELECT * FROM sale.orders
WHERE DATEDIFF(DAY, order_date, shipped_date) > 2 -- 463 rows
"""

########## DATEADD: BELIRTTIGIMIZ ZAMANA DEGER EKLEMEK, EOMONTH : AYIN SON GÜNÜ
"""
SELECT DATEADD(DAY,5,GETDATE())     -- Şu anki zamana 5 gün ekledi
SELECT DATEADD(MINUTE,5,GETDATE())  -- Şu anki zamana 5 dakika ekledi
SELECT EOMONTH(GETDATE())    -- içinde bulunduğumuz ayın son gününü getirdi
SELECT EOMONTH(GETDATE(),2)  -- içinde bulunduğumuz aydan 2 ay sonrasındaki ayın son gününü getirdi
"""

########## ISDATE : İfadenin geçerli bir tarih olup olmadığını kontrol eder. Tarih ise output 1, değilse 0
"""
SELECT ISDATE('Anyting')       -- Output: 0 
SELECT ISDATE('05/05')         -- Output: 0 
SELECT ISDATE('05-05-2013')    -- Output: 1 
SELECT ISDATE('2013/05/05')    -- Output: 1 
"""

#############################
# 2.STRING FUNCTIONS
# ÖNEMLİ NOT:sampleretail --Programmability-functions--system functions -- string functions. Burada çıkanlar tanımlanmış fonksiyonlardır

########## STRING FUNCTIONS 1                          
# LEN                                           : Karakter  uzunluğu
# CHARINDEX(substring, string[,start_location]) : Karakterin indexi, örn: ahmet te "H" harfi kaçıncı karakter
# PATINDEX('%pattern%', input_string)           : Bir patern aradığımız zaman örn: Bir sütunda "h" ve "m" harflerinin yan yana olduğu pattern i aramak istersek

"""
SELECT LEN ('  CHARACTER')                -- Output : 11  -- çünkü boşluk var burada onu da karakter olarak sayıyor
SELECT LEN ('CHARACTER   ')               -- Output : 9   -- Bu şekilde olunca saymıyor
SELECT CHARINDEX('R','CHARACTER')         -- Output : 4   -- String içerisinde "R" nin indexini bulalım 
SELECT CHARINDEX('R','CHARACTER',5)       -- Output : 9   -- Saymaya 5. karakterden başla ilk R nin indexini bul.
SELECT CHARINDEX('RA','CHARACTER')        -- Output : 4   -- String içerisinde "RA" patterinin başladığı indexini bulalım
SELECT CHARINDEX('RA','CHARACTER')  -1    -- Output : 3   -- String içerisinde "RA" patterinin başladığı indexini bulalım o indexten 1 çıkart
SELECT PATINDEX('%R', 'CHARACTER')        -- Output : 9   -- String R ile biterse "R" nin indexi(İçindeki R ler önemli değil)
SELECT PATINDEX('%H%', 'CHARACTER')       -- Output : 2   -- String içinde H geçiyorsa indexi(Eğer 1 den fazla H varsa ilk yakaladığının indexini getirir)
SELECT PATINDEX('__A______', 'CHARACTER') -- Output : 1   -- A dan önce 2, A dan sonra 6 karakter olan bir pattern var mı? (1: Var , 0: Yok)
SELECT PATINDEX('__A%', 'CHARACTER')      -- Output : 1   -- A dan önce 2 karakter olan bir pattern var mı?(Sonrasının kaç karakterli olduğu önemli değil) (1: Var , 0: Yok)
SELECT PATINDEX('______T%', 'CHARACTER')  -- Output : 1   -- T dan önce 6 karakter olan bir pattern var mı?(Sonrasının kaç karakterli olduğu önemli değil) (1: Var , 0: Yok)
SELECT PATINDEX('%A__', 'CHARACTAER')     -- Output : 8   -- Pattern e uyan Son A nın indexini getirdi. (Üsttekilerle aynı mantıkta çalışmıyor)
-- %R  : Buradaki yüzde; sayısını bilmediğim kadar karakter
-- NOT : charindex fonksiyonunda indexlemeye 1 den başlıyor
"""
########## STRING FUNCTIONS 2
# LEFT()      : Soldan istediğimiz kadar karakter almamıza yarar
# RIGHT()     : Sağdam istediğimiz kadar karakter almamıza yarar
# SUBSTRING() : Başlangıç ve bitiş karakterini vererek  sağdan,soldan veya ortadan istediğimiz kadar karakter almamıza yarar
"""
SELECT LEFT('CHARACTER',3)         -- Output: CHA 
SELECT RIGHT('CHARACTER',3)        -- Output: TER 
SELECT SUBSTRING('CHARACTER',3,5)  -- Output: ARACT  -- 3 ten başla(3 dahil) , 5 karakter al
SELECT SUBSTRING('CHARACTER',4,9)  -- Output: RACTER -- 4 ten başla(4 dahil), 9 karakter al(ama 4 ten sonra 9 karakter alamadığı için sonuna kadar aldı)
"""
########## STRING FUNCTIONS 3
# LOWER()      : Küçük harfe döndürür
# UPPER()      : Büyük harfe döndürür
# STRING_SPLIT : A table-value function: Öncekiler(Yukarıdakiler) tek bir değer döndürüyordu, A table-value function bir tablo döndürecek
# NOT: Altta bazı kodlar hatalı gibi görünüyor ama SQL Server da ama çalışıyor
"""
SELECT LOWER('CHARACTER')                                              -- output : character
----------------------------------------
SELECT UPPER('character')                                              -- output : CHARACTER
----------------------------------------
SELECT * FROM STRING_SPLIT('jack,martin,alain,owen', ',')              -- Her bir ismi tek bir sütunda tablo kaydı olarak döndürdü
----------------------------------------
SELECT value FROM STRING_SPLIT('jack,martin,alain,owen', ',')          -- value ile de tablonun değerlerini yakalayabiliriz --
SELECT value as name FROM STRING_SPLIT('jack,martin,alain,owen', ',')  -- sütun ismi "name" oldu -- Her bir ismi tek bir sütunda tablo kaydı olarak döndürdü
-- NOT: Burada virgül: "ayırt edici değer"
----------------------------------------
--  'character' kelimesinin ilk harfini büyüten bir script yazınız
SELECT UPPER(LEFT('character',1))+ (RIGHT('character',8))
SELECT UPPER(LEFT('character',1)) + LOWER(SUBSTRING('character',2,9))     
-- Üstte burda tek string yerine bir sütun olsaydı(Yani string uzunluğunu bilmeseydim, 9 yerine her bir string için farklı değer girmem gerekirdi. Çözüm;
SELECT UPPER(LEFT('character',1)) + LOWER(SUBSTRING('character',2,LEN('character')))
-- Concat ile bakalım
SELECT CONCAT (UPPER(LEFT('character',1)) , LOWER(SUBSTRING('character',2,LEN('character'))))  -- DIKKAT: Arada artı yerine virgül var burada
"""

############################################################################################################################
#%% SQL-5
########## STRING FUNCTIONS 4
# NOT      : Özellikle text datalarda bir hücredeki girdinin bazen başında ya da sonunda boşluklar olabiliyor
#          .. Bunlar bazen eşitlemede, sorguda ya da join vs yaparken sorun çıkartabiliyor. O yüzden TRIM fonk. kullanıyoruz
# TRIM()   : Verinin başında ve sonundaki boşlukları temizler
# LTRIM()  : Sadece solundaki boşlukları siler
# RTRIM()  : Sadece sağdaki boşlukları siler
"""
SELECT ' CHARACTER'                          -- CHARACTER yazısının başında boşluk var, çıktıda hala görünüyor
SELECT TRIM(' CHARACTER')                    -- CHARACTER yazısının başında boşluk vardı, çıktıda gitti
SELECT TRIM(        '       CHAR ACTER X')   -- Tek tırnaktan önce yazılan boşlukların anlamı yok, tırmaktan sonra text ifadenin başladığını biliyor fonksiyon
----------------------------------------
-- TRIM diğer kullanım
SELECT TRIM('X' FROM 'ABCXXDE')										  --  Output : ABCXXDE      -- Kenarlarda "X" varsa kırp
SELECT TRIM('X' FROM 'XXXXXXXABCXXDEXXXXX')							  --  Output : ABCXXDE      -- Kenarlarda "X" varsa kırp
SELECT TRIM('ABC' FROM 'CCCCBBBAAAFRHGKDFKSLDFJKSDFACBBCACABACABCA')  -- Output : FRHGKDFKSLDFJKSDF 
-- Kenarlarda A,B ve C ler herhangi biri araya başka harf girmeden varsa kırp
SELECT TRIM('ABC' FROM 'CCCCBBBXAAAFRHGKDFKSLDFJKSDFACBBCACABACABCA') -- Output : XAAAFRHGKDFKSLDFJKSDF -- NOT: Araya X gelince çıktı değişti
----------------------------------------
SELECT LTRIM ('     CHARACTER ')		  -- Sadece soldaki boşluklar gitti çıktıda
SELECT RTRIM ('     CHARACTER ')           -- Sadece sağdaki boşluklar gitti çıktıda
"""

########## STRING FUNCTIONS 5
# REPLACE() : Bir textin içerisindeki ifade yerine başka bir ifade yazmamızı sağlar
# STR()     : Nümerik sayının string e çevrilmesini istersek kullanıyoruz
"""
SELECT REPLACE('CHARACTER STRING', ' ', '/')                         -- output: CHARACTER/STRING 
-- 'CHARACTER STRING' içinde Boşluk varsa, bunu slash(/) ile değiştir 
SELECT REPLACE('CHARACTER STRING', 'CHARACTER STRING', 'CHARACTER')  -- Output: CHARACTER        
-- 'CHARACTER STRING' içinde 'CHARACTER STRING' varsa, bunu 'CHARACTER' ile değiştir 
-----------------------------------------
-- String fonksiyonu bize 10 karakterlik text döndürüyor. Mesela 10 dan fazla yazarsak
SELECT STR (5454)                   -- Output:       5454  -- Output da dtype: Text # NOT: başına 6 boşluk ekleyip sonra texte çevirdi
SELECT STR (1234567890123456)       -- Output: **********  -- 10 karakter döndürmek yerine SQL çıktı vermenin mantıksız olacağını düşünüp 10 tane * veriyor
SELECT STR (2135454654)             -- Output: 2135454654  -- Output da dtype: Text           
SELECT STR (133215.654645, 11, 3)   -- Output: 133215.655  -- Toplam 11 karakter olsun(boşluklarla vs), 3 karakterde virgülden sonra olacak 
-- Sonu 655 geldi çünkü sondaki 4 ü 5 e yuvarladı  -- Not: Burada noktayıda 11 in içine dahil ediyor
"""

#############################
# 3.OTHER FUNCTIONS
# ÖNEMLİ NOT:sampleretail --Programmability-functions--system functions -- Other functions. Burada çıkanlar tanımlanmış fonksiyonlardır

########## OTHER FUNCTIONS 1
# CAST()    : Bir ifadenin başka bir veritipine dönüştürülmesini sağlıyor. Mesela text ile numeric i concat ederken işe yarıyor
# CONVERT() : Tanımlanmış cast işlemleri. Tarih veriyorum. Bunların içinden  belii parçasını getir. Veri tipini döndürmeyede yarar. Örneklerde göreceğiz
            # CONVERT özellikle tarih veritiplerinde kullanırız
"""
SELECT CAST (12345 AS CHAR)  -- Output: 12345   integer ı string e çevirdik   
SELECT CAST (123.65 AS INT)  -- Output: 123     float ı integer a çevirdi               
-----------------------------------------
SELECT CONVERT(int, 30.60)                              -- Output: 30                       -- integer veritipinde bir sonuç istiyoruz       
SELECT CONVERT(VARCHAR(10), '2020-10-10')               -- Output: 2020-10-10               -- VARCHAR(10) veritipinde bir sonuç getirdi    
SELECT CONVERT(DATETIME, '2020-10-10')                  -- Output: 2020-10-10 00:00:00:000  -- DATETIME veritipinde bir sonuç getirdi      
SELECT CONVERT(NVARCHAR, GETDATE(),112)                 -- Output: 20220606                 -- NVARCHAR veritipinde bir sonuç getirdi   -- 112 formatında(YYYYMMDD)(bkz str 464)   
-----------------------------------------
SELECT CAST('20201010' AS DATE)                         -- output: 2020-10-10
SELECT CONVERT(NVARCHAR, CAST ('20201010' AS DATE),103) -- output: 10/10/2020               -- NVARCHAR veritipinde bir sonuç getirdi 
-- NOT: Yazdığımız sorgunun veritipini görme ; Sorgunuzu tablo olarak create edip sonrasında sp_help 'dbo.table_name' yazdığınız zaman görürüz
"""

########## OTHER FUNCTIONS 2
# COALESCE    : Bir takım girdileriniz var bazılarını boş olabilir. Siz ilk dolu olanı almak istediğinizde kullanıyorsunuz
# ISNULL()    : 2 parametre yazacağız mesela birinci parametre NULL sa ikinci parametreyi getirecek
              # ÖRN: Öğrenci yaş ortalamasını al diyeceğiz mesela. NULL olmayan değerlerin ortalamasını al derken bunu kullanacağız.
# NULLIF()    : 2 değerin birbirine eşit olup olmaması. Eşitse boş değer döndürmesini, eşit değilse ilk dolu olanı getirmesini istersek bu fonksiyonu kullanıyoruz
# ROUND()     : Float veritipinde virgülden sonra Round diyerek yuvarlayabilmemizi sağlar
# ISNUMERIC() : Tablo içerisinde değerleri ortalama işlemine dahil etmek istiyorsunuz ama içerde karakterler içerde karışmış olabilir
# .. bundan önce bu veri nümeric mi değil mi derken bu fonk. kullanıyoruz
"""
SELECT COALESCE(NULL,'Hi','Hello',NULL)  -- Output: Hi  -- En az 2 parametre atamalıyız parantez içine 
-----------------------------------------
select ISNULL(NULL,'No')        -- Output: No
select ISNULL(11,10)            -- Output: 11
select ISNULL(10,11)            -- Output: 10
-----------------------------------------
SELECT NULLIF (10,10)           -- Output: NULL
SELECT NULLIF (10,11)           -- Output: 10
SELECT NULLIF(ISNULL(11,10),10) -- Output: 11
-----------------------------------------
SELECT ROUND (432.368, 2,0)     -- Output: 432.370  -- Virgülden sonraki 2 karaktere göre yuvarla. Yani 368 i 37 ye yuvarladı
-- Buradaki 0 yazan yer : 0 ya da 1 değer alıyor    -- default olarak 0 alıyor yukarı yuvarlar. 1 yazarask aşağı yuvarlar
-----------------------------------------
SELECT ISNULL(NULL, 'ABC')      -- Output: ABC
SELECT ISNULL('', 'ABC')        -- Output: (Boş geldi)  # Dikkat: burada ilk parametre NULL DEĞİL
-----------------------------------------
SELECT ISNUMERIC(123)           -- Output: 1  -- 1:True
SELECT ISNUMERIC('ABC')         -- Output: 0  -- 0:False
"""

#############################
# JOINS : Birden fazla tablonun birleştirilmesi. Ona göre sorgu yazacağız
########## 
# 1.INNER JOIN : 2 tane tabloda ortak olan satırları döndürür   
        # SELECT COLUMNS FROM table_A INNER JOIN table_B ON join_conditions
        # join_conditions: Mesela 1. tablodan gelen TC ile 2. tablodan gelen TC lerinin eşit olanları getir
        # Birden fazla tabloyu conditionlar ile join etmek istersek;
        # SELECT COLUMNS FROM table_A INNER JOIN table_B ON join_conditions1 AND join_conditions2 INNER JOIN table_C ON join_conditions3 OR join_conditions4 ...
"""
-- Soru: Select product ID, product name, category ID and category name and make join example 
SELECT	A.product_id, A.product_name, B.category_id, B.category_name
FROM	product.product AS A
INNER JOIN product.category AS B
ON A.category_id = B.category_id
-----------------------------------------
-- Soru: List employees of stores with their store information. select employee name, surname, store names
SELECT	A.first_name, A.last_name, B.store_name
FROM	sale.staff AS A
INNER JOIN sale.store AS B
ON A.store_id = B.store_id

-- NOT:Bu 2 tablo arasında ilişki olmak zorunda değil ,örneğin staff ile customer tablosunda last_name e göre join yapabiliriz
-- .. ve bunlar arasında direk ilişki yok diagrama bakarsak. Sadece önemli olan veri tiplerinin eşit olması
"""
##########
# 2.LEFT JOIN  : 2 tane tabloda soldaki tabloyu baz alarak değerleri getiriyor. 
    # 2. tablodaki değerler 1. tablodada varsa getirir, yoksa NULL getirir
    # SELECT columns FROM table_A LEFT JOIN table_B ON join_conditions
"""
-- SORU: Write a query that returns products that have never been ordered. Select product ID, product name, orderID
SELECT A.product_id, A.product_name, B.order_id 
FROM product.product A
LEFT JOIN sale.order_item B 
on A.product_id = B.product_id
WHERE B.order_id is null    
-- WHERE B.order_id is null: B de order_id sinde veri olmayan satırlar -- 213 rows
-----------------------------------------
-- Soru: Report the stock status of the products that product id greater than 310 in the stores
-- .. Expected columns: product_id, product_name, store_id, product_id,
SELECT A.product_id, A.product_name, B.*
FROM product.product A
LEFT JOIN product.stock B 
on A.product_id = B.product_id
WHERE A.product_id >310 

-- 237 rows -- NOT: EĞER ; WHERE B.product_id >310 yazsaydık  # 159 rows gelecekti
-- Çünkü asıl sorgumuzda B den null lar geldi(B deki product_id den-4.sütun), B.product_id >310 yazınca null lar gelmedi
"""
##########
# 3.RIGHT JOIN   : 2 tane tabloda sağdaki tabloyu baz alarak değerleri getiriyor.
    # 1. tablodaki değerler 2. tablodada varsa getirir, yoksa NULL getirir
    # SELECT columns FROM table_A RIGHT JOIN table_B ON join conditions
"""
-- Önceki sorguyu right joinle yazalım 
-- DIKKAT: Burada product.stock --> A,product.product B --> Where şartında B.product_id gibi farklılıklar yaptık
SELECT B.product_id, B.product_name, A.*
FROM product.stock A
RIGHT JOIN product.product B 
on A.product_id = B.product_id
WHERE B.product_id >310 

-- Aynı çıktı geldi. 237 rows
"""    
##########
# 4.FULL OUTER JOIN: 2 tabloyu join edeceğiz 1. tabloda olup 2. tabloda olmayan, 2.tabloda olup 
# .. 1. tabloda olmayan ve 2 tabloda da olanlar var.Bu 3 durum birleşip olarak hepsini getirir
"""
--Soru: Write a query that returns stock and order information together for all products(top100)
--expected columns product_id, store_id, quantity, order_id, list_price
SELECT TOP 100 A.product_id, B.store_id, B.quantity, C.order_id, C.list_price
FROM product.product A
FULL OUTER JOIN product.stock B
ON A.product_id = B.product_id
FULL OUTER JOIN sale.order_item C
ON A.product_id = C.product_id
ORDER BY B.store_id               

-- ORDER BY B.store_id:  NULL ları net görmek için bunu yazdık(Top 100 yazmasakta görebiliriz)
-- 443 numaralı product_id(product tablosunda) -- Bu ürün stocklarda bulunmuyor, bu ürünün siparişide söz konusu olmamış vs
"""
##########
# 5.CROSS JOIN
# İki tablonun birbirleriyle kartezyen olarak çarpılması. Bütün varyasyonları görmek istiyorsak bunu kullanıyoruz
"""
-- Soru: In the stocks table, there are not all products held on the product table and 
-- .. you want to insert these products into the stock table.
-- .. You have to insert all these products for every three stores with '0(zero)' quantity

SELECT	B.store_id, A.product_id, 0 quantity
FROM	product.product A
CROSS JOIN sale.store B
WHERE	A.product_id NOT IN (SELECT product_id FROM product.stock)  
ORDER BY A.product_id, B.store_id 

-- WHERE A.product_id NOT IN (SELECT product_id FROM product.stock) : product_id stock tablosunda olmayan ürünleri
-- ..  listele.Yani mesela 443 product_id nin quantity si 0. Bu ürünler stocklarda bulunmuyor, bu ürünün siparişi söz konusu olmamış.
-- 0 quantity : Tüm satırlara 0 yazılması için sabit bir değer verdik quantity den önce
-- NOT: Buradaki "quantity" bir isimlendirmeden ibaret. oraya "miktar" da yazabilirdik. 
-- .. O yüzden A.quantity, B.quantity yazılması gerekiyor gibi bir şey değil orası 
"""

############################################################################################################################
#%% SQL-6
#############################
# VIEWS
    # 1.Bir tablonun görüntüsünü oluşturuyoruz. Bu görüntü fiziksel olarak ayrı bir yer kaplamıyor. Tablolara bağlantı sağlıyor
    # 2.Bir sorgumuz var. Çok uzun bu sorgu ama ihtiyaç duyuyoruz diyelim. Bunu farklı bir yerde bir kural olarak tanımlarsak
        # .. Bu view üzerinden daha rahat bir şekilde sorgumuzu yapabiliriz
    # CREATE VIEW view_name AS SELECT columns from tables [WHERE conditions];
# Advantages of Views: Performance(Uzun sorguyu view olarak kaydedip kullanma), Security, Storage, Simplicity
"""
-- Soru: Ürün bilgilerini stok miktarları ile birlikte listeleyin product_id 310 büyük olanlar demiştik önceki derste
-- Soru şuydu Report the stock status of the products that product id greater than 310 in the stores
SELECT	A.product_id, A.product_name, B.*
FROM	product.product A
LEFT JOIN product.stock B ON A.product_id = B.product_id
WHERE	A.product_id > 310;
-----------------------------------------
-- Bu sorguyu bir view olarak kaydedelim
CREATE VIEW ProductStock AS
SELECT	A.product_id, A.product_name, B.*
FROM	product.product A
LEFT JOIN product.stock B ON A.product_id = B.product_id
WHERE	A.product_id > 310;
-- Hata Column names in each view or function must be unique. product_id 2 kere geçiyor
-----------------------------------------
CREATE VIEW ProductStock AS
SELECT	A.product_id, A.product_name, B.store_id,B.quantity
FROM	product.product A
LEFT JOIN product.stock B ON A.product_id = B.product_id
WHERE	A.product_id > 310;
-- Command completed sucsesfully
-- sampleretail-views-dbo.ProductStock
-----------------------------------------
-- Bunu sorgularımın içinde tablo olarak kullanabilirim
SELECT * FROM dbo.ProductStock -- Sorgu sonucunun aynısı geldi
-----------------------------------------
-- Koşul da ekleyebiliriz
SELECT * FROM dbo.ProductStock WHERE store_id=1
-----------------------------------------
# NOT: Bunu tek sorgu için yapabiliriz. Daha fazla sorgu için "procedure" kullanacağız ilerde
# NOT: ProductStock sadece bir script, asıl tabloyla olan bir ilişkisi var. Depolamada büyük katkısı var
# NOT: Bunu tablo olarak create edemez miyiz? Edebiliriz. O tablo fiziksel bir tablodur, dinamik bir tablo olmaz
# NOT: Tablonun hep son durumu(değişmeden önceki(eğer değiştiyse)) ile ilgili bilgi almak istersem view kullanmalıyız
# DIKKAT: VIEW içerisinden ORDER BY kullanamayız(VIEW OLUŞMAYACAKTI). VIEW oluştuktan sonra ORDER BY ı kullanabiliriz
# NOT: VIEW içinde oluşturulan sorguyu görmek için sampleretail-->view-->dbo.ProductStock--> sağ tık-->design
-------------------------------------------------
-- Soru: Mağaza çalışanlarını çalıştıkları mağaza bilgileriyle birlikte listeleyin. Çalışan adı, soyadı, mağaza adlarını seçin
CREATE VIEW SaleStaff as
SELECT  A.first_name, A.last_name, B.store_name
FROM    sale.staff A
INNER JOIN sale.store B
    ON  A.store_id = B.store_id
-----------------------------------------
Select * from SaleStaff
-----------------------------------------
-- VIEW gibi başka bir kullanım;
SELECT	A.product_id, A.product_name, B.store_id, B.quantity
INTO	#ProductStock
FROM	product.product A
LEFT JOIN product.stock B ON A.product_id = B.product_id
WHERE	A.product_id > 310;

SELECT * FROM #ProductStock;
-- Bu da diez ile bir bağlantı ile oluşturulan geçici view. Bağlantı kapanınca bu gider
"""

#############################
# ADVANCED GROUPING FUNCTIONS
# Table of Contents
# 1.Having clause,  2.Grouping sets,  3.Rollup, 4.Cube, 5.Pivot
# NOT: SQL SERVER OKUMA SIRASI: FROM--> WHERE --> GROUP BY --> HAVING -- > SELECT --> ORDER BY
# Önce group by mantığını anlayalım. Sonra konulara geçelim
"""
-- Soru: Kaç farklı markaya ait ürünüm var
Select brand_id, count(*) as CountOfProduct from product.product
group by brand_id
-- Count(*): Satırın tamamını sayar, eğer eksik verisi olan satıra count dersek eksik kalabilir
-----------------------------------------
-- Soru: Kategori bazındaki toplam ürün sayısı
SELECT A.category_id, B.category_name, count(*) CountOfProduct from product.product A
INNER JOIN product.category B
ON A.category_id = B.category_id
group by A.category_id, B.category_name
-----------------------------------------
-- Soru: Her bir siparişteki toplam fiyat. (discount' ı ve quantity' yi ihmal etmeyiniz.)
SELECT	order_id, SUM((list_price * quantity)*(1-discount)) Net_Price 
FROM sale.order_item
GROUP BY order_id
"""
##########
# 1.Having Clause
# Group by lı sorgu sonucunda olan filtrelemeleri HAVING ile yapıyoruz

"""
-- Soru: Model yılı 2016 dan büyük olan ürünlerin liste fiyatlarının ortalamasının 1000 den fazla olduğu markaların fiyatlarını listeleyin
-- NOT: INNER JOIN yerine alltaki şekilde virgül koyarak yapabiliriz
select	b.brand_name, avg(a.list_price) AS AvgPrice
from	product.product a, product.brand b
where	a.brand_id = b.brand_id
		and a.model_year > 2016
group by b.brand_name
having avg(a.list_price) > 1000
order by 2 DESC
-- NOT: AVG(A.list_price) ifadesine, Alias vermiş olsaydık bunu Having kısmında kullanamam
-----------------------------------------
-- Soru: Write a query that checks if any product id is repeated in more than one row in the products table
-- Products id si 1 den fazla olan satır var mı
SELECT	product_id, COUNT (product_id) num_of_rows FROM	product.product
GROUP BY product_id
HAVING COUNT (product_id) > 1
-- Product_id ler product tablosunda unique olduğu için her değerden 1 tane gelecek. Dolayısıyla 1 den büyük yok ve çıktı boş
-----------------------------------------
-- Soru: max liste fiyatı 4000 üstü, min liste fiyatı 500 altında olan category_id leri getirin
SELECT	category_id, Min(list_price) min_ , Max(list_price) max_  FROM	product.product
GROUP BY category_id
HAVING Min(list_price) <500 or Max(list_price) > 4000
"""

##########
# 2.Grouping sets
# Raporlama yaparken tüm gruplama sonuçlarının tek bir sorguda getiriyoruz
# grouping sets e yazdıklarımı grupluyorum, her bir satır sonuçları ve toplamları
# NOT: Her bir grup kombinasyonunu oluşturup ona göre sonuç getirir(Grouping sets, Rollup, Cube benzer çıktılar farklı formatlarda getirir)
# SELECT column1, column2, aggregate_fucntion(column3) FROM table_name Group by GROUPING SETS...

"""
-- Herbir kategorideki toplam ürün sayısı
-- Herbir model yılındaki toplam ürün sayısı
-- Herbir kategorinin model yılındaki toplam ürün sayısı

-- group by ile ; 
select	category_id, model_year, count(*) CountOfProducts
from	product.product
group by category_id, model_year
--- burada sütunlardaki grup setlerin satır toplamlarını getirtemedik.(Tam tanım bu değil ama model_year sütununa bakınca anlayabiliriz)
-- 37 rows. Alttaki çıktı 54 rows, Aradaki fark 17 rows NULL lar(Aslında grupların toplamlarını getiren satırlar)

-- grouping sets
select	category_id, model_year, count(*) CountOfProducts
from	product.product
group by
	grouping sets (
				(category_id), -- 1. group
				(model_year),  -- 2. group
				(category_id, model_year) -- 3. group
	)
order by 1, 2
-- NOT: "having model_year is null"  gibi filtrelemede ekleyebiliriz
"""
##########
# 3.Rollup
# Sorgunun sonucunu istediğimiz sırada sonuç getirir
# Her bir grup kombinasyonunu oluşturup ona göre sonuç getirir
# Select d1,d2,d3,aggregate_function(c4) FROM table_name Group by rollup(d1,d2,d3)
# NOT: Her bir grup kombinasyonunu oluşturup ona göre sonuç getirir(Grouping sets, Rollup, Cube benzer çıktılar farklı formatlarda getirir)
"""
Select category_id,model_year, count(*) FROM product.product Group by rollup(category_id,model_year)

-- GROUPING SETS ile hemen hemen(50 rows biri, diğeri 51rows-NULL toplam eklenince) aynı çıktı altta
-- (rollup içine yazdıklarımızı ekliyoruz grup olarak)
select	category_id, model_year, count(*) CountOfProducts
from	product.product
group by
	grouping sets (
				(category_id),
				(category_id, model_year))
order by 1, 2
-----------------------------------------
-- Soru: Her bir marka id, her bir category id ve her bir model yılı için toplam ürün sayılarını getiriniz. Sonuç tablosunda tüm ihtimaller bulunsun
Select category_id,brand_id,model_year, count(*) FROM product.product Group by rollup(category_id,brand_id,model_year)

-- GROUPING SETS ile benzer çıktı altta (rollup içine yazdıklarımızı ekliyoruz grup olarak)
select	category_id, brand_id, model_year, count(*) CountOfProducts
from	product.product
group by
	grouping sets (
				(category_id),
				(category_id,brand_id,model_year))
order by 1, 2
"""

##########
# 4.CUBE
# Roll up category_id: 1-1-1-1-2-2-2-2    model_year: 2018-2019-2020-2021-2018-2019-2020-2021 gibi yapıyor
# CUBE category_id:  1-2-3-4-1-2-3-4      model_year: 2018-2018-2018-2018-2019-2019-2019-2019 gibi ...
# NOT: Her bir grup kombinasyonunu oluşturup ona göre sonuç getirir(Grouping sets, Rollup, Cube benzer çıktılar farklı formatlarda getirir)
"""
-- Soru: Her bir category id ve herbir model yılı için toplam ürün sayılarını getiriniz.
Select category_id,model_year, count(*) FROM product.product Group by CUBE(category_id,model_year)  
 -- 55 rows model_year 14 Null, category_id 5 Null(Mantıklar benzer. Çıktılar farklı)
Select category_id,model_year, count(*) FROM product.product Group by rollup(category_id,model_year)
 -- 51 rows model_year 14 Null, category_id 1 Null(Mantıklar benzer. Çıktılar farklı)
"""

##########
# 5.PIVOT
# SQL de her bir sütun başlığını tanımlamamız gerekiyor. Python la aynı sonucu veriyor
# Pivota taşıyacağımız sütunları biliyorsak python da yapılabilir.
"""
--  Model year a göre ürün sayısı. Normalde bunu nasıl yapıyorduk
Select model_year,count(*) from product.product group by model_year
-- 2018 yılına ait 177 ürün , 2019 model yılına ait, 140 ürün varmış, 2020 yılı 121, 2021 yılı 82

--  Pivot table ile 
SELECT * FROM (SELECT product_id, Model_Year FROM product.product) A
PIVOT
(count(product_id) FOR Model_Year IN ([2018], [2019], [2020], [2021])
) AS PIVOT_TABLE
-- Not: Burada from dan sonraki subquery ye alias vermem lazım yoksa hata alıyoruz
-----------------------------------------
-- 3. değişken için

SELECT * FROM (SELECT category_id, Model_Year, product_id FROM product.product) A
PIVOT
(count(product_id) FOR Model_Year IN ([2018], [2019], [2020], [2021])
) AS PIVOT_TABLE

-- category_id index görevi gördü.
-----------------------------------------
-- ÜSTTEKİ KODUN SONUNA TOPLAMLARI DA YAZDIRMAK İSTERSEK..
SELECT * FROM (SELECT category_id, Model_Year, product_id FROM product.product) A
PIVOT
(count(product_id) FOR Model_Year IN ([2018], [2019], [2020], [2021])
) AS PIVOT_TABLE
UNION ALL
SELECT NULL, * FROM (SELECT product_id, Model_Year  FROM product.product) A
PIVOT
(count(product_id) FOR Model_Year IN ([2018], [2019], [2020], [2021])
) AS PIVOT_TABLE
"""
############################################################################################################################
#%% SQL-7
# SET OPERATIONS
# Birden fazla sorgunun tek bir sorgu sonucu olarak gözükmesi(Buna python da append diyebilirsiniz)
# Satırları alt alta gelecek şekilde birleştirmek, aralarındaki farkı almak, sorguların kesişimi, birleşimi vs için kullanıyoruz
    # Veri tipleri aynı olmalı
    # Sütun sayıları aynı olmalı
    # Bütün işlemleri yaptıktan sonra ORDER BY ı  kullanabiliyoruz(VIEW de de izin vermiyordu mesela)

##########
# 1.UNION
# İki veri setini alt alta eklemeye yarar
# Karşımıza çıkan veri seti DISTINCT bir veri setidir. Aynı satırdan 1 den fazla olmaz
    # SELECT emp_id, first_name, last_name, job_title from employees_A UNION SELECT emp_id, first_name, last_name, job_title from employees_B;
"""
TABLE_A      TABLE_B     TABLE_A UNION TABLE_B      
  A            C                    A
  B            D                    B
  C            E                    C
                                    D
                                    E
-- UNION sorgu sonucunda DISTINCT bir küme döndürür
"""
# -----------------------------------------
"""
-- Soru: Charlotte şehrindeki müşterilerle aurora şehrindeki müşterilerin soyisimlerini listeleyin
-- Normalde set operater kullanmadan da yapabiliriz ama biz burada göstermek için kullanacağız
SELECT last_name FROM sale.customer WHERE city ='Charlotte'      --- 49 rows
UNION
SELECT last_name soyisim FROM sale.customer WHERE city ='Aurora' --- 79 rows
-- SONUÇ: 105 rows geldi. UNION sorgu sonucunda DISTINCT bir küme döndürdü
-- NOT: Değişkenlerin sırası ve sayısı önemli, sütun ismini değiştirdiğimizde UNION ın üstündeki sütun ismini baz alır
-----------------------------------------
-- SORU: Çalışanların ve müşterilerin e-posta unique olacak şekilde listeleyiniz.
SELECT email FROM sale.staff     -- 10 rows
UNION
SELECT email FROM sale.customer  -- 2000 rows
-- 2004 rows
"""

##########
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
-- UNION ALL Duplicate yaptı. UNION dan farkı bu. DISTINCT yapmadığı için performansı ve hızı daha iyi
-- Ancak unique değerler istersek UNION kullanmalıyız
"""
# -----------------------------------------
"""
-- Soru: Müşterilerin içinde Thomas isminde olanlar veya soyismi thomas olanları getirelim
SELECT first_name FROM sale.customer WHERE first_name ='Thomas'        -- 10 rows
UNION ALL
SELECT last_name soyisim FROM sale.customer WHERE last_name ='Thomas'  -- 27 rows
-- 37 rows
"""

##########
# 3.INSERSECT
# iki tabloyu karşılaştırıp 2 tablo sonucunda ortak(Kesişim) olanı döndürüyor

"""
TABLE_A      TABLE_B     TABLE_A INTERSECT TABLE_B      
  A            B                    B
  B            D                    D
  D            E                    
""" 
# -----------------------------------------
"""
-- Soru: model_year ı hem 2018 yılında hem de 2019 yılında olan brand_id ler?
-- Not INNER JOIN yerine altta tablo arasına virgül koyarak yazabiliyorduk
SELECT A.brand_id, B.brand_name FROM product.product A, product.brand B
WHERE a.brand_id = b.brand_id AND a.model_year = 2018   -- 177 rows
INTERSECT
SELECT A.brand_id, B.brand_name FROM product.product A, product.brand B
WHERE a.brand_id = b.brand_id AND a.model_year = 2019   -- 140 rows
--35 rows. Toplamda 40 marka vardı
-----------------------------------------
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
-----------------------------------------
-- Üstteki sorguda müşterilerin yaptıkları siparişleri görüntüleyelim
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
-----------------------------------------
-- Soru: AURORA VE CHARLOTTE  da aynı soyisimli kişiler yaşıyor olabilir. Bunları bulalım.
-- Öncekinde UNION la yaptığımızda 105 rows gelmişti(bkz str 1024)
SELECT last_name FROM sale.customer WHERE city ='Charlotte'
INTERSECT
SELECT last_name FROM sale.customer WHERE city ='Aurora'
---- 9 rows
-----------------------------------------
-- Soru: Çalışanların ve müşterilerin ortak e-posta ları varsa bunları listeleyiniz.
SELECT email FROM sale.staff
INTERSECT
SELECT email FROM sale.customer
---- Boş
"""

##########
# 4.EXCEPT
# A kümesinde olup B kümesinde olmayan
"""
TABLE_A      TABLE_B     TABLE_A EXCEPT TABLE_B      
  A            B                    A
  B            C                    
  C            D                   
"""
# -----------------------------------------
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
-- 2 rows. Sadece 2 marka bu şarta uyuyor.
-----------------------------------------
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
-----------------------------------------
-- product_id ye göre 2019 yılında sipariş verilen diğer yıllarda sipariş verilmeyen ürünler
-- Bunu except ile yaptık üstteki sorguda. Bunu pivot table başka bir çıktıya bakalım. O 5 tane sonucu bu pivot çıktısında göreceğiz
-- .. burada  product_id ye göre bir nevi indexleme yaparak hangi product id den ne kadar ona bakıyoruz
SELECT * FROM
	 (SELECT	b.product_id, year(a.order_date) OrderYear, B.item_id FROM SALE.orders A, sale.order_item B
	 WHERE	A.order_id = B.order_id) A
PIVOT
(count(item_id) FOR OrderYear IN ([2018], [2019], [2020], [2021])
) AS PIVOT_TABLE
order by 1
----------------------------------------
-- Üstte pivot table ile gösterilen çıktıyu başka bir şekilde gösterelim
SELECT	b.product_id, year(a.order_date) OrderYear, COUNT(item_id) item_count 
FROM	SALE.orders A, sale.order_item B
where	A.order_id = B.order_id
group by b.product_id, year(a.order_date)
order by 1
----------------------------------------
-- SORU:brand ı getir, 2018 yılında herhangi bir ürünü ve 2019 yyılında herhangi bir ürünü olsn DEMİŞTİK INTERSECT te
-- 40 satırdan 35 rows dönmüştü. Şimdi onu bir alt sorgu olarak kullanarak  Bunların dışında kalan 5 ürünü bulmak istiyoruz
select	brand_id, brand_name
from	product.brand
EXCEPT
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
-----------------------------------------
"""

##########
# 5.CASE Expression
# Yeni bir sütun oluştururken başka bir sütunu referans gösteriyorsak kullanıyoruz
# Yeni sütunda, örneğin departmanda DS e , "Data science", diğerlerine "others" yazdırsın gibi...

#####
# A.SIMPLE CASE
"""
CASE case_expression
     WHEN ...
     WHEN ...
     end give_table_name
from	table_1
"""
# -----------------------------------------
"""
--- SORU: Generate a new columns containing what the meaning of the values in the Order_Status column
--- 1.Pending 2.Processing 3.Rejected, 4.Completed
select	order_id, order_status,
		CASE order_status               -- hangi sütuna göre koşul
			when 1 then 'Pending'
			when 2 then 'Processing'
			when 3 then 'Rejected'
			when 4 then 'Completed'
		end order_status_desc            -- yeni sütun ismi
from	sale.orders
-- order_status = 1 ise bunu "Pending", 2 ise "Processing", 3 ,se 'Rejected', 4 se 'Completed' olarak yaz..
-- NOT: Bu kalıcı bir değişiklik yapmıyor tablolarda
-- DDL kodlarıyla tablomuza yeni alan ekleriz sonra bu sorguyla update ederiz bu değerler veritabanımızda kalır
-----------------------------------------
--- SORU: Add a column to sale.staff table containing the store names of the employees
--- Bunu normalde kendimiz staff ve store kullanarak alabiliriz ama bunu CASE ile yapalım
--- 1.Davi techno Retail; 2.The BFLO Store 3.Burkes Outlet
SELECT first_name, last_name, store_id,
	CASE store_id                         -- hangi sütuna göre koşul
		WHEN 1 THEN 'Davi techno Retail'
		WHEN 2 THEN 'The BFLO Store'
		WHEN 3 THEN 'Burkes Outlet'
	END AS store_name                     -- yeni sütun ismi
FROM sale.staff

-- Bu simple case di  sonra searched case e geçeceğiz
-- Burada 1 değişken var buna eşitliğine bakıyoruz 1 ise şunu yap, 2 ise şunu yap vs gibi
-- searched case de 0 ile 1000 arasındaysa şu, 1000 ile 2000 arasınysa şu ya da detaylı koşul varsa search case yapıyoruz
"""

#####
# B.SEARCHED CASE
# NOT: Burada -- hangi sütuna göre koşul diye when den sonra belirtiyoruz(simple case de when den önce case den sonraydı)
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
--- Bu "WHEN" kısımları Boolean bir değer döndürüyor gibi düşünebiliriz
--- Başka bir alternatif yok(order_status ü 5 olan yok mesela) ama olsaydı else 'other' yazarak diğerlerine "other" yazdır dedik
-----------------------------------------
-- SORU:  Müşterilerin e-mail adreslerindeki servis sağlayıcılarını yeni bir sütun oluşturarak belirtiniz.
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
-----------------------------------------
-- Soru: Aynı siparişte hem mp4 player, hem Computer Accessories hem de Speakers kategorilerinde ürün sipariş veren müşterileri bulunuz.
-- Önce bu kategoriler veritabanında nasıl yazılıyor bakalım
Select * from product.category A, product.product B, sale.order_item C
WHERE A.category_name in ('Computer Accessories','Speakers','mp4 player') AND
A.category_id = B.category_id AND
    B.product_id = C.product_id

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
-- 20 rows
--- Bir de bu siparişi veren kişilerin isim soyisimleri alalım. Bunu nested query yapıp isimleri getirelim sipariş no dan siparişi veren kişilere gideceğiz 
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
-- 20 rows
"""
############################################################################################################################
#%% SQL-8
# SUBQUERIES/INNER QUERY/NESTED QUERY
# Subquery, başka bir query içerisinde bir parantez içinde tanımlanmış alt query dir
# Select bloğunda, where bloğunda ve from bloğunda kullanabiliyoruz. Sonuç tablo mu, değer mi olduğuna göre kullanım yeri değişmektedir
# FROM da olursa--> tablo döndürür
# SELECT, WHERE --> tablo veya value dönebilir
"""
-- SELECT
Select order_id, list_price,
(select avg(list_price) from product.product) AS avg_price
from sale.order_item
-- Tek bir değer kullandığım için select bloğunda kullandım
-- Sonuçta bütün satırlarda aynı değerin dönmesini istiyorsak select bloğu içerisinde kullanabiliriz subquery yi
-----------------------------------------
-- WHERE 
Select order_id, order_date from sale.orders
where order_date IN (select TOP 5 order_date from sale.orders ORDER BY order_date DESC) -- Siparişin verildiği son 5 gün
-- Eğer aynı tarihler gelmiş olsaydı, tekilleştirmek isteseydik;
select Top 5 order_date from 
(Select distinct order_date from sale.orders) A
where order_date IN (select TOP 5 order_date from sale.orders ORDER BY order_date DESC) 
-----------------------------------------
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
    # Correlated subquery çok performanslı değil, çok kullanılmıyor, joinlerle daha iyi sonuçlar geliyor

##########
# 1.SINGLE-ROW SUBQUERIES
    # Bir sütun bir hücre döndürüyor
    # Karşılaştırma yapacağımız değerler arasında =,>,>=,<= gibi karşılaştırma araçları kullanıyoruz
    # where ve select ile kullanılabiliyor
    # Bir çok query joinle kullanılabiliyor. Hangi durumda daha anlamlı bir query yazacaksa ihtiyaca göre
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
-----------------------------------------
-- NOT
-- IKİ kod ARASINDAKİ FARKIN NEDENLERİNIN MANTIKSAL AÇIKLAMASI ???
-- 1. KOD
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
-----------------------------------------
-- Soru :Davis Thomas'nın çalıştığı mağazadaki tüm personelleri listeleyin
select	*
from	sale.staff
where	store_id = (
					select	store_id
					from	sale.staff
					where	first_name = 'Davis' and last_name = 'Thomas'
					)
-- subquery -- davis thomas ın çalıştığı store_id
-----------------------------------------
--- alternatif çözüm
select *
from (
    select store_id
    from sale.staff
    where first_name = 'Davis' and last_name= 'Thomas'
) as a, sale.staff b
where a.store_id = b.store_id
-----------------------------------------
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
-- manager_id  = :  manager_id si sale.staff dan  where first_name = 'Charles' and last_name = 'Cussona' şartını sağlayan ı getirdik
-----------------------------------------
-- Soru: -- 'Pro-Series 49-Class Full HD Outdoor LED TV (Silver)' isimli üründen daha pahalı olan ürünleri listeleyin.
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
##########
# 2.MULTIPLE ROW SUBQURIES
    # Tek fark; Sonuç olarak birden fazla satır dönmesi. O yüzden direk büyüktür, küçüktür gibi operatörler kullanamayız direkt olarak
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

-- Subquery ile outer query arasında bir ilişki tanımlamadık
-- Burada subquey tek başına çalışıyor çünkü subquey içinden SO.order_date veya SC.customer_id yazarken
-- SO ve SC ile tabloları subquery içinde tanımlandığı için hata veremiyoruz
-- Önce Laurel Goldammer alışveriş yaptığı tarihleri istiyorum.
-- Önce customer tablosundan isim buluyorum, sipariş bilgileri orders tablosunda
-- hangi müşterinin hangi tarihlerde alışveriş yaptığını alttaki sorgu sonucunda elde ettim
-- select * from sale.customer A, sale.orders B where A.customer_id = B.customer_id
-- Bütün müşterilerden Laurel goldammer ı seçiyoruz WHERE first_name = 'Laurel' AND last_name='Goldammer'
-- Bu subqueyden bir satır dönseydi eşittir operatörü kullanacaktık ama burada eşittir kullanamayacağım
-- O yüzden burada "IN" operatörünü kullandık.
-- WHERE order_date IN: outer query de bu tarihlerden(subquery sonuçlarından) herhangi birisi olmalı
-- AND SO.order_status = 4 : Alışverişi tamamlayanlar
-----------------------------------------
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
-----------------------------------------
------ Alternatif yol : NOT IN yerin IN ,  IN yerinde NOT IN getirerek yapabiliriz
select	*
from	product.product
where	model_year = 2021 and
		category_id IN (
						select	category_id
						from	product.category
						where	category_name NOT in ('Game', 'GPS', 'Home Theater')
						)
-----------------------------------------
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
-----------------------------------------
-- 2. yol -- Eğer subquery tek değer döndürmüyorsa , IN, NOT IN , > ALL vs gibi şeyler kullanıyoruz
select * from	product.product
where	model_year = 2020 and
		list_price > ALL (
			select	B.list_price
			from	product.category A, product.product B
			where	A.category_name = 'Receivers Amplifiers' and
					A.category_id = B.category_id
			)
-- Burada çoklu satır döndürür subquery o yüzden ">" operatörünü kullanamayız. "> ALL" kullanmalıyız
-- Subquery den dönen bütün hepsinden büyük mü diye bakıyor.(97.13 den , 105 den büyük mü vs mi diye bakıyor)
-- 6 ürünümüz , bizim ürünümüzün bulunduğu kategorideki bütün ürünlerin fiyatlarından büyük
-- ALL () : Subquery içinden dönen tüm değerlerden büyük olan
-----------------------------------------
-- Soru: List products made in 2020 and its prices more than "any" products in the Receivers Amplifiers category
-- 1. yol -- minimum liste fiyatını çekip 
select	*
from	product.product
where	model_year = 2020 and list_price >
(select	min(B.list_price)
 from	product.category A, product.product B
				where	A.category_name = 'Receivers Amplifiers' And
                        A.category_id = B.category_id
						)   ---  A.category_name = 'Receivers Amplifiers' deki en pahalı fiyat
-----------------------------------------
-- 2. yol
select * from	product.product
where	model_year = 2020 and
		list_price > ANY (
			select	B.list_price
			from	product.category A, product.product B
			where	A.category_name = 'Receivers Amplifiers' and
					A.category_id = B.category_id
			)
-- bizim ürünümüzün categorysindeki minimum fiyatı baz almamız lazım bunu "> ALL" yerine "> ANY" yazarak sağlayabiliriz
-- ANY () : Subquery içinden dönen herhangi bir değerlerden büyük olan
-- Burada SON 2 örnekte yukarda ki çözümlerden 1. yolu kullanmamız performans açısından daha iyi olacaktır
-- Bu bir text verisi ise ya da farklı tablolardan gelen UNION lardan oluşan bir veri setiyse
-- Yani group by la bir değer çıkartmanın mümkün olmadığı durumlarda 2. yolu kullanmalıyız
"""

############################################################################################################################
#%% SQL-9

##########
# 3.CORRELATED SUBQUERIES
    # Çok yaygın kullanılır. 2 fonksiyon var burada. 1.Exist 2.not-exist
    # EXIST : tabloya bir sorgu atıyoruz. A tablosunda bu kayıtların başka bir yerde bulunup
        # .. bulunmadığına bakıyoruz. Bir alan çekmiyorsunuz oradan. Sadece var mı yok mu buna bakıyoruz. Bir check etme işlemi yani
    # NOT EXIST : Tam tersi 2. tabloda olmama durumunu test ediyorsunuz
"""
-- EXIST
Select * from sale.customer WHERE EXISTS(SELECT 1)
-----------------------------------------
SELECT * from sale.customer A WHERE EXISTS (SELECT 1 FROM sale.orders B WHERE B.order_date > '2020-01-01' AND A.customer_id=B.customer_id)
-- Bana sadece 2020 ocak 1 den sonra sipariş veren müşteri bilgilerini(SELECT * from sale.customer) göster
-- SELECT 1: Buradaki 1 in hiç bir anlamı yok
----------------------------------------------------------------------------------
-- NOT EXIST
Select * from sale.customer WHERE NOT EXISTS(SELECT 1)
-----------------------------------------
SELECT * from sale.customer A WHERE NOT EXISTS (SELECT 1 FROM sale.orders B WHERE B.order_date > '2020-01-01' AND A.customer_id=B.customer_id)
-- Bana sadece 2020 ocak 1 den sonra sipariş vermiş OLMAYAN müşteri bilgilerini(SELECT * from sale.customer) göster
-- Soru: Bu sorguda diyelim biri yeni kaydedilmiş ve siparişi olmamış. Bu sorgu sonucunda bu müşteri gelir mi gelmez mi ?
-- ... Kriter şu burada: Customer tablosuna gidiyor her bir satır için customer_id 1 sonra order tablosuna gidiyor orders ı varsa alıyor yoksa almıyor
-- ... inner query içinde varsa o kişiyi alıyor yoksa eliyor. Yani gelmesi lazım
"""
# -----------------------------------------
"""
-- Soru: Apple - Pre-Owned iPad 3 - 32GB - White ürünün hiç sipariş verilmediği eyaletleri bulunuz.
-- Eyalet müşterilerin ikamet adreslerinden alınacaktır.
Select * from product.product WHERE product_name = 'Apple - Pre-Owned iPad 3 - 32GB - White'

-- Bu ürünün hangi siparişlerde verildiğini bir sorgulayayım sonra eyalet kısmına geçiş yapalım
select	distinct C.state
from	product.product P,
		sale.order_item I,
		sale.orders O,
		sale.customer C
where	P.product_name = 'Apple - Pre-Owned iPad 3 - 32GB - White' and
		P.product_id = I.product_id and
		I.order_id = O.order_id and
		O.customer_id = C.customer_id
-- Şimdi bana öyle eyaletler getirsin ki o eyaletlerde bu ürün satın alınmamış olsun
-- UNION la birleştirip olmayanları EXCEPT ile çıkartabiliriz vs ama şimdi biz NOT EXIST ile yapacağız burada

-- Exist içine yukarıdaki sorguyu yapıştırıyoruz outer query de from dan sonra sale.customer C2 dedik
-- .. Çünkü bir şart eklemeliyiz(Altta açıklanıyor)
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
-- Şartımız: C2.state = C.state : Yani, outer query de gelen statelerin inner query de olmama şartını inner query ye ekliyorum
-- EXIST ya da NOT EXIST i foreign keyler ya da primary keyler üzerinden yaparsak daha hızlı çalışır. Diğer türlü tüm tabloyu taraması gerekiyor
-----------------------------------------
-- Soru: Burkes Outlet mağaza stoğunda bulunmayıp, Davi techno mağazasında bulunan ürünlerin stok bilgilerini döndüren bir sorgu yazın
SELECT PC.product_id, PC.store_id, PC.quantity
FROM product.stock PC, sale.store SS
WHERE PC.store_id = SS.store_id AND SS.store_name = 'Davi techno Retail' AND
NOT EXISTS( SELECT DISTINCT A.product_id, A.store_id, A.quantity
FROM product.stock A, sale.store B
WHERE A.store_id = B.store_id AND B.store_name = 'Burkes Outlet' AND PC.product_id = A.product_id AND A.quantity>0)

-- Davi techno Retail da stoğu bulunnanları alacak. Burkes Outlet in stocklarında quantity>0 olanları not exists yapacak
-- quantityi belirtmeseydik;
-- çıktı hiçbir şey getirmedi. Buradan şu çıkıyor olabilir. Bu ürünlerin(Çıktıdaki 5 tane) Burkes outlet mağazaında satırları var
-- ancak bu ürünlerin stock miktarları 0.

-- Bütün ürünlerimin stock bilgisi stock tablosunda var. Burkes in stoğunda 0 olarak gözüken ürünlerden bul diye de sonuca ulaşabiliriz
-- Exists ve quantity=0 diyerek
SELECT PC.product_id, PC.store_id, PC.quantity
FROM product.stock PC, sale.store SS
WHERE PC.store_id = SS.store_id AND SS.store_name = 'Davi techno Retail' AND
EXISTS( SELECT DISTINCT A.product_id, A.store_id, A.quantity
FROM product.stock A, sale.store B
WHERE A.store_id = B.store_id AND B.store_name = 'Burkes Outlet' AND PC.product_id = A.product_id AND A.quantity=0)
-----------------------------------------
-- Soru: -- Brukes Outlet storedan alınıp The BFLO Store mağazasından hiç alınmayan ürün var mı?
-- Varsa bu ürünler nelerdir? Ürünlerin satış bilgileri istenmiyor, sadece ürün listesi isteniyor.



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
-- P.product_name: product name geliyor ancak bu aşağıdaki kurala uymalı(subquery de)
-- NOT EXIST Dediğine göre birşeyleri eleyeceğiz. (The BFLO Store mağazasından hiç alınmayan)
-- Elemek istediğimiz yer: P.product_id = I.product_id  bu kod.
-- Bütün product listemizde "The BFLO Store" dan sipariş edilmiş ürünleri eliyorum
-- Bir kriter daha vardı: Brukes Outlet storedan alınan o yüzden AND diyip EXISTS diyip devam ediyorum
-- Sonuç olarak 8 tane ürün geldi. 520 tane üründen 8 geldi. Tek sorguda product tablosunda istediğimiz 8 satırı seçmiş olduk
-----------------------------------------
-- Bunu yine EXCEPT ile yapabilirdik
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
"""

##########################################
# CTE(Common Table Expressions)
    # Bir VIEW gibi çalışırlar. Sorgu sürecinde o sırada meydana gelip daha sonra Sorgu sonunda kaybolan objelerdir.
    # Sadece sorguya özgü VIEW diyebiliriz. ALL CTEs(ordinary or recursive) start with a "WITH" clause ...
    # Bir common table içinde birden fazla WITH clause kullanılabilir
    # 2. çeşiti var 1.Ordinary 2. Recursive

#######################################
# 1.Ordinary Common Table Expressions
"""
-- Soru: -- Jerald Berray isimli müşterinin son siparişinden önce sipariş vermiş ve Austin şehrinde ikamet eden müşterileri listeleyin
SELECT  max(b.order_date) 
FROM sale.customer a, sale.orders b
WHERE a.first_name = 'Jerald' and a.last_name ='Berray'
    and a.customer_id = b.customer_id 

-- Austin şehrinde ikamet edenler
SElect * from sale.customer a , sale.orders b
where a.city = 'Austin' and a.customer_id = b.customer_id

-- Şimdi with ile birleştirip sona koşul ekleyeceğiz
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

-- b.order_date < c.JeraldLastOrderDate koşulu sona eklemiş olduk
-- NOT : With clause sadece tek bir sorguda çalışıyor. Fakat with bloğunda birden fazla sorgu tanımlayabiliriz
-- Bununla ilgili bir örnek yapalım
-----------------------------------------
-- Herbir markanın satıldığı en son tarihi bir CTE sorgusunda,her bir markaya ait kaç farklı ürün bulunduğunu da ayrı bir 
-- .. CTE sorgusunda tanımlayınız Bu sorguları kullanarak  Logitech ve Sony markalarına ait son satış tarihini ve toplam 
-- .. ürün sayısını (product tablosundaki) aynı sql sorgusunda döndürünüz
with tbl as(
	select	br.brand_id, br.brand_name, max(so.order_date) LastOrderDate
	from	sale.orders so, sale.order_item soi, product.product pr, product.brand br
	where	so.order_id=soi.order_id and
			soi.product_id = pr.product_id and
			pr.brand_id = br.brand_id
	group by br.brand_id, br.brand_name
) ,  ---1. tablo sonucunda her bir product ın son sipariş tarihi .Örn: 23 brand_id li DENAQ 2020-04-23 te en son sipariş verilmiş
tbl2 as(
	select	pb.brand_id, pb.brand_name, count(*) count_product
	from	product.brand pb, product.product pp
	where	pb.brand_id=pp.brand_id
	group by pb.brand_id, pb.brand_name
)  ---2. tabloda Her bir markada kaç ürünün bulunduğu. 40 satır geldi
select	*
from	tbl a, tbl2 b
where	a.brand_id=b.brand_id and
		a.brand_name in ('Logitech', 'Sony')
--- Sony markasına ait herhangi bir ürün en son 2020-10-21 de sipariş verilmiş ve sony markasına ait envanterimde 46 ürün varmış 
--- Logitect markasına ait herhangi bir ürün en son 2020-08-23 de sipariş verilmiş ve sony markasına ait envanterimde 27 ürün varmış
"""

###################
# 2.Recursive CTE Expressions
# İçerisinde UNION ALL yazıp CTE içerisinde belirtmiş olduğumuz tabloyu kullanacağız recursive şekilde
"""
-- 0'dan 9'a kadar herbir rakam bir satırda olacak şekide bir tablo oluşturun.
-- Normalde kalıbımız aşağıdaki gibi
WITH CTE AS ()
SELECT * from CTE;

-- Bu hata veriyor.Şimdi parantez içini dolduracağım Tablo adım CTE olsun
WITH CTE AS (select 0 rakam UNION ALL select 1 rakam)  -- Bu şekilde 10 a kadar gidebiliriz
SELECT * from CTE;

-- 1 ekleyerek devam etsin ve WHERE bloğunda bunu sınırlayalım
WITH CTE AS (select 0 rakam UNION ALL select rakam+1 from cte where rakam<9)
SELECT * from CTE;

-- Raporlamada bu tip tablolar çok kullanıyorlar. Mesela PowerBI da bir database oluşturarak bunu kullanacaksınız
-- DB ler genelde tarihler olur. Haftanın günü, tatil mi değil. O tarihin içinde bulunduğu ayın ilk günü, son günü vs gibi 
-- .. attribute lar olur. Bunlar çok büyük esneklik sağlar. Sizde CTE ile başlayıp böyle bir attribute(ya da tablo) oluşturabilirsiniz
"""
# -----------------------------------------
"""
-- Soru: 2020 ocak ayının herbir tarihi bir satır olacak şekilde 31 satırlı bir tablo oluşturunuz.
with ocak as (
	select	cast('2020-01-01' as date) tarih             -- veriyi date olarak cast ettik
	union all
	select	cast(DATEADD(DAY, 1, tarih) as date) tarih   -- üstteki "tarih" ile tanımlanana 1 ekle DATEADD(DAY, 1, tarih) as date datetime olarak geldiği için bunuda cast ettik
	from ocak
	where tarih < '2020-01-31'
)
select * from ocak
-- şimdi bu sütunun yanına gün, ay, yıl ve ayın son gününü ekleyelim
with cte AS (
	select cast('2020-01-01' as date) AS gun
	union all
	select DATEADD(DAY,1,gun)
	from cte
	where gun < EOMONTH('2020-01-01')  -- EOMONTH: ayın son gününü alır
) -- buradan sonra biz tarih tablosu oluşturalım
select gun tarih, day(gun) gun, month(gun) ay, year(gun) yil, EOMONTH(gun) ayinsongunu
from cte;
-- Siz bunun yanına tarih tablosu oluşturacaksanız ekleme yapabilirsiniz Bu şekilde bir çok attribute oluşturabilirsiniz
-- Her bir tablodaki tarih ile bu tabloyu joinlersiniz. Yani bu tarihleri diğer tablolarda kullanabilirsiniz.
-- Bunun çıkış noktası common table expressions
-----------------------------------------
-- Soru: Write a query that returns all staff with their manager_ids(use recursive CTE)
-- Her bir çalışanın patronunu bulun. CTE recursive ile
Select staff_id, first_name, manager_id from sale.staff where staff_id =1 -- staff_id si 1 in manager i yok. En üst kişi bu
-- Şimdi de manager ı james olan kişileri getirelim
Select * from sale.staff a where a.manager_id = 1

-- Şimdi with ekleyelim ve a.manager_id = 1 i manuel olarak almayacağız.Bir önce tanımlamış olduğum kişinin staff_id sine eşitleyeceğiz
with cte as (
	select	staff_id, first_name, manager_id
	from	sale.staff
	where	staff_id = 1
	union all
	select	a.staff_id, a.first_name, a.manager_id
	from	sale.staff a, cte b
	where	a.manager_id = b.staff_id
)
select * from	cte

-- a.manager_id = b.staff_id si 1 olanları çağır sonra   a.manager_id ye dönecek sonra sale.staff a tekrar gidecek tekrar
-- .. a.manager_id = b.staff_id  ye bakacak vs vs böyle devam edip En sonra manager_id si olmayana dönecek ve break olacak sorgumuz
-- .. Bu tip bir sorgu raporlama yaparken işe yarar yoksa şu şekilde de yapabilirdik.
select staff_id, first_name, manager_id from sale.staff
order by manager_id
-----------------------------------------
-- Soru: -- 2018 yılında tüm mağazaların ortalama cirosunun altında ciroya sahip mağazaları listeleyin.
-- List the stores their earnings are under the average income in 2018.
-- with clause un altında 2 tane tablo tanımlayacağız
WITH T1 AS (
SELECT	c.store_name, SUM(list_price*quantity*(1-discount)) Store_earn
FROM	sale.orders A, SALE.order_item B, sale.store C
WHERE	A.order_id = b.order_id AND	A.store_id = C.store_id AND	YEAR(A.order_date) = 2018
GROUP BY C.store_name
),
T2 AS (
SELECT	AVG(Store_earn) Avg_earn
FROM	T1
)
SELECT *
FROM T1, T2
WHERE T2.Avg_earn > T1.Store_earn
-- 1. tabloda Her bir store name her bir mağazanın yapmış olduğu satış tutarı. Filtre olarak da yıla 2018 dedik
-- 2.tabloda T1 deki değerlere göre ortalama aldık
-- Tabloları birbiri içerisinde referans gösterebiliyoruz
-- Final de T1,T2 tablosuna git T2 deki ortalama cironun T1 deki store cirolarından büyük olan mağazaları getir
"""

############################################################################################################################
#%% SQL-10
######################################
# WINDOW FUNCTIONS
# Group by ile yapamadığımız bazı şeyleri WF ile yapacağız.
# Grup içinde gruplama yapıyoruz gibi düşünülebilir. Hem daha az satır sorgu hem de verideki detayı kaybetmiyoruz

# CONTENT
# GROUP BY vs WINDOW FUNCTIONS(WF) vs 
# Types of WF
# WF Syntax and Keywords
# Window frames      -- Çok önemli
# How to Apply WF

##################
# 1.GROUP BY vs WF
# GROUP BY  aggregate fonksiyon ile tek satır sonuç döndürüyordu.
# WF Aynı group by mantığında çalışıyor ama satır sayısında azalma olmuyor
# Group by biraz yavaş, WF daha hızlıdır(Genelde)

"""
                                    Group by      Window Functions      
# Distinct                          necessity      optional
# Aggregation                       necessity      optional
# Ordering                          invalid         valid
# Performance                       shower          faster
# Dependency on selected Field      dependent      independent

Distinct    : Group by da distinct sonuç gelir, WF de bu oladabilir olmayadabilir
Aggregation : Aggregate kullanmak gerekir group by da, WF de bu şart değildir çünkü aggregare haricinde bir çok fonksiyonu vardır 
Ordering    : Group by içinde  bir çok grup arasında kullanılmıyor. Bir grup belirliyorsunuz. Tabloda birden fazla sınıf olsun
 .. bu tabloda sınıfa göre gruplama yaparsanız öğrencilerin notları arasında ortalama değişmez group by da
 .. WF de order by gerekiyor genelde. Belirlediğiniz grubun ortalamasına göre farklı sonuçlar döndürüyor WF
Performance : Group by biraz yavaş, WF daha hızlıdır(Genelde)
Dependency on selected Field: Group by yaparken bilgilerin seçilen alana bağlıdır. Bazı bilgiler kaybolur çıktıda WF de bu bağımsızdır
"""
# -----------------------------------------
"""
-- Group by ve WF kullanarak bir örnek yapalım
-- Soru: Her bir ürünün toplam stok miktarını hesaplayın
---------- group by ; 
select product_id, Sum(quantity) from product.stock
group by product_id
order by 1
----------- WF;
-- Önce bir stock tablomuza bakalım
select * from product.stock
order by product_id

-- Yeni bir sütun ekleyeceğiz şimdi
-- 1 numaraları ürünün bütün satırlardaki toplamını yazdırmak istiyorum -- 1089 rows dur distinct ten sonra 442 rows
select	distinct product_id, sum(quantity) over(partition by product_id) sumWF
from	product.stock
order by product_id
-- sum(quantity) over(partition by product_id) sumWF : her bir product_id için quantity toplamını al ve sumWF sütununda yazdır
-- group by ile aynı sonuç istediyor çıktıda o yüzden için distinct attık product_id ye
-- ÖNEMLİ NOT: Where şartına yazacağınız şart WF hesaplanmadan önce uygulanır
-----------------------------------------
-- Soru: markalara göre ortalama ürün fiyatlarını group by ve WF ile yapalım
----------- group by;
select brand_id, avg(list_price)
from product.product
group by brand_id 

------------ WF; -- 520 rows
select brand_id, avg(list_price) over(partition by brand_id) as avg_price
from product.product

--  group by ile aynı çıktı gelmesi için distinct ekleyelim -- 40 rows
select distinct brand_id, avg(list_price) over(partition by brand_id) as avg_price
from product.product
-----------------------------------------
-- 2 tane WF kullanalım
-- Soru: brand_id ye göre her bir brand_id de kaç ürün var ve her bir brand id ye göre en yüksek fiyatlı ürün
select	*,
		count(*) over(partition by brand_id) CountOfProduct,
		max(list_price) over(partition by brand_id) MaxListPrice
from	product.product
order by brand_id, product_id
-- NOTLAR
-- WF ile oluşturduğunu kolonlar birbirinden bağımsız hesaplanır.
-- Dolayısıyla aynı select bloğu içinde farklı partitionlar tanımlayarak yeni kolonlar oluşturabiliriz
-- group by lı sorgularda tek bir partition vardır(Select den sonra yazılan aggregate fonksiyonlar tek bir partition dır)
-- WF de sütunlar arasında partitionlar farklı olabilir
-----------------------------------------
--Soru: WF ile her bir markadan kaçar tane ürün var ve her bir kategory içindeki toplam ürün sayısını bulalım
select	product_id, brand_id, category_id, model_year,
		count(*) over(partition by brand_id) CountOfProductinBrand,
		count(*) over(partition by category_id) CountOfProductinCategory
from	product.product
order by brand_id, product_id, model_year

-- 520 rows
-- brand_id    si 1 olandan toplam 41 ürün varmış, vs vs
-- category_id si 1 olandan toplam 40 ürün varmış, 4 numaralı kategoriden 283 tane ürün varmış vs vs
-- order by ile sıralamayı değiştirip ona göre çıktımızı istediğimiz sıralamada getirebiliriz. Sonucu daha rahat gözlemliyoruz
-- NOT: Burada distinct yapabilir miyiz? Sonuç değişmez Çünkü product_id ler unique zaten
"""

##################
# 2.TYPES of WF
# a.Aggregate Functions --- Avg, min, ...
# b.Navigation Funtions --- Partition içerisinden gezinerek yaptığımız 
# c.Numbering Functions --- Partition lar içerisinde belirlediğimiz sıralama ile

##################
# 3.TYPES of WF
# Syntax and Keywords
# Select(columns) FUNCTION() OVER(PARTITION BY ... ORDER BY ... WINDOW FRAME) from table1;
# Hesaplayacağımız fonksiyonda sıralama önemliyse partition içinde order by yapıyoruz
"""
-- Örnek kod
-- SELECT *, avg(time) over (partition by id order by date rows between 1 preceding and current row) as avg_time from time_of_sales
-- rows between 1 preciding and current row : 1 önceki satırla içinde bulunduğu satırın .... (Ortalamasını al, toplamını al vs vs)
"""

##################
# 4.Window frames 
# Verinin tamamı bir partition olsun sonra biz bunu farklı partition lara bölüyoruz sonra da
# .. bi basamak sonra satırlar arasındaki ilişkiye window frame tanımlıyoruz. Asıl konu burada dönüyor.Belirlediğimiz frame üzerinde
# .. fonksiyonumuz çalışıyor. Bunun sınırlarını değiştirebiliyorum. Örneklerde daha net oturacak.
# current row: işlem yapılan satır
# partition başından itibaren current row a kadar olan satır bu satır benim frame im olsun diyebilirim(current row dahil)
# partition current row dan itibaren sona kadar olan satır bu satır benim frame im olsun diyebilirim .. 
# N Preciding, M following Current row dan başlarsam; 3 önceki satırdan başlayıp 5 sonraki satıra kadar git diyebilirim.
# .. current row u da dahil edince Toplam 9 satırım olacaktır

##################
# 5. How to Apply WF
"""
/*
örnek

id      date       time
1     2019-07-05    22
1     2019-04-15    26
2     2019-02-06    28
1     2019-01-02    30
2     2019-08-30    20
2     2019-03-09    22

PARTITION BY id                ---> ORDER by             -- avg(time)(ROWS BETWEEN 1 PRECEDING AND CURRENT ROW)
id      date        time      id  date         time     id        date    time       avg_time
1     2019-07-05    22        1   2019-01-02    30       1   2019-01-02    30          30 -- Burada 1 önceki satır olmadığı için 30
1     2019-04-15    26        1   2019-04-15    26       1   2019-04-15    26          28
1     2019-01-02    30        1   2019-07-05    22       1   2019-07-05    22          24
                                                         2   2019-02-06    28          25
id      date        time      id  date         time      2   2019-03-09    22          25
2     2019-02-06    28         2  2019-02-06   28        2   2019-08-30    20          21
2     2019-08-30    20         2  2019-03-09   22
2     2019-03-09    22         2  2019-08-30   20
-- NOT: Çalışacağınız yerde raporlama yapılıyorsa bu WF konusunu çok fazla kullanıyorsunuz
*/
"""
# -----------------------------------------
"""
-- Sürekli kullanılabilecek bir sorgu göstereceğiz WF ile alakalı. Windows frame i anlamak için bir örnek:
-- Herbir satırda işlem yapılacak olan frame in büyüklüğünü (satır sayısını) tespit edip window frame in nasıl oluştuğunu 
-- aşağıdaki sorgu sonucuna göre konuşalım.

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

--Detay olarak category_id, product_id yi aldık sadece. 8 tane de WF yazdık
-- farklı frame yapıları tanımlandı. her bir frame de kaç satır geliyor görmek için bu örneği kullanıyoruz
-- sorgunun tümünü çalıştırınca -520 rows. Herhangi bir satırda herhangi bir filtreleme yapmadık demek bu

-- 1 WF: OVER() NOTHING : Partition ınımız tablomuzun tamamıdır ve tek bir partition vardır. Büyüklüğü tablomuzun tamamıdır. --520 rows
-- 2 WF: COUNT(*) OVER(PARTITION BY category_id) countofprod_by_cat : her bir category_id için farklı bir değer hesaplanacak
-- 3 WF: COUNT(*) OVER(PARTITION BY category_id ORDER BY product_id) countofprod_by_cat_2: order by eklenmiş. 
-- .. ürünlerin sıralaması önemli değil normalde ama order by tanımladığımız için Window frame imiz değişiyor. Yani Window frame 
-- .. tanımlamazsak partition başından current row a kadar olan bizim window frame imizdir. 
-- .. (örn: 10. satır için ilk satırdan 10 a kadar gidiyor hepsini count yapıyor vs vs)
-- 4 WF:ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) prev_with_current, : Bu default değerdir WF de. Defaultolduğu için bir 
-- .. üstteki ile aynı çıktı geldi. Açıklaması :  1 önceki satırla içinde bulunduğu satırın count u
-- 5 WF: ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) current_with_following:
-- .. üsttekinin tam tersi bir window frame var (yukarda unb-current), burada (current-unb fol)
-- .. BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING: Current rowdan(parition ımızın) partition ımın sonuna kadar(ilk satır için 
-- .. partition ın tamamıdır yani 40) . 2. satırdaonun 1 eksiği vs (yani birinci partition da 40 yazdırdı, sonra 39, sonra 37 vs vs.)
-- 6 WF:  BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) whole_rows:
-- .. ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) whole_rows : partition ın en başı ve en sonu. Partition da hangi 
-- .. satırda olursam olayım daima partition ımın başı ve sonu arasında işlem yap. O yüzden hepsi 40 geldi. 1. WF ile aynı sonuç geldi
-- 7 WF: ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) specified_columns_1, : ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING : partition 
-- .. içerisinde 1 satır öne git ve 1 satır sonraya git. (Toplamda 1 önceki current ve 1 sonrakini alıp 3 satır alıyor 
-- .. NOT: Eğer 1 üst satır ya da 1 alt satır partition içerisinde değilse onu işleme alamıyoruz
-- .. (1. satır için count(*)=2 dir(current ve sonraki toplam 2), 2. satır için 3, 3. satır için 3 vs , partition sonunda
-- .. Yani mesela 40. satırda yine 2 gelmiş(1 önceki ve 1 current toplam 2))
-- 8 WF: ROWS BETWEEN 2 PRECEDING AND 3 FOLLOWING) specified_columns_2 : Bu da üstteki ile aynı mantık ilk 
-- .. frame 4(1 current ve 3 following), 2. si 5(1 üst,1 current ve 3 following), 3. sü 6(2 satır üst,1 current ve 3 following)
"""

#################
# WF lerde aggregate functions
# Analytic Aggregate Functions :  min(), max(), avg(), count(), sum()
"""
-- Soru: Her bir kategorideki en ucuz ürünün fiyatı nedir? category_id ve "cheapest_by_cat"
select	distinct category_id, min(list_price) over(partition by category_id) cheapest_by_cat
from	product.product
-- Her kategorinin yanına o ürünün en ucuz fiyatını getirdi. distinct li sonuç istediği için distinct atalım

-----------------------------------------
-- Soru: Product tablosnda kaç farklı product var. Toplam ürün sayısını WF ile yapınız
select distinct count(*) over() as num_of_product
from product.product
-- Tek bir satırlık sonuç istiyor. Toplam ürün sayısını istiyor
-- Farklı ürünü bulurken count(*) yapmamız yeterli çünkü product_id unique
-- her bir product için o sayı(520) tekrarlayacağı için distinct yazmalıyım
-----------------------------------------
-- Soru: How many differnt product in the order_item table? 520 tane ürünün kaç tanesini satmışım?
-- Bu soru diğer soruya göre biraz farklı
-- 1 ürün bu tabloda 1 den fazla tabloda geçebilir burada. product_id unique değil
select distinct product_id, count(*) over(partition by product_id) as num_of_order
from sale.order_item
-- 307 rows -- Bu tabloda 307 farklı ürün(product_id) varmış Bu 307 sonucunu tek satırda istiyoruz.
----------- group by ile bunu yapsaydık
select count(distinct product_id) UniqueProduct from sale.order_item

------------ WF ile deneyelim
select count(distinct product_id) over() UniqueProduct from sale.order_item -- HATA(Use of DISTINCT is not allowed with the OVER clause)
-- .. Bunu count içinde distinct olacaksa bunu group by ile yapabiliriz ya da select distinct product_id yi başka yerde tanımlayacağız
select distinct count(*) over()
from (select distinct product_id,  count(*) over(partition by product_id) as number_of_product
from sale.order_item) as a
-----------------------------------------
-- Soru: Write a query that returns how many products are in each order?
-- Her bir siparişte kaç farklı ürün olduğunu döndüren bir sorgu yazın? 

---------- group by ile
select	order_id, count(distinct product_id) UniqueProduct,
		sum(quantity) TotalProduct
from	sale.order_item
group by order_id
-- o siparişte uniquer product sayısı ve toplam kalem sayısını getirdi
-- sum(quantity) TotalProduct: Mesela order_id 1 de toplam 5 farklı ürün var toplam 8 ürün var

---------- WF ile
select distinct order_id, 
count(product_id) over(partition by order_id) Count_of_Uniqueproduct,
SUM(quantity) over (partition by order_id) Count_of_product
from sale.order_item
-----------------------------------------
-- How many different product are in each brand in each category?
-- Herbir kategorideki herbir markada kaç farklı ürünün bulunduğu
select distinct category_id, brand_id,
 count(*) over(partition by brand_id, category_id) count_of_Product
from product.product
-- 1 numaraları kategoride 1 numaralı markaya ait 15 tane ürün varmış,
-- 4 numaraları kategoride 8 numaralı markaya ait 15 tane ürün varmış vs vs ...
-----------------------------------------
-- brand isimlerini getirmek istersek üstteki sorguyu bir subquery olarak kullanabiliriz
select A.*, B.brand_name from 
(select distinct category_id, brand_id,
 count(*) over(partition by brand_id, category_id) count_of_Product
from product.product
 ) A, product.brand B
where A.brand_id = B.brand_id
-----------------------------------------
-- join ile WF örneği- aynı sonucu alalım
select distinct category_id, A.brand_id,
count(*) over(partition by A.brand_id, A.category_id) count_of_Product,
B.brand_name
from product.product A, product.brand B
WHERE A.brand_id = B.brand_id
"""

############################################################################################################################
#%% SQL-11
"""
-- How many different product are in each brand in each category?
--------- group by ile
select category_id,brand_id,COUNT(product_id)
from product.product
group by category_id,brand_id
--------- WF ile

select distinct category_id,brand_id,COUNT(product_id) OVER(PARTITION BY category_id,brand_id) cnt_prod
from product.product
"""

##########
# FIRST_VALUE 
# Bir sütun için en üst satırda yer alan değeri getiriyor(Partition, WF ve koşullara göre)
"""
-- Örnek kod
Select A.customer_id, A.first_name, B.order_date,
FIRST_VALUE(order_date) OVER (ORDER BY B.Order_date) first_date from sale.customer A, sale.orders B 
WHERE A.customer_id = B.customer_id
"""
# -----------------------------------------
"""
-- Soru: Write a query that returns most stocked product in each store
-- Sorunun ilk kısmını yapalım burada her bir store a göre en çok stoğu olan product_id ne buna bakacağım
Select store_id, product_id,
FIRST_VALUE(product_id) OVER(PARTITION BY store_id ORDER BY quantity DESC) most_stocked_prod
FROM product.stock
-- product_id nin ilk değerini alıp , quantity ye göre DESCENDING sıralamam gerekiyor. 
-- Çünkü azalan sıralamada en yüksekten düşüğe gidiyor. Yani first value dediğimde
-- bunun en üsttekini yani order by yaptığımız için maximum değerini aldı
-- store_id 1 karşısına gelen 30 numaralı ürün 30 tane varmış. store_id 2 karşısına gelen 64 numaralı ürün 30 tane varmış
-- most_stocked_prod --> first_value of product_id
-- Şimdi istediğimiz çıktıyı getirelim
Select distinct store_id, 
FIRST_VALUE(product_id) OVER(PARTITION BY store_id ORDER BY quantity DESC) most_stocked_prod
FROM product.stock
-- Elde etmek istediğimiz sonuç geldi
-----------------------------------------
-- Üstteki sorguda En yüksek quantity ye sahip ürün ve miktarı
Select distinct store_id, 
FIRST_VALUE(product_id) OVER(PARTITION BY store_id ORDER BY quantity DESC) most_stocked_prod,
FIRST_VALUE(product_id) OVER(ORDER BY quantity DESC) MSP_W
FROM product.stock
-----------------------------------------
-- Soru: --Write a query that returns customers and their most valuable order with total amount of it.
-- Müşterilerin en yüksek miktara sahip değerlerini döndürün
-- En değerli siparişi nasıl bulabiliriz. müşteriler- siparişler ve net price larına bakacağım ve her bir müşteri için en yükseğini bulacağım
SELECT	customer_id, B.order_id, SUM(quantity * list_price* (1-discount)) net_price
FROM	sale.order_item A, sale.orders B
WHERE	A.order_id = B.order_id
GROUP BY customer_id, B.order_id
ORDER BY 1,3 DESC;
-- net price ı her bir customer_id ve sipariş için bulmuş olduk
--customer_id 1 için en yüksek amoun 1038.5370, -- order_id 1555, 3 için, 6763.3454 -- order_id 1612
-- Devam edelim ve üsttekini bir alt sorguya alıp kaydedelim WITH ile
-- Sonra onu(WITH T1) i kullanarak istediğimiz sonuca ulaşalım
WITH T1 AS (
select customer_id, B.order_id, SUM(quantity*list_price*(1-discount)) net_price
from sale.order_item A, sale.orders B where A.order_id = B.order_id
Group by customer_id, B.order_id
)
Select distinct customer_id,
FIRST_VALUE(order_id) OVER(PARTITION BY customer_id ORDER BY net_price Desc) MV_order,
FIRST_VALUE(net_price) OVER(PARTITION BY customer_id ORDER BY net_price Desc) MV_order_NET_PRICE
from T1
-- En yüksek net price a sahip siparişi getirdik ve distinct yaptık
-- 2. partition da net price ı getireceğiz ve ilk satırdaki değeri alacağız
-- MV: most valuable
-----------------------------------------
-- Soru: Write a query that returns first order date by month
Select distinct Year(order_date) Year, Month(order_date) Month,
FIRST_VALUE(order_date) OVER(PARTITION BY Year(order_date),Month(order_date) ORDER BY Year(order_date)) first_order_date 
from  sale.orders
-- FIRST_VALUE(order_date): Her bir ay bazında ilk order_date
"""

##########
# LAST_VALUE
# Sıralanmış sütun değerleri içerisinden son değeri getiriyor
"""
-- Örnek kod
Select A.customer_id, A.first_name, B.order_date,
last_value(order_date) OVER (ORDER BY B.Order_date desc) last_date from sale.customer A, sale.orders B 
WHERE A.customer_id = B.customer_id

-- order_date ve last_date aynı değerler gelmiş. Çünkü default frame koşulunu kullandı
-- Her bir satır için bir önceki satırı hesaba kattı
-- 1. satır, önceki satır yok, kendisini aldı, 2. satırda önceki satırı 1. satır, bunlardan last_valueyu alıyor yani 2 yi  vs vs
-- O yüzden Rows between unboundend preciding and unbounded following demek lazım.
-- yani last_value kullanırken Window frame Rows between unboundend preciding and unbounded following şeklinde kullanmalıyız
------------------------------------------
-- Soru: Store tablosunda en yüksek quantity ye sahip ürünü last_value ile getirmek istiyorum
-- Önce stock tablomuza bakalım tekrar
select * from product.stock order by 1,3 asc
-- Devam edelim
SELECT	DISTINCT store_id,
		LAST_VALUE(product_id) OVER (PARTITION BY store_id ORDER BY quantity ASC, product_id DESC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) most_stocked_prod
FROM	product.stock

-- order by da 2 tane sütun kullandık
-- NOT: range ile rows hemen hemen aynı işlemleri yapıyor
    -- rows : unbounded preciding/following gibi keyword lerle kullanıp staır sayısı belirtmek istiyorsanız kullanıyoruz
    -- range: yine keyword ler kullanılıyor ANCAK Manuel olarak satır sayısı belirtemiyorsunuz
"""

###########
# LAG() AND LEAD()
# LAG() : Her bir satır için kendisinden belirttiğimiz kadar önceki satır değerini getiriyor
        # Örneğin; order_date sütunundan 3 önceki değeri o değerin yanına getiriyoruz
        # default u 1 : Kendisinden 1 önceki satır değerini al
        # Null değer için bir şey yazdırmak istiyorsak, onu null un yerine yazdırabiliyoruz
"""
-- Örnek kod
SELECT order_date,
lag(order_date,2) OVER(ORDER BY order_date) previous_second_w_lag from sale.orders
"""
# LEAD() : lag ın tersi olarak sonraki satır değerlerini alıyoruz
"""
-- Örnek kod
SELECT order_date,
lead(order_date,2) OVER(ORDER BY order_date) next_second_w_lead from sale.orders
"""
# ------------------------------------------
"""
-- Soru: Her bir staff için çalışanların aldığı siparişlerin 1 önceki sipariş tarihlerini yazdırın
SELECT	A.staff_id, B.first_name, B.last_name, A.order_id, A.order_date,
		LAG(order_date) OVER(PARTITION BY A.staff_id ORDER BY A.order_id) prev_order
FROM	sale.orders A, sale.staff B
WHERE	A.staff_id = B.staff_id
------------------------------------------
-- Soru Write a query that returns the order date of the one next sale of each staff (use the LEAD function)
SELECT	DISTINCT A.order_id, B.staff_id, B.first_name, B.last_name, order_date,
		LEAD(order_date, 1) OVER(PARTITION BY B.staff_id ORDER BY order_id) next_order_date
FROM	sale.orders A, sale.staff B
WHERE	A.staff_id = B.staff_id

-- Sütunları çektik
-- her bir siparişin kendisinden 1 önceki sipariş tarihini aldık
-- Örneğin ;3. siparişten bir önceki sipariş 9 , bunun tarihi 2018-01-05 sonra 3. satırda 12, 2018-01-06 nın yanına 2018-01-05 geldi
-- diğer satırlar aynı mantık. İlk sütundan önce sipariş olmadığı için NULL geldi
-- Not: order_id 20 numaralı sipariş için 1 önceki tarih aynı o yüzden order_by da A.order_date yerine
-- .. A.order_id ye göre yaparsak daha mantıklı olabilir. Çünkü order_date e göre sıralayınca önce order_id 19 u mu almalı yoksa 20 yi mi
-- .. gibi bir sorun oluşuyor. O yüzden order_id ye göre sıraladık

-- Eğer partition yapmasaydım order_id 1,2,3,4 diye gidecek ve staff ler farklı olacaktı
SELECT	A.staff_id, B.first_name, B.last_name, A.order_id, A.order_date,
		LAG(order_date) OVER(ORDER BY A.order_id) prev_order
FROM	sale.orders A, sale.staff B
WHERE	A.staff_id = B.staff_id
"""

############################################################################################################################
#%% SQL-12

#################################
# NUMBERING FUNCTIONS
# Sıralama ile partition lara bölme, kümülatif oranlar oluşturma, Numaralandırma vs

############ NUMBERING FUNCTIONS 1
# ROW_NUMBER : HEr bir partition içerisinde 1 den başlayıp artan bir sütun oluşuyor
# RANK : 1 den başlayarak Değerler arasında fark var ise sıralıyor. Aynı değerlere aynı rankı veriyor. (Örnekle daha iyi anlaşılacak)
# DENSE_RANK: Dense_rank e benziyor ancak --> (Örnekle daha iyi anlaşılacak)
    # aynı partition içinde; 
        # row_number: 1-2-3-4-5
        # Rank örnek: 1-2-2-2-5
        # DEnse_rank: 1-2-2-2-3    
"""
-- Row_Number()
--Soru: Her bir kategori içinde ürünlerin fiyat sıralamasını yapınız.
select product_id, category_id, list_price
from product.product

-- Partition içinde sıralama yaptı
----------------------------------
-- Rank() -- Dense_Rank()
select product_id, category_id, list_price,
ROW_NUMBER() over(partition by category_id order by list_price) RowNum,
RANK() over(partition by category_id order by list_price) [Rank],
DENSE_RANK() over(partition by category_id order by list_price) Dense_Rank
from product.product

-- satır 16 -- > rank:15,  dense_rank:16 çünkü list_price satır 14 ve 15 te aynı. Eğer satır 12,13,14,15 te 
-- list_price aynı olsaydı, satır 12,13,14,15 de rank:12 , dense_rank:12 olup, satır 16 da rank: 16, dense_rank : 13 olacaktı
-- NOT: RowNum : Buna "Camel type" isimlendirme deniyor
-- NOT: [Rank] : Köşeli parantez içinde yazdığım içindeki kelimeleri SQL server string ifade gibi algılar.
-- NOT: Dense_Rank: Pembe olarak çıkıyor. Çünkü bu SQL de bir fonksiyon ismi. Bunu değiştirmek önerilir.
----------------------------------
-- Soru: Herbir model_yili içinde ürünlerin fiyat sıralamasını yapınız (artan fiyata göre 1'den başlayıp birer birer artacak)
-- Row_number(), Rank(), Dense_Rank()
SELECT product_id, model_year,list_price,
		ROW_NUMBER() OVER(PARTITION BY model_year ORDER BY list_price ASC) RowNum,
		RANK() OVER(PARTITION BY model_year ORDER BY list_price ASC) RankNum,
		DENSE_RANK() OVER(PARTITION BY model_year ORDER BY list_price ASC) DenseRankNum
FROM product.product;
"""

############ NUMBERING FUNCTIONS 2
# CUME_DIST()    : Kümülatif distribution = Row number/total rows. Kümülatif değerler getirecek ve son satır "1" olacak
# PERCENT_RANK() : Percent_rank = (row number -1) /(total rows -1)
# NTILE(N)       : Eşit sayıda kümelere bölme. Veri sıralandıktan sonra küme sayısını belirtip kümeleme yapıyoruz

"""
-- Soru: Write a query that returns the cumulative distribution of the list price in product table by brand.
-- product tablosundaki list price' ların kümülatif dağılımını marka kırılımında hesaplayınız
SELECT brand_id,list_price,
    ROUND(CUME_DIST() OVER(PARTITION BY brand_id ORDER BY list_price),3) as CUM_DIST
FROM product.product;

-- brand_id partition a göre ilk veri yüzde kaçlık dilime denk geliyorsa yazdı, partition bittiğinde, yani son değer 1 oldu
-- Hatırlatma: ROUND(x,3) --- virgülden sonra kaç basamak görmek istiyoruz: 3 basamak		
----------------------------------
-- Soru: Write a query that returns the relative standing of the list price in product table by brand.
SELECT brand_id,list_price,
    ROUND(CUME_DIST() OVER(PARTITION BY brand_id ORDER BY list_price),3) as CumDist,
    ROUND(PERCENT_RANK() OVER(PARTITION BY brand_id ORDER BY list_price),3) as PercentRank
FROM product.product;
----------------------------------
-- Yukarıdaki CumDist sütununu CUME_DIST fonksiyonu kullanmadan hesaplayınız
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
-- WITH ile geçici tablo oluşturduk, sorgumuz daha sade gözüksün diye
-- Row_number la hesaplamak mı, Rank_number la hesaplamak mı daha doğru baktık. --
-- Tam istediğimiz sonuca ulaşamadık 2 si ile de. Hoca bakıp sonucu atacak
"""
# ----------------------- Farklı örnekler
"""
-- Write a query that returns both of the followings:
-- The average product price of orders.
-- Average net amount.
-- Aşağıdakilerin her ikisini de döndüren bir sorgu yazın:
-- Siparişlerde yer alan ürünlerin liste fiyatlarının ortalaması
-- Tüm siparişlerdeki ortalama net tutarı
SELECT DISTINCT order_id, 
AVG(list_price) OVER(PARTITION BY order_id) avg_price, 
AVG(list_price * quantity* (1-discount)) OVER() avg_net_amount
FROM sale.order_item

-- OVER() : Tablonun tamamı tek bir partition olmasını istediğimiz için partition yapmadık burada
-----------------------------------
-- Soru: -- List orders for which the average product price is higher than the average net amount.
-- Ortalama ürün fiyatının ortalama net tutardan yüksek olduğu siparişleri listeleyin.
select * from (SELECT DISTINCT order_id, 
cast(AVG(list_price) OVER(PARTITION BY order_id) as numeric(6,2)) AvgPrice, 
cast(AVG(list_price*quantity*(1-discount)) OVER() as numeric(6,2)) AvgNetPrice
FROM sale.order_item) A
where A.AvgPrice > A.AvgNetPrice
-------------------------------------------
----------- Cumulative sorusu
-- Soru : Calculate the stores' weekly cumulative number of orders for 2018
SELECT A.store_id, A.store_name, B.order_date,
DATEPART(ISO_WEEK, B.order_date) WeekOfYear
FROM sale.store A, sale.orders B where A.store_id = B.store_id And Year(B.order_date)= '2018'
order by 1,3
-- Şimdi partition ım burada store_id ve week of year olacak
-- Yani store id ve Select bloğunda DATEPART(ISO_WEEK, B.order_date) fonksiyonun sonucundan dönene göre partition yapacağız
SELECT A.store_id, A.store_name, B.order_date,
DATEPART(ISO_WEEK, B.order_date) WeekOfYear,
COUNT(*) OVER(PARTITION BY A.store_id, DATEPART(ISO_WEEK, B.order_date)) weeks_order
FROM sale.store A, sale.orders B where A.store_id = B.store_id And Year(B.order_date)= '2018'
order by 1,3
-- Bir sonraki sütuna geçelim. Mağazanın kümülatif satış sayısı(haftalık)
select  a.store_id, a.store_name, -- b.order_date,
	datepart(ISO_WEEK, b.order_date) WeekOfYear,
	COUNT(*) OVER(PARTITION BY a.store_id, datepart(ISO_WEEK, b.order_date)) weeks_order,
	COUNT(*) OVER(PARTITION BY a.store_id ORDER BY datepart(ISO_WEEK, b.order_date)) cume_total_order
from sale.store A, sale.orders B
where a.store_id=b.store_id and year(order_date)='2018'
ORDER BY 1, 3
-- 1. haftada toplam 4 satış, ccum satış 4 , 2. hafta 6, cum satış 10 , 3. hafta 3, cum_satış 13 vs vs
-- Son olarak buna bir distinct atalım.
select distinct a.store_id, a.store_name, -- b.order_date,
	datepart(ISO_WEEK, b.order_date) WeekOfYear,
	COUNT(*) OVER(PARTITION BY a.store_id, datepart(ISO_WEEK, b.order_date)) weeks_order,
	COUNT(*) OVER(PARTITION BY a.store_id ORDER BY datepart(ISO_WEEK, b.order_date)) cume_total_order
from sale.store A, sale.orders B
where a.store_id=b.store_id and year(order_date)='2018'
ORDER BY 1, 3
-- Sonuç: Her bir satır o haftanın toplam satış sayısını gösteriyor
-------------------------------------------
-- Soru: Calculate 7-day moving average of the number of products sold between '2018-03-12' and '2018-04-12'
-- O günlük satış ve 1 önceki haftanın ortalama satış sayısı '2018-03-12' and '2018-04-12' tarihleri arasında
--- Önce ihtiyacımız olanlara bakalım
select B.order_date, A.order_id, A.product_id, A.quantity
from sale.order_item A, sale.orders B
where A.order_id = B.order_id
-- Ayın 1 inde toplam 11 tane ürün satışmış, ayın 2 sinde toplam 2 ürün
-- günlük bazda kaç ürün satıldığını bilmem lazım
-- 7 gün geri ve ileri gidebileceğim ve birbiriyle kıyaslayabileceğim bir yapı olmalı
-- Bu veri setinden tek bir gün için toplam quantity yi görmem lazım onu 1 hafta öncesiyle katşılaştıracağız
-- Bunu da sorgum karışık olmasın diye WITH ile geçici tablo oluşturalım

-- Son 7 gündeki hareketli ortalamayı hesaplayacağız. Bunu da o günden geriye 7 satır git
-- .. o değerlerin ortalamasını getir diyeceğiz. O günün yanına yazdıracağız
with tbl as (
	select	B.order_date, sum(A.quantity) SumQuantity --A.order_id, A.product_id, A.quantity
	from	sale.order_item A, sale.orders B
	where	A.order_id = B.order_id
	group by B.order_date
)
select	*,
	avg(SumQuantity) over(order by order_date rows between 6 preceding and current row) sales_moving_average_7
from	tbl
where	order_date between '2018-03-12' and '2018-04-12'
order by 1

-- partition yapmama gerek yok ancak frame belirlemem lazım(7 satırlık ortalama için)
-- between 6 preciding and current row : 6 satır geriye + 1 current row = 7 günlük 
-- Ortalamayı integer yerine float istersek cast(.. as float.. ) şeklinde yapabiliriz
-- Siparişi olmayan tarihler var. O zaman gerideki günleri sayamayacağız.
-- Eğer bu kayıp günler önemliyse, tariht tablosu oluşturmamız lazım
-- .. left joinle olmayan tarihleride ekleyelim sonra olmayan tarihlerin karşısına 0 yazıp sonra
-- .. üstteki sorgumuzla sonuca ulaşabiliriz
-- where bloğunda koşulu alıp ondan sonra filtreleme yapıyor burada
-- önce partition yapıp sonra filtrelemeyi yapacaksam . partitionlı sorguyu bir tabloya kaydedip
-- .. sonra where bloğu ekleyebilirim başka bir sorguda
-------------------------------
-- Soru: List customers whose have at least 2 consecutive orders are not shipped
"""

#%% SQL-13
# DATABASE INDEX

# Bir tabloda belli alanlara yapılan sorgular daha fazla ise
# .. ( Mesela: Kişi tablosunda sürekli isim üzerinden sotgu yapılıyor)
# .. Bu alanlara index atıyorsunuz. Bize fayda sağlıyor
# .. Indexler database seviyesinde oluyor. Yani DB deki bütün sütunlara index atalım diyemiyoruz
# NOT: Primary key ler ve foreign key ler de birer indextir aslında
# Management studioda bir sorgu yazdıktan sonra bu sorgu ne kadar sürüyor bunun için bir yapı sunuyor
# .. Bu bilgiye göre tablo ya da sorgularınızı değiştirebilirsiniz

# Burada 2 temel terim var. SCAN, SEEK
# Scan : SQL server sorguya bakıp bu kriter hangi satırlarda var ona bakıyor. Yani Full scan yapıyor.
# .. Bu yavaş metodtur ama her zaman doğru sonuç getirir
# Seek : Indexleri koyduktan sonra dict mantığıyla ilgili yeri bulur
# .. Index seek : 1.Clustered 2.Non-clustered
# a.Clustered Index: Belirli bir sütun üzerinde oluşturmuş olduğunuz cluster indexte SQL o sorgusunda
# .. o alana nerede ise o alana(kümeye) gidiyor hızlıca buluyor. Her bir tabloda tek bir clustered index
# .. olabiliyor. Çünkü sıralama belli bir sütuna göre yapıldıysa, diğer sütunlar o sıralanan sütuna göre 
# .. sıraya gireceği için tek bir clustered index oluyor. (B-tree mantığıyla çalışır)
"""
-- Örnek kod
-- CREATE CLUSTERED INDEX index_name ON schema_name.table_name (column_list);
-- Bunu çalıştırınca bir "VIEW" mantığıyla DB de bir nesne oluşuyor
"""
# b.Non-Clustered Index: Bir tabloda clustered index oluşturdunuz. Sonra farklı alanlara da index oluşturmak istiyorsunuz
# .. Bunlar non-clustered indexler olacaktır. Birden fazla tabloda non-clustered index oluşturulabiliyor ve 2 den fazla
# .. sütun üzerinde non-clustered index oluşturulabiliyor.(B-tree yapısı burada da geçerli)

# ADVANTAGES AND DISADVANTAGES
# ADVANTAGE    : 1.Hız, 2.sıralama 3.Unique indexes guarantee
# DISADVANTAGES: 1.INSERT, UPDATE and DELETE becomes slower, 2.Disk alanında yer kaplar

"""
--önce tablonun çatısını oluşturuyoruz.
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

-- indexleri oluşturdunuz diyelim. Ama zaman içinde tabloda değişiklikler oldu diyelim.
-- SQL server sorgular arasında yönlendirme yapabilir. Yönlendirme yapabilmesi için bu istatistikleri kullanır
-- Biz bu istatistikleri kapatıp açabiliyoruz. Biz bu istatistikleri açalım
--İstatistikleri (Process ve time) açıyoruz, bunu açmak zorunda değilsiniz sadece yapılan işlemlerin detayını görmek için açtık.
SET STATISTICS IO on
SET STATISTICS TIME on

-- basit bir sorgu yapalım.
select * from website_visitor where visitor_id = 100 -- Burada 200000 satırı taradı

-- MS-SQL server da sorgumuzu seçip Execute ın sağında "V" işareti var onunda sağındakine(execution plan) tıklayalım
-- Çıktıda bazı şeyler geldi onların üzerine mouse la geldiğimizde bilgiler görünüyor
-- Select Coat: .. 
-- Table scan: Kullanmış olduğu yöntem. Bu ekranda en üstte. (Cluster yapınca burası "Clustered Index seek" olacak)
-- .. "Estimated number of rows to be read-->199999",
-- .. "Estimated number of execution -- 1" 
-- .. vs vs
-- 2 sorguyu karşılaştırmak için bunu kullanabilirsiniz
"""

# Tabloda index oluşturalım
"""
Create CLUSTERED INDEX CLS_INX_1 ON website_visitor (visitor_id);
-- CLS_INX_1          : Index adı. NOT: Index adı DB içinde unique olmalı
-- ON website_visitor : website_visitor tablosu üzerinde tanımlandı
-- (visitor_id)       : Hangi alana uygulanacağı
-- Object Explorer da -- > tables - dbo.website_visitor -- > Indexes -- > CLS_INX_1(Clustered) ... Oluşmuş

-- Indexi attık artık SQL server visitor ID lerin nerede olduğunu biliyor. Artık sorgu daha hızlı gelecektir
select * from website_visitor where visitor_id = 100 -- Burada 200000 ın hepsini okumadı
-- sorguyu seçip yine "execution plan" a tıklayalım. Çıktıda "Clustered_Index seek" geldi
-- Not: Eğer tablolar çok büyükse mutlaka index atmamız gerekiyor.

-- visitor_id de index var şu an tekrar bir index oluşturursak bu artık clustered index olmayacak bu non-clustered index olacak
select ad from website_visitor where ad = 'visitor_name17'; -- 200000 satırı okudu yine
-- "execution plan"a bakalım
-- Peki bu alana index nasıl atacağız(Non-cluster)
CREATE NONCLUSTERED INDEX ix_NoN_CLS_1 ON website_visitor (ad);
-- "execution plan"a bakalım. Index seek. Artık en alttaki "leaf" leri okumak zrounda değil(B-tree de)
-- .. index içerisindeki ismi bulmaya çalışıyor. Sonra sonucu getiriyor.
"""
# --------------------------------------
"""
-- İsim ve soyisme beraber index atalım.(Aynı isim soyisme ait başka bir kişi olmadığı için)
Create unique NONCLUSTERED INDEX ix_NoN_CLS_2 ON website_visitor (ad) include (soyad)
-- Artık isim ve soyisme beraber gönderilen planda ne olacak bakalım 
select ad, soyad from website_visitor where ad = 'visitor_name17';
-- "execution plan" a göre indexe göre arama yaptı. Extra isim soyisim üzerinde arama yapmadı
"""
# --------------------------------------
"""
-- clustered index (visitor_id)
-- non-clustered index (ad)
-- non-clustered index (ad) include (soyad)
-- Üsttekileri yaptık. Peki sadece soyadı üzerinden sorgu yapsaydı
select ad, soyad from website_visitor where soyad = 'visitor_name17'; -- çıktı yok ama execution plana bakmak için böyle yazdık
-- execution plan "Index scan" yani tablonun hepsini kontrol ediyor Yani "index seek" yapmadı
"""

#%% SQL-14

# Table of Contents: # Stored procedures: # User Defined/Valued Functions

# Stored procedures : DB tarafında insert,update, alter vs gibi işlemlerle ilgili kullanıyoruz
    # .. Örneğin: denormalize verisetini normalize hale getirmeniz gerekiyor. Bunu sürekli
    # .. yapmanız gerekiyor. Siz bir stored procedures oluşturursunuz. Bunu kaydediyorsunuz.
    # .. Bu günde 1 çalışsın ya da şu tablo üzerinde çalışsın diyebiliyoruz
    # .. Arka plan işlerinin yapıldığı yer olarak düşünebiliriz
    # User Defined/Valued Function: Fonksiyon adı üzerinde , DDL de fonksiyonlar kullanılmaz, 
    # Yararları: Performance, Maintainability, Productivity and Easy to Use, Security

##########################
# 1.STORED PROCEDURES
"""
select 'Hello World!'
-- Bu sorguyu bir procedure ile çalıştıralım

create procedure sp_sampleproc1 as
select 'Hello World!';
-- sonra bu kaydettiğim procedure u çalıştırıyorum bunu
EXEC sp_sampleproc1
-- asıl kod(2. yol): EXECUTE sp_sampleproc1 --
"""

# BEGIN & END
# Bir sorgu kümesinin başladığını ve bittiğini ifade eder
"""
create procedure sp_sampleproc2 as
BEGIN
select 'Hello World!';
END
--
EXEC sp_sampleproc2
"""

# Procedure de bir silmek,  değişiklik istersek drop edip sonra tekrar oluşturabiliriz
"""
drop procedure sp_sampleproc2
-- tekrar create edelim
create procedure sp_sampleproc2 as
BEGIN
select 'Hello World!';
END
--
EXECUTE sp_sampleproc2;

-- Değiştirmek
alter procedure sp_sampleproc1
AS
begin
select 'Hello World 3 !'
end
;
--
EXECUTE sp_sampleproc1;
"""

# Create ettiğimiz procedure leri MS-SQL de nasıl göreceğiz
# Sample Retail -- Programmability--Stored Procedures --> (Burada görebiliriz)
# NOT: System Store Procedures: Bunlar DB nin düzgün işlemesini sağlayan sistem procedure leri

# Tablo create edip, veri insert edeceğiz Sample retail e
"""
CREATE TABLE ORDER_TBL 
(
ORDER_ID TINYINT NOT NULL,
CUSTOMER_ID TINYINT NOT NULL,
CUSTOMER_NAME VARCHAR(50),
ORDER_DATE DATE,
EST_DELIVERY_DATE DATE--estimated delivery date
);
----------------------------------------
INSERT INTO ORDER_TBL VALUES (1, 1, 'Adam', GETDATE()-10, GETDATE()-5 ),
						(2, 2, 'Smith',GETDATE()-8, GETDATE()-4 ),
						(3, 3, 'John',GETDATE()-5, GETDATE()-2 ),
						(4, 4, 'Jack',GETDATE()-3, GETDATE()+1 ),
						(5, 5, 'Owen',GETDATE()-2, GETDATE()+3 ),
						(6, 6, 'Mike',GETDATE(), GETDATE()+5 ),
						(7, 6, 'Rafael',GETDATE(), GETDATE()+5 ),
						(8, 7, 'Johnson',GETDATE(), GETDATE()+5 )
---------------------------------------
select * from ORDER_TBL
"""
# Başka bir tablo daha create edeceğiz
"""
CREATE TABLE ORDER_DELIVERY
(
ORDER_ID TINYINT NOT NULL,
DELIVERY_DATE DATE -- tamamlanan delivery date
);
----------------------------------------
SET NOCOUNT ON -- çıktı da 8 rows affected diye uyarı gelmiyor
INSERT ORDER_DELIVERY VALUES (1, GETDATE()-6 ),
				(2, GETDATE()-2 ),
				(3, GETDATE()-2 ),
				(4, GETDATE() ),
				(5, GETDATE()+2 ),
				(6, GETDATE()+3 ),
				(7, GETDATE()+5 ),
				(8, GETDATE()+5 )
----------------------------------------    
select * from ORDER_DELIVERY      
"""
# 2 tablomuz var. Order tablosu sürekli değişecek. Öyle bir procedure yazayım ki order_tbl deki
# .. satır sayısını döndürsün
"""
CREATE procedure sp_sum_order
as
BEGIN
select count(*) as TOTAL_ORDER
from ORDER_TBL
END
--- Procedure ü çağıralım
EXECUTE sp_sum_order
"""

# Herhangi bir tarih girip. O tarih sayısındaki sipariş sayısını döndürsün
# Bunun için input tanımlamamız gerekiyor
"""
CREATE PROCEDURE sp_wantedday_order (@DAY DATE) AS
BEGIN
select count(*) as TOTAL_ORDER
from ORDER_TBL
where ORDER_DATE = @DAY
END
-- Eğer input tanımlayacaksam procedure un isminden sonra parametre adı(DAY) sonra veritipini(DATE) yazıyorum
-- Procedure ü nasıl çağıracağız
EXECUTE sp_wantedday_order '2022-06-22'
-- sp_wantedday_order procedure e gidecek  '2022-06-22' a bakacak day parametresi ile
-- Çıktı da 3 geldi
"""

# DECLARE: Bir parametreye değer atayıp bu parametreyi sorgularımda kullanabilirim.
"""
DECLARE
@p1 INT,
@p2 INT,
@SUM INT
SET @p1 = 5  -- parametrenin birine değer atadık
SELECT @p1 -- Output: 5
--
DECLARE
	@p1 INT,
	@p2 INT,
	@SUM INT
SET @p1 = 5
SELECT *
from ORDER_TBL
where ORDER_ID = @p1

-- p1: Parametre 1
-- SET ile parametreye veri atadık
------------------------------------------
-- order_id si 5 olan müşterinin customer_name i getireceğiz
DECLARE
	@order_id INT,
	@customer_name nvarchar(100)
SET @order_id = 5
SELECT @customer_name = customer_name
from ORDER_TBL
where ORDER_ID = @order_id
select @customer_name
-- select @customer_name : customer_name e gelen sonuç
-- where order_id > @order_id : ... şeklinde bir yapı kullanabiliriz
-- Burası OOP olarak geçiyor
------------------------------------------
declare
	@day date
set @day = getdate()-2     -- bugünden itibaren 2 gün öncesinde kayıt varsa getiriyor
EXECUTE sp_wantedday_order @day
;
"""

####################
# 2.FUNCTIONS
# Table-Valued Function -- > Tablo döndürür
# Scalar-Valued Functions -- > Değer döndürür


"""
-- Scalar-Valued Functions örnek
-- Input alarak almış olduğu metni büyük harfe çeviren fonksisyon
CREATE FUNCTION fnc_uppertext
(
	@inputtext varchar (MAX)
)
RETURNS VARCHAR (MAX)
AS
BEGIN
	RETURN UPPER(@inputtext)
END

-- Fonksiyonumuzu tanımladık
-- NOT:Declare ile parametreler atıyabilirdik
-- Bu fonksiyonu nasıl kullanacağız bakalım
SELECT dbo.fnc_uppertext('Hello world')
-- fonksiyonu create ederken şema adı vermezsek "dbo" altında ister bunu çağırırken o yüzden "dbo" yazmamız gerekli

-------------------------------------------------
-- Table-Valued Funtions örnek
-- Müşteri adını parametre olarak alıp o müşterinin alışverişlerini döndüren bir fonksiyon yazınız.
-- Önce bunun sorgusunu yazalım sonra fonksiyon yazalım
Select * from ORDER_TBL where customer_name = 'Smith'
--
CREATE FUNCTION fnc_getordersbycustomer1(@CUSTOMER_NAME NVARCHAR(100))
RETURNS TABLE AS
RETURN
Select * from ORDER_TBL where customer_name = @CUSTOMER_NAME

-- @CUSTOMER_NAME: input parametresi
-- Bu fonksiyon tablo döndürecek. O yüzden bunu tabloyu yazabildiğimiz yerde yazacağız(Mesela "from" dan sonra)
--
select * from dbo.fnc_getordersbycustomer1('Owen')
-- Owen ın siparişleri geldi
"""

#############
# IF / ELSE
# IF den sonra koşul, sonra koşu varsa "else if", "else if" vs yapacağız

"""
-- Bir fonksiyon yazınız. Bu fonksiyon aldığı rakamsal değeri çift ise çift, tek ise tek döndürsün
-- Eğer 0 ise sıfır döndürsün. 3 tane koşul
-- Önce bir sayının tek veya çift olduğunu anlamak için "mod" kullanacağız
DECLARE
    @input int,
    @modulus int

SET @input = 10
SELECT @input % 2
--------------------------
DECLARE
    @input int,
    @modulus int

SET @input = 10
SELECT @modulus = @input % 2
-- Çıktı yok çıktı için
DECLARE
    @input int,
    @modulus int

SET @input = 10
SELECT @modulus = @input % 2
PRINT @modulus
------------------
-- Şimdi bu alttaki mantığı kullanacağız
IF ...
	BEGIN
	...
	END
ELSE IF ...
	BEGIN
	...
	END
ELSE ...
--------------------input u tek olacak şekilde yapalım
DECLARE
	@input int,
	@modulus int
SET @input = 5
SELECT @modulus = @input % 2
IF @input = 0
	BEGIN
	 print 'Sıfır'
	END
ELSE IF @modulus = 0
	BEGIN
	 print 'Çift'
	END
ELSE print 'Tek'
-------------------- input u çift yapalım
DECLARE
	@input int,
	@modulus int
SET @input = 10
SELECT @modulus = @input % 2
IF @input = 0
	BEGIN
	 print 'Sıfır'
	END
ELSE IF @modulus = 0
	BEGIN
	 print 'Çift'
	END
ELSE print 'Tek'
-- Bunun üzerine fonksiyonu create edeceğiz
------------------------------------------
create FUNCTION dbo.fnc_tekcift
(
	@input int
)
RETURNS nvarchar(max)
AS
BEGIN
	DECLARE
		-- @input int,
		@modulus int,
		@return nvarchar(max)
	-- SET @input = 100    -- NOT:Bunu kaldırırsak her zaman çift değerini döndürecekti. Ama sonuç bizim girdiğimiz parametreye bağlı oldu burayı kaldırdığımız için
	SELECT @modulus = @input % 2
	IF @input = 0
		BEGIN
		 set @return = 'Sıfır'
		END
	ELSE IF @modulus = 0
		BEGIN
		 set @return = 'Çift'
		END
	ELSE set @return = 'Tek'
	return @return
	
END
;

-- if bloğundaki her bir değerde @return ün eşitindekileri atayacak('Sıfır','Çift','Tek')
-- if yapısında @return parametreme değer atamış oldum o yüzden en sonra return olarak @return ü döndürdük
-- Fonsiyon tanımlarken yazdırma değil de return yapacağımız için printler yerine return yazdık
-- input parametresini fonksiyon içinde tanımladığımız için DECLARE içinde tekrar tanımlamadık hata almamak için
-- Bunu scalar value ların olduğu yerde kullanabiliriz. Mesela select bloğunda, where bloğunda vs
select dbo.fnc_tekcift(100) A, dbo.fnc_tekcift(9) B,dbo.fnc_tekcift(0) C
"""

###########
# WHILE
# Belli bir sayıda bir şey dönmesini istiyorsak kullanıyoruz
"""
-- 1 den 50 ye kadar olan sayıları yazdıralım
select 1
-----------
PRINT 1
----------
-- Biz parametreleri belirleyelim
-- 1 den başlayacağını belirleyeceğimiz parametremizi oluşturalım
DECLARE
    @counter int

set @counter= 1
PRINT @counter
PRINT @counter + 1
PRINT @counter + 2
PRINT @counter + 3
-- Şimdi burada bir yerde durmasını istediğimiz için total parametresini de ekleyelim
-- counter ımız artacak sürekli ve total dan küçük olduğu sürece yazdıracak
DECLARE
	@counter int,
	@total int
set @counter = 1
set @total = 50
while @counter < @total
	begin
		PRINT @counter
		set @counter = @counter + 1
	end
;

-- Hoca: begin ve end i belirtmemiz gerekiyor
"""

"""
--Siparişleri, tahmini teslim tarihleri ve gerçekleşen teslim tarihlerini kıyaslayarak
--'Late','Early' veya 'On Time' olarak sınıflandırmak istiyorum.
--Eğer siparişin ORDER_TBL tablosundaki EST_DELIVERY_DATE' i (tahmini teslim tarihi) 
--ORDER_DELIVERY tablosundaki DELIVERY_DATE' ten (gerçekleşen teslimat tarihi) küçükse
--Bu siparişi 'LATE' olarak etiketlemek,
--Eğer EST_DELIVERY_DATE>DELIVERY_DATE ise Bu siparişi 'EARLY' olarak etiketlemek,
--Eğer iki tarih birbirine eşitse de bu siparişi 'ON TIME' olarak etiketlemek istiyorum.
--Daha sonradan siparişleri, sahip oldukları etiketlere göre farklı işlemlere tabi tutmak istiyorum.
--istenilen bir order' ın status' unu tanımlamak için bir scalar valued function oluşturacağız.
--çünkü girdimiz order_id, çıktımız ise bir string değer olan statu olmasını bekliyoruz.

-- ilk önce sorgumuzu yazalım adım adım
select * from ORDER_TBL A, ORDER_DELIVERY B
WHERE A.ORDER_ID = B.ORDER_ID
------------------------------------
create FUNCTION dbo.fnc_orderstatus
(
	@input int
)
RETURNS nvarchar(max)
AS
BEGIN
	declare
		@result nvarchar(100)
	-- set @input = 1
	select	@result =
				case
					when B.DELIVERY_DATE < A.EST_DELIVERY_DATE
						then 'EARLY'
					when B.DELIVERY_DATE > A.EST_DELIVERY_DATE
						then 'LATE'
					when B.DELIVERY_DATE = A.EST_DELIVERY_DATE
						then 'ON TIME'
				else NULL end
	from	ORDER_TBL A, ORDER_DELIVERY B
	where	A.ORDER_ID = B.ORDER_ID AND
			A.ORDER_ID = @input
	;
	return @result
end
;
-- Case aslında 1 değer döndürüyor. Bu döndüren değeri bir parametreye atayacağız yani,
-- case içindeki ifadeleride bir parametreye atayalım yoksa kodda "where" de order_id ye değer vermem gerekiyor
-- .. onun yerin @input değeri gireceğiz orada
-- fonksiyonu çağıralım
select	dbo.fnc_orderstatus(3);
-- şu şekilde de çalıştırabilirdik fonksiyonu;
-- fonksiyonun döndürdüğü bir scalar value olduğu fonksiyon içine parametre olarak ORDER_ID yazarsak select bloğunda hepsi için sonucu alabiliriz
select	*, dbo.fnc_orderstatus(ORDER_ID) OrderStatus
from	ORDER_TBL ;
"""





 ############################################ END ###########################################################
