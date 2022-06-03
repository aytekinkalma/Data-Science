import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)

#############################################################################################
#%% MATPLOTLIB
################################
# LINEPLOTS (SERIES/DATAFRAMES)
# A line chart or line plot is a type of plot which displays information as a series of data points 
# .. called 'markers' connected by straight line segments.
x = np.arange(0, 10)
y = 2*x
plt.plot(x,y)              # x ve y nin default olarak "line plot" unu çizecek
plt.show()                 # Grafiğin çıktıda gösterilmesi için kullanılabilir # 2. yol : sonuna noktalı virgül koymak--> plt.plot(x,y);
#********************************# 
x = np.arange(-5,6)
y = x**2
plt.plot(x,y);             # x ve y nin default olarak "line plot" unu çizecek
plt.xlabel("x_label")      # X eksenine isim verdik
plt.ylabel("y_label")      # Y eksenine isim verdik
plt.title("Title");        # Grafiğe başlık verdik
plt.savefig("example.jpg") # Bu notebook un bulunduğu yere plt.plot(x,y) grafiğini jpg olarak kaydetti
plt.savefig("example.png") # Bu notebook un bulunduğu yere plt.plot(x,y) grafiğini png olarak kaydetti
#********************************# 
xpoints = np.array([1, 2, 6, 8,])
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, ypoints);
#********************************# 
age = [25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45]
salary = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
len(age)                   # salary ile  uzunlukları aynı olmalı
len(salary)                # age ile  uzunlukları aynı olmalı
plt.plot(age, salary)      # Default olarak age ve salary nin "line plot" unu çizecek
plt.show()

##################################################
# 2 METHODS USED TO CREATE PLOTS IN MATPLOTLIB
# There are essentially two ways to use Matplotlib: 1.The Object-Oriented, 2.the Pyplot interfaces (Functional)
############################
# 1 - FUNCTIONAL METHOD
salary_2 = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.subplot(2,1,1)             # 2: satır sayısı, 1: sütun sayısı, 1: çizileceği yer(0,1 indexi)
plt.plot(age,salary,"r")       # age ve salary nin default olara "line plot" unu çizecek. color "r"= red
plt.subplot(2,1,2)             # 2: satır sayısı, 1: sütun sayısı, 2: çizileceği yer(1,1 indexi)
plt.plot(age,salary_2,"b");    # age ve salary_2 nin default olarak "line plot" unu çizecek. color "b"= blue

############################
# 2 - OBJECT-ORIENTED METHOD
fig, ax = plt.subplots(2,1)    # 2: satır sayısı, 1: sütun sayısı
ax[0].plot(age, salary,"r")    # 0. index satırına age ve salary line plot u kırmızı renkte çiz
ax[1].plot(age,  salary_2);    # 1. index satırına age ve salary_2 line plot u çiz
#********************************# 
fig , ax = plt.subplots(2,3)   # OOP ile subplot kullanarak nesne oluşturuyoruz. 2 satır 3 sütunluk "figure" oluşturduk
ax[1][2].plot(age,salary)      # Oluşturduğum ax ın 1.index satırı, 2.index sütununda age ve salary için line plot çiz
# ax[1,2].plot(age,salary);    # 2. yol
plt.tight_layout();            # Çıktıda rakamlar üst üste olmaması için tight_layout()
#********************************# 
# Bunu functional ile yapalım
plt.subplot(2,3,1)             # 2: satır sayısı, 3: sütun sayısı, 1: çizileceği yer(0,0 indexi)
plt.subplot(2,3,2)             # 2: satır sayısı, 3: sütun sayısı, 2: çizileceği yer(0,1 indexi)
plt.subplot(2,3,3)             # 2: satır sayısı, 3: sütun sayısı, 3: çizileceği yer(0,2 indexi)
plt.subplot(2,3,4)             # 2: satır sayısı, 3: sütun sayısı, 4: çizileceği yer(1,0 indexi)
plt.plot(age,salary)           # 4 ten sonra bu komutu yazdığımız için grafiği, 4. yere(1,0 indexine) çizdi 
plt.subplot(2,3,5)             # 2: satır sayısı, 3: sütun sayısı, 5: çizileceği yer(1,1 indexi)
plt.subplot(2,3,6)             # 2: satır sayısı, 3: sütun sayısı, 6: çizileceği yer(1,2 indexi)
plt.tight_layout();
#********************************# 
fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize=(6, 3)) # satır sayısı:1, sütun sayısı:2, grafik boyutları:(6,3)
ax[0].plot(age, salary)        # 0. index sütununa age ve salary line plot u çiz 
ax[0].set_xlabel('age')
ax[0].set_title('First')       # 0. index sütununa başlık verdik
ax[1].plot(age, salary_2)      # 1. index sütununa age ve salary_2 line plot u çiz 
ax[1].set_xlabel('age')
ax[1].set_title('Second')      # 1. index sütununa başlık verdik
plt.tight_layout()

#############################
# Multiple-Line in the Same Graph
salary_2 = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(age, salary, label= "Salary1")  # label: Bunu grafik üzerindeki legend da görünecek şeyi yazıyoruz
plt.plot(age, salary_2, label= "Salary2")
plt.xlabel("age")
plt.ylabel("salary")
plt.title("Salary by Age")
plt.legend()                             # Grafik üzerinde dikdörtgen şeklinde yapı oluşturur ve plot içinde verdiğimiz labelları gösterir
plt.show()
#********************************# 
x = np.arange(0, 11)
y = x.copy()
z = x*2
t = np.log(x)
fix , ax = plt.subplots()
ax.plot(x,y)
ax.plot(x,z)
ax.plot(x,t)
ax.set_xlabel("x")
ax.set_ylabel("y or z")
ax.set_title("title");
#********************************# 
fig = plt.figure() 
ax1 = fig.add_axes([0.0, 0.0, 1, 1])     # Grafik pozisyon bilgisi: ax = fig.add_axes([left, bottom, widht, height]), # (range 0 to 1)
ax2 = fig.add_axes([1.3, 0.3, 0.4, 0.4])
ax1.plot(age, salary, "r")
ax1.set_xlabel("Age")
ax1.set_ylabel("Salary")
ax1.set_title("Salary by Age")
ax2.plot(age, salary_2, "b");
ax2.set_xlabel("Age")
ax2.set_ylabel("Salary_2")
ax2.set_title("Salary_2 by Age");
plt.show()

############################
# Subplot
# FUNCTIONAL
plt.subplot(2, 1, 1)
plt.plot(age, salary, "r")
plt.subplot(2, 1, 2)
plt.plot(age, salary_2, "b")
plt.show()

# OOP
fig, ax = plt.subplots(2,1)
ax[0].plot(age, salary , "r")
ax[1].plot(age, salary_2)
plt.tight_layout()

# FUNCTIONAL
plt.subplot(1,2,1)
plt.plot(age, salary, "r")
plt.subplot(1,2,2)
plt.plot(age, salary_2, "g")
plt.tight_layout()

# OOP
fig, ax = plt.subplots(1, 2)
ax[0].plot(age, salary, 'r')
ax[1].plot(age, salary, 'b')
plt.tight_layout()
plt.show()

# FUNCTIONAL 
plt.figure(figsize=(15, 3))
plt.subplot(1, 2, 1)
plt.plot(age, salary, "r+", ls="--")   # r+: kırmızı renkte + işareti yaparak çiz, ls: linestyle
plt.subplot(1, 2, 2)
plt.plot(age, salary_2, "bo", ls=":")  # bo: mavi renkte o işareti yaparak çiz, ls: linestyle
plt.show()

# OOP
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 3))
ax[0].plot(age, salary)
ax[0].set_xlabel('age')
ax[0].set_title('First')
ax[1].plot(age, salary_2)
ax[1].set_title('Second')
ax[1].set_xlabel('age')
plt.tight_layout()
plt.show()

# OPTIONAL
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')
    plt.title(f"Subplot: {i}")
plt.suptitle("This is Functional Matplotlib Subplots Created By For Loop")
plt.tight_layout() 
plt.show()
# NOTE: Adding Text Inside the Plot in Matplotlib : The matplotlib.pyplot.text() function is used to add text 
# .. inside the plot. The syntax adds text at an arbitrary location of the axes. 
# .. It also supports mathematical expressions

#############################
# How to Manipulate Color?
# FUNCTIONAL
plt.subplot(2, 2, 1)
plt.plot(age, salary, "r")
plt.subplot(2, 2, 2)
plt.plot(age, salary_2, "b")
plt.subplot(2, 2, 3)
plt.plot(age, salary, "g")
plt.subplot(2, 2, 4)
plt.plot(age, salary_2, "y")
plt.tight_layout();

# OOP
fig, ax = plt.subplots(2,2)
ax[0,0].plot(age, salary, 'r')
ax[0,1].plot(age, salary_2, 'b')
ax[1,0].plot(age, salary, 'g')
ax[1,1].plot(age, salary_2, 'y')
plt.tight_layout();

###########################
# LINEWIDTH & LINESTYLES & MARKERS & MARKERSIZE & COLOR
#############
# Linewidth
x = np.arange(0, 10)
x

# OOP
fig, ax = plt.subplots(figsize=(12, 6))
fig.suptitle("To change the line width, we can use the `linewidth` or `lw` keyword argument", fontsize=18)
ax.plot(x, x-1, color="r", linewidth=0.25)  # 
ax.plot(x, x-2, color="blue", lw=0.50)      # lw: linewidth
ax.plot(x, x-3, color="red", lw=1)
ax.plot(x, x-4, color="b", lw=10)
plt.show()
# NOTE: suptitle : Figure ün title ı

# FUNCTIONAL
plt.subplot()
plt.plot(x, x-1, color="r", linewidth=0.25)
plt.plot(x, x-2, color="blue", lw=0.50)
plt.plot(x, x-3, color="red", lw=1)
plt.plot(x, x-4, color="b", lw=10)
plt.show()

#############
# Linestyle
plt.plot(range(5), range(5), linestyle='--', drawstyle='steps')
plt.plot(range(5), range(5)[::-1], linestyle=':', drawstyle='steps')
plt.xlim([-1, 5])    # -1 den 5 e kadar x eksenini sınırla
plt.ylim([-1, 5]);   # -1 den 5 e kadar y eksenini sınırla
#********************************# 
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(x, x-1, color="green", lw=3, linestyle=':') # solid 
ax.plot(x, x-2, color="red", lw=3, ls='-.')         # dash and dot
ax.plot(x, x-3, color="g", lw=3, ls=':')            # dots
ax.plot(x, x-4, color="r", lw=3, ls='--')           # dashes
plt.show()
# NOTE: possible linestype options ‘--‘, ‘–’, ‘-.’, ‘:’

#############
# Marker & Markersize
fig, ax = plt.subplots(figsize=(12, 6))
# Use marker for string code
# Use markersize or ms for size
ax.plot(x, x-1, marker='+', markersize=20)
ax.plot(x, x-2, marker='o', ms=20)         # ms can be used for markersize
ax.plot(x, x-3, marker='s', ms=20, lw=0)   # make linewidth zero to see only markers # lw=0 : aradaki line yokoldu
ax.plot(x, x-4, marker='1', ms=20)
plt.show()

#############
# Color
color = "#ff00ff" # RGB hex code # Renkler için RGB kodlarını kullanabiliriz

plt.figure(figsize=(15, 5))
plt.suptitle("LineStyles & Markers & Markersize & Color", fontsize=16, y = 1.6) # Figure e atılan başlık, 
# .. y=1.6: y ekseninde yazının yazılacağı hiza(üstteki grafiklerin üst kısmı y=0.9 noktasından başlıyor gibi düşünülebilir)
plt.subplot(2, 2, 1)
plt.plot(age, salary, "r", ls="-", marker="+" , markersize=30)
plt.subplot(2, 2, 2)
plt.plot(age, salary_2, "b", ls="-.", marker="o" , markersize=30)
plt.subplot(2, 2, 3)
plt.plot(age, salary, "g", ls=":", marker="x" , markersize=30)
plt.subplot(2, 2, 4)
plt.plot(age, salary_2, "y", ls="--" , marker="*" , markersize=30)
plt.tight_layout();
plt.show()

############
# Legend
"""
legend location
'best' 0          # best ya da 0 yazmalıyız legend ın yeri için
'upper right' 1   # upper right ya da 1 yazmalıyız legend ın yeri için vs
'upper left' 2
'lower left' 3
'lower right' 4
'right' 5
'center left' 6
'center right' 7
'lower center' 8
'upper center' 9
"""
plt.plot(age, salary, label="salary")
plt.plot(age, salary_2, label="salary_2")
plt.xlabel("age")
plt.ylabel("salary")
plt.title("Salary by Age")
plt.legend(loc=9)               # loc=9: Legend ın nerede duracağı(pozisyonu) default "best"
plt.show()
#********************************# 
plt.plot(age, salary, label="salary")
plt.plot(age, salary_2, label="salary_2")
plt.xlabel("age")
plt.ylabel("salary")
plt.title("Salary by Age")
plt.legend(loc='upper center')
plt.show()

#################################################
# How to Plot Range & Add Extra Line
x = np.arange(1, 10)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
ax[0].plot(x, x**2, x, x**3, x, x**4)
ax[1].plot(x, x**2, x, x**3, x, x**4)
ax[1].set_xlim([1, 3])                   # x eksenininde görmek istediğim nokta aralığı(Zoom)
ax[1].set_ylim([1, 50])                  # y eksenininde görmek istediğim nokta aralığı(Zoom)
plt.show()
#********************************# 
x  = np.arange(1, 10)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
ax[0].plot(x, x**2, x, x**3, x, x**4, 'r')
ax[1].plot(x, x**2, x, x**3, x, x**4, 'r')
ax[1].set_xlim([1, 3])                  # x eksenininde görmek istediğim nokta aralığı(Zoom)
ax[1].set_ylim([1, 50])                 # y eksenininde görmek istediğim nokta aralığı(Zoom)
ax[0].axvline(x=5, ls="--")             # 0. index sütununda, x=5 doğrusunu "--" stilinde çizdir 
ax[1].axhline(y=15, ls="--")            # 1. index sütununda, y=15 doğrusunu "--" stilinde çizdir 
ax[1].axvline(x=2, ls="--" , color="r") # 1. index sütununda, x=2 doğrusunu "--" stilinde ve kırmızı olarak çizdir
plt.show()


#############################################
# Some Additional Exercises
# Matplotlib - Subplot2grid() Function
# This function gives more flexibility in creating an axes object at a specific location of the grid. 
# .. It also allows the axes object to be spanned across multiple rows or columns.

# rowspan and colspan: Kolonları ve rowları birleştirerek yapmak
plt.figure()  # Bir çerçeve oluşturduk
a1 = plt.subplot2grid((3, 3),(0, 0), colspan = 2)              # 0,0 indexine gel, 2 kolon kullan (exp)
a2 = plt.subplot2grid((3, 3),(0, 2), rowspan = 3)              # 0,2 indexine gel, 3 tane row kullan(Square)
a3 = plt.subplot2grid((3, 3),(1, 0), rowspan = 2, colspan = 2) # 1,0 indexine gel, 2 satır, 2 kolon kullan(log)
# Toplamda 3x3 = 9 tane boşluk olduğunu düşünürsek figure de, üstüne aşağıdaki şekli yerleştirdik
x = np.arange(1, 10)
a1.plot(x, np.exp(x))
a1.set_title('exp')
a2.plot(x, x*x)
a2.set_title('square')
a3.plot(x, np.log(x))
a3.set_title('log')
plt.tight_layout()
plt.show()

######################################################################################################## 
#%% SPECIAL PLOT TYPES
age = [25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45]

salary = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

salary_2 = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
##############################
# 1.SCATTER PLOT
x = np.array([15, 17, 18, 17, 12, 17, 12, 19, 14, 11, 12, 19, 16, 13])
y = np.array([99, 86, 87, 88, 81, 86, 93, 87, 94, 78, 77, 85, 86, 85])
plt.scatter(x,y);
#********************************# 
y1 = np.random.randint(10, 100, 50)
x1 = np.random.randint(10, 100, 50)
plt.scatter(x1,y1);
#********************************# 
tips = sns.load_dataset("tips")
plt.figure(figsize=(12,8))             # figsize: default 10,6
plt.scatter(tips.tip,tips.total_bill);

##############################
# 2.BAR PLOT
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23, 17, 35, 29, 12]
fig , ax = plt.subplots(figsize=(14,8))
ax.bar(langs, students);
# ax.barh(langs, students);     # Horizontal
#********************************# 
tips.groupby("day").sum()
day = list(tips.day.unique())    # Thur, Fri, Sat, Sun
day_of_total_bill_list = list(tips.groupby("day")["total_bill"].sum())
day_of_total_bill_list
fig,ax = plt.subplots()
plt.bar(day, day_of_total_bill_list);
#********************************# 
day_tip = np.array(tips.groupby("day")["tip"].sum())
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(day, day_of_total_bill_list,  label="total_bill")
ax.bar(day, day_tip, label="tip")
plt.legend();

#######
# Optional
fig, ax = plt.subplots(figsize=(10, 5))
p = np.arange(len(day))   # 0 dan 3 e kadar 1 liste oluşturduk. (X ekseninin pozisyonları)
width = 0.20
ax.bar(p - width/2, day_of_total_bill_list, width, label="total_bill") # day_of_total_bill_list i sola kaydır(width/2 kadar)
ax.bar(p + width/2, day_tip,width, label="tip")                        # day_of_total_bill_list i sağa kaydır(width/2 kadar)
ax.set_xticks(p)
ax.set_xticklabels(day)
plt.legend()
plt.show()

##############################
# 3.HISTOGRAM
x = np.random.randn(250)
plt.hist(x,bins=30)
plt.show()
#********************************# 
plt.hist(tips["total_bill"], bins=30);
#********************************# 
plt.hist(tips["tip"], bins=20);

##############################
# 4.BOX PLOT
x = np.random.normal(170,10,150)
x
plt.boxplot(x);
# plt.boxplot(x, vert=False); # Horizontal
#********************************# 
box = np.array(np.random.rand(10,4))
plt.boxplot(box, labels= ['A','B','C','D'])
plt.show()
#********************************# 
plt.boxplot(tips["tip"]);

##############################
# 5.PIE CHART
plt.figure(figsize=(10, 8))
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels=mylabels, labeldistance=0.7, autopct="%.1f") # autopct="%.1f" : virgülden sonra 1 basamak gelsin
plt.show()
#********************************# 
plt.figure(figsize=(10, 8))
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.1, 0, 0, 0]
plt.pie(y, labels = mylabels, explode=myexplode, labeldistance=None, autopct="%.1f")
plt.legend()
plt.show()
#********************************# 
plt.figure(figsize=(10, 8))
colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0, 0, 0.1, 0.1] # 0 pozisyonunda dilimler pastaya bitişik, 0.1 de dilimler bir adım geriye çekilip ayrı görünüyor
y = np.array([25, 35, 25, 15])
mylabels = ["Banana", "Apples", "Cherries", "Dates"]
plt.pie(y,
        labels = mylabels,
        labeldistance=0.7,    # mylabels ın dilimler üzerindeki konumu
        autopct="%.1f",       # Virgülden sonra 1 basamak yazdır
        startangle=90,        # Pie plot un hangi açıdan başlayacağının belirlenmesi: 90 derece
        shadow=True,          # Figure üzerinde dilimlerin gölgelerini oluşturuyor
        pctdistance=1.1,      # y nin değerlerininkonumu. (pctdistance=1 : dilimin dış hizası)
        colors=colors_list,
        explode=explode_list)
plt.legend()
plt.show()
#********************************# 
# Other way
plt.figure(figsize=(10, 8))
colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0, 0, 0.1, 0.1] # ratio for each continent with which to offset each wedge.
y = np.array([25, 35, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
sizes = [35, 25, 25, 15]
# use a list comprehension to update the labels
labels = [f'{l}, {s:0.1f}%' for l, s in zip(mylabels, sizes)]
plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=mylabels)
plt.pie(y,
        labels = labels,
        labeldistance=0.7,
        startangle=90,
        shadow=True,
        pctdistance=1.1,
        colors=colors_list,
        explode=explode_list)
plt.show()


####################################################-----END-----####################################################




