import numpy as np 
import pandas as pd
from sklearn import preprocessing 

arr = {'Name':['Tom', 'nick', 'krish', 'jack', 'Nakib', 'Abul'],
        'Age':[20, 21, 19, 18, 24, 45],
        'Address':['Dhaka', 'Rajshahi', 'Khulna', 'Dhaka', 'Rajshai', 'Jhenidah'],
        'Weight':[40, 45, 60, 56, 51, 60],
        'Postal':[1205, 6000, 9201, 1205, 6000, 7300]
    }

data = pd.DataFrame(arr)

data.to_csv('newData.csv')

print(data)
def encoder(d, col):
    le = preprocessing.LabelEncoder()
    le.fit(d[col])
    transformed = le.transform(d[col])
    d[col]=transformed
    return d

data = encoder(data, "Name")
data = encoder(data, "Address")
print(data)