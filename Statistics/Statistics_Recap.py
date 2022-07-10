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




