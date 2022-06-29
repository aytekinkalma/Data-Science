#%% SQL-3. ders_03.01.2022_ LAB DERSI

# Insertten devam edeceğiz bu gün
# Insert: Tabloya veri girmemizi sağlıyordu

########################################################################
# INSERT / INSERT INTO ...
"""
INSERT INTO Person.Person (SSN, Person_FirstName, Person_LastName) VALUES (75056659595,'Zehra', 'Tekin')

# SSN, Person_FirstName, Person_LastName e 75056659595,'Zehra', 'Tekin' değerlerini ekledim
# INSERT yerine INSERT INTO yazabilirdik
"""
####################################
"""
INSERT INTO Person.Person  VALUES (889623212466,'Kerem',"Yılmaz")

# Sütun ismi yazmazsam tüm sütunlara insert edecek
"""
####################################
"""
INSERT INTO Person.Person  VALUES (889623212466,'Kerem')

# HATA, 3 sütun, 2 değer var
"""
####################################
"""
INSERT INTO Person.Person (SSN, Person_FirstName) VALUES (889623212466,'Kerem')

# Kabul etti çünkü  Person_LastName sütunu "NULL" olabiliyordu
# Eğer "NOT NULL" constraint i olsaydı çalışmazdı
# Diğer bir nokta integer a nümerik, varchar sütuna string değer girmeliyiz
"""
####################################
"""
INSERT INTO Person.Person (Person_LastName,SSN, Person_FirstName) VALUES ("Yalnız",889623212466,'Ahmet')

# Sütun sırasını değiştirebilirim ama values sırasını da değiştirmeliyim
# HATA: primary key olan satıra aynı değeri bu unique değer olmalı, yukarda girdin aynısını diyor
# Bunu değiştirirsek hata düzelecektir -- Örn: 639623212466
"""
####################################
"""
INSERT INTO Person.Person (SSN, Person_FirstName, Person_LastName) VALUES (459623212466, "Zeki",Null)

# Insert edeceğiniz sütunları yazmazsak bütün sütunlara değer ekleyeceğimizi anlar SQL
"""
####################################
"""
INSERT INTO Person.Person  VALUES (459623264466, "Zeki",Null)
INSERT INTO Person.Person VALUES (459652212466, "Metin",Null)

# İki kayıt yapabiliriz bu şekilde ya da tek query de yapabiliriz bunu ; aşağıya bakalım
"""
####################################
"""
INSERT INTO Person.Person  VALUES (459623264466, "Zeki",Null),
                                  (459652212466, "Metin",Null)
"""
####################################
"""
INSERT INTO Person.Person_Mail (Mail, SSN) VALUES ('zehtek@gmail.com',75056659595),
                                  ('meyet@gmail.com',13056659595),
                                  'metsak@gmail.com',24056659595)

# Mail_ID identity(1,1) constraint ine sahip olduğu için buna değer girmeye çalışırsak hata alırız
# O yüzden bu sütunu almadık
"""
####################################
"""
INSERT INTO Person.Person_Mail VALUES ('zehtek@gmail.com',75056659595),
                                  ('meyet@gmail.com',15076659595),
                                  'metsak@gmail.com',24056659595)

# Peki sütun isimlerini yazmazsam? Kabul eder mi? Etti.
"""

########################################################################
# SELECT .... INTO
####################################
"""
SELECT * FROM Person.Person  # 7 değer girmişiz.
"""
####################################
"""
SELECT * INTO person.person_2 from Person.Person

# Person tablosunun tamamını person_2 tablosuna kopyala
# person_2 tablosu yoktu, artık var altta
"""
####################################
"""
SELECT * FROM person.person_2
"""
############################################################################################################
# INSERT INTO SELECT : Bir tabloya farklı bir query nin sonucunda gelen değerleri insert etmemize yarıyor
"""
INSERT person.person_2 SELECT * FROM person.person WHERE Person_FirstName = 'Zeki'

# Primary key olmadığı için 2 tane kayıt geldi person_2 ye
"""
####################################
# DEFAULT VALUES null olabilen sütun için NULL, otomatik artan için sıradaki değeri ata
"""
INSERT Book.Publisher DEFAULT VALUES

# Publisher_ID otomatik artan, Publisher_Name Null değer alabiliyor

SELECT * FROM Book.Publisher

# Eklenmiş
"""
####################################
# UPDATE : Değerleri güncellemek için kullanılır
"""
UPDATE person.person_2 SET Person_FirstName = 'Default_name'

# Üsttekini çalıştıralım. (Genelde bu şekilde kullanmıyoruz)

SELECT * from person.person_2 
"""
####################################
"""UPDATE person.person_2 SET Person_FirstName = 'Ahmet'
WHERE Person_lastName = 'Yalnız'
"""
########################################################################
# HOCA: join ve subquery konularına şimdilik girmeyeceğiz
# DELETE : 
"""
SELECT * FROM Book.Publisher
DELETE FROM Book.Publisher
"""
####################################
"""
Insert Book.Publisher values ('İLETİŞİM')

SELECT * FROM Book.Publisher
"""
####################################
"""
DELETE FROM Book.Publisher WHERE Publisher_Name = 'İLETİŞİM'

# Üstte insert ettiğimiz değer gitmiş oldu
"""
########################################################################
# DROP TABLE: Verileri ile birlikte tablo gider
"""
DROP TABLE Person.person_2
"""
########################################################################
# TRUNCATE : Tabloya format atar. Tabloyu silmez. İçindeki veriler gider
"""
TRUNCATE TABLE Person.Person_Mail;
TRUNCATE TABLE Person.Person;
TRUNCATE TABLE Book.Publisher;
"""
########################################################################
# ALTER: Veritabanındaki verilerin yapısını değiştirir
"""
ALTER TABLE book.book ADD CONSTRAINT FK_Author FOREIGN KEY (Author_ID)
REFERENCES book.author (Author_ID)

# HATA: reference tablosunda primary key yok diyor.
# Author tablosunda kısıt var mıydı? foreing key olabilecek hiç bir durum yok
# .. Önce bunu düzelteceğiz -- ALTTA

# book.book tablosunu yenileyeceğim
# FK_Author : Constraint e verdiğimiz isim
# FOREIGN KEY   : Hangi sütuna foreign key uygulayacağım --> Author_ID 

"""
####################################
"""
ALTER TABLE Book.Author ADD CONSTRAINT pk_author PRIMARY (Author_ID)

# HATA .null olabilen bir sütunu primary key yapamazsın diyor
# Book.Author tablosundaki Author_ID sütunun tipini değiştirmeliyiz
"""
####################################
"""
ALTER TABLE Book.Author ALTER COLUMN Author_ID INT NOT NULL

# Şimdi tekrar çalıştıralım kodumu altta

ALTER TABLE book.book ADD CONSTRAINT FK_Author FOREIGN KEY (Author_ID)
REFERENCES book.author (Author_ID)

# Şu an oldu. Author_ID yi foreign key yaptık
"""
####################################
# Diagrama bakıyorum henüz bir bağlantı oluşmuş görünmüyor
# HOCA: Author tablosunda primary key neden görünmüyor? Sonra kapatıp açıp tekrar bakarız

"""
# Publisher_Id yi de foreign key yapmalıyım

ALTER TABLE Book.Book ADD CONSTRAINT FK_Publisher FOREIGN KEY (Publisher_ID)
REFERENCES Book.Publisher (Publisher_ID) 

# Publisher_ID de foreign key oldu
"""
####################################
"""
ALTER TABLE Person.Loan ADD CONSTRAINT FK_PERSON FOREIGN KEY (SSN)
REFERENCES Person.Person (SSN) 
ON UPDATE NO ACTION
ON DELETE NO ACTION

# ON UPDATE  : ana tabloda update yaptığımda NO ACTION yapsın
# ON DELETE  : ana tabloda delete yaptığımda NO ACTION yapsın
"""
####################################
"""
ALTER TABLE Person.Loan ADD CONSTRAINT FK_book FOREIGN KEY (Book_ID)
REFERENCES Book.Book (Book_ID) 
ON UPDATE NO ACTION
ON DELETE CASCADE
"""
########################################################################
# CHECK CONSTRAINT
"""
SELECT * FROM person.Person

# person.Person SSN sütununa 11 haneden fazla rakam giremesin kullanıcı. Bunu yapmaya çalışalım
"""
####################################
"""
ALTER TABLE person.person ADD CONSTRAINT CHECK_SSN CHECK (SSN > 9999999999 AND SSN <=99999999999)

# Şimdi altta SSN e 7 digitli değer girmeye çalışalım
"""
####################################
"""
INSERT Person.Person (SSN) VALUES (8989565)

# HATA
"""
####################################
"""
INSERT Person.Person (SSN) VALUES (89895658572)

# Hata YOK
"""
####################################
"""
Alter table Person.Person_Phone add constraint FK_Person2 Foreign key (SSN) References Person.Person(SSN)
"""
####################################
"""
Alter table Person.Person_Mail add constraint FK_Person4 Foreign key (SSN) References Person.Person(SSN)
"""
# Hemen hemen bütün constraintlerimizi oluşturduk. Bakalım Database diagramlarımız oluşmuş mu
# Tüm tablolar birbiri ile bağlantılı
# Loan -- SSN üzerinde - person a bağlı , aynı zamanda book_Id üzerinden Book tablosuna bağlı
# Book --- Publisher_ID üzerinden Publisher a bağlı ve Author_ID üzerinden Author a bağlı
# O sayfada sağ tık -- > properties -- dediğimde ne olduğu ile ilgili bilgi veriyor
# relationships e tıklayıp bağlantıları da görebiliriz

# MSSQL Türkçe karakterlerde hata veriyorsa
# Tools--> Options --> (açılan yerde sol üst arama yerine language yazıyoruz), --> language --> same as windows

# Şemalar:
# Hoca: Şemalar tabloları birbirinden ayırmak, onları ayrı yetkilendirme yapabilmek için Şema yapıyorsunuz
# ... Bazı şemalara yetki verip bazılarına yetki vermiyoruz vs


###################################################### END ##############################################

