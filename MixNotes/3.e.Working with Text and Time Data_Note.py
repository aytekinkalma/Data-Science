import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)

#%% WORKING WITH TEXT DATA
# Pandas provides a set of string functions which make it easy to operate on string data. Most importantly,
# .. these functions ignore (or exclude) missing/NaN values. Almost, all of these methods work with Python string 
# .. functions. So, while studying with the Series Object, convert it to String Object and then perform the operation

# There are two ways to store text data in pandas
# 1."Object"-dtype NumPy array
# 2."StringDtype" extension type
# NOTE: Pandas recommend using StringDtype to store text data

# String Methods --> pandas.Series.str.string_method
# 1.Python built-in string methods
# 2.Pandas string methods
# df["Column_name"].str.split()
# df["Column_name"].str.split().str[0]     # str den sonra split uyguladık sonra tekrar str yazıp 0. elemanını al diyebilirim
# df["Column_name"].str.split().str[0].str.replace("-","&") # Burada da yine araya "str" leri koyarak sıralayabiliriz
# -Return boolean
# -Changing upper/lower case

########################################################################################
# %% STRING METHODS
df = pd.read_excel("text_exercise.xlsx")   # read_excel, read_csv ile aynı görevi xlsx için yapıyor 
df
df.info() # Sıkıntı var gibi veride
# Örneğin age: "-" işareti var ama "NaN" olarak gözükmüyor ve bu durum sütunun tipini "object" e çevirmiş

#######################################################
# LOWER      str.lower()      => Converts a string into lower case
# UPPER      str.upper()      => Converts a string into upper case
# CAPITALIZE str.capitalize() => Converts the first character to upper case
# TITLE      str.title()      => Converts the first character of each word to upper case
# SWAPCASE   str.swapcase()   => Swaps the case lower/upper

# df.staff.lower()        # HATA. Çünkü seri ile beraber python ın built-in lower fonksiyonunu çalıştıramam. Çözüm için str eklemeliyim
df.staff.str.lower()      # Tüm harfleri küçük yaptı
df.staff.str.upper()      # Tüm harfleri büyük yaptı
df.staff.str.capitalize() # Sadece ilk harfi büyük yaptı
df.staff.str.title()      # Kelimelerin baş harflerini büyük yaptı
df.staff.str.swapcase()   # Büyük gördüğünü küçük, küçük gördüğünü büyük yaptı
# Not:Bunlar kalıcı değil. Bunu sütuna eşiletmemiz gerekli. # NOTE: inplace=True YOK burada

####################################################################
# ISALPHA    str.isalpha()    => Returns True if all characters in the string are in the alphabet
# ISNUMERIC  str.isnumeric()  => Returns True if all characters in the string are numeric
# ISALNUM    str.isalnum()    => Returns True if all characters in the string are alphanumeric
# STARTSWITH str.startswith() => Returns true if the string starts with the specified value
# ENDWITH    str.endswith()   => Returns true if the string ends with the specified value
# CONTAINS   str.contains()   => Returns a Boolean value True for each element if the substring contains in the element, else False.

df.job
df.job.str.isalpha()                # Alfabetik değer mevcut olduğunda True
df.age
df.age.str.isnumeric()              # NOTE: Tireyi False döndürdü, Peki nümerik değerler neden NaN geldi
# .. Çünkü elemanlara tek tek bakacak olursak dtype integer gelecek ama sütun tipi objectti.
# ..  Bunu düzeltmek için ne yapmalıyım? age sütununun dtype ını değiştirmem gerekli "string" olarak
df.age.astype("str").str.isnumeric()
df.salary
df.salary.str.isalnum()                 # Sadece harf veya sayılardan oluşanlar True
df.job
df.job.str.startswith("data")           # "data" ile başlayan satırlar True
df.job.str.endswith("per")              # "per" ile biten satırlar True 
df.job.str.contains("data")             # içinde "data" geçenler True   # Not: contains i regex ile de kullanabiliriz
# df.salary.str.contains("[a-z]+")      # içinde "a" dan "z" ye kadar herhangi bir tane harf geçenler geçenler
df.loc[df.job.str.contains("data")]                      # True olanlar satırlar df olarak geldi
df.loc[df.job.str.contains("data"), "department"] ="DS"  # "data" içerenlerin department kısımlarını "DS" e çevirdik
df.loc[df.job.str.contains("data"), "department"] ="IT"  # Eski haline getirdik

####################################################################
# STRIP   str.strip()   => Returns a trimmed version of the string
# REPLACE str.replace() => Returns a string where a specified value is replaced with a specified value
# SPLIT   str.split()   => Splits the string at the specified separator, and returns a list
# FIND    str.find()    => Searches the string for a specified value and returns the position of where it was found
# FINDALL str.findall() => Returns a list of all occurrence of the pattern.
# JOIN    str.join()    => Converts the elements of an iterable into a string

# Salary yi tamamen sayısal hale getirmek istiyorum.(Not:regex le daha kolay)
df.salary.str.strip('""')                     # Hem sağdaki hem soldaki tırnak işaretlerini götürdük 
df.salary.str.strip("\"")                     # 2. yol. \": Tırnakların içindeki tırnağı özel anlamı dışında bir anlamla kullan
df.salary.str.strip("\"").str.rstrip("dolar")                 # "dolar" sadece sağda olduğu için "rstrip" kullanıldı
df.salary.str.strip("\"").str.rstrip("dolar").str.lstrip("$") # "$" işareti sadece solda olduğu için "lstrip" kullanıldı
df.salary.str.strip("\"dolar$")                               # 2. yol
df.salary.str.strip("\"dolar$").replace(",","")               # Virgüller kalkmadı. Çözüm için str kullanmalıyız yine
df.salary.str.strip("\"dolar$").str.replace(",","")
# str.replace: O sütuna gelir her bir string ifade arasında bir substring e bakar. 
# .. O satır komple bir stringti. O string altındaki virgül bir substring tir.
# replace; o sütuna gelir o satırın tamamına bakar. O yüzden değiştiremedi.
# .. tek başına virgülle dolu olan bir satır olsaydı "replace" onu değiştirirdi
df.salary.str.strip("\"dolar$").str.replace(",","").astype("int")                # Son sorun veri tipi. Bunu da int a çevirdik
df["salary"] = df.salary.str.strip("\"dolar$").str.replace(",","").astype("int") # Kalıcı yaptık
df  # "salary" sütunu düzgün sayısal bir ifade oldu artık

# Age sütununa bakalım
df.age.replace("-",np.nan)              # "-" yerin np.nan dedik.
# Bunu str ile yapacak olsaydık bize hata verecekti çünkü np.nan ifadesini string olarak isteyecekti.(Altta)
# df.age.str.replace("-", np.nan)       # "Hata"
# df.age.str.replace("-","np.nan")      # "Hata yok" ama anlamsız böyle bir değişiklik
df["age"] = df.age.replace("-", np.nan) # Kalıcı yaptık
df.staff.str.title()                    # Bazı isimler küçük harfle başlıyor, bazı soyadları komple büyük ya da küçük. Düzelttik

df.staff.str.title().str.split()        # Otomatik olarak boşluklardan böldü. 2 kelimeden oluşan isimleri liste içerisine aldık.
df["first_name"] = df.staff.str.title().str.split().str[0]  # Listenin 0. indexi
df["last_name"]  = df.staff.str.title().str.split().str[1]  # Listenin 1. indexi
df.drop("staff", axis=1, inplace=True)
df

df.job.str.find("developer") # -1 olanlar "developer" geçmeyenler

df.job.str.findall("developer")            # "developer" varsa o satırda o ifadeden kaç tane varsa getirdi
df.job.str.findall("d")                    # "d" varsa o satırda o ifadeden kaç tane varsa getirdi
# NOT: find ve findall çok kullanılmıyor
df.job.str.findall("developer").apply(len) # O ifadeden satırlarda kaç adet olduğunu gösterir

# df e 2 tane sütun ekleyelim
df["skills"] = [[],["Java","C++"],["Python","Tableau","SQL"],[],["React","Django"],["JavaScript","Python"],["R","SQL"],["SQL","Python"]]
df["Skills"] = [[],[],["Python","Tableau","SQL"],[],["React","Django"],["JavaScript","Python"],["R","SQL"],["SQL","Python"]]
df.loc[1, "Skills"] = "Java,C++"
df                        # İkisi arasındaki fark mesela 1. indexte "Java, C++" liste içinde diğeri değil
df.skills.str.join(",")   # Liste içerisinde gördüğü elemanları virgül ile birleştir ve tek bir string haline getir
df.skills.str.join("-")
# NOTE: Buradaki join pandasın join metodu
df.Skills.str.join(",")   # Aynısını diğer(Skills) sütununa yaptık. Çıktı farklı
# .. Bu sefer 1. indexteki her bir ifade arasına virgül geldi.
# .. Bu liste içinde mi değil mi diye tek tek bakmak yerine, çözüm için;
[",".join(x) if type(x) == list else x for x in df.Skills]
df["Skills"]= [",".join(x) if type(x) == list else x for x in df.Skills]

#######################################################################################
#%% DUMMY OPERATIONS - 
# Bir datasetini modele sokmadan önce değerlerimizin hepsi nümerik olmalı
# .. Yani label encoding ve one-hot encoding yaparak kategorik sütunları nümeric sütunlara çevirebiliyoruz.
### get_dummies()
"""
pd.get_dummies(arraylike)
pd.get_dummies(Series)
pd.get_dummies(DataFrames)

Color 
                          Red  Green  Yellow 
Red                   0    1     0      0
Red                   1    1     0      0
Yellow                2    0     1      0
Green                 3    0     0      1
Yellow
"""
df.department # Nominal olduğu için get_dummies uygulayabilirim
pd.get_dummies(df.department)
pd.get_dummies(df.department, drop_first=True)
# Bunu modelin biraz daha hızlı çalışması için drop_first yapmalıyız. Bilgi kaybı olmuyor yani sütunlardan 
# .. hangisi düşerse düşsün(drop olsun) modelin başarısı değişmez("RMSE" veya "Accuracy, Precision, Recall,F1))
df.Skills                                                # Çıktıda virgülle ayrılmış değerler var. get dummies yaparsak;
df.Skills.str.get_dummies(sep=",")                       # Aynı bilgiyi(korelasyona sahip) taşıyan sütunlar oluştu
df.Skills.str.get_dummies(sep=",").add_prefix("Skills_") # Birden fazla sütuna get_dummy yapmak zorunda 
# .. kalırsam, add_prefix() ile o dummy nin hangi sütundan geldiğini görebilirim
df_final = df[["department","job","salary","Skills"]]
df_final

df_final.join(skill_dummy) # df in yanına dummy yaptığımız kısmı ekledik
df_final = df_final.join(skill_dummy)
df_final.drop("Skills", axis=1, inplace=True)             # Skill i dummy yaptığımız için drop ettik
df_final


pd.get_dummies(df_final, drop_first= True)                # Hala kategorik sütunlarımız var onları tamamen alalım get_dummy içine
df_final = pd.get_dummies(df_final, drop_first= True)     # Bunu da df_final a eşitleyip kalıcı hale getirdik
df_final

#%% WORKING WITH TIME DATA
##############################
# pd.to_datetime()
# pd.to_datetime() : String , list_like vs vs gibi ifadeyi time tipine çevirmeyi sağlar(Eğer time a 
# .. dönüştürülebilecek bir halde ise)
# datetime a bir sütunu çevirdikten sonra araya dt koyarsam. Yıl, gün, ay vs yi bana ayrı ayrı çekebilir
"""
date["year"]  = date["year"].dt.year
date["month"] = date["year"].dt.month
date["day"]   = date["year"].dt.day
date["hour"]  = date["year"].dt.hour
date["minute"]= date["year"].dt.minute
"""
# Pandas kendi içerisinde modüllerle bunu yapabiliyor ama ayrıca Datetime module ü var
"""
class datetime date
class datetime time
class datetime datetime   # mikrosaniyeye kadar bilgi gösterir
class datetime timedelta  # parantez içine bilgiler yazıp bunu matematiksel işlemler için kullanabilirim. 
                          # .. Şu kadar gün öncesine git vs gibi
class datetime tzinfo
class datetime timezone

# Sadece class datetime datetime ve class datetime timedelta ı kullanacağız
"""

# strftime() & strptime()
# strftime() : datetime object sonuna .strftime() yazarsam içindeki formattaki ifadeye çevir dersem o formata çevirir ifadeyi
# strptime() : Sadece string bir ifadeyi datetime a çeviriyor. Örneğin : "21 June, 2018" i veriyoruz parantez içine
# .. sonra vermesini istediğim şekilde içerdeki formatı veriyorum o formatta veriyor
# NOT: to_datetime çok daha geniş kapsamlı buradakilere göre

df1 = pd.read_csv("time_exercise.csv")
df1.head()

df1.info() # order_date be entry_date i datetime a çevirmeliyiz
# Siz de çalışmalarınızda bunları datetime a çevirip öyle çalışmalısınız

df1.order_date                 # Bunu datetime a çevirelim
pd.to_datetime(df1.order_date) # Görsel olarak değişiklik yok ama dtype:datetime
# Aynısını diğer sütun içinde yapalım ve kalıcı yapalım bir değişkene atayarak
df1["entry_date"] = pd.to_datetime(df1["entry_date"])
df1["order_date"] = pd.to_datetime(df1["order_date"])
df1.info() # Veri tipi datetime olmasına rağmen max,min vs gibi değerleri görebilirim
df1.entry_date.min()
df1.entry_date.max()
df1.entry_date.max() - df1.entry_date.min() # Bunlar arasında matematiksel işlemler yapabilirim

a = pd.Series(["15-03-2020", "18-05-2019", "24-07-2018"]) # Bir seri oluşturalım ve stringlerde max, min deneyelim
a
a.max() # Bu sütun maximum u değil .. ASCI kodlarına göre hangisi büyükse onu aldı
# String ifade üzerinde sonuç alabilirsiniz ama bu size sıkıntı çıkartacaktır
# a.max() - a.min() # Hata . dtype:String olduğu için

pd.to_datetime(a,format="%d-%m-%Y") # Gönderdiğim string ifadeyi formatta yazdığım şekilde yazdır ve datetime a çevir

##############################
###### Series ######
# Datetime a çevrilmiş datalarımız üzerinde çalışalım şimdi
df1.entry_date
df1.entry_date.dt.year       # Sadece yılı aldı
# NOTE: it can be date, year, quarter, month, week, day, weekday, dayofweek, hour, minute, second, microsecond, day_name()
df1.entry_date.dt.quarter    # Hangi çeyreklikte olduğunu aldı dataların
df1.entry_date.dt.dayofweek
df1.entry_date.dt.day_name()

#############################
# Datetime Module
from datetime import datetime
datetime.now() # Bilgisayarınızdaki o anki tarih ve saat bilgisini alır
# Daha düzgün bir çıktı istersek
print(datetime.now())
print(datetime.today()) # Aynı çıktı
current_datetime = datetime.now()
print(current_datetime)
current_datetime.date() # Bunu bir seride kullanmak isterseniz apply içerisinde
# .. yapmak zorunda kalırsınız o yüzden seriler üzerinde "dt" kullanmak daha mantıklı olacaktır
current_datetime.weekday()   # Haftanın 2. günü. weekday()    : Monday e 0 veriyor
current_datetime.isoweekday() # Haftanın 3. günü. isoweekday() : Monday e 1 veriyor

###########
# class datetime.timedelta
from datetime import timedelta
timedelta(days=2) # Docstring e bakarak parametreleri girebiliriz. 
# Biz sadece day yazdık
current_datetime
two_days_before = current_datetime - timedelta(days=2) #Bugünden 2 gün çıkardım
two_days_before
# Hoca: Analiz firmasında çalışırsanız böyle şeyler kullanabilirsiniz
# .. Mesela: 2 gün öncesindeki değerle kıyasla.. gibi..
current_datetime + timedelta(weeks=2, days=3, hours=4, minutes=10)
# 2 hafta 3 gün 4 saat 10 dk sonrasına baktık
# Yukarda yaptıklarımızın düzgün şekilde gözüken özeti
print(f"{'current_date': <15}", current_datetime)
print(f"{'plus': <15}", timedelta(weeks=2, hours=4, minutes=10))
print(f"{'total': <15}", current_datetime + timedelta(weeks=2, days=3, hours=4, minutes=10))
# Genel bir örnek
datetime.now()-pd.to_datetime("21.07.1980") # Steve hocanın yaşadığı gün sayısı

###########
# strftime() : Converting from date/datetime/timedelta object to string type.
print(current_datetime)
current_datetime.year # .year diyebiliyorduk. Veri tipine bakarsak;
type(current_datetime.year) # int
current_datetime.strftime("%Y") # Sadece içinden yıl alsın. Üstteki çıktıyı
# .. string olarak alıyorum
type(current_datetime.strftime("%Y"))  # str
# Sonuç olarak amacınıza uygun olarak hangisini(Hangi veri tipini)
# .. kullanacağımıza karar vereceğiz çalışmalarımızda

# Özet ve Örnek
year = current_datetime.strftime("%Y")
print("year:", year)
month = current_datetime.strftime("%m")
print("month:", month)
day = current_datetime.strftime("%d")
print("day:", day)
time = current_datetime.strftime("%H:%M:%S")
print("time:", time)
date_time = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)
# Mesala Bunu her türlü analizi yaptıktan sonra sunum safhasında hangi ülkede sunum yapacaksanız o ülkenin anlayacağı 
# .. şekle göre tarihi değiştirebiliriz çalışmalarımızda

###########
# strptime()
date_string = "21 June, 2018" # String
date_string
datetime.strptime(date_string,"%d %B, %Y")   # strptime ile datetime a çevirebilirim ama formatını vermem gerekli
# datetime.strptime(date_string,"%d %B %Y")  # HATA. Virgülü koymadığım için match olmadı ve hata verdi

###############################################
# Operation with Datetime Object
# HOCA: Gerçek dünyada iş verenin sorduğu 2 soruyu nasıl cevaplandırdığıma bakalım
df1

##############
# 1. Let's detect the time between first order date and entry date for each product
# Not: Order_date ler unique değil
df1.order_date - df1.entry_date # 911 satır
df1["time_delta"] = df1.order_date - df1.entry_date
# Şimdi ilk başta şunu yapmam lazım. time_deltayı sayısal değere çevirmem lazım çünkü onun üzerinde işlem yapacağım
# df.time_delta.str.split() # HATA. (Normalde bölüp ilk indexi(sayıları) alacaktık)(Alttaki gibi)
df1.time_delta.astype("str").str.split().str[0].astype("int") # string e çevirip 0. elemanları alıp sonra string olarak kalmasını 
# .. istemediğim için tekrar integer a çevirdik. 
df1["time_delta"] = df1.time_delta.astype("str").str.split().str[0].astype("int")

df1.groupby("id_product")["time_delta"].min() # Çıktıda 401 no lu ürün için 781 gün vs gibi değerler var
# 498 satır var, benim satır sayım ile uyuşmuyor. Bunu çözmek için "transform" ile bu işlemi yapmalıyız
df1.groupby("id_product")["time_delta"].transform(min) # Her 401 gördüğü yere 781 yazacak, her 416 gördüğü yere 485 yazacak vs vs
df1["passing_time_to_firstsale"] = df1.groupby("id_product")["time_delta"].transform(min)
df1 # Örneğin çıktıda 906 ve 907. indeexte id_product ı aynı olan ürün için
# .. "time_delta" da 48 yazılmış(DIKKAT:order_date ler farklı olmasına rağmen)

##############
# 2.Let's detect the time between last order date and today for each product
df1.groupby("id_product").order_date.max()
df1.groupby("id_product").order_date.transform(max).dt.date
last_order_date = df1.groupby("id_product").order_date.transform(max).dt.date
today = pd.to_datetime("27-02-2021", format='%d-%m-%Y').date()
print(today)
today - last_order_date
df1["passing_time_from_lastsale"] = today - last_order_date
df1
df1["passing_time_from_lastsale"] = df1["passing_time_from_lastsale"].astype("str").str.split(" ").str[0].astype(int)
df1


####################################################-----END-----####################################################




