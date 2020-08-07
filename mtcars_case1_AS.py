# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 23:35:49 2020

@author: aditya sandala
"""

#%%

#Case Study on mtcars dataset in Python	download data

#Download data
import statsmodels.api as sm

#https://vincentarelbundock.github.io/Rdatasets/datasets.html
dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
dataset_mtcars.data.head()
mtcars = dataset_mtcars.data

#structure
type(mtcars)

#summary
mtcars.describe()

#print first / last few rows
mtcars.head()
mtcars.tail()

#print number of rows
rows = mtcars.index
len(rows)

#number of columns
column = mtcars.columns
len(column)

#print names of columns
print(mtcars.columns)

#Filter Rows
#cars with cyl=8
cyl8 = mtcars['cyl']==8
print(mtcars[cyl8])

#cars with mpg <= 27
mpg27 = mtcars['mpg']<=27
print(mtcars[mpg27])

#rows match auto tx
autotx = mtcars['am']==1
print(mtcars[autotx])

#First Row
print(mtcars.iloc[0,:])

#last Row
len(mtcars)
print(mtcars.iloc[31,:])

# 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
print(mtcars.iloc[0,0])
print(mtcars.iloc[0,5])
print(mtcars.iloc[0,6])

print(mtcars.iloc[3,0])
print(mtcars.iloc[3,5])
print(mtcars.iloc[3,6])

print(mtcars.iloc[6,0])
print(mtcars.iloc[6,5])
print(mtcars.iloc[6,6])

print(mtcars.iloc[24,0])
print(mtcars.iloc[24,5])
print(mtcars.iloc[24,6])

# first 5 rows and 5th, 6th, 7th columns of data frame
print(mtcars.iloc[4, 4:7])

#rows between 25 and 3rd last
len(mtcars)
print(mtcars.iloc[24:30,:])

#alternative rows and alternative column
print(mtcars.iloc[1::2, 1::2])

#find row with Mazda RX4 Wag and columns cyl, am
print(mtcars.loc['Mazda RX4', ['cyl', 'am']])

#find row betwee Merc 280 and Volvo 142E Mazda RX4 Wag and columns cyl, am
mtcars.loc['Merc 280':'Volvo 142E', ['cyl', 'am']]

# mpg > 23 or wt < 2
mpg23 = mtcars['mpg']>=23
wt2 = mtcars['wt']<2
mpg23orwt2 = mpg23 | wt2
print(mtcars[mpg23orwt2])

#find unique rows of cyl, am, gear
mtcars[['cyl', 'am', 'gear']].drop_duplicates()

#create new columns: first make a copy of mtcars to mtcars2
len(mtcars)
mtcars2 = mtcars.assign(newcolumn = ['1', '1','1','1','1','1', \
                                     '1','1','1','1','1','1','1', \
                                         '1','1','1','1','1','1','1', \
                                             '1','1','1','1','1','1','1', \
                                                 '1','1','1','1','1', ])
print(mtcars2)

#keeps other cols and divide displacement by 61
mtcars2['disp'] = mtcars2['disp'] /61
print(mtcars2)

# multiple mpg * 1.5 and save as original column
mtcars2['mpg'] = mtcars2['mpg'] *1.5
print(mtcars2)
