######################################################
# AB Testing
######################################################
# Martyn Jones, Managing Director at Cambriano Energy "Without a grounding in Statistics, a Data Scientist is a
# .. Data Lab Assistant"
# Veriye dayalı karar almanın temeli istatistiktir.(Hipotez testleriyle, AB testleriyle bilimsel bir dayanak sağlayarak,
# .. sonuç ortaya koyar.)
# ÖNEMLI: AB testi TEK BAŞINA iş aldıran serisindendir.
# Istatistik: Belirsizlik altında karar vermek üzere belirsizliği azaltmaya çalışmak(Yarınki hava durumunu tahmin ederek
# .. belirsizliği azaltmaya çalışırız yarın dışarı çıkacaksak mesela. Yüzde 80 yağmayacak dese bile öncekinden daha iyi
# .. yani önceden hiç bilgi yoktu şimdi hata payı olan bir tahminimiz var)
# Belirsizlik altında karar vermek üzere belirsizliği azaltmaya çalışmak yani amaç
# H. James Wilson:"The Future of AI Will Be About Less Data, Not More"

# Population nedir?...
# Örneklem nedir?: Anakitle üzerinden örneklem seçip üzerinde çalışıyoruz. Yansız olmalı ve kitleyi temsil etmeli.
# ..Belirli hatalar da olabilir

# Descriptive Statistics(Betimsel/Tanımlayıcı Istatistikler)(EDA-Keşifçi veri analizi çalışmalarına karşılık geliyor)
# Ort, Medyan, Mod, Kartiller, Değişim Aralığı, Standart Sapma, Korelasyon
# Ort vs Medyan farkı önemli burada(Bunu biliyoruz.Değişken aykırı değerlere sahipse 'medyan'ı göz önünde bulundur)
# Std sapma: Merkezden olan uzaklığı ifade eden "sapmaların ortalamasıdır" .

# Confidence Intervals(Bu konu önemli.Hoca: Sadece bunu kullanarak çözdüğüm case oldu)
# Anakütle parametresinin tahmini değerini(istatistik) kapsayabilecek iki sayıdan oluşan bir aralık bulunmasıdır.
# Diyelim ki; Web sitesinde geçirilen ortalama sürenin güven aralığı nedir?
# Ortalama: 180 saniye, std sapma: 40 saniye
# Benim web sitemde geçirilen süre bilimsel olarak yüzde 95 ile 172-188 arasındadır.
# Web siteme gelen 100 kullanıcıdan 95 i 172 ile 188 saniye arasında vakit geçirecek.
# Bunu niye bilmeliyim. Mesela ona göre reklam çıkmak isteyebilirim vs vs.
# .. ya da 172-188 arasında 182. saniyesinde pop-up çıkarabilirim mesela
# Ortalama için, Oran için, iki ortalama farkı için ya da iki oranın farkı için güven aralığı hesaplayabiliriz.
# .. veya std sapma içinde yapabiliriz....
# Buraya kadarki şeylerin uygulamalarını bir yapalım sonra hipotez testlerine geçeceğiz.(Satır 66 ya gidelim)

"""
# Temel İstatistik Kavramları
# - Sampling (Örnekleme)
# - Descriptive Statistics (Betimsel İstatistikler)
# - Confidence Intervals (Güven Aralıkları)
# - Hypothesis Testing (Hipotez Testleri)
# - Correlation (Korelasyon)

# AB Testing
# - İki Grup Ortalamasını Karşılaştırma (Bağımsız İki Örneklem T Testi)
#       - Parametrik Karşılaştırma
#       - Nonparametrik Karşılaştırma
# - İki Grup Oran Karşılaştırma (İki Örneklem Oran Testi)
# - İkiden Fazla Grup Ortalaması Karşılaştırma (ANOVA)
"""
######################################################
# Temel İstatistik Kavramları
######################################################

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

############################
# Sampling (Örnekleme)
############################
# Ml de öğrenme işi istatistik teorisiyle gerçekleşir, öğrenme sürecinin optimizasyonu ise bilgisayar bilimlerince
#.. gerçekleşir(Bunu bi prof söylemiş TR den) O yüzden öğrenme için burada örneklem çok önemli bir konu.

# Anakitleden bunu temsil edecek ve bir örneklem çekmek istediğimizi düşünelim.
populasyon = np.random.randint(0, 80, 10000)
populasyon[0:10]
populasyon.mean() # 39.3462

np.random.seed(115)
orneklem = np.random.choice(a=populasyon, size=100)
orneklem[0:10]
orneklem.mean() # 36.87

# Şirketlerden çalışma için veri istiyoruz bize sorduğunda verinin boyutu ne olmalı diye. Yanıtımız;
# Sizin uğraştığınız problemle ilgili varsaydığınız örüntüyü(pattern'ı) barındırdığını düşüneceğiniz bir büyüklükte
# .. olmalı.

np.random.seed(10) # Başka örneklemler çekelim
orneklem1 = np.random.choice(a=populasyon, size=100)
orneklem2 = np.random.choice(a=populasyon, size=100)
orneklem3 = np.random.choice(a=populasyon, size=100)
orneklem4 = np.random.choice(a=populasyon, size=100)
orneklem5 = np.random.choice(a=populasyon, size=100)
orneklem6 = np.random.choice(a=populasyon, size=100)
orneklem7 = np.random.choice(a=populasyon, size=100)
orneklem8 = np.random.choice(a=populasyon, size=100)
orneklem9 = np.random.choice(a=populasyon, size=100)
orneklem10 = np.random.choice(a=populasyon, size=100)

(orneklem1.mean() + orneklem2.mean() + orneklem3.mean() + orneklem4.mean() + orneklem5.mean()
 + orneklem6.mean() + orneklem7.mean() + orneklem8.mean() + orneklem9.mean() + orneklem10.mean()) / 10
# output: 37.61
# Örneklem sayısı arttığında Anakitle ortalamasına yaklaşır. Yani anakitleyi daha fazla yansıtır. Bu yüzden
# .. verinin fazla olması genelde arzu edilen bir şeydir.

orneklem1.mean() # 40.62
orneklem7.mean() # 35.35
orneklem8.mean() # 36.41

############################
# Descriptive Statistics (Betimsel İstatistikler)
############################
df = sns.load_dataset("tips")
df.describe().T
# Bu betimsel istleri ilgili değişkenin dağılımı ile ilgili bilgi edinmek için kullanıyorduk.
# Hoca: Betimsel istatistikleri yorumlaması işe aldığım biri için kriterlerimden birisi
# Ortalama 20 birim ama medyan ne diye vs sormalıyım. Sonra std sapmasını sormalıyım veriyi tanımak için
# .. veri simetrik mi vs vs .. O yüzden mesela muhattaplarla sadece 'ortalamanın' sonucu ile konuşmamalıyım.
############################
# Confidence Intervals (Güven Aralıkları)
############################
# Tips Veri Setindeki Sayısal Değişkenler için Güven Aralığı Hesabı
df = sns.load_dataset("tips")
df.describe().T
sms.DescrStatsW(df["total_bill"]).tconfint_mean()
sms.DescrStatsW(df["tip"]).tconfint_mean()
# Ortalama ne kadar bahşiş ödendi yerine bu restorandaki kişilerin yüzde 95 i şu aralıkta(18.66-20.90) hesap ödeyecektir
# Güven aralıklığı genelliyor bu durumu yüzde 5 hatayla. Bu güzel bir şey

# Titanic Veri Setindeki Sayısal Değişkenler için Güven Aralığı Hesabı
df = sns.load_dataset("titanic")
sms.DescrStatsW(df["age"].dropna()).tconfint_mean()
sms.DescrStatsW(df["fare"].dropna()).tconfint_mean()

# Retail Veri Setindeki Sayısal Değişkenler için Güven Aralığı Hesabı
df_ = pd.read_excel("datasets/online_retail_II.xlsx",
                    sheet_name="Year 2010-2011")
df = df_.copy()

sms.DescrStatsW(df["Quantity"].dropna()).tconfint_mean()
sms.DescrStatsW(df["Price"].dropna()).tconfint_mean()

############################
# Hypothesis Testing (Hipotez Testi)
############################
# Bir inanışı bir savı test etmek için kullanılan yöntemlerdir.
# AB testi dendiğinde ya da iş dünyasında bir karar almak gerektiğinde en geçerli bilimsel yer burasıdır(Hipotez testi)
# Bütün konunun özeti(ÖNEMLİ): Grup karşılaştırmalarında temel amaç olası farklılıkların şans eseri ortaya çıkıp
# .. çıkmadığını göstermeye çalışmaktır.
# Örneğin; Mobil uygulamada yapılan arayüz değişikliği sonrasında kullanıcıların uygulamada geçirdikleri günlük ortalama
# .. süresi arttı mı? (Bu bir hipotezdir savdır)
# .. Burada 2 tasarımdan biri bi kullanıcı grubuna diğeri diğer kullanıcı grubuna gösterilmiş
# .. ilk durumda kullanıcılar 1 dk 55 sn vakit geçiriyor tasarımda, ikinci durumda 2 dk 58 sn vakit geçiriyor.
# .. Peki burada bir artış var diyebilir miyim? 2. çalışma daha iyidir diyebilir miyim?
# .. Bilemem şans eseri ortaya çıkmış olabilir. Hipotez testi yapılmalı.

# Başka bir tasarım (bu hocanın yaptığı): Kayıt ekranı sadeleştirilmesinden sonra çarpan-kaydolan oranı arttı mı?
# .. Çarpma: 'kişi gördüğünde' demek..
# Tasarım 1: 100 kişi çarpmış 42 tanesi üye olmuş : 0.42
# Tasarım 2: 0.38
# Aynı örneklem sayıları ile sonuç böyle.
# Çarpan-kaydolan oranı tasarım 2 den 1 e ARTMIŞ GİBİ GÖRÜNÜYOR ama bu örneklem bir şans-hata barındırıyor. Bu şansı
# .. göz önünde bulundurmalıyım. O yüzden tasarım 1 daha iyidir diyemiyorum.
# .. Hipotez testiyle bir fark olup olmadığını şansa değer olup olmadığını test edeceğiz.

# Başka çalışma 2 tane covid aşısı var.
# p1: 0.80 koruma oranı
# p2: 0.84
# 2. aşı daha iyidir diyebilir miyiz?(Bilemiyoruz)

# NOT: Ama biri 40 biri 400 ise böyle durumlara da test yapmayın. Bariz farklar varsa siz de 'buna da test yapmak lazım'
# .. denmemeli muhattaplara(Bu çaylaklığa düşmeyin) :)

##############################################
# AB TESTİ(Bağımsız İki Örneklem T Testi)
# İki grup arasında karşılaştırma yapılmak istediğinde kullanılır.
# Hipotezler : H0: M1=M2, H1: M1!=M2 . Odağımız H0 burada. H0 ı reddediyorum ya da reddedemiyorum diyeceğiz.
# Örneklem çekip, x1ort=x2ort mayı test edeceğiz.

# İki Grup Ortalamasını Karşılaştırma(Bağımsız İki Örneklem T Testi)(AB Testing)
# Örnek sayıları aynı, varyanslar homojen ise:        t = (X1ort-X2ort)/ [Sp x kök(2/n) , Sp = Kök[(skarex1+skarex2) / 2
# Örnek sayısı farklı, varyanslar homojen ise:        t = ... , Sp = ...
# Örnek sayıları farklı varyanslar homojen değil ise: t = ... , Sp = ...
# t testi , z testi nedir? Birisi diyor ki ben bi tablo oluşturdum (z tablosu mesela) kıyaslamak için ben size bir
# .. referans tablosu oluşturdum demiş.

# P-VALUE
# p value < alfa=0.05 ise H0 red.

# Varsayımlar
# 1. Normallik(2 grubunda dağılımları normal olmalı)
# 2. Varyans Homojenliği(İki grubun varyanslarının birbirine benzerliğini ifade ediyor)
# Bu varsayımlara bakmayıp testleri yapıp yorumlayanlara güven duymayın.

# Bir problem var makine öğrenmesi projesi önceki sistem A, sonrası makine öğrenmesi sistemi B olsun.
# İş uygulaması: ML Modelinin Başarı Testi(AB Testi)
# Bir ML modeli geliştirilip canlıya alınmış. Bunun başarısı test edilmek isteniyor.
# A eski sistemi , B yeni sistemi ifade ediyor
# ML modeli anlamlı farklılık oluşturabildi mi?
# Problem: Bir ML projesine yatırım yapılmış. Ürettiği tahminler neticesinde oluşan gelir ile
# .. eski sistemin ürettiği gelirler karşılaştırılıp anlamlı farklılık olup olmadığı test edilmek isteniyor
# .. Hoca: 9 ay uğraşıldı buna
# Bu proje insanlara ürün öneriyor. Yeni sistemde ML nin ürettiği tahminlerle ürün öneriliyor.
# Detaylar:
# 1.Model geliştirilmiş ve web sitesine entegre edilmiş
# 2.Site kullanıcıları belirli bir kurala göre ikiye bölünmüş olsun.
# 3.A gurubu eski B grubu yeni sistem.
# 4.Gelir anlamında anlamlı bir iş yapılıp yapılmadığı test edilmek isteniyor
# Yani 9 ay boşa mı uğraştık yoksa sistemimiz başarılı mı ?
# H0: mü1 = mü2 , H1: mü1 != mü2
# mü1:Eski sisteme göre insanlar ürün satın aldığındaki gelirler , mü2: yeni sisteme....

# Burada dönüşüm oranı kıyaslanabilir normalde. Gelirler kıyaslanabilir. Business tan business a farklılaşabilir.
# NOT: Muhattaplarınızla bunu iyi belirlemeli ve onlara şunu sormalısınız. Ben neyi yaparsam başarı olarak kabul ediliyo

# Mesela gelir açısından
"""
A(Eski)         B(Eski)
gün-gelir       Gün-Gelir
1    12         1    14
2    15         2    8
3    20         3    30
...         ...
40  21          40   28

n1=40, n2=40
Aort=18K
Bort=20K
s1=5, s2=10
Sonuç: H0 reddedilemez. Yani fark var diyemeyiz. Peki ML modelimizi hemen canlıdan çıkaralım mı?
# .. Hayır. iyileştirmeye çalış ya da başka bir çözüm bul.
"""
# Altakileri atlıyoruz ve satır 320(AB Testing) e gidiyoruz.

# Tek Örneklem T Testi

# Bir web analytics tool'u kullanıcılarımının web sitemde geçirdiği ortalama sürenin 170 saniye olduğunu
# iddia ediyor.

# İnanıyorum tabi ama bir test edeyim diye düşünüyorum.

# H0: Web sitemizde geçirilen ortalama süre 170 saniyedir.
# H1: ..değildir


session_duration = pd.DataFrame(np.random.normal(175, 10, 1000), columns=["session_duration"])
session_duration.describe().T

ttest_1samp(session_duration, popmean=170)

p_value = ttest_1samp(session_duration, popmean=170)[1][0]

print(f"{p_value:.5f}")

# p-value < ise 0.05 'ten HO RED.
# p-value < değilse 0.05 H0 REDDEDILEMEZ.


######################################################
# Correlation (Korelasyon)
######################################################

# Bahşiş veri seti:
# total_bill: yemeğin toplam fiyatı (bahşiş ve vergi dahil)
# tip: bahşiş
# sex: ücreti ödeyen kişinin cinsiyeti (0=male, 1=female)
# smoker: grupta sigara içen var mı? (0=No, 1=Yes)
# day: gün (3=Thur, 4=Fri, 5=Sat, 6=Sun)
# time: ne zaman? (0=Day, 1=Night)
# size: grupta kaç kişi var?


df = sns.load_dataset('tips')
df["total_bill"] = df["total_bill"] - df["tip"]

df.plot.scatter("tip", "total_bill")
plt.show()

###########################
# Varsayım Kontrolü
###########################

# Varsayım sağlanıyorsa pearson sağlanmıyorsa Spearman.

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır.

test_stat, pvalue = shapiro(df["tip"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(df["total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

###########################
# Hipotez Testi
###########################

# Korelasyon Katsayısı
# Varsayım sağlanıyorsa pearson:
df["tip"].corr(df["total_bill"])

# Varsayım sağlanmıyorsa: spearman:
df["tip"].corr(df["total_bill"], method="spearman")

# H0: Değişkenler arasında korelasyon yoktur.
# H1: Değişkenler arasında korelasyon vardır.

# Korelasyonunu Anlamlılığının Testi
test_stat, pvalue = pearsonr(df["tip"], df["total_bill"])
print('Korelasyon Katsayısı = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Nonparametrik Hipotez Testi
test_stat, pvalue = spearmanr(df["tip"], df["total_bill"])
print('Korelasyon Katsayısı = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = kendalltau(df["tip"], df["total_bill"])
print('Korelasyon Katsayısı = %.4f, p-value = %.4f' % (test_stat, pvalue))

######################################################
# AB Testing (Bağımsız İki Örneklem T Testi)
######################################################

# 1. Varsayım Kontrolü
#   - 1. Normallik Varsayımı
#   - 2. Varyans Homojenliği
# 2. Hipotezin Uygulanması
#   - 1. Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi (parametrik test)
#   - 2. Varsayımlar sağlanmıyorsa mannwhitney testi (non-parametrik test)
# Not:
# - Normallik sağlanmıyorsa direk 2 nin 2 si. Varyans homojenliği sağlanmıyorsa 2 nin 1 ine(t testi ne) numaraya arguman girilir.(equal_var=True # satır 406)
# - Normallik incelemesi öncesi aykırı değer incelemesi ve düzeltmesi yapmak faydalı olabilir.

############################
# Uygulama 1: Sigara İçenler ile İçmeyenlerin Hesap Ortalamaları Arasında İst Ol An Fark var mı?
############################
# Ortalamaların incelenmesi:
df = sns.load_dataset("tips")
df.groupby("smoker").agg({"total_bill": "mean"})
# Bu fark şans eseri mi ortaya çıkıyor

############################
# 1. Varsayım Kontrolü
############################
# Normallik Varsayımı(Shapiro Wilks)
# Varyans Homojenliği(levene)

############################
# Normallik Varsayımı
############################
# Bunu test etmek için bir hipotez testi kurmamız gerekiyor.
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır.

test_stat, pvalue = shapiro(df.loc[df["smoker"] == "Yes", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value < ise 0.05'ten HO RED.
# p-value < değilse 0.05 H0 REDDEDILEMEZ.
# H0 red, 1. grup için Normal dağılım varsayımı sağlanmıyor.

test_stat, pvalue = shapiro(df.loc[df["smoker"] == "No", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value < ise 0.05'ten HO RED.
# p-value < değilse 0.05 H0 REDDEDILEMEZ.
# HO red, 2. grup için Normal dağılım varsayımı sağlanmıyor.

# Non-parametriğe gideceğiz normalde ama biz sanki varsayımlar sağlanmış gibi devam edeceğiz.
# Normalde bu sağlansaydı varyans homojenliğine bakacaktık. Devam edelim.
############################
# Varyans Homojenligi Varsayımı
############################
# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

test_stat, pvalue = levene(df.loc[df["smoker"] == "Yes", "total_bill"],
                           df.loc[df["smoker"] == "No", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value < ise 0.05 'ten HO RED.
# p-value < değilse 0.05 H0 REDDEDILEMEZ.
# H0 red. Yani varyanslar homojen değildir.

# 2 varsayımda sağlanmadı--> Nonparametrik. Ama dediğimiz gibi biz sağlanmış gibi devam edeceğiz.
############################
# 2. Hipotezin Uygulanması
############################
# 1. Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi (parametrik test)
# 2. Varsayımlar sağlanmıyorsa mannwhitneyu testi (non-parametrik test)

# Eğer normallik sağlanmazsa her türlü nonparametrik test yapacağız.
# Eger normallik sağlanır varyans homojenliği sağlanmazsa ne olacak?
# T test fonksiyonuna arguman gireceğiz.

# H0: M1 = M2 (... iki grup ortalamaları arasında ist ol.anl.fark yoktur)
# H1: M1 != M2 (...vardır)

# NOT: Hipotezin tanımını yapmak yani H0 a ne yazılacağını sormak bizim mülakat sorularından birisi

# Varsayımlar sağlanmış gibi devam ediyoruz.
############################
# 1.1 Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi (parametrik test)
############################
test_stat, pvalue = ttest_ind(df.loc[df["smoker"] == "Yes", "total_bill"],
                              df.loc[df["smoker"] == "No", "total_bill"],
                              equal_var=True) # varyans homojenliği = True

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue)) # pvalue:0.1820

# p-value < ise 0.05 'ten HO RED.
# p-value < değilse 0.05 H0 REDDEDILEMEZ.
# H0 reddedilemez. O zaman istatistiki olarak anlamlı bir farklılık yokmuş
# Sigara içenler ile içmeyenler arasında .... anlamlı bir fark yoktur.

# Varsayım sağlanmamıştı şimdi non-parametrik testimizi yapalım
############################
# 1.2 Varsayımlar sağlanmıyorsa mannwhitneyu testi (non-parametrik test)
############################
test_stat, pvalue = mannwhitneyu(df.loc[df["smoker"] == "Yes", "total_bill"],
                                 df.loc[df["smoker"] == "No", "total_bill"])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value < ise 0.05 'ten HO RED.
# p-value < değilse 0.05 H0 REDDEDILEMEZ.
# p-value>0.05 .. H0 reddedilemez : iki grup ort. arasında ist. ol. anl. fark yoktur.
# Zaten ort. yakındı gerçekte de. Yani bu sonuç örtüşüyor.

############################
# Uygulama 2: Titanic Kadın ve Erkek Yolcuların Yaş Ortalamaları Arasında İstatistiksel Olarak Anl. Fark. var mıdır?
############################
# df = pd.read_csv("datasets/titanic.csv")
df = sns.load_dataset("titanic")
df.groupby("sex").agg({"age": "mean"})
# Kadınla erkek yaşları arasında fark var mı ?

# Normallik varsayımı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır.

test_stat, pvalue = shapiro(df.loc[df["sex"] == "female", "age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# H0 red . Sağlanmıyor. Non-parametriğe gitmemiz lazım normalde ama bakalım.

test_stat, pvalue = shapiro(df.loc[df["sex"] == "male", "age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# H0 red . Sağlanmıyor. Non-parametriğe gitmemiz lazım normalde

# Yine de bakalım varyans homojenliğine
# Varyans homojenliği
# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir
test_stat, pvalue = levene(df.loc[df["sex"] == "female", "age"].dropna(),
                           df.loc[df["sex"] == "male", "age"].dropna())

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Varsayımlar sağlanmadığı için nonparametrik
# H0: M1 = M2 (... iki grup ortalamaları arasında ist ol.anl.fark yoktur.)
# H1: M1 != M2 (...vardır)
# mannwhitneyu
test_stat, pvalue = mannwhitneyu(df.loc[df["sex"] == "female", "age"].dropna(),
                                 df.loc[df["sex"] == "male", "age"].dropna())

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Bu üstteki 2 örneğe AB testi yerine Hipotez testi demek daha doğru olur
############################
# Uygulama 3: Diyabet Hastası Olan ve Olmayanların Yaşları Arasında Ist. Ol. Anl. Fark var mıdır?
############################
df = pd.read_csv("datasets/diabetes.csv")
df.groupby("Outcome").agg({"Age": "mean"})

# Normallik Varsayımı (H0: Normal dağılım varsayımı sağlanmaktadır.)
test_stat, pvalue = shapiro(df.loc[df["Outcome"] == 1, "Age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# 1. grup h0 red

test_stat, pvalue = shapiro(df.loc[df["Outcome"] == 0, "Age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# 2. grup için de ho red

# Varyans Homojenliği Varsayımı (H0: Varyanslar homojendir)
test_stat, pvalue = levene(df.loc[df["Outcome"] == 1, "Age"].dropna(),
                           df.loc[df["Outcome"] == 0, "Age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# H0 reddedilemez

# DIKKAT: levene de 2 grubu bir arada girdik, shapiro da ayrı ayrı girdik.

# Normallik varsayımı sağlanmadığı için nonparametrik.(Gerçek hayatta sürekli nonparametriğe gideceksiniz)
# Hipotez (H0: M1 = M2)
test_stat, pvalue = mannwhitneyu(df.loc[df["Outcome"] == 1, "Age"].dropna(),
                                 df.loc[df["Outcome"] == 0, "Age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# H0 red ort arasında anlamlı bir fark istatistiki olarak vardır.

# Daha gerçekçi iş problemlerine geçelim.
###################################################
# İş Problemi: Udemy'de Sorulan Sorulara Yanıt Verilmeli mi?
###################################################
df = pd.read_csv("datasets/course_reviews.csv")
df.head()

# Yanıt alamayanlar:
df[(df["Questions Asked"] > 0) & (df["Questions Answered"] < 1)]["Rating"].mean()
# 4.72

# Yanıt alanlar:
df[(df["Questions Asked"] > 0) & (df["Questions Answered"] >= 1)]["Rating"].mean()
# 4.77

# Bir fark var gibi ama sizce bu fark gerçekten var mı?
# Yanıt alanların daha iyi puan verdiğini söyleyebilir miyiz?

# H0: "Soru sorup yanıt alamayan kişilerle soru sorup yanıt alan kişilerin verdiği
# puan ortalamaları arasında istatistiki olarak anlamlı bir yoktur"
# H1: ...vardır.

# Önce varsayımlar:
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır.
# p-value < ise 0.05'ten HO RED.
# p-value < değilse 0.05 H0 REDDEDILEMEZ.

test_stat, pvalue = shapiro(df[(df["Questions Asked"] > 0) & (df["Questions Answered"] < 1)]["Rating"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(df[(df["Questions Asked"] > 0) & (df["Questions Answered"] >= 1)]["Rating"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# H0: M1 = M2 (... iki grup ortalamaları arasında ist ol.anl.fark yoktur.)
# H1: M1 != M2 (...vardır)
# HO RED. direk non-parametriğe gidelim bu sefer varyans homojenliğine hiç bakmayalım.

test_stat, pvalue = mannwhitneyu(
    df[(df["Questions Asked"] > 0) & (df["Questions Answered"] < 1)]["Rating"],
    df[(df["Questions Asked"] > 0) & (df["Questions Answered"] >= 1)]["Rating"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Fark yoktur. O yüzden sorulara cevap vermeye gerek yok.
# Başka bir case a bakalım
###################################################
# İş Problemi: Kursun Büyük Çoğunluğunu İzleyenler ile İzlemeyenlerin Puanları Birbirinden Farklı mı?
###################################################
# kursun büyük çoğunluğunu izleyenler
df[(df["Progress"] > 75)]["Rating"].mean() # 4.86

# kursun büyük çoğunluğunu izlemeyenler
df[(df["Progress"] < 40)]["Rating"].mean() # 4.74

# H0: M1 = M2 (... iki grup ortalamaları arasında ist ol.anl.fark yoktur.)
# H1: M1 != M2 (...vardır)

test_stat, pvalue = mannwhitneyu(df[(df["Progress"] > 75)]["Rating"],
                                 df[(df["Progress"] < 40)]["Rating"])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# H0 red. Yani fark vardır. Kursun büyük çoğunluğunu izleyenlere ya da küçük bölümünü izleyenlere
# .. bir aksiyon almalı mı ?. Yüzde 75 üstüne hoca birebir mail atmış. Yani yüzde 75 den büyük olanlarla hoca
# .. ilgilenmiş. "Yardımcı olabileceğimiz bir şey var mı?" vs diye yazmış. Puanlar değişmiş

###################################################
# İş Problemi: Yine de bazı soruları yanıtlayacak olsak hangi kişilerin sorularını yanıtlamalıyız?
###################################################
# Ilerlemesi düşük olup sorularına yanıt alamayanlar ile ilermesi yüksek olup sorularına yanıt alamayanlar arasında
# .. anlamlı fark var mı yok mu?
df[(df["Questions Asked"] > 0) & (df["Questions Answered"] < 1) & (df["Progress"] < 25)]["Rating"].mean()
df[(df["Questions Asked"] > 0) & (df["Questions Answered"] < 1) & (df["Progress"] > 75)]["Rating"].mean()

test_stat, pvalue = mannwhitneyu(
    df[(df["Questions Asked"] > 0) & (df["Questions Answered"] < 1) & (df["Progress"] < 25)]["Rating"],
    df[(df["Questions Asked"] > 0) & (df["Questions Answered"] < 1) & (df["Progress"] > 75)]["Rating"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# SONUÇ: H0 red edilemez. Yani sorulara dönmeye gerek yok :)

######################################################
# AB Testing (İki Örneklem Oran Testi)
######################################################
# Burada iki oranı karşılaştıracağız. AB testinde en çok karşılaşılan senaryolardan birisidir.

# Örnek
# H0: Yeşil Butonunun Dönüşüm Oranı ile Kırmızı Butonun Dönüşüm Oranı Arasında İst. Ol. Anlamlı Farklılık Yoktur.
# H1: ... vardır

# Yeşil Butonu gören 1000 kişi tıklayan 300 kişi
# Kırmızı Butonu gören 1100 kişi tıklayan 250 kişi
basari_sayisi = np.array([300, 250])
gozlem_sayilari = np.array([1000, 1100])
proportions_ztest(count=basari_sayisi, nobs=gozlem_sayilari)
# Varsayım 1 tanedir.(n>30). O da genelde 30 dan büyük olur zaten

# H0 red. Yani anlamlı bir fark vardır.

# Gerçek hayatta bu oranları çıkarmak problem olabiliyor. Yoksa test kolay. O yüzden şimdi
# ..daha farklı bir senaryoya bakalım.
############################
# Uygulama: Kadın ve Erkeklerin Hayatta Kalma Oranları Arasında İst. Olarak An. Farklılık var mıdır?
############################
df = sns.load_dataset("titanic")

# Hayatta kalma oranları:
df.loc[df["sex"] == "female", "survived"].mean()
df.loc[df["sex"] == "male", "survived"].mean()
# Fark açık. Normalde test yapmaya gerek yok burada ama bakalım.

# Oran senaryomuza uyarlamak için sum alalım.(Bu üst senaryodaki başarı sayısı)
female_succ_count = df.loc[df["sex"] == "female", "survived"].sum() # kadın için başarı sayısı("yeşil butona tıklanma sayısı:300" anlamında)
male_succ_count = df.loc[df["sex"] == "male", "survived"].sum()

# Frekanslar(Gözlem sayısı)
df.loc[df["sex"] == "female", "survived"].shape[0]
df.loc[df["sex"] == "male", "survived"].shape[0]

test_stat, pvalue = proportions_ztest(count=[female_succ_count, male_succ_count],
                                      nobs=[df.shape[0], df.shape[0]])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# H0 red . Yani fark vardır. Zaten barizdi.
# AB Testi dendiğinde aklımıza 2 şey gelmeli. Grup ortalaması testi ve Oran Testi
# 2 sini de değerlendirdik. Oran testindeki metriklere gitmek bazen uğraştırıcı olabilir.
# .. Bu sizin derdiniz olmamalı aslında. Geliyor olursa diye böyle bir uygulama koyduk buraya

######################################################
# ANOVA (Analysis of Variance)(Varyans Analizi)
######################################################
# İkiden fazla grup ortalamasını karşılaştırmak için kullanılır.
# En az bir dönemlik derstir.
# Tıp,tarım,ilaç alanlarında, biyoistatistik çalışmalarında(ilaç yaptım test edeyim vs..) yaygındır.

# İş uygulaması: Anasayfa İçerik Stratejsi Belirlemek
# İnsanlar websitesinde uzun süre geçirirse marka bağlılığı, reklama tıklama, ürünlerin satılması oranı artar
#.. Amaç insanların sitede geçirdiği süreyi artırmak
# Problem: 3 tarz haber var hangisine odaklanılmalı(A,B,C). Anasayfada geçirilen süre artırılmak isteniyor
# Detaylar:
# 1.Bir web sitesi için başarı kriterleri: Ortalama ziyaret süresi, hemen çıkış oranı vb
# 2.Uzun zaman geçiren kullanıcıların reklamlara daha fazla tıkladığı ve markaya olan bağlılıklarının arttığı biliniyor
# 3.Buna yönelik olarak benzer haberler farklı resimler ya da farklı formatlarda hazırlanarak oluşturulan test
# .. gruplarına gösteriliyor.
# A:Doğal şekilde , B:Yönlendirici , C:İlgi çekici (haberler farklı fotmatta hazırlanarak test
#.. gruplarına gösteriliyor)
# A:Doğal şekilde - olduğu şekliyle haberi sunmak
# B:Yönlendirici - kullanıcıların düşüncelerine etki edip bazı uygulamalar yapılması.
# ... iki takım berabere kaldı diyelim B: beşiktaş 8 kişi kalan rakibine galip gelemedi
# C:İlgi çekici - görsellerin çağrışım yapabileceği görseller ya da tık tuzağı(yüzyılın maçı)
# Veriler bize sağlıklı gelmeli ya da verileri bizim oluşturmamız lazım
# Verinin oluşma sürecinde mutlaka işin içinde olmalıyız.
# Veri bize csv,txt,excel formatında gelecek.(BURADA BİR SORUN VARDI.. ISTATISTIK ON HAZIRLIK NOTLARINA BAK)

# Anavo tablosundaki 'significance' yani p-value değeri <0.05 is H0 red. Gruplar arası anlamlı bir fark vardır denir
#.. Hangisinin ilgi gördüğüne bakılır. Gerçi bu açık(Hoca videoda gösterdi o değerler daha yüksekti)

###########################
# Varsayım Kontrolü
###########################
# 1.Normallik varsayımı
# 2.Varyans homojenliği varsayımı

# Tüm grupların normallik varsayımını sağlaması gerekmektedir.
# Varsayım sağlanıyorsa one way anova testini
# Varsayım sağlanmıyorsa kruskal testini
# .. kullanacağız

# H0:Normal dağılım varsayımı sağlanmaktadır. Normallik varsayımı.
# Burada 4 grup yani 4 gün(day) var. Bunlara shapiro wilks testi uygulayayım.
# Bunu fonksiyonla yapayım kısa olsun diye.
for group in list(df["day"].unique()):
    pvalue = shapiro(df.loc[df["day"] == group, "total_bill"])[1]
    print(group, 'p-value: %.4f' % pvalue)

# Hepsi için H0 RED. Bütün gruplar için sağlanmıyor. Non-parametrik normalde ama sağlanmış gibi yapacağız

# H0: varyans homojenliği varsayımı sağlanmaktadır.
test_stat, pvalue= levene(df.loc[df["day"] == "Thur", "total_bill"],
                          df.loc[df["day"] == "Fri", "total_bill"],
                          df.loc[df["day"] == "Sat", "total_bill"],
                          df.loc[df["day"] == "Sun", "total_bill"])
print('Test Stat = %.4f, p-value= %.4f' % (test_stat,pvalue))

# H0 reddedilemedi. Varsayım sağlanıyor ama önceki normallik varsayımından patlamıştık zaten

# Hipotez testimizle devam edelim
# Hipotez Testi
# Değerlerimizi görelim
df.groupby("day").agg({"total_bill": ["mean", "median"]})
# H0: varyans homojenliği varsayımı sağlanmaktadır

# H0: Grup ortalamaları arasında ist ol anl fark yoktur:

# Nonparametrik anova testi:
kruskal(df.loc[df["day"] == "Thur", "total_bill"],
        df.loc[df["day"] == "Fri", "total_bill"],
        df.loc[df["day"] == "Sat", "total_bill"],
        df.loc[df["day"] == "Sun", "total_bill"])

# H0 red. Fark varmış

# Varsayım sağlansaydı..
# parametrik anova testi:
f_oneway(df.loc[df["day"] == "Thur", "total_bill"],
         df.loc[df["day"] == "Fri", "total_bill"],
         df.loc[df["day"] == "Sat", "total_bill"],
         df.loc[df["day"] == "Sun", "total_bill"])

# Burada işimiz bitti diyip durabiliriz. Ya da fark var ama bu farklılık kimden kaynaklanıyor sorusunu sorabiliriz.
# Bunun için bir çoklu karşılaştırma yapmamız lazım tukey testiyle

# İkili karşılaştırma
from statsmodels.stats.multicomp import MultiComparison
comparison = MultiComparison(df['total_bill'], df['day'])
tukey = comparison.tukeyhsd(0.05)
print(tukey.summary())
# Çıktıda , group1 -group 2 .. Ortalamalar için çoklu karşılaştırma yapıyor
# meandiff: Farklarını almış
# p-adj : Düzeltilmiş p value değeri
# lower,upper: Alt üst sınır güven aralığı. Bununla ilgilenmiyorum
# reject: H0 ı reddediyor musun. False
# Burada her bir grup kendi aralarında karşılaştırıldığında anlamlı bir fark bulunamadı.
# .. Burada bir soru işareti var. 2 grup karşılaştırıldığında bir fark yok. 3 grup olunca fark var.
# Hoca bu bir problem değil ama bende de soru işareti dedi. Bıraktı..

# R tarzı çıktı ve t test ikili karşılaştırması için bakalım
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Ordinary Least Squares (OLS) model
model = ols('total_bill ~ day', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

pair_t = model.t_test_pairwise('day')
pair_t.result_frame

# Farklılık bulunmamış. İhtiyaç olurda ararsanız diye bu ikili karşılaştırma bölümünü ekledik.