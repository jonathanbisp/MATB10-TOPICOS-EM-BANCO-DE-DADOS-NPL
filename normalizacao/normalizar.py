import pandas as pd


df = pd.read_csv('tweet_text.csv', sep=',', encoding='utf8')

#print(df.rows)

df.replace({' qdo ': ' quando '}, regex=True, inplace=True)
df.replace({' qto ': ' quanto '}, regex=True, inplace=True)
df.replace({' Vcs ': ' Vocês '}, regex=True, inplace=True)
df.replace({' Pq ': ' Por que '}, regex=True, inplace=True)
df.replace({' pq ': ' porque '}, regex=True, inplace=True)
df.replace({' smp ': ' sempre '}, regex=True, inplace=True)

df.to_csv('tweet_text_norm.csv', index=False, encoding='utf8', header=False, line_terminator='\n')


for i, row in df.iterrows():
    print('- ', i, row[0])

