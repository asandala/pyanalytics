# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 16:49:45 2020

@author: aditya sandala
"""

#%%
# Case Details: Linear Regression
#
# Problem Statement
# It is a dataset containing the impact of three advertising medias (youtube, facebook and newspaper) on sales. The first three columns are the advertising budget in thousands of dollars along with the fourth column as sales. #The advertising experiment has been repeated 200 times. Hence, it has 200 rows.
#
# Objectives
# Perform Multiple Linear Regression
#
# Research Qs
# Is sales related to other variables - youtube, facebook, newspaper
# Does the model exist ?
#
# Tasks
# ●	Name the dataframe : marketing
# ●	Perform Linear regression  model that can be used to predict sales by establishing a statistically significant linear relationship with other variable
# ●	#also explain the model output, draw boxplot, density and histogram to understand the data. predict sales for any unknown value of combination of other variables
# ●	R2, Adjt R2, RMSE 	
#
# Data Description
# Marketing Data - A data frame containing the impact of three advertising medias (youtube, facebook and newspaper) on sales. Data are the advertising budget in thousands of dollars along with the sales. The advertising experiment has been repeated 200 times.
#
#%%
# Linear Regression -1 Marketing Data - Sales - YT, FB, print

#libraries
import pandas as pd
import seaborn as sns

url ='https://raw.githubusercontent.com/DUanalytics/datasets/master/R/marketing.csv'
marketing = pd.read_csv(url)
marketing.head()

#describe data
marketing.describe
marketing.shape
marketing.info()

#null values check
marketing.isnull().sum()  

#visualise few plots to check correlation
sns.scatterplot(data=marketing, x='sales', y='youtube')
sns.scatterplot(data=marketing, x='sales', y='facebook')
sns.scatterplot(data=marketing, x='sales', y='newspaper')

#split data into train and test
marketing.head()
X = marketing[['youtube', 'facebook', 'newspaper']].values
X
y = marketing['sales'].values
y

# 1. Using SKLearn Method
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
X_train.shape, X_test.shape
y_train.shape, y_test.shape

#build the model
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(X,y)
model.score(X,y)  #R2
model.intercept_ # constant
model.coef_ #b0, b1

#predict on test values
y_pred = model.predict(X_test)
y_pred

#find metrics - R2, Adjt R2, RMSE, MAPE etc
from sklearn.metrics import mean_squared_error, r2_score
model.score(X,y)  #R2
mean_squared_error(y_test, y_pred)  #RMSE
r2_score(y_test, y_pred) 

#predict on new value
newdata = pd.DataFrame({'youtube':[50,60,70], 'facebook':[20, 30, 40], 'newspaper':[70,75,80]})
newdata
y_pred2 = model.predict(newdata)
y_pred2

# 2. Using StatsModel Method
import statsmodels.api as sm  
X = sm.add_constant(X)  
X
model2 = sm.OLS(y,X)
model2
results = model2.fit()
results
results.summary()
results.rsquared  #coeff of determination
results.rsquared_adj 
results.params  #bo, b1, b2

results.fittedvalues
results.predict(X)

# end