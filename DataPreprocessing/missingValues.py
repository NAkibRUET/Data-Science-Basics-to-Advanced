import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('class-grades.csv',error_bad_lines=False)
print('Tutorial Column: ',df['Tutorial'].isnull().sum())
print('Prefix Column: ',df['Prefix'].isnull().sum())
print('Assignment Column: ',df['Assignment'].isnull().sum())
print('Midterm Column: ',df['Midterm'].isnull().sum())
print('TakeHome Column: ',df['TakeHome'].isnull().sum())
print('Final Column: ',df['Final'].isnull().sum())

missing_value = ['na','-','Nan']
df = pd.read_csv('class-grades.csv', na_values=missing_value,error_bad_lines=False)

print('2.Tutorial Column: ',df['Tutorial'].isnull().sum())
print('2.Prefix Column: ',df['Prefix'].isnull().sum())
print('2.Assignment Column: ',df['Assignment'].isnull().sum())
print('2.Midterm Column: ',df['Midterm'].isnull().sum())
print('2.TakeHome Column: ',df['TakeHome'].isnull().sum())
print('2.Final Column: ',df['Final'].isnull().sum())

df['Tutorial'].fillna(df['Tutorial'].median(),inplace = True)

print('Assignment:\n',df['Assignment'].mean())
print(df['Assignment'].median())

#Here only one value is under 30 and even close to 30, so we are considering it as outlier
count = 0
for row in df['Assignment']:
    if row < 30.0:
        df.loc[count,'Assignment'] = df['Assignment'].mean()
    count+=1


# Another way of removing ourlier

#The quantile of a value is the fraction of observations or population less than or equal to the value.
#The quantile of the median is 0.5, by definition. People often are interested in the 0.25 quantile 
# (also known as the 25 percentile, percentiles are just quantiles multiplied by 100) and the 0.75, 
# these are known as quartiles, and the difference between them in the interquartile range. 
# You also hear about deciles, the 0.1, 0.2 and so on up to 0.9 quantiles.
# lower_bound = .1
# upper_bound = 0.9
# res = df['Assignment'].quantile([lower_bound, upper_bound])

print(df[df['Assignment']<30].__len__())
#plt.hist(df['Assignment'])

#Replacing NaN values with mean value or median value.
print('Midterm:\n',df['Midterm'].mean())
print(df['Midterm'].median())
#print(df[pd.to_numeric(df['Midterm'],errors='coerce').fillna(0).astype(np.int64)<30.0]) #this is the way if data type is string
df['Midterm'].fillna(df['Midterm'].median(),inplace = True)
print(df[df['Midterm'].isnull()].__len__())
plt.hist(df['Midterm'])
#print(df['Midterm'])
print('TakeHome:\n',df['TakeHome'].mean())
print(df['TakeHome'].median())
print(df[df['TakeHome'].isnull()].__len__())
df['TakeHome'].fillna(df['TakeHome'].median(),inplace = True)
print(df[df['TakeHome'].isnull()].__len__())
#plt.hist(df['TakeHome'].dropna())
print('FInal:\n',df['Final'].mean())
print(df['Final'].median())
print(df[df['Final'].isnull()].__len__())
df['Final'].fillna(df['Final'].median(),inplace = True)

df.to_csv('corrected_values.csv')
#plt.hist(df['Final'].dropna())