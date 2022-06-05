/*===================================================
 JOINS
====================================================*/
    
-- Join islemleri farkli tablolardan secilen sutunlar ile yeni bir tablo 
-- olusturmak icin kullanilabilir.
--     
-- JOIN islemleri Iliskisel Veritabanlari icin cok onemli bir ozelliktir. Çunku
-- Foreign Key'ler ile iliskili olan tablolardan istenilen sutunlari cekmek 
-- icin JOIN islemleri kullanilabilir.

-- Standart SQL'de en çok kullanılan Join islemleri:
-- 1) FULL JOIN:  Tablodaki tum sonuclari gosterir
-- 2) INNER JOIN:  Tablolardaki ortak olan sonuc kumesini gosterir
-- 3) LEFT JOIN:  Ilk tabloda (Sol) olup digerinde olmayan sonuclari gosterir
-- 4) RIGHT JOIN: Sadece Ikinci tabloda olan tum sonuclari gosterir.

--	NOT: SQLite Sadece INNER, LEFT VE CROSS JOIN İşlemlerini desteklemektedir.
 
/*===================================================*/


/* araclar.db adındaki veritabanını kullanarak Markalar ve 
Siparisler tablolarındaki marka_id'si ayni olan kayıtların
marka_id, marka_adi, siparis_adedi ve siparis_tarihi   
bilgilerini  listeleyen bir sorgu yaziniz.*/

SELECT 		m.marka_id,  m.marka_adi, 
		s.siparis_adedi, s.siparis_tarihi
FROM 		markalar as m
JOIN		siparisler as s
		ON m.marka_id = s.marka_id;


/* Markalar ve Siparisler tablolarındaki tüm araç markalarının siparis bilgilerini
(marka_id,marka_adi,siparis_adedi,siparis_tarihi) listeleyen bir sorgu yaziniz.*/
SELECT 		m.marka_id,  m.marka_adi, 
		s.siparis_adedi, s.siparis_tarihi
FROM 		markalar as m
LEFT JOIN	siparisler as s
		ON m.marka_id = s.marka_id;


/* Chinook veritabanındaki tracks tablosunda bulunan her bir şarkının
türünü (genre) listeleyiniz.*/
SELECT 		t.name, g.name
FROM 		tracks t
JOIN		genres g
		ON t.GenreId = g.GenreId;


/* invoice tablosundaki faturaların her birinin müşteri adını (FirstName),soyadını (lastName),
fatura tarihini (InvoiceDate) ve fatura meblağını (total) listeleyen sorguyu yazınız */
SELECT 		c.FirstName, c.LastName, i.InvoiceDate, i.total   
FROM 		invoices i
JOIN		customers c
		ON i.CustomerId = c.CustomerId;


/* invoice tablosundaki faturaların her birinin müşteri adını 
(FirstName),soyadını(lastName) ve fatura meblağlarının 
toplamının(total) 40 dolardan fazla olanlarını artan sırada
listeleyen sorguyu yazınız */
SELECT 		c.FirstName, c.LastName,
		sum(i.total) as total_amount
FROM 		invoices i
JOIN 		customers c
		ON i.CustomerId = c.CustomerId
GROUP BY 	c.FirstName
HAVING 		total_amount > 40
ORDER BY	total_amount DESC;

-- CUstomerID ye göre gruplandırır isek
SELECT 		c.CustomerId, c.FirstName, c.LastName,
		sum(i.total) as total_amount
FROM 		invoices i
JOIN 		customers c
		ON i.CustomerId = c.CustomerId
GROUP BY 	c.CustomerId
HAVING 		total_amount > 40
ORDER BY	total_amount DESC;

/*===================================================
 SUBQUERIES
====================================================*/

/* albums tablosundaki Title sutunu 'Faceless' olan kaydın albumid'si elde ederek 
tracks tablosunda bu değere eşit olan kayıtların bilgilerini SUBQUERY yazarak listeyiniz.
Listelemede trackid, name ve albumid bilgilerini bulunmalıdır. */
SELECT 		TrackId, name, AlbumId
FROM		tracks
WHERE		AlbumId in (
			SELECT 	AlbumId
			FROM	albums
			WHERE	Title = 'Faceless');

--JOIN
SELECT 		t.TrackId, t.name, t.AlbumId
FROM		tracks t
JOIN		albums a
		ON t.AlbumId = a.AlbumId AND a.Title = 'Faceless';

/* albums tablosundaki Title sutunu Faceless veya Let There Be Rock olan kayıtların 
albumid'lerini elde ederek tracks tablosunda bu id'lere eşit olan kayıtların bilgilerini 
SUBQUERY kullanarak listeyiniz. Listelemede trackid, name ve albumid bilgileri bulunmalıdır. */


/* albums tablosundaki Title sutunu Faceless veya Let There Be Rock olan kayıtların 
albumid'lerini elde ederek tracks tablosunda bu id'lere eşit olan kayıtların bilgilerini 
JOIN kullanarak listeyiniz.Listelemede trackid, name ve albumid bilgileri bulunmalıdır. */