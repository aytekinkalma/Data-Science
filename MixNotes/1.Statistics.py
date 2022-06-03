# STATISTICS
# 1.Kodlar
# 2.Konu Anlatımı

########################################################################################
# 1.KODLAR
########################################################################################
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
salary = [102,33,26,27,30,25,33,33,24]
len(salary)

print("mean:", np.mean(salary))
print("median:", np.median(salary))
print("mode:", stats.mode(salary))

########################################
# Min & Max & Range & Q1 & Q2 & Q3 & IQR & std & var
data = [32, 36, 46, 47, 56, 69, 75, 79, 79, 88, 89, 91, 92, 93, 96, 97, 101, 105, 112, 116]
np.min(data)
np.max(data)
np.max(data)-np.min(data) # Range
np.percentile(data,25)    # Q1
np.percentile(data,50)    # Q2
np.percentile(data,75)    # Q3
stats.iqr(data)           # IQR # also IQR = Q3-Q1
np.std(data)
np.var(data)

list1 = [102, 33, 26, 27, 30, 25, 33, 33, 24]
print("skewness: ", stats.skew(list1, bias=False))
print("kurtosis: ", stats.kurtosis(list1, bias=False))

########################################
sns.get_dataset_names()
df = sns.load_dataset("mpg") # mpg : miles per gallon


#######################################
# Boxplot
data = [32, 36, 46, 47, 56, 69, 75, 79, 79, 88, 89, 91, 92, 93, 96, 97, 101, 105, 112, 116]
plt.boxplot(data)
sns.boxplot(data2)

data2 = [32, 36, 46, 47, 56, 69, 75, 79, 79, 88, 89,145]
plt.boxplot(data2)
sns.boxplot(data2)

df.boxplot("mpg");
sns.boxplot(df["mpg"])


#######################################
# Scatter Plot
# 2 adet sayısal değişken ile kullanılır
plt.scatter(x=df["weight"] , y=df["acceleration"])

sns.scatterplot(x="weight", y="acceleration",data=df)
sns.scatterplot(x="mpg", y="horsepower",data=df)
sns.scatterplot(x="acceleration", y="horsepower",data=df)

#######################################
# Histogram
# 1 adet sayısal değişken ile
plt.hist(df["mpg"], bins=20)
sns.histplot(df["mpg"])

# NOT: 1 adet kategorik değişkenle benzer çıktı aldıran "count plot"
#######################################
# Pie Plot
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs') # Hogs u dilimlenmiş olarak gösterecek

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

#######################################
# Heatmap
# plt.heatmap           # Hata #  module 'matplotlib.pyplot' has no attribute 'heatmap'
sns.heatmap(df.corr())

########################################
# Correlation
x = [93, 84, 82, 78, 98, 70]
y = [13, 10, 11, 8, 15, 9]
np.cov(x, y)
a = np.corrcoef(x,y)
a
df.corr()
df["cylinders"].corr(df["displacement"])
df.describe().T              # Betimsel istatistikler
stats.pearsonr(df["cylinders"], df["displacement"])[0] # 0. indexte korelasyon sonucu var
# .. eğer oraya 1 yazılsaydı "p-value" değerini görürdük çıktıda
stats.pearsonr(df["cylinders"], df["displacement"])[1]
stats.spearmanr(df["cylinders"], df["displacement"])[0]
stats.spearmanr(df["cylinders"], df["displacement"])[1]

#%%
########################################################################################
# 2.KONU ANLATIMI
########################################################################################
####################################################3
# DATA TYPES & PATTERN & GRAPHS
"""
According to Wikipedia:
Statistics is the discipline that concerns the collection, organization, 
.. analysis, interpretation and presentation of data.

According to Merriam-Webster's Collegiate Dictionary:
Statistics is a branch of mathematics dealing with the collection, analysis, 
.. interpretation, and presentation of masses of numerical data.
"""

# Two basic divisions of statistics are descriptive and inferential statistics
# 1.Descriptive statistics are numbers that are used to summarize and describe data.
# 2.Inferential statistics is a way of making inferences about populations based on samples.

# The American Statistical Association defines the statistics as ; “the science of 
# .. learning from data and of measuring, controlling, and communicating uncertainty"

# Data scientist: A person who knows more statistics than a programmer and more
# .. programming than a statistician

# Data science is at the intersection of computer science, math&statistical skills,
# .. and domain knowledge

# Data:Data are characteristics or information, usually numerical, that are 
# .. collected through observation.

# There are two main types of data types: numerical (or quantitative data) and
# .. categorical (or qualitative) data.

# Numerical --> 1.Continious(infinite options) 2.Discrete(finite options)
# 1.Continious --> Age, Weight, Blood pressure
# 2.Discrete --> Shoe size, Number of children
"""
Discrete data contains only finite values. For example the number of students in a school, 
.. the number of buildings in a city, the number of desks in a classroom, etc. A possible 
.. number of students in a school cannot be infinite. It can be 300, 301 or 302, but it 
.. cannot be something between 300 and 301. You can somehow count the values it can take.

Continuous data can have an infinite number of values between any two values. For example 
.. age, height or weight of a person, the time assigned to a special task, house price, 
.. stock price, etc. A stock price might be 10, 11 or 10.4565 dollars, so it can have an 
.. infinite number of values. The age of a person is a continuous data because your exact
.. age might be 28, 28.1 or 28.5.
"""

# Categorical --> 1.Ordinal(Data has a hierarchy) 2.Nominal(Data has no hierarchy)
# 1.Ordinal --> Pain severity, Satisfaction rating, Mood
# 2.Nominal --> Eye color, Dog breed, Blood type
"""
Ordinal and Nominal Data
An ordinal data is a categorical one for which the categories are ordered 
.. from low to high in some sense.
A nominal data is a categorical data that do not have a natural order or ranking.
"""

# Data Patterns in Statistics
# In general, we can define the patterns in data as follows: center, spread,
# .. shape, and unusual features.

# Center : Medyan
# Spread : Less spread, wide spread
# Shape  : Symmetry, Number of peaks, Skewness, Uniform
"""
Symmetry: Distribution, the two sides of the distribution are equal and symmetrical.
Number of Peaks: Distributions with one or multiple peaks. Distribution with one
.. clear peak is known as unimodal, and distribution with two clear peaks is called bimodal. 
.. A single peak symmetric distribution at the center, is referred to as bell-shaped.
Skewness : Skewed right, Skewed left
Uniform: When the set of observations has no peak and have data equally spread across 
.. the range of the distribution, then the distribution is called a uniform distribution
"""
# Unusual Features : Gaps, Outliers 
"""
Gaps: Gaps points to areas of a distribution having no observations. It is like for example;
.. there is no bar(stick) in histogram graph
"""

# Pie Chart
# A pie chart is a circle having a “slice of the pie” for each category.
# Pie charts are effective for displaying the relative frequencies of a SMALL number
# .. of categories
# Tips: When slices become too small, pie charts have to rely on colors,
# .. textures or arrows so the reader can understand them
# Avoid: Pie charts are not recommended if there are too many categories of data being presented

# Bar Chart
# A bar chart is a chart that presents categorical data with rectangular bars with 
# .. heights proportional to the values that they represent
# Here is how to read a bar chart.
# The columns are positioned over a label that represents a categorical variable.
# The height of the column indicates the size of the group defined by the column label.
# Tips:
# The bars can be plotted vertically or horizontally. 
# A vertical bar chart is sometimes called a column chart.
# Avoid:
# Do not start the axis with a value above zero. If you do this, you shrink the bars 
# .. and get confusing visuals.
# Do not use the rainbow effect. Although coloring the graphics sounds good, it often 
# .. makes the tables difficult to understand.
# Do not use more display dimensions than data dimensions. Three-dimensional bar charts 
# .. are not as clear as two-dimensional bar charts.

# Histogram
# A histogram is a graphical representation of a distribution
# Your choice of bin width determines the number of class intervals.
# Tips:
# With bar charts, the labels on the X axis are categorical; 
# .. with histograms, the labels are numerical (quantitative)

# Population
# A population is the total group about whom you want to make conclusions

# Sample
# A sample is a subset of the population for whom you actually have data.
# Tips:We observe samples but are interested in populations.
# We learn about the population by taking the sample from the collection

# Population & Sample
# The mean x̄ and the standard deviation s
# .. The formulas that define x̄ and s refer to sample data
# .. They are sample statistics.(x̄ and s)
# The population mean is the average of all observations in the population
# The population standard deviation describes the variability of the population 
# .. observations about the population mean
# Note: A parameter is a numerical summary of the population, 
# .. and a statistic is a numerical summary of a sample

# To draw valid conclusions from your results, you have to carefully decide 
# ..how you will select a sample that is representative of the group as a whole. 
# ..There are two types of sampling methods:
# 1.Probability Sampling: Involves random selection, allowing you to
# .. make strong statistical inferences about the whole group
# 2.Non-Probability Sampling: Involves non-random selection based on
# .. convenienve(uygun koşullar) or other criteria, allowing you to easily collect data
"""
Sampling Techniques

1.Probability Sampling Methods
Probability sampling means that every member of the population has a chance of being selected.

a.Simple Random Sample: In a simple random sample, every member of the population 
.. has an equal chance of being selected.
Note: Simple Random Samples represents population better than the others
b.Systematic Sample: Every member of the population is listed with a number, but
.. instead of randomly generating numbers, individuals are chosen at regular intervals.
c.Stratified Sample: Stratified sampling involves dividing the population into 
.. subpopulations that may differ in important ways.
d.Cluster Sample: Cluster sampling involves dividing the population into subgroups,
.. but each subgroup should have similar characteristics to the whole sample.
# Linkteki 4 lü resme bak, aralarındaki farkı anlatıyor
https://www.scribbr.com/methodology/sampling-methods/

2.Non-probability Sampling Methods
In a non-probability sample, individuals are selected based on non-random criteria, and not every
..individual has a chance of being included.

a.Convenience sample(Elverişli örnekleme): A convenience sample includes the observations who are 
.. most accessible to the researcher.
b.Voluntary response sample(Gönüllü örnekleme): Similar to the convenience sample, the voluntary 
.. response sample is basically based on ease of access. Instead of the researcher
.. selecting participants and communicating directly with them, participants volunteer themselves.
c.Purposive sample(Amaçsal örnekleme): This sampling method involves the researcher
.. using their expertise to select the sample that best suits their research purpose.
d.Snowball sample(Kartopu örneklemesi): If the population is difficult to access, snowball sampling can be
.. used to recruit participants through other participants.
e.Quota sample(Kota örnekleme):(For example: 50 men and 50 women)
# Linkteki 4 lü resme bak, aralarındaki farkı anlatıyor
https://www.scribbr.com/methodology/sampling-methods/
"""

#%% CENTRAL TENDENCY & DISPERSION

# Description: The central tendency concept is that one single value can best describe the data
# Mean, median, and mode. 
# ..Essentially, all three of them refer to a single aspect called the Central Tendency.

# Mean: The mean is equal to the sum of the values in the dataset divided by the number of values
# Not: Balance point
# Population mean: μ , Sample mean: x-
# Under various conditions, one measure of central tendency might become more appropriate than others
# Note: The mean is the balance point of the data

# Median: The median is the middle score for a dataset that has been sorted from small to large
# Not: n+1/2 --> Position of the median in a dataset
# Not: Median: Pysical middle point
# Outliers less affect the median
# The median is the middle score. If the sample size is 9(odd), the fifth element is the median
# .. If the sample size is 10(even), we simply have to take the middle two scores and average the result

# Mean vs Median
# While the mean is the balance point of the data, the median is the middle point.
"""
ATTENTION:
The mean can be highly influenced by an outlier. 
#####The mean is better if a large set of scores does not have an outlier#####

The median is not sensitive to outliers. 
#####The median is better if a small set of scores has an outlier#####

Generally, if the shape is;
Perfectly symmetric, the mean equals the median.
Skewed to the right(Positively skewed), the mean is larger than the median.
Skewed to the left(Negatively skewed), the mean is smaller than the media
"""
# Mode: The mode is the most frequent score in a dataset. 
# It represents the highest bar in a histogram or bar chart
# NOTE: If all observations are repeated an equal number of times, then the mode does not exist

# Note: In a symmetrical distribution, the mean, median and mode are identical
# 

# Calculate Mean, Median and Mode with Python
# We use the "Numpy" library for the mean and median, and the "SciPy" library for the mode
import numpy as np
from scipy import stats
a = [102, 33, 26, 27, 30, 25, 33, 33, 24]
print("mean:", np.mean(a))
print("median:", np.median(a))
print("mode:", stats.mode(a))

# Dispersion(Measure of Spread)
# For example; 𝜇 =100 for two dataset
# The first population is much more dispersed than the second population, however, 
# .. the mean value for both populations is the same. Therefore;
# .. (Tips): we can say a dispersion explains something more than the central tendency does

# Range, standard deviation and interquartile range are the three widely used measures of dispersion

# Range
# The range is the simple measure of dispersion, which is defined as the difference 
# .. between the maximum and the minimum values

# Standard Deviation(𝜎)
# The most commonly used measure of dispersion is the standard deviation (𝜎). 
# Standard deviation measures the spread around the mean
# It is also expressed as the square root of variance.
# Variance is defined as the average of the squared differences from the mean
# Variance= SUM(xi-𝜇)/N # 𝜇 = population mean # 𝑁 = number of items in the population
# Like the range, also standard deviation is affected by outliers
# One value could contribute greatly to the results of the standard deviation
# This also means the standard deviation is a good indicator of the existence of outliers
# The standard deviation is also useful when comparing the spread of 
# .. two different datasets that have the same mean.
# The dataset with the smaller standard deviation has a narrower spread of 
# ..measurements around the mean and therefore usually has relatively less high or low values
# Tips: The data with the smaller standard deviation has a narrower spread of 
# .. measurements around the mean

# Interquartile Range (IQR)
# Quartiles are the values that divide a group of numbers into quarters.
# Q1 or the 25th percentile is the first quartile and defined as the middle 
# .. number between the smallest number and the median of the dataset.
# Q2 is the second quartile which is the median of the whole dataset.
# Q3 or 75th percentile is the third quartile which is the middle value between 
# .. the median and the highest value of the dataset
"""
For example, a dataset consists of those numbers: 0,4,5,7,8,9,10,12,13,14,15,16,20.
The median (Q2) is the value in the middle of the list. In this case, 10 is the median number.
The first quartile (Q1) is the middle number in between the smallest number (0) and the median 
.. (10) which is 7. In other words, the middle number between 0 and 10 is 7.
The third quartile (Q3) is the middle value between the median (10) and the highest value (20)
.. in this case that will be 14. In other words, the middle number between 10 and 20 will be 14.
Interquartile Range(IQR) is the difference between Q3 and Q1. In this case:
IQR = Q3 - Q1
IQR = 14 - 7 = 7
"""
# An outlier is a data point that differs significantly from other observations. 
# .. IQR helps us to make a technical description of outliers
# A typical definition of the outlier is, any data point more than 1.5 interquartile 
# .. ranges (IQRs) below the first quartile or above the third quartile.1
# Outliers are any data point below (Q1 - 1.5 * IQR) or above (Q3 + 1.5 * IQR)
# Tips: Outlier is, any data point more than 1.5 IQR below the Q1 or above the Q3.

# Box Plot
# Box plots (also called box-and-whisker plots or box-whisker plots) give a good 
# .. graphical image of the concentration of the data
# They also show how far the extreme values are from most of the data
# A box plot is constructed from five values: the minimum value, the first quartile, 
# .. the median, the third quartile, and the maximum value. We use these values to 
# .. compare how close other data values are to them.
# One of the more effective graphical summaries of a data set, the box plot generally 
# .. shows mean, median, 25th and 75th percentiles, and outliers

# Box Plot (Min & Max)
# he two whiskers extend from the first quartile to the smallest value and from 
# .. the third quartile to the largest value. The median is shown in the middle of the box.
# Tips: You may encounter box-and-whisker plots that have dots marking outlier values. 
# .. In those cases, the whiskers are not extending to the minimum and maximum values.

# Calculate Range, Variance, Std Dev, Quartiles and IQR with Python
# We can easily calculate range, variance and standard deviation values with NUMPY.
import numpy as np
from scipy import stats

salary = [102, 33, 26, 27, 30, 25, 33, 33, 24]
print("Range: ", (np.max(salary)-np.min(salary)))
print("Variance: ", (np.var(salary)))
print("Std: ", (np.std(salary)))
print("Q1:", (np.percentile(salary, 25)))
print("Q2:", (np.percentile(salary, 50)))  #q2 is also called median
print("Q3:", (np.percentile(salary, 75)))
print("IQR:", (stats.iqr(salary)))

"""
OUTPUT:
    
Range:  78
Variance:  539.5555555555555
Std:  23.22833518691246
Q1: 26.0
Q2: 30.0
Q3: 33.0
IQR: 7.0
"""
#%% Correlation and Covariance
# Scatter Plot
# A scatter plot shows the direction of a relationship between the variables
# A way to display the relation between two variables x and y. 
# .. The most common and easiest way is a scatter plot.

# A clear direction happens when there is either:
# .. 1.High values of one variable occurring with high values of the other variable 
# .. or low values of one variable occurring with low values of the other variable.
# .. 2High values of one variable occurring with low values of the other variable.

# You can determine the strength of the relationship by looking at the scatter plot 
# .. and seeing how close the points are to a line, a power function, an exponential function, 
# .. or to some other type of function.

# When you look at a scatterplot, you want to notice the overall pattern and any 
# .. deviations from the pattern The following scatterplot examples illustrate these concepts.
# a.Positive linear pattern(strong)
# b.Negative linear pattern(strong)
# c.Positive linear pattern(weak)
# d.Negative linear pattern(weak)
# e.Linear pattern w/ one deviation(one point is out of linear point line)
# f.Exponential growth pattern(Like a curve)
# g.No pattern(Messy pattern)

# Tips: A scatter plot displays the relationship between two numerical variables.
# .. This type of plot not only shows the functional form of the relationship(linear or non-linear),
# .. but also gives information about the degree of this relationship.

# Correlation and Covariance
# Correlation is one of the most common statistical concepts. 
# .. It is a statistical technique that determines how one variable changes with another variable. 
# .. It gives us the degree of the linear relationship between the two variables

# Covariance provides similar information with correlation. However, correlation goes 
# .. beyond covariance and gives information also about the strength of the relationship 
# .. between two variables. Covariance does not provide information about the strength of 
# .. the relationship
# Covariance: The expected value of the product of the deviations of two random variables 
# .. from their respective means.

# Both can be positive or negative. Correlation or covariance is positive if one 
# .. increases the other also increases and negative if one increases the other decreases

# Tips: Covariance shows the direction of the linear relationship between two variables.
# .. Correlation gives information about the DIRECTION and the STRENGHT of the linear 
# .. relationship between two variables
"""
Population Covariance⟹Cov(X,Y)=∑ni=1(Xi−X¯¯¯¯)(Yi−Y¯¯¯¯)N
Sample Covariance⟹Cov(x,y)=∑ni=1(xi−x¯¯¯)(yi−y¯¯¯)n−1
Xi=data value of X
Yi=data value of Y
X¯¯¯¯=mean of X
Y¯¯¯¯=mean of Y
N=number of data values
After calculating the covariance the correlation is calculated as:
Correlation=Cov(X,Y) / σXσY or Cov(x,y) / sxsy
We can say correlation is calculated by the division of covariance
.. by the standard deviation of variables
Because the correlation is a number between -1 and 1 it is often referred to as 
.. the correlation coefficient
"""

# Example
"""
Temperature (°F) = 93, 84, 82, 78, 98, 70 (Variable x)
Number of People = 13, 10, 11, 8, 15, 9 (Variable y)
xi    xi−x¯     yi	 yi−y¯      (xi−x¯¯¯)(yi−y¯¯¯) 
93	8.8333 	    13	   2	           17.667
84	-0.1667 	10	  -1               0.167
82	 -2.1667	11	   0	           0
78	-6.1667 	8	  -3	           18.5 
98	 13.8333	15     4 	           55.333
70	 -14.1667	9	  -2	           28.333
Cov(x,y)=∑ni=1(xi−x¯¯¯)(yi−y¯¯¯) / n−1=17.667+0.167+0+18.5+55.333+28.3336−1=1205=24
Correlation=Cov(x,y)sxsy=24 / 10.128×2.608=24 / 26.409=0.909
he 0.909 which is called the correlation coefficient shows that there is a very strong
.. and positive correlation between temperature and number of people
"""
# Tips: Correlation is calculated by the division of covariance by the standard deviation of variables.
# .. While covariance values are not standardized, correlation values are standardized.
# .. In fact, nowadays no one does these manual calculations anymore. All calculations are made
# .. with a single line of code with a computer software.

# Pearson Correlation Coefficient
# There are different methods to calculate the correlation coefficient between two variables. 
# .. The most famous one is the Pearson Correlation Coefficient. It is a number between -1 and 1
# .. that indicates the strength of the relationship.
# -1 : Indicates complete negative correlation (Perfect negative correlation)(Perfect linear relationship)
# +1 : Indicates complete correlation (Perfect Positive correlation)(Perfect linear relationship)
#  0 : Indicates no correlation (There is no linear relationship)
# The Pearson correlation coefficient is calculated as follows:
# r=∑(x−μx)(y−μy) / √∑(x−μx)^2 x √∑(y−μy)^2

# It captures not only the strength but also the direction of the linear association
# .. between two continuous variables. And it tries to draw a line of best fit through 
# .. the data points of two variables

# Tips: Pearson Correlation Coefficient tries to draw a line of best fit through 
# .. the data points of two variables.
# Linear transformations have no effect on Pearson's correlation coefficient.
# Pearson's correlation is symmetric in the sense that the correlation of X with Y 
# .. is the same as the correlation of Y with X

# Calculate Correlation and Covariance with Python
# We can easily calculate covariance and correlation with numpy. 
# The results of np.cov() and np.corrcoef() commands are displayed in matrix form


#with numpy library
import numpy as np
temp=[93,84,82,78,98,70]
number_of_people=[13,10, 11, 8, 15, 9]
print("covariance: ", np.cov(temp, number_of_people))
print("correlation: ", np.corrcoef(temp, number_of_people))

# OUTPUT: cov:  [[102.56666667  24.        ]
                 [ 24.           6.8       ]]
        corr: [[1.         0.90876934]
              [0.90876934 1.        ]]

#with scipy library
from scipy import stats
print("correlation coefficient and p-value: ", stats.pearsonr(temp, number_of_people))

# OUTPUT:correlation coefficient and p-value:  (0.9087693361896165, 0.012104893069677013)


# Explanatory Variable(Independent Variable)
# Response Variable(Dependent Variable)
# When determining correlation Explanatory Variables(Independent Variables) 
# .. and Response Variables(Dependent Variables) are NOT necesarry

# NOT: Don't interpret correlation just by looking at the scatter plot
# .. because the scales of the axes may be different

# Normal Distribution
"""
The normal distribution, also called the gaussian or bell curve, is a naturally 
.. occurring distribution in most cases. The normal distribution can be seen in tests
.. like the GRE or SAT. Most students will get an average score (C), while fewer 
.. students will receive a B or D. An even smaller number of students score an F or an A.
.. That generates a distribution that resembles a bell that is why the normal distribution
.. is also called the bell curve. The form of the normal distribution is symmetrical. 
.. Half of the data will fall to the right of the mean and the other half will fall to the left.
.. Most of the data follow this type of pattern. The normal distribution is therefore commonly
.. used in industry, statistics and public bodies.

# NOTE: There are many things are well modelled by the normal distribution such as;
# .. IQ scores in the world follow the normal distribution pattern but also 
# .. There are many things are NOT well modelled by the normal distribution such as;
# .. House prices, incomes, human weights(Many are right-skewed)

# Additional examples;
For example;
- Weights of people,
- Blood pressures,
- Scores on a test,
- IQ scores,
- Wages,

 follow the normal distribution pattern.
"""
# Single Peak
# Median = Mean
# σ + 2u = %95


# NOTE: Probability of any specific value in normal distrubution is "0" because it is 
# .. a continuous distribution. We can find probability in a certain interval

# Properties of a Normal Distributions
# The normal distribution has its characteristics. The most important of these are listed below.
# 1.Normal distributions are symmetric around their mean. 
# 2.The mean, median, and mode of a normal distribution are equal. 
# 3.The total area under the normal curve is equal to 1.0. 
# 4.Normal distributions are described by two parameters, the mean (μ) and the standard deviation (σ). 

"""
# Parameter : A number that describes the data from a population
# Statistics: A number that describes the data from a sample
# Population: u , σ (These are parameters) ,
# .. u:characterizes the POSITION of the normal distribution
# .. if you increase the mean the curve will follow and move towards right, if you decrease ... left
# .. σ: u:characterizes the SPREAD of the normal distribution. if you increase... more spread(and curve
# .. get "flatter"(Flat --> flatter(Comperative))), 
# .. if decrease ... less spread(Curve gets taller)
# Sample: Xbar(X ortalama) , s (These are statistics)

We are above mentioned about that that the total area under the normal curve is equal to 1.0. 
By using the two parameters we can split the area under the normal distribution curve. 
In other words, the area under the normal distribution curve tells us what percentage of 
.. the data falls within a certain number of standard deviations from the mean:

Approximately 68% of the area of a normal distribution is within one standard deviation of the mean,
Approximately 95% of the area of a normal distribution is within two standard deviations of the mean,
Approximately 99,7% of the area of a normal distribution is within three standard deviations of the mean.
"""

####### Z-Score
"""
We calculate the probability of an outcome by determining the area under the normal distribution curve. 
However, sometimes we need to find the probability of an outcome that does not fall directly
 within 1, 2, or even 3 standard deviations from the mean.

We use the z score to standardize the normal distribution curve. 
Instead of mean in the normal distribution curve we insert the zero. 
Similar to the standard deviations to the left and right of the mean, 
we insert 1,2,3 and -1,-2,-3 to the left and right of the zero. The z scores 
represent the standard score. Therefore, a z-score of 1, is one standard deviation
 above the mean, and a z-score of -1, is one standard deviation below the mean.

Rather than creating a normal distribution curve for each dataset, we can use 
one standard normal distribution curve by z-score and use the formulas to find probabilities.

The basic z score formula for a z-score is:
z=x−μσ


For example, let’s say you have a test score of 205. The test has a mean (μ) of 
180 and a standard deviation (σ) of 20. Assuming a normal distribution, your z score would be:
z=205−18020
z=2520
z=1,25


The z score tells you how many standard deviations from the mean your score is.
 In this example, your score is 1,25 standard deviations above the mean.
"""

######## Z Table
"""
Z Table
The z-table helps us to make a probability calculation by the z-score. 
The table provides us with accurate proportion values for all z scores within -3.9 and +3.9 
standard deviations from the mean. Therefore, we can find the probability for any
 dataset that is normally distributed by using the z-sore in the z-table. When using
 a z table, you should keep in mind that the values provided in the table represent 
 the probability at or below the indicated z score. Therefore, if you wish to find the
 probability of an outcome occurring after, or to the right, of the z-score you will 
 need to use the fact that the total area under the normal curve is equal to 1.0 and 
 subtract to find the desired probability. We calculated the z-score as 1,25 for the 
 previous example. By using this value in the z-table we can find the probability of 
 getting a score of 205 or less. The z score tells you how many standard deviations 
 from the mean your score is. In this example, your score is 1,25 standard deviations
 above the mean. (1.2+0.05=1.25)
Normal Dist

We divide the z-score into two parts as 1,2 and 0,05 (1,2+0,05=1,25). We use the 
value of 1,2 on the left side of the table, and use the value of 0,05 on the top of 
the table. So we reach the probability of 0,8944 at the intersection point. That value
means, % 89,44 of the students receive a score of 205 or less, where the test has a mean (μ) 
of 180 and a standard deviation (σ) of 20. Because the total area under the normal curve is 
equal to 1, we can say also that the probability of getting a score of greater than 205 is % 10,56.

"""


#%%

# Interview Questions About Statistics

#%% 
INTERVAL -- RATIO??? NOTLARDA YUKARDA NEREYE KOYACAĞIZ

#%% TERM
"""
Statistics
A discipline that allows researchers to evaluate conclusions derived from sample data.

Nominal Scale
A type of measurement scale. Values assigned to variables represent a descriptive category, 
but have no inherent numerical value with respect to magnitude.

Ordinal Scale
A type of measurement scale. Each value has a unique meaning, and it has an ordered 
relationship to every other value on the scale.

Interval Scale
A type of measurement scale. A type of measurement scale that is characterized by equal 
intervals between scale units.

Ratio Scale
A type of measurement scale. It is characterized by equal intervals between scale units and 
a minimum scale value of zero.

Variable
Any characteristic observed in a study.

Data
Characteristics or information, usually numerical, that are collected through observation.

Skewness
Distortion or asymmetry in a symmetrical bell curve, or normal distribution, in a set of data.

Gaps in Graphs
Areas of a graphic display where there are no observations.

Outlier
A data point that diverges greatly from the overall pattern of data.

Frequency Table
A listing of possible values for a variable, together with the number of observations
 for each value.

Pie Chart
A circle having a "slice of the pie" for each category.


Reklamsız içerik için üyeliğinizi yükseltin
Yılda yalnızca $35,99
Bar Chart
A chart that presents categorical data with rectangular bars with heights proportional 
to the values that they represent.

Histogram
A graph of vertical bars representing the frequency distribution of a set of data.

Population
The total group about whom you want to make conclusions.

Sample
A subset of the population for whom you actually have data.

Parameter
A measurable characteristic of a or a population, such as a mean or a standard deviation .

Statistic
A numerical measurement describing some characteristic of a sample

Mean
It is equal to the sum of the values in the dataset divided by the number of values.

Median
It is the middle score for a dataset that has been sorted from small to large.

Mode
It is the most frequent score in a dataset.

Range
It is difference between the biggest and smallest random variable.

Standard Deviation
It is a statistic that measures the dispersion of a dataset relative to its mean and 
is calculated as the square root of the variance.


Variance
It is a measurement of the spread between numbers in a data set.

Interquartile Range (IQR)
It is a measure of variability, based on dividing a data set into quartiles.

Correlation
It is a statistical technique that determines how one variable changes with another variable.

Covariance
It is a measure of the strength of the correlation between two or more sets of random variates.

Probability
It is the branch of mathematics concerning numerical descriptions of how likely an event 
is to occur or how likely it is that a proposition is true.

Permutation
It is an arrangement of all or part of a set of objects, with regard to the order of the arrangement.

Combination
It is a selection of all or part of a set of objects, without regard to the order 
in which objects are selected.

Intersection
It is the set of elements that belong to two or more sets.

Union
It is the set that contains all of the elements that are in at least one of the two sets.

Complement
It is the subset of outcomes in the sample space that are not in the event.

Conditional Probability
The probability that event A occurs, given that event B has occurred

Random Variable
It is the set of possible numerical values in a random experiment.

Probability Distribution
It is a table or an equation that links each outcome of a statistical experiment with 
its probability of occurrence.

Binomial Distribution
A probability distribution for independent events for which there are only two possible 
outcomes such as a coin flip.

Sampling Distribution
It can be thought of as a relative frequency distribution with a very large number of samples.

Null Hypothesis (H0)
It is a hypothesis tested in significance testing. It is typically the hypothesis that 
a parameter is zero or that a difference between parameters is zero.

Alternative Hypothesis (Ha)
It is the hypothesis used in hypothesis testing that is contrary to the null hypothesis.

Significance Level
It is the highest value of a probability value for which the null hypothesis is rejected.
"""












    
