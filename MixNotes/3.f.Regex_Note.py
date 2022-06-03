import numpy as np
import pandas as pd
import re
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)

#%% REGEX - Regular Expression
# A Regular Expression (RegEx) is a special sequence of characters that helps you match or 
# .. find other strings or sets of strings, using a specialized syntax held in a pattern.
# The Python module re provides full support for regular expressions in Python.
# NOTE: https://regex101.com/

# Common Expressions
# \d Any numeric digit from 0 to 9.
# \D Matches any character which is not a decimal digit. This is the opposite of \d.
# \w Any letter, numeric digit, or the underscore character. (Think of this as matching "word" characters.)
# \W Any character that is not a letter, numeric digit, or the underscore character.
# \s Any space, tab, or newline character. (Think of this as matching white-space characters.)
# \S Any character that is not a space, tab, or newline.

# Common Metacharacters
# "[]" A set of characters "[a-m]"
# "\" Signals a special sequence (can also be used to escape special characters)
# "." Any character (except newline character)
# "^" Starts with "^hello"
# "$" Ends with "world$"
# "*" Match zero, one or more of the previous
# "+" Match one or more of the previous
# "?" Match zero or one of the previous
# "{}" Match exactly the specified number of occurrences
# "|" Either or "falls|stays"
# "()" Capture and group

######################################################################################################################
#%% RAW STRING ("r / R")
# Python raw string is created by prefixing a string literal with 'r' or 'R'.
# Python raw string treats backslash (\) as a literal character. This is useful when we want to have a string
# .. that contains backslash and don’t want it to be treated as an escape character
"""
            "Hello \t World"
           /                \
 default string            raw string
   Hello World           Hello \t World
"""
print("backslash: \\")         # 2 slash arka arkaya yazdım tek slash verdi. Tek slash verseydim problem olacaktı
print("new_line char: \\n")    # new_line ifadesinin row string olmasını istersem bu şekilde yapmalıyım
print(r"backslash: \\")        # raw string olarak bana ne yazdıysam verdi
print(r"new_line char: \\n")   # raw string olarak bana ne yazdıysam verdi
my_string = "hello\nworld"     # \n new_line verdi
print(my_string)               # new_line olarak verdi
my_string = r"hello\nworld"
print(my_string)               # Normal string karakteri olarak verdi(new_line vermedi)

#############################
# Invalid Raw String
# print("\") # HATA
# print(r"\") # HATA. Normalde hata vermemesini beklerim.

# print(r"abc\") # HATA
# print(r"abc\\\") # HATA
# Üsttekilerim çalışması için ya boşluk koymamız lazım ya da iki slash olmalı(Alttaki gibi)
print(r"abc\ ")
print(r"abc\\")

######################################################################################################################
#%% COMMON PYTHON REGEX FUNCTIONS(search, match, fullmatch, findall, sub, split)
text1 = "ALT785L41K_?%&.!S,*^#+/()"
text2 = "&.!S,*^#+/()A578LT785L_41K?%"
text3 = "&.!S456,*^#+/()A578LT785L_41K?%"
text4 = "AL   T785L ase8\n"               # NOTE: L ve T arasında 3 boşluk var
text5 = "hello\n\n\nwor ld"
text6 = 'My phone number is 123 456 7890'
text7 = 'My phone number is 123-456 7890'
text8 = 'My phone number is (415) 555-1212'

###############################################
# SEARCH # re.search(): Scan through string looking for a match to the pattern.
re.search("785L",text1)         # <re.Match object; span=(3, 7), match='785L'>

# \d                     # 0-9(dahil) arası decimalleri yakalar
re.search("\d", text1)                    # <re.Match object; span=(1, 2), match='7'>
re.search("\d+",text1)                    # <re.Match object; span=(3, 6), match='785'>
re.search("\d\d",text1)                   # <re.Match object; span=(3, 5), match='78'>
re.search("\d\d\d\d",text1)               # Boş. Ard arda 4 digit yok stringte
re.search("\d\d\d \d\d\d \d\d\d\d",text6)              # <re.Match object; span=(19, 31), match='123 456 7890'>
re.search('\d'*3 + "-" + '\d'*3 + " " + '\d'*4, text7) # <re.Match object; span=(19, 31), match='123-456 7890'>
re.search("(\d\d\d)-(\d\d\d) (\d\d\d\d)", text7)       # <re.Match object; span=(19, 31), match='123-456 7890'>
re.search("(\d\d\d) (\d\d\d)-(\d\d\d\d)", text8)       # Boş.Parantez olduğu için 415 i yakalayamadı
re.search("((\d\d\d)) (\d\d\d)-(\d\d\d\d)", text8)     # Boş.Parantez koyduk ama algılamadı. Çözüm: Kaçış karakteri(\)(Altta)
re.search("(\(\d\d\d)\) (\d\d\d)-(\d\d\d\d)", text8)   # <re.Match object; span=(19, 33), match='(415) 555-1212'>

telno = re.search("(\d\d\d)-(\d\d\d) (\d\d\d\d)", text7) # Bir üsttekini değişkene eşitledik
telno2 = re.search("(\d+)-(\d+) (\d+)", text7)           # 2. yol
telno.group()               # '123-456 7890'    # 2. yol --> telno2.group() 
telno.group(2)              # '456'             # 2. yol --> telno2.group(2) 
telno.group(2,3)            # ('456', '7890')   # 2. yol --> telno2.group(2,3) 

# \D                     # \d nin tam tersi
re.search("\D", text1)           # <re.Match object; span=(0, 1), match='A'>
re.search("\D+",text1)           # <re.Match object; span=(0, 3), match='ALT'>
re.search("\D", text2)           # <re.Match object; span=(0, 1), match='&'>
re.search("\D+",text2)           # <re.Match object; span=(0, 13), match='&.!S,*^#+/()A'>
re.search("\D\D",text1)          # <re.Match object; span=(0, 2), match='AL'>

# \w                     # \w Herhangi bir numara, sayı ve alt çizgiyi yakalar(Sadece alt çizgi)
re.search("\w", text1)           # <re.Match object; span=(0, 1), match='A'>
re.search("\w+",text1)           # <re.Match object; span=(0, 11), match='ALT785L41K_'>
re.search("\w", text3)           # <re.Match object; span=(3, 4), match='S'>
re.search("\w+",text3)           # <re.Match object; span=(3, 7), match='S456'>
re.search("\w\w", text3)         # <re.Match object; span=(3, 5), match='S4'>

# \W                     # \w nin tam tersi
re.search("\W", text1)           # <re.Match object; span=(11, 12), match='?'>
re.search("\W+",text1)           # <re.Match object; span=(11, 16), match='?%&.!'>
re.search("\W", text2)           # <re.Match object; span=(0, 1), match='&'>
re.search("\W+",text2)           # <re.Match object; span=(0, 3), match='&.!'>
re.search("\W\W", text2)         # <re.Match object; span=(0, 2), match='&.'>

# \s                     # Boşluk, sekme veya yeni satır karakteri(Think of this as matching white-space characters)

re.search("\s", text4)           # <re.Match object; span=(2, 3), match=' '>
re.search("\s+", text4)          # <re.Match object; span=(2, 4), match='  '>
re.search("\s", text5)           # <re.Match object; span=(5, 6), match='\n'>  
re.search("\s+", text5)          # <re.Match object; span=(5, 8), match='\n\n\n'>
re.search("\s\s", text5)         # <re.Match object; span=(5, 7), match='\n\n'>

# SEARCH with compile method
comp=re.compile("\d\d")          # önce hangi ifadeyi arıyorsam onu text ti vermeden önce compile a yazıyorum
comp.search(text1)               # <re.Match object; span=(1, 3), match='78'>
num = comp.search(text1)         # Çıktıdaki bazı bilgileri çekmek için değişkene eşitleyip metod uygulayalım
num.start()                      # 3
num.end()                        # 5
num.span()                       # (3, 5)
num.group()                      # '78'

###############################################
# MATCH  # re.match(): Try to apply the pattern at the start of the string.
# Note: If you want to locate a match anywhere in string, use search() instead of match()
text9 = "A7856L41K"

re.match("\d\d",text9)                # Boş. Stringin başında sayı aradı bulamadı.
re.match("\D\d\d",text9)              # <re.Match object; span=(0, 3), match='A78'>
re.match("\w\d+",text9)               # <re.Match object; span=(0, 5), match='A7856'>

###############################################
# FULLMATCH  # re.fullmatch(): Try to apply the pattern to all of the string.
re.fullmatch("\D\d+\D\d+\D",text9)    # <re.Match object; span=(0, 9), match='A7856L41K'> 
re.fullmatch("\D\d+\D\d+",text9)      # Boş. Bir eksik yazınca(Full match olmayınca) çıktı gelmedi
re.fullmatch("\w+", text9)            # <re.Match object; span=(0, 9), match='A7856L41K'>

###############################################
# FINDALL  # re.findall(): Return a list of all non-overlapping matches in the string.
text10 = "O 1, t 10, o 100. 100000"   # Dikkat ilk karakter "O" harfi. Sıfır değil
text11 = "O 1, t 10, o 100. 001000"   # Dikkat ilk karakter "O" harfi. Sıfır değil
text12 = "O1t10o100001000"
text13 = 'set width=20 and height=10'
text14 = "hello world"

re.findall("\d",text10)               # ['1', '1', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0']
#.. Tek karakter istediğim için sayıları tek tek list içinde verdi.
re.findall("\d{2}",text10)            # ['10', '10', '10', '00', '00'] 
# .. En az 2 rakamdan oluşanlardan 2 şer 2 şer sayı getirdi. 100 olandan sadece 10 aldı.
# .. 1000 olsaydı, 10 ve 00 ı olarak ayırıp alacaktı
re.findall("\d{1,4}",text11)          # ['1', '10', '100', '0010', '00']
# .. En az 1 rakamdan ve en çok 4 rakamdan oluşanları, 1 erli, 2 şerli, 3 lü ve 4 lü getirdi
re.findall("\d+",text11)              # ['1', '10', '100', '001000']
re.findall("\d+",text12)              # ['1', '10', '100001000']

re.findall("\w+=\d+",text13)          # ['width=20', 'height=10']
re.findall("\w=\d+",text13)           # ['h=20', 't=10']
re.findall("\w+=\d",text13)           # ['width=2', 'height=1']
re.findall("(\w+)=(\d+)",text13)      # [('width', '20'), ('height', '10')]   # Grup grup aldık

re.findall("hello",text14)            # ['hello']
re.findall("^hello",text14)           # ['hello'     # ^ : başında "hello" varsa
re.findall("world$",text14)           # ['world']    # $ : sonunda "world" varsa

# FINDALL Extract words begining with "f", "e", etc
text15 = 'which foot or hand fell fastest'
re.findall("f[a-z]*",text15)          # ['foot', 'fell', 'fastest']
re.findall("e[a-z]*",text15)          # ['ell', 'est']

###############################################
# SUB  # re.sub(): Return the string obtained by replacing the leftmost non-overlapping occurrences of 
# .. the pattern in string by the replacement repl.
# Note: repl can be either a string or a callable; if a string, backslash escapes in it are processed. 
# .. If it is a callable, it's passed the Match object and must return a replacement string to be used.
text16 = "2004-959-559 # This is Phone Number"

re.sub("\D","",text16)                             # '2004959559'
re.sub("\d",".",text16)                            # '....-...-... # This is Phone Number' # Digitleri nokta ile değiştirdi
re.sub("\d",".",text16, count=4)                   # '....-959-559 # This is Phone Number'
pd.Series(text16).str.replace("\d",".",regex=True) # 0    ....-...-... # This is Phone Number
# .. NOTE: regex=True kullanmazsak  uyarı veriyor kod(Sonraki sürümlerde Python kodunda default regex=False olacak") 

###############################################
# SPLIT  # re.split(): Split the source string by the occurrences of the pattern, returning a list 
# .. containing the resulting substrings.
text16 = "ab56cd78_de fg3hıi49"
re.split("\D+",text16)              # ['', '56', '78', '3', '49']   # Digit olmayan ifadelerden text i split et
# NOTE: En baş ile "ab" arasında bi boşluk olduğunu varsaydığı için orayı da aldı
# NOTE: DIKKAT "de" ile "fg" arasındaki boşluğu almıyor. Orası ile işi yok split in.
re.split("\D+", text16, maxsplit=2) # ['', '56', '78_de fg3hıi49']  
# .. Digit olmayan ifadelerden sadece 2 yerden split et sonraki TÜM ifadeyi bölmeden getir

#######################################################################################################################
#%% # PANDAS FUNCTIONS ACCEPTING REGEX(Count, replace, contains, findall, match, split, extract)
data = [['Evert van Dijk', 'Carmine-pink, salmon-pink streaks, stripes, flecks. #94569# Warm pink, clear carmine pink, rose pink shaded salmon.  Mild fragrance.  Large, very double, in small clusters, high-centered bloom form.  Blooms in flushes throughout the season.'],
        ['Every Good Gift', 'Red.  Flowers velvety red.  #079463895689# Moderate fragrance.  Average diameter 4".  Medium-large, full (26-40 petals), borne mostly solitary bloom form.  Blooms in flushes throughout the season.'], 
        ['Evghenya', 'Orange-pink.  75 petals.  Large, very double #68345_686# bloom form.  Blooms in flushes throughout the season.'], 
        ['Evita', 'White or white blend.  None to mild fragrance.  35 petals #9897#.  Large, full (26-40 petals), high-centered bloom form.  Blooms in flushes throughout the season.'],
        ['Evrathin', 'Light pink. [Deep pink.]  Outer petals white. Expand rarely #679754YH89#.  Mild fragrance.  35 to 40 petals.  Average diameter 2.5".  Medium, double (17-25 petals), full (26-40 petals), cluster-flowered, in small clusters bloom form.  Prolific, once-blooming spring or summer.  Glandular sepals, leafy sepals, long sepals buds.'],
        ['Evita 2', 'White, blush shading.  Mild, wild rose fragrance #AGHJS876IOP#.  20 to 25 petals.  Average diameter 1.25".  Small, very double, cluster-flowered bloom form.  Blooms in flushes throughout the season.']]
  
df = pd.DataFrame(data, columns = ['name', 'bloom']) 
df

# NOTE: DS te bizim uğraşacağımız alanlar buralar daha çok

###############################################
# COUNT   pandas.Series.str.count(): Count occurrences of pattern in each string of the Series/Index
df.bloom.str.count("\d+")   # How many characters are there in each row of "bloom" feature?
df.bloom[1]                 # 4 farklı yerde digit karakter var.
df.bloom.str.count(".")     # "." : Any character (except newline character) # 2.yol --> df.bloom.apply(len) 
df.bloom.str.count("\.")    # How many sentences are there in each row of "bloom" feature? # Noktaları saydı

###############################################
# REPLACE pandas.Series.str.replace(): Replace the search string or pattern with the given value.Equivalent to str.replace() or re.sub(), depending on the regex value
df["bloom"]
df.bloom.str.count("#\S+#")            # Her sütunda 1 tane bu koşulu sağlayan ifade varmış
df["bloom"] = df.bloom.str.replace("#\S+#","",regex = True)
df["bloom"][0]                         # #94569# ifadesi gitti
df.bloom.str.count("#\S+#")            # Hepsi gitti

###############################################
# CONTAINS pandas.Series.str.contains(): Test if pattern or regex is contained within a string of a Series or Index. Calls re.search() and returns a boolean 
df.bloom.str.contains("diameter")      # Normalde böyle diameter içeren satırları bulabilirim
df.bloom.str.contains('\d+"')          # diameter yazısından (sonra sayı + ") geldiği için aynı çıktıyı verir. 
# .. NOTE: Burada   tırnak(") işareti inch anlamında.(Domain knowledge)
# .. Yani sayı ile başlayan, devam eden ve sonra tırnak(") işareti gelenler(Örneğin: 1.25" ).(Inch li ifadelerin içerip içermediğine baktık aslında)
df.loc[df.bloom.str.contains('\d+"')]  # Üstte True gelenleri df şeklinde gösterdi

###############################################
# FINDALL pandas.Series.str.findall(): Find all occurrences of pattern or regular expression in the Series/Index. Equivalent to applying re.findall() on all elements
df.bloom.str.findall("\d+")            # Her bir satırda geçen sayısal değerler
# Bu yukardaki çıktıdaki sayısal değerlerden hangileri çap(diameter) değeri onları versin istiyorum
df.bloom.str.findall('\d+\.\d|\d+"')   # Sayı ile başlayan, devam eden ve nokta ile devam edip sayı ile devam edenleri ya da(|) 
# ..Sayı ile başlayan, devam eden ve sonra tırnak(") işareti gelenleri bul
df.bloom.str.findall('\d+"|\d+\.\d+"') # Sayı ile başlayan, devam eden ve sonra tırnak(") işareti gelenleri ya da(|)
# .. Sayı ile başlayan, devam eden ve nokta ile devam edip sayı ile devam edenleri ve sonra tırnak(") işareti gelenleri bul

###############################################
# MATCH pandas.Series.str.match(): Determine if each string matches a regular expression. Calls re.match() and returns a boolean
# Başta geçen carmine-pink, pink, light pink vs leri çekmek istiyorum yani pink ile başlayan her türlüsünü
df.bloom
df.bloom.str.match("pink|\w+-pink|\w+ pink") # uzun yol
df.bloom.str.match("pink|\w+[- ]?pink")      # 2. yol # \w+[- ]? : Any letter, numeric digit, or the underscore character, tire veya boşluk olsun veya olmasın 
# Reminder: "[]" A set of characters "[a-m]"
df.bloom.str.match(".+pink")                 # 3. yol # .+ : Any character (except newline character) and Match one or more of the previous

###############################################
# SPLIT pandas.Series.str.split(): Split strings around given separator/delimiter and accepts string or regular expression to split on
# Cümle cümle bölmek istiyorum split ile açıklamaları
df.bloom.str.split("\. ")                # Noktadan bölecek # NOT: Noktadan sonrada hep boşluk var veride o yüzden boşluk koyduk
df.bloom.str.split("\. ", expand = True) # Üsttekini df e dönüştürdük

info1 = ["id:345, age:25, salary:1200", "id:346, age:32, salary:1500", "id:347, age:28, salary:1400"]
s1 = pd.Series(info1)
s1

s1.str.split("\D+", expand=True) # Nümerik olmayanlardan bölmesini isteyelim ve df e dönüştürdük
# Baş tarafta splitten dolayı(Boşluk olarak aldığı için orayı) extra sütun oluştu. Onu atalım
df1 = s1.str.split("\D+", expand = True).iloc[:,1:]
df1.columns = ["id","age","salary"]
df1

###############################################
# EXTRACT pandas.Series.str.extract(): Extract capture groups in the regex pat as columns in a DataFrame and returns the captured groups
# En çok kullanacağımız şey extract
# - Parantez içinde yazdığımız şeyleri döndürür
# - Gruplar ile çalışmalıyız bunda
# - df döndürür
s2 = pd.Series(['a3aa', 'b4aa', 'c5aa'])
s2
# s.str.extract("\d+")             # HATA. Çünkü extract kullanırken gruplarla(paranteze alarak) çalışmamız lazım
s2.str.extract("(\d+)")            # Seriyi df e çevirdi. Parantezlerle yaptığım her grup bize satır olarak döndü
# a, b, c bir sütunda , aa, aa, aa farklı sütunda olsun(Rakamın solu ve sağı)
s2.str.extract("(\D+)\d(\D+)")     # \d : Arada nümerik değeri istemediğim için ekledim araya
s2.str.extract("(\D+)\d(\D)(\D+)") # 3 ayrı grup
s2.str.extract("(\D+\d\D+)")       # Birlikte

info2 = ["id:345, age:25, salary:1200", "id:346, age:32, salary:1500", "id:347, age:28, salary:1400"]
s3 = pd.Series(info2)
s3

# Bunu split ile yapmıştık, extract ile yapalım şimdi
df2 = s3.str.extract("(\d+)\D+(\d+)\D+(\d+)") # \D+ : digit olmayanları almadık
df2 # split e göre daha mantıklı

s4= pd.Series(['40 l/100 km (comb)', 
        '38 l/100 km (comb)', '6.4 l/100 km (comb)',
       '8.3 kg/100 km (comb)', '5.1 kg/100 km (comb)',
       '5.4 l/100 km (comb)', '6.7 l/100 km (comb)',
       '6.2 l/100 km (comb)', '7.3 l/100 km (comb)',
       '6.3 l/100 km (comb)', '5.7 l/100 km (comb)',
       '6.1 l/100 km (comb)', '6.8 l/100 km (comb)',
       '7.5 l/100 km (comb)', '7.4 l/100 km (comb)',
       '3.6 kg/100 km (comb)', '0 l/100 km (comb)', 
       '7.8 l/100 km (comb)'])
s4

s4.str.extract("(\d+\.\d+|\d+)")     # 1. yol
s4.str.extract("(\d*\.?\d+\d*)")     #  \d* : 1 veya daha fazla digit olsun ya da olmasın veya devamında digit olsun , 
# ..  .?: nokta olsun veya olmasın. \d* : digit olsun veya olmasın veya devamında digit olsun
s4.str.extract("(\S+)")              # (\S+) space i görene kadar her şeyi(Any character that is not a space, tab, or newline) aldı # 3. yol
s4.str.extract('(\d*.\d*).+/(\d*)')  # Extract first and second number # .+: Herhangi bir karakter(except newline character) veya daha fazlası

s5 = pd.Series(['06/2020\n\n4.9 l/100 km (comb)',
'11/2020\n\n166 g CO2/km (comb)',                                 
'10/2019\n\n5.3 l/100 km (comb)',
'05/2022\n\n6.3 l/100 km (comb)',
'07/2019\n\n128 g CO2/km (comb)',
'06/2022\n\n112 g CO2/km (comb)',                                                 
'01/2022\n\n5.8 l/100 km (comb)',
'11/2020\n\n106 g CO2/km (comb)',
'04/2019\n\n105 g CO2/km (comb)',
'08/2020\n\n133 g CO2/km (comb)',
'04/2022\n\n133 g CO2/km (comb)'])
s5

s5.str.extract("(\d\d).(\d\d\d\d)") # Extract date as month and year separately
s5.str.extract("(\d{2}).(\d{4})")   # Extract date as month and year separately 
s5.str.extract("(\d*).(\d*)")       # Extract date as month and year separately
s5.str.extract("(\d\d)/(\d*)")      # Extract date as month and year separately
s5.str.extract("(\d\d)/(\d\d\d\d)") # Extract date as month and year separately
s5.str.extract("(\d+).(\d+)")       # Extract date as month and year separately
s5.str.extract("(\S+)/(\S+)")       # Extract date as month and year separately

s5.str.extract('(\d+/\d+)\s+(\d+.\d+|\d+)') # Extract date and comsuption value(4.9, 166, etc.)
# (\d+/\d+) : tarihi aldı,.. \s+: new_line ı aldı, .. (\d+.\d+|\d+): rakamı aldı

s6 = pd.Series(['\n\n4.9 06/2020 l/100 km (comb)',
'\n\n166 11/2020 g CO2/km (comb)',                                 
'\n\n5.3 10/2019 l/100 km (comb)',
'\n\n6.3 05/2022 l/100 km (comb)',
'\n\n128 07/2019 g CO2/km (comb)',
'\n\n112 06/2022 g CO2/km (comb)',                                                 
'\n\n5.8 01/2022 l/100 km (comb)'])
s6

# 06/2020 olan sütuna ulaşmak istiyorum
s6.str.extract("\S+\s(\d+)/(\d+)")   # 
s6.str.extract("(\d+)/(\d+)")        # (\d+): digit veya dahası , slash , (\d+) digit veya dahası

####################################################-----END-----####################################################





