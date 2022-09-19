import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import warnings
# warnings.filterwarnings("ignore")
# warnings.warn("this will not show")

plt.rcParams["figure.figsize"] = (10,6)  # görsellerin gelme boyutunu ayarladık

sns.set_style("whitegrid")               # görsellerin arka planı "whitegrid" olsun
pd.set_option('display.float_format', lambda x: '%.3f' % x) # noktadan sonra 3 e kadar gitsin

# Set it None to display all rows in the dataframe
# pd.set_option('display.max_rows', None)   # # None: Tüm satırları göster

# Set it to None to display all columns in the dataframe
pd.set_option('display.max_columns', None)  # None: Tüm sütunları göster

#%% Exploratory Data Analysis (EDA) on Titanic Dataset
# Aim: Applying Exploratory Data Analysis (EDA) and preparing the data to implement the 
# .. Machine Learning Algorithms
# Analyzing the features according to survival status (target feature)
# Preparing data to create a model that will predict the survival status of 
# .. people (So the "survive" feature is the target feature)

###########################
# Reading & Understanding Data
# Let's read the data from file
df = pd.read_csv("titanic.csv", sep="\t")
Let's understand the data
df.head(5)
df.shape
df.info()
df.isnull().sum()
df.isnull().sum()/df.shape[0] * 100
# Roughly 20 percent of the Age data and 80 percent of the Cabin data are missing.
# Only 1 people aboard has no information about where he/she got on the ship.
# This one row can be dropped.
# The heatmap below shows the distribution of the missing data within all data.

sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis');
df.describe().T
df.describe(include = "O").T #  156-->145 -->	2651-->	2 # Aynı kişi 2 ticket almış
df.select_dtypes(include='object')
object_col = df.select_dtypes(include='object').columns
object_col

for col in object_col:
    print(col)
    print("--"*8)
    print(df[col].value_counts(dropna=False))
    print("--"*20)

###########################
# The Detailed Examination of Data Column by Column
##########
# Age
# Lets examine the Age column and decide how we will handle with missing values.
sns.histplot(data=df, x='Age', kde=False, bins=30);
mean = df.Age.mean()
median = df.Age.median()
#print('Age mean:{}\nAge median:{}'.format(mean, median))
print(f'Age mean:{mean}\nAge median:{median}')
sns.boxplot(data=df, x='Age');
df.groupby('Pclass').Age.median()
sns.boxplot(data=df, x='Pclass', y='Age'); # 1. sınıfta yolculuk yapanların yaş ortalaması daha yüksekmiş

df.groupby(['Pclass', 'Sex']).Age.median()
sns.boxplot(data=df, x='Pclass', y='Age', hue="Sex"); # From these boxplots can be interpreted that the older people preferd to be 
# .. in first class, and as the class quality decreases the median age decreases. Lets find these median values.

df.groupby(['Pclass', 'Sex']).Age.transform("median")
sns.boxplot(data=df, x='Pclass', y='Age', hue="Sex");
# In addition to above interpretation, also median of male's age is more than female's in each class quality
# Lets find these median values.
df.groupby(['Pclass', 'Sex']).Age.transform("median")
df['Age'] = df['Age'].fillna(df.groupby(['Pclass', 'Sex']).Age.transform("median"))

##########
# Cabin
# 80 percent of the Cabin data are missing. We can't fill these missing values accurately enough. So let's drop this column
df.drop('Cabin', axis = 1, inplace= True)

##########
# Embarked
# here is just 1 missing value in Embarked column and we can't fill this missing value accurately enough. Let's drop just this row
df.dropna(inplace = True) # Tek bir NaN ı sileyim dedik
df.isnull().sum()

#####################################
# Survive (target feature)
df.Survived.value_counts(normalize=True) # Bunu iyi incelemeliyiz.Target değişkeninin diğer değişkenlere göre analizini yapacağız
sns.countplot(data=df, x='Survived');

##########
# Sex
# Let's examine the affect of each feature on survival status
df.Survived.value_counts() # df.groupby("Sex").Survived.value_counts()
sns.countplot(data=df, x='Sex', hue='Survived');
df.groupby("Sex").Survived.value_counts(normalize=True)
survive = df.groupby(["Sex"])["Survived"].value_counts(normalize=True)
survive

survive = pd.DataFrame(survive)
survive.rename(columns = {"Survived" : "ratio"}, inplace = True)
survive.reset_index(inplace =True)
survive

sns.barplot(data = survive, x = "Sex", y = "ratio", hue = "Survived", ci = None)

###########
# Pclass
sns.countplot(data=df, x='Pclass', hue='Survived');

###########
# SibSp
sns.countplot(data=df, x='SibSp', hue='Survived');

###########
# Parch
sns.countplot(data=df, x='Parch', hue='Survived');

###########
# Embarked
sns.countplot(data=df, x='Embarked', hue='Survived');

##########
# Age
df.groupby("Survived").Age.median()
sns.boxplot(data = df, x = "Survived", y = "Age");
sns.kdeplot(data = df, x = "Age", hue = "Survived", fill=True);

#########
# Fare
df.groupby("Survived").Fare.median()
sns.boxplot(data = df, x = "Survived", y = "Fare");
sns.kdeplot(data = df, x = "Fare", hue = "Survived", fill=True);

###############################################
# Some Feature Engineering
################
# From "Ticket" to "is_group"
# Ticket sürununu kullanamam buradan "is_group" isminde bir sütun oluşturayım
# Bilet tekil mi alınmış, grup olarak mı alınmış
df.Ticket.value_counts(dropna = False).head(5)
df.Ticket.value_counts(dropna = False).tail(5)
ticket = df.Ticket.value_counts()
ticket                                          # Bilet tekil mi alınmış, grup olarak mı alınmış # 2 olanlara grup diyelim
ticket[ticket != 1]
group_list = list(ticket[ticket != 1].index)
group_list
df["is_group"] = df.Ticket.isin(group_list) * 1 # çarpı(*) 1 : olanlara True
df.is_group
sns.countplot(data=df, x='is_group', hue='Survived');

################
# From "SibSp" and "Parch" to "is_alone"
df["is_alone"] = ((df.SibSp == 0) & (df.Parch == 0)) * 1
df.is_alone
sns.countplot(data=df, x='is_alone', hue='Survived');
df.groupby("is_group").is_alone.value_counts()  # Bir kişi grup değilse bu kişi yalnız mış(0-1-83)
# .. ticketları farklı numarada almışlar ama yalnız değiller(0-0-50)

#################
# Let's implement some useful methods on "Name" and "Ticket" features
########
# Name
df.Name
df.Name.sample(10)
# df.Name.str.split(",").str[1].str.split("(").str[0].str.split('"').str[0].str.split('.').str[1].str.strip()
# .. Bunun gibi de böyle bölüp bir şeyler yapabilirsiniz
df.Name.str.extract("\w+\.\s(\w*\s*\w*)")  # \w+\. : alphanumeric noktaya kadar al(örn:Mrs.),
# .. \s: boşluk , (\w*\s*\w*): 0-1 veya more olan alpha numericler(isimler(1 ve ya 2 isim olabilir)), 
# .. boşluk al ya da olmayabilir, 0-1 veya more olan alpha numericler(soyadı için)
# Mr, Mrs ws den sonra gelen isimleri alalım
df["Name"] = df.Name.str.extract("\w+\.\s(\w*\s*\w*)")

########
# Ticket
df.Ticket
# Ticket ların numara kısımlarını alalım
#df.Ticket.str.replace("\S*\s", "") # 1. yol # \S*: boşluk olmayan bir ve more değer, \s: boşluk
df.Ticket.str.extract("(\d*)$")     # 2. yol
df["Ticket"] = df.Ticket.str.extract("(\d*)$")
df.head() # Son hali


########################################################
# Dropping Unnecessary Features
df_final = df.drop(['PassengerId', 'Name' , 'Ticket'], axis=1) # Gereksiz sütunlar
df_final
plt.figure(figsize=(12, 10))
sns.heatmap(df_final.corr(), annot=True);
df_final = df_final.drop(['SibSp', 'Parch'], axis=1)
df_final


#########################################################
# Dummy Operation
df_dummy = pd.get_dummies(data = df_final, drop_first=True)  # Kategorik değişkenleride dummy ile sayısala çevirip ML modeline sokacak
# .. hale getiriyoruz
df_dummy
df_dummy = pd.get_dummies(data = df_dummy, columns=["Pclass"], drop_first=True)
df_dummy

####################################################-----END-----####################################################























