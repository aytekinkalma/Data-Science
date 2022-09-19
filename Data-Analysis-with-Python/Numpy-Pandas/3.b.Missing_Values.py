import numpy as np
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)


#%% Missing Values
# Buraya kadar numpy, pandas ın temellerini gördük. Şimdi missing values da bunların bazılarını kullanacağız.
# Bu günkü konularımız
# 1.What is Missing Value?
# 2.Types of Missing Values
# 3.Handling with Missing Values
# 4.Some Useful Methods

# Eda dan sonra yapacağımız şey missing values ları handle etmek
# NOT : Çözüm için net metod yok(Veriden veriye değişiklik gösteriyor)
# NaN : Not a Number
"""
index   car_price
1          22.000
2          24.000
3          NaN
4          28.000
5          NaN
"""
# Missing Value neden oluşur?
# 1.Manuel girerken oluşabilir
# 2.Cihazdan alıyorsak veriyi (cihazda hata vs)
# 3.Yanlış ölçümler

#Types of missing values
# 1.Missing completely at random(MCAR)
###.Follow no discernable pattern
###.Cannot be predicted from the remaining know variable
###.Example: data generated explicitly at random or survey data using a random subset
# .. of questions from a pre-defined list
# 2.Missing at Random(MAR)
### Errors with recording the data correctly
### Can roughly be interpolated from remaining values to a reasonable degree of accuracy
### Example: A sensor that misses a particular minutes measurements
# 3.Missing not at random(MNAR)
### Why the data is missing is known
### Can not effectively be inferred or predicted
### Example: people in a certain age/income brackert refuse to answer how many houses or cars they have
# 4.Structurally missing
### The missing data is missing for an apparent reason
### Mechanism that caused the missing data is easily inferred
### Example: a survey  that asks for income from employment would have missing values for those who don't have a job

# Handling with missing values?
# 1.Remove the missing data instances:(This method should be acceptable if there are few missing values and you have a lot of data)
# 2.Imputation methods(This is a common approach it allows most models to function as usual without any modifications)
# 3.Keep the missing values and use model which incorporates them(This methods limits the data. BIZ BUNU KULLANMAYACAĞIZ)

# Alttaki ilk 3 ünü kullanacağız
# 1.Countinuous: mean, median, mode
# 2.Categorical: mode
# 3.Othe Methods: ffill(forward fill), bfill(back fill), interpolate(linspace mantığına benzer dolduruyor)
# 4.Prediction of Missing values(Bir sütunla başka sütun arasında korelasyon varsa diğer sütuna bakarak ML ile tahmin edebiliriz. 
# 5.Using DL(Datawig): Datawig bir kütüphane. Missing value ları doldurma ile alakalı kütüphane

# Example: 3 araba modelimiz var diyelim. Biz araçların eksik değerlerini dolduracağım(Beygir gücü)
# .. Eğer mean ile doldursam mean:200 olsun, bununla doldurayım desem renault yu 200 girersem yüksek olur
# .. audi için doldursam 200 az olur. O yüzden gruplandırma yapacağız ve daha doğru sonuç elde edeceğiz
# .. Bu sefer renault ların ortalamasını alıp boş olan renault u mean ile doldurup, aynı şeyi
# .. audi vs için de yapabilirim.

# The most important point when handling with missing value : DOMAIN KNOWLEDGE
# Yukarda araba örneği bilgi sahibi olduğumuz bir şeydi ama mesela TIP ile alakalı
# .. bir konuda bilgi sahibi biriyle vs konuşup, araştırma yapmalıyız gerekirse

#%%
import numpy as np
import pandas as pd
import seaborn as sns
id_no = ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010", "P011"]
gender = ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M"]
status = ["FT", "PT", "-", "FT", "PT", "PT", "FT", "-", "PT", "FT", np.nan]
dept = ["DS", "FS", "AWS", "AWS", "DS", None, "FS", "FS", np.nan, "DS", "AWS"]
V1 = np.array([2, 3, 5, np.nan, 7, 1, np.nan, 10, 14, "-", 6])
V2 = np.array([8, np.nan, 5, 8, 11, np.nan, np.nan, 2, 3, 7, 9])
salary = np.array([np.nan, 54, 59, 120, 58, 75, None, 136, 60, 125, np.nan])

df = pd.DataFrame({"id" : id_no,"gender": gender,"status": status,"dept": dept,"var1" : V1,"var2" : V2,"salary" : salary})
df

# Not: Yukarda çıktıda bazı değerler "NaN", bazı değerler "nan" şeklinde görünüyor Bunun neden o arrayde "-" olduğu için object 
# .. olarak aldı veritipini ve "nan" yazdı v2 dekiler de integerlar var o yüzden "NaN" yazıyor

#############################################
# Bazı Notlar
print(0 * np.nan)               # nan
print(np.nan == np.nan)         # DIKKAT: False
print(np.inf > np.nan)          # False
print(np.nan - np.nan)          # nan
print(np.nan + np.nan)          # nan
print(np.nan - 10)              # nan
print(np.nan + 10)              # nan
print(np.nan in set([np.nan]))  # DIKKAT: True
print(np.nan is np.nan)         # DIKKAT: True

#############################################
# Type of NaN Values
# Verimizi önce bir inceleyelim
df.info() # Yukarda görünen non-null değerleri doğru mu kontol edelim # Çünkü bazı yerde NaN yazar ama o stringtir görünmüyordur vs
# NOT: type(np.NaN)    # float gelecek
type(np.nan)           # float NOT: Default değeri float
type(np.NaN)           # float
type(None)             # NoneType # NOTE: Bazı yerlerde "None" yazmak veri tiplerinden dolayı o sütunu
# .. doldurmaya çalışırken hata döndürebilir. O yüzden "None" ları "np.NaN" a çevirmeniz gerekebilir
df.salary              # Burada dtype: object, NaN değerler olduğu için kapsayıcı görevinde o yüzden object görünüyor
type(df.salary[0])     # float
type(df.salary[6])     # NoneType
type(df.salary[1])     # int

df.status
type(df.status[2])     # str
type(df.status[10])    # float #Liste içerisindeki elemanlar kendi dtype larını koruyabilir o yüzden float geldi
# .. ama array de durum farklı olacak çünkü array tek tip veri tutuyordu(En kapsamlısını tutacak array)

df.var1
type(df.var1[3])       # DIKKAT: str(Normalde floattı ama string ifade var 9. indexte o yüzden string yaptı)
# .. Ama array için böyle, liste olsaydı dtype float gelecekti(Üstte bahsetmiştik)


#############################################
# Detecting Missing Values
# Missing values ları tespit etmeden önce verimizi hatırlayalım
df
df.isnull()                       # 2. yol: df.isna()  #  Null olanlar # NaN/nan/None olan değerleri "True", olmayanları "False" 
df.notnull()                      # 2. yol: df.notna() # Null olmayanlar # NaN/nan/None olan değerleri "False", olmayanları "True"
df.isnull().any()                 # DEFAULT axis=0 # Herhangi bir sütunda Null değer var mı gösteriyor
df.isnull().any(axis=1)           # Sütunlar boyunca satır bazında bakıyor. Örn; 0. indexteki satırda null değer var mı? --> True
df.isnull().sum()                 # DEFAULT axis=0 # Satır bazında bakıp sütunlarda kaç tane null değer var gösteriyor
df.isnull().sum().sum()           # Tüm dataframe de kaç tane null değer var gösteriyor
df.salary.isnull()                # Seriye isnull uyguladık # Salary sütunu için satır satır null olup olmadığını gösteriyor 
df.salary.isnull().any()          # Salary sütununda null değer var mı gösteriyor
df.salary.isnull().sum()          # Salary sütununda toplam kaç tane null değer olduğunu gösteriyor
df.isnull().sum()/len(df)*100     # Sütunların yüzde kaçı null gösterir.
df[df.isnull().any(axis=1)]       # True olan satırları alarak, sütunları(axis=1) getirsin
df[~df.isnull().any(axis=1)]      # Tilda işareti :Kendisinden sonra gelenin tam tersini yap("NOT" anlamında)
# DIKKAT: V1 sütununda 3. indexi nan görmüyor, string ile alakalı bir durum(6. index NaN olarak görünüyor)(Arrayde veritipiyle alakalı)
df.loc[df.dept.isnull(),"salary"] # dept sütununda boş olan yerlere denk gelen satırlardaki salary leri getirdi

##########################################
# Converting Inappropriate Values to NaN Values
# map() , replace()
df['var1'].map({"-":np.nan}) # Belirtmediğim ne kadar yer varsa hepsini NaN a çevirdi
# .. Bunun çözümü için "replace" kullanmalıyız

df["var1"].replace(to_replace="-",value=np.nan)                 # tireyi NaN a çevirdik. dtype:object
# NOT: df["var1"].replace(to_replace=["-","nan"],value=np.nan)  # nan yazan yerleri de böyle "NaN" a çevirebiliriz
df["var1"].replace(to_replace="-",value=np.nan).astype("float") # Eğer arada object değer kaldıysa, bu kod hata verir
df["var1"]                                                      # Kalıcı olmadı.
df["var1"] = df["var1"].replace(to_replace="-",value=np.nan).astype("float")

df.status
df["status"] = df["status"].replace("-",np.nan)  # Buradaki tireleri NaN a çeviriyoruz(Kalıcı olarak)
df["status"]                                     # dtype: Object. Buranın Object kalmasında problem yok çünkü sütun zaten stringlerden oluşuyor
df

df["gender"].map({"M":1,"F":0})           # male(M) ler yerine 1, female(F) yerine 0 verelim.
df["gender"].replace({"M":1,"F":0})       # 2. yol Aynı sonuç gelecektir
df["gender"].replace(["M", "F"], [1, 0])  # 3. yol  # Not: Bu 3 yolda "gender" sütununu "dummy" değişken yaptık aslında

###############################################
# Missing Value Handling Methods 
"""
Deleting (Dropping) Rows ----->if it has more than 70-75% of missing values
Replacing (Filling) With Mean/Median/Mode (Imputation)--->can be applied on a feature which has numeric data
Assigning An Unique Category--->If a categorical feature has definite number of classes, we can assign another class
Predicting The Missing Values---> we can predict the nulls with the help of a machine learning algorithm like linear regression
Using Algorithms Which Support Missing Values--->KNN is a machine learning algorithm which works on the principle of distance measure.
.. This algorithm can be used when there are nulls present in the dataset. KNN considers the missing values by taking the majority of 
.. the K nearest values
"""
###############################
# 1 - Dropping
# dropna() , drop()
# df in herhangi bir satırında bir tane bile(how="any") NaN varsa bunları drop edelim ve "dropna" nın default argümanlarını kullanalım
# any : If any NA values are present, drop that row or column.
# all : If all values are NA, drop that row or column Source.
df.dropna(axis=0, how="any", thresh=None, inplace=False) # Satırlara göre yaptık
df.dropna(axis=1, how="any", thresh=None, inplace=False) # Sütunlara göre yaptık
df.dropna(axis=1, how="all", thresh=None, inplace=False) # Hepsi("all") NaN ise drop et.(Burada hiç bir sütunda tüm değerler NaN değil)
df["delete_me"] = np.nan # Hepsi nan lardan oluşan sütun
df
df.dropna(axis=1, how="all", thresh=None, inplace=True) # inplace=True olsun
df

# thresh=N requires that a column has at least N non-NaNs to survive.
df.dropna(axis=1, how="all", thresh=9, inplace=False) # 9 ve fazla NaN olmayan değer varsa, o sütunu drop etme. 
# NOTE: Burada how="all" u gözardı ediyor . how="any" yazsak bir şey değişmez. Önce thresh i baz alır sonra how

df.drop([1,3,5])                          # index numaralarına göre drop etmek istersem; Satırları drop etti
# df.drop(["var1","var2"])                # HATA . axis belirtmeliyim
df.drop(["var1","var2"], axis=1)          # DIKKAT Kalıcı yapmıyoruz şu an bunları
df.drop(columns=["var1","var2"], axis=1)  # Kalıcı

###############################
# 2 - Filling Missing Values (Imputation)
df

#####################
# a.Filling with a specific value
df.fillna(0)      # NaN gördüğü tüm değerleri 0 ile dolduracak.NOTE: ilgili sütunun veri tipine göre doldurdu
df.var1.fillna(0) # Sadece var1 sütunu için  NaN gördüğü değerleri 0 ile dolduracak

#####################
# b.Filling with any Proper Value
# Biz sabit bir değer ile doldurduk, başka değerlerle doldurmaya bakalım
df.var1.mean()                 # 6.0
df.var1.fillna(df.var1.mean()) # var1 in NaN değerlerini var1 in mean i ile(6.0 ile) doldur
df.mean()                      # Sayısal sütunların ortalamalarını verdi
df.fillna(df.mean())           # Sütunlardaki boşlukları o sütunun ortalamasına göre doldurdu. Çok kullanılmıyor
df.fillna({"dept":"other","var1":df.var1.mean(), "var2":df.var2.median()}) # dept sütunundaki NaN lara "other" dedik, 
# .. var1 deki NaN ları var1 in mean i ile, var2 deki NaN ları var2 nin median ı ile doldurduk

############
# where() Replace values where the condition is False
# Where ile atama yaparken False olan yerlere atama yapacağız
df.notna()                                           # Bunu altta "condition" olarak koyacağız
df.where(cond = df.notna(), other=df.mean(), axis=1) # Condition da False gördüğü yerlerde ilgili sütunların ortal. göre atama yaptı
# NOT: Bu çok kullanılmıyor. fillna daha çok kullanılıyor

############
# Fill NaN values using an interpolation method
df.interpolate() # Orjinal df de var1 de 3. index NaN dı. 2. indexteki değeri : 5, 4.indexteki değeri:7, ortalamasını aldı ve
# .. 3. indexe :6 dedi vs vs interpolate bunu yapıyor
# .. salary de bunu neden yapmadı? "None" type olduğu için yapmadı. Ders başında "None" tipin sıkıntı çıkarabileceğini not almıştık
# .. salary nin 0. indexinden önce değer olmadığı için atama yapamadı ve 
# .. salary nin 10. indexinden sonra değer olmadığı için atama yapamadı

#####################
# c.Filling the Missing Values of Categorical Variables
df.dept.mode()                     # Mode değeri 1 den fazla verdi. Çözüm için indexleme yapacağız
df.dept.mode()[0]                  # Hepsini AWS(0. indexe karşılık gelen değer) ile dolduracak
df.dept.fillna(df.dept.mode()[0])  # 5. ve 8. indexi "AWS" ile doldurdu
df["dept"].fillna(method="ffill")  # Yukardan aşağı dolduruyor. 4. indexte DS olduğu için, 5. indexi de DS ile doldurdu
df["dept"].fillna(method="bfill")  # Aşağıdan yukarı dolduruyor. 9. indexte DS olduğu için, 8. indexi de DS ile doldurdu.

# Not: method un eşitine ;
# 1.pad / ffill: propagate last valid observation forward to next valid
# 2.backfill / bfill: use next valid observation to fill gap
# NOTE: oranı bozmayayım benim kategorik değişkenimin dağılımı değişmesin dersek bu ffill ve bfill i kullanabiliriz
# NOTE: NaN değerler başta ve sonda ise önce bfill sonra ffill ya da önce ffill sonra bfill yapacak şekilde oraları doldurabiliriz

#####################
# d.Filling by condition & by Group of the Categorical Variables
df
df.dept.fillna(method="ffill",inplace=True) # Kalıcı olarak "dept" sütununu dolduralım
df
# Let's fill the missing values at "status" column with defined condition by "salary"
df.loc[df["salary"]>=100, "status"]         # Maaşı 100000 dolardan fazla olan statuslar
# Bu çıktıya bakarak buradaki(7.index) NaN ı FT olarak doldurabilirim diyorum
df.loc[df["salary"]<=100, "status"]         # Bu çıktıya bakarak da NaN değer PT dır diyorum

df.loc[df["salary"]>=100, "status"].fillna(df.loc[df["salary"]>=100, "status"].mode()[0], inplace=True) 
#..  condition a denk gelen değerleri yine o condition a denk gelen yerlerin mode u ile dolduruk
# .. (Not: mode()[0] yerine mode() yazılsa da olur)
df.loc[df["salary"]<100, "status"].fillna(df.loc[df["salary"]<100, "status"].mode()[0], inplace=True)
df # status de NaN değerler var hala. Olmadı. Neden? loc la bir doldurma yapacaksanız "inplace=True" çalışmaz
# .. inplace çıkaralım ve conditiona alttaki değişikliği eşitleyeceğiz

df.loc[df["salary"]>=100, "status"] = df.loc[df["salary"]>=100, "status"].fillna(df.loc[df["salary"]>=100, "status"].mode()[0])
df.loc[df["salary"]<100, "status"] = df.loc[df["salary"]<100, "status"].fillna(df.loc[df["salary"]<100, "status"].mode()[0])
df
# NOTE: salary de son indexteki değer "NaN" ve status te de o index "NaN" olduğu için orası(status son index) NaN olarak kaldı
# Bunu transform metoduyla ile çözeceğiz birazdan

# Let's fill the last missing value at "status" column with the mode of the group of "gender" and "dept"
# df.groupby(["gender","dept"])["status"].mode()                           # HATA
df.groupby(["gender","dept"])["status"].apply(lambda x:x.mode()[0]) 
df.groupby(["gender", "dept"])["status"].transform(lambda x : x.mode()[0]) # Üstteki çıktıya bakarak F-AWS gördüğü yere FT 
# F-DS gördüğü yere FT vs vs yaptı. Bunu yeni bir sütun olarak ekleyelim

df["trans_status"] = df.groupby(["gender", "dept"])["status"].transform(lambda x : x.mode()[0])
df
df.status.fillna(df.trans_status, inplace=True)
df

# Let's fill the missing values at "salary" column with the mean of the group of "status" and "dept"
df.groupby("dept").salary.mean()              # Bu değerlerle veriyi doldurmak mantıklı olmayabilir ama;
df.groupby(["status", "dept"]).salary.mean()  # status te FT , dept te DS gelen yerlerin salary ye karşılık 
# .. gelen değerlerinin ortalamasını aldık.
# Bunu transform da sütun oluşturmak için kullanıp sonra o oluşturduğumuz sütunu salary deki NaN değerleri doldurmak için kullanacağız
df

df.groupby(["status", "dept"]).salary.transform("mean") # Yeni bir seri oluşturduk. Bunu da ayrı bir sütun yapalım
df["trans_salary"] = df.groupby(["status", "dept"]).salary.transform("mean")
df # Yukarıdaki yaptığımızla aynı mantıkla 125.0 i salary nin ilk değerine verecek, 136.0 yı salary de "None" yazan yere verecek vs vs
df.salary.fillna(df.trans_salary, inplace=True)
df

####################################################-----END-----###################################################


