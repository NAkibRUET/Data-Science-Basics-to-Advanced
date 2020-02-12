import numpy as np
import pandas as pd

df = pd.read_csv('class-grades.csv',error_bad_lines=False)
print('Tutorial Column: ',df['Tutorial'].isnull().sum())
print('Prefix Column: ',df['Prefix'].isnull().sum())
print('Assignment Column: ',df['Assignment'].isnull().sum())
print('Midterm Column: ',df['Midterm'].isnull().sum())
print('TakeHome Column: ',df['TakeHome'].isnull().sum())
print('Final Column: ',df['Final'].isnull().sum())

missing_value = ['na','-']
df = pd.read_csv('class-grades.csv', na_values=missing_value,error_bad_lines=False)
print('2.Tutorial Column: ',df['Tutorial'].isnull().sum())
print('2.Prefix Column: ',df['Prefix'].isnull().sum())
print('2.Assignment Column: ',df['Assignment'].isnull().sum())
print('2.Midterm Column: ',df['Midterm'].isnull().sum())
print('2.TakeHome Column: ',df['TakeHome'].isnull().sum())
print('2.Final Column: ',df['Final'].isnull().sum())
