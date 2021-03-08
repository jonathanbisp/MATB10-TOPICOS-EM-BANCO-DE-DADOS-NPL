# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:40:17 2021

@author: JJSS
"""

import pandas as pd

df = pd.read_csv('tweet.csv', sep=',', encoding='utf8')

df = df.text.str.replace('\n',' ')

df.to_csv('tweet_text.csv', index=False, encoding='utf8', header=False, line_terminator='\n')
