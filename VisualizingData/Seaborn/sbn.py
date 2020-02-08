import seaborn as sbn 
import matplotlib.pyplot as plt

titanic = sbn.load_dataset('titanic')

print(titanic)

print('\nPrinting Top 5 Data\n',titanic.head())
print('\nPrinting Top 10 Data\n',titanic.head(10))

print('\nPrinting Bottom 5 Data\n',titanic.tail())
print('\nPrinting Bottom 10 Data\n',titanic.tail(10))


print('\nPrinting Data Where fare greater than 400\n',titanic[titanic['fare']>400])

#Different kinds of plotting (use any one of them in a single page)
sbn.jointplot(x='fare', y='age',data=titanic)
sbn.distplot(titanic['fare'], kde=False, color="red", bins=20)
sbn.boxplot(x='class', y='survived',data=titanic)
sbn.swarmplot(x='sex', y='age',data=titanic)
sbn.countplot(x='class',data=titanic)

#Heatmap of correlated data. The value more closer to 1 the more correlated. 
sbn.heatmap(titanic.corr())
plt.title("Correlation") #Plt is from Matplotlib.pyplot

g = sbn.FacetGrid(titanic, col="sex")
g.map(plt.hist,'age')

p = titanic['adult_male']==True
r = titanic['sex']=='female'
q = titanic['survived']==1
print(titanic[p & q].__len__())
print(titanic[r & q].__len__())

print(titanic[r]['age'].mean())