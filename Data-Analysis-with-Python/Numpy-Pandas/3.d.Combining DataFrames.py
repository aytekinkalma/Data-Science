import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)

#%% COMBINING DATAFRAMES

# There are 4 main ways of combining DataFrames together: Appending, Concatenating, Joining and Merging. 
# In this lecture we will discuss these 4 methods with examples A Detailed Video Source.
# 1.Append is the specific case(axis=0, join='outer') of concat
# 2.Concat gives the flexibility to join based on the axis( all rows or all columns)
# 3.Join is based on the indexes (set by set_index)/key columns on how variable =['left','right','inner','outer']
# 4.Merge is based on any particular column each of the two dataframes, this columns are variables on like 'left_on', 'right_on', 'on'

# 1.APPEND : vertically    # APPEND , CONCAT ın axis=0 hali. Kalan her şey aynı
# 2.CONCAT : vertically or horizontally
# 3.JOINING: horizontally
# 4.MERGE  : horizontally

#%%
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']}
                    )

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']}
                    ) 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']}
                   )

df4 = pd.DataFrame({'C': ['C12', 'C13', 'C14', 'C15'],
                    'A': ['A12', 'A13', 'A14', 'A15'],
                    'D': ['D12', 'D13', 'D14', 'D15'],
                    'B': ['B12', 'B13', 'B14', 'B15']}
                    )
# DIKKAT: df4 de sütun isimleri farklı

display(df1,df2,df3,df4)

##########################################################
# APPENDING
df1.append(df3)                    # df3 ü, df1 in altına ekledik. Başka hiç bir şey yapmadı bu kod
df1.append(df3, ignore_index=True) # index numaralarını düzeltti ve df3 ü, df1 in altına ekledik
df1.append(df4)                    # df4 ü df1 in altına ekledik ama df1 in sütun sırasını baz aldı(df1 i önce yazdığımız için)
df4.append(df1)                    # df1 ü df4 in altına ekledik ama df4 in sütun sırasını baz aldı(df4 i önce yazdığımız için)

##########################################################
# CONCATENATION
pd.concat([df1,df2,df3],axis=0) # NOT:Default axis=0, df leri Yazılan sıraya göre birleştirme yapar alt alta
pd.concat([df1,df2,df3],axis=0, ignore_index=True) # index sırasını değiştirdi ve Yazılan sıraya göre birleştirme yapar alt alta
pd.concat([df1.iloc[:,:2], df2.iloc[:,1:], df3], axis=0, ignore_index=True)
pd.concat([df1,df2,df3],axis=1) # indexlere göre işlem yaptı. index numaralarıda aynı olduğu için problemsiz yan yana ekledik

df5 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])

df6 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7]) 

df7 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])

display(df5,df6,df7)            # df lerin sütun sıraları aynı ama index leri farklı
pd.concat([df5,df6,df7],axis=0) # df leri Yazılan sıraya göre birleştirme yapar alt alta. ignore_index yapmaya bile gerek yok burada
pd.concat([df5,df6,df7],axis=1) # indexlere göre birleştirme yapacağı için. indexleri farklı olduğu için df5 i yanına ekledi ve 
# .. sütun olarak(Yani A,B,C,D yi koydu yana) ama indexleri uyuşmadığı için alta 4,5,6,7. indexi ekledi ve onunla kendisine ait
# .. olan A,B,C,D(ikinci A,B,C,D) ile birleştirdi.
pd.concat([df5,df6,df7],axis=1, join="inner")                    # Boş geldi çünkü "inner" kesişim yapar. Kesişen index olmadığı için.
pd.concat([df5,df6,df7],axis=1, join="inner", ignore_index=True) # Yine boş. ignore_index işe yaramadı
pd.concat([df5,df6.reset_index(drop=True), df7.reset_index(drop=True)], join="inner", axis=1) # Her şey düzeldi.
# .. reset_index(drop) yapınca eski indexi drop etmiş olduk(df6 için 4,5,6,7 yi drop etmiş olduk , df7-->8,9,10,11)

##########################################################
# MERGING
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})   

display(left, right)
pd.merge(left=left, right=right, how="inner", on="key") # left e(Sola) left df ini, right a(Sağa) right df ini koyduk.
# .. Ortak sütun(key e ) göre birleştrdi, how="inner" yerine "outer" ya da "left" yazsaydık da aynı sütun gelirdi.
# NOTE: Burada on="key" yazmasakta olurdu. Python bunu anlayıp "key" sütununu en başa koyacaktı

left2 = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})

display(left2, right2) # Burada key lerin değerleri farklı
pd.merge(left=left2,right=right2, how="inner",on="key") # how="inner" yaptığımız için key lerin değerlerinde ortak olan indexleri aldı
# ..  ve diğerlerinisola left2 yi sağa right2 df i gelecek şekilde getirdi yana
pd.merge(left=left2,right=right2, how="outer",on="key") # how="outer" her iki df dede tüm indexlere karşılık gelen değerleri aldık, 
# .. üstteki aynı mantıkta yaptı ama eşleşmeyen değerlere NaN verdi
pd.merge(left2,right2, how="left",on="key")      # how="left" yazında soldaki df in(left2 nin) key değerlerine göre birleştirme.
pd.merge(left2,right2, how="right",on="key")     # how="right" yazında sağdaki df in(right2 nin) key değerlerine göre birleştirme.

left3 = pd.DataFrame({'key': ['K0', 'K0', 'K1', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right3 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K2'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})

display(left3, right3)

pd.merge(left3,right3, how="inner",on="key") # how="inner" ortak olanları alıyordu # 0. indexte 2 sinde de "key" de 
# K0 olduğu için onu aldı A ve B yi normal yazdı, C ve D yi 0. indexi normal yazdı 1. indexi çoğalttı/çokladı otomatik
# .. 2. ve 3. index aynı mantıkta(3. indexteki C ve D sütununu çokladı)
pd.merge(left3,right3, how="left",on="key") # Aynı çıktıyı verdi
pd.merge(left3,right3, how="outer",on="key") # how="outer" 2 df dede tüm indexlere karşılık gelen değerleri aldık(2 index daha
# ..  ekledi(K2 lere karşılık gelen 4. ve 5. indexi. Üstteki ile aynı mantıkta yaptı ama A ve B - K2 kesişimi 2 df de de olmadığı
# ..  için o değerlere NaN verdi

left4 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right4 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})

display(left4, right4) # Burada primary key ler 2 tane

pd.merge(left4, right4, how="inner", on=["key1","key2"]) # how="inner". key1 ve key2 si 2 df de de eşleşen key değerlerini aldık. 

pd.merge(left4, right4, how="outer", on=["key1","key2"]) # how="outer" 2 df de de key1 ve key2 nin indexlerine karşılık gelen değerler
pd.merge(left4, right4, how="left", on=["key1","key2"])
pd.merge(left4, right4, how="right", on=["key1","key2"])

left5 = pd.DataFrame({'lkey': ['x', 'y', 'z', 'x', 'z'],
                     'lvalue': [2, 3, 5, 7, 0]})

right5 = pd.DataFrame({'rkey': ['a', 'x', 'z', 'b'],
                     'rvalue': [7, 8, 9, 10]})

display(left5, right5)

pd.merge(left5, right5, left_on="lkey", right_on="rkey", how="inner") # how="inner" ortak olan aynı değerleri döndürdü 2 ayrı sütunda
pd.merge(left5, right5, left_on="lkey", right_on="rkey", how="outer")
pd.merge(left5, right5, left_on="lkey", right_on="rkey", how="left")
pd.merge(left5, right5, left_on="lkey", right_on="rkey", how="right")

left6 = pd.DataFrame({'lkey': ['x', 'y', 'z', 'x'],
                        'lvalue': [2, 3, 5, 7]})

right6 = pd.DataFrame({'rkey': ['a', 'b', 'c', 'b'],
                         'rvalue': [7, 8, 9, 10]})

display(left6, right6) # Burada da indexler üzerinden yola çıkarak birleştirme yapacağız

pd.merge(left6, right6, left_on="lkey", right_on="rkey", how="inner")   # how="inner" ilgili ortak index bulamadığı için boş geldi
pd.merge(left6, right6, left_on="lkey", right_on="rkey", how="outer")   # Tüm lkey ve rkey değerlerini aldı Eşleşmeyenler NaN
pd.merge(left6, right6, left_on="lkey", right_on="rkey", how="left") 
pd.merge(left6, right6, left_on="lkey", right_on="rkey", how="right") 
pd.merge(left6, right6, left_index=True, right_index=True, how="outer") # left_index=True, right_index=True: indexleri kullanabiliriz

##########################################################
# JOINING
left7 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index = ['K0', 'K1', 'K2']) 

right7 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index = ['K0', 'K2', 'K3'])
display(left7, right7)

left7.join(right7) # left7 nin yanına right7 ui kodu, indexleri ortak olanların değerleri geldi. 
# .. Ortak olmayan "K1" indexinin C ve D değerleri NaN geldi
# Not: Burada how="left" default. O yüzden soldaki df in(left7 nin) indexlerini getirdi
right7.join(left7) # Üsttekinin tam tersi

left8 = pd.DataFrame({'key': ['K0', 'K2', 'K3', 'K4', 'K5', 'K6'],
                   'X': ['X0', 'X2', 'X3', 'X4', 'X5', 'X6']})

right8 = pd.DataFrame({'key': ['K0', 'K2', 'K3'],
                      'Y': ['Y0', 'Y2', 'Y3']})
display(left8, right8)

# left8.join(right8)  # HATA. Aynı isimdeki column(key) olunca birleştirmiyor "join". Bunu concat yapıyordu
# .. Bunu engellemek için "lsuffix" ve "rsuffix" kullanabiliriz
left8.join(right8, lsuffix="_left", rsuffix="_right") # Ortak isimli sütunların sonuna "_left" ve "_right" ekledi

# If you want to join using the key columns, you need to set key to be the index in both df and other.
# The joined DataFrame will have key as its index.
# Öyle birleştirelim "key_left", "key_right" çıktısı gelmesin dersem; # "Key" leri index e taşıyabilirim.
left8.set_index("key").join(right8.set_index("key")) # merge ün yaptığı bir işlem için burada "set_index" vs yazıp işlemi uzatıyoruz

# Another option to join using the key columns is to use the "on" parameter.
# DataFrame.join always uses other’s index but we can use any column in df.
# This method preserves the original DataFrame’s index in the result.

# left8.join(right8, on="key") # Hata. on="key" dediğimizde sadece left8 e göre "key" i alacak. Çözüm için;
left8.join(right8.set_index("key"), on="key") 


###########################################################
# MORE EXAMPLES
emps = pd.read_csv("employees.csv")
emps.head()
emps.info()

jobs = pd.read_csv("jobs.csv")
jobs.head()
jobs.info()

pd.merge(emps,jobs, on="job_id",how="left")

authors = pd.read_csv("authors.csv")
authors.head()
authors.info()

publishers = pd.read_csv("publishers.csv")
publishers.head()
publishers.info()

pd.merge(publishers, authors, on="city", how="left")

##################################
# Difference between Merge, join, and concatenate
"""
Merge

The merge() function used to merge the DataFrames with database-style join such as
.. inner join, outer join, left join, right join.
Combining exactly two DataFrames.
The join is done on columns or indexes.
If joining columns on columns, the DataFrame indexes will be ignored.
If joining indexes on indexes or indexes on a column, the index will be passed on.

Join

The join() function used to join two or more pandas DataFrames/Series horizontally.
Join() uses merge internally for the index-on-index (by default) and column(s)-on-index join.
Aligns the calling DataFrame’s column(s) or index with the other objects’ index (and not the columns).
Defaults to left join with options for right, inner and outer join

Concat

concatenate two or more pandas DataFrames/Series vertically or horizontally.
Aligns only on the index by specifying the axis parameter.
Defaults to outer join with the option for inner join
"""


####################################################-----END-----####################################################





