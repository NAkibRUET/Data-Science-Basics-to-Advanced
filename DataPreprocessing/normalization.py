import numpy as np 
from sklearn import preprocessing 

data = np.array([[35,45,60],[50,80,60],[1,2,3]])
data_normal_l1 = preprocessing.normalize(data, norm="l1")
data_normal_l2 = preprocessing.normalize(data, norm="l2")

print(data_normal_l1)
print(data_normal_l2)