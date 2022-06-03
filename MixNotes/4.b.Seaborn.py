import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
# %matplotlib inline
import matplotlib.pyplot as plt
import scipy
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)


#%% SEABORN
# SEABORN vs MATPLOTLIB
# 1.Functionality:
# Matplotlib: Matplotlib is mainly deployed for basic plotting. Visualization using Matplotlib generally consists of
# .. bars, pies, lines, scatter plots and so on.
# Seaborn: Seaborn, on the other hand, provides a variety of visualization patterns. It uses fewer syntax and has easily
# .. interesting default themes. It specializes in statistics visualization and is used if one has to summarize data in visualizations
# .. and also show the distribution in the data.

# 2.Handling Multiple Figures:
# Matplotlib: Matplotlib has multiple figures that can be opened, but need to be closed explicitly. plt.close() only closes the current 
# .. figure. plt.close(‘all’) would close them all.
# Seaborn: Seaborn automates the creation of multiple figures. This sometimes leads to OOM (out of memory) issues.

# 3.Visualization:
# Matplotlib: Matplotlib is a graphics package for data visualization in Python. It is well integrated with NumPy and Pandas. 
# .. The pyplot module mirrors the MATLAB plotting commands closely. Hence, MATLAB users can easily transit to plotting with Python.
# Seaborn: Seaborn is more integrated for working with Pandas data frames. It extends the Matplotlib library for creating beautiful 
# .. graphics with Python using a more straightforward set of methods.

# 4.Data frames and Arrays
# Matplotlib: Matplotlib works with data frames and arrays. It has different stateful APIs for plotting. The figures and axes are
# .. represented by the object and therefore plot() like calls without parameters suffices, without having to manage parameters.
# Seaborn: Seaborn works with the dataset as a whole and is much more intuitive than Matplotlib. For Seaborn, replot() is the entry 
# .. API with ‘kind’ parameter to specify the type of plot which could be line, bar, or many of the other types. Seaborn is not stateful. 
# .. Hence, plot() would require passing the object.

###############################################################################################################################
#%% Seaborn
tips = sns.load_dataset("tips")
tips.head()

############################################################
# 1.SCATTERPLOT : İki sayısal veri arasındaki ilişki hakkında bilgi veriyor
sns.scatterplot(x="total_bill", y="tip", data=tips)
# Pozitif yönde kuvvetli bir ilişki olduğunu söyleyebiliriz
# Not: default olarak labellar geldi. Matplotlibde bunları vermek zorundaydım. Bu label ları değiştirebiliriz.
#********************************# 
plt.figure(figsize=(12,8))  # NOTE: Seaborn, matplotlib komutları ile birlikte kullanılabiliyor
# 2. yol: plt.rcParams['figure.figsize']=(12, 8)
# 3. yol: sns.set(rc={'figure.figsize':(12, 8)})
sns.scatterplot(x="total_bill", y="tip", data=tips)
#********************************# 
sns.set(rc={'figure.figsize':(12, 8)}, style ="darkgrid")    # Figure boyutları ve arka plan desen tipi
sns.scatterplot(x="total_bill", y="tip", data=tips);
# sns.set ile yaptığımızda figure ün arka planı beyaz yerine grid ve koyu alan geldi. Eğer; 
# .. sns.set(rc={'figure.figsize':(12, 8)}, style="white") kodunu kullansaydık matplotlib gibi görürdük arka planı.
# NOTE: default: style="darkgrid"

#################
# "hue" Parameter
sns.scatterplot(x="total_bill", y="tip", data=tips, hue = "sex");
# hue: Renklerle gruplama yapar. Seçmiş olduğum feature daki kategorilerin sayısı kadar renk atar
# Sol üstte etiketlerde geldi çıktıda(Matplotlibdeki legend)
# Burada total_bill ile tip arasındaki kuvvetli ilişkinin erkeklerde daha kuvvetli diye yorum yapabiliriz

################
# "size" Parameter
sns.scatterplot(x="total_bill", y="tip", data=tips, hue = "smoker", s=200); # s : Grafikteki noktaların boyutlarını değiştirdi

###############
# "style" Parameter
sns.scatterplot(x="total_bill", y="tip", data=tips, s=200, style="sex");
# style: gruplama yöntemlerinden bir tanesi. style="sex" : female çarpı olarak , male: yuvarlak olarak geldi
# Bunu "hue" ile birlikte kullanmak daha mantıklı olabilir. Çıktı böyle karmaşık görünüyor.
#********************************# 
sns.scatterplot(x="total_bill", y="tip",hue ="sex", data=tips, s=200, style="sex");
#********************************# 
sns.scatterplot(x="total_bill", y="tip", data=tips, size="sex");
# male : büyük, female: küçük yuvarlak olarak atıyor. Bu gösterim çok iyi görünmüyor.
#********************************# 
sns.scatterplot(x="total_bill",y="tip", data=tips,hue="day",s=200,style="day");
# Saturday harici diğerlerinin benzer pattern gösterdiğini söyleyebiliriz

#################
# "alpha" Parameter
sns.scatterplot(x="total_bill",y="tip", data=tips,s=200,style= "sex",alpha=None);
# alpha: Grafikteki noktaların saydamlığını kontrol etmemizi sağlıyor. default: None yani "1" . 
# .. NOTE: float değerler almalı.
# "palette" parametresi ile rengi değiştirebiliriz

#################
# Save a seaborn figure
plt.figure(figsize=(12, 8))
sns.scatterplot(x='total_bill', y='tip', data=tips, style='sex', hue='sex', s=100);
# plt.savefig('example_scatter.jpg') 
# jpg formatında dosyanın olduğu klasöre çıktıyı kaydediyor(pdf,png,tif vs de olabilir)

############################################################
# 2.RUGPLOT :  Verinin sıklığının(nerede yoğunlaştığı) dağılımı hakkında bilgi veriyor.
sns.rugplot(x="total_bill", data=tips); # sns.rugplot(tips["total_bill"]) 
# Bunu kdeplot veya displot ile ile kullanmak daha mantıklı olabilir
# İçine tek değişken atmam yeterli
# Noktaların 10-20 arasında yoğunlaştığını görüyoruz.
# y ekseni: default height=0.025
#********************************# 
sns.rugplot(x="total_bill", data=tips, height=0.5)
#********************************# 
sns.kdeplot(x="tip", data=tips) # y:Kitledeki elemanların o değeri alma olasılığı.Yani veride 2 değerinin olma 
# .. olasılığı 0.32 civarında. KDE: kernel density estimation
sns.rugplot(x="tip", data=tips)
# So based on this histogram, you can see that the majority of the tips given are roughly between  1.50𝑎𝑛𝑑𝑗𝑢𝑠𝑡𝑢𝑛𝑑𝑒𝑟 4.
# You see the occasional tip at  9𝑎𝑛𝑑 10. But the majority are in the  1.50− 4 range.
# So you can see how rugplots gives vertical lines horizontally across to plot data.
# Areas where there is great occurrence has great density because the lines are stacked up on each other, giving a thicker appearance.
#********************************# 
sns.displot(x="total_bill", data=tips, kde=True, color="g") # displotla birlikte kde yi çizdirdik
# Burada kde üsttekinden farklı. Elemanın kitlede hangi değeri alacağının tahmini değerleri
sns.rugplot(x="total_bill", data=tips)

############################################################
# 3.DISPLOT
sns.displot(x='total_bill', data=tips) # sns.displot(tips["total_bill"])
# displot: sayısal değişkenin dağılım hakkında bilgi veriyor
#********************************# 
sns.displot(x='total_bill', data=tips, kde=True);

###########################################
# 4. HISTPLOT :  histplot: Sayısal değişkenin dağılımı hakkında bilgi veriyor.
sns.histplot(x="total_bill", data=tips);           # sns.histplot(tips["total_bill"])
#********************************# 
sns.histplot(x="total_bill", data=tips, kde=True);

################
# The Number of Bins in Histogram AND Adding in a Grid & Styles
sns.set(style='whitegrid')                        # This function may be removed in the future.
sns.histplot(x="total_bill", data=tips, bins=30); # bins: temelde x eksenininin aralığını kaç parçaya böleceğimizi gösteriyor

###############
# Adding in Keywords from Matplotlib
sns.displot(data=tips,x='total_bill',bins=20,kde=False,color='red',edgecolor='black',lw=4,ls='--');

###############
# DISPLOT & HISTPLOT
# displot(), a figure-level function with a similar flexibility over the kind of plot to draw
# histplot(), an axes-level function for plotting histograms, including with kernel density smoothing

###########################################
# 5.THE KERNEL DENSITY ESTIMATION (KDE) PLOT : Dataların yoğunluğuna göre Sample dan genel çerçeveyi tahmin etmeye çalışıyor.
# .. Yada değerin veride olma olasılığını çıkartıyor. Yukarıda bahsedildi
########################
# 1-DIMENSIONAL KDE PLOT
sns.kdeplot(x="tip",data=tips)
# sns.rugplot(x="tip", data=tips)   # Yoğunluk nerede diye görmek istersek bunu kullanabiliriz
#********************************# 
sns.kdeplot(x="total_bill", data=tips, clip=[10,20]); 
# clip=[10,20]: matplotlib deki ylim, xlim gibi 10 ile 20 arasını kesip oraya odaklanabilirim

############
# Bandwidth
sns.kdeplot(x="total_bill", data=tips, bw_adjust=0.1); 
# bw_adjust # Bu değeri arttırdığımızda grafiğin görüntüsü pürüzsüz/düzgün(smooth) olur
# Bunu 0.1 deyip hassaslaştırdığımızda verilerin değerlerinin iniş çıkışlarını(daha fazla detaylandığını) görebiliriz
#********************************# 
sns.kdeplot(x="total_bill", data=tips, bw_adjust=0.5, shade = True, color="red");
# shade = True : kde plotun altını dolduracak
#********************************# 
sns.kdeplot(data=tips, x="total_bill", bw_adjust=0.7)
sns.kdeplot(data=tips, x="total_bill", bw_adjust=0.2)

########################
# 2-DIMENSIONAL KDE PLOT : radar çarklar gibi izoip şeklinde bir grafik çıkarıyor
data = pd.DataFrame(np.random.normal(0, 1, size=(100, 2)), columns=['x', 'y'])
data
#********************************# 
sns.kdeplot(x = "x", y = "y", data = data);
# Yorum: x in ve y nin dağılımını görüyoruz örneğin x=0 çizgisi çekersek yukarıya solda ya da sağda
# .. kalan kısma bakıp y nin dağılımını görebiliriz
# Aynı şekilde y=0 çizgisi çekersek sağa doğru yukarıda ya da aşağıda kalan kısma bakıp y nin dağılımını görebiliriz
# Bu grafik bize veriin nerede yoğunlaştığı hakkında da bilgi sunuyor. (x=0 a y=0 etrafında verinin yoğunlaştığı söylenebilir)

###############################################################################################################################
#%% SEABORN - 2.DERS
tips = sns.load_dataset("tips")
tips.head()
###########################################
# 6.COUNTPLOT: Kategorik değişkenin unique değerlerinin count unu grafikte göstermek için kullanılır
# Pandasdaki value_counts() metodunun grafikleştirdiğimizi düşünebiliriz countplotta
tips['day'].value_counts()
plt.figure(figsize=(12,8))
sns.countplot(x="day", data=tips)
#********************************# 
fig, ax = plt.subplots(figsize=(18,12))
ax = sns.countplot(x="day", data=tips)
for p in ax.patches:
    ax.annotate((p.get_height()),(p.get_x()+0.35, p.get_height()+1), fontsize=25)
    
############
# "hue" Parameter
# Optional hard to coding (REMEMBER Matplotlib Session 02)
day = tips.groupby("day").sum().index   # tips.day.unique()
day_of_total_bill= tips.groupby("day")["total_bill"].sum()
day_tip = np.array(tips.groupby("day")["tip"].sum())
fig, ax = plt.subplots(figsize=(10, 5))
p = np.arange(len(day))
width = 0.20
ax.bar(p - width/2, day_of_total_bill, width, label="total_bill") # p - width/2: The x coordinates of the bars
ax.bar(p + width/2, day_tip,           width, label="tip")        # .. Try:  p = np.array([10,20,22,25]) (3 satır üstteki p yerine)
ax.set_xticks(p)                      # X eksenindeki yazıların pozisyonları # Try: ax.set_xticks(np.array([0, 1, 2, 3, 4]))
ax.set_xticklabels(day)               # X exsenindeki yazıların etiketleri. Yazılmazsa p nin aldığı değerler label olarak yazılır
plt.legend()
plt.show()
#********************************# 
# Bunun benzerini seabornda kolayca yapalım
sns.countplot(x="day", data=tips, hue="sex")
#********************************# 
fig, ax = plt.subplots()
ax = sns.countplot(x='day', data=tips, hue="sex")
for p in ax.patches:
    ax.annotate((p.get_height()), (p.get_x()+0.1, p.get_height()+1)) # Parametre isimleri text ve xy 
#.. ax.annotate(text=(p.get_height()), xy=(p.get_x()+0.1, p.get_height()+1))
#********************************# 
ax=sns.countplot(x="day",data=tips,hue="sex")
for i in ax.containers:
    ax.bar_label(i)
#********************************# 
mpg = sns.load_dataset("mpg")
ax = sns.countplot(x="origin", data = mpg)
#for i in ax.containers:
#    ax.bar_label(i)
#********************************# 
sns.countplot(x="model_year", data=mpg)
#********************************# 
sns.countplot(x="model_year", data=mpg, hue="origin")
# Her bir model_year ı origin bazında kıyasladık

###########################################
# 7.BARPLOT : Kategoriye bağlı olarak nümerik değerlerin karşılaştırılması. Default olarak mean ini alır.
# NOTE: Burada şekil üzerindeki siyah çizgi Güven aralığını gösteriyor
sns.barplot(x="sex", y="total_bill", data=tips); # default mean # estimator = np.mean
#********************************# 
sns.barplot(x="day", y="total_bill", data=tips, hue="sex");
#********************************# 
sns.barplot(x="sex", y="total_bill", data=tips, ci='sd'); # default :95 , ci=coinfidence interval,  sd:std sapma
#********************************# 
sns.barplot(x="day", y="total_bill", data=tips, estimator = np.sum);
#********************************# 
sns.barplot(x="day", y="total_bill", data=tips, estimator = np.count_nonzero); # Bunun bir std sapması yok zaten. count unu aldık
#********************************# 
###########################################
# 8.BOXPLOT  # Sayısal değişkenin Q1,Q2,Q3, Outlier gibi değerlerini görmemiz için kullanılır
sns.boxplot(x="total_bill",data=tips)
#********************************# 
sns.boxplot(x="day",y="total_bill",data=tips)
#********************************# 
plt.figure(figsize=(14,5))
sns.boxplot(y="day",x="total_bill",data=tips, hue="sex",orient="h"); # orient="h" : horizontal
# Dikkat burada yerler değişik: y="day", x="total_bill"
#********************************# 
sns.boxplot(x="day",y="total_bill",data=tips, hue="sex")
plt.legend(bbox_to_anchor=(1.05,1), loc=2,borderaxespad=5)
#********************************# 
sns.boxplot(x="day",y="total_bill",data=tips, hue="sex", width=0.5) # width = 0.5 Kutuların genişliği
#********************************# 
df = pd.read_csv("StudentsPerformance.csv")
df.head()
#********************************# 
plt.figure(figsize=(12,6))
sns.boxplot(x="parental level of education", y="math score", data=df, hue="gender", width=0.3)

###########################################
# 9.VIOLINPLOT  # Boxplot ile birlikte kullanılabilen verinin yoğunluğu ve dağılımı hakkında bilgi veren grafik
sns.violinplot(x="time",y="total_bill", data=tips);
#********************************# 
sns.violinplot(x="day",y="total_bill", data=tips, hue="sex");
#********************************# 
sns.violinplot(data=tips, x="day", y="total_bill")
sns.boxplot(data=tips, x="day", y="total_bill")
#********************************# 
plt.figure(figsize=(12,6))
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex",split=True); # split=True: hue daki değerlerin(Male, Female)
# .. ayrı ayrı dağılımlarını gösterdi. Biri violinin solunda, biri sağında
#********************************# 
plt.figure(figsize=(12,6))
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex",split=True, inner=None);
# inner=None : Violinin ortasındaki değerler(Noktalar) gitti
#********************************# 
plt.figure(figsize=(12,6))
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex",split=True, inner="quartile");
# inner=quartile : Violinin ortasındaki Q1,Q2,Q3 değerlerini gösteriyor
#********************************# 
plt.figure(figsize=(12,6))
sns.violinplot(data=tips, x="day", y="total_bill", bw=0.2);
# bw=0.2: Hassasiyeti arttırdık # bw=1 olursa smooth olacak grafik

###########################################
# 10.SWARMPLOT: Verinin nerede yogunlaştığını görebileceğimiz noktalardan oluşan grafik
# Yoğunluğun nerede olduğunu gösteren başka bir grafiktir
sns.swarmplot(x="total_bill",data=tips)
#********************************# 
sns.swarmplot(x="total_bill", y="smoker", data=tips, hue="sex");
#********************************# 
sns.swarmplot(x="total_bill", y="smoker", data=tips, hue="sex", dodge=True);
# dodge=True: Yukarıdaki koddaki grafikleri ayrı ayrı gösterdi
#********************************# 
plt.figure(figsize=(12,6))
sns.swarmplot(x="total_bill",data=tips, size=15) # size default 5

###########################################
# 11.BOXENPLOT (LETTER-VALUE PLOT)
# Çok yüksek miktarda satır içeren dataların kullanılması için kullanılır. Hangi aralıkta datalar nerelerde kullanmak için kullanılır
# Çok kullanılan bir şey değil
sns.boxenplot(x="math score", y="race/ethnicity",data=df);
#********************************# 
sns.boxenplot(x="total_bill", y="day",data=tips);
#********************************# 
###########################################
# 12.LINEPLOT
flights = sns.load_dataset("flights")
flights.head()
#********************************# 
plt.figure(figsize=(20, 6))
sns.lineplot(x='year', y='passengers', data=flights);
# Çizgi etrafındaki gölge güven aralığını temsil ediyor
#********************************# 
f_sum = flights.groupby(["year","month"]).sum()
plt.figure(figsize=(20,6))
sns.lineplot(y=f_sum.passengers, x = f_sum.reset_index().index);
# yolcu sayılarını topladığı için(Sum) bunlar actual değerler bundan dolayı burada bir güven aralığı vermiyor
#********************************# 
f_sum1 = flights.groupby(["year", "month"]).sum().reset_index()
f_sum1
#********************************# 
# Yıllara göre yolcu sayıları
plt.figure(figsize=(20, 6))
sns.lineplot(x=f_sum1.passengers , y=f_sum1.year);
#********************************# 
# pivot_table
flights_wide = flights.pivot("year","month","passengers")
flights_wide
#********************************# 
# Her bir yıla karşılık gelen ay bazında yolcu sayıları 
sns.lineplot(data=flights_wide)
plt.legend(loc=(1.04,0));
#********************************# 
# 2. yol
sns.lineplot(data=flights, x="year", y="passengers", hue="month")
plt.legend(loc=(1.04, 0));

###############################################################################################################################
#%% LAB DERSI
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import scipy
import warnings
warnings.filterwarnings('ignore')
##################################
print(sns.get_dataset_names())
penguins = sns.load_dataset("penguins")
penguins.info()
penguins.describe()

##################################
# LINEPLOT
sns.lineplot(x='flipper_length_mm',y='body_mass_g',data=penguins);
##################################
# SCATTERPLOT
sns.scatterplot(x='flipper_length_mm',y='body_mass_g',data=penguins);
#********************************# 
sns.scatterplot(x='flipper_length_mm',y='body_mass_g',data=penguins,hue='sex');
#********************************# 
plt.figure(figsize=(12,5))
sns.scatterplot('bill_depth_mm','flipper_length_mm',data=penguins,hue='sex',s=150,style='sex',alpha=0.5,palette='viridis');

##################################
# RUGPLOT
# A rugplot is a graph that places a dash horizontally with each occurrence of an item in a dataset. 
# Areas where there is great occurrence of an item see a greater density of these dashes.
# As such it is analogous to a histogram with zero-width bins, or a one-dimensional scatter plot.
sns.rugplot(penguins.body_mass_g,height=0.25);
#********************************# 
sns.kdeplot(penguins['body_mass_g'])
sns.rugplot(penguins['body_mass_g'],height=0.15);

##################################
# DISPLOT & HISTPLOT
# Displot represents the overall distribution of continuous data variables.
# A histogram is a classic visualization tool that represents the distribution of one or more variables
# by counting the number of observations that fall within disrete bins.
plt.figure(figsize=(15,7))
sns.displot(data=penguins, x='body_mass_g',hue='species',bins=20);
#********************************# 
sns.histplot(penguins.body_mass_g,bins=20);
# sns.histplot(data=penguins, x='body_mass_g',hue='species',bins=20);
#********************************# 
sns.histplot(penguins.body_mass_g,bins=20,color='red',lw=2,ls='--');

##################################
# KDE PLOT
# A kernel density estimate (KDE) plot is a method for visualizing the distribution of observations in a dataset, 
# analagous to a histogram. KDE represents the data using a continuous probability density curve in one or more dimensions.
sns.set(style='whitegrid')
sns.kdeplot(penguins.body_mass_g,clip=[2500,6500]);
#********************************# 
plt.figure(figsize=(8, 4), dpi=150)
sns.kdeplot(penguins.body_mass_g,clip=[2800,6400],bw_adjust=0.2,shade=True,color='red');

##################################
# COUNTPLOT
# A simple plot, it merely shows the total count of rows per category.
penguins.sex.value_counts()
#********************************# 
sns.countplot(penguins.sex);
#********************************# 
plt.figure(figsize=(12,8));
fig,ax=plt.subplots()
ax=sns.countplot(penguins.sex);
for p in ax.patches:
    ax.annotate((p.get_height()),(p.get_x()+.35,p.get_height()+.5));

##################################
# BARPLOT
sns.barplot(penguins.sex, penguins.flipper_length_mm);
#********************************# 
sns.barplot(penguins.sex, penguins.flipper_length_mm,estimator=np.std);

##################################
# BOXPLOT : display distribution through the use of quartiles and an IQR for outliers.
sns.boxplot(x='sex',y='bill_depth_mm',data=penguins);
#********************************# 
plt.figure(figsize=(12,5))
sns.boxplot(x='sex', y="bill_length_mm", data=penguins,hue='species',width=.9);
plt.legend(bbox_to_anchor=(1.1,1),loc=2);

##################################
# VIOLINPLOT
# A violin plot plays a similar role as a box and whisker plot. It shows the distribution of quantitative data
# across several levels of one (or more) categorical variables such that those distributions can be compared.
plt.figure(figsize=(12,5))
sns.violinplot(x='sex', y="bill_length_mm", data=penguins,hue='species');

plt.figure(figsize=(12,5))
sns.violinplot(x='species', y="bill_length_mm", hue='sex',data=penguins,split=True);

##################################
# SWARMPLOT
sns.swarmplot(x='body_mass_g', data=penguins,size=7);
#********************************# 
sns.swarmplot(x='body_mass_g',y='sex', data=penguins,size=7,hue='species');
#********************************# 
sns.swarmplot(x='body_mass_g',y='sex', data=penguins,size=7,hue='species',dodge=True);

##################################
# BOXENPLOT
# It is similar to a box plot in plotting a nonparametric representation of a distribution in which
# all features correspond to actual observations.
sns.boxenplot(x='body_mass_g',y='sex', data=penguins);
#********************************# 
sns.boxplot(x='body_mass_g',y='sex', data=penguins);
# Classic boxplots can have too many outliers and don't show as much information about the distribution. 
# Letter-value plots (boxenplots) start with the median (Q2, 50th percentile) as the centerline. 
# Each successive level outward contains half of the remaining data. 
# So the first two sections out from the centerline contain 50% of the data. 
# After that, the next two sections contain 25% of the data. This continues until we are at the outlier level.

###############################################################################################################################
#%% 5. DERS(Seborn 3. ders)
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import scipy
import warnings
warnings.filterwarnings('ignore') 
import seaborn as sns
import numpy as np

##################################
# 13.CATPLOT
# It allows us to work with categorical values efficiently, and we can
# .. plot the data into eight different types of graphs specified by the kind parameter
# kind: box, swarm, violin
# Kategorik değişkenleri birbiri ile karşılaştırabileceğim plot türü
titanic = sns.load_dataset("titanic")
titanic
#********************************# 
# Her bir class a göre ortalama bilet fiyatları
titanic.groupby("pclass")['fare'].mean()
#********************************# 
titanic.groupby("pclass")['fare'].mean().plot.bar(x="pclass", y='fare');
#********************************# 
titanic.groupby("pclass")['fare'].mean().plot(x="pclass", y='fare', kind="bar"); # 2.yol
#********************************# 
titanic.groupby("pclass")['survived'].count()
#********************************# 
titanic.groupby("pclass")['survived'].count().plot(x="pclass",y="survived",kind="bar")
#********************************# 
ax = titanic.groupby("pclass")['survived'].count().plot(x="pclass",y="survived",kind="bar")
for p in ax.patches: #Bu rectangle oluşturuyor
    ax.annotate((p.get_height()),(p.get_x()+0.2, p.get_height()+2));
#********************************# 
titanic['survived'].value_counts()
titanic[titanic['survived']==1] # Bunu bir df olarak atarsak, Bu 1 lerden oluşan data üzerinde analiz yapabilirim
#********************************# 
sns.catplot(x="pclass", y="survived", kind="bar", data=titanic, estimator=np.sum); # np.count_nonzero: 0 lar haricindekileri say
#********************************# 
sns.catplot(x="pclass", y="survived", kind="bar", data=titanic, estimator=np.sum, hue="sex"); # np.count_nonzero: 0 lar haricindekileri say
#********************************# 
titanic['embarked'].value_counts()
titanic['alone'].value_counts()
sns.catplot(x="alone", y="survived", kind="bar", data=titanic, estimator=np.count_nonzero, hue="sex"); # np.count_nonzero: 0 lar haricindekileri say
#********************************# 
sns.catplot(x="alone", y="survived", kind="bar", data=titanic, estimator=np.count_nonzero, hue="sex"); # np.count_nonzero: 0 lar haricindekileri say
#********************************# 
sns.catplot(x="pclass", 
            y="survived", 
            kind="bar", 
            data=titanic, 
            estimator=np.count_nonzero, 
            hue="sex",
            col="alone",     # alone:  2 unique değişkenim var
            row="embarked"); # embark: 3 unique değişkenim var
#********************************# 
###############
# col parameter
tips = sns.load_dataset("tips")
tips
#********************************# 
sns.catplot(x="day", 
            y="total_bill", 
            kind="bar", 
            data=tips, 
            col="smoker")
#********************************# 
# row parameter
sns.catplot(x="day", 
            y="total_bill", 
            kind="bar", 
            data=tips, 
            col="smoker",row="time")
#********************************# 
sns.catplot(x="day", 
            y="total_bill", 
            kind="bar", 
            data=tips, 
            col="smoker",row="time",estimator= np.count_nonzero);
#********************************# 
sns.catplot(x="day", y='total_bill', kind="box", data=tips);
#********************************# 
sns.catplot(x="day", y='total_bill', kind="violin", data=tips, hue="sex");
#********************************# 
sns.catplot(x="day", y='total_bill', kind="violin", data=tips, hue="sex");
#********************************# 
sns.catplot(x="day", y='total_bill', kind="swarm", data=tips, hue="sex");

##################################
# 14.JOINTPLOT
# kind : scatter, hex, reg, kde
# Hex: scatter daki her bir point i balpeteği olarak gösterir
# reg: Regresyon: Scatter plotta noktalar arasından regresyon doğrusu çizecek
sns.jointplot(x ="total_bill", y="tip", data=tips);
#********************************# 
sns.jointplot(x ="total_bill", y="tip", data=tips, hue="sex");
#********************************# 
sns.jointplot(x ="total_bill", y="tip", data=tips, kind="reg");
#********************************# 
sns.jointplot(x ="total_bill", y="tip", data=tips, kind="hex");

##################################
# 15.PAIRPLOT
# Özellikle EDA da olmazsa olmaz plotlar: 1.Boxplot 2. Pairplot
sns.pairplot(tips);
#********************************# 
sns.pairplot(tips, corner=True);
#********************************# 
sns.pairplot(tips,palette='coolwarm', hue="sex", corner=True);
#********************************# 
sns.pairplot(tips,palette='coolwarm', hue="sex", corner=True, diag_kind="hist"); # Diag_kind: diagonaldeki grafik tiplerin değiştirir

##################################
# 16.PAIRGRID
# Figure oluşturup, sonra subplotları oluşturup sonra hangi grafiklerimi istiyorsam onları mapliyorum altta
g = sns.PairGrid(tips)
#********************************# 
g = sns.PairGrid(tips)
g = g.map(sns.scatterplot)
#********************************# 
g = sns.PairGrid(tips)
g = g.map_upper(sns.scatterplot,color="green")
g = g.map_diag(sns.histplot)
g = g.map_lower(sns.kdeplot, color="red")
#********************************# 
g = sns.PairGrid(tips)
g = g.map_upper(sns.scatterplot,color="green")
g = g.map_diag(sns.histplot)
g = g.map_lower(sns.kdeplot, color="red")
#********************************# 
g = sns.PairGrid(tips,hue="sex",palette="viridis")
g = g.map_upper(sns.scatterplot, linewidth=1,edgecolor="w",s=100)
g = g.map_diag(sns.histplot)
g = g.map_lower(sns.kdeplot)
g = g.add_legend(loc=7)
#********************************# 
# Kategorileri baz alarak sayısal değişkenlerin analizini yapabileceğim plot
g = sns.FacetGrid(data=tips)
#********************************# 
g = sns.FacetGrid(data=tips, col="time",row="smoker")
#********************************# 
g = sns.FacetGrid(data=tips, col="time",row="smoker")
g = g.map(plt.hist, "total_bill")           # matplotlib i seaborn a entegre ettik
#********************************# 
g = sns.FacetGrid(data=tips, col="time",row="smoker")
g = g.map(plt.scatter, "total_bill", "tip") # matplotlib i seaborn a entegre ettik ,
#********************************# 
g = sns.FacetGrid(data=tips, col="time",row="smoker", hue="sex")
g = g.map(plt.scatter, "total_bill", "tip")

##################################
# 17.HEATMAP
# Değişkenler arasındaki korelasyonu gösteren grafik
tips.corr()
#********************************# 
sns.heatmap(tips.corr())
#********************************# 
sns.heatmap(tips.corr(),annot=True, cmap="viridis")
#********************************# 
penguins = sns.load_dataset("penguins")
penguins
#********************************# 
is_NaN = penguins.isnull()
row_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = penguins[row_has_NaN]
rows_with_NaN
#********************************# 
NAN_index = rows_with_NaN.index
NAN_index
#********************************# 
sns.heatmap(penguins.isnull()) # penguins deki missing values ları göstermek istedik

##################################
# 18.CLUSTERMAP : # Hoca: Çok önermiyorum
sns.clustermap(tips.corr(),annot=True)

###############################################################################################################################
#%% Capstone (Bike Store Sharing)
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from pylab import rcParams
sns.set_style("darkgrid")
# import lux
import warnings
warnings.filterwarnings("ignore")
# Set it None to display all rows in the dataframe
# pd.set_option('display.max_rows', None)
# Set it to None to display all columns in the dataframe
pd.set_option('display.max_columns', None)

##################################
# 1.TASK 01 - READING THE DATASET
df0 = pd.read_csv('store_sharing.csv')
df = df0.copy()
df.head()

##################################
# 2.TASK 02 - CHECKING MISSING VALUES & IF THERE ARE SOME DUBLICATE ROWS OR NOT
df.duplicated().value_counts()   # Tekrar eden satırlar var mı yok mu bakıyoruz. Eğer True olsaydı drop etmeliydik
df.isnull().sum()                # Sütunlardaki eksik değer sayısı
df.sample(10)                    # Veride eksik değer yok ama acaba gözden kaçırdığımız bir şeyler var mı diye sample alıyoruz
df["season"].value_counts() # Mevsimlerin unique() değerlerinin saydırılması, aşağıda index ve değerlerini alıp görselleştirelim

##################################
# 3.TASK 03 - PLOTTING THE DISTRIBUTION OF VARIOUS DISCRETE FEATURES ON SEASON-HOLIDAY-WEEKEND-WEATHERCODE
df["season"].value_counts()       # Mevsimlerin unique() değerlerinin saydırılması, aşağıda index ve değerlerini alıp görselleştirelim
df["season"].value_counts().index
df["season"].value_counts().values
#********************************# 
# Pandas ile season value_counts() için bar plot
df["season"].value_counts().plot(kind="bar", x=df['season'].value_counts().index, y=df['season'].value_counts().values);
# df["season"].value_counts().plot.bar(x=df['season'].value_counts().index, y=df['season'].value_counts().values); # 2. yol : 
#********************************# 
fig, ax = plt.subplots()
sns.countplot(x="season", data=df)
for p in ax.patches:
    ax.annotate((p.get_height()),(p.get_x()+0.3, p.get_height()+20)) 
# text : (p.get_height()) , xy=(p.get_x()+0.3, p.get_height()+20)
# text : barların y eksenine karşılık gelen değerinin yazdırılması
# xy   : değerin pozisyonunun ayarlanması    
#********************************# 
fig, ax=plt.subplots()
chart = sns.countplot(x="is_holiday", data=df)
chart.bar_label(chart.containers[0]);            # Değer bulma : OOP de containers parametresini kullanıp barın y ekseninde karşılık gelen değerini bulabiliyoruz
#********************************# 
fig, ax=plt.subplots()
chart = sns.countplot(x="is_weekend", data=df)   # Aynı şeyi is_weekend değişkeni için yaptık
chart.bar_label(chart.containers[0]);
#********************************# 
fig, ax=plt.subplots()
chart = sns.countplot(x="weather_code", data=df) # Aynı şeyi weather_code değişkeni için yaptık
chart.bar_label(chart.containers[0]);
"""
"weather_code" category description:
1 = Clear ; mostly clear but have some values with haze/fog/patches of fog/ fog in vicinity
2 = scattered clouds / few clouds
3 = Broken clouds
4 = Cloudy
7 = Rain/ light Rain shower/ Light rain
10 = rain with thunderstorm
26 = snowfall
94 = Freezing Fog
"""
##################################
# 4.TASK 04 - LOOKING AT THE DATA TYPES OF EACH VARIABLE, TRANSFORM TIMESTAMP IN TYPE & SET IT AS INDEX
df.info() # type ı datetime olması gereken bir sütunu string olarak görüyoruz (timestamp sütunu)
type(df["timestamp"][0])
df["timestamp"] = pd.to_datetime(df["timestamp"]) # Sütunun type ını bu şekilde datetime a çevirebiliriz 
df.info()                                         # Düzeldi
df.set_index("timestamp", inplace=True)           # Bu sütunu index olarak atadık. Tarih sırasına göre analizler yapmak daha mantıklı
# .. olacağı için(Bu veri için)

##################################
# 5.TASK 05 - MAKING FEATURE ENGINEERING. EXTRACTING NEW COLUMNS (DAY OF WEEK, DAY OF MONTH, HOUR, MONTH, SEASON, YEAR ETC.
df.index
df.index.year                      # .year ile sadece yılları görebiliriz
df.index.max() - df.index.min()    # Bu şekilde max ve min arasında kaç gün var bakabiliriz yani datetime da matematiksel
# ... işlemler yapabiliyorduk

f = lambda x: x.strftime("%Y-%m")  # Yıl ve ay ı alan fonksiyonu strftime ile tanımladık ve altta year_month olarak atadık
# Burada feature engineering yapıyoruz. Yani bizim analizimize yardımcı olacak yeni sütunlar oluşturuyoruz
df["year_month"]=f(df.index)
df["year"] = df.index.year
df["month"] = df.index.month
df["day_of_month"] = df.index.day
df["day_of_week"] = df.index.dayofweek
df["hour"] = df.index.hour
#********************************# 
df.info() # Yeni sütunlarımız gelmiş
df.head()

##################################
# 6.TASK 06 - VISUALIZING THE CORRELATION WITH A HEATMAP
df.corr()                         # Sütunların birbirleri ile olan korelasyonuna bakalım
#********************************# 
# Seaborn ile sütunların birbiri arasındaki korelasyonları görselleştirdik
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot = True, cmap = "coolwarm");            # annot=True : Hücrelerin içine çıktıda korelasyon değerlerini yazar
#********************************# 
df_corr = df.corr()[["cnt"]].sort_values(by="cnt", ascending=False) # cnt değişkeninin diğer sütunlar ile olan korelasyonlarını
# .. en yüksekten en düşüğe göre oluşturduk
#********************************# 
# Üstte oluşturduğumuz sütunu seabornda heatmap ile görselleştirelim
plt.figure(figsize=(2, 7))
sns.heatmap(df_corr, annot= True, cmap="coolwarm", vmin = -1, vmax=1) # yandaki(sağdaki) bar ın nerede başlayıp biteceği

##################################
# 7.TASK 07 - VISUALIZING THE CORRELATION OF THE TARGET VARIABLE & THE OTHER FEATURES WITH BARPLOT
# Üstte oluşturduğumuz sütunu pandasta barplot ile görselleştirelim
plt.figure(figsize=(12,8))
df.corr()["cnt"].sort_values().plot.barh()

##################################
# 8.TASK 08 - PLOTTING BIKE SHARES OVER TIME BY USING LINEPLOT
plt.figure(figsize=(15,5))
sns.lineplot(x = df.index, y="cnt", data=df)  # indexlerde tarihler vardı. Bu tarihlere göre cnt sütununun lineplot grafiği
# .. 2015-07 inci ay ve da  the count of a new bike shares 8000 lere ulaşmış o dönemde bir şey olmuş olabilir
# .. kış aylarında diğer aylara nazaran daha az bike shares olmuş gibi 2016 nın ilk ayında ve 2017 ilk ayında düşüş var
# .. demekki christmast zamanlarında bike shares çok kulannılmıyor

##################################
# 9.TASK 09 - PLOTTING BIKE SHARES BY MONTHS & YEAR_OF_MONTH (USE LINEPLOT, POINTPOT, BARPLOT)
df.head()
df_sum = pd.DataFrame(df.groupby("year_month").cnt.sum())  # yıl ve aya göre bike shares toplamlarını alalım
#********************************# 
plt.figure(figsize=(20, 5))
sns.lineplot(x = "year_month" , y = "cnt", data = df_sum)  # yıl ve aya göre bike shares toplamlarını line plotta çizdirelim
plt.ticklabel_format(style="plain", axis= "y")             # style="plain" : y ekseninin gerçek değerlerini vererek yazdırıyor
plt.xticks(rotation=90);
# Yukardakilere benzer yorumlar yapabiliriz burada da
#********************************# 
df_month = df.groupby("month").cnt.sum() # Aylara göre bike shares toplamlarını alalım
df_month

plt.figure(figsize=(20, 5))
sns.lineplot(x = df_month.index, y = df_month.values, data = df_month) # aylara göre bike shares toplamlarını line plotta çizdirelim
plt.ticklabel_format(style="plain", axis= "y")
#********************************# 
plt.figure(figsize=(15, 5))
sns.pointplot(x=df_month.index, y= df_month.values, data = df_month)
#********************************# 
df.groupby("month")["cnt"].mean()            # Aylara göre bike shares lerin ortalamaları
#********************************# 
sns.pointplot(x="month", y ="cnt", data=df); # 7. ayda bike shares kullanımının tavan yaptığını, kış aylarında yine kullanımın
# .. yarı yarıya düştüğünü görüyoruz

# Aynı şeyi barplot için gözlemleyelim
plt.figure(figsize=(14, 6))
sns.barplot(x="month", y ="cnt", data=df, ci= 60)
#********************************# 
plt.figure(figsize=(14, 6))
ax = sns.barplot(x="month", y ="cnt", data=df, estimator = sum, ci = None) # estimator = sum: O aydaki toplam için bir 
# .. tahmin değeri çıkartıyor... ci = None : güven aralıklarını grafikte göstermesin demek
ax.bar_label(ax.containers[0]);

##################################
# 10.TASK 10 - PLOTTING BIKE SHARES BY HOURS ON (HOLIDAYS, WEEKEND, SEASON)
sns.lineplot(x="hour", y= "cnt", data=df, hue= "is_weekend") # Hafta içi kullanımın sabah 7-8 ve akşam 17-18 gibi tavan
# .. yaptığını görüyoruz yani insanlar işe giderken ve dönerken çok kullanmışlar. Hafta sonu genelde saat 11-16 saatleri
# .. arasında kullanımın diğer saatlere göre daha çok olduğu görülüyor
#********************************# 
# Üstteki grafiğin altta mevsimlere göre değişimine bakalım. Mevsimlerin farklı olması kullanım saatlerinde değişiklikler yapmamış yani
# ... insanlar yine işe gidip gelirken daha çok kullanmışlar bike shares i. Yani o pik noktalarının haftaiçinden geldiğini
# .. üssteki grafikten biliyoruz. Haftasonu ayrımı için yorum yapmak doğru olmayabilir burada
sns.lineplot(x="hour", y= "cnt", data=df, hue= "season")
#********************************# 
# ÜStteki yaptıklarımızı tek çıktıda görelim pointplot ile
fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, figsize=(18, 15))
sns.pointplot(data=df, x='hour', y='cnt', ax=ax1)                   # Normal saatlik trend
sns.pointplot(data=df, x='hour', y='cnt',hue="is_holiday", ax=ax2)  # Tatil olup olmamasına göre saatlik trend
sns.pointplot(data=df, x='hour', y='cnt',hue="is_weekend", ax=ax3)  # haftasonu olup olmamasına göre saatlik trend
sns.pointplot(data=df, x='hour', y='cnt',hue="season", ax=ax4)      # mevsim durumuna göre saatlik trend

##################################
# 11.TASK 11 - PLOTTING BIKE SHARES BY DAY OF WEEK
sns.barplot(x = "day_of_week", y = "cnt", data=df, hue="is_weekend") # Hafta içi bike shares kullanımının hafta sonuna 
# .. nazaran daha fazla olduğunu söyleyebiliriz
#********************************# 
# Yukarda yaptığımızı point plot ile gösterelim. Ayrıca mevsimlere haftanın günlerine göre kullanıma pointplot ile bakalım
fig, (ax1, ax2,) = plt.subplots(nrows=2, figsize=(18, 15))
sns.pointplot(data=df, x='day_of_week', y='cnt', ax=ax1)
sns.pointplot(data=df, x='day_of_week', y='cnt',hue="season", ax=ax2)

##################################
# 12.TASK 12 - PLOTTING BIKE SHARES BY DAY OF MONTH
# Yukarıda yaptıklarımızı ayın günlerine göre yapalım.
plt.figure(figsize=(15, 5))
sns.lineplot(x='day_of_month', y='cnt', data=df)
pd.DataFrame(df.groupby('day_of_month').cnt.mean().apply(lambda x: round(x))).T # round(x): virgülden sonrasını aşağı yuvarlar(0 a yuvarlar.Yani direk atar diyebiliriz)
# Çizginin etrafındaki gölge güven aralığını göstermektedir.
# Ayın 9 inde bike share in diğer günlere göre daha fazla olduğu görülmektedir.
# Ayın 31 inde kullanım en az. Bazı ayların 30 çekmesinden dolayı, ayın 31 indeki kullanım sayısının az olduğu söylenebilir
# Günlük bike shares in ortalama 1000 in üzerinde olduğu söylenebilir

##################################
# 13.TASK 13 - PLOTTING BIKE SHARES BY YEAR & PLOTTING BIKE SHARES ON HOLIDAYS BY SEASON
sns.barplot(x="year", y="cnt", data=df) # 2017 deki veri az olduğu için güven aralığının bile share in az olduğunu görüyoruz
# .. Bu sebeple güven aralığı da diğer yıllara nazaran artmış(Hata(std sapma) artmış da diyebiliriz)
# Güven aralığı : x(ortalama) - z(tablo değeri) x std / kök(n) 
# Örn: x(ortalama)=20, z(tablo değeri)=2, std=3, n=100 olsun , güven aralığı : 20 -+ 2x3/10  = (19.4 , 20.6) olacak. Burada
# std = 5 olsaydı ---> 20 -+ 2x5/10 = (19,21) güven aralığının uzunluğu arttı. Yani std sapma(hata) artınca G.A. artar denebilir
#********************************# 
sns.barplot(x="season", y="cnt", data=df) # Mevsimlere göre kullanım # Turuncu olan mevsim(heralde yaz) kullanım daha fazla
# .. kırmızı olan mevsimde(heralde kış) kullanım daha az olduğunu söyleyebiliriz

##################################
# 14.TASK 14 - VISUALIZING THE DISTRIBUTION OF BIKE SHARES BY WEEKDAY-WEEKEND WITH USING PIECHART & BARPLOT
df["is_weekend"].value_counts()
df["is_weekend"].value_counts().values
#********************************# 
# is_weekend için bike share kullanımının pie grafiğine bakalım
fig, ax=plt.subplots(figsize=(5,5))
#********************************# 
explode = (0, 0.1)
ax.pie(x=df["is_weekend"].value_counts().values, labels=["weekday", "weekend"],
      explode=explode,
      autopct="%.1f%%")
plt.show()
#********************************# 
# Alternative Solution
sns.countplot(x="is_weekend", data=df)

##################################
# 15.TASK 15 - PLOTTING THE DISTRIBUTION OF WEATHER CODE BY SEASON
"""weather_code
1 = Clear ; mostly clear but have some values with haze/fog/patches of fog/ fog in vicinity
2 = scattered clouds / few clouds
3 = Broken clouds
4 = Cloudy
7 = Rain/ light Rain shower/ Light rain
10 = rain with thunderstorm
26 = snowfall
94 = Freezing Fog"""

sns.countplot(x="weather_code", data=df) # Hava durumuna göre kullanım sayısındaki değişimleri görüyoruz.
# .. Clear da kullanım en fazla vs gibi bir çok yorum yapılabilir burada...
#********************************# 
sns.catplot(x="weather_code", data=df, kind="count", col="season") # Mevsim kırılımında hava durumuna göre kullanımlar
#********************************# 
df["weather_code2"] = df["weather_code"].astype('O')
# Üstteki grafiği tek bir grafikte görmek istersek hue="season" ekleyip bunu görebiliriz
sns.catplot(x="weather_code2", data = df, kind="count",hue="season")
# NOT: catplotta grafiğin boyutlarını büyütmek için "height" ve "aspect" parametrelerini kullanmalıyız
# sns.catplot(x="weather_code2", data = df, kind="count",hue="season", height=10, aspect=3)

##################################
# NOTE
# Thu Lux is an extra visualization Libarary 
# which is, at the begining of your analysis, beneficial to get first insight about the data before going further.
import lux
# !pip install lux-api
# !jupyter nbextension install --py luxwidget
# !jupyter nbextension enable --py luxwidget



####################################################-----END-----####################################################




