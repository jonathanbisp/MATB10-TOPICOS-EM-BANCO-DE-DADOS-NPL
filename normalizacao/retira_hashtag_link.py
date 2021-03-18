import pandas as pd
import re


df = pd.read_csv('tweet_text_norm.csv', sep=',', encoding='utf8',header=None)

#print(df.rows)


df.replace({r'#': ''}, regex=True, inplace=True)
df.replace({r'https\S+': ''}, regex=True, inplace=True)

df.to_csv('tweet_text_norm_sem_hashtag_link.csv', index=False, encoding='utf8', header=False, line_terminator='\n')

df.to_html('teste.html', index=False, encoding='utf8', header=False)
for i, row in df.iterrows():
    print('- ', i+1, row[0])

