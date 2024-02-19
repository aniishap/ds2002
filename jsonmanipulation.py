#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:51:04 2024

@author: Anisha
"""

# question 1 
import pandas as pd 
import json
with open('/Users/Anisha/Downloads/coll bb_SortByConf.json') as f:
    data = json.load(f)


# question 2 
df = pd.DataFrame(data)


# question 3 

print(df.head(100))

# question 4
df_teams = pd.json_normalize(df['teams'])
print(df_teams)

# a
teams_count = len(df_teams)
print(teams_count)


# b
va_teams = df_teams[df_teams['state'] == 'VA']
va_teams_count = len(va_teams)
print(va_teams_count)

# c
mascot_counts = df_teams['name'].value_counts()
mascots_grouped = mascot_counts[mascot_counts > 1]
print(mascots_grouped)