import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)

#%% DATA INPUT AND OUTPUT
pwd  # Find where you work and the current directory

# NOTE: Hız açısından en hızlı Json dosyaları, sonra csv, sonra excel dosyalarıdır
################################
# CSV Input & Output
#####################
# 1.CSV Input
pd.read_csv('example.csv')                   # read_csv : csv uzantılı dosyaları okur
# Notepad de açtığımızda virgülle ayrılmış olarak görüyoruz. Genelde virgül kullanılır
import csv
reader = csv.DictReader(open('example.csv')) # 2. yol

# What is the difference between CSV reader and CSV DictReader
# The DictReader() is used to read the file of the csv in the format of the dict object. 
# .. class csv.DictReader creates an object that operates like a regular reader but maps the
# .. information in each row to a dict whose keys are given by the optional fieldnames parameter.
# csv.Reader() allows you to access CSV data using indexes and is ideal for simple CSV files.
# ..  csv.DictReader() on the other hand is friendlier and easy to use, especially when working
# ..  with large CSV files

# pd.read_csv("C:/Users/cansi/OneDrive/Masaüstü/Data Science/CLARUSWAY/3.Pandas/g.Data input output/ornekcsv.csv") # 1. yol
pd.read_csv("ornekcsv.csv")                               # 2. yol(Aynı klasör) Çıktıda sorun var. Noktalı virülle ayrılmış
pd.read_csv("ornekcsv.csv", sep=';')                      # "sep" ile düzelttik. sep default ",(virgül)"
pd.read_csv("ornekcsv.csv", sep=';', index_col=0)         # index_col : Kaçıncı sütunu index olarak görmek istediğimi belirtiyoruz
pd.read_csv("ornekcsv.csv", sep = ";", usecols=['a', 'b'], nrows=10) # usecols=['a', 'b']: a ve b sütununu al, nrows=10 : 10 satır al

pd.read_csv("titanic.csv")                        # Çıktıda sorun var. Sütunlar arasında "tab" kullanılmış 
pd.read_csv("titanic.csv", sep = "\t")            # Bu şekilde çözdük

pd.read_csv("https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2020-financial-year-provisional/Download-data/annual-enterprise-survey-2020-financial-year-provisional-size-bands-csv.csv")
# .. internette bulduğumuz csv uzantılı dosyaları da bu şekilde okutabiliriz

#####################
# 2.CSV Output
# Dosyalarımızı tekrar csv olarak kaydetmek istersek bunu kullanıyoruz
df = pd.read_csv("example.csv")
df.to_csv('example_1.csv')                   # Klasörüm içerisinde example_1 adında csv dosyası oluştu
pd.read_csv("example_1.csv")                 # Tekrar okuttuk ama indexi sütuna getirmiş sonra kendi index oluşturmuş
pd.read_csv("example_1.csv", index_col = 0)  # 1.yol index_col = 0: Sıfırıncı kolunu indexe al
df.to_csv('example_1.csv', index = False)    # 2. yol . index = False: indexi sütuna taşımasın
pd.read_csv("example_1.csv")                 # Tekrar okutalım. Düzeldi

##############################################
# Excel Input & Output
#####################
# 1.Excel Input
# default sheet_name is 0. It means the first sheet comes into.
df1 = pd.read_excel('Excel_Sample.xlsx')                        # read_excel: xlsx uzantılı dosyaları okur
df1                                                             # 2 tane dosya var içinde ilkini okuttu default: 0
df2 = pd.read_excel('Excel_Sample.xlsx', sheet_name = "Sheet2") # sheet_name : Hangi dosyayı kullanacağımı seçtik # sheet_name = 1
df2
df3 = pd.read_excel('Excel_Sample.xlsx', sheet_name = None)     # sheet_name = None: Bütün dosyaları okur. type:dict olarak verir
df3
type(df3)
pd.ExcelFile('Excel_Sample.xlsx').sheet_names                   # içindeki dosyaların(sheetlerin) isimlerini verdi

#####################
# 2.Excel Output
# Writing a pandas DataFrame to Excel file
df1.to_excel('Excel_Sample1.xlsx', sheet_name='Sheet1', index = False)    # Klasörümde example_1 adında excel dosyası oluştu(sheet1)
df2.to_excel("Excel_Sample1.xlsx", sheet_name = "Sheet2", index = False)  # Klasörümde example_1 adında excel dosyası oluştu(sheet2)
# .. index = False: indexi sütuna taşımasın
# Not: Bunları yaparken excel dosyası kapalı olması gerekli. Yoksa hata alırız

#
with pd.ExcelWriter('combined_df.xlsx') as writer:           # For döngüsü gibi düşünürsek bunu writerın içine df1, df2 yi yazdırabilirim
    df1.to_excel(writer, sheet_name='sample1', index=False)
    df2.to_excel(writer, sheet_name='sample2', index=True)   # index= True olduğu için indexi sütuna taşıdı

pd.read_excel("combined_df.xlsx", sheet_name = "sample1")
pd.read_excel("combined_df.xlsx", sheet_name = "sample2")
# df1 ve df2 yi writer üzerine yazdıracağım. Bunu bu şekilde yapıyorum
# Yeni excel oluştu "combined_df". sample1 ve sample2 ikiside oluştur
# sample1 de indexi tuttu. Çünkü index=False, sample 2 de yeni sütun oluşturdu. Çünkü index=True
##############################################
# HTML Input & Output
# Pandas can read and write excel files, keep in mind, this only imports data. Not formulas or images,
# .. having images or macros may cause this read_excel method to crash.
# How can I open and read an HTML file in Pandas?
# You may need to install htmllib5, lxml, and BeautifulSoup4. In your terminal/command prompt run:
# conda install lxml
# conda install html5lib
# conda install BeautifulSoup4
# Then restart Jupyter Notebook. (or use pip install if you aren't using the Anaconda Distribution)
# Pandas can read table tabs off of html

#####################
# 1.HTML Input
# pip install lxml
# Istediğimiz sayfadaki tabloyu çekelim
df = pd.read_html('https://www.bbc.com/news/world-51235105') # read_html: Internetteki sayfalardaki tabloları okutur
df
df[0]                      # O sayfadaki ilk tabloyu aldık
df[0].columns
df2=pd.read_html('https://www.imdb.com/chart/top/')
df2
df2[0]

#####################
# 2.HTML Output
# Render a DataFrame as an HTML table
df2[0].to_html('simple.html',index=False) # simple html diye yeni html dosyası oluştu klasörümüzde

#################################################
# SQL Connections (IMPORTANT)
#####################
# 1.SQLite Connection with Python
# pip install sqlalchemy
from sqlalchemy import create_engine
temp_db = create_engine('sqlite:///:memory:') # Geçici tablo(database) oluşturacağız bilgisayarımızda sonra sql komutları göndereceğiz
temp_db.table_names()                         # Tablonun içi boş. Henüz bir şey doldurmadım.
# Wikipediadan tablolar çekelim yine
tables = pd.read_html('https://en.wikipedia.org/wiki/World_population')
tables
tables[6]                                         # 6. tablo ile çalışacağım dedik. Bunu oluşturduğum database içerisine göndereceğiz
tables[6].to_sql(name='populations', con=temp_db) # con=temp_db : connection nereye yapılacak --> temp_db ye
temp_db.table_names()                             # Bakalım tablo gitmiş mi temp_db ye # output : ['populations']

# How can I open and read a SQL file in python?
df = pd.read_sql(sql='populations', con=temp_db)
df
# How can I make a SQL query in python?
pd.read_sql_query(sql="SELECT Country, Population FROM populations", con=temp_db)
# NOTE: Geçici db de olanlar notebook u kapatınca gidecek. Bu eğitim amaçlıydı. Şimdi sql lite a geçelim.

import sqlite3
# Python dan daha rahat çalışmak için yapılmış bir db kütüphanesi
# Sql lite ı açıp sample_data isminde sqlite içerisinde boş tablolu bir db oluşturuyorum
with sqlite3.connect('sample_data.db') as cnnt:
    df.to_sql('sample1', cnnt)
# cnnt ismiyle tanımladık
# sample1 adlı tablo oluşturup onun içerisine atacağız
# python da oluşturduğum tabloyu burada sample1 içerisine atmış oldum
query = 'SELECT Country, Population FROM sample1'
with sqlite3.connect('sample_data.db') as cnnt:
    df_new = pd.read_sql_query(query, cnnt)
# db deki tablo üzerine query gönderip query deki sonucu df_new e verecek
df_new

#####################
# 2.MSSQL Connection with Python
# As we all know, one of the most widely used databases is Microsoft SQL Server. In this part of our
# ..  session, we will run a simple SELECT query by connecting to the MSSQL Server database with Python,
# ..  one of the languages widely used in data science studies
# Step 1: Import pyodbc in your Python Script. ...
# Step 2: Set the Connection String. ...
# Step 3: Create a Cursor Object from our Connection and Execute the SQL Command. ...
# Step 4: Retrieve the Query Results from the Cursor.

#!pip install pypyodbc
import pypyodbc
# MS SQL kurulu değilse  bir işlem yapamayız
# 2 türlü irtibat sağlayabilirsiniz 
# 1.Connection with Windows Authentication
# 2.Connection with SQL Server Authentication # Bunu kullanacağız

# Hoca: MS SQL i açtık db var orada içinde tablolar var. İşlemler yapacağım siz bunları şu an yapamazsınız

# Connection with Windows Authentication
# db = pypyodbc.connect(
#    'Driver={SQL Server};'
#    'Server=serveradi;'
#    'Database=veritabaniadi;'
#    'Trusted_Connection=True;')

# Connection with SQL Server Authentication(We will use this)
db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-RV0P6OM;'
    'Database=BikeStores;'
    'UID=sa;'
    'PWD=Sd110307;'
)
# MS sql ile irtibate geçtik burada. irtibat kodu değişebilir(pypyodbc)

"""
# db = pypyodbc.connect(
#     'Driver={SQL Server};'
#     'Server=DESKTOP-HNUHM85;'
#     'Database=BikeStores;'
#     'UID=sa;'
#     'PWD=16Hek72$;'
# )
"""

# Burada çalışmak için 2 yol var.
# 1. yol # Uzun yol
cursor = db.cursor()                            # cursor ı oluşturduğum db üzerinde oluşturuyorum curser değişkeni içerisine atıyorum
cursor.execute('SELECT * FROM sales.customers') # Bir object oluşturdu
# Bu objectin içerisine ulaşmak için;
# customers = cursor.fetchone()
# customers
customers = cursor.fetchall() # fetchall() : Bütün satırları al
customers
# 1. satır ... , 2. satır ..., # liste içinde tuplelar verdi bana
# Bunu nasıl düzgün okuyabiliriz peki; 

for i in customers:
    print(i)
# Daha düzgün bir çıktı geldi. Bunu df e çevirelim. Bu tablo şu an cursor ın içerisinde

cursor.description                  # Çıktıda tuple ın ilk elemanı sütun isimleri
[i[0] for i in cursor.description]
col_names = [i[0] for i in cursor.description]
col_names
df = pd.DataFrame(customers, columns=col_names)
df

# Yukardaki kodların özeti;
# cursor = db.cursor()
# cursor.execute("select * from sales.customers")
# customer = cursor.fetchall()
# col_names = [i[0] for i in cursor.description]
# pd.DataFrame(customers, columns=col_names)


# 2. yol # Kısa yol
df = pd.read_sql_query('SELECT * FROM sales.customers', db)
df
# cursor.close()
# db.close()
# Bağlantınızı kapatıyoruz işimiz bitikten sonra


"""
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('chinook.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')
  
    # Write a query and execute it with cursor
    query = 'select sqlite_version();'
    cursor.execute(query)
    
    # Fetch and output result
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))

    # Write a query and execute it with cursor
    query2 = 'SELECT * FROM tracks;'
    cursor.execute(query2)
    
    # Fetch and output results
    results = cursor.fetchall()

    col_names = [i[0] for i in cursor.description]
    
    df = pd.DataFrame(results, columns = col_names)

"""

#################################################
# BONUS
# db = pypyodbc.connect(
#     'Driver={SQL Server};'
#     'Server=DESKTOP-HNUHM85;'
#     'Database=BikeStores;'
#     'UID=sa;'
#     'PWD=16Hek72$;'
# )

orders = pd.read_sql_query('SELECT * FROM sales.orders', db).to_csv('orders.csv', index = False)
order_items = pd.read_sql_query('SELECT * FROM sales.order_items', db).to_csv('order_items.csv', index = False)
staffs = pd.read_sql_query('SELECT * FROM sales.staffs', db).to_csv('staffs.csv', index = False)
stores = pd.read_sql_query('SELECT * FROM sales.stores', db).to_csv('stores.csv', index = False)

pd.read_csv('orders.csv')

####################################################-----END-----####################################################


