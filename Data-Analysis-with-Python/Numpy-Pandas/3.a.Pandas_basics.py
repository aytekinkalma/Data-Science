import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)

#%% PANDAS BASICS
# Pandas series is a one-dimensional data structure
# Bir kaç seri bir df oluşturabilir
# Nasıl bir pandas seri oluşturabiliriz
# pandas.Series(data=None, index=None, ...)
# You can create a series by calling pandas. Series() . 
# .. A list, numpy array, dict and scalar value can be turned into a pandas series.

######################################################################################################################
#%% CREATING A PANDAS SERIES
labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {'a': 10, 'b': 20, 'c': 30}
pd.Series(labels)
pd.Series(my_list)
pd.Series(arr)
pd.Series(data = arr, index=labels) # Data uzunluğu ile index uzunluğu aynı olmalı
# pd.Series(data = arr, index=["a","b","c","d"]) # Hata
pd.Series(d)
pd.Series(d, index = ["aa","bb","cc"]) ## NaN değerler geldi
pd.Series(data="deneme")
pd.Series(data="deneme", index= range(5))
pd.Series(data=10, index=["a","b","c"])
# Liste, array ,dictionary, scaler value lar ile 4 tane series oluşturma gördük

########################################
# DATA IN A SERIES
# A series is a one-dimensional data structure
# What differentiates the NumPy array from a Series, is that a Series can have axis labels, 
# .. meaning it can be indexed by a label, instead of just a number location.
# It also doesn’t need to hold numeric data, it can hold any arbitrary Python Object
# So important point to remember for Pandas series is 1.Homogeneous data 2.Size Immutable 3.Values of Data Mutable

ser = pd.Series(data = [set, list, dict])
ser[0]([1,3,3,4,4,5])                 # Set in işlevi ne işe onu yaptı.
pd.Series(data=[sum,print,len])       # Python ın built-in fonksiyonları olduğunu söyledi
ser1 = pd.Series(data=[sum,print,len]) 
ser1[1]("hello world")                # print in işlevini yaptı
ser1[2]("hello world")                # len in işlevini yaptı

mix_data = ["ahmet",5 , True, 5.8]
ser2 = pd.Series(mix_data)
ser2
ser2.dtype                            # Object
type(ser2[3])                         # float
mix_data2 = [5 , True, 5.8]
ser3 = pd.Series(mix_data2)
ser3.dtype                            # Object
arr = np.array(mix_data)
arr                                   # Tüm dtypes: string. Array kullanıldığından dolayı

s1 = pd.Series(['a', 'b', 'c', 'd', 'e'])
s2 = pd.Series(np.random.randn(4), name='Daily Returns')

# Series.dtype       It returns the data type of the data.
# Series.shape       It returns a tuple of shape of the data.
# Series.size        It returns the size of the data.
# Series.ndim        It returns the number of dimensions in the data.
# Series.index       Defines the index of the Series.
# Series.keys        Return alias for index.
# Series.values      Returns Series as ndarray or ndarray-like depending on the dtype.
# Series.items       Lazily iterate over (index, value) tuples.
# Series.head        Return the first n rows.
# Series.tail        Return the last n rows.
# Series.sample      Return a random sample of items from an axis of object.
# Series.sort_index  Sort Series by index labels.
# Series.sort_values Sort by the values.
# Series.isin        Whether elements in Series are contained in values.

ser = pd.Series(data = np.random.randint(0,100,7))
ser
ser.dtype
ser.shape
ser.size         # 2. yol len(ser)
ser.ndim
ser.index
ser.keys         # type: method
ser.keys()
list(ser.keys())
ser.values
ser.items        # Hem key ler hem values ları gösterir # type: method
ser.items()
ser.head()
ser.tail()
ser.sample(3)
ser.sort_index(ascending = False)
ser.sort_index(ascending = True).head(7)
ser.sort_values(ascending=True)
ser.isin([54,10,11]) # NOTE: Bu bir condition aslında

ser1 = pd.Series([1, 2, 3, 4], index = ['USA', 'Germany','RF', 'Japan'])
ser2 = pd.Series([1, 2, 5, 4, 6], index = ['USA', 'Germany','Italy', 'Japan', 'Spain'])

ser1.sort_index()             # or ser1.sort_index(ascending=True)
ser1.sort_values()            # or ser1.sort_values(ascending=True)
ser1[3]                       # ser1.values[3]
ser1.index[3]
ser1.index.get_loc("Japan")   # Japan ın lokasyonunu ver # Çok kullanılmıyor
ser1.Japan                    # or ser1["Japan"] # Bu yazim tekniginin(ser1.Japan) ismi "SQL syntex" dir
ser1[2:]
ser1[::-1]                    # Tersten sıralama
ser1 + ser2                   # Indexleri aynı olanları topladı, farklı olanlara birşey yapmadı
ser1.add(ser2,fill_value=1)
ser1*ser2

ser = pd.Series(data = [121, 200, 150, 99], index = ["terry", "micheal", "orion", "jason"])
ser

ser["terry"]
ser[0]
ser[[0,2]]
ser[["terry","orion"]]
ser[:3]              # DIKKAT: rakam kullanınca dahil etmedi "Jason" ı
ser["terry":"jason"] # DIKKAT: "jason" ı dahil etti
ser.value_counts() 
ser.value_counts(normalize=True)

###########################################
# SELECTION WITH CONDITION AND BROADCASTING
"terry" in ser    # DIKKAT: indexe bakıyor. Value değerine bakmıyor
121 in ser.values # DIKKAT: values a bakıyor
ser<100
ser[ser<150]
ser[ser<130] = 140
ser
ser.isin([150])            # bolean ifadeyi condition olarak yazabiliriz(Altta)
ser[ser.isin([150])]
ser[ser.isin([150])] = 125 # bolean ifadeyi condition olarak yazdık
ser

#%% CREATING A DATAFRAME
# Using the list of Data & Columns
data = [1, 3, 5, 7, 9]
pd.Series(data)
df1 = pd.DataFrame(data=data, columns=["column_1"])
df1

# Using a Numpy Arrays
data = np.arange(1,24,2).reshape(3,4)
df2 = pd.DataFrame(data = data, columns = ["var1", "var2", "var3", "var4"])
df2

# Using a Dictionary
s1 = np.random.randint(2, 10, size = 4)
s2 = np.random.randint(3, 10, size = 4)
s3 = np.random.randint(4, 15, size = 4)
s1, s2, s3

mydict = {"var1":s1, "var2":s2, "var3":s3}
df = pd.DataFrame(data = mydict)
df

#########################################
# The Examination of Some Attributes on Data
df.head(2)
df.tail(2)
df.sample(2)
df.columns
df["var1"]
df.value_counts() 
df.value_counts(normalize=True)
df.index
df.columns = ["new1", "new2", "new3"]
df.index = ["a", "b", "c", "d"]
df.rename(columns = {"new1":"aaa", "new2":"bbb"})
df.rename(index = {"a":1, "b":2})
df.shape        # (4,3)
df.shape[1]     # 3
len(df)         # 4
df.size         # 12
df.ndim         # 2
df.values
type(df)
type(df.values)
type(df["new1"])
"new2" in df

##########################################
# Indexing, Slicing & Selection
from numpy.random import randn
'A B C D E'.split()
np.random.seed(101)
df = pd.DataFrame(randn(5, 4), index = 'A B C D E'.split(), columns = 'W X Y Z'.split())
df

df["Y"]                   # dtype: series    # 2. yol df.Y
df[["Y"]]                 # dtype: DataFrame
df[["X", "Y"]]
df["W":"Y"]
df[:][['W', 'Y']]    # Bir fark yok üstteki ile
df[2:4][['W', 'Y']] 
df["A":"C"]
df["A","C"]               # HATA
df["A":"C"]["W": "Z"]     # Yazdığımız sıra ile bize verecek(önce "Y", sonra "W")
df[["Y", "W"]]["A":"C"]   # Aynı sonucu verir

#########################################
# Creating a New Column
df["new1"] = df["W"] * df["X"]         # Yeni bir seri oluşturduk
df["new2"] = df["new2"] = np.arange(5) # Yeni bir seri oluşturduk
df

####################
# Removing Columns
df.drop("new2",axis=1)             # new2 düştü ama kalıcı olmadı içinde "inplace=True" yazmalıyız
df.drop(["new1","new2"], axis=1)   # 2 sütun birden drop etmek istersek böyle yapıyoruz
df.drop(columns=["new1","new2"])
df.drop(columns=["new1","new2"], inplace = True)
####################
# Removing Rows
df.drop("C", axis=0)
df.drop(index="B")
df.drop("E")
df.drop(["B", "D"])

#########################################
# .loc[ ] and iloc[ ] - Selecting Rows and Column

# .loc[] → allows us to select data using labels (names) of rows (index) & columns
# .iloc[] → allows us to select data using index numbers of rows (index) & columns. it's like classical indexing logic

data = np.random.randint(1, 40, size=(8, 4))
df = pd.DataFrame(data, columns = ["var1", "var2", "var3", 'var4'])

df.loc[4]
df.loc[[4]]                           # 4 numaralı satır
df.loc[2:5]                           # DIKKAT 5 dahil. loc ile çalışıyorsak dahil eder
df.loc["d":"g","var2"]
df.loc["d":"g"]["var2"]
df.loc["d":"g"][["var2"]]             # dtype: DataFrame
df.loc["d":"g",["var2"]]              # dtype: DataFrame
df.loc["d":"g"][["var2","var3"]]
df.loc["a","var1"]
df.loc[["a"],["var1"]]
df.loc[["a","c"],["var1","var3"]]     # a dan var1 e a dan var 3 e, c den var 1 e c den var 3 e
df.loc["a":"d"]
df.loc["d","var3"]  

df.index = 'a b c d e f g h'.split()  # indexleri değiştirdik
df.iloc[2:5]                          # DIKKAT 5 dahil değil.
df.iloc[1:4]
df.iloc[2:5,2]
df.iloc[2:5,[2]]
# df.iloc[1:5][[2]]                   # HATA. Buradaki 2 iloc dışında kaldığı için sütun ismi yazmalıyız
df.iloc[1:5][["var2"]]                # Bunu iloc da yapmak isteseydik eğer;
df.iloc[3,2]
   

df = pd.read_csv('test_lab.csv')
df.loc[:, "country": "POP"]           # Bütün satırları al, "country" den "POP" a kadar olan sütunları al( "POP DAHİL")
df.loc[2:6, "country": "POP"]         # 2. indexten 6. indexe kadar al, "country" den "POP" a kadar olan sütunları al("POP DAHİL")
df.loc[:, ('country', 'country isocode', 'year', 'POP')] # Bu 4 sütunu tuple içine koysaydık kod yine çalıştı
df.loc[:, 'country':'POP']            # Tüm satırları al, "country" sütunundan "POP" sütununa kadar olanları al(POP dahil)
df.loc[:, 'country isocode':]         # Tüm satırları al, "country isocode" dan son sütuna kadar al(son sütun dahil)
df.loc[:, :'XRAT']                    # Tüm satırları al, ilk sütundan "XRAT" sütununa kadar al(XRAT dahil)
df.loc[:, ['country', 'year', 'POP']] # Tüm satırları al, ve parantez içinde yazan sütunları al
df.loc[:, ::2]                        # Tüm satırları al, ilk sütundan(ilk dahil) 2 şer sütun atlayarak sütunları al

df.iloc[:, [1, 3, 4]]                 # Tüm satırları al, 1. 3. ve 4. sütunları al
df.iloc[:, 1:4]                       # Tüm satırları al, 1. sütundan 4. sütuna kadar olan sütunları al(4. sütun dahil değil)
df.iloc[:, 1:]                        # Tüm satırları al, 1. sütundan sondaki sütunlara kadar seç(Son sütun dahil)
df.iloc[:, :2]                        # Tüm satırları al, ilk sütundan 2. sütuna kadar olan sütunları seç(2. sütun dahil)
df.iloc[:, -1]                        # Tüm satırları al, son sütunu seç # DIKKAT: Seri olarak geldi

########################################
# Conditional Selection
# One Conditional Statement
df>10             # True-False lardan oluşan df getirdi
df[df>10]         # Seri de bunu yazdığımda sadece ilgili olanları veriyordu. df de yazdığımda
# .. koşulu sağlamayanları NaN verdi. NaN değeri burada float döndürdü
# .. serinin diğer elemanlarıda o yüzden NaN lardan dolayı float olarak döndü
df[df["var1"]>10] # Sütun 1 de 10 dan büyük olan satırlar hangisi ise ona göre filtreleme yapıp df verdi
df[df["var1"]>10]["var2"]   # Sadece var2 sütununu görmek istersek
df[df["var1"]>10][["var2"]] # dtype: DataFrame
df[df["var1"]>10][["var2", "var3"]]

####################
# Two or More Conditional Statements
# df[() & ()]
df[df["var1"]>10 & (df["var2"]<20)]

####################
# Conditional Selection Using .loc[ ] and .iloc[ ]
df.loc[df["var1"]>10 , ["var2", "var3"]]
df.loc[((df["var1"] < 10) | (df["var1"] > 30)), ['var2','var3']] # 2 condition

########################################
# reset_index() & set_index()
df.reset_index()                            # indexi sütuna taşıdı ve indexi 0 dan başlatıp resetledi
df.reset_index(drop = True, inplace = True) # sütuna getitilen indexi düşürdük
df.set_index("var4", inplace=True)          # Sütunu indexe taşımak

########################################
# Multi-Index & Index Hierarchy
# Özellikle data Analyst lerin bu bölüm karşılarına çıkıyor
outside = ['M1', 'M1', 'M1', 'M2', 'M2', 'M2','M3', 'M3', 'M3']
inside = [1, 2, 3, 1, 2, 3, 5, 6, 7]
multi_index = list(zip(outside, inside))
multi_index
hier_index = pd.MultiIndex.from_tuples(multi_index) # Tuple dan multiindex dtype ına çevirdi
hier_index
np.random.seed(101)
df = pd.DataFrame(np.random.randn(9, 4), index = hier_index, columns=['A', 'B', 'C', 'D']) # Bunları normalde groupby vs ile yapacağız
df

df.index.names
df.index.names = ["Group","Num"] # # Bunlara isim atadık
df.index.names
df.index.levels
df.index.levels[1]                      # df.index.levels[0] , df.index.levels[-1]
df.index.get_level_values(0)
df.index.get_level_values(1)
df.index.get_level_values("Group")
df["A"]   # seri verdi(2 index var)
df[["A"]]
df[["A", "C"]]
df.loc["M1"]
df.loc["M1"]
df.loc[("M1",2)]
df.loc[[("M1",2)]]
df.loc["M1","A":"C"]
df.loc["M1":"M2"]
df.loc[("M1",2):("M2",1)]
df.loc["M1":"M2":2]
df.loc[[("M2",3), ("M3",5)]]

#################################################################
#%% WORKING ON IRIS DATA SET
sns.get_dataset_names()        # Seaborn içindeki datasetlerin isimleri
df = sns.load_dataset("iris")  # iris dataset i seaborn kütüphanesi içinden yükledik
df                             # species: Çiçek tipleri , diğer sütunları yaprak tiplerinin uzunluk ve genişlikleri
df.head(3)                     # dataframe de ilk 3 değeri gösterecek
df.tail()                      # dataframe de son 3 değeri gösterecek
df.info()                      # Özet bilgiler geldi.
df.sample(5)                   # dataframe den 5 tane rasgele 5 örnek değer getirdi
df.describe()                  # Sadece nümerik değerlerin betimsel istatistiklerini getirdi
df.describe(include = "all")   # Kategorik veriyi de getirdi burada ama burada include = 'O' dersek, sadece kategorikler gelir 
df.describe().T                # Transpozu ile # df.describe().transpose()
df.corr()                      # Sütunlar arasındaki korelasyonu gösterir matris şeklinde
df.corr()[["sepal_length"]]    # sepal_length sütununun diğer sütunlarla olan korelasyonunu gösterir
df["petal_length"].corr('petal_width') # petal_length ile petal_width arasındaki korelasyon
df.species.unique()                    # dataframe deki species sütunu içindeki unique değerler
df.species.nunique()                   # dataframe deki species sütunu içindeki unique değer sayısı
df.species.values_counts()             # unique değerlerden kaç tane var "species" sütununda gösteriyor
df.species.value_counts(dropna=True)   # Burada NaN value olsaydı ona göre sıralamaya sokacaktı
df.species.value_counts(dropna=True, normalize=True) # Oransal olarak çıktı aldık
df.loc[df.species == "setosa",["sepal_length"]]
df.loc[(df.sepal_length > 4) & (df.sepal_length)<5 ] 
df.loc[(df.species == "virginica") & (df.sepal_length > 4) & (df.sepal_length < 5)] # 3 condition
df.loc[(df.species == "virginica") & (df.sepal_length > 4) & (df.sepal_length < 5), 'sepal_length']
df.sort_values(by="sepal_length", ascending=False) # Sepal length e göre azalan sıralama

######################################################################
#%% GROUPBY ve AGGREGATION
# Groupby
# Çoğu zaman analizlerimizi kategorik verilere göre gruplandırarak yaparız.
# Analistlerin işlerinin %90 ının işi budur aslında. O yüzden aslında biz büyük dataları küçük parçalara bölmüş oluyoruz.
# SQL deki "group by" daki aynı mantık burada da var.
# ÖNEMLİ NOT: groupby dan sonra aggregation metodu yazmamız GEREKLI
# örn: df.groupby('species').sum() # her bir sayısal sütunun "species" daki unique değerlere göre toplamını verecek

# AGGREGATE VEYA AGG (Fark yok) : Birden fazla satırdan bilgi çıkarmak demek aggregate
# Tüm satırlara bakıp tek değer döndürüyorsa bu aggregate metoddur
# Not: describe() bir aggregate metoddur
# Ben tüm df ye hangi aggregation metodları uygulayacağımı söylersem o bilgileri bana verir. örn1: df.agg(['sum','min'])
# Sütun bazında bunu istersem; örn2: df.agg({'A':['sum','min'], 'B':['min',max]}) # dictionary parantezi kullandık
# Diğer bir kullanım ; örn3: df.agg('mean', axis="columns") # Sütunlar bazında  ortalama aldı. 
# .. "columns" yerine "row" deseydim satırlara göre yapacaktı

# count()  ==> Counts non-NA cells for each column or row.
# mean()   ==> Returns the mean of the values over the requested axis.
# median() ==> Returns the median of the values over the requested axis.
# min()    ==> Returns the minimum of the values over the requested axis.
# max()    ==> Returns the maximum of the values over the requested axis.
# std()    ==> Returns sample standard deviation over requested axis.
# var()    ==> Returns unbiased variance over requested axis.
# sum()    ==> Returns the sum of the values over the requested axis.
# idxmin() ==> Returns index of first occurrence of minimum over requested axis.
# idxmax() ==> Returns index of first occurrence of maximum over requested axis.
# corr()   ==> Computes pairwise correlation of columns, excluding NA/null values.

df = pd.DataFrame(np.random.randint(0, 100, size=(7, 5)), 
                  columns=["x1", "x2", "x3", "x4", "x5"])
df

df.count()            # Her bir sütunda kaç tane eleman olduğunu gösterir
df.x1.count()         # x1 de kaç eleman olduğunu gösterir
df.mean()             # Her bir sütunun ortalama değerini gösterir
df.median()           # Her bir sütundaki ortanca(medyan) değerlerini gösterir
df.min()              # Her bir sütundaki minimum değerleri gösterir
df.max()              # Her bir sütundaki minimum değerleri gösterir
df.std()              # Her bir sütundaki std sapma değerlerini gösterir
df.var()              # Her bir sütundaki varyans değerlerini gösterir
df.idxmax()           # df de ilgili sütundaki maksimum değerin hangi indexte olduğunu gösterir
# NOT: idxmax() seriler üzerinde de çalışır
# Not2: df.argmax() yazarsak # Hata .df de argmax çalışmaz AMA;alta bakalım
df.x1.argmax()        # argmax serilerde çalışır(x1 seri üzerinde çalıştı)
df.x1.idxmax()        # idxmax bir seri üzerinde de çalıştı gördüğümüz gibi
df.x1[df.x1.argmax()] 
df[['x1','x2']].std() # Sadece x1 ve x2 sütunlarındaki std sapma değerlerini gösterir
df.sum(axis=0)        # df içindeki sütunları topladı
df.sum(axis=1)        # df içindeki satırları topladı
df.describe()         # Veride sayısal değişkenlerin(Hepsi sayısal aslında burada) betimsel istatistikleri

###################################################
# DataFrame.groupby()
# Başka df ile devam edelim
data = {'Company':['GOOG', 'GOOG', 'MSFT', 'MSFT', 'GOOG', 'MSFT', 'GOOG', 'MSFT'],
        'Department':['HR', 'IT', 'IT', 'HR', 'HR', 'IT', 'IT', 'HR'],
        'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah', 'Tom', 'Terry'],
        'Age':[30, 28, 35, 40, 42, 25, 32, 48],
        'Sales':[200, 120, 340, 124, 243, 350, 180, 220]}
df1 = pd.DataFrame(data)
df1
df1.groupby('Company')                             # Sonuç gelmedi çünkü bir aggregate fonksiyonu kullanmalıyım
df1.groupby('Company').mean()                      # Bu çıktıdan örne: GOOG da çalışanların yaş ort: 33 , maaş ort: 185.75 imiş.
df1.groupby('Company')['Sales'].mean()             # Sadece "Sales" ortalamasını görmek istedik # NOTE: Bunun sonucu bir seri geldi
df1.groupby('Company')[['Sales']].mean()           # Üsttekini df şeklinde almak istersek bu şekilde yazmalıyız
df1.groupby('Company')[['Sales']].count()          # Şirketlerde kaç kişi çalışıyormuş görüyoruz
df1.Company.value_counts()                         # Bu şekilde de şirketlerde kaç kişi çalıştığını görebilirim
df1.groupby('Company')[['Sales']].count()

aaa = df1.groupby(['Company','Department']).mean() # Company ve departmana göre age ve sales değişkenlerinin ortalaması
aaa
aaa.describe()                                              # Betimsel istatistikler
df1.groupby(['Company','Department'])[['Sales']].mean()     # Company ve departmana göre sales değişkeninin ortalamasını aldı
df1.groupby(['Company','Department'])[['Sales']].describe() # Company ve departmana göre sales değişkeninin betimsel istatistikleri
by_comp = df1.groupby('Company')
by_comp.mean()

#####################################################
# DataFrame.agg()
# DataFrame.aggregate(func=None, axis=0, *args, **kwargs)
# Başka df ile devam edelim
df2 = pd.DataFrame({'groups': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
                   'var1': [10, 23, 33, 22, 11, 99, 76, 84, 45],
                   'var2': [100, 253, 333, 262, 111, 969, 405, 578, 760]})
df2

# NOT: dataframe direk aggregation uygulayabiliyoruz
df2.agg(['sum','min'])                            # 2. yol df2.agg([sum, min])
df2[['var1','var2']].agg([sum,min])               # var1 ve var2 2 sütunlarımın toplamını ve min değerlerini getirir
df2.agg({"var1":sum,"var2":min})                  # var1 in toplamı var2 nin min değerini getir
df2.agg({"var1":[sum],"var2":[min]})              # Üsttekini df olarak görmek istersem
df2.agg({"var1":[sum,np.mean],"var2":[min,max]})  # var1 sütununun toplam ve ortalamasını, var2 sütununun min ve max değerlerini getirir

#######################################
# DataFrame.groupby().agg()
df2.groupby('groups').agg({np.min,np.median,np.max})    # Çıktıda amin : array min , amin: array max anlamında
df2.groupby('groups').agg({min,'median',max})           # Bu amax, amin olmasın düzgün göreyim dersek bu şekilde yazabiliriz
df2.groupby('groups').agg({'var1':(min,'max'),'var2':['median','mean']}) # "groups" sütununa(sütunun içindeki unique değerlere) göre 
# .. var1 sütununun min ve max değerleri, var2 sütununun median ve mean değerlerini gösterir
df2.groupby("groups")["var1"].agg([min, max])           # Yukardakinden farklı olarak sadece var1 sütununa göre min max yaptırdım
df2.groupby("groups")[["var1", "var2"]].agg([min, max]) #  Burada "groups" sütununa göre var1 ve var2 nin min ve max değerleri

########################################
# DataFrame.filter()
# Sütun isimlerine ve index isimlerine göre filtreleme yapıyor
# Diğerlerinin yapamadığı ve filter ın yaptığı 2 şey, (1.regex ve 2.like)
# "regex" yazdığınız pattern leri çekmeye yarıyo ve "like" var 
# regex = e$ (NOT: $ işareti son eleman(biten) demek. Yani bu :son elemanı e olanları(e ile biten) getir
# like ='bbi' içerisinde bbi geçen satırları getir
# filter ı groupby ile de kullanabiliriz. Alta bakalım

df2.filter(['groups',"var1"])     # Bu en temel örneğimiz ama burada filter kullanmaya gerek yok --> # 2. yol df2[['groups','var1']]
df2.filter(regex="^var", axis=1)  # Sütun isimlerinden başlangıcı "var" olanları getirdi
df2.filter(like="var", axis=1)    # içerisinde "var" olan sütunları getirdi
df2.filter(like="5", axis=0)      # 5 yazan(içeren) satırı getirdi 

#######################################
# DataFrame.groupby().filter()
df2.groups.unique()                                            # Groups sütununun unique değerleri
df2.groupby('groups').mean()                                   # groups sütununa göre gruplandı ve sütunların ortalamasını al
def filter_func(x):
    return x['var1'].mean() > 39
df2.groupby('groups').filter(filter_func)                      # filter kullanarak fonksiyonu uyguladık
# Groups sütununun unique değerlerine göre grupla, var1 39 dan büyük olan( B ve C grupları) df teki değerleri getir
df2.groupby("groups").filter(lambda x: x["var2"].sum() < 800)  # groups sütununa gmre var2 değişkeninin toplamının 800 den küçük
# .. olan df teki değerlerini getir

#######################################
# DataFrame.transform()
# Transform bizim vereceğimiz fonksiyona göre bir dönüşüm sağlar.
# Bu dönüşümün sonunda df ile AYNI UZUNLUKTA bir df sonuç oluşturur.(seri ise seri)
df2
df_num = df2.iloc[:,1:3]          # df2 den sadece nümerik sütunları alıyorum
df_num
df_num.transform(lambda x : x+10) # Her elemanına git, 10 ekle #  Her bir elemanını transform ettik. # 2. yol df_num+10
df_num.var1.transform(np.sqrt)    # var1 de her bir satırın karekökünü al # 2.yol np.sqrt(df_num.var1) # 3.yol  df_num.var1.agg(np.sqrt)
df_num.var1.transform([np.sqrt,np.exp])

##########################################
# DataFrame.groupby().transform()
df2.groupby("groups")['var1'].mean()                                            # Transform başlığındaki açıklamadaki örnek
df2.groupby("groups")['var1'].transform("mean")                                 # A ya denk gelenlerin ortalaması 36, B, C aynı mantık
df2['var1_mean_transform'] = df2.groupby("groups")['var1'].transform("mean")    # üstteki yaptığımızı sütun olarak ekledik
df2['var1_median_transform']= df2.groupby("groups")['var1'].transform("median") # Başka bir sütun ekledik(fark:median olması)
df2['var1_max_transform']= df2.groupby("groups")['var1'].transform("max")       # Başka bir sütun ekledik(fark:max olması)


###########################################
# Series.apply() & DataFrame.apply()
# En çok kullanacağımız fonksiyonlardan birisi apply
# Belirttiğiniz fonksiyon için for döngüsüyle işlem yaptırıyor
# Series.apply : Serinin her bir elemanına apply içine yazdığımız fonksiyonu uygular
# DataFrame.apply: Vereceğimiz axis(satıra ya da sütuna) e göre işlem yapacağız
# DataFrame.applymap: İçine yazılan fonksiyonu dataframe in her bir elemanına uygular. NOT: Sadece df e kullanılır

df3 = pd.DataFrame({'col1':[1, 2, 3, 4],
                    'col2':[444, 555, 666, 444],
                    'col3':['abc', 'def', 'ghi', 'xyz']})
df3

####################
# Series.apply() , df["col"].apply()
def squared(x):
    return x**2
df3['col1'].apply(squared)                               # col1 sütunundaki(serideki) her elemanın(satırın) karesini aldı
df3['col2'].apply(np.log)                                # col2 sütunundaki(serideki) her elemanın(satırın) logaritmasını aldı
df3['col3'].apply(len)                                   # col3 sütunundaki(serideki) her elemanın(satırın) uzunluğunu verdi
df3['col3'].apply(lambda x: x[0]*3)                      # Col3 satırının ilk indexteki elemanını 3 ile çarptı
df3['col2'].apply(lambda x : 'high' if x>500 else 'low') # col2 deki her bir eleman>500 ise "high", değilse, "low" yazacak
# NOT: Bunlar kalıcı değişikler değil. Bir değişkene eşitlememiz gerekiyor

####################
# DataFrame.apply()
df2 = df2[["groups", "var1", "var2"]]
df2
df_num = df2.iloc[:,1:3] 
df2.apply(np.sum)                    # Her bir sütunu topladı
# df2.apply(np.sum, axis=1)          # Hata, gives an error. Çünkü string ifade ile(groups daki değerler), sayısal ifadeleri toplayamaz
# df_num.apply(np.sum, axis=1)       # Apply ı burada kullanmamıza gerek yok. Aynı sonucu;
df_num.sum(axis=1)                   # .. şeklinde yaparak alabiliriz
df_num.apply(lambda x: x + 2)        # Burada evdeki sensörde her bir değeri 2 birim eksik ölçüyor 
df2.groupby("groups").mean()
df2.groupby('groups').apply(np.mean) # Aynı çıktıyı verdi ama "apply" kullanmaya gerek yok aslında burada

###########################################
# DataFrame.applymap()
# Element wise tüm dataframe de işlem yapıyor
df_num.applymap(lambda x: x*5)         # apply ve applymap burada Aynı işlemi yaptı
df_num.apply(lambda x: x*5)            # apply ve applymap burada Aynı işlemi yaptı. AMA mesela
df_num.applymap(np.sum)                # Bir şeyleri toplayamadı Çünkü element wise işlem yaptığı için sadece o eleman üzerinde çalıştı
df_num.apply(np.sum)                   # Burada sütunlarda çalıştı
df_num.applymap(lambda x: len(str(x))) # Her bir elemanın kaç haneli olduğunu verdi
df_num.apply(lambda x: len(str(x)))    # Çıktıdaki değerlerin nasıl geldiği;
# len(df_num.apply(lambda x: str(x)).values[0])
# len(df_num.apply(lambda x: str(x)).values[1])
# Not: groupby dan sonra applymap direk uygulanamıyor. Hata veriyor. Ama şöyle olabilir
df2.groupby('groups').mean().applymap(np.sum)

"""
Then what is the difference between applymap() & apply() ?¶

applymap() is only available in DataFrame and used for element-wise operation 
.. across the whole DataFrame. It has been optimized and some cases work much faster than apply()

applymap() method only works on a pandas dataframe where function is applied on 
.. every element individually. apply() method can be applied both to series and dataframes 
.. where function can be applied both series and individual elements based on the type of function provided.
"""

##########################################
# Series.map()
# Serideki value ları map eder. Vereceğimiz değerlere göre neyi neyle değiştirmemiz gerekiyorsa değiştirir(map eder)
s = pd.Series(['fox', 'cow', np.nan, 'dog'])
s
s.map('I am a {}'.format)                           # NaN değeri değiştirir
s.map('I am a {}'.format, na_action = 'ignore')     # NaN değeri değiştirmez
df3
df3.col1.map({1:"A", 2:"B"}) # col1 sütunun daki "1" değerini "A", "2" değerini "B". Kullanmadığım değerleri NaN a çevirdi
# NOT: apply : df ve serilerde
#      map :  sadece serilerde
#      apply map: sadece df de
# .. kullanılır

# apply()    is used to apply a function along an axis of the DataFrame or on values of Series.
# applymap() is used to apply a function to a DataFrame elementwise.
# map()      is used to substitute each value in a Series with another value.


##########################################
# .transform() vs .apply()
# Similarties
# Both apply() and transform() can be used to manipulate the entire DataFrame.
# Both apply() and transform() support lambda expression.
# Both apply() and transform() can be used for manipulating a single column.

# transform() bize aggregare sonuç döndürmez. Her halükarda serinin/df uzunluğunda verir bana
# örnek: df.apply(lambda x: x.sum()) sütunları toplarken
# .. bunu transformla denersek hata alırız
# apply() tüm serilere aynı anda ayrı ayrı işlem yaparken transform aynı anda tek bir seriye işlem yapabilir
# df.apply(lambda x:x['B']-x['A'], axis=1) bunu transform yapmaz yine hata alırız
df5 = pd.DataFrame({'A': [1,2,3], 'B': [10,20,30] })
df5
df5.apply(lambda x: x+10)                    # Sütun bazında işlem yapıyor. A sütununu al, hepsine 10 ekle sonra B sütununu al, ...
df5.transform(lambda x: x+10)                # Burada da aynı ama element wiser bazında çalıştı, Önce 1 i aldı 10 ekledi 11 oldu 
# .. sonra 10 u aldı 10 ekledi 20 oldu, ...
df5['B_ap'] = df5['B'].apply(lambda x: x+10) # B_ap : apply uygulanmış hali
df5['B_tr'] = df5['B'].apply(lambda x: x+10) # B_tr : transform uygulanmış hali
# apply     : B sütununu al her bir elemana 10 ekle
# transform : B sütunundaki ilk elemanı al 10 ekle, sonra 2. elemanı al 10 ekle, 3. elemanı al 10 ekle
df5

#########################################
# Differences between .apply() and .transform() when manupulating
# transform() cannot produce aggregated results.
# apply() works with multiple Series at a time. But, transform() is only allowed to work with a single Series at a time.

df5 = df5[['A','B']] # Sadece A ve B sütunlarını alıyorum
df5
df5.apply(lambda x: x.sum())
# df5.transform(lambda x: x.sum())                # HATA .aggregate sonuçlar döndüremiyor transform
df5.apply(lambda x:x['B']-x['A'], axis = 1)
# df5.transform(lambda x:x['B']-x['A'], axis = 1) # HATA Function did not transform Burada 2 tane sütundan bahsedildiği için hata

######################################
# Differences Between .apply() and .transform() when using them in conjunction with groupby()
# transform() returns a DataFrame that has the same length as the input, but apply() cannot
# apply() works with multiple Series at a time. But, transform() is only allowed to work with a single Series at a time.
df6 = pd.DataFrame({'key': ['a','b','c'] * 3,
                    'A': np.arange(9),
                    'B': [1,2,3] * 3})
df6
df6.groupby('key')['A'].sum()                        # Apply ile yaparsam aynı sonucu alırım(Alttaki kodda)
df6.groupby('key')['A'].apply(lambda x: x.sum())
df6.groupby('key')['A'].transform(lambda x: x.sum()) # Transformdan beklediğim sonuç geldi
df6 # df6 üzerinde bakalım bir de
df6.groupby('key').apply(lambda x:x['B']-x['A'])    # key deki (unique) değerlere göre grupladı,sonra A sütununu direk yazdı
# .. en sağa da B-A yı yazdı(Çıktı da bug var :) ) .. Hiyerarşik indexleme gibi çıktı yapıyor.. 1. indexi "key" ,
# ..  2. indexi "A" gibi alıp çıktı veriyor.

#########################################
# pivot() vs pivot_table()
"""
pivot_table()

pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True,
.. margins_name='All', observed=False, sort=True).
Create a spreadsheet-style pivot table as a DataFrame.
The levels in the pivot table will be stored in MultiIndex objects(hierarchical indexes) on the index and columns of the result DataFrme

pivot()
DataFrame.pivot(index=None, columns=None, values=None).
Return reshaped DataFrame organized by given index / column values.
Reshape data (produce a “pivot” table) based on column values. Uses unique values from specified index / columns
to form axes of the resulting DataFrame.
This function does not support data aggregation, multiple values will result in a MultiIndex in the columns.
Differences

Pivot_table is a generalization of pivot that CAN handle duplicate values for one pivoted index/column pair. 
However, pivot() is used for pivoting without aggregation. Therefore, it CANNOT deal with duplicate values for one index/column pair.
Pivot_table will only allow numeric types as "values=", whereas pivot will take string types as "values=".
Pivot_table also supports using multiple columns for the index.
SOURCE
"""
# pivot_table, pivotun genelleştirilmiş hali
# pivot_table duplicate değerler ile başa çıkabiliyor(aggregation function ile)
# pivot_table value parametresinde nümerik sütun vermeliyim,
# pivot will take string(DIKKAT: string kapsayıcıydı) values
# pivot ve pivot_table aynı sonucu verir ama duplicate değer yoksa ya da values da vereceğim değerler nümerikse
# Eğer duplicate değer varsa pivot_table değer döndürür, pivot döndürmez ve pivot bir sürü NaN değer döndürür
data = {'gender':['male', 'female', 'female', 'male', 'female', 'male'],
        'sport':['tennis', 'tennis', 'basketball', 'football', 'voleyball', 'basketball'],
        'status':["professional","professional","professional","amateur","amateur","amateur"],
        'age':[20, 24, 26, 23, 22, 21],
        'height':[185, 172, 175, 178, 182, 196],
        'weight':[83, 58, 62, 80, 65, 90]}

df7 = pd.DataFrame(data)
df7

df7.pivot_table(index = 'gender', columns = 'sport', values = 'age', aggfunc = 'mean')
# NOT: default olarak aggfunc = mean zaten yazmasakta olur
# Aynı görseli pivot ile elde edelim
df7.pivot_table(index = 'gender',columns = 'sport',values = ['age','height','weight'],aggfunc = 'mean')
# Burada da bir sorun yok. Henüz duplicate değer yok burada

df7.pivot(index = 'gender',columns = 'sport',values = ['age','height','weight'])
# aggfunc = 'mean' ı çıkardık çünkü öyle bir parametresi yok "pivot" un
# Aynı sonuç geldi gördüğümüz gibi çünkü duplicate değer yok

# Peki "values" e kategorik değer verirsem ne olur?
df7.pivot(index = 'gender', columns = 'sport',values = 'status') 
# Pivotta "values" e verdiğim 'status' kategorik bir veri olduğu için çalıştı
df7.pivot_table(index = 'gender',columns = 'sport',values = 'status') 
# pivot_table da "values" e verdiğim 'status' kategorik veri olduğu için hiç bir şey döndürmedi. 
# Çünkü pivot_table: ben aggregate kullanıyorum(mean). Ben aggregate i kategorik bir değişkende kullanamam dedi . AMA mesela;
df7.pivot_table(index="gender",columns="sport", values=["status","age"]) # pivot_table sadece kategorik değer olursa kabul etmedi7
# ..  ama hem kategori hem de numerik olunca kategorik değeri yok sayıp sadece numerik değeri yazdırdı
# df7 de 2. indexteki basketball u tennis e çevireceğim duplicate olması için
df7.loc[2,"sport"] = "tennis"
df7
df7.pivot_table(index = 'gender',columns = 'sport',values = ['age','height','weight'],aggfunc = 'mean')
# df7.pivot(index = 'gender',columns = 'sport',values =['age','height','weight']) # HATA.Index contains duplicate entries,cannot reshape
df7.pivot(columns = 'sport', values = ['age','height','weight'])
df7.groupby(['gender','sport']).mean() # Aynısını pivot table ile yapabilirim
df7.pivot_table(index= ['gender','sport'],values= ['age','height', 'weight'], aggfunc='mean')

#########################################
# stack() vs unstack()
# Reshape using stack() and unstack() function in Pandas python: 
# ..Reshaping the data using stack() function in pandas converts the 
# ..data into stacked format .i.e. the column is stacked row wise. 
# ..When more than one column header is present we can stack the 
# ..specific column header by specified the level. unstack() function 
# ..in pandas converts the data into unstacked format Source.

# Why and when should use a stack() and unstack() methods?

####################
# .stack()
# DataFrame.stack(level=- 1, dropna=True)

# Stack the prescribed level(s) from columns to index.
# Return a reshaped DataFrame or Series having a multi-level index with one or more new 
# .. inner-most levels compared to the current DataFrame.
# The new inner-most levels are created by pivoting the columns of the current dataframe:
# if the columns have a single level, the output is a Series;
# if the columns have multiple levels, the new index level(s) is (are) taken from the prescribed level(s) and the output is a DataFrame

df7
df7["level"] = ["high", "high", "low", "high", "low", "low"]
df7

df8 = df7.pivot_table(index=['gender','sport'],columns=["status","level"], values=['age','height','weight'],aggfunc='mean')
df8 # yeni df oluşturmak için pivot_table kullandık üstte

df8.stack(level=-3) # level ın default değeri -1
# -1 :level	high	low	high	low	high	low	high	low	high	low	high	low
# -2 :status	amateur	professional	amateur	professional	amateur	professional
# -3 :age	height	weight
# df8 deki -1 level ını aldı ve index olarak koydu oraya
df8.stack(level=[-1,-2]) # -1 ve -2 deki sütunları indexe geçirdi

####################
# unstack()
# DataFrame.unstack(level=- 1, fill_value=None)
# Pivot a level of the (necessarily hierarchical) index labels.
# Returns a DataFrame having a new level of column labels whose inner-most level consists of the pivoted index labels.
# If the index is not a MultiIndex, the output will be a Series.
# unstack() function pivots a level of the (necessarily hierarchical) index labels, returning a DataFrame having a new level 
# .. of column labels whose inner-most level consists of the pivoted index labels Source.

# NOT: stack te yön sütundan indexe eleman atıyor , unstack te indexten sütuna eleman atıyor
df8
df8.unstack()                           # default -1 leveldeki indexi sütuna geçirdi
df8.unstack(level=-1)                   # -1 leveldeki indexi sütuna geçirdi
df8.unstack(level=-2)                   # -2 leveldeki indexi sütuna geçirdi
# Ben NaN görmek istemiyorum NaN lara - demek istiyorum
df8.unstack(level=-2, fill_value = '-') # -2 leveldeki indexi sütuna geçirdi ve
# .. Orjinal df8 de NaN olan değerleri -(tire) yapmadı, diğerlerine yaptı Eğer unstack missing value üretirse onlara -(tire) atar

####################################################-----END-----####################################################






