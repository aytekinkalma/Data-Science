import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import random



"""1-The hourly wages in a particular industry are normally distributed with mean 
$13.20 and standard deviation $2.50. A company in this industry employs 40 
workers, paying them an average of $12.20 per hour. Can this company be accused
 of paying substandard wages? Use an α = .01 level test. (Wackerly, Ex.10.18)"""

xbar = 13.20
sigma = 2.50
n = 40
mu = 12.20
z = (xbar - mu) / (sigma/np.sqrt(n))
z
#2.5298221281347035

p_value=1-stats.norm.cdf(z)
p_value
#0.005706018193000872

alpha = 0.01

if p_value < alpha:
    print("Reject the null")
else:
    print("Fail to reject the null")

#Reject the null


"""EXERCISE 2.Shear strength measurements derived from unconfined compression 
tests for two types of soils gave the results shown in the following 
document (measurements in tons per square foot). Do the soils appear to 
differ with respect to average shear strength, at the 1% significance level?"""

df=pd.read_csv("C:\\Users\\hp\\Desktop\\DataScience\\STATİSTİCS\\assigment3\\soil - Sheet1.csv")

df.head()
"""
   Soil1  Soil2
0  1.442  1.364
1  1.943  1.878
2  1.110  1.337
3  1.912  1.828
4  1.553  1.371"""

#H0 : μ1=μ2
#H1 : μ1!=μ2


indTest = stats.ttest_ind(df["Soil1"].dropna(), df["Soil2"].dropna(), equal_var=True, alternative='two-sided')

indTest
#Out: Ttest_indResult(statistic=5.1681473319343345, pvalue=2.593228732352821e-06)

alpha = 0.01

if indTest.pvalue < alpha:
    print("Reject the null")
else:
    print("fail to reject the null")

#Reject the null



"""EXERCISE 3. The following dataset is based on data provided by the World Bank 
(https://datacatalog.worldbank.org/dataset/education-statistics). World Bank
 Edstats.  2015 PISA Test Dataset

Get descriptive statistics (the central tendency, dispersion and shape of
                            a dataset’s distribution) for each continent 
group (AS, EU, AF, NA, SA, OC).
Determine whether there is any difference (on the average) for the math 
scores among European (EU) and Asian (AS) countries
 (assume normality and equal variances). Draw side-by-side box plots."""
df1=pd.read_csv("C:\\Users\\hp\\Desktop\\DataScience\\STATİSTİCS\\assigment3\\2015 PISA Test - Sheet1.csv")
df1.head()
df1.columns
"""Index(['Country Code', 'Continent_Code', 'internet_users_per_100', 'Math',
       'Reading', 'Science'],
      dtype='object')"""

df1.groupby("Continent_Code")["Math"].value_counts()

sns.boxplot(y='Math',x='Continent_Code',data=df1);
df1[df1['Continent_Code']=='EU']["Math"]
df1[df1['Continent_Code']=='AS']["Math"]




indTest1 = stats.ttest_ind(df1[df1['Continent_Code']=='EU']["Math"].dropna(), 
                           df1[df1['Continent_Code']=='AS']["Math"].dropna(),
                           equal_var=True, alternative='two-sided')
indTest1

#Ttest_indResult(statistic=0.870055317967983, pvalue=0.38826888111307345)

alpha = 0.01

if indTest1.pvalue < alpha:
    print("Reject the null")
else:
    print("fail to reject the null")

#fail to reject the null




"""EXERCISE 4.  A gym operator organized a 2-month exercise and diet program 
for 15 customers suffering from their excess weight. To evaluate whether 
this diet program was effective, he measured the customers' starting and 
ending weights and recorded them in the computer. Did the exercise and 
diet program have an impact on customers' weight loss? Use an α = .01 level test.
  Weight Dataset"""



df2=pd.read_csv("C:\\Users\\hp\\Desktop\\DataScience\\STATİSTİCS\\assigment3\\weight - Sheet1.csv")

df2
"""
    ID  starting  ending
0    1        76      72
1    2        81      82
2    3        86      84
3    4        71      71
4    5        88      83
5    6        78      74
6    7        76      70
7    8        81      80
8    9        79      78
9   10        77      79
10  11        83      80
11  12        77      76
12  13        79      77
13  14        81      83
14  15        83      82"""





depTest = stats.ttest_rel(df2["ending"], df2["starting"], alternative='greater')
depTest

#Ttest_relResult(statistic=-2.6780834840499255, pvalue=0.9909935348249338)


alpha = 0.01

if depTest.pvalue < alpha:
    print("Reject the null")
else:
    print("fail to reject the null")

#fail to reject the null





