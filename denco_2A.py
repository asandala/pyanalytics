# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:53:45 2020

@author: aditya sandala
"""

# Code discussed in class

import pandas as pd
import numpy as np

data2d = pd.read_csv('denco.csv')
data2d.head()

#Who are the most loyal Customers -
grouped_single=data2d.custname.value_counts('')
grouped_single.sort_values(ascending=False).head(5)
    
#Which customers contribute the most to their revenue -
grouped_single=data2d.groupby('custname').agg({'revenue':sum})
grouped_single=data2d.groupby(['custname', 'region']).agg({'revenue':sum})
grouped_single

grouped_single.sort_values('revenue',ascending=False)

#What part numbers bring in to significant portion of revenue
grouped_single=data2d.groupby('partnum').agg({'revenue':sum})
grouped_single.sort_values('revenue',ascending=False)

#What parts have the highest profit margin 
grouped_single=data2d.groupby('partnum').agg({'margin':sum})
grouped_single.sort_values('margin',ascending=False)