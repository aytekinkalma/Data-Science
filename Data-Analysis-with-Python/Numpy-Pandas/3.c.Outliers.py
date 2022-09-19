import numpy as np
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)

#%% OUTLIERS
# What is Outlier? : Outliers can create biased results while calculating the stats of the data due to its extreme nature, 
# .. thereby affecting data

# Causes of Outliers
# 1.Data entries errors       : Yanlış giriş yapılmış olabilir elle 
# 2.Measurement errosr or instrument errors : Cihazda problem olabilir
# 3.Sampling erros            : Örnek çekerken alt sınıf arabalar ve üst sınıf arabaların olduğu bir yerde örneklem sadece 
# .. bir gruba göre çekilmiş olabilir(Örnek: 9 alt sınıf 1 üst sınıf. gibi...)
# 4.Data processing errors    : data manipulation or data set unintended mutations
# 5.Natural novelties in data : Yıllar ile ilgili bir data ile ilgileniyorsunuz diyelim.Ama mesela bu yılın başlarında extreme bir olay 
# .. olmuştur doların sadece o aylarda uçması gibi. Sizin tahminleriniz yanlış olacaktır dolayısıyla
# 6.Experimental errors (data extraction or experiment planning/executing errors)
# 7.Intentional (dummy outliers made to test detection methods)

# Types of Outliers
# 1.Univariate Outliers   : Generally referred to as extreme points on a variable : Tek bir sütuna göre outlier incelemesi
# 2.Multivariate Outliers : Generally combination of unusual data points for two or more variables : 
# .. Iki veya daha fazla sütuna göre outlier incelemesi . 
# Genelde multivariate ile ilgilenmeyeceğiz

# Detecting Outliers
# 1.Graphs : Box plot, Histogram, Scatter plot
# 2.InterQuartile range(IQR) technique 
# 3.Statistical Tests : Grubbs' test, Chi-square test, Dixon's Q test (Bu kısımla burada ilgilenmeyeceğiz. 
# .. Bunlar genelde akademik anlamda kullanılıyor)
# Not: Outlierları sayısal sütunlar için bakıyoruz

# Handling with Outliers
# 1.Remove the outliers
# 2.Limitation (winsorize)
### Q1-1.5*IQR = 5 olsun , eğer "4" değeri varsa bunu "5" değerine eşitlerim(baskılarım) 
### Hoca: Bana bu yöntem hiç mantıklı gelmiyor
# NOT: dropping outliers vs limiting outliers?(Hoca: drop daha mantıklı, eğer o outlier yerine bir şey ile 
# .. dolduramıyorsanız düşmelisiniz(drop etmelisiniz) outlier ları))
# 3.Data transformation(log, square root)
### Örneğin her değerin logaritmasını alınca o değerler outlier olarak görünmeyecek
### Dataları ölçeklendirme işine transformation diyoruz
# 4.Replacing the outliers(mean, median, mode)
# 5.Using different analysis methods(statistical/nonparametric tests)
# 6.Valuing the outliers(Valid reason for the outlier to exist)

# Guideline for Handling Outliers
# If the outlier in question is:
# 1.A measurement error or data entry error, correct the error if possible. If you can't fix it, 
# .. remove that observation because you know it's incorrect
# 2.Not a part of the population you are studyinh(i.e., unusual properties or conditions), you can legimately remove the outlier
# 3.A natural part of the population you are studying, you should not remove it

##################################################################
#%% CATCHING AND DETECTING OUTLIERS
df1 = pd.DataFrame({"a":[1,2,3],"b":[4,5,6]})
df1.info()
sns.get_dataset_names()
df = sns.load_dataset("diamonds")
"""
info about dataset

carat :Carat weight of the diamond
depth % :The height of a diamond, measured from the culet to the table, divided by its average girdle diameter
table % :The width of the diamond's table expressed as a percentage of its average diameter
price :the price of the diamond
x :length mm
y :width mm
z :higth mm
"""

# Bu gün yapacağımız şeylerde sayısal veriler lazım. Onları seçelim ve df imize eşitleyelim
df = df.select_dtypes(include="number")
df.info() # Herhangi bir NaN değer yok

#####################
# Detecting Outliers with Graphs
# Önce grafiklerle bakmamız lazım
plt.figure(figsize=(15,8)) # Default değerleri var ama figsize: 15 e 8 lik olsun dedik. NOTE: dpi=200 yazarsak şekil netleşir
# NOTE: dpi=200 yazarsak parantez içine şekil netleşir
sns.boxplot(x=df.table);   # Bir çok extreme değer olduğunu görüyoruz

plt.figure(figsize=(8,6))
sns.histplot(df.table, bins=30, kde=False); # 80 ve 90 larda değerler olduğunu vs görüyorum
# .. Bu görsellerle bunu anladım. Peki bu extreme değerlerin gerçek değerlerini nasıl görebilirim sort yapabilirim

df.table.sort_values().tail(10) # Alttaki değerlerden 10 tane görelim
# Bunların index değerlerini alıp bu indexlere karşılık gelen diğer sütunlara bakayım

tail_index = df.table.sort_values().tail(10).index
tail_index

df.loc[tail_index] # Örn; 24932 ye baktığımda table, price vs değerleri uyumlu bu outlier değil diye düşünebilirim

######################
# Detecting Outliers with Tukey's Fences | Tukey's Rule
Q1 = df.table.quantile(0.25) # table sütununda yüzde 25 e denk gelen değer 56
Q3 = df.table.quantile(0.75) # table sütununda yüzde 75 e denk gelen değer 59
IQR = Q3-Q1
IQR
df.table.describe()

Q1 = df.table.describe().loc["25%"]
Q3 = df.table.describe().loc["75%"]
IQR = Q3-Q1
IQR
lower_lim = Q1 - 1.5*IQR
upper_lim = Q3 + 1.5*IQR
lower_lim, upper_lim

(df.table < lower_lim).sum()                            # lower_lim in altında kaç tane değer olduğunu gösterdik
((df.table < lower_lim) | (df.table > upper_lim)).sum() # Bunların toplamını görelim burada(Kaç tane outlier olduğunu görelim)

######################
# Removing the Outliers
drop_index = df.loc[((df.table < lower_lim) | (df.table > upper_lim))].index # outlier indexlerini çektik burada sonra drop edeceğiz
drop_index

df.loc[~((df.table < lower_lim) | (df.table > upper_lim))].index             # outlier olmayan değerlerin index
df_cleaned = df.loc[~((df.table < lower_lim) | (df.table > upper_lim))]      # outlier olmayan değerlerden oluşan dataframe
df_cleaned
df.drop(index=drop_index, axis=0) # 2. yol

plt.figure(figsize=(15,8))
sns.boxplot(x=df_cleaned.table);                   # Grafikte hiç outlier kalmadı gördüğümüz gibi
sns.histplot(df_cleaned.table, bins=10, kde=False);
# Describe ile betimsel istatiktiklerini karşılaştıralım
df_cleaned.table.describe()
df.table.describe()
compare = pd.DataFrame(df.table.describe().values, index=df.table.describe().index, columns = ["first"])
compare["second"] = df_cleaned.table.describe().values
compare
pd.DataFrame([df.table.describe(), df_cleaned.table.describe()], index=['first', 'clean']).T # 2. yol

##########################
# Limitation & Transformation of the Outliers
# Limitation using .winsorize() method
# With winsorizing, any value of a variable above or below a percentile k on each side of the
# .. variables’ distribution is replaced with the value of the k-th percentile itself. 
# .. For example, if k=5, all observations above the 95th percentile are recoded to the value
# .. of the 95th percentile, and values below the 5th percent are recoded, respectively

"""
Cautions on Winsorizing Data
Here are a few things to keep in mind when deciding to winsorize data:
1. If there aren’t extreme outliers, then winsorizing the data will only modify the smallest and 
.. largest values slightly. This is generally not a good idea since it means we’re just modifying 
.. data values for the sake of modifications.
2. Outliers can represent interesting edge cases in the data. Thus, before modifying outliers 
.. it’s a good idea to take a closer look at them to see what could have caused them.
3. You should decide whether or not to winsorize data after collecting the data, not before. 
.. You should see if there actually are extreme outliers before you decide to perform winsorization.
.. If no extreme outliers are present, winsorization may be unnecessary.
"""
from scipy.stats.mstats import winsorize

df
# winsorize çalışma mantığına bakalım önce
winsorize(df.table, (0.02, 0.05)) # Hangi sütuna winsorize uygulamak istiyorsam onu yazıyorum, sonra tuple içerisine hangi 
# .. oranda sıkıştırmak istiyorsam onu yazıyorum. sol taraftan(100 tane değer varsa) yüzde 2 lik kısmı(2 tanesini) 
# .. outlier olmayan en küçük değere ya da outlier olmayan en büyük değere eşitler

winsorize(df.table, (0.02, 0.05))
a = len(df.table[df.table<lower_lim])/len(df) # lower_lim den küçük olan değerlerin yüzdesi
b = len(df.table[df.table>upper_lim])/len(df) # upper_lim den büyük olan değerlerin yüzdesi
table_win = winsorize(df.table, (a,b))
table_win

# Şimdi bunu görselleştirelim
plt.figure(figsize=(10,6))
sns.boxplot(x=table_win); # Gördüğümüz gibi extreme değerlerden kurtulmuş olduk
sns.histplot(table_win, bins=10, kde=False); # Gördüğümüz gibi extreme değerlerden kurtulmuş olduk

table_win_ser = pd.Series(table_win) # Table_win i seriye çevirirsek daha kolay işlem yaparız
table_win_ser

pd.DataFrame([df.table.describe(), table_win_ser.describe()], index=['first', 'clean']).T # 2. yol
df.table.sort_values().head(20)
table_win_ser.sort_values().head(20) # min=51.6 olan değere eşitlemiş outlierları (küçük olanlar için)

###############################
# Transformation using log() method
# The Numpy.log() method lets you calculate the mathematical log of any number or array. The numpy.log() is a mathematical 
# .. function that helps user to calculate Natural logarithm of x where x belongs to all the input array elements.
# The natural logarithm log is the inverse of the exponential function, so that log(exp(x)) = x. 
# .. The natural logarithm is logarithm in base.

# Transformation using log() method
# En sık kullanılan yöntem log almaktır.
df.carat
sns.boxplot(x=df.carat);                    # Çok fazla outlier görünüyor
sns.histplot(df.carat, bins=10, kde=False);
carat_log = np.log(df.carat)                # Carat sütununundaki tüm değerlerin log unu aldık
carat_log
sns.boxplot(x=carat_log);
sns.histplot(carat_log, bins=10,kde=False);

df["carat_log"] = np.log(df.carat)
df

################################
# Removing outliers after log() transformation
# first method to drop outliers
df.carat_log.sort_values().tail(2)
drop_index = df.carat_log.sort_values().tail(2).index
drop_index

df.drop(drop_index, axis=0) # Bu 2 indexi drop ettik

# second method to drop outliers
Q1 = df.carat_log.quantile(0.25)
Q3 = df.carat_log.quantile(0.75)
IQR = Q3-Q1
IQR
lower_lim = Q1 - 1.5*IQR
upper_lim = Q3 + 1.5*IQR
lower_lim, upper_lim
(df.carat_log < lower_lim).sum()
(df.carat_log > upper_lim).sum()
df.loc[~((df.carat_log < lower_lim) | (df.carat_log > upper_lim))].index
df_cleaned1 = df.loc[~((df.carat_log < lower_lim) | (df.carat_log > upper_lim))] # outlier olmayan değerlerden oluşan dataframe
df_cleaned1

# third method to drop outliers
# Normalde burada drop etmiyor, baskılıyoruz
a = len(df.carat_log[df.carat_log<lower_lim])/len(df) # lower_lim den küçük olan değerlerin yüzdesi
b = len(df.carat_log[df.carat_log>upper_lim])/len(df) # upper_lim den büyük olan değerlerin yüzdesi
table_win = winsorize(df.carat_log, (a,b))
table_win

plt.figure(figsize=(10,6))
sns.boxplot(x=table_win); 


####################################################-----END-----####################################################






