# PANDAS
#%%
####
#Pandas series vs numpy array??
# What is Pandas series
# Pandas df ui anlatıyor hoca, index, sütun
# .. 4 sütun var. Buna 4 tane seri de diyebiliriz
# .. Bir kaç seri bir df oluşturabilir
# Nasıl bir pandas seri oluşturabiliriz
# pandas.Series(data=None, index=None, ....)
# Pandas Series Basic methods & attributes
# .. bazı
"""
Content

¶
IMPORTING LIBRARIES NEEDED IN THIS NOTEBOOK
CREATING PANDAS SERIES
Using Lists
Using Numpy Arrays
Using Dictionaries
Using Scalar Value
DATA IN A SERIES
BASIC ATTRIBUTES & METHODS OF SERIES
INDEXING AND SLICING WİTH PANDAS SERIES
Selection with Condition and Broadcasting
RECAP FOR SEVERAL SELECTING ATTRIBUTES
THE END OF THE SESSION-03
"""
#%%
import numpy as np
import pandas as pd
labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {'a': 10, 'b': 20, 'c': 30}
pd.Series(labels)
pd.Series(my_list)
pd.Series(arr)
pd.Series(data = arr, index=labels)
# Data uzunluğu ile index uzunluğu aynı olmalı
# pd.Series(data = arr, index=["a","b","c","d"]) # Hata
pd.Series(d)
pd.Series(d, index = ["aa","bb","cc"]) ## NaN değerler geldi
pd.Series(data="Ilknur")
pd.Series(data="Ilknur", index= range(5))
pd.Series(data=10, index=["a","b","c"])
# Liste, array ,dictionary, scaler value lar ile 4 tane series oluşturma gördük
# Note: # Using Scalar Value
# .. Scalars are single values representing one unit of data, such as an integer or bool, as opposed to data 
# .. structures like a list or tuple, which are composed of scalars.
# .. If data is a scalar value, an index must be provided. The value will be
# .. repeated to match the length of index Source.

ser = pd.Series(data = [set, list, dict])
ser[0]
ser[0]([1,3,3,4,4,5]) # Set in işlevi ne işe onu yaptı.
pd.Series(data=[sum,print,len]) # Bunların python ın built-in fonksiyonları
# .. olduğunu söyledi
ser1 = pd.Series(data=[sum,print,len]) # Bunların python ın built-in fonksiyonları
# .. olduğunu söyledi
ser1[1]("hello world") # print in işlevini yaptı
ser1[2]("hello world") # len in işlevini yaptı
mix_data = ["ahmet",5 , True, 5.8]

ser2 = pd.Series(mix_data)
ser2
ser2.dtype # En kapsamlı olanını aldı
# Yani object i float a ya da int e çevirirsin ama
# .. integer ı vs string e çeviremezsin
# Ama.. data tiplerini ilk hali ile muhafaza etmeye devam ediyor
type(ser2[3])
# Sadece boolean olursa içeride yine "Object"
mix_data2 = [5 , True, 5.8]
ser3 = pd.Series(mix_data2)
ser3.dtype # dtype('O')
# Array lere bakalım
arr = np.array(mix_data)
arr
# Hepsini string yaptı array
#%%
"""
BASIC ATTRIBUTES & METHODS OF SERIES
SOME COMMON ATTRIBUTES Official Pandas API Document

Series.dtype It returns the data type of the data.
Series.shape It returns a tuple of shape of the data.
Series.size It returns the size of the data.
Series.ndim It returns the number of dimensions in the data.
Series.index Defines the index of the Series.
Series.keys Return alias for index.
Series.values Returns Series as ndarray or ndarray-like depending on the dtype.
Series.items Lazily iterate over (index, value) tuples.
Series.head Return the first n rows.
Series.tail Return the last n rows.
Series.sample Return a random sample of items from an axis of object.
Series.sort_index Sort Series by index labels.
Series.sort_values Sort by the values.
Series.isin Whether elements in Series are contained in values.
"""
ser = pd.Series(data = np.random.randint(0,100,7))
ser
ser.dtype
ser.shape
ser.size
len(ser)
ser.ndim
ser.index
ser.keys # type: method
ser.keys()
list(ser.index)
list(ser.keys())
ser.values
ser.items
ser.items()
ser.head()
ser.tail()
ser.sample(3)
ser.sort_index(ascending = False)
ser.sort_index(ascending = True).head(7)
ser.sort_values(ascending=True)
ser.isin([54,10,11]) 

ser1 = pd.Series([1, 2, 3, 4], index = ['USA', 'Germany','RF', 'Japan'])
ser2 = pd.Series([1, 2, 5, 4, 6], index = ['USA', 'Germany','Italy', 'Japan', 'Spain'])
ser1.sort_index() # or ser1.sort_index(ascending=True)
ser1.sort_values() # or ser1.sort_values(ascending=True)
ser1[3] # ser1.values[3] # 4
ser1.index[3] # 'Japan'
ser1.index.get_loc("Japan") # Japan ın lokasyonunu ver. 3. sırada diyor # Çok kullanılmıyor
ser1.Japan # or ser1["Japan"] # Bu yazim tekniginin(ser1.Japan) ismi "SQL syntex" dir
ser2[2:]
ser[::-1] # Tersten sıralama

ser1 + ser2 # Indexleri aynı olanları topladı, farklı olanlara birşey yapmadı
ser1.add(ser2,fill_value=1) # Boş olan değerlere 1 deyip topladı yine
ser1*ser2

ser = pd.Series(data = [121, 200, 150, 99], index = ["terry", "micheal", "orion", "jason"])
ser["terry"]
ser[0]
ser[[0,2]]
ser[["terry","orion"]]
ser[:3]   # DIKKAT: rakam kullanınca dahil etmedi "Jason" ı
ser["terry":"jason"] # DIKKAT: "jason" ı dahil etti
"terry" in ser # DIKKAT: indexe bakıyor. Value değerine bakmıyor
121 in ser.values # DIKKAT: values a bakıyor
ser<100
ser[ser<150]
ser[ser<130] = 140
ser
ser.isin([150]) # bolean ifadeyi condition olarak yazabilirsiniz
ser[ser.isin([150])]
ser[ser.isin([150])] = 125 # bolean ifadeyi condition olarak yazdık burada











