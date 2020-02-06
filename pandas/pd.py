import numpy as np
import pandas as pd
from numpy.random import randn

x = pd.DataFrame(randn(5,4),index="A B C D E".split(), columns="i ii iii iv".split())
print('\n',x)

df = pd.DataFrame({'Name':['Sam', 'Andrea', 'Alex', 'Robin', 'Kia'], 'Weight':[45, 88, 56, 15, 71], 'Age':[14, 25, 55, 8, 21]},index="1 2 3 4 5".split()) 
print('\n',df)
print('\nPrinting the row named 1\n',df.loc['1'])
print('\nPrinting the row named 1 and column name Age\n',df.loc['1'][['Name','Age']])
print('\nPrinting the 2nd row\n',df.iloc[1])
print('\n',df['Name'])

df['Weight+Age'] = df['Weight'] + df['Age']
print('\n',df)
print('\n',df[['Name','Weight+Age']])

df.drop('Weight+Age',axis=1, inplace=True) 
print('\nDroping the column named Weight+Age\n',df)

df.drop('5',axis=0, inplace=True) 
print('\nDroping the row named 5\n',df)

print('\nNumber of People with weight greater than 50\n',(df.Weight>50).sum())
p = df['Weight']>50
q = df['Age']<50
print('\nPeople with weight greater than 50 and age less than 50\n',df[p & q])

print('\nChanging Index to Name\n',df)


outside = ['G1','G1','G2','G2']
inside = ['1','2','3','4']
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df.set_index(hier_index,inplace=True) #df.set_index('Name',inplace=True) #in this way we can set any column to it's index


print('\nChanging Index\n',df)

print('\nShowing rows of G1\n',df.loc['G1'])

df.index.names = ['Group', 'Number']
print('\nNaming the index columns\n',df)


print('\nRow of Number 1\n',df.xs('1',level='Number'))

print('\nRows of Group G1\n',df.xs('G1',level='Group'))