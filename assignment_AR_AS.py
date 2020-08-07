# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 18:58:47 2020

@author: aditya sandala
"""

#%%
# Association Rule Analysis Assignment
#
# Problem Statement
# The dataset in a list form contains preference of purchases of Fruits. Use Association Rule Analysis to find Frequent Items Sets and items with interesting rules
#
# Objectives
# Perform Association Rule
#
# Research Qs
# Does Support, Confidence, Lift show the interestingness of the purchase
#
# Tasks
# Convert the data from List to Transaction format
# Find Frequent Items Sets. Which are the top 2 items sets 
# Use association rules to find rules with different metrics.
# Support (.3), Confidence(.6) and Lift(1.5)
# Also perform filter of rules with combination support, confidence, lift
# What marketing strategy will you apply on the interesting rules you have found	
#
#%%

import pandas as pd
#pip install mlxtend
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

pd.set_option('display.max_columns',None)

dataset = [['Apple', 'Beer', 'Rice', 'Chicken'],  ['Apple', 'Beer', 'Rice'], ['Apple', 'Beer'],  ['Apple', 'Bananas'], ['Milk', 'Beer', 'Rice', 'Chicken'], ['Milk', 'Beer', 'Rice'],  ['Milk', 'Beer'], ['Apple', 'Bananas']]

dataset
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
te_ary
df = pd.DataFrame(te_ary, columns=te.columns_)
df
te.columns_
df.shape

#%%% #frequent itemsets 

support_threshold = 0.01

frequent_itemsets = apriori(df, min_support= support_threshold, use_colnames = True)
frequent_itemsets
frequent_itemsets.head()

#%%%%  - Support Rules

supportRules1 = association_rules(frequent_itemsets, metric="support", min_threshold = .3)
print(supportRules1)

print(supportRules1[['antecedents', 'consequents', 'support','confidence','lift']])

#%%%% Lift  : generally > 1 for strong associations

lift1 = association_rules(frequent_itemsets, metric="lift", min_threshold=1.5)
print(lift1)
lift1
print(lift1[['antecedents', 'consequents', 'support', 'lift','confidence']])

#twin condition : lift> 2;  confidence > .5, support > .2
lift1[(lift1.confidence > .5)  & (lift1.support > .2)]
      
#%%%% Confidence

confidence1 = association_rules(frequent_itemsets, metric="confidence", min_threshold=.6)
print(confidence1)
print(confidence1[['antecedents', 'consequents', 'support','confidence']])
