# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:40:53 2020

@author: aditya sandala
"""

#%%
# Clustering AssignmenT
# 
# Problem Statement:
# Mtcars contains data description of 32 cars eg. mpg, wt, hp
# Cluster the cars into groups so that they described in that manner
#
# Objective:
# Perform Kmeans Clustering for 2 clusters
#
# Research Qs
# Find mean of mpg, hp, wt of each representative value of 2 clusters
#
# Tasks:
# Ensure that data is numeric
# Scale the data
# Perform Kmeans with 2 clusters
# Find the cluster groups
# Calculate the group means of each cluster (mpg, wt, hp)
#
#%%

# standard libraries
import pandas as pd
import matplotlib.pyplot as plt

# importing mtcars data
from pydataset import data
mtcars = data('mtcars')
data = mtcars.copy()
data

# scaling the data - checking for missing values
data.dtypes
data.isnull().any()
data.isnull().sum().sum()
data1 = data.dropna(axis = 0, thresh = 1, subset = None, inplace = False)
data1
data2 = data1[['mpg','wt']]
data2
data3 = data1[['mpg','hp']]
data3

# visualize - clustering by mpg vs. weight
plt.scatter(data.mpg, data.wt)
plt.xlabel('Mileage')
plt.ylabel('Vehicle Weight')
plt.show();

from sklearn.cluster import KMeans
Kmean2 = KMeans(n_clusters=2)
Kmean2.fit(data2)
centers2 = Kmean2.cluster_centers_
centers2
Kmean2.labels_

plt.scatter(data2.mpg, data2.wt, s=30, c = Kmean2.labels_)
plt.scatter(centers2[:,0], centers2[:,1], s=100, marker='*', color =['red'])
plt.xlabel('Mileage')
plt.ylabel('Vehicle Weight')
plt.show();

pd.options.display.max_columns =None
data2.groupby([Kmean2.labels_]).mean()

# visualize - clustering by mpg vs. horsepower
plt.scatter(data.mpg, data.hp)
plt.xlabel('Mileage')
plt.ylabel('Vehicle Horsepower')
plt.show();

from sklearn.cluster import KMeans
Kmean3 = KMeans(n_clusters=2)
Kmean3.fit(data3)
centers3 = Kmean3.cluster_centers_
centers3
Kmean3.labels_

plt.scatter(data3.mpg, data3.hp, s=30, c = Kmean3.labels_)
plt.scatter(centers3[:,0], centers3[:,1], s=100, marker='*', color =['red'])
plt.xlabel('Mileage')
plt.ylabel('Vehicle Horsepower')
plt.show();

pd.options.display.max_columns =None
data3.groupby([Kmean3.labels_]).mean()
