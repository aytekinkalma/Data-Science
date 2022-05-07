# NUMPY
# 1.Kodlar
# 2.Konu Anlatımı

########################################################################################
# 1.KODLAR
########################################################################################



import numpy as np
np.array([1,2,3,4,5,6])              # Tek boyutlu array
np.array([[1,2,3],[5,6,7],[8,9,10]]) # İki boyutlu array(Matris)
list1 = [1,2,3]
list2 = [[1,2,3],[4,5,6],[7,8,9]]
list3 = [[[1,2,3],[4,5,6],[7,8,9]]]
np.array(list1)                     # Listeden bir boyutlu array oluşturma
np.array(list2)                     # Listeden iki boyutlu array oluşturma
np.array(list3)                     # Listeden üç boyutlu array oluşturma

np.arange(10)                        # 0 dan 10(10 dahil değil) a kadar sırayla(1,2,...,9) tek boyutlu array
np.arange(10,20)                     # 10 dan 20(20 dahil değil) ye kadar sırayla(10,11,...,19) tek boyutlu array
np.arange(2,8,2)                     # 2 den 8(8 dahil değil) e kadar 2 şer 2 şer artan tek boyutlu array
np.arange(9).reshape(3,3)            # 0 dan 9(9 dahil değil) a kadar olan sayılardan 3 e 3 lük matris
np.arange(10,19).reshape(3,3)        # 10 dan 19(19 dahil değil) a kadar sırayla 3 e 3 lük matris

np.zeros(10,dtype=int)               # 0 lardan oluşan 10 elemanlı array # dtype=int yazmazsak çıktı "float" değerler görürüz
np.zeros((3,5), dtype=int)           # 0 lardan oluşan 3 e 5 lik matris  # dtype=int yazmazsak çıktı "float" değerler görürüz
np.zeros((5,5), dtype=bool)          # 0=False anlamına geldiği için bool veri tipinde 5 e 5 lik False boolean veritipli matris
np.ones(10, dtype=int)               # 1 lerden oluşan 10 elemanlı array # dtype=int yazmazsak çıktı "float" değerler görürüz
np.ones((3,3), dtype=int)            # 1 lerden oluşan 3 e 3 lük matris  # dtype=int yazmazsak çıktı "float" değerler görürüz
np.ones((5,5), dtype=bool)           # 1=True anlamına geldiği için bool veri tipinde 5 e 5 lik True boolean veritipli matris
np.full(3,10)                        # 10 lerden oluşan 3 elemanlı array(Tek boyutlu)
np.full((3,4),5)                     # 5 lerden oluşan 3 e 4 lük matris
np.full((3,5),"Steve")               # Her hücrede "Steve" yazan 3 e 5 like matris 
np.full((2,4,3),255)                 # Her hücrede 255 yazan 2 tane 4 e 3 lük array oluşturduk 
# np.full(3)                         # HATA # full() missing 1 required positional argument: 'fill_value'

np.random.randint(10)                # 0-10(10 dahil değil) arası sayı üretti
np.random.randint(10,15,size=8)      # 10-15(15 dahil değil) arası uniform dağılıma göre rasgele integerlardan oluşan 8 elemanlı tek boyutlu array
np.random.randint(10,size=(3,4))     # 0-10(10 dahil değil) arası uniform dağılıma göre rasgele integerlardan oluşan 3 e 4 lük matris
np.random.rand(3)                    # 0 ile 1 arasında "3" sayı üretti(Uniform dağılıma göre)
np.random.rand(5,5)                  # 0 ile 1 arasında "5x5" lik matris için rasgele sayı üretti(Uniform dağılıma göre)
np.random.normal(10,3,size=10)       # ort: 10 , std sapma: 3 olan 10 elemanlı normal dağılıma göre rasgele sayılar alan array
np.random.normal(10,2,size=(3,3))    # ort: 10 , std sapma: 2 olan 3 e 3 lük normal dağılıma göre rasgele sayılar alan matris
np.random.randn(4)                   # Ortalaması 0 ve verinin yüzde 99.7 si -3 ile +3 arasında olacak şekilde standart normal dağılıma göre rasgele sayılardan array oluşturdu
np.random.randn(4,4)                 # Ortalaması 0 ve verinin yüzde 99.7 si -3 ile +3 arasında olacak şekilde standart normal dağılıma göre rasgele sayılardan 4x4 matris oluşturdu
# np.random.randn(10,3,size=10)      # HATA # randn() got an unexpected keyword argument 'size'
np.random.seed(42)

np.linspace(0,10,5)                   # 0 ile 10 arasında 0 ve 10 DAHIL eşit aralıklı 5 sayı
np.linspace(0,10,5, dtype="int")  
np.linspace(0,[10,20],5)              # 0 dan 10 a(0 ve 10 dahil), 0 dan 20 ye(0 ve 20 dahil) eşit aralıklı 5 sayı(Sütunlar olarak üretecek)(default: axis=0)
np.linspace(0,[10,20],5, axis=1)      # 0 dan 10(0 ve 10 dahil) a, 0 dan 20 ye(0 ve 20 dahil) eşit aralıklı 5 sayı(Satırlar olarak üretecek)
np.linspace([0,20],[15,30],5, axis=0) # 0 dan 15(0 ve 15 dahil) e, 20 dan 30 a eşit aralıklı 5 sayı(Sütunlar olarak üretecek)
np.linspace([0,20],[15,20],5, axis=1) # 0 dan 15(0 ve 15 dahil) e, 20 dan 30 a eşit aralıklı 5 sayı(Satırlar olarak üretecek)

np.eye(4)                             # 4x4 lük Birim matris
np.eye(4)*33                          # 4x4 lük Değerleri 33 olan birim matris
np.eye(4, dtype = bool)               # 4x4 lük Değerleri boolean olan birim matris

#############################################
# Arraylerin bazı Özellikleri (Some attributes of arrays) # ndim , shape, size, dtype
# Tek boyutlu
a = np.random.randint(10, size=10)
a
a.ndim                   # Boyut sayısı
a.shape                  # DIKKAT Output : (10,) # a.reshape(10,1) yapılabilir(Bazen gerekli olacak)
k = a.reshape(10,1)
k
k.ndim                   # DIKKAT --> Boyutu 2 ye çıktı
a.size                   # Arraydeki eleman sayısı
a.dtype                  # Arrayin veri tipi
a[5].dtype               # 5. indexteki elemanın veritipi
a.itemsize               # Array içerisindeki elemanların kapladığı boyutu söylüyor.

# İki boyutlu
m = np.random.randint(10, size=(4,6))
m
m.ndim
m.shape
m.size
m.dtype
#############################################
# Yeniden Şekillendirme (Reshaping) (Üstte de vardı)
np.arange(1, 10)
np.arange(1, 10).reshape((3, 3))
a.reshape(1,1,10) # 2 boyuttan 3 boyuta çıkardık
m.reshape(-1,2) # sütun sayım 2 olsun, satır sayım için; m daha önce 4x6(24 elemanlı) olduğu için şimdi satır 12 olacak
m.reshape(3,-1) # satır sayım 3 olsun, sütun sayım için; m daha önce 4x6(24 elemanlı) olduğu için şimdi satır 8 olacak

# Index Seçimi (Index Selection)
# Tek boyutlu
a = np.random.randint(10, size=10) # 0 dan 10 a kadar rasgele 10 eleman oluştur
a
a[0]
a[-1]
a[0] = 999 # Değiştirdik değeri(Kalıcı)
a

# İki boyutlu
m = np.random.randint(10, size=(3, 5))
m
m[0, 0]
m[1, 1]
m[2, 3]
m[2, 3] = 9999 # Değiştirdik değeri(Kalıcı)
m

# Not
m[2, 3] = 2.9 ## DIKKAT. Çıktıda 2 geldi çünkü (arrayler)tek tip veri tipini tuttu float tutmadı
m

#############################################
# Slicing
# Tek boyutlu
a = np.random.randint(20, size=11)
a
a[8]         # 8. indexteki elemanı verir.
a[-3]        # -3. index teki eleman
a[4:10]      # 4. indexten 10. indexe kadar olanları aldı(10 dahil değil)
a[5:]        # 5. indexten sona kadar olanları aldı(10 dahil değil)
a[1::2]      # 1 inci indexten başlayıp 2 adım aralığı ile tek indexlere karşılık gelen elemanlar
a[::2]       # 0 ıncı indexten başlayıp 2 adım aralığı ile çift indexlere karşılık gelen elemanlar 
a[:5] = 77   # arrayin belirli bir bölümünü alıp değerlerini değiştirebiliriz.
# Not:#  arrayin kopyasını alarak kopyası üzerinden işlem yaparsanız orjinal arrayde yaptığınız değişiklikler gerçekleşmez.
array_copy =a.copy()

# İki boyutlu
m = np.random.randint(20, size=(3, 5))
m
m[:, 0]
m[1, :]
m[0:2, 0:3]
m[:2,1:]           # Baştan ikinci indexe kadar olan satırlar ile 1 inci indexten sona kadar olanların kesişimi
m[1,1]             # veya arr_2d[1][1]   1. satır ve 1. sütundaki eleman
m[1][1]            # 1. satır ve 1. sütundaki eleman
m[2,:2]            # ikinci satır, baştan 2. indexine kadar olan sütun kesişimi.
arr_2d[1,:1] = 55  # Bu şekilde slicelama ile aldığımız parçadaki değerleri kalıcı olarak başka bir değer ile değiştirebiliriz.
arr_2d[1,:1] = 5.5  # float değer atadığınızda arrayin default değeri int olduğu için int'a çevirerek atar.(Çıktıda integer gelir)

#############################################
# any_array[[row indices], [column indices]]
jj = np.arange(1,17).reshape(4,4)
jj
jj[[1,2],[0,3]]      # 1. satırın 0. elemanı, 2. satırın 3. elemanı
jj[[1,2,0],[0,3,2]]  # 1. satırın 0. elemanı, 2. satırın 3. elemanı, 0. satırın 2. elemanı
jj[1,[2,3]]          # 1. satırın 2. elemanı, 1. satırın 3. elemanı  
jj[[1],[1,3]]        # Satır indexi köşeli parantez içinde de yazılabilir.
jj[:,[1,3]]          # Tüm satırların 1. ve 3. sütunları

#############################################
# Step
step = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11])
step
step[1:11:3] # 1. indexten 11. indexe kadar 3 er 3 er artarak yazdır(11 dahil değil)


#############################################
# Fancy Index # ONEMLI
#############################################
v = np.arange(0, 30, 3)
v
v[1]
v[4]
v[3]

catch = [1, 2, 3]
v[catch]   # catch bir liste ve biz liste içine bir liste koyduk burada aslında(v[[1,2,3]])

m = np.arange(9).reshape((3, 3))
m
m[2, [1, 2]] #2. satır - 1. ve 2. sütun ları getir
m
m[0:1, [1, 2]] # 0 dan 1 e kadar satır - 1. ve 2. sütun ları getir
#############################################
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
# Tek boyutlu
v = np.array([1, 2, 3, 4, 5])
v
v < 3             # Bolean
v[v < 3]
v[v > 3]
v[v >= 3]
v[v <= 3]
v[v == 3]
v[(v < 3) | (v > 7)]                  # Aradaki işaret "veya" anlamında
arr[(arr < 3) | (arr > 7) & (arr!=9)] # & işareti "ve" anlamında

# İki boyutlu
u = np.array([[1, 2, 3],[4, 5,6]])
u
u<5
u[u > 2]             # DIKKAT. Tek boyuta düştü. Bkz. aşağı
a = u[u > 2]
a.ndim
u[u < 5]

#############################################
# Matematiksel İşlemler (Mathematical Operations)
v = np.array([1,2,3,4,5])
v / 5
v * 5 / 10
v ** 2      # Karelerini aldı
v - 1       # Hepsinden 1 çıkarttı
v * 5       # Hepsini 5 ile çarptı

v + v
v - v
v / v
1 / v       # bir sayıyı bir arraye bölebilirsiniz.
v -5        # bir arrayden başka bir sayıyı çıkartabilirsiniz.
v * 7       # bir arrayi başka bir sayı ile çarpabilirsiniz.
v ** 2      # bir arrayin istediğiniz kuvvetini alabilirsiniz. 

np.subtract(v, 1)   # arrayin tüm elemanlarından 1 çıkarttı 
np.subtract(1, v)   # 1 den arrayin tüm elemanlarını çıkarttı
np.add(v,1)         # arrayin tüm elemanlarına 1 ekledi   
np.add(1, v)        # 1 ile arrayin tüm elemanlarını topladı    
np.multiply(arr, 3) # np.multiply() fonksiyonu ile bir array ile bir sayı/arrayi çarpabilirsiniz.
np.divide(2, v)     # bir arrayi  bir sayıya ya da arraye bölebilirsiniz.
np.divide(v, 2)     # bir sayıyı bir arraye bölebilirsiniz.
np.sum(v)           # arrayin elemanlarını kendi arasında topladı
v.sum()

np.power(v,4)     # np.power() fonksiyonu ile bir arrayin bir sayı/array kuvvetini alabilirsiniz.
np.absolute(-9)   # N bir sayının mutlak değerini almak için
np.abs(10-v)      # Bir arrayin elemanlarının mutlak değerini almak için
np.sqrt(v)        # bir arrayin elemanlarının karekökünü almak için
np.exp(v)         # bir arrayin elemanlarının exponansiylini almak için
np.sin(v)         # bir arrayin elemanlarının sinusunu almak için
np.sin(np.pi/2)
np.tan(np.pi/4)
np.log(arr)       # bir arrayin elemanlarının logaritmasını almak için
np.log10(arr)     # bir arrayin elemanlarının log10'unu almak için
np.mod(v, 2)  # DIKKAT: mode değil! np.mod() fonksiyonu ile bir array ile bir sayı/arrayin modulus(kalan değer) bulabilirsiniz.

np.min(v)
v.min()
v.argmin() # min sayının index numarasını verir
np.max(v)
v.max()
v.argmax() # max sayının index numarasını verir

np.mean(v)
np.median(v)
# v.median()    # HATA
np.percentile(v, 50)  # arrayin medyanı 
np.std(v)
v.std()
np.var(v)
v.var()

arr = np.arange(15).reshape(3,5)
arr
np.amin(arr, axis=0)            # axis=0 boyunca min değerleri döndürür
np.min(arr, axis=0)             # axis=0 boyunca min değerleri döndürür
np.amax(arr, axis=1)            # axis=1 boyunca max değerleri döndürür
np.mean(arr, axis=0)            # axis=0 boyunca meam değerleri döndürür
np.std(arr, axis=1)             # axis=1 boyunca std değerleri döndürür
np.var(arr, axis=0)             # axis=1 boyunca var değerleri döndürür
np.percentile(arr, 25, axis=0)  # # axis=0 boyunca q1(%25) değerleri döndürür
np.corrcoef(arr)

#############################################
# Concatenate
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.array([7, 8, 9])

np.concatenate([x,y])             # Yanyana birleştirdi (default axis=0)
np.concatenate([x, y, z], axis=0) # Yanyana birleştirdi 
# np.concatenate([x, y, z], axis=1)  # HATA tek boyutlu arraylerde axis=1 olduğu zaman hata verir.

np.concatenate([x.reshape(1,3), y.reshape(1,3), z.reshape(1,3)], axis=0) # arraylere reshape() ile boyut kazandırırsak bu şekilde çalışır.
# 2. yol:
np.concatenate([[x, y, z]], axis=0)  # x,y,z 'yi ikinci bir köşeli parantez içine alarak axis=0(satırlar boyunca )da birleştirme yapabiliriz.
# 3. yol:
np.concatenate([x, y, z], axis=0).reshape(3,3)  # tek boyutlu birleştirdiğimiz 
# .. arrayin şeklini değiştirerek de axis=0 boyunca birleştirme yapmış oluruz.
# [[x,y,z]]  # OUTPUT: [[array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]]

# iki boyutlu arraylerde concatenate yapabilmek için birleştirilecek arraylerin satır veya sütun sayıları eşit olmalı.
# Satır bazında (axis=0) birleştirme yapılacak ise sütun sayıları eşit olmalı.
# Sütun bazında (axis=1) birleştirme yapılacak ise satır sayıları eşit olmalı.
x = np.array([[1, 2, 3], [4, 5, 6]])                   # 2 satır, 3 sütun
y = np.array([[7, 8, 9], [10, 11, 12], [13, 14, 15]])  # 3 satır, 3 sütun
np.concatenate([x,y], axis=0) # axis=0 bazında birleştirme yapıldığında sütun sayıları eşit ise birleştirmeyi yapar ve hata vermez.
# np.concatenate([x,y], axis=1) # Hata # axis=1 bazında birleştirme yapıldığında satır sayıları eşit değilse birleştirmeyi yapamaz ve hata verir.
a = np.random.randint(10, size = (2, 3))
b = np.random.randint(10, size = (2, 3))
np.concatenate([a,b], axis=0)
np.concatenate([a,b], axis=1)


#############################################
# Splitting of the Arrays
# Tek boyutlu
x = np.array([1,2,3,99,99,3,2,1])
x

np.split(x, [3,5])      # 0:3, 3:5, 5:  şeklinde böldü
np.split(x, [4])        # 0:4, 4:, şeklinde iki parçaya böldü.
np.split(x, 4)  # index numarasını köşeli parantez içinde vermezsek 4 eşit parçaya böler.
# .. Ancak bu durumda arrayin eleman sayısının 4'e bölünebilen bir sayı olması gerekir.

# İki boyutlu
# İki boyutlu arraylerde split işlemi yapılırken indexlerde birlikte axis'in de belirtilmesi gerekir.
m = np.arange(20).reshape(5,4)
m

np.split(m, [1,3], axis = 0)  # satırlar boyunca :1, 1:3:, 3:, şeklinde üç parçaya böldük
np.split(m, [1,3], axis = 1)  #  sütunlar boyunca :1, 1:3:, 3:, şeklinde üç parçaya böldük.
np.split(m, 5, axis = 0)      # satırlar boyunca 5 eşit parçaya böldük.

np.vsplit(m,[3])  # vertical split ile satırlar boyunca(axis=0 gibi) :3, 3: şeklinde iki parçaya böldük.
np.hsplit(m,[3])  # horizontal split ile sütunlar boyunca (axis=1 gibi) :3,3: şeklinde iki parçaya böldük.

#############################################
# Sorting of the Arrays
# Tek boyutlu
v = np.array([2,1,4,3,5,8,1])
v

np.sort(v)           # Orjinal array değişmez
v.sort()             # Orjinal array değişir
 
# İki boyutlu
y = np.random.randint(5, 100, (3,3))
y

np.sort(y, axis=0)  # axis=0 verince satırlar boyunca sıralama yapar.
np.sort(y, axis=1)  # axis=1 verince sütunlar boyunca sıralama yapar.

#%%
########################################################################################
# 1.KONU ANLATIMI
########################################################################################
###################################################
"""
It is the fundamental package for scientific computing with Python. 
It contains various features including these important ones:

* A powerful N-dimensional array object,
* Sophisticated (broadcasting) functions,
* Tools for integrating C/C++ and Fortran code,
* Useful linear algebra, Fourier transform, and random number capabilities
"""

"""
Q:  What is a NumPy Array?
A:  A NumPy array is a multidimensional array of objects all of the same type. 
In memory, it is an object which points to a block of memory, keeps track of the 
type of data stored in that memory, keeps track of how many dimensions there are 
and how large each one is, and - importantly - the spacing between elements along each axis.

- Interview Q&A
"""

"""
Q:  What Advantages Do Numpy Arrays Offer Over (nested) Python Lists?
A: Python’s lists are efficient general-purpose containers. They support (fairly) efficient insertion, deletion, appending, and concatenation, and Python’s list comprehensions make them easy to construct and manipulate. However, they have certain limitations: they don’t support “vectorized” operations like elementwise addition and multiplication, and the fact that they can contain objects of differing types mean that Python must store type information for every element, and must execute type dispatching code when operating on each element.

- Interview Q&A
"""

"""
Q:  Is Python NumPy better than lists?
A:We use python numpy array instead of a list because of the below three reasons:

Less Memory,
Fast,
Convenient.
- Interview Q&A
"""

















