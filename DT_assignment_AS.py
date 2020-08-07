# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 17:29:21 2020

@author: aditya sandala
"""
#%%
#Topic: Decision tree using Wine Data Set
#
#%%

#libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

#dataset - understand it first : target class based on other parameters
#https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html
from sklearn.datasets import load_wine
wine = load_wine()
wine
wine.data

# feature matrix
X = wine.data
X

# target vector
y = wine.target
y

# class labels
labels = wine.feature_names
labels

#join X & y to dataframe
df = pd.DataFrame(wine.data)

#name the columns
df.columns = ['Alcohol', 'Malicacid', 'Ash', 'AlcalinityOfAsh', 'Magnesium',
'TotalPhenols', 'Flavanoids', 'NonflavanoidPhenols', 'Proanthocyanins',
'ColorIntensity', 'Hue', 'OD280_OD315', 'Proline']
df
df['target'] = pd.Series(wine.target) #add class column as target
df

#%%% what to do in this assignment
##in this case example Alcohol, Magnesium, Proline are used as IV to predict two
# target class, you required to select 3 different sets of variables and then
# predict the class
#you will have use different variables, create test data accordingly for
# prediction
#%%%

#select class 0 & 1 from target column
df.shape
df.target.value_counts()
data = df[df.target != 2]
data.target.value_counts()

#use only 3 columns for constructing a model
data3 = data[['Malicacid', 'Flavanoids', 'Hue', 'target']]
data3.head()
data3.describe()

#%%plots
#barplot
data3.target.value_counts().plot.bar()
plt.show();

#histogram
data3.Malicacid.plot.hist()
plt.show();

#density
data3.Malicacid.plot.density()
plt.show();

#correlation plot
corr = data3.corr()
sns.heatmap(corr, annot=True)
plt.show();

#%%predict target
data3.sample()
newdata = pd.DataFrame({'Malicacid':[1.5,2.1], 'Flavanoids':[2.6,2.9], 'Hue':[0.88,1.12]})
newdata

#X & y
data3.head()
X = data3[['Malicacid', 'Flavanoids', 'Hue']].values
X
y = data3['target'].values
y
data3.columns

#train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
X_train.shape, X_test.shape

#%%decision tree model
from sklearn import tree
clsModel = tree.DecisionTreeClassifier() #model with parameter
clsModel.fit(X_train, y_train)

#predict
y_pred1 = clsModel.predict(X_test)
len(y_pred1)

#%%%performance
from sklearn import metrics
metrics.accuracy_score(y_test, y_pred1) #accuracy
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred1)
print(confusion_matrix)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred1))

#predict on unknown target
newdata
y_pred1B = clsModel.predict(newdata)
y_pred1B
y_pred1C = clsModel.predict_proba(newdata)
y_pred1C
pd.concat([newdata, pd.Series(y_pred1B)], axis=1)

#first predicted as 1, 2nd rows as 0
#visualise the tree
from sklearn import tree
tree.plot_tree(decision_tree=clsModel, node_ids=True, filled=True )
fig = plt.figure(figsize=(10,8))
_ = tree.plot_tree(clsModel, feature_names= ['Malicacid', 'Flavanoids', 'Hue'],
class_names=['0','1'], filled=True) #see plot
