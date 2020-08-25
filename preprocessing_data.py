#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:27:58 2020

@author: gustavo
"""
import numpy as np
import pandas as pd

df = pd.read_csv (r'dataset/survey.csv')

# Getting rid of useless columns
df = df.drop('Timestamp', 1)
df = df.drop('state', 1)
df = df.drop('comments', 1)

# Check genders.
print(df.Gender.unique())

# Transforming genders to uppercase and trimming
df.Gender =  df.Gender.str.upper().str.strip()

# Check genders again.
print(df.Gender.unique())

# Reducing genders into 3 categories (F/M/O)
female_identifiers = ['FEMALE', 'CIS FEMALE', 'F', 'WOMAN', 'FEMAKE', 
                      'CIS-FEMALE/FEMME', 'FEMALE (CIS)', 'FEMAIL']
male_identifiers = ['M', 'MALE', 'MAILE', 'CIS MALE', 'MAL', 'MALE (CIS)', 
                    'MAKE', 'MAN', 'MSLE', 'MAIL', 'MALR', 'CIS MAN', 
                    'OSTENSIBLY MALE, UNSURE WHAT THAT REALLY MEANS']

female_filter = df.Gender.isin(female_identifiers)
male_filter = df.Gender.isin(male_identifiers)

df.loc[female_filter, 'Gender'] = 'F'
df.loc[male_filter, 'Gender'] = 'M'

other_filter = ~df.Gender.isin(['M', 'F'])
df.loc[other_filter, 'Gender'] = 'O'

df.to_csv(r'outputs/cleaned_survey.csv')
