#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:09:13 2019

@author: ep9k
"""

#template of how to combine columns (pandas DataFrames)
#if column1 is empty, use value from column2. 
#if column2 is empty, use value from column3, and so on
#using combine_first function from pandas library


import pandas

df = pandas.read_csv('/Users/ep9k/Desktop/NewCSV.csv')

print(df)

df.mapping = df.col1.combine_first(df.col2)

print()
print(df)

df.mapping = df.col1.combine_first(df.col3)

print()
print(df)

#df.to_csv('/Users/ep9k/Desktop/New2CSV.csv')




