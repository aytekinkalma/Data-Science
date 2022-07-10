""" ---Statistics-4---ders1


 Sampling Distrubition:10000 kisilik universitenin boy dagilimini gormek istiyoruz
 10000 kisiyi incelemek zor olacagi icin bunlarin icinden orneklem alacagiz
 n=100(orneklem) olsun,bunlarin boy ortamasini hesaplayacaz(x̄)
 bugun sectigimiz 100 kisiyle yarin sectigimiz 100 kisinin ortalamasi ayni olmayacak
 sectigimiz ornekleme gore ortalamalar da degisir
 bu orneklemlerden alacagimiz olasi tum ortalamalar bize orneklem dagilimini olusturacaktir
 populasyon dagilimindan daha az varyansi olan ve populasyon ortalamasi etrafinda dagilan bir dagilim olur

 ornek
Bir zari atma durumunu inceleyelim
 x       1     2     3     4     5    6
 p(x)   1/6   1/6   1/6   1/6   1/6  1/6
 boyle bir dagilim discrete uniform bir dagilimdir
 Ayrık tekdüze dağılım (İngilizce discrete uniform distribution), olasılık kuramı
 ve istatistik bilim kollarında, bir rassal değişken için belirli bir alt ve üst sınır
 tam sayı arasında mümkün olan bir sıra tam sayı sonuç değerlerin hepsinin eşit ölçüde
 olasılık göstermesi özelliğini taşıyan ayrık olasılık dağılımıdır.
 adil bir zarda her durumun gelme olsailigi 1/6 dir

 Uniform bir dagilimdan iki zar cekecegiz x1,x2
 Sampling Distrubitionx(x̄)=(x1+x2)/2
 Sample distubition burada orneklemi iki olan tum olasiliklara bakacaktir buda .
 (1/6) yani bu bir sayinin gelme olasiligi orneklem iki oldugu icin
 1/6*1/6=1/36 36 farkli ihtimal gelecektir(ayni anda iki zarin atilmasi)
 Sampling Distrubitionx(x̄) populasyon ortalamasina p(x̄) esit olacaktir
 iki zar deneyinde ortalama=3.5                          populasyon ortalamasi=3.5
 standart sapma=1.21(populasyon standart sapmasi/√¯n)    populasyon standart sapmasi=1.71

 (populasyon standart sapmasi/√¯n)  standart hata olarak da isimlendirilir(ortalamamnin standart hatasi)
 ornek:Aunt Erma isimli yiyecek ve icecek satan bir resturant var.Gunden gune satislari degisiyor.Gecmis kayitlar
 gunluk olarak 900$ elde edildigini gosteriyor(μ) ve standart sapmasi(σ)=300$
 haftalik satislarin varyansi(variability) degiskenligi ne kadar olur?
 orneklem ortalamasinin dagilimin standart sapmasi nedir(Haftalik satislara iliskin standart hata)?
 orneklem dagilimin standart sapmasini yorumlayiniz
 cozum:
 μ=900$
 σ=300$
 n=7 (Haftalik dedigi icin n i 7 aldik)
 σx(standart hata-standart error)=populasyon standart sapmasi(σ)/√¯n=300/√7=113.4
 orneklem sayisi 7 olan sampling distrubitionun ortalamasini ve standart sapmasini hesapladik
 yukarida belirtildigi gibi populasyon dagilimin ortalamasi ile orneklem dagilimin ortalamasi ayni(900),
 standart saomalari(300-113.4) is farklilik gosterdi
 soruda aylik kazan ortalamasi istenseydi n i 30 alacaktik


 ---------EK NOT----------
 *Normally, the sampling distribution of the mean does not exist. It is theoretical. Because we need infinite numbers of samples.
 Merkezi limit teoremi çok sayıda bağımsız ve aynı şekilde dağılmış rastgele değişkenlerin ortalamasının
 yaklaşık olarak normal bir dağılım gösterdiğini söyler.
 Yani, merkezi limit teoremi, \mu ortalamasına ve \sigma standart sapmasına sahip bir veri
 kümesinden (popülasyondan) yeterince büyük rastgele örnekler alındığında, aynı popülasyondan
 gelen tüm örneklerin (örneklemlerin) ortalamasının popülasyonun ortalamasına yaklaşık olarak eşit
 olacağını belirtir. Özetle, bir veri setinin dağılımı ne şekilde olursa olsun, veri setinden yeterli
 miktarda seçilen örneklerin ortalamaları normal bir dağılıma sahip olacaktır.

 Örneğin, bir ülkedeki insanların ortalama yaşı hakkında bir fikir edinilmek isteniliyor.
 Böyle bir durumda, rastgele 100 kişinin yaşı öğrenilip, ortalaması alındığında 35 çıkıyor.
 Daha sonra rastgele 100 kişinin daha yaşı öğreniliyor ve ortalaması 38 olarak hesaplanıyor.
 Bu şekilde, 100‘er tane örneklerden daha fazla sayıda toplandığında, örneklem dağılımı elde edilmiş olunuyor.
 Örneklem dağılımı, toplanan örneklerin ortalamasının bir dağılımıdır. Merkezi limit teoremi,
 örneklem dağılımının, yani toplanan örneklerin ortalamalarının dağılımının, yaklaşık olarak
 popülasyon ortalamasının etrafında bir çan eğrisi şeklinde dağılacağını söyler ve bu şekilde bir dağılım,
 normal dağılım olarak bilinir. Dikkat edilmesi gereken nokta, merkezi limit teoremi,
 herhangi bir popülasyonun normal dağılıma sahip olacağını değil, örneklem dağılımının normal
 dağılıma sahip olacağını söyler. Alınan örneklerin sayısı sonsuza yaklaştıkça olasılık dağılımı simetrik bir hale gelecektir.

 Merkezi limit teoremi, veriden istatistiksel çıkarım yapmayı sağlar.
 Güven aralığı ve hipotez testi kavramları merkezi limit teoremine dayanmaktadır.
 Geçerli bir örneklem bilgisine sahip olunduğunda popülasyon hakkında doğru varsayımlarda bulunulabilir
 veya tam tersi şekilde popülasyon hakkında bir bilgiye sahip olunduğunda örneklem hakkında doğru
 varsayımlarda bulunulabilir. Hem popülasyon hem de geçerli bir örneklem hakkında bilgi sahibi
 olunduğunda ise örneklemin o popülasyondan alınıp alınmadığı kesin olarak anlaşılabilir.
 İki farklı geçerli örneklem hakkında bilgi sahibi olunduğunda ise iki örneklemin aynı popülasyondan
 alınıp alınmadığı konusunda doğru bir şekilde çıkarım yapılabilir.

 Sampling Error:	Örnekleme hatası bir tür hatadır, seçilen örneklem ilgi popülasyonunu
 mükemmel bir şekilde temsil etmediğinden oluşur.
 Örnekleme Hatası, ilgilenilen popülasyonu temsil etmeyen belirli bir örneklemden kaynaklanan
 istatistiksel bir hatayı gösterir. Basit bir ifadeyle, seçilen numune tüm popülasyonun gerçek özelliklerini,
 niteliklerini veya rakamlarını içermediğinde meydana gelen bir hatadır.

 Örnekleme hatasının arkasındaki ana neden, örnekleyicinin aynı popülasyondan çeşitli
 örnekleme birimleri çizmesidir, ancak birimlerin bireysel farklılıkları olabilir.
 Ayrıca, hatalı numune tasarımı, ünitelerin hatalı şekilde ayrılması, yanlış istatistik seçimi,
 numaralandırıcı tarafından yapılan numune alma ünitesinin uygunluğu için değiştirilmesi de ortaya çıkabilir.
 Bu nedenle, orijinal örnek için gerçek ortalama değer ile popülasyon arasındaki sapma olarak kabul edilir.
 Sectigimiz orneklem(n) ne kadar artarsa ortalamanin standart hatasi o kadar azalir
 -------------------------------------------------------------------

 ---Statistics-4---ders2

 Örneklem sayısı(n) 30 dan büyük olduğu surece populasyon dağılımı ne olursa olsun sample distrubition normale yakınsar.
 Polasyon normal dağılımda ise n değeri ne olursa olsun normale yakınsar
 --------------------
 Ek Not:
 Normal Dağılım
 Normal dağılım, Gauss dağılımı olarak da bilinmektedir.
 Standart normal dağılım bir veri setinde ortalamanın 0,
 varyansın ise 1 olduğunu durumda sağlanmaktadır. Elimizdeki verilerin
 ortalamalarını çizgi grafiği ile gösterecek olursak, grafiğin orta noktasında çizginin yüksek olduğu,
 sağ ve sol kenarlara doğru yüksekliğin azaldığını görebiliriz.
 Normal Dağılım Hangi Amaçla Kullanılır?
 Normal dağılım istatistiksel birtakım
 analizleri yapmadan önce uygulanan ve hangi analizi yapmamıza karar veren yardımcı bir analizdir.
 Örneğin iki farklı (bağımsız) grubun tek ölçüme ait ortalamalarının karşılaştırılması için Independent
 Samples t Test (Bağımsız Örneklem T testi) veya Mann Whitney U testi kullanılabilir.
 Veri setimizdeki veriler normal dağılım gösteriyor ise Independent Samples t Test kullanılır.
 -----------------------------------------

 Pratikte populasyon dağılımını bilmek çok mümkün değildir.Araştırmacı örneklemi seçer
 daha sonra buradan elde ettiği örneklem veriler üzerinden populasyona ilişkin çıkarımda bulunmaya çalışır
 Pratikte örneklem toplanır ve populasyona ilişkin çıkarımda bulunulur
 Veri bilimciler genellikle big datalarla çalıştığı için populasyonu çok düşünmezler hatta eldeki verinin populasyon
 olduğunu varsayarlar

 Sadece ortallama için değil bütün istatistikler için örneklem dağılımı vardır(oran,range,varyans...)
 Pratikte genellikle ortalamanın örneklem dağılımına ihtiyaç duyulur


 CENTRAL LİMİT THEOREM(MERKEZİ LİMİT TEOREMİ)

 Populasyon dağılımı ne olursa olsun örneklem büyüklüğü 30(genel kabul görülen değer) dan büyük
 olursa örneklem dağılımı her türlü populasyona yakınsar.Buna central limit teorem denir
 n arttıkça normal dağılıma yakın dağılım oluşacaktır

 Soru:225 öğrenci bir teste giriyor.Test sonuçlarının ortalaması(mean) 75,standart sapması(standard deviation) 10 ve
 populasyon dağılımı sağdan çarpık dağılım(slightly positively skewed)
 eğer buradan her seferinde 25 öğrenci seçilirse ve ortalamaları tekrar tekrar hesaplanıp bir veri seti oluşturulursa
 oluşacak sampling distribution un ortalaması,standart sapması ve bu dağılımın çarpıklığı ne olur?

 çözüm:
 populsayon dağılımı ile örneklem dağılımın ordalaması aynı olur demiştik.75 olacak
 örneklem dağılımın standart sapması=populasyon dağılımının standart sapması(10)/ √25=2
 Populasyon dağılımı normale yakın olur

 Point and Interval Estimates--NOKTA VE GÜVEN ARALIĞI
               Point estimate
 -------------|-------*-----------|---------
             0.7      0.73       0.8

         İnterval Estimate(Güven Aralığı)
 -------------|----*********--------|---------
             0.7   0.71   0.75        0.8

 Örneklem ortalamasının standart hatası hesaba katılmaz ise bu point estimate olur yani nokta değer verir
 Örneklem ortalamasının standart hatası hesaba katılır ise bir aralık ortaya çıkar bu bizim tahmin aralığımızdır
 Buna güven aralığı denir

 örn bir referandum yapılacak araştırma şirketi araştırdı ve %73 olarak bu referanduma evet çıkacak sonucu çıktı.Bu
 nokta tahmindir standart hatayı hesaba katmaz isek bu değer muhtemelen yanlış çıkacaktır aa bir aralık tahmini yapılırsa
 bi güven aralığı belirtebiliriz örneğin referandum gününde %95 doğrulukta bu oran %71 ile 75 arasında değişecek.\
 İnterval Estimatede hata payı standart hata dan hesaplanır

 Güven aralığı hesaplanırken örneklemin ortalaması point estimate dır


               |---------------------*--------------|
               Lower              Point          Upper
               Confidence         Estimate       Confidence
               Limit                              Limit

 Upper Confidence Error=Point Estimate+Margin Of Error(moe)
 Lower Confidence Error=Point Estimate-Margin Of Error(moe)
 Alt limit ile üst limit arasındaki farka güven aralığının genişliği denir(Widht of confidence interval)=2*moe

 Confidence level(Güven Seviyesi)=1-α or 100(1-a)%
 α:Hesaplanılan güven aralığının gerçek parametreyi kaçırma olasılığıdır

 ---------------------------------------------------------------------------------------------

 ---Statistics-4---ders3

 Confidence Interval = ( x̄ – z * ơ / √n) to ( x̄ + z * ơ / √n)
 formulun (z * ơ / √n) kısmına hata marjı denir alt limitin ve üst limitin bulunması için
 ortalamaya eklenir ve çıkartılır
 Confidence Interval = x̄ ± z * ơ / √n
 x̄: Sample Mean
 z: Confidence Coefficient
 ơ: Population Standard Deviation
 n: Sample Size

 Level of Confidence     α/2       z
      (1-α)
      .90                .05      1.645
      .95                .025     1.96
      .99                .005     2.58

 güven seviyesi arttıkça z çarpanının arttığını görüyoruz.Yani ne kadar fazla güvenilirlik istenirse
 hata da o oranda artacaktır yani alt limit ve üst limit genişleyecektir,çok fazla geniş güven aralığı
 istenmez asıl istenen olabildiğince dar bir güven aralığıdır
 Güven aralığında kontrol edebileceğimiz faktör sample size(n) dır


 örnek:Normal nağılımdan 2,3,5,6,9 olarak bir sample(örneklem alındı)
çözüm:
 x̄=(2+3+5+6+9)/5=5
 ơ=2.5
 σx=ơ / √n=2.5/√5=1.118

 güven aralığı formulunu hatırlayalım
 Confidence Interval = (x̄ – z * ơ / √n) to(x̄ + z * ơ / √n)
 lower limit=5-(1.96)(1.118)=2.81  z(confidence multiplier) güven çarpanı 1.96 alındı çünkü %95 güven aralığı için işlem yaptık
 yukarıdaki tablodan tekrar bakılabilir
 upper limit=5+(1.96)(1.118)=7.19
 CL=[2.81,7.19] güven aralığı
# Oluşturacağımız 100 güven aralığının 95 i doğru populasyon parametresini yakalayabilir


 örnek:Bir bilgisayar şirketinin aylık satış sayıları var ve elimizde 25 aylık veri var.geçmiş satışlardan satış sayılarının
 standart sapmasının 75 olduğunu biliyoruz.bu örneklem ortalaasının etrafına %95 lik bir güven aralığı oluşturmamız
 isteniyor

                 235 374 309 499 253
                 421 361 514 462 369
                 394 439 348 344 330
                 261 374 302 466 535
                 386 316 296 332 334

 çözüm:
 x̄=370.16(örneklem toplamları/25)
 z=1.96 (tekrar %95 güven aralığı için işle yapacaz,üstteki tablo) z değeri critical value olarak ta geçebilir
 Confidence Interval = (x̄ – z * ơ / √n) to(x̄ + z * ơ / √n)=
 lower limit=370.16-(1.96)*75/√25 =370.16-29.40
 upper limit=370.16+(1.96)*75/√25 =370.16+29.40

 örnek:n=25 olan test scorunun ortalaması 38 ve populasyon standart sapması 6.5 tir

 not:populasyon standart sapması biliniyorsa kesinlikle z dağılım kullanılacaktır,bilinmiyorsa
 örneklemden standart sapma hesaplanacak ve t dağılımı kullanılacak

 n=25
 x̄=38
 ơ=6.5

 Confidence Interval = (x̄ – z * ơ / √n) to(x̄ + z * ơ / √n)
 lower limit=38-1.96*6.5/ √25=35.45
 upper limit=38+1.96*6.5/ √25=40.55
 CL = [35.45,40.55]


 !!Eğer populasyon standart sapması bilmiyor ise güven aralığı ve hipotez testlerinde t dağılımı kullanılır
 Serbestlik derecesi 30 olan t dağılımı normal dağılım olmuş olarak değerlendirilir
 degrees of Freedom(Serbestlik derecesi df)=sample size-1

 t = (x̄ – μ) / (s/√n)
 s is the standard deviation. n is the size of the given sample."""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Confidence Intervals Using the Normal Distribution

sns.get_dataset_names()
tips = sns.load_dataset('tips')
tips.head()

tips.describe().T
# Hangi gün ortalama daha fazla hesap ödeniyor?
sns.barplot(x='day', y='total_bill', data=tips, ci = 95) #ci:güven aralığı( Confidence Interval)
#genelde pazar günü daha fazla hesap ödeniyor

# Cuma günleri ödenen hesap için güven aralığı?
tipsFri=tips[tips['day']=='Fri']
tipsFri.head()
x_bar=tipsFri.total_bill.mean()
x_bar
tipsFri.shape #shape(19,7) geldi yani örneklem sayısı 19 
std_error = tipsFri.total_bill.sem() #standard error of the mean(Ortalamanın standart sapması)
std_error

moe = 1.96 * std_error  #(z * ơ / √n)

lower = x_bar - moe
lower  # 13.41
upper = x_bar + moe
upper  # 20.88

# Scipy ile yapalım
stats.norm.interval(0.95, loc=x_bar, scale = std_error)

# t dağılımı ile yapalım

"""populasyon standart sapması bilinmediği için ve örneklem sayısı 30 dan 
küçük olduğundan t  dağılımı kullanmak daha doğrudur"""
stats.t.interval(0.95, df=len(tipsFri)-1, loc=tipsFri.total_bill.mean(), 
                 scale= tipsFri.total_bill.sem())
# degrees of Freedom(Serbestlik derecesi df)=sample size-1
# t ve z istatistiği hesabı
stats.t.ppf(0.975,75)
stats.t.ppf(0.025,75)
stats.norm.ppf(0.975)
"""güven aralığı hesabı yaparken populasyonun standart sapmasını bilmemiz çok 
mümkün olmayacağı için çoğunlukla t dağılımı kullanılır"""


#Sunday için güven aralığını bulunuz
tipsSun=tips[tips['day']=="Sun"]
tipsSun.shape  
"""76/7 örneklem 76 noralmade populasyonun standart sapmasını bilmediğimiz
 için direk olarak t dağılım kullanmamız gerekiyor
fakat örneklem sayısı 30 büyük olduğundan z dağılım kullanmakta bize yakın 
değerler getirecektir"""
stats.t.interval(0.95, df=len(tipsSun)-1, loc=tipsSun.total_bill.mean(), 
                 scale= tipsSun.total_bill.sem())

stats.norm.ppf(0.975)#%yüzde 95 güven aralığı için z değerini bulmak ile istersek


#------------------------------------------------------------------------------


"""---Statistics-5---ders1

Steps for Performing a Siginificance test(Anlamlilik(Hipotez) testlerinin adimlari)

*Orneklem istatistiklerini kullanarak populasyon parametlerine yonelik 
tahminlerde bulunulmaya calisilir
*Onceki derste guven araligini kullanarak populasyon ortalamasi buldugumuz iki aralik
arasindadir diyebildik
*inferential statistics denildiginde guven araligi ve hipotez testleri akla gelir
*Hem guven araligini kullanarak hem hipotez testleri ile populasyona ait cikarimlarda
bulunulabilir

Once elimizde bir arastima sorusu olmasi gerekiyor ornegin biz bir gruba diyet 
uyguluyorsak diyet oncesi ve diyet sonrasi kilolari aliyoruz ve diyoruz ki diyet
sonrasi kiloda azalma oldu mu yani uyguladigimiz diyet karsi taraftaki bireylere
etkili oldu mu.
Bu sorudan sonra hipotezler olusturulur,hipotezler olusturulduktan sonra hangi
testin kullanilacagina karar verilip daha sonra hipotez testlerinin adimlari
sergilenir 

ornegin 20 kisilik bir obez gruba diyet programi uyguluyoruz,grubun kilolarini
programdan once olcuyoruz bide programdan sonra olcuyoruz
Burda hipotezimizi soyle kurariz,sifir hipotezi diyet programinin kisilerin
kilo ortalamasi uzerinde etkisi olmadigi,alternatif hipotezde de deriz ki diyet
programinin kisilerin kilo vermesinde etkisi oldugu daha sonra kullanilacak  
teste karar verilir(ornk t test)

Hypothesis(hipotez):Populasyon parametresi hakkinda bir iddada bulunmak,buna
iliskin bir cumle yazmaktir
Hipotez testlerinin ilk asamasi varsayimlardir,daha sonra diğer asamalar gelir
Populasyan parametreleri oran(proportion) ve ortalama(mean) olabilir.Biz 
ortalama uzerinde ilerleyecez

Hipotez testinin 5 adimi:
    *Assumptions (varsayimlar)
    *Hypotheses(hipotezler)
    *Test Statistic
    *P-Value
    *Conclusion(sonuc)--iki durum ortaya cikar ya 0 hopatezi red edilir yada edilemez
    
    
Step 1:Assumptions (varsayimlar)
Her hipotez testin bir varsayimi vardir,orn z test varsayimlarina bakalim
*Butun orneklemlerin random olarak secilmesi
*Butun gozlemler birbirinden bagimsiz
*Populasyon standart sapmasi biliniyor yada en az 30 gozlemin olmasi 

Step 2:Hypotheses(hipotezler)
Iki hipotezden olusur
*Null Hypothesis:Populasyon paranetresinin herhangi bir degeri alabilecegine 
dair bir durum
*Alternative Hypothesis:Sifir hipotezisin tamamen tersine kurulmus bir durum
Tek kuyruk,cift kuyruk ilerleyen derslerde anlatilacak

ornegin ulkedeki vatandaslarin gelir ortalamasi 2000 $ diye bir sifir hipotezi
ortaya konulduysa,alternatif hipotez iki turlu kurulabilir ya mean!=2000$ cift 
kuruk yani yon gostermeden kurulabilir yada yon gosterilir mean<2000$ tek kuyruk

*Sifir hipotezi H0 ile gosterilir.Baslangicta dogru kabul edilen iddadir.Yapilacak
test ile bu idda red edilmeye calisilir
*Alternatif hipotez Ha ile gosterilir tamamen sifir hipotezinin tersine kurulmus cumledir

Ornek:Bir mahkemede mahkeme karsinda sanik her zaman masumdur(Sifir Hipotezi Ho)
Arastirmaci olan savci ortaya alternatif bir idda atar sanigin suclu oldugunu iddia eder,
savci veri toplar juri de test yapar,eger yeteri kadar kanit bulunursa sifir hipotezi 
red edilir,alternatif hipotez kabul edilir.Savci yeterince kanit toplayamazsa sifir 
hipotezi red edilemez

Step 3:Test Statistic
*populasyon standart sapmasi biliniyor ise z test yapilir
*populasyon standart sapmasi bilinmiyor ise t test yapilir
*populasyon standart sapmasi bilimiyor fakat n 30 dan buyukse t ve z yapilabilir

Step 4:P-Value
P değeri sıfır hipotez testi bağlamında istatistiksel anlamlılığı ölçmek için kullanılır. 
Sıfır hipotez testi reductio ad absurdum(saçmalığa indirgeme)
argümanının istatistiğe uygulanmasıdır.
Özetle, bir savın karşıtının mümkün olmadığını gösterilirse, 
o savın geçerli olduğu kabul edilir.

P değeri, gözlemlenen sonuçların aslında test edilmek istenen durumla hiçbir
alakası olmamasının olasılığıdır. Farklı bir deyişle, modelin (sıfır hipotezi)
doğru olduğu kabul edilirse, p değeri test edilen değere eşit ya da aşırı
değerler elde etme olasılığıdır

P value α(anlamlilik seviyesi) dan kucuk olursa yeterince guclu kanit olusur,buyuk olursa sifir
hipotezi red edilemez
a genellikle 0.05 olarak alinir
P value kucuk olursa kanit buyuk oluyor 

Step 5:Conclusion(sonuc)
Sample dan yola cikilarak P value hesaplandi 
Bide elimizde α seviyesi var
P value α dan kucuk olursa degerimiz anlamli olur ve sifir hipotezi red edilir
P value α dan buyuk olursa degerimiz anlamli olmaz ve sifir hipotezi red edilemez """

"""---Statistics-5---ders2

Significance Level(Anlamlılık Seviyesi)
*P value yu karlşılaştıracağıız değerdir
*Genelde 0.05 olarak alınır 
*P value significance level den kucuk olursa degerimiz anlamli olur ve sifir hipotezi red edilir

Type 1 Error 
Örnek:Sıfır hipotezi erkek hamile değil,alternatif hipotez de erkek hamile
ama buna rağmen sıfır hipatezi red ediyor ve gerçekte olmayacak bir hata yapıyor
*Sıfır hipotezi doğru olduğunda hipotezin red edilmesi

Type 2 Error
Örnek: Sıfır hipotezi bayan hamile değil alternatif hipotez bayan hamile 
daha sonra test uyguluyorsunuz fakat kadın hamile olduğu halde hamile değil 
diyorsunuz hipotezi red edemiyorsun 
*Sıfır hipotezini red etmek gerekirken red edilemediği durum

note:type 1 error genelde daha ciddi bir problem olarak değerlendirilir

                              Hipotez Testi Sonucundaki Karar
                           H0 red                 H0 reddedilemez

                   H0     Yanlış Karar              Doğru karar
                 doğru  Tip I hata (α)                (1- α)
Gerçek 
Durum      
                 H0      Doğru Karar               Yanlış Karar
                yanlış  (Testin Gücü)             Tip II hata (β)
                           1-β  

One tail and two tail statistical test(tek ve çift kuyruk istatistik test):
Alternatif hipotezi nasıl kurduğumuzla alakalıdır.
Alternatif hipotezi eşit değildir şeklinde yön belirtmeden kurarsak two tails olur
Eğer büyüktür küçüktür şeklinde kuruluyorsa one tail olur 

z = (x – μ) / (σ / √n)

Large Sampe-Example:
bir sahilde yüzülebilmesi için sudaki kabuledilebilir kurşun miktarı 10.0 parts/million dur.
populasyon standart sapması biliniyor(μ,σ=1.5)
Belediye sahilden suyu alark test ediyor,40 su örneği alınmış ve test istatistiği hesaplanmış
sample mean=10.5 yani kabul edilebilir kurşun miktarı bu çıktı
α=0.05

buna z testi yapacaz(populasyon standart sapmasını biliyoruz)
Hypotheses:Başlangıçta kabul edilen değer μ=10,aleternatif hipotezde μ>10 olduğu 
idda edilecek(> kullanıldığı için tek kuyruk olduğunu anlayacaz)

Hatıtlarma
***Confidence Interval = ( x̄ – z * ơ / √n) to ( x̄ + z * ơ / √n)
formulun (z * ơ / √n) kısmına hata marjı denir alt limitin ve üst limitin bulunması için
ortalamaya eklenir ve çıkartılır
Confidence Interval = x̄ ± z * ơ / √n
x̄: Sample Mean
z: Confidence Coefficient
ơ: Population Standard Deviation
n: Sample Size  ***

x̄=10.5

z = (x – μ) / (σ / √n)=(10.5-10)/(1.5/√40)=2.1

z test istatistiğine göre p value tablodan =0.0179 geldi
p<α larak çıktı yani sıfır hipotezini reddedebiliriz,sahildeki kurşun miktarı kabul 
edilenden daha fazla çıkmış oldu """

"""---Statistics-5---ders3

Örnek:Bir mağaza menejeri yeni bir faturalandırma sisteminin cost effective olup
olmadığını ölçmek istiyor.Eğer aylık ortalama hesap 170 dolardan büyük olursa cost 
effective olarak değerlendirliyor faturalandırma sistemi,400 tane aylık hesap 
seçilmiş ve bunun ortalamasını 178$ olduğu hesaplanmış,populasyon standart 
sapması 65$ olarak verilmiş.
Yeni faturalandırma sistemi cost effective mi?

çözüm:
z testi kullanılabilir çünkü populasyon standart sapmasını(ơ=65) biliyoruz ve
örneklem sayısı(n=400) 30 dan büyük.

z = (x – μ) / (σ / √n)=(178-170)(65/√400)=8/3.25=2.46

The null hypothesis(sıfır hipotezi)=Ho:μ=170
The alternative hypothesis Ha:μ>170

import scipy.stats as stats
1-stats.norm.cdf(2.46)

P-value=0.0069(2.46 değerinin karşılık gediği p value değeri yukarıdaki kod ile
               bulduk)
Alternatif Hipotez Ha:μ>170 di.(yani tek kuyruk)

P-value(0.0069)<α(0.05) yani sıfır hipotezi red edilecek.Faturalandırma sisteminin 
cost effective olduğunu diyebiliriz(Reject the null)



Örnek:Bon Air ELEM okulunda 1000 öğrenci var.Müdür öğrencilerin IQ skor
ortalamalarının en az 110 olduğunu düşünüyor.Bunu da kanıtlamak için rastgele
20 tane öğrenci seçmiş.Bu öğrencilerin IQ ortalamasını 108 ve standart sapmasını
10 bulmuş.Buna dayanarak müdür kendi orjinal hipotezini kanul mü yoksa red mi 
etmeli?(α=0.01 verilmiş)

Çözüm:
    
t testi kullanacaz.Çünkü populasyon standart sapmasını bilmiyorum ve örneklem 
sayısı 30 dan küçük

The null hypothesis(sıfır hipotezi)=Ho:μ=110
The alternative hypothesis Ha:μ<110


t = (x – μ) / (σ / √n)=(108-110)(10/√20)=-0.894

t=-0.894

(-0.894 ün karşılık geldiği p değerine bakacaz)
import scipy.stats as stats
stats.t.cdf(-0.894,19)

P-Value=0.1913 geldi
yani P>a dan sıfır hipotezi red edilemez(fail to reject the null).
Müdür orjinal hipotezini kabul etmelidir"""

#---
"""Örnek:bir sahilde yüzülebilmesi için sudaki kabuledilebilir kurşun
miktarı 10.0 parts/million dur.
populasyon standart sapması biliniyor(μ,σ=1.5)
Belediye sahilden suyu alark test ediyor,40 su örneği alınmış ve
test istatistiği hesaplanmış
sample mean=10.5 yani kabul edilebilir kurşun miktarı bu çıktı
α=0.05  (Yukarıda çözmüştük şimdi python ile çözecez)"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

xbar=10.5
sigma=1.5
n=40
mu=10

#Ho:mu=10
#Ha:mu>10 yani mu 10 dan büyükse sahil kapatılacak 

#Test Statistict
z=(xbar-mu)/(sigma/np.sqrt(n))
#z=2.108 çıktı

"""p-Value (tablodan da bakılabilir python ilede hesaplanabilir.
2.108 in karşılık geldiği değere bakacaz)"""

p=1-stats.norm.cdf(z) #tek kuruk olduğu için bu şekil yazıldı
p

#p 0.017 geldi

"""z test istatistiğine göre p value tablodan =0.0179 geldi
p<α larak çıktı yani sıfır hipotezini reddedebiliriz,sahildeki kurşun miktarı kabul 
edilenden daha fazla çıkmış oldu""" 

#---

sns.get_dataset_names()
df=sns.load_dataset("mpg")
df

df[df["origin"]=="usa"].describe()

"""usa orijinli arabaların horsepower nın 110 eşit olup olmadığı H0:μ=110 yada
HA:μ>110 durumlarına bakacaz"""

#scipy.stats.ttest_1samp(a, popmean, axis=0, nan_policy='propagate', alternative='two-sided')

stats.ttest_1samp(df[df["origin"]=="usa"]["horsepower"],110,alternative="greater")

#Ttest_1sampResult(statistic=nan, pvalue=nan) ---null değerler olduğu için nan çıktı
stats.ttest_1samp(df[df["origin"]=="usa"]["horsepower"].dropna(),110,alternative="greater")
#out:test_1sampResult(statistic=3.550044602017898, pvalue=0.0002310035889540432)

"""p value değeri çok küçük geldi.yani amerika originli arabaların beygir güçleri 
anlamlı olarak 110 dan büyük sonucu aldık.H0 red edilir(p-value<α)"""



"""usa orijinli arabaların mpg lerinin H0:μ=22 yada
HA:μ<22 durumlarına bakacaz"""
stats.ttest_1samp(df[df["origin"]=="usa"]["mpg"],22,alternative="less")

#Ttest_1sampResult(statistic=-4.723072192881628, pvalue=1.9455026028456406e-06)
#pvalue=1.9455026028456406e-06(1.89*10^-6 yani sıfıra çok yakın bir değer olacak)
#H0 hipotezi red edilir 


"""Origin i avrupa olan arabaların beygir güclerinin H0:μ=100 yada
HA:μ>100 durumlarına bakacaz"""

stats.ttest_1samp(df[df["origin"]=="europe"]["horsepower"].dropna(),100,alternative="greater")

#Out: Ttest_1sampResult(statistic=-7.953024725516988, pvalue=0.9999999999853763)

"""p value değeri 1 e çok yakın H0 hipotezi red edilemez """


"""origini avrupa olan arabaların ağırlıkları 3000 midir değil midir.
H0:μ=3000,Ha:μ!=3000 """


df.columns
stats.ttest_1samp(df[df["origin"]=="europe"]["weight"],3000)
"""Ttest_1sampResult(statistic=-9.84610838848352, pvalue=8.80766713530181e-15)
P-value sıfıra çok yakın bir değer olarak geldi H0 red edilir"""

#----------------------------------------------------------------------------
#Statistics Lab2

import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('http://jse.amstat.org/datasets/normtemp.dat.txt',
   delim_whitespace=True, names=["temperature", "gender", "heart_rate"])

df.head()
"""Out[57]: 
   temperature  gender  heart_rate
0         96.3       1          70
1         96.7       1          71
2         96.9       1          74
3         97.0       1          80
4         97.1       1          73"""

df.info()
df["gender"] = df["gender"].replace(to_replace=[1,2], value=["male", "female"])
df

#Task-1. Is the body temperature population mean 98.6 degrees F?
#yukarıdaki soru için güven aralığına yada hipotez testine bakılabilir
df.temperature.mean() #*What is the mean for body temperature?
# ortalama 98.24923076923076  

#What is the standard deviation for body temperature?
df.temperature.std()
#0.7331831580389456

#What is the standard error of the  mean for body temperature?
#standart error=populasyon standart sapmasi(σ)/√n
df.temperature.std() / np.sqrt(df.shape[0]) #formul üzerinden heaplama
#0.06430441683789102
df.temperature.sem()#Bu da bize direk standart error u verir
#0.06430441683789102
stats.sem(df.temperature)#Bu da bize direk standart error u verir
#0.06430441683789102

#Plot the distribution of body temperature.You can either use Pandas or Seaborn.
df.temperature.plot.density()

sns.distplot(df["temperature"], kde=True, hist=True, bins=10);

"""Key Notes about Confidence Intervals

💡A point estimate is a single number.

💡A confidence interval, naturally, is an interval.

💡Confidence intervals are the typical way to present 
estimates as an interval range.

💡The point estimate is located exactly in the middle of the confidence interval.

💡However, confidence intervals provide much more information
 and are preferred when making inferences.

💡The more data you have, the less variable a sample estimate will be.

💡The lower the level of confidence you can tolerate, the narrower the 
confidence interval will be.

⭐Investigate the given task by calculating the confidence interval for 
this sample of 130 subjects. (Use 90%, 95% and 99% CIs) """

#95% Confidence Interval
#interval(alpha, df, loc=0, scale=1)
stats.t.interval(alpha=0.95, 
                 df=len(df)-1, 
                 loc=df.temperature.mean(), 
                 scale=df.temperature.sem())
"""Out: (98.12200290560803, 98.3764586328535) populasyon ortalaması ½95 güvenilirlik
ile bu aralıktadır
Bize 98.6 soruldu yani güven aralığının dışında kaldı Dolayısı ile sıfır 
hipotezini red etmiş oluyoruz"""

"""Yukarıda t testi ile yaptık fakat örnekle sayısı 30 dan büyük olduğu için
istersek z testi ni de kullanabiliriz."""
#95% Confidence Interval
#95% Confidence Interval
stats.norm.interval(alpha=0.95, 
                    loc=df.temperature.mean(), 
                    scale=df.temperature.sem())

#Out:(98.12319642818164, 98.37526511027988)

#95% Confidence Interval
stats.t.interval(alpha=0.95, 
                 df=99999999999999, 
                 loc=df.temperature.mean(), 
                 scale=df.temperature.sem())

#Out:(98.12319642818164, 98.37526511027988)
"""t testinde  degrees of Freedom(Serbestlik derecesi df) sonsuza
 gittikçe normal dağılıma yaklaşır.Üstteki sonuçla aynısı geldi"""

df.temperature.sem() #standart error 
#0.06430441683789102

lower = []
upper = []

for i in [0.90, 0.95, 0.99]:
    ci = stats.t.interval(i, len(df.temperature)-1, loc=df.temperature.mean(),
                          scale=df.temperature.sem())
    lower.append(ci[0])
    upper.append(ci[1])
    print("CI {i}%: {interval}".format(i=int(i*100), interval=ci))
    
"""
out:
CI 90%: (98.14269432413488, 98.35576721432665)
CI 95%: (98.12200290560803, 98.3764586328535)
CI 99%: (98.08110824239758, 98.41735329606395)
"""
plt.plot((lower,upper), (range(len(lower)),range(len(upper))), 'ro-',color='red')
plt.yticks(range(3),["CI 90%","CI 95%","CI 99%"]);

"""
One Sample t Test
⭐Investigate the given task by using One Sample t Test.

Key Notes about Hypothesis Testing (Significance Testing)

💡Assumptions(varsayımlar)

💡Null and Alternative Hypothesis

💡Test Statistic

💡P-value

💡Conclusion

___🚀First, check the normality. *Use scipy.stats.shapiro

H0: "the variable is normally distributed"
H1: "the variable is not normally distributed"

"""
stat, p = stats.shapiro(df.temperature) 
"""shapiro normalliği kontol etmek için kullanılır,yukarıda görsel olarak 
kontrol etmiştik"""
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Sample looks Gaussian (fail to reject H0)')
else:
	print('Sample does not look Gaussian (reject H0)')

"""out:
Statistics=0.987, p=0.233
Sample looks Gaussian (fail to reject H0)
Ho red edilemedi yani normal dağılmış"""

"""
H0: mu = 98.6

H1: mu != 98.6

___🚀Then, conduct the significance test. Use scipy.stats.ttest_1samp"""
oneSamp = stats.ttest_1samp(df.temperature, popmean=98.6)#
oneSamp
#Ttest_1sampResult(statistic=-5.454823292364077, pvalue=2.410632041561008e-07)
#p value sıfıra çok yakın Ho red edilir (p<α)

alpha = 0.05

if oneSamp.pvalue < alpha:
    print("Reject the null hypothesis")
else:
    print("fail to reject the null hypothesis")
#Reject the null hypothesis



#******************************************************************


#---Statistics-6---ders1

"""
İndependent Samples Test (Bağımsız Grup T testi)
*Bağımsız grup t testi (Independent Samples t Test) her bir alt gözenek 
(örneğin kız ve erkek grupları) normal dağılım özelliği gösterdiğinde 
(N1>30; N2>30) iki aritmetik ortalama arasındaki farkın manidarlığını
 test etmede kullanılan parametrik bir tekniktir.
 
*ilaç alan alamayan,vatandaş olan vatandaş olmayan...vb birçok örnek verilebilir. 

İlk yıl mezunlarının maaşları cinsiyet açısından farklılık gösteriyor mu?
salary gender
$35000  Male
$45000  Male
$38000  Female
$50000  Female
$28000  Male

Ho:μ(M)=μ(F)
h1:μ(M)!=μ(F)
Ho da erkek grubu ile kadın grubunun maaş ortalamaları birbirine eşittir diyecez
h1 alternatif hipotezde de ortalamalar eşit değildir diyecez

Hipotez adımlarına tekrar bakalım:
    
*Assumptions (varsayimlar)
*Hypotheses(hipotezler)
*Test Statistic
*P-Value
*Conclusion(sonuc)

*Assumptions (varsayimlar):
 -bir tane kategorik değişken olacak
 -bir tane sayısal değişken olacak 
 -Kategorik değişkenin iki seviyesi olacak
 -Her iki grubun sayısal değişkeninin normal dağılıma yaklaşık olduğu varsayılır

*Hypotheses(hipotezler)
Ho:μ(M)=μ(F)
h1:μ(M)!=μ(F)
Ho da erkek grubu ile kadın grubunun maaş ortalamaları birbirine eşittir diyecez
h1 alternatif hipotezde de ortalamalar eşit değildir diyecez

*Test Statistic
Bağımsız örneklemler t testinde 2 durum var,iki grubun varyanslarının eşit 
olup olmama durumu 


varyansların eşit olma durumu(Equal Variances Assumed)

t=(x̄1-x̄2)/sp√((1/n1)+(1/n2))

sp=√((n1-1)s1^2+(n2-1)s2^2)/(n1+n2-1)

df=n1+n2-2

x̄1 = Mean of first sample
x̄2 = Mean of second sample
n1 = Sample size (i.e., number of observations) of first sample
n2 = Sample size (i.e., number of observations) of second sample
s1 = Standard deviation of first sample
s2 = Standard deviation of second sample
sp = Pooled standard deviation


varyansların eşit olmama durumu(Equal Variances Not Assumed)

t=(x̄1-x̄2)/√((s1^2/n1)+(s2^2/n2))

df(degrees of Freedom) var formul çok uzun 


örnek:
    
Body Temperatures(F)
Men    Women
96.4   97.8
97.4   98.0
97.5   98.2
97.8   98.2
97.8   98.2
97.9   98.6
98.0   98.8
98.6   99.2
98.8   99.4

*Normal conditions u çek etme diyor yani normal olduğu varsayılacak.
*Erkeklerle kadınların vucüt sıcklarıkları ortalamada birbirine eşit mi değil mi?
*Cinsiyet açısından ortalamalar değişiyor mu bunun için yeterince kanıt var mı?

*Assumptions (varsayimlar):
-kaegorik değişkenin iki seviyesi var
-örneklelerim birbirinden bağımsız
-her grup normal dağıldı(bunu kendisi verdi)

*Hypotheses(hipotezler)
Ho:μ(M)=μ(F)
h1:μ(M)!=μ(F)
Ho da erkek grubu ile kadın grubunun  ortalamaları birbirine eşittir diyecez
h1 alternatif hipotezde de ortalamalar eşit değildir diyecez

*Test Statistic
Bu teste iki grubunda vücüt sıcaklık dağılımlarının varyanslarının eşit olduğu
varsayımı üzerine test yapıldı

formul:
    t=(x̄1-x̄2)/sp√((1/n1)+(1/n2))

    sp=√((n1-1)s1^2+(n2-1)s2^2)/(n1+n2-1)

    df=n1+n2-2

    x̄1 = Mean of first sample
    x̄2 = Mean of second sample
    n1 = Sample size (i.e., number of observations) of first sample
    n2 = Sample size (i.e., number of observations) of second sample
    s1 = Standard deviation of first sample
    s2 = Standard deviation of second sample
    sp = Pooled standard deviation


n1=9  -gruplar eşit verilmiş fakat eşit verilmeyebilirdi 
n2=9
s1=0.5833
s2=0.5487

sp=0.5663 formulden geliyor 

x̄1=97.856

t=-2.371
df=9+9-2=16 

*df i 16 olan bir t dağılımını kullanarak p value hesabı yapılacak.

p-value hesabı

import scipy.stats as stats
2*stats.t.cdf(-2.371,16)
#Out: 0.030634485990952903
P-value=0.0306

p<a Ho hipotezi red edilecek(Reject the Null)
"""


"""#---Statistics-6---ders2

Örnek:
Bir boya ürün geliştiricisi iki boya formulü ile ilgileniyor,
formul 1 standart kimya ile kullanılıyor,
formul 2 nin ise içerisinde yeni bir içerik var
Eski tecrübelere dayanarak 2 formulünde kuruma zamanının standart sapması 8 dk verildi
Yeni içerik kuruma zamanını etkilememiş(Equal Variances)
İki formulden de 10 tane örnek alındı
Sonra formul 1 in kuruma zamanı x̄1=121 bulunmuş
formul 2 nin kuruma zamanı x̄2=112 bulunmuş

Yeni maddenin kuruma zamanında bir etkisi olmuş mu??(a=0.05)

çözüm:

s1,s2=8
n1,n2=10
x̄1=121
x̄2=112
a=0.05


*Assumptions (varsayimlar):
-populasyon standart sapması verildiği için z testi kullanılabilir
-örneklelerim birbirinden bağımsız
-her grup normal dağıldı(bunu kendisi verdi)

**Hypotheses(hipotezler)
Ho:μ1=μ2
ha:μ1>μ2  (tek kuyruk)

*Test Statistic

z=(x̄1-x̄2)/√((s1^2/n1)+(s2^2/n2))

z=2.52 çıktı,x1,x2,s1,s2,n1,n2 yi biliyoruz

p-value hesabı

import scipy.stats as stats
1-stats.norm.cdf(2.52)

Out: 0.005867741715332553
p<a Ho hipotezi red edilecek(Reject the Null)

Yeni madde eklemek kuruma zamanını azaltır



Hypothesis Test:Dependent T test (Bağımlı örneklem t-testi)

Bağımlı örneklem t-testi, bir değişkenin, iki farklı durumda gözlemlenen
değerlerinin ortalamalarını karşılaştırır. Bu iki durum genellikle uygulanacak
bir yöntemin öncesi ve sonrası şeklinde olur. 

*Aynı gözlem üzerinden iki farklı ölçüm vardır

önek:6 haftalık sigara bırakma programının öncesi ve sonrası verilerinde farklılık var mı
ID ÖNCE  SONRA FARK  (Günlük sigara içme miktarları incelenmiş )
1   12     10   2
2   18     7    11
3   23     22   1
4   10     12  -2
5   8      4    4

Aynı Id ler incelenmiş yani dependent(bağımlı) data

*Assumptions (varsayimlar):
-Aynı sample birbirinden farklı zamanda incelenmiş(program öncesi ve sonrası)
-örneklerim birbiriyle bağımlı
-sonuçlar arasındaki fark normal dağıldı(bunu kendisi verdi)

*Hypotheses(hipotezler)
Ho:μ(D)=0  farkların ortalması sıfır yani program etki göstermemiştir
Ha:μ(D)!=0 program etki göstermiştir 


*Test Statistic
t=(x̄diff-0)/sx̄
sx̄=Sdiff/√n

x̄diff:Sample mean of the differences
n=Sample size
sdiff=Sample standart deviation of the differences
sx̄=Estimated standart error of the mean(s/sqrt(n))

---------------------------------------
Örnek:
9 adet çelik levha giriş var.2 farklı metod ile kesme mukavemetleri ölçülmüş.
Kesme mukavemet ortalamaları arasında fark var mı yok mu?(a=0.05)

girder      Method1         Method2   Difference dj
S1/1        1.186            1.061         0.125
S2/1        1.151            0.992         0.159
S3/1        1.322            1.063         0.259
S4/1        1.339            1.062         0.277
S5/1        1.2              1.065         0.135
S2/1        1.402            1.178         0.224
S2/2        1.365            1.037         0.328
S2/3        1.537            1.086         0.451
S2/4        1.559            1.052         0.507

*Assumptions (varsayimlar):
-Aynı sample birbirinden farklı zamanda incelenmiş(program öncesi ve sonrası)
-örneklerim birbiriyle bağımlı
-Her iki method yaklaşık olarak normal dağıldı(bunu kendisi verdi)


*Hypotheses(hipotezler)
Ho:μ(D)=0 
Ha:μ(D)!=0 

*Test Statistic
t=(x̄diff-0)/sx̄
sx̄=Sdiff/√n

x̄diff=0.2769  
sdiff=0.1350
n=9

t=0.2769/(0.1350/√9)=6.15
df=9-1=8

P-Value 

import scipy.stats as stats
2*(1-stats.t.cdf(6.15,8))

 p-value=0.00027399606897193785
 
p<a Sıfır hipotezi red edilir(Reject the null)
method 1 method 2 e göre daha yüksek kesme mukavemet değerleri ortaya koyuyor 


-------------------------------------------"""
"""#---Statistics-6---ders3

One-way ANOVA(Tek yönlü varyans analizi )

Tek yönlü varyans analizi (ANOVA) normal dağılımlı bir seride üç ve daha 
fazla bağımsız ortalama arasındaki farkın manidarlığının hesaplanmasında kullanılır. 
ANOVA tek başına üç veya daha fazla grubun aritmetik ortalamalarını kümülatif
olarak karşılaştırır; bu karşılaştırmalardan en az birisi anlamlı olduğunda 
ANOVA sonucu da anlamlı bulunur. Bu durumda hipotezler;

H0: Ortalamalar arasında fark yoktur.
H1: En az iki ortalama arasında anlamlı bir farklılık vardır.


Örnek:Kişilerin sprint zamanları ölçülüyor
0:sigara içmeyenler 
1:eskiden sigara içenler
2:hala sigara içenler

Sprint Smoking
5.1      0
7.8      2
7.1      1
8.6      2
4.9      0
7.7      1

3 bagimsiz grup var 0,1,2.one-way anova analizi yapilacak.Bunlarin sprit 
ortalama zamanlari arasinda anlamli fark var mi ona bakacaz
-Python ile devam edecez 

*Assumptions (varsayimlar):
Bagimli degiskenin sayisal olmasi 
Bagimsiz degiskenin kategorik olmasi 
Kategorik degisken 3 yada daha fazla gruptan olusmasi 
Bagimli degiskenin normal dagilmasi
Varyanslarin homojenligi

*Hypotheses(hipotezler)
Ho:*Hypotheses(hipotezler)
Ho:μ1=μ2=μ3=...=μk   Butun gruplarin ortalamaliri birbirine esittir
Ha:En az bir μ digerlerinden farkli 

*Test Statistic

ANOVA table	
Source	      SS	       DF	        MS	         F
Treatments	  SSR	       k−1	     SSR/(k−1)	 MSR/MSE
Error	      SSE	       N−k	     SSE/(N−k)
Total     SST=SSR+SSE	   N−1

SSR:regression sum of squares
k-1:model degrees of Freedom
MSR:regression mean square
SSE:Error sum of squares
SST:Total sum of squares
n-k:error degrees of freedom 
n-1:total degrees of freedom
MSE:Mean square error
MSR/MSE:F statistik

Bu tabloyu cok kullanmayacaz python ile hesaplayacaz



----------------------------------------------
Ornek:MASS veri seti verilmis,bunun icerisinde Cushings veri seti var
Bu veri setinde bir type syndrome tipi degiskeni var ve 4 kategorisi var
-adenoma(a)
-blater hyperplasia(b)
-carcinoma(c)
-unknown(u)

4 farkli sendrom tipi incin tetraydrocortisone un idrarla atilim hizi olculuyor
ve bu 4 farkli sendrom grubunun ortalamalari arasinda  bir fark var mi yok mu 
diye arastirilacak
toplam gozlem sayisi n=27
her grup icin ayri ayri gozlem sayisi n1=6,n2=10,n3=5,n4=6
hergrubun idrarla atilim hizi ortalamalari 3.0,8.2,19.7,14.0
degrees of freedom;
df1=4-1=3(k-1)
df2=27-4=23(n-k)
k:grup sayisi
SSb:893.5 ve SSw:2123.6


*Assumptions (varsayimlar):
Bagimli degiskenin sayisal olmasi 
Bagimsiz degiskenin kategorik olmasi 
Kategorik degisken 3 yada daha fazla gruptan olusmasi 
Bagimli degiskenin normal dagilmasi
Varyanslarin homojenligi

*Hypotheses(hipotezler)
Ho:*Hypotheses(hipotezler)
Ho:μ1=μ2=μ3=...=μk   Butun gruplarin ortalamaliri birbirine esittir
Ha:En az bir μ digerlerinden farkli 

*Test Statistic
ANOVA table	
Source	      SS	       DF	        MS	         F
Treatments	  SSR	       k−1	     SSR/(k−1)	 MST/MSE
Error	      SSE	       N−k	     SSE/(N−k)
Total     SST=SSR+SSE	   N−1

--Tablodan MSR/MSE 3.226 geldi(F test istatistigi) bunu anlamli hale 
getirebilmek icin ilgili f dagilimina gitip p-value olarak hesaplanir,daha sonra
yorumlanir

import scipy.stats as stats
1-stats.f.cdf(3.226,dfn=3,dfd=23)

Out: 0.041207862659964456

P-value:0.041 cikti yani anlamli bir deger cikti
p<a sifir hipotezi red edilir.Ortalamalardan en az biri anlamli olarak farklidir"""


-------------------------------------------------------
#Arsenic ornegi
"""Arsenik konsatrasyonu kamuya gonderilen su kaynaklarindan potansiyel saglik 
riski teskil ediyor
Bir makale yayinlanmis bu makalede arsenik konsatrasyonunu iki farkli gruptan
toplamislar
Birinci grup  metropol  Phoenix bolgesi
Ikinci grup kirsal Arizona bolgesi
Iki grup icinde 10 ar adet ornek toplanmis
konsatrasyon ppb(parts per billion) ile olculuyor"""

import pandas as pd
import scipy.stats as stats
df = pd.read_csv('C:\\Users\\hp\\Desktop\\DataScience\\STATİSTİCS\\arsenic.csv')
df

"""Out[87]: 
     Metro Phoenix  x1      Rural Arizona  x2
0          Phoenix   3            Rimrock  48
1         Chandler   7           Goodyear  44
2          Gilbert  25          New River  40
3         Glendale  10    Apache Junction  38
4             Mesa  15            Buckeye  33
5  Paradise Valley   6            Nogales  21
6           Peoria  12  Black Canyon City  20
7       Scottsdale  25             Sedona  12
8            Tempe  15             Payson   1
9         Sun City   7        Casa Grande  18"""


df['x1'].mean()
#12.5 Phoenix bolgelerinin ortalamalari

df['x2'].mean()
#12.5 Kirsal bolgelerinin ortalamalari


#varyanslarini esit kabul ederk devam ediyoruz 
indTest = stats.ttest_ind(df["x1"], df["x2"], equal_var=True, alternative='two-sided')
#Two-sided yaptin one-sided da yapabilirdik sonuc degismeyecekti
indTest
#Ttest_indResult(statistic=-2.7669395785560553, pvalue=0.012704425122128032)

indTest.statistic
#-2.7669395785560553
indTest.pvalue
#0.012704425122128032

alpha = 0.05

if indTest.pvalue < alpha:
    print("Reject the null")
else:
    print("fail to reject the null")
"""Reject the null.Makaledeki verilere gore Metropol bolgesi ile kirsal bolgenin
arsenic konsatrasyonlari anlamli sekilde birbirlerinden farklilasiyor kirsalda 
yasayanlar daha fazla arsenic konsatrasyonuna maruz kalmislar"""


#Varyanslarin esit olup olmadigini test edebiliyoruz(Levene Test)

#Levene Test

stats.levene(df["x1"], df["x2"])
#LeveneResult(statistic=7.7015516672169, pvalue=0.012482954069299166)
#Anlamli cikti yani varyanslar birbirine esit degildir,equal_var=False olarak
#girilecek

indTest = stats.ttest_ind(df["x1"], df["x2"], equal_var=False, alternative='two-sided')
indTest
#Ttest_indResult(statistic=-2.7669395785560558, pvalue=0.015827284816100885)


#Prozac Data

"""Well-being scale ölçeği geliştirilmiş(prozak)
Bu ölçekten 0-20 aralığında skor elde ediliyor
Yüksek skorlar insanın depresif açıdan iyi olduğunu gösteriyor
Prozakın depresif bireyleri iyiye götürüp göturmediği hakkında bir araştırma
yapılacak

Dependent T test uygulanacak

"""



df = pd.read_csv("C:\\Users\\hp\\Desktop\\DataScience\\STATİSTİCS\\prozac.csv")
df

"""Out[95]: 
   moodpre  moodpost  difference
0        3         5           2
1        0         1           1
2        6         5          -1
3        7         7           0
4        4        10           6
5        3         9           6
6        2         7           5
7        1        11          10
8        4         8           4 """


#H0: dbar = 0 Prozak etki etmedi 
#H1: dbar > 0 Prozak pozitif etki etti 


depTest = stats.ttest_rel(df["moodpost"], df["moodpre"], alternative='greater')
depTest
#Ttest_relResult(statistic=3.1428571428571423, pvalue=0.006872912197394244)
#degisken yazim sirasi onemlidir.df["moodpost"], df["moodpre"] 
stats.ttest_rel(df["moodpre"], df["moodpost"] , alternative='less')
#Ttest_relResult(statistic=-3.1428571428571423, pvalue=0.006872912197394244)

alpha = 0.05

if depTest.pvalue < alpha:
    print("Reject the null")
else:
    print("fail to reject the null")
#Reject the null




"""
One-way ANOVA



Örnek:Kişilerin sprint zamanları ölçülüyor
0:sigara içmeyenler 
1:eskiden sigara içenler
2:hala sigara içenler

Sprint Smoking
5.1      0
7.8      2
7.1      1
8.6      2
4.9      0
7.7      1

3 bagimsiz grup var 0,1,2.one-way anova analizi yapilacak.Bunlarin sprit 
ortalama zamanlari arasinda anlamli fark var mi ona bakacaz"""

survey = pd.read_csv("C:\\Users\\hp\\Desktop\\DataScience\\STATİSTİCS\\students_2014.csv")
survey

"""Out[99]: 
       ids        bday  enrolldate  ... CommuteTime SleepTime StudyTime
0    43783   3/22/1995              ...                     7         1
1    20278    1/1/1995              ...                     5         2
2    20389  12/31/1994              ...                     8         7
3    22820   12/1/1994              ...                     2         6
4    24559  11/10/1994              ...                     7         3
..     ...         ...         ...  ...         ...       ...       ...
430  34021   7/18/1987  1-Aug-2011  ...          18         1        10
431  40697   4/29/1987  1-Aug-2011  ...          26         6        15
432  34272              1-Aug-2011  ...          29         6        10
433  33628              1-Aug-2011  ...          14         4        10
434  39298              1-Aug-2011  ...          27         2        10

[435 rows x 23 columns]"""


survey["Sprint"] = pd.to_numeric(survey["Sprint"],errors='coerce')
survey["Smoking"] = pd.to_numeric(survey["Smoking"],errors='coerce')


df1 = survey[["Sprint", "Smoking"]].dropna()
df1.head()

"""Out[101]: 
   Sprint  Smoking
0   7.978      0.0
1   8.004      0.0
5   4.650      0.0
6   4.750      0.0
8   6.279      0.0"""

stats.f_oneway(df1[df1["Smoking"] == 0]["Sprint"], df1[df1["Smoking"] == 1]["Sprint"],
               df1[df1["Smoking"] == 2]["Sprint"])

#F_onewayResult(statistic=9.208599845380919, pvalue=0.00012659768158159465)
#Ho red edilir.p<a sifir hipotezi red edilir.Ortalamalardan en az biri anlamli 
#olarak farklidir 

df1.groupby("Smoking").Sprint.mean()
"""Out[103]: 
Smoking
0.0    6.411487
1.0    6.835333
2.0    7.120915
Name: Sprint, dtype: float64"""

#------------------------CansınHoca--------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd

# Table of Contents
    # Sampling Distributions
    # Central Limit Theorem
    # Confidence Intervals
    # t Distributions

#########################
# ÇIKARIMSAL ISTATISTIK
# Örneklem ve populasyon arasındaki ilişkiyi kurmak için kullanılıyor

#########################
# Sampling Distribution
# Istatistik, genellikle, Bir istatistik populasyon parametresini tahmin etmek için kullanılır
# Tanım : Örneklem Dağılımı: Bir istatistiğin(örneğin ortalama) olasılık dağılımıdır
# Diğer bir tanım : Bütün olası ortalamaların dağılımı
# Örneklem ortalamasının ortalaması popülasyon ile aynı, standart sapması populasyondan daha azdır
# NOT   : Örneklem dağılımının standart sapmasına, standart hata denir
# NOT   : Populasyon dağılımı çarpık bile olsa, örneklem dağılımı ne olursa olsun n>30 dan sonra normal dağılıma yakınsar

"""
    Population                                   Sample
Descriptive Statistics <-----Estimate---- Inferential Statistics
"""

"""
# Örnek: Zar attığımızda 6 farklı ihtimal vardır. Burada populasyon dağılımımız uniform dağılımdır
 x       1      2      3      4      5      6
P(x)    1/6    1/6    1/6    1/6    1/6    1/6

Mu            = 1*(1/6) + 2*(1/6) + 3(1/6) + 4*(1/6) + 5*(1/6) + 6(1/6) = 3.5
sigma(square) = (1-3.5)^2 * (1/6) + (2-3.5)^2 * (1/6) + (6-3.5)^2 * (1/6) = 2.92
sigma         = np.sqrt(2.92) = 1.71

# Populasyon için
"""
# Zarın 2 kere atılması(Populasyondan her seferinde 2 adet seçim yaparsak)
# .. sonucunda gelen sonuçların örneklem dağılımına bakalım
"""
n = 2 için bütün olası ortalamaların dağılımına bakacağız(Örneklem dağılımı)
Xbar = X1+X2 / 2

Sample         mean       Sample         mean        Sample       mean
1,1            1.0         3,1           2.0          5,1          3.0
1,2            1.5         3,2           2.5          5,2          3.5
1,3            2.0         3,3           3.0          5,3          4.0
1,4            2.5         3,4           3.5          5,4          4.5
1,5            3.0         3,5           4.0          5,5          5.0
1,6            3.5         3,6           4.5          5,6          5.5
2,1            1.5         4,1           2.5          6,1          3.5
2,2            2.0         4,2           3.0          6,2          4.0
2,3            2.5         4,3           3.5          6,3          4.5
2,4            3.0         4,4           4.0          6,4          5.0
2,5            3.5         4,5           4.5          6,5          5.5
2,6            4.0         4,6           5.0          6,6          6.0
-----------------------------------------------------------------------
Xbar     P(Xbar)
1.0       1/36
1.5       2/36
2.0       3/36
2.5       4/36
3.0       5/36
3.5       6/36
4.0       5/36
4.5       4/36
5.0       3/36
5.5       2/36
6.0       1/36

Xbar        = 1*(1/36) + 1.5*(2/36) + ... + 6*(1/36) = 3.5
S(square)  = (1-3.5)**2 * (1/36) + (1.5-3.5)^2 * (2/36) + .. + (6-3.5)^2 * (1/36) = 1.46
S = 1.21   
NOT: S  = sigma / kök(n)  = 1.71 / np.sqrt(2) = 1.21
"""

"""
# Sonuç
# Örneklem ortalamasının örneklem dağılımı için;

Xbar               = Mu             --> Populasyon ortalamasına eşit oldu
S(square)          = sigma(square)
Sx = Standart hata = sigma / kök(n) --> Populasyon std sapmasını bilirsem örneklem dağılımının standart hatasını bulabilirim

Xbar = Örneklem ortalaması
n    = Örneklem büyüklüğü
Sx   = Standart hata = örneklem ortalamasının standart sapması
"""

# Örnek : u = 900 , sigma = 300 , n=7 örneklem alalım bu örneklemin;
# .. ortalaması ve standart hatası nedir?
# Xbar = 900 , Sx = 300/np.sqrt(7) = 113.4
# NOT: Örneklem sayısı(n) artarsa Sx düşer(daralır).
# .. Yani çektiğimiz örneklem sayısını arttırdıkça hata yapma oranımız azalır

# https://onlinestatbook.com/stat_sim/samp_dist_js/index.html

# NOT   : std sapma, range, oran vs için de örneklem dağılımı hesaplanabilir

#########################
# CENTRAL LIMIT THEOREM
# Yeterince büyük bir örnekleminiz varsa örneklem ortalamasının dağılımı yaklaşık normal dağılım sergiler
# Yeterince büyük ? n>30 ya da bazı kaynaklarda n>40 olduğunda

# N(kitle sayısı) = 225 , n = 25 örneklem alınıyor , mu = 75, sigma = 10 ise
# .. Örneklem dağılımının ortalaması ve standart hatası?
# Xbar = 75 , Sd = 10/np.sqrt(25) = 2

#########################
# CONFIDENCE INTERVAL
# Örneklem ortalamasının standart hatasını işin içine katarak bir hata buluyoruz ve populasyon parametresinin
# .. olabileceği aralık hakkında belli bir güvenilirlik ile bir tahmin yapıyoruz.

# Alt güven seviyesi : Xbar - moe(margin of error) # Xbar  - z(tablo değeri)(alpha/2) * sigma/kök(n)
# Üst güven seviyesi : Xbar + moe(margin of error) # Xbar  + z(tablo değeri)(alpha/2) * sigma/kök(n)

# NOT: Populasyon std sapmasını biliniyorsa z istatistiği
# NOT: Populasyon std sapmasını bilinmiyorsa n<30 ise t , n > 30 ise z istatistiğini kullanacağız
# Alt güven seviyesi : Xbar - moe(margin of error) # Xbar  - t(tablo değeri)(alpha/2, n-1) * s/kök(n-1)
# Üst güven seviyesi : Xbar + moe(margin of error) # Xbar  + t(tablo değeri)(alpha/2, n-1) * s/kök(n-1)

# NOT: Ne kadar güvenirlirlik istersek Alt güven seviyesi ve Üst güven seviyesi arasındaki fark artacaktır

# Güven seviyeleri: Genelde %95(1-alpha) dir(Bu bilgi verilmezse %95 kabul ederek işlem yaparız).
# .. %99, %90 vs olabilir domaine göre.
# Jason hoca: n=50 için 100 farklı örneklem çekersek bu 100 örneklem için farklı güven aralıkları olacaktır
# .. Bu 100 güven aralıklığının 95 i populasyon parametresini kapsar

# ÖNEMLİ NOT: Bu şu demek değildir. "Kitlenin 100 ünün 5 i bu aralıkta değil" demek değildir
x1 = pd.Series(data=(1, 2, 3, 4, 5, 16, 17, 18, 19, 20))
# Output: (4.744944923173322, 16.25505507682668)
stats.t.interval(0.95, df=len(x1)-1, loc=x1.mean(), scale=x1.sem())

# Örnek1: Veri: 2,3,5,6,9 ---> n=5, xbar = 5 , sigma = 2.5 , sx = 1.118 . Yüzde 95 güven ile G.A?
# Alt limit: 5 - 1.96*(2.5/np.sqrt(n)) = 2.81
# Üst limit: 5 + 1.96*2.5/np.sqrt(n))= 7.19
# Güven aralığı : [2.81 , 7.19] -- > Populasyon ortalaması yüzde 95 güven ile bu aralıktadır

# NOT: Güven aralığı varyans, oran ve ortalamalar farkı için oluşturulabilir

# Örnek2: n = 25 , xbar = 38 , sigma = 6.5 is güven aralığı ?
# Alt limit: 38 - 1.96*(6.5/np.sqrt(25)) = 35.45
# Üst limit: 38 + 1.96*(6.5/np.sqrt(25)) = 40.55
# Sigma bilgisi olmasaydı t dağılımı kullanırdık t(0.025,df) yi kullanacaktık

# t distribution
# Örneklem büyüklüğü(n)(serbestlik derecesi(n-1)) az olursa o kadar yayvan bir dağılıma sahip olur dağılım
# Örneklem büyüklüğü(n)(serbestlik derecesi(n-1)) arttıkça  o kadar sivri bir dağılıma sahip olur dağılım
# Serbestlik derecesi sonsuz olan t dağılımına "normal dağılım" denir
# Serbestlik derecesi = df = sample size - 1

#########################
# ÖRNEKLER
tips = sns.load_dataset('tips')
tips.head()

# Hangi gün ortalama daha fazla hesap ödeniyor?
sns.barplot(x='day', y='total_bill', data=tips, ci=95)
# Pazar günü ortalaması daha yüksek.

# Cuma günleri ödenen hesap için güven aralığı hesaplayalım(Manuel). Sonra fonksiyonla yapacağız
tipsFri = tips[tips['day'] == 'Fri']
tipsFri.head()
x_bar = tipsFri.total_bill.mean()
x_bar      # 17.151578947368417

std_error = tipsFri.total_bill.sem()
std_error  # 1.904760773479416
# NOT: sem : standard error of the mean

moe = 1.96 * std_error   # 3.7333311160196554

lower = x_bar - moe
lower  # 13.41
upper = x_bar + moe
upper  # 20.88

# Scipy ile yapalım
stats.norm.interval(0.95, loc=x_bar, scale=std_error)
# (13.418316432184106, 20.88484146255273)

# t dağılımı ile yapalım
stats.t.interval(0.95, df=len(tipsFri)-1,
                 loc=tipsFri.total_bill.mean(), scale=tipsFri.total_bill.sem())
# (13.149825056979093, 21.15333283775774)

# t ve z istatistiği hesabı
stats.t.ppf(0.975, 75)  # df = 75   # 1.9921021536898653 = t tablo değeri
stats.t.ppf(0.025, 75)  # -1.9921021536898658 # Eksilisi

stats.norm.ppf(0.975)  # 1.959963984540054  --> Yaklaşık 1.96
# NOT: ppf: Percent point function


# %% 2. ders
# Table of Contents
    # Performing a Significance Test
    # Type I and Type II Errors
    # One an Two Tailed Tests
    # Significance Test About a Population Mean

##################################################
# 1.Performing a Significance Test
# Örneklem istatistiklerini kullanarak populasyon ile ilgili tahminde bulunmak
# Anlamlılık: Örneklemden hesapladığımız ortalamanın "istatistiksel olarak" anlamlı olup olmadığı,
# .. ya da 2 grup arasındaki ortalamanın "istatistiksel olarak" anlamlı olup olmadığı 

# Hipotez: Populasyon parametresi(oran, ortalama vs) hakkında bir iddiada bulunmak
# Hipotez Testlerinin aşamaları
    # 1.Assumptions
    # 2.Hypotheses
    # 3.Test Statistic
    # 4.P-value
    # 5.Conclusion

#########################
# 1.Assumptions
# Her istatistiksel testin bir varsayımı vardır

# Z-Test Assumptions
    # Örneklemler rasgele seçilmeli
    # Gözlemler bağımsız olmalı
    # Populasyon standart sapması biliniyorsa veya 30 gözlem varsa z testi kullanılıyor

#########################
# 2.Hypotheses
# 0 hipotezi ve alternatif hipotez kavramları vardır
# Hipotezler genelde aşağıdaki gibi kurulur
    # H0: Populasyon parametresi "x" değerine eşittir/fark yoktur
    # H1: Populasyon parametresi "x" değerine eşit değildir(fark yoktur)/büyüktür/küçüktür
# Not: Eşit değildir: çift kuyruk, -- Büyüktür/Küçüktür: Tek kuyruk

# Sonuç: H0 ı başta doğru olduğunu varsayarız sonra bunu testederiz

#########################
# 3.Test Statistic
# Ortalama üzerine bir istatistik yapıyorsak, z testi veya t testi kullanabiliriz
# Korelasyon testi, Oran testi, Ki kare hipotez testleri için farklı test istatistikleri vardır
"""
            Populasyon standart sapması biliniyor mu ?
                    /                  \
                  YES                  NO
                  /                      \
               Z-Test                 Örneklem sayısı 30 dan büyük mü?
                                         /                    \
                                        YES                   NO
                                        /                      \
                                Z-test or t-test          t-test
"""

#########################
# 4.P-value
# Jason Hoca: Örneklem ortalamasının ne kadar uç bir değer olduğu hakkında bilgi verir
# p-value ne kadar küçük olursa H0 hipotezinden uzaklaşmış oluruz(ortalamadan uzaklaşmış oluruz).
# ..  Dolayısıyla reddetme gücü artar

#########################
# 5.Conclusion
# p value yu alpha değeriyle karşılaştırıyoruz
# p value < alpha ise H0 red          (reject the null(H0))
# p value > alpha ise H0 reddedilemez (fail to reject the null(H0))

# NOT: H0 hipotezini reddedememek ve H0 ı reddetmek için veriyle oynamak?

#########################
# Significance level: 0.01, 0.05, 0.1 vs

##################################################
# 2. Type I and Type II Errors / False Negatif and False Pozitif
# Type I   : Gerçek değeri 1 iken 0 olarak tahmin etmek
    # Örnek: Gerçekte dolandırıcı(1) olan bir işlemi dolandırıcı değil(0) olarak etiketlemek
# Type II  : Gerçek değeri 0 iken 1 olarak tahmin etmek
    # Örnek: Gerçekte masum(0) olan birini suçlu(1) olarak etiketlemek

# Hangi hata daha kritiktir ?
# Confusion matrix: Mülakat sorusu

##################################################
# 3.One an Two Tailed Tests
#########################
# One Tail statistical Tests
    # z(test) = (xbar - mu) / (sigma/kök(n))
        # H1 hipotezi "büyüktür" şeklinde kurulduysa z(test) > z(alpha)
        # H1 hipotezi "küçüktür" şeklinde kurulduysa z(test) < z(alpha) ise H0 red
        # p < alpha ise H0 red

#########################
# Two Tail statistical Tests
    # z(test) = xbar - mu / sigma/kök(n)
        # z(test) < z(alpha/2) ya da z(test) > z(alpha/2) ise H0 red
        # p < alpha ise H0 red. DIKKAT: p < alpha/2 ise "DEĞİL"

# NOT: z tablosunu okuma ?

##################################################
# 4.Significance Test About a Population Mean
# Araştırdığımız sonuç anlamlı mı değil mi

#######################
# TEK ÖRNEKLEM t-test
###############
# Örnek 1: Mu = 10, sigma = 1.5, sample mean = 10.5, alpha = 0.05, n=40

# 1.Varsayımlar
# n=40 > 30
# ÖNEMLİ NOT: Normalde TEK ÖRNEKLEM t-test te asıl varsayımım örneklemimin dağılımı normal mi değil mi bakmalıyım

# 2.Hipotez testi
# H0 : Mu = 10
# H1 : Mu > 10 

# 3.Test istatisliği
# z(test) = (xbar - mu) / (sigma/kök(n)) = (10.5-10) / 1.5 /√¯40 = 2.1

# 4.P-value
# P-value = 0.0179
# z test(2.1) için alanımız 0.0179 

# 5.Sonuç
# z(test) > z(alpha) = 2.1 > 1.645 olduğunda H0 red diyebiliriz ya da
# P-value = 0.0179 < 0.05 olduğundan H0 red

# Python tarafı
import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns

xbar  = 10.5
sigma = 1.5
n = 40
mu = 10

# H0: mu = 10 
# H1: mu > 10

# Test Statistics
z = (xbar-mu) / (sigma / np.sqrt(n))
z   # 2.10

# p-value
p = 1-stats.norm.cdf(z)
p   # 0.0175

# z < z(alpha)=1.645 ya da p >0.05 olduğundan H0 red edilemez

# 2. yol # Elimizde array olsaydı a yerine array i koyup böyle yapabilirdik
# stats.ttest_1samp(a,10, alternative='greater') 

###############
# Örnek 2: Mu = 170, sigma = 65, sample mean = 178, alpha = 0.05, n=400

# 1.Varsayımlar
# n=400 > 30 z kullanabiliriz
# ÖNEMLİ NOT: Normalde TEK ÖRNEKLEM t-test te asıl varsayımım örneklemimin dağılımı normal mi değil mi bakmalıyım

# 2.Hipotez testi
# H0 : Mu = 170
# H1 : Mu > 170

# 3.Test istatisliği
# z(test) = (xbar - mu) / (sigma/kök(n)) = (178-170) / 65 /√¯400 = 2.46
# P-value = 0.0069 < 0.05 olduğundan H0 red

# 4.P-value 
# z test(2.46) için alanımız 0.0069
# P-value = 0.0069

# 5.Sonuç
# z(test) > z(alpha) = 2.46 > 1.645 olduğunda H0 red diyebiliriz ya da
# P-value = 0.0069 < 0.05 olduğundan H0 red

###############
# Örnek 3: Mu = 110, s = 10, sample mean = 108, alpha = 0.01, n=20
    
# 1.Varsayımlar
# n=20 < 30 z kullanamayız. t kullanacağız ve populasyon std sapmasını da bilmiyoruz
# t = (xbar - mu) / (s / kök(n))
# ÖNEMLİ NOT: Normalde TEK ÖRNEKLEM t-test te asıl varsayımım örneklemimin dağılımı normal mi değil mi bakmalıyım

# 2.Hipotez testi
# H0 : Mu >= 110   # Not: Bu hipotez, Mu = 110 şeklinde kurulsaydı da yanlış olmazdı
# H1 : Mu < 110

# 3.Test istatisliği
# t(test) = (xbar - mu) / (s/kök(n)) = (108-110) / 10 /√¯20 = - 0.846
# P-value = 0.0069 < 0.05 olduğundan H0 red

# 4.P-value 
# t test(-0.846) için alanımız 0.19
# P-value = 0.19

# 5.Sonuç
# t(test) > t(alpha,n-1) = - 0.846 > -2.539 olduğunda H0 red edilemez ya da
# P-value = 0.19 > 0.05 olduğundan H0 reddedilemez

###############
df = sns.load_dataset('mpg')
df.head()
df[df['origin'] == 'usa'].describe()  # beygir gücü mean: 110

###############
# Örnek 4:
# H0: U.S originli arabaların beygir güçleri ortalaması 110 a eşittir
# H1: U.S originli arabaların beygir güçleri ortalaması 110 dan büyüktür iddiamız olsun
# Normalde verim normal dağılıyor mu dağılmıyor mu bakmalıyım

stats.ttest_1samp(df[df['origin'] == 'usa']['horsepower'],110, alternative = 'greater')
# Null değer olduğu için NaN geldi
stats.ttest_1samp(df[df['origin'] == 'usa']['horsepower'].dropna(),110, alternative = 'greater')
# Ttest_1sampResult(statistic=3.550044602017898, pvalue=0.0002310035889540432)
# p < alfa  .. H0 red. Yani U.S originli arabaların beygir güçleri 110 dan büyüktür

###############
# Örnek-5
# H0: U.S originli arabaların mpg leri ortalaması 22 a eşittir
# H1: U.S originli arabaların mpg leri ortalaması 22 ye eşit değildir

stats.ttest_1samp(df[df['origin'] == 'usa']['mpg'].dropna(), 22, alternative="two-sided")
# Ttest_1sampResult(statistic=-4.723072192881628, pvalue=3.891005205691281e-06)
# p < alfa .. H0 red

# Claruswayda gördüğümüz istatistik dersi için hangi testi nerede kullanıyoruz; 
    # https://sk.pinterest.com/pin/352477108344113157/

# Varsayım sağlanmıyorsa?
# Jason Hoca: Burada bizim öğretmeye çalıştığımız şey hipotez testi mantığı, varsayımlar
# .. sağlanmıyorsa non-parametrik testleri google dan bulup uygulayabilirsiniz

# https://towardsdatascience.com/parametric-vs-non-parametric-tests-and-where-to-use-them-85130b3877dc
# https://blog.minitab.com/en/understanding-statistics/data-not-normal-try-letting-it-be-with-a-nonparametric-hypothesis-test
# https://en.wikipedia.org/wiki/Sign_test

#%% 3. ders
# Table of Contents
    # Basic Concepts Review(Önceki ders tekrarı)
        # (One Sample T Test)
    # Independent Samples T Test
    # Dependent T Test(Paired)
    # One-way ANOVA
   
##############################
# Independent Samples T Test
# Diğer bir ismi: Bağımsız 2 örneklem T testi
# İş ilanlarındaki ismi : A/B testi(Bu isim 2 den fazla grup içinde kullanılır.)
    # A/B testi;  En iyi performansı sağlayan modeli belirlemek üzere kullanılır
    
# TANIM:2 bağımsız grup ortalamaları karşılaştırılır(Kadın ve Erkeğin Maaş ortalamaları farklı anlamlı mı gibi..)

# 1.Varsayımlar
# 1 sayısal değişken(Maaş), 2 kategorik değişken olacak(Kadın, Erkek)
# Bağımsız rasgele örneklem
# Normal dağılım varsayımı
# Varyans homojenliği

# 2.Hipotezler
# H0: Mu1  = Mu2  ya da Mu1 - Mu2  = 0
# H1: Mu1 != Mu2  ya da Mu1 - Mu2 != 0 , Mu1 < Mu2, Mu1 > Mu2

# 3.Test istatistiği
# Varyansların eşit olmadığı varsayımı ile t testi
# Varyansların eşit olduğu varsayımı ile t testi
# Not: Yukarıda bahsi geçen t testleri için Formüller ve serbestlik dereceleri hesabı farklı

# 4.P-value
# 5.Sonuç

# Örnek1: Normal şartlar altında(Normallik varsayımı) kadın ve erkek vücut sıcaklığı aynı mıdır?
"""
Men       Women
96.9       97.8
97.4       98.0
97.5       98.2
97.8       98.2
97.8       98.2
97.9       98.6
98.0       98.8
98.6       99.2
98.8       99.4
"""
# Aynı şeyleri yapacağız
    # 1.Varsayımlar kontrol edilecek(Burada varyansların eşit olduğu varsayılmış. Normalde s1: 0.5833, s2:0.5487)
    # 2.Hipotezler kurulacak
    # 3.Test istatistiği(Varyansların eşit olduğu varsayımı ile t testi)
        # t = -2.371  , df = 16 bulunacak
    # 4.p-value
        # Çift yönlü hipotezdi, t = -2.371 den küçük ve t = 2.371 den büyük yerlerin alanlarını toplayacağız
        # p-value : 0.0306 çıkmış -- python kodu : 2*stats.t.cdf(-2.371, 16)
    # 5.Sonuç
        # p<0.05 olduğundan H0 reddedilir. Yorum: Fark anlamlıdır(Vücut sıcaklıkları arasındaki)

##############################
# Dependent T Test(Paired)
# Eşleştirilmiş örneklemler T-testi / Bağımlı örneklemler t testi

# TANIM: Aynı gözlemler üzerinden 2 farklı ölçüm(Diyet programının öncesi- sonrası için kilo "farkı" anlamlı mı gibi...)

# 1.Varsayımlar
# 1 bağımlı sürekli değişken olacak
# 2 farklı ölçüm olacak
# Normal dağılım varsayımı(Farkların -- > The distribution of the differences in the
# ..  dependent variable between the two related groups should be approximately normally distributed)
# https://statistics.laerd.com/spss-tutorials/dependent-t-test-using-spss-statistics.php

# 2.Hipotezler
# H0: d = 0 
# H1: d != 0   d < 0, d > 0

# 3.Test istatistiği
# t = (d-0) /S(xbar)  , S(xbar) =  Sdiff / kök(n)
# d       : Sample mean of differences
# n       : Sample size
# Sdiff   : Sample standart deviation of differences
# S(xbar) : Estimated standart error of the mean (x/sqrt(n))

# 4.P-value
# 5.Sonuç

# Örnek : https://mustafaotrar.net/istatistik/bagimli-iliskili-gruplar-t-testi/
# Örnek1: Çelik levha kirişleri kesme oranları ölçümüş 2 methodla(AYNI kirişe uygulanmış)
"""
ID          1.Method          2.Method        Difference
1             1.186             1.061          0.125
2              ...               ...           0.159
3              ...               ...           0.259
4              ...               ...           0.277
5              ...               ...           0.135
6              ...               ...           0.224
7              ...               ...           0.328
8              ...               ...           0.451
9              ...               ...           0.507
"""
# Aynı şeyleri yapacağız
    # 1.Varsayımlar kontrol edilecek(Burada varyansların eşit olduğu varsayılmış. Normalde s1: 0.5833, s2:0.5487)
    # 2.Hipotezler kurulacak
    # 3.Test istatistiği(Varyansların eşit olduğu varsayımı ile t testi)
        # t = 6.15  , df = 8 bulunacak
    # 4.p-value
        # Çift yönlü hipotezdi, t = -6.15 den küçük ve t = 6.15 den büyük yerlerin alanlarını toplayacağız
        # p-value : 0.0003 çıkmış -- python kodu : 2*(1-stats.t.cdf(6.15, 8))
    # 5.Sonuç
        # p<0.05 olduğundan H0 reddedilir. Yorum: Fark anlamlıdır(Vücut sıcaklıkları arasındaki)
        # 1. method ve 2.method farklıdır. Independent a benziyor? Evet ancak burada "aynı kirişe" uygulandı test
        # .. Yani dependent a uygulandığı için "paired" kullandık.

# Örnek2: Prozac(ilaç) sorusu

##############################
# One-way ANOVA(Analysis of Variance)
# Independent Sample T-test(grup sayısı 2) e alternatif bir testtir. 
# Karşılaştıracağımız bağımsız grup sayısı 3 veya daha fazla olursa ANOVA(Varyans analizi) kullanıyoruz
# Grup sayısı 2 iken ANOVA yapılırsa Independent Sample T-test ile aynı sonuç alınır
# Bağımsız iki örneklem T-testinde , 2 gruptan

# Örneğin: 4 farklı tedavi sonuç ortalamaları arasında fark var mı yok mu
# Örneğin; Kişilerin sprint zaman ortalamaları arasında fark var mı yok mu 
# 3 bağımsız grup: Nonsmokers(0), Past smokers(1), Current smokers(2)
"""
Sprint     Smoking
5.1           0
7.8           2
7.1           1
8.6           2
4.9           0
7.7           1
"""

# 1.Varsayımlar
# 1 bağımlı sürekli değişken olacak(Sprint zamanı, sigara içip içmeme durumlarına bağlı)
# 2 veya daha fazla bağımsız kategorik değişken olacak(Nonsmokers(0), Past smokers(1), Current smokers(2))
# Normal dağılım varsayımı
# Varyans homojenliği

# 2.Hipotezler
# H0: Mu1 = Mu2 = Mu3 = Mu4 = ....  =Muk
# H1: Herhangi bir grubun ortalaması farklı
# ÖNEMLİ NOT: Mu1 = Mu2 çıkabilir ama Mu2 != Mu3 olabilir. Yani H1 3 grubun ortalaması birbirinden
# .. farklı anlamında "DEĞİL" En az bir grubun ortalaması farklı anlamında
# Peki gruplar arasında 2 li karşılaştırmalar yapabilir miyiz? "Tukey" testi kullanılabilir bunun için

# 3.Test istatistiği
# F = MSR/MSE  (Gruplar arası kareler toplamı/Gruplar içi kareler toplamı)
# MSR: Regression mean square= SSR(Sum of Squares) / df    (Diğer ad: Gruplar arası varyans)
# MSE: Mean square Error = SSE(Error Sum of Squares) / df  (Diğer ad: Grup içi varyans)
# https://www.cuemath.com/anova-formula/

# 4.P-value
# 5.Sonuç


############################
# PANDAS ÖRNEKLER
import pandas as pd
import scipy.stats as stats

############################
# INDEPENDENT 2 SAMPLES T-TEST  ÖRNEK
df = pd.read_csv("arsenic.csv")
df.head() # Arsenik konsantrasyonunu 2 farklı gruptan toplanmış(Metro Phoenix, Rural Arizona)
"""
Arsenic concentration in public drinking water supplies is a potential health risk.
An article in the Arizona Republic (May 27, 2001) reported drinking water arsenic 
concentrations in parts per billion (ppb) for 10 metropolitan Phoenix communities 
and 10 communities in rural Arizona.
"""

df["x1"].mean()  # 12.5
df["x2"].mean()  # 27.5
# Ciddi fark var arada

# H0: M1 = M2
# H1: M1 != M2

# Normal dağılım ve Varyans homojenliğinin olduğunu varsayalım
# Yine de bakalım varyans homojenliğine
test_stat, pvalue = stats.levene(df["x1"], df["x2"])
test_stat, pvalue  # (7.7015516672169, 0.012482954069299166) .. p<0.05 H0 red. Varyanslar homojen "DEĞİL" normalde

indTest = stats.ttest_ind(df["x1"],df["x2"], equal_var=True, alternative='two-sided') # default equal_var = True
indTest

indTest.statistic
indTest.pvalue

alpha = 0.05
if indTest.pvalue < alpha:
    print("Reject the null")
else:
    print("fail to reject the null")
# Sonuç: Reject the null
# Yorum: Kırsalda(Rural Arizona) yaşıyanlar daha fazla bir arsenic konsantrasyonuna maruz kalmışlar

############################
# DEPENDENT T-TEST(PAIRED) ÖRNEK
df = pd.read_csv("prozac.csv")
df
"""
Let us consider a simple example of what is often termed "pre/post" data or "pretest/posttest" data.
Suppose you wish to test the effect of Prozac on the well-being of depressed individuals, using a standardised "well-being scale" that sums Likert-type items to obtain a score that could range from 0 to 20.
Higher scores indicate greater well-being (that is, Prozac is having a positive effect).
While there are flaws in this design (e.g., lack of a control group) it will serve as an example of how to analyse such data.
"""

# H0: dbar = 0
# H1: dbar > 0

# 
stats.ttest_rel(df["moodpost"], df["moodpre"], alternative = "greater")
# statistic=3.1428571428571423, pvalue=0.006872912197394244)
# p < 0.05 olduğundan H0 red. Farkların ortalaması 0 dan büyüktür yani prozac etki göstermiştir

############################
# ONE-WAY ANOVA ÖRNEĞİ
survey = pd.read_csv("students_2014.csv")
survey.head()
"""
In the sample dataset, the variable Sprint is the respondent's time (in seconds) to sprint a given distance, and Smoking is an indicator about whether or not the respondent smokes (0 = Nonsmoker, 1 = Past smoker, 2 = Current smoker). Let's use ANOVA to test if there is a statistically significant difference in sprint time with respect to smoking status. Sprint time will serve as the dependent variable, and smoking status will act as the independent variable.
The null and alternative hypotheses of one-way ANOVA can be expressed as:
"""
# H0: µ0 = µ1 = µ2 ("all k population means are equal")
# H1: At least one µi different ("at least one of the k population means is not equal to the others")

# Veride sorun var numeric e çeviriyoruz alttaki değişkenlerin veri tiplerini
survey["Sprint"] = pd.to_numeric(survey["Sprint"], errors = 'coerce')
survey["Smoking"] = pd.to_numeric(survey["Smoking"], errors = 'coerce')

df1 = survey[["Sprint","Smoking"]].dropna() # NaN ları da atalım
df1.head()

stats.f_oneway(df1[df1["Smoking"]==0]["Sprint"],df1[df1["Smoking"]==1]["Sprint"],df1[df1["Smoking"]==2]["Sprint"])
# F_onewayResult(statistic=9.208599845380919, pvalue=0.00012659768158159465)

# p<0.05 H0 red. En az bir grubun ortalaması istatistiksel olarak farklı

df1.groupby("Smoking").Sprint.mean()

from statsmodels.stats.multicomp import MultiComparison
comparison = MultiComparison(df1["Sprint"], df1["Smoking"])
tukey = comparison.tukeyhsd(0.05)
print(tukey.summary())
# Çıktıda , group1 -group 2 : Ortalamalar için çoklu karşılaştırma yapıyor
# meandiff: Farklarını aldı
# p-adj : Düzeltilmiş p value değeri
# lower,upper: Alt üst sınır güven aralığı.
# reject: H0 ı reddediyor musun reddedemiyor musun
