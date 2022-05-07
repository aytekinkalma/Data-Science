# PATIKA.DEV--> EĞİTİMLER
# Git&Github(Global information Tracker)
#%% 1. VİDEO- Git kurulumu
# Visual Studio Code kurulumu
# Git kurulumu

# Visual studio yazdık google a ve ilk çıkan siteden indirdik VS Code u.
# Git: Version kontrol sistemleri/Kaynak kod yönetim sistemi
# Visual Studio dan soldan 3 üncü "Source kontrol" a tıkladık. Git kurulmadığı 
# .. için oradan install ettik.
# Sonra başlattan "git bash" e basıp çalıştırdık. Bu git bash de hem
# .. linux hem de windows komutları çalışabiliyor. Yani windows un içerisinde
# .. linux komutlarını(mesela "ls" yaz) kullanabiliyor olacağız. Mesela bir 
# .. websitesinde kurulum yaparken linux komutları isteyecek vs vs.
# Sonuç: hem linux hem de windows komutlarını tek bir ekranda kullanabilir
# .. hale geldik.

# Tekrar soldan 3. ye tıklarsak(visual studio) oradan Open folder, clone rep..
# Open folder: Açtığımızda o klasör içerisinde git in çalışmasını sağlayabilirz
# Clone repository: Herhangi bir yerden version kontrol sistemi içerisindeki
# .. yapıyı direk buraya(visual studio ya) aktarabiliriz. Mesela bir "repo" yu
# (github reposundan bahsediyor sanırım) alıp burada kullanabiliriz.

# Kurulumda Visual studio code un terminalden kullanılabileceği ile ilgili bir
# .. ayar yapmıştık. 
# cmd yi açtık
# "dir"
# "cd Desktop"       # Desktop a geldik
# "mkdir test"/"md test"       # test diye bir klasör açtık
# "cd test"
# "code ."   # "code boşluk nokta" deyince her şey yolunda ise test klasörünün
# .. içinde visual studio yu açabileceğiz.

#%% 2.VİDEO GIT: Version kontrol sistemleri/Kaynak kod yönetim sistemi nedir?
# SCM : Source Code Management:Kaynak kod yönetimi
# 2005 te Linux çekirdeğinin geliştirilmesi için çıkarıldı.2013 te pazarın
# .. %30 una ulaşmıştır.
# Genelde versiyon kontrol sistemi deniliyor
"""
GIT Versiyon Kontrol Sistemi Nedir?
GIT nedir? diye sorduğunuzda versiyon kontrol sistemi cevabını almışsınızdır. İyi de versiyon kontrol sistemi nedir?
Projemi geliştirirken "proje", "projee", "projee_son", "projee_son_5" şeklinde klasörlesem olmaz mı? GIT öğrenmeden olmaz mı? - OLMAZ!
Son sorudan başlayayım. Eğer profesyonel işler yapacaksanız GIT öğrenmek zorundasınız. Klasör isminin sonuna fazladan harfler, rakamlar
.. ekleyerek proje geliştirmek ilerleyen süreçlerde başa çıkılabilecek bir yöntem değildir.
Versiyon Kontrol Sistemi Nedir? sorusuna gelirsek; Bir döküman (yazılım projesi, ofis belgesi vb.) üzerinde yaptığınız degişiklikleri 
.. adım adım izleyen, istediğinizde kayıt eden ve isterseniz bunu internet üzerindeki 
.. bir bilgisayarda veya yerel bir cihazda (respository / repo / depo) saklamanızı ve yönetmenizi sağlayan bir sistemdir. [3]
Versiyon Kontrol Sistemi yerine Kaynak Kod Yönetim Sistemi ifadesini de duymuş olabilirsiniz. İkisi de aynı şeyi ifade etmektedir.

GIT'i Anladım Fakat GitHub, GitLab, BitBucket Nedir?
En sade şekilde GIT versiyon kontrol sistemini kullanan depolama servisleri diyebiliriz.

GitHub
Yazılımcılar için bir kod kütüphanesi ve bir çeşit sosyal medya ortamıdır.

Yazılım geliştiriciler projelerini halka açık veya özel olarak saklayabilir. Ücretli ve ücretsiz paket seçenekleri mevcuttur.

GitLab
GitHub gibi bir GIT servisidir. Farklı olarak firmalara GitLab'ı kendi sunucularına kurma imkanı verildiği için genelde kurumsal tarafta kullanılır. GitLab ile firmalar kendi içerisinde GIT hizmetlerinden faydalanabilir.

BitBucket
Genelde kişisel kullanıma yöneliktir. GitHub tarafındaki açık kaynak projeler ve sosyal medya ortamı burada gelişmemiştir.

Yukarıda açıkladığımız servisler haricinde GitKraken, SourceTree gibi irili ufaklı farklı servisler de mevcuttur.

GIT sistemini kullanmaya başladığınızda karşınıza daha önce aşina olmadığınız bazı tanımlar çıkacaktır. Temel bazı terimleri kısaca açıklayarak içeriğimizi bitirelim.
"""


# GIT-SCM denildiğinde
# 1.Dağıtık Versiyon Kontrol Sistemi # Yani birden fazla yerde versiyon kontrol
# .. sistemi yapısı bulunabiliyor. Böylece projeniz bir çok yerde bulunabilir
# 2.Takımların Aynı Proje Ortamında Çalışmasını Kolaylaştırır
# .. Projenin son hali nerede? Kim neyi düzenledi? Ne zaman düzenledi vs
# .. bunları görebiliyoruz.
# 3.Kim Düzenledi? Ne Değişti? ve Ne Zaman Değişti? Bilgilerini tutar
# 4.Herhangi Bir Dosyaya veya Versiyona Her Zaman Geri Dönüş Yapılabilir
# .. Projenin ilk haline veya 10 dk öncesine geri dönebilirsiniz.Snapshot
# .. yapıyorsunuz ve o kaydı içerde tutuyor. Bu sayede o kaydı içeride tutuyor
# .. Not: Sıkıştırma yaparak içerde tutuyor. Yani dosyaları ziplemenize gerek
# .. yok.
# 5.Yerel Bilgisayarda ve Uzak Bilgisayarlarda Çalışır
# .. Bilgisayarınızın başına birşey gelirse vs bu versiyon kontrol sisteminin
# .. dağıtık yapısına siz projenizi gönderebilirsiniz. Burada GITHUB devreye
# .. giriyor. GITHUB versiyon kontrol sistemi için bir web sitesidir(Hosting)

# Meler Yapabilirsiniz?
# 1.Proje içindeki Tüm Dökümanları İzler # Hangi dökümanda ne gibi değişiklikler
# .. olmuş vs bakabilirsiniz.
# 2.İstenilen Çalışma Anında Projenin veya Dosyaların SnapShot Özelliği ile o 
# .. anki halini alabilirsiniz(Commit)
# 3.Her zaman SnapShot'ları İnceleyebilir veya Geri Dönüş Yapabilirsiniz.
# 4.Hangi dosyanın SnapShot Aldıktan sonra değiştiğini görebilirsiniz.
# .. Commitledikten sonra bir değişiklik yapılmış olabilir bunlarıda görebilirsiniz
# 5.ÖNEMLİ:Projende Versiyonlanmamasını istediğin dosyaları, dosya tiplerini
# .. (*.log, *.mp4) veya klasörleri belirtebilirsin
# Mesela müzik dosyaları, video dosyalarının vs sıkıntı yaratacağı için
# .."git ignore" sayesinde nelerin versiyonlanmaması gerektiğini nelerin takip
# .. edilmemesi gerektiğini de belirtebiliyoruz.
# .. Not: Çoğu kişi "git ignore" dosyasını hazırlamadığı için projenin içerisinde
# .. versiyonlanmaması gereken bir çok şeyi tutuyor ve büyük bir hata yapıyor
# .. bunu da bir çok kere hatırlatacağız.

# GIT-SCM - En çok kullanılan komutlar
# git init     # ilk defa projeyi oluştururken kullandığımız initialize etme komutu
# git add      # Bunu çok kullanacağız. Herhangi bir dosya veya klasörü takip için ekleyebiliyoruz
# git commit   # SnapShot almak için
# git status   # Neler değişmiş(Hangi dosyalar vs) görebiliyoruz
# git push     # Uzak sunucuya gönder. Örneğin github a gönderebiliyorsunuz
# git pull     # Uzak bilgisayardan/sunucudan çek
# git clone    # O projeyi klonlamak/kopyalamak için kullandığımız yapı
# git checkout # Projenin içerisinde birden fazla kişi ya da yapı çalışıyor bunlar arasında geçiş yapabiliyorsunuz
# git rm       # rm:remove # dosyaları ya da klasörleri silmek için

# Bunlardan bazılarını çok az kullanacağız.
# Hangilerini en çok kullanacağız: git add/commit/status

#%% 3.VIDEO GIT Bash ile GIT Temel Komutları
# Project1 diye bir klasörümüz olsun. Ona sağ tıklayıp "git bash here" a tıklıyoruz
# NOT: Ama önce Visual studio code u açıyoruz ve open folder deyip oraya geliyoruz.
# .. Videoda zaten gelinmiş halde başlamış.
# Sonra bir terminal açılacak(Yani proje klasöründe otomatik olarak "git bash" i
# .. aç dedik aslında). Terminal de proje klasörüm nerede ise onun içerisinde olacağım
# .. Yani o terminalde gözüküyor üstte klasör yeri
# İkinci yol Project1 klasörüne girdiğimizde boşluğa sağ tıklayıp "git bash here"
# ... dersek yine aynı şeyi yapmış oluyoruz. 

# Şimdi git i "ilk defa" bu projenin içinde başlatmak istiyorsak "git init" demeliyiz
# Bu ne yapacak.Bir tane gizli klasör açacak. Bu klasörün ismi ".git" olacak.
# Bununla birlikte biz "git" ile birlikte her türlü işlemi yapabiliyor olacağız
# ... Yani Versiyon kontrol sistemimizi proje içerisinde kullanabiliyor olacağız
# .. Eğer başka bir projemiz varsa ve yeni bir proje açtıysak, yine bu proje için de
# .. "git init" dememiz gerekiyor.
# Açılan terminalde "git init" yazalım. Extradan bir klasör oluşturdu gördüğümüz gibi
# .. ".git" adında.Bu klasörün içine bakmamıza gerek yok. Içerisindeki yapı zaten 
# .. git tarafından yönetiliyor.Bi daha "git init" dersek uyarı veriyor
# "git status" yazalım. Kırmızı yazılı yerde; içinde css, index.html ve scss var(hocada)
# .. bunlarla ilgili hiç bir işlem yapılmadı demek istiyor(kırmızı olması sanırım)
# NOT: Hocada klasör(Project1) içinde css ve scss klasör şeklinde, index.html bir dosya
# .. yani html uzantılı bir dosya.. ayrıyeten 2 tane klasör daha var ama onlar burada
# .. gözükmüyor(js ve img) çünkü içlerinde bir şey yok(DIKKAT!)
# Şimdi bir tane dosyanın takip edilmesini istiyorum bu "index.html" olsun şimdilik
# .. "git add index.html" yazıyoruz. Bunu dedikten sonra artık bunu takip etmeye
# .. başlıyor.Tekrardan "git status" yazarsak, css ve scss kaldı orada ve kırmızı
# .. renkli bunlar. yeşil renkte "new file: index.html" yazıyor. 
# Eğer diyelim ki yanlış yazdık bunu "git rm --cached index.html" diye yazarak 
# .. takipten çıkartabilirsin.
# Tekrar "git status" yazarsak css, index.html, scss kırmızı olarak görünecek yine

# NOT: Tek seferde bütün dosyaları eklemek için:
# $ git add .  veya  $ git add *  veya   $ git add -A 
# Şimdi tekrar "git add index.html" diyelim ve takibe başlasın. Bütün olay bitti mi?
# .. Hayır. Takibe başladı ama buradaki değişiklerle ilgili herhangi bir şey yapmadım
# .. Ilk defa projemi onaylamak istiyorsam ve bunun snapshot ini almak istiyorsam;
# "git commit" dersek; bir uyarı geliyor."şu şu ayarları yapar mısın diyor"
# .. Hangi ayarlar? "Run" yazısının altında;
# git config --global user.email "you@example.com" 
# git config --global user.name "Yout Name"
# .. yazıyor 2 satır. Yani "global"(tüm bilgisayarda gibi düşünebilirsiniz) Bunu yapalım
# .. Bunu bir kere yapmamız yeterli
# "git config --global user.email "cansinkutlucann@gmail.com" # Bu bilgi olarak tutuluyor
# .. Yani bu kullanıcı bu versiyon kontrol sistemi ile birlikte bu eklemeleri yaptı diyecek
# .. Yani her türlü eklemeyi ve bilgiyi kullanıcının bilgisi ile kaydedecek. Devam edelim
# "git config --global user.name "Cansin Kutlucan" # Türkçe karakter kullanmıyoruz
# NOT: Bu ayarların bütününü görüntülemek için:git config --list
# Not: Eğer windows işletim sistemi kullanıyorsanız, böyle bir hata ile karşılaşabilirsiniz.
# .. warning: LF will be replaced by CRLF in kaynak/dosya/yolu
# Bu hatanın çözümü için aşağıdaki komutu kullanabilirsiniz.
# git config core.autocrlf true
# Şimdi "git commit" diyelim. Enter a basınca başka bir ekrana attı bizi
# Biz kurarken default olarak "v"(tam anlaşılmıyor başka bir şeyde olabilir) editörünü
# .. kullan diye ayar yapmıştık. v editörünü kullanırken bazı şeyleri bilmiyor olabilirim.
# .. Burada ":q" deyip enter a basıp çıkabiliriz.Şu an commit i mizi iptal ettik 
# .. hiç bir şey yapmadık. Bunu yapmanın daha kolay bir yolu var;
# "git commit -m 'Açıklama'" # .. yazıyoruz genelde ilk commit yaptığımız zaman;
# git commit -m 'First Commit' # ..yazarız
# Şimdi ne oldu bir tane file eklendi bu file da index.html.
# Peki ne oldu şimdi. Visual studio code da sol da index.html in üzerine tıklıyorum
# .. Herhangi bir şey yok. Sağ üstte kod satırı var oraya "deneme" yazalım ve
# .. kaydedelim(ctrl + s)
# Sonra geri gelelim git-bash e "git status" yazalım
# Neler olmuş?
# kırmızı renkle modified: index.html yazıyor...
# Şimdi ben değişikleri görmek istiyorum.
# "git diff" # diff:difference # Bütün değişiklikleri gösterecek. Enter a basarsak
# satırlarda;
"""
...
---a/.index.html
+++b/.index.html
@@ -0,0 +1 @@     # Yer imi1
+deneme
"""
# a ile b nin arasındaki fark şudur(Yer imi1 e bak) diyor ve deneme yazısı olmuş diyor
# Tekrar visual studio code a dönelim ortadaki boşluğun sağ üstünde çarpı var kapatalım
# Sol da "style.css" in yanında "U"(untracked) işareti var. "main.scss" nin yannında aynı şekilde "U"
# .. index.html in yanında "M"(Modified) işareti var yani dosyanın değiştiğini ifade ediyor.
# .. NOT: orada 1 vs yazarsa; HATA anlamında
# geri Git bash e gelelim
# git commit -m 'index dosyasi degisti'
# Uyarı geldi. Tamam da ne ile ilgili işlem yapmak istediğini söylemedin diyor.
# Şimdi devam edeceğiz ama bir tane daha ekleme yapalım
# git add css/style.css diyelim
# 1 tane yeni dosya 1 tane modifiye edilmiş dosya var bi yane untracked
# git commit -m 'style dosyasi eklendi'
# .. dersem;
# git status
# .. sadece style dosyasını commitlemiş olduk. Şu anda index.html ile ilgili herhangi bir şey yapmadım
# .. Her seferinde şunu hatırlamalıyım;
# git add index.html
# git commit -m 'index dosyasi degisti'
# .. deyip enter a basarsam, artık uyarı vermneyecek bana 
# 1 file changed, 1 insertion(+) yazacak. Önceden 0 insertion dı.
# Yani 1 dosya değişti . 1 insertion(ekleme) yapıldı
# Tekrar visual studio code a gelirsem index.html in yanındaki "M" gitti.
# style.css in yanındaki "U" gitti sadece main.scss nin yanında "U" duruyor.
# style css de code yerine "dosyada degisiklik yapildi" yazdık kaydet(CTRL + s)
# index.html e gelip oradaki "deneme" yazısını da silelim ve kaydedelim.(CTRL + s)
# tekrar git bash e gelip "git diff" dersem hepsini gösterir
# git diff index.html  # .. diyelim
# Bu sefer "deneme" yazısı kırmızı renkte yani silindi diyor
# git diff dersem hem style.css deki ekleme işlemini(yeşil renkte) hem de 
# index.html deki deneme yazısını silme işlemini gösteriyor.(kırmızı renkte)

# git commit -m 'index ve style dosyasi degisti' (NOT:HOCA: daha açıklayıcı
# .. yazılar yazarsanız daha iyi olur) .. Uyarı geldi. Yine eklememişsin dedi
# git add index.html
# git add css/style.css
# git commit -m 'index ve style dosyasi degisti' 
# Şimdi oldu ve "2 files changed, 1 insertion(+), 1 deletion(-)" geldi

# Peki bu işlemleri daha farklı yapabilir miyiz? Yani visual studio code un içerisindeki
# .. terminali kullanarak yapabilir miyiz?
# Aynı işlemleri yapacağım ama buradaki bilgileri de sileceğim.
# Bu 3 yöntemden birisiydi, Şimdi diğer yönteme(visual studio içerisindeki terminali kullanarak
# yapmamaya) geçelim.

## EXTRA NOTLAR
"""
git log
Projedeki commit geçmişini görüntülememizi sağlar. Bütün commit'ler, id'si, yazarı, tarihi ve mesajı ile beraber listelenir.

git branch
Local veya remote repository üzerinde yeni bir branch (dal) eklemek, silmek veya listelemek için kullanılır.
git branch <branch_name>

git checkout
Branch’ler arası veya commit'ler arası geçiş yapmak istediğimizde kullanılır.
git checkout <branch_name>

Yeni bir branch oluşturup, bu branch'a geçiş yapmak için;
$ git checkout -b <branch_name>

Commitler arası geçiş yapmak için: (Eski bir versiyona dönmek istediğimiz zaman)
$ git checkout <commit_ID>

git merge
Başka bir branch'da olan değişiklikleri, bulunduğumuz branch ile birleştirmek istediğimizde kullanılır.
$ git merge <branch_name>

git clone
Mevcut bir Remote Repository'de bulunan dosyaların bilgisayarımızda bir kopyasının oluşturulmasını sağlar.
$ git clone <remote_URL>

git push
Projemizde aldığımız commit'leri, remote repository'e gönderir.
$ git push origin master
Burada bahsi geçen origin remote repository’nin kök dizinini belirtir ve sabit bir isimdir. master ise sizin çalıştığınız branch (dal)’ı belirtir.

Henüz remote repository’niz yoksa aşağıdaki komut ile local deponuzu uzak sunucudaki depoya bağlayabilirsiniz.
$ git remote add origin http://uzak_deponun_adresi.git
"""

#%% 4.VİDEO - VS Code içinde Terminal Kullanarak GIT Temel Komutları
# önce klasöre geçiş yapalım. git bash de;
# "explorer ." yazalım. Klasörler geldi
# üstte görünüm-->(sağda)seçenekler --> klasör ve arama seçeneklerini değiştir -->
# .. -->gizli dosyaları göster.
# Şimdi ".git" dosyasını görüyoruz. Buna sağ tıklayıp silelim.
# NOT:Hoca: Bunu size tavsiye etmem. Çok büyük risklere yol açabilirsiniz.
# Şimdi visual studio kod a girelim.Project1 klasörünün içerisinde iken üstte 
# .. "Terminal" --> "new terminal" e tıklayalım.windows powershell ile birlikte geldi
# git --version yazalım
# çıktı: git version 2.29.2.windows.3 # Yani git bu projenin içerisinde varmış
# git init dedik # Bu dosyanın içinde ".git" klasörü oluşmuş oldu tekrardan
# git add index.html
# git add .\css\style.css
# Bu şekilde ekledik
# git status # Dosyaların durumlarına baktım
# git commit -m 'index ve style eklendi'
# çıktı: 2 files changed, 1 insertion(+)
# vs vs aynı kodları deneyebilirim.
# Bir şeyler değiştirdik üstte kod satırlarına bir şeyler yazdık hem css de hem index.html de
# git diff
# .. dedikten sonra en altta "(END)" yazıyor. "q" ya basarak çıkabiliyoruz
# git add index.html
# git add .\css\style.css
# git status
# .. status te bu dosyaların modifiye edildiğini söylüyor, ama 
# .. bu dosyaları biz halen onaylamadık.Onaylamak için
# git commit -m "iki dosyada degisti" # NOT: normalde açıklamaları daha düzgün yapmalıyız
# .. commitledik ve soldaki "M" işaretleri gitti.
# git status
# .. Şu anda herhangi bir değişiklik yok diyor
# Yani terminalden de aynı işlemleri yapabiliyorum

# 3. yöntem visual studio codun kendisi ile bu işlemleri nasıl yapabiliriz. Onlara bakalım
#%% 5.VİDEO - 
# DİKKAT solda en üstteki menüde dosyaları ve statülerini görüyorum 3. yer versiyon kontrol sistemi
# .. 3. yerden ekleme değiştirme vs yapacağız.
# Vs code da soldan 3 üncüye tıkla--> Initialize Repository(Yani "git init" in yapılması gerektiğini söylüyor)
# .. tıkladık(yani kendisi yapsın bunu)
# .. Dosyalar geldi solda üç dosyadada değişiklik yok diyor ( "U"(UNTRACKED) )
# Ne yapmamız lazım? solda dosyanın üzerine gelince işaretler çıkıyor
# Orada "+" ya basalım birine. "Changed" durumu "staged change" e döndü. Yanında "A" yazıyor
# Sonra "SOURCE CONTROL" ün sağındaki "V(Tick)" e basalım(Bu commit butonu)
# ... Çıkan yere "first commit" yazalım.
# .. Şimdi "index.html" in yanından işaret gitt yani UNTRACKED değil artık TRACKED yani
# .. takip ediliyor.
# Kodda bi r şeyler yazıp değişiklik yazalım "CTRL + s" ile kaydettim
# index.html yanında "M" yazıyor. solda dosyanın üzerine gelip tıklayalım 
# .. sağ da ne çıkarılmış ve ne eklenmiş görünüyor
# Dosya üzerine gelirsem yine "+" ya basarsam şuanki "stage" ini değiştirebilirim
# .. Ya da "(geri işareti)" ne basarsam eski haline geri getirebilirim.basaslım--discard changes
# .. Dosyanın ilk hali geldi
# .. Yine değişiklik yapalım
# .. yine commit(V) tuşuna basalımn vs
# Neler olduğunu görmek için SOURCE CONTROL ün ssağında "..." ya tıkla --> views --> source control repositories

# index.hmtl e gelelim şimdi
# html kodu yazalım
# Tekrar dosyaya tıklayalım değişiklikleri görelim
# "+" ya basalım sonra bunları eklenmesini istiyorsam "commit(V)" e basalım
# .. çıkan yere "index.html değişti" diye not yazdık

# HOCA: Terminal de bu işlemleri yaparsanız eliniz alışırsa, daha iyi olur

#%% 6.VİDEO - gitignore Dosyası Ne İşe Yarar? Nasıl Kullanırız?
# Her bir dosyayı vs code içinden de olsa terminalden de olsa tek tek eklemek
# .. çok can sıkıcı. Belki 10 dosya var çünkü orada. Ama ben projemin içerisindeki
# .. her şeyi version kontrol sistemine eklemek istiyor muyum?
# Mesela bir tanıtım videomuz var diyelim. Bunun versiyon kontrol sisteminde işi 
# .. var mı gerçekten ? Aslında bu 1 kere yüklendi ve bitti youtube duruyor.
# .. Yanlışlıkla proje klasörüne girmiş olabilir.
# Aslında bu tür dosyaları proje klasörünün içinde tutmamamız lazım. Ne tür dosyaları
# .. tutmamamız lazım? 
# görseller, videolar, logolar, paket yöneticisi ile kurulmuş dosyalar
# .. Bu tarz yapıları versiyonlamak istemem. Çünkü içerisine kod yazmıyoruz
# Şimdi bunları versiyon kontrol sisteminde tutmamayı sağlayacağım
# vs code da soldan ilk menü, sonra project1 in sağındaki ilk ikona basıp
# .. yeni bir dosya açıyoruz(Yani projenin içerisinde yeni bir dosya açıyoruz)
# .. ismini de ".gitignore" koyalım. Bu ".gitignore" sayesinde istemediğimiz
# .. herhangi bir yapının versiyon kontrol siteminde olmamasını sağlayabilirsiniz
# Hangi programı geliştiriyorsanız ona göre internette hangi dosyaları ignore etmeniz
# .. gerektiğini bulabilirsiniz. Örneğin "gitignore Python" yazarak
# Bu gitignore un kod kısmına bunları yapıştırıyoruz.
"""
# IDE- VS code
.vscode/*  # Not: ide ile alakalı bir dosya bu(vs code ide si). Bunu da tutmama gerek yok mesela
...
...

# img
*.jpg
*.png
logo.jpg
img/
# Şimdi buraya kadar olan yerde hoca kaydetti ve vs code da soldan 3 üncü menünün
# .. üzerinde "9" yazıyordu o "1" e düştü çünkü dosya içinde jpg ler vs vardı ve
# .. onları iptal ettik

# videos
*.mp4

log
*.log
password.txt

# NOT: BURADA "password.txt" bir dosya ismiydi yani ben hem isim belirtebilirim
# .. Hem uzantı ".log" için "*.log" yazdık gibi
# .. Hem klasör ismi "img" gibi.(Hocanın klasörünün içinde "img" isimli bir klasör var
# .. biz onu "img/" diye yazıyoruz "gitignore" a
"""

# ilk projenizi açtığınızda hiç bir şey yapmadan önce gitignore dosyasını oluşturmak
# .. daha iyi olacaktır. Hangi dosyaları almayacağınıza karar verebilirsiniz.
# NOT: gitignore olmadan github a gönderirseniz projenizi insanlar boş yere video,resim
# .. gibi dosyaları indirmek zorunda kalabilir. Bu da istemedikleri bir şeydir

# Şimdi bunu oluşturduk sonra soldan 3 üncü menüde iken dosyanın(.gitignore) üzerine geldik
# .. "+" tuşuna bastık "M" çıktı. Sonra commit(V) edeceğiz. Nota "gitignore added" yazabiliriz
# gitignore u sürekli olarak güncellemeniz de gerekebilir bazen

"""
NOTLAR
.gitignore Dosyası Ne İşe Yarar? Nasıl Kullanırız?
.gitignore dosyası projemizin kök dizinine oluşturulan düz bir metin dosyasıdır.
 Adından anlaşıldığı gibi diyor ki beni göz ardı et. Daha doğrusu göz ardı etmek istediğin, 
 local çalışma alanındaki takip edilmesini istemediğin, takım arkadaşların için gerekmeyen 
 dosyaların varsa veya bu dosyaların boyutu reponuza atmanıza gerek olmayacak kadar büyük ölçekli ise buyur beni kullan diyor.

Gel bu dosyaları .gitignore dosyasına koy ki GIT de senin bu dosyalarını artık takip etmesin. 
Üstelik bu işlemler yapılırken senin halihazırdaki dosyalarını da hiç bir şekilde etkilemesin. Daha ne olsun!

Peki nedir bu tür dosyalar ?
Paket yöneticisinden indirilen bağımlılıklar,
image ve video dosyalarınız(dosya boyutları çok fazla olabilir)
IDE eklentileri( örneğin .vscode)
Sadece kendi çalışma alanınızda olması gereken başkaları tarafından görülmemesi gereken dosyalarınız (veritabanınıza ilişkin konfigürasyonlar)
API anahtarları, kimlik bilgileri veya hassas bilgiler içeren dosyalar(.env)
Çalışma dizinizdeki geçici dosyalar
Log dosyaları
Yararsız sistem dosyaları (örneğin MacOS işletim sisteminin .DS_Store dosyası )
dist gibi oluşturulan dosyalar
Veya herhangi bir dosyanız da olabilir.

Nasıl oluşturulur?
Reponuzu oluştururken verilen seçeneklerde add gitignore file dosyasına tıklayarak reponuzla 
beraber oluşturabilirsiniz. Aynı şekilde editörünüzde .gitignore şeklinde de oluşturabilirsiniz.

Yok ben terminal aşığıyım diyorsanız da buyrun :)

Proje dizininize cd komutu ile gelerek **MacOS /Unix için; **
$ touch .gitignore 

Windows için;
$ echo some-text or nothing > .gitignore

şeklindeki komutlarla dosyanızı komut satırından oluşturabilirsiniz. 
Buradaki some-text or nothing kısmı .gitignore dosyasına yazılmasını istediğiniz metini ekler. Hiçbir şey de yazmayabilirsiniz.

Nasıl çalışır, nasıl kullanılmalı?
.gitignore dosyasının her satırına takip edilmesini istemediğimiz dosyaları veya dizinleri yazarak göz ardı edebiliriz.

Tabii bu dosyaları yazarken bize kolaylık sağlayan bazı formatlar var. İşte onlar:
-Uzantılar
.env

- Dizinleri ise klasörün sonuna `/` işareti ekleyerek  belirtiriz. 
node-modules/ dist/ logs/

- `*` yıldız karakteriyle ise belirtilen ilk örnekte `.log` uzantısına sahip dosyaların tümünü, ikinci örnekte ise `files` klasör içerisindeki bütün dosyaları izlemeyi bırakacaktır. 
.log files/

- Eğer ki bir klasörümüzü içerisindeki bir dosya haricinde izlenmesini istemiyorsak `!` işareti ile bunu sağlayabiliriz. 
Bu örnekte `files` klasörü içerisindeki `example.txt` haricindeki dosyalar izlenmeyecektir. 
Files klasörü içerisindeki sadece **example.txt** git akışında görülecektir.
!files/example.txt

- Yukarıdaki örnekte dikkat edilmesi gereken önemli bir ayrıntıyı açıklayacak olursak eğer ki daha öncesinde
 `files` klasörü `.gitignore` dosyasına eklenmişse sonrasında ise `!`  içerisindeki dosya ile işlem yapmak işe **yaramayacaktır.**
files/ !files/example.txt

- `.gitignore` dosyasında yorum satırı oluşturmak için ise `#` karakteri kullanılır.

Kullanımından da bahsettiğimize göre gelelim dikkat edilmesi gereken hususlara...
## Neye dikkat etmeliyim?

- Eğer projenizi `git add .` veya `git commit ` etmişseniz sonrasında  `.gitignore`  dosyasına eklemek
 istediğiniz dosyayı ekleseniz de bu işlem gerçekleşmeyecektir ve o dosyanız reponuzda hala GIT ile 
 takip edilecektir. Tabi her şeyin bir çözümü olduğu gibi bu sorunu da çözmenin bir yolu var. İşte o çözüm .

```bash
$ git rm --cached FILENAME


Hani olur da derseniz ben belli dosyalarımı her seferinde .gitignore dosyasına eklemek istemiyorum 
bunu tek seferde halledebilir miyim ? Tabii ki buna da bir çözüm bulmuş GIT babamız :)
Burada kastımız başka başka projeler için her seferinde eklememek.

-Windows kullanıcısı iseniz C:\Users\{myusername}\ adresine giderek .gitignore_global dosyası 
oluşturup içerisine global olmasını istediğiniz dosyaları ekledikten sonra git bash terminalinizi 
açarak aşağıdakı komut ile konfigürasyon sağlayabilirsiniz.
$ git config --global core.excludesfile "%USERPROFILE%\.gitignore"

-Dosyanızın doğru çalıştığını kontrol etmek için ise aşağıdaki komutu çalıştırarak aşağıdaki 
çıktıyı aldığınızda sorunsuz çalıştırabilmişsinizdir. 
(Aşağıdaki kodu kopyala yapıştır yapmadan önce kullanıcı adını değiştirin.)
$ git config --global core.excludesfile
> C:/Users/user-name/.gitignore_global  

Son olarak hangi .gitignore dosyalarını eklemeliyim derseniz buradan(https://github.com/github/gitignore)
hangi dil, framework vs kullanıyorsanız ona ait .gitignore dosyalarını bulabilirsiniz. 
Global olarak düzenlemek istediğiniz .gitignore dosyalarına da 
buradan(https://github.com/github/gitignore/tree/main/Global) erişebilirsiniz.
"""

#%% 7.VIDEO - GIT - Proje İçindeki Birden Fazla Dosyanın Versiyon Kontrol Sistemine Eklenebilmesi
# Daha önce git add i kullanarak hangi dosyaları eklememiz gerekiyorsa onları eklemiştik
# .. Bu hoş bir kullanım değildi. Niye tek tek eklemeye çalıştık? Çünk önceden ".gitignore"
# .. dosyamız yoktu ondan dolayı. ".gitignore" varsa artık tüm dosyaları "git add" ile birlikte
# .. ekleyebilirim. Yani bir değişiklik oldu diyelim.Mesela;
# Sol üstteki menüye tıkla sonra dosyaların olduğu yere sağ tıkla-->new file
# buna "test.html" diyelim.
# Dosyada bir değişiklik yapalım.
# Sonra "index.html" dosyasında da değişiklikler yapalım.
# NOT: "index.html" de değişiklik yapınca komut satırındaki değişiklik yapılan numaraların yanında
# .. mavi bir çizgi oluştu. "M" olarak değişti
# Geri gelelim "test.html" e yanında "U" var yani arşivlenmemiş/Takip edilmiyor henüz
# Diğer 2 dosyada da değişiklik yapalım 3 tane "M" bir tane "U" oldu
# terminali açalım
# "git add ." dersek tüm dosyaları hep birlikte ekleyebiliyoruz
# "git commit -m 'html files changed'
# Sonra solda 3.üncü menüdeki 4 rakamı gitti. 4 dosyada değişiklik oldu yani her şey yolunda

# vs code da bu işlemi şöyle yaparız. Diyelim değişiklikleri yaptık sonra
# .. soldan 3 üncü menüden changes in üzerine gelip "+" ya basarsak hepsini ekler. Ya da "(undo işareti)"
# .. ile geri de çevirebilirim. Ya da dosyanın yanındaki "+" lara tek tek basabilirim
# .. Sonra yukarda ki commit(V) e bastık

# Şimdi geriye dönüp bakmak istiyorum. Sol üstteki menüye tıkla
# Sol alttaki kısımda timeline a gelelim. Orada alttan itibaren neler olmuş görebiliriz tıklayınca

# Başka neler yapabiliriz
# Projende bir değişiklik yapmak istiyorum. log in ekranında çalışma yapıp denemek istiyorum ve değişiklik
# .. olsun istemiyorum. Bunu yapmak için ;
# soldan 3 üncü menüye gel --> (SOURCE CONTROL YANINDAKI) ...(üç nokta) --> branch --> create branch
# .. branch name e "loginForm" dedik.
# Sol en altta loginForm yazıyor artık. Daha önce ne vardı? "master" vardı
# .. Geçişi nasıl yapabiliriz. Sol altta "loginform" yazan yere tıkla sonra "master" a tıkla 
# .. ya da terminalden "git checkout master" yaz
# şimdi login form a geldik . Sol en üstteki menüdeyken dosyaların oraya sağ tıkladık ve new file dedik
# "login.html" diye bir yapı oluşturduk.
# Bu branch in içerisinde bir işlem yapalım. Sonra dedik test edelim. test ettik sonra kaydettik
# 3. menüde baktık bir değişiklik var "M" . "+" butonuna bastık. commit ettik. "form eklendi" dedik
# Sonra master a geçiş yaptığımız zaman sol en üst menüye tıkladığımızda "loginform" dosyası kayboldu
# Geri dönmeye çalışalım. Nerede bu dosya? terminal i açayım
# "git checkout loginForm" dersek tekrardan o dosyamızı görebiliriz.
# Bu branchlerde başka başka kişilerde çalışabilir. Bu branch ismi "Cansın" da olabilir vs vs
# NOT: ÖNEMLİ loginform un içerisinden "create branch" dersek "loginform.html" dosyasıda gözükür
# .. ama masterdan yapsaydık işlemi gözükmeyecekti. DALLANMA yapıyor aslında
# "Cansın" ın içindeki "loginform.html" i değiştirirsem "loginform" un içindeki "loginform.html" DEĞİŞMEYECEKTİR
# "Cansın" yapısı ile "master" ı birleştirmek istersek, "cansın" içindeyken terminal açıp
# "git checkout master" dedik. master ın içerisindeyiz
# "git merge Cansın" diyoruz. 
# Sonra "master" ın içerisinde "loginform.html" dosyasını görebiliyorum artık
# "Cansın" içinde "loginform.html" i değiştirelim commit vs edelim. 
# .. "master" içinde değişmemiş olacak. Ama değişmesini istersem yine;
# "git merge Cansın" dersem "master" içindeki dosyada değişecektir.

# "master" branch i projemizin Canlıya alınacağı hali diye düşünebilirsiniz

# Şimdi bunu uzak bilgisayara atıp bunu uzak bir sunucudan takip edelim.
# Bu versiyon kontrol hosting üzerinden olmalı. Bunu da "github" üzerinde yapacağız

# NOTLAR
"""
git push
Commit’lediğimiz dosyaları versiyon kontrol sistemimize gönderir.

GitHub hesabımızı kontrol ettiğimizde tüm dosyaların ve commit işlemlerimizin ulaştığını görmüş oluruz.
"""

#%% 8. VIDEO - GitHub'a Projemizin Eklenmesi ve Diğer Repo Hosting Web Platformları
# GIT vs GITHUB
# GIT: Bir versiyon kontrol sistemi
# GITHUB: Bu versiyon kontrol sisteminin içerisinde tuttuğunuz repoları host edebileceğiniz
# .. bir platform

# Github a girince sağ üstte "+" butonuna basıp "new repository" diyelim
# Repository name "deneme" olsun.
# private veya public i seçelim. şimdilik private seçelim
# "add a README file" : Projemizin içerisinde yaptığımız işlemler daha iyi gözükecek
# .. şimdilik eklemiyorum
# "add .gitignore" : Eklemiyoruz çünkü daha önce eklemiştik
# "Choose a license" : Yaptğınız işlemlerle ilgili lisan seçenekleri
# .. Hiç birini işaretlemedik.
# "Creating repository" ye basalım

# Sürükle-bırak ile buradaki yapının içerisine aktarabiliyorum veya
# "set up in Desktop": masaüstü uygulaması ile kullanabiliyormuşum

# Yeni repo oluşturmak için
# "Create a new rep..." nin altında "readme" dosyasını oluştur diyo
# .. git init yap diyor vs vs aşamaları söylüyor
# .. yine o bölümde "git branch -M main" var.
# Bunu bir deneyelim "vs code" da
# terminal e gelelim
# "git branch -M main" yapalım. main branch e geçtik. branch i oluşturduk
# Altta "git remote add origin https://github.com/cansinkutlucan/deneme.git" var
# Bunu kopyalayalım vs code a dönelim. terminal açalım
# "git remote" dersem sonuç gelmeyecek.Hata da yok. Bu reponun içerisine herhangi
# .. remote bir bağlantı eklenmemiş. Peki ekliyorum şimdi;
# git remote add origin https://github.com/cansinkutlucan/deneme.git
# Sonra tekrar "git remote" yazıyorum .. çıktı: "origin" isimli bir remote bağlantı
# .. eklenmiş.
# NOT: # "or push an existing ...." in altında da benzer şeyler var(DEVAM EDELİM ALTTAN)
# En sonda da (githubda)yazan"git push -u origin main" i de terminal e yazalım
# .. bunu origin e aktaralım. Bunu yapınca kullanıcı ismi ve şifrenizi yazdıysanız
# .. otomatik olarak aslında bu branchin içerisine eklemeleri yapacak. Bu eklemeleri
# .. yapıyor şu anda. Bitince github da bunu sayfa yenileyince göreceğiz
# Ama diyoki read mi dosyasını eklememişsin diyor. Yanından "add a readme" var
# .. Ona tıklayabiliriz ama onun yerine biz , git e gelip soldaki boşluğa sağ
# .. tuşa tıklayıp "newFile" , dosya ismi "README.md" diyoruz. Bu "md:" "markdown"
# .. dosyası anlamına geliyor.
# .. Markdown yazalım sağa diez(#) koyup vs. Alttakileri yazalım
"""
# Deneme

## Alt Bilgi

sadasgaksg
asgasg
[lorem ipsum](https://google.com)
"""
# .. kaydedelim. Kaydettikten sonra; soldan 3 üncü menüye gel sonra README.md
# .. nin yanındaki + ya basalım sonra commit(V) edelim. nota "readme added" yazalım
# .. Peki uzak yapıya ekledi mi? Hayır eklemedi. Ekranın sol altında 
# .."0 altokişareti 1 üstokişareti" var orada 1 in anlamı: 1 tane eklenecek
# .. yapı var demek oraya tıklıyoruz. Üstte gelen yerde "OK" a tıklıyoruz
# .. şu anda git push yaptı. İşlemi otomatik yaptı.. sol alttaki 1, 0 a döndü.
# Github a geldim sayfayı yeniledim. DENEME nin altında yukarda yazdıklarımız
# .. görünüyor. DIKKAT: Orada linki google.com yazdığımız için lorem ipsum tıkladığımızda;
# .. bizi google a götürüyor.
# Yukarda 1 branch yazıyor. Yani 1 tane branch in olduğunu bu branch le birlikte
# .. yapının aktarıldığını söylüyor.
# Sağ da Languages var./HTML: %93.6, CSS:6,4 .. Yani yapıda ne kadar HTML ne kadar
# .. CSS olduğunu söylüyor.
# Projeyi silmek istersem. Üstte "settings". En altta "delete this repository"
# .. ye basabiliriz. Silmeden önce şöyle bir şey yapalım;
# README.md nin yanındaki "kalem işaretine(düzenle)" tıkla. Burada değişiklik yapayım
# .. linki silelim mesela
# altta "commit changes" altındaki şeyi silip "readme file changed" yazdık ve
# ... "commit changes" e tıkladık. Tekrar geri dönüp "Deneme" ye bakalım. Link gitmiş
# Peki projemde değişti mi ? Git bash e geliyorum bakıyorum link orada duruyor
# .. Bunun içinde terminale "git pull" yazabilirim. Yani uzak bilgisayarda değiştiyse
# .. burada da değişmesini sağlayabilirim. Git pull yaptıktan sonra enter dan sonra 
# .. üstteki link gitti kod satırında.
# SONUÇ: "push" la gönderiyorum uzak bilgisayara "pull" la çekiyorum uzak bilgisayardan
# Githun da sağ üstte 13 commits yazıyor 13 commit olmuş. tıklayalım neler olmuş
# .. görebiliriz. Geri gelelim. index.html e tıklayalım sağ üstte history ye 
# .. tıklayalım. ne tür değişikler olduğunu görebiliriz.

# Github da sağ üstte "Code" a tıklayalım orada "Clone" var. "Clone" ne yapıyor?
# .. Eğer izniniz varsa(ki bu benim kullanıcı olduğumdan dolayı iznim var)
# .. oradaki linki kopyalayıp sonra cmd yi açıp
# "git clone https://github.com/hakan..." yazıp bu repoyu direkt olarak
# .. çağırabilirim.
# .. sonra "dir" yazalım yine cmd ye. "deneme" klasörü oluştu(isim ne ise o
# .. isimde klasör oluşuyor)
# .. sonra "cd deneme/" yazalım
# .. "dir" yazalım
# .. Sonuçta daha önceki benim yapım ile birlikte daha önceki repoyu buraya
# .. koymuş oldum.

# GITHUB dışında hostingler var. GITLAB, BİTBUCKET da var.
# GITLAB içinde mesela bir projeniz var ve bu projenizde kendi sunucunuuzu
# .. yani kendi versiyon kontrol sistemi sunucunuzu kurmak istiyorsunuz, çünkü
# .. kapalı bir alanda projenizin çalışmasını istiyorsunuz. Bununla ilgili
# .. GITLAB ın çözümleri var. Ama GITHUB ı kullanabilirsiniz siz. Çünkü
# .. herkes GITHUB ı kullanıyor.

# Son olarak komutları hatırlayalım
# git init -- ilk kez proje oluştururken kullandık
# git add <file> # 1. yol
# git add . (all)
# git commit -m 'aciklama'
# git status
# git status
# git diff
# git checkout branchName
# git push
# git pull
# git clone

# Başlangıç için 10 tane komut kullandık bunlar size şimdilik yetecektir.
# git scm sitesinde solda "BOOK" a bakacak olursanız orada türkçe dökümanı
# .. inceleyebilirsiniz. 
# SONUÇ: Herkes GITHUB diyor ama GIT i önce öğrenmemiz gerekli aslında

# Aşağıdakilerden hangileri versiyon kontrol sistemine yapılan değişikliği göndermek için uygulanan doğru yoldur ?0
# CEVAP: "git add README.md" -> "git commit -m "mesaj" -> "git push"

#%% 9. VİDEO - Markdown Nedir? Nasıl Kullanırız?
# Markdown a neden ihtiyaç duyuyoruz?
# Sadece read.me için markdown u kullanmıyoruz.
# Bunu öğrenirseniz hayatınız kolaylaşacak
# www.commonmark.org sitesinde markdown ile ilgili güzel bilgiler var
# Bir çok dildede markdown kullanılabiliyor. Markdown çeviriciler var

# Başlık yapacaksak (#)
# Maddeler yapacaksak (*)

# Bir editörden bahsedelim .. www.typora.io
# Yazdığınız herşeyi markdown dan normal görüntüye çekiyor.
# Mesela; ##Markdown ... yazdık

# Markdown da 4 temel yapıyı öğrendikten sonra güzel şeyler yapabilirsiniz
# Yeni bir sayda açalım(READ.me) dosyasını düzenleyelim git bash de
"""
#    -> h1
##   -> h2
###  -> h3
"""
# Bunu typora da denersek typora da yazılar nasıl görünüyor bakabiliriz
# Typora da üstte themes da farklı temalar var

"""
-   ... Bu maddeler oluşturacak
- list item 1
- list item 2

ya da

* list item 1
* list item 2

"""
# diğer özellik (*)
"""
*italic*
** bold**
*** bolditalic***

ya da

_italic_
__Bold__
"""
# link eklemek isteyelim.
# linkin 2 kısmı var. Biri açıklama, diğeri linkin kendisi
"""
[]() köşeli parantez açıklama için, normal parantez link için

[Google a gitmek için tıklayınız](www.google.com)

# Eğer bir imag vermek istersek başına ünlem ---> ![]() 

![Lorem picsum görsel](https://picsum.photos/200/300) .. bunu typora da yazınca resim gelecek

git bash de sağ altta "plain text" yazan yere basıp sonra gelen yazma yerinde "markdown"
.. yazalım yani kaydettik aslında sonra "open markdown preview" geldi. Enter
.. artık burada da resim görebiliyoruz.

# Bu preview ın benim yazımın yanında gözükmesini istersem;
# Üstteki sekmeyi git bash de sağa doğru sürüklersem ekran 2 ye bölünecek
"""
# Başka bir özellik: Çizgiler
"""
---------------------------

Mesela yukarıdaki gibi çizgi çekersek sağ tarafta da bir çizgi oluşuyor
ya da 

***
"""
# Bu arada curser solda curser neredeyse sağ da da aynı yerde oluyor
# başka örnek :* list item 1 [Google a gitmek için tıklayınız](www.google.com)

# www.commonmarkdowm.org sitesinde "LEARN MARKDOWN IN 60 SECONDS" a tıkladığınızda
# .. yukarıda anlattılanlar çıkıyor özet olarak

# Diğer önemli bir özellik. Kod bloğu oluşturmak için "backtrick" işareti
"""
```  
print('hello word')
```

# Aşağıdaki şekilde yaparsak bunun python olduğunu söylemiş oluyoruz

```python  
print("hello word")
```
ya da mesela

```javascript  
console.log("hello word")
```
"""

# notion.sh .. çok fazla kişi kullanıyor
# notion markdown ı destekliyor. Bunun içinde markdown kullanarak çok güzel
# .. içerikler oluşturabilirsiniz
# git bash den file -- export dan farklı şekillerde yazabilirsiniz. İlla HTML
# .. yapmanıza gerek yok.

# SONUÇ: Markdown güzel, kaliteli yazı yazmanızı sağlıyor











